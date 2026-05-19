"""Gait-cycle segmentation: detect heel-strike events and emit per-cycle slices.

Heel-strike (HS) is the canonical cycle boundary in clinical gait analysis.
This module detects HS from vertical heel-marker trajectory using
robust-percentile normalization plus stance-region depth/length gating.
The detector works on both OpenCap-derived synthetic marker data (heel
range ~[0,100], zero baseline) and real OpenCap Lab Validation Mocap
calcaneus markers (heel range ~[50,330] mm, ~25 mm R/L baseline offset,
short trial cropping ≈1.3–1.5 s ≈ 1 cycle).

A gait cycle = HS_n to HS_{n+1} of the SAME side.
A stride includes both legs; a cycle here is one side.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np
import pandas as pd
from scipy.signal import find_peaks


@dataclass
class Cycle:
    subject: str
    trial_id: str
    condition: str
    side: str            # "R" or "L"
    cycle_number: int    # 1-indexed within trial+side
    start_idx: int
    end_idx: int
    start_time: float
    end_time: float
    duration_s: float
    df: pd.DataFrame     # slice of source df, [start_idx:end_idx+1]
    quality_flag: str = "ok"
    # Cycle endpoints come from either ipsilateral marker detection
    # ("measured", produced by `detect_heel_strikes`) or contralateral
    # inference from the opposite-side HS plus a half-stride offset
    # ("inferred_contralateral", produced by
    # `scripts.segmentation_contralateral.segment_trial_with_contralateral_l`).
    # Default preserves pre-cph#28 behavior for callers that construct
    # Cycle directly.
    detection_method: str = "measured"


def detect_heel_strikes(heel_y: np.ndarray, fs: float,
                        min_cycle_s: float = 0.6,
                        max_cycle_s: float = 2.0,
                        stance_thr: float = 0.30,
                        deep_thr: float = 0.10,
                        min_stance_s: float = 0.15) -> np.ndarray:
    """Return sample indices of heel-strike events.

    Method: stance-region detection on the vertical heel-marker trace,
    with robust per-trial percentile normalization. Each contiguous run
    of `yn < stance_thr` (where `yn = (smoothed_heel - q05) / (q95 - q05)`)
    that lasts ≥`min_stance_s` AND reaches a deepest value `< deep_thr`
    is one stance phase; the HS event for that phase is the first sample
    inside the deep-stance plateau (`yn < deep_thr`) — i.e. the onset of
    ground contact, matching the conventional marker-based HS definition.

    This replaces an earlier falling-edge / fixed-threshold detector
    that worked on the smoke-test synthetic schema (heel ~[0,100] mm,
    zero R/L baseline offset) but failed on real OpenCap Lab Validation
    Mocap calcaneus markers (heel ~[50,330] mm, ~25 mm R/L baseline
    offset, short trial cropping ≈1.3–1.5 s ≈ 1 cycle). Robust-percentile
    normalization removes baseline + amplitude bias; stance-region depth
    + length gating rejects boundary noise and partial-stance edges.

    `min_cycle_s` enforces a refractory period between successive
    detections; defaults are conservative for adult walking
    (cycle 0.8–1.4 s, stance ≥0.4 s, swing ≈0.4 s).
    """
    v = np.asarray(heel_y, dtype=float)
    N = len(v)
    if N < int(fs * min_cycle_s):
        return np.array([], dtype=int)
    finite = np.isfinite(v)
    if int(finite.sum()) < int(fs * min_cycle_s):
        return np.array([], dtype=int)
    if not finite.all():
        v = v.copy()
        v[~finite] = np.interp(np.flatnonzero(~finite),
                                np.flatnonzero(finite), v[finite])

    window = max(3, int(fs * 0.04))
    if window > N:
        smooth = v.copy()
    else:
        kernel = np.ones(window) / window
        smooth = np.convolve(v, kernel, mode="same")

    q05 = float(np.percentile(smooth, 5))
    q95 = float(np.percentile(smooth, 95))
    amp = q95 - q05
    if amp < 1e-3:
        return np.array([], dtype=int)
    yn = (smooth - q05) / amp

    min_stance_n = max(3, int(min_stance_s * fs))
    below = yn < stance_thr
    idx = np.flatnonzero(below)
    if len(idx) == 0:
        return np.array([], dtype=int)
    breaks = np.flatnonzero(np.diff(idx) > 1)
    starts = np.concatenate([[idx[0]], idx[breaks + 1]])
    ends = np.concatenate([idx[breaks], [idx[-1]]])

    candidates: list[int] = []
    for s, e in zip(starts, ends):
        if (e - s + 1) < min_stance_n:
            continue
        seg = yn[s:e + 1]
        if float(np.min(seg)) > deep_thr:
            continue
        deep_idx = np.where(seg < deep_thr)[0]
        if len(deep_idx) > 0:
            hs_local = int(deep_idx[0])
        else:
            hs_local = int(np.argmin(seg))
        candidates.append(int(s + hs_local))

    if not candidates:
        return np.array([], dtype=int)

    candidates.sort()
    refrac = int(min_cycle_s * fs)
    refrac_filtered: list[int] = [candidates[0]]
    for h in candidates[1:]:
        if h - refrac_filtered[-1] >= refrac:
            refrac_filtered.append(h)

    out: list[int] = [refrac_filtered[0]]
    for h in refrac_filtered[1:]:
        if (h - out[-1]) / fs <= max_cycle_s:
            out.append(h)
    return np.array(out, dtype=int)


def segment_trial(df: pd.DataFrame,
                  subject: str,
                  trial_id: str,
                  condition: str,
                  fs: float,
                  side_marker_col: dict[str, str] | None = None) -> list[Cycle]:
    """Segment a trial dataframe into per-side gait cycles.

    `side_marker_col` maps side → column name to use for HS detection.
    Default uses RHEE_Y / LHEE_Y if present in df.
    """
    if side_marker_col is None:
        side_marker_col = {"R": "RHEE_Y", "L": "LHEE_Y"}
    cycles: list[Cycle] = []
    for side, col in side_marker_col.items():
        if col not in df.columns:
            continue
        heel = df[col].to_numpy()
        hs = detect_heel_strikes(heel, fs)
        for i in range(len(hs) - 1):
            start, end = int(hs[i]), int(hs[i + 1])
            t0, t1 = float(df["time"].iloc[start]), float(df["time"].iloc[end])
            duration = t1 - t0
            sub_df = df.iloc[start:end + 1].copy().reset_index(drop=True)
            cycles.append(Cycle(
                subject=subject, trial_id=trial_id, condition=condition,
                side=side, cycle_number=i + 1,
                start_idx=start, end_idx=end,
                start_time=t0, end_time=t1, duration_s=duration,
                df=sub_df,
                quality_flag=("short" if duration <= 0.5
                              else "long" if duration >= 1.8
                              else "ok"),
            ))
    return cycles


def summary_table(cycles: list[Cycle]) -> pd.DataFrame:
    """Per-trial × side summary: cycles extracted, mean duration, failure count."""
    if not cycles:
        return pd.DataFrame(columns=["subject", "trial_id", "condition", "side",
                                      "n_cycles", "mean_duration_s", "n_quality_fail"])
    rows = []
    by_key: dict[tuple, list[Cycle]] = {}
    for c in cycles:
        by_key.setdefault((c.subject, c.trial_id, c.condition, c.side), []).append(c)
    for (subj, trial, cond, side), cs in by_key.items():
        n = len(cs)
        mean_dur = float(np.mean([c.duration_s for c in cs])) if n else float("nan")
        n_fail = sum(1 for c in cs if c.quality_flag != "ok")
        rows.append({"subject": subj, "trial_id": trial, "condition": cond,
                     "side": side, "n_cycles": n, "mean_duration_s": mean_dur,
                     "n_quality_fail": n_fail})
    return pd.DataFrame(rows)


def time_normalize_cycle(cycle: Cycle,
                          columns: list[str],
                          n_samples: int = 101) -> pd.DataFrame:
    """Resample a cycle to `n_samples` points (0–100% of cycle).

    Linear interpolation per column.
    """
    src_t = cycle.df["time"].to_numpy()
    if len(src_t) < 2:
        return pd.DataFrame()
    norm_t = np.linspace(src_t[0], src_t[-1], n_samples)
    out = {"phase_pct": np.linspace(0, 100, n_samples)}
    for col in columns:
        if col not in cycle.df.columns:
            out[col] = np.full(n_samples, np.nan)
            continue
        out[col] = np.interp(norm_t, src_t, cycle.df[col].to_numpy())
    return pd.DataFrame(out)
