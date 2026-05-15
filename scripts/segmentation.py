"""Gait-cycle segmentation: detect heel-strike events and emit per-cycle slices.

Heel-strike (HS) is the canonical cycle boundary in clinical gait analysis.
This module detects HS from vertical heel-marker trajectory using a
velocity zero-crossing heuristic, which works equally on OpenCap-derived
marker data and synthetic data with the same column convention.

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


def detect_heel_strikes(heel_y: np.ndarray, fs: float,
                        min_cycle_s: float = 0.6,
                        max_cycle_s: float = 2.0) -> np.ndarray:
    """Return sample indices of heel-strike events.

    Method: detect the falling-edge of the vertical heel marker through
    a smoothed-threshold crossing. The heel marker rises into mid-swing
    (peak lift) and falls back to the ground at heel-strike; we find the
    instant the (smoothed) trajectory crosses below a small threshold
    derived from the trial's own amplitude. This is more robust than
    local-minimum search in the noise-flat stance region.

    `min_cycle_s` enforces a refractory period between successive
    detections; the default 0.6s is conservative for adult walking
    (cycle durations of 0.8–1.4s are typical).
    """
    if len(heel_y) < int(fs * min_cycle_s):
        return np.array([], dtype=int)
    # Smooth lightly with a moving average to suppress noise without
    # destroying the falling-edge timing.
    window = max(3, int(fs * 0.04))
    if window > len(heel_y):
        smooth = heel_y.copy()
    else:
        kernel = np.ones(window) / window
        smooth = np.convolve(heel_y, kernel, mode="same")
    amp = float(np.max(smooth) - np.min(smooth))
    if amp < 1e-3:
        return np.array([], dtype=int)
    # Threshold: low fraction of the trial's amplitude above the min.
    thresh = float(np.min(smooth)) + 0.05 * amp
    above = smooth > thresh
    # Falling-edge: above → not above (i.e. ground contact)
    edges = np.where(above[:-1] & ~above[1:])[0]
    if len(edges) == 0:
        return edges
    # Refractory filtering
    refrac = int(min_cycle_s * fs)
    keep = [edges[0]]
    for e in edges[1:]:
        if e - keep[-1] >= refrac:
            keep.append(e)
    keep = np.array(keep, dtype=int)
    # Drop cycles whose duration exceeds max_cycle_s by splitting
    if len(keep) > 1:
        durs = np.diff(keep) / fs
        out = [keep[0]]
        for k, d in zip(keep[1:], durs):
            if d <= max_cycle_s:
                out.append(k)
        keep = np.array(out, dtype=int)
    return keep


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
                quality_flag="ok" if 0.5 < duration < 1.8 else "out_of_range",
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
