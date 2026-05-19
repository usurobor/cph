"""Contralateral-anchored L-cycle inference (cph#28).

The OpenCap Lab Validation archive crops each trial to ~1.3–1.5 s
(≈1 stride) windowed against the R stride; 47/60 L-side trials end
mid-swing and 12/60 start mid-swing, leaving only 1 L cycle measurable
by ipsilateral heel-strike detection (`scripts.segmentation.detect_heel_strikes`).
This module recovers L cycles by inference, anchored against the
detected R HS events plus a half-stride offset.

Approach (matched-duration, partial-clip allowed):

1. Run the R-side detector (`detect_heel_strikes` on `RHEE_Y`) to obtain
   R HS events and estimate cycle duration T (median of R HS spacing,
   or a population-mean fallback when only one R HS is present).
2. For each R cycle [r_i, r_{i+1}], predict the matched L cycle
   start at l0 = r_i + T/2 and the matched L cycle end at l1 = l0 + T
   (i.e., one full stride starting from the inferred L HS, offset half
   a stride from R cycle i). When `LHEE_Y` is available, snap l0 to
   the local minimum of `LHEE_Y` within ±150 ms.
3. If l0 falls inside the trial sample window, emit an L cycle slice
   from l0 to min(N-1, l1). When l1 extends past trial end (the common
   case on this archive — most trials are ~1.4 s, T ≈ 1.0 s, so 0.5T
   of the matched L cycle is clipped), the cycle is flagged with
   `detection_method="inferred_contralateral_partial"` and the slice
   covers the available portion of the L stride. Coverage is reported
   in the per-trial metadata. A minimum coverage threshold (default
   0.80) gates emission — slices shorter than that are dropped.

Honesty / claim-scope. Inferred L HS times are not direct measurement,
and partial-clip cycles do not cover the full 0–100% gait phase. The
contralateral assumption ("L stride runs in counter-phase to R", offset
= 0.5 of R cycle duration) is true in healthy steady-state walking but
is itself the kind of property a bilateral asymmetry analysis intends
to *test*. The partial-clip approach gives the L joint trace coverage
from approximately phase 0% through phase ~85% of the L cycle (HS through
mid-swing); the missing terminal swing biases range features slightly
downward and makes timing / coordination features at the cycle boundary
unreliable. Features derived from inferred L cycles therefore carry an
inference layer that R-vs-R features do not. The field report names
this explicitly so downstream consumers (R3 bilateral pairing, R4
falsification re-evaluation) can bound their claims accordingly.

R-side detector is not touched. `detect_heel_strikes` (the R2 detector)
remains the sole producer of R HS; this module only consumes its output.
The L cycles emitted here carry `detection_method="inferred_contralateral"`
(full coverage) or `detection_method="inferred_contralateral_partial"`
(clipped at trial end) so consumers can filter / distinguish them from
measured cycles.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.segmentation import Cycle, detect_heel_strikes, segment_trial  # noqa: E402


# Population-mean R cycle duration on this archive, lifted from
# `reports/field-report-01-existing-data-zeroth-pilot.md` §"Per-side
# cycle yield" (60 R cycles, mean 1.06 s, range 0.84–1.37 s). Used
# only when a trial yields a single R HS and no per-trial estimate
# of cycle duration is available.
DEFAULT_CYCLE_S = 1.06

# Half-stride contralateral offset. In healthy steady-state walking the
# L stride runs in counter-phase to the R stride; offset = 0.5 of the
# R cycle period. The fraction is exposed for sensitivity checks.
DEFAULT_OFFSET_FRACTION = 0.5

# Refinement search window (seconds either side of the predicted L HS)
# inside which we snap to the local LHEE_Y minimum when the L heel
# marker is available. Disabled by default (0.0): empirical refinement
# on this archive shifted predicted L HS toward noisy local minima
# that reduced matched-duration cycle coverage below the emission
# threshold. The half-stride offset is the model; data-driven
# refinement adds variance without improving fit (calibration against
# subject8/walkingTS1 shows the raw half-stride prediction at sample
# 87 matches the measured L HS at sample 84 within 3 samples / 30 ms,
# while refinement snapped to 102 — a window-boundary artifact).
# Callers can re-enable refinement by passing a non-zero value.
DEFAULT_SEARCH_WINDOW_S = 0.0

# Minimum fraction of the matched L cycle that must lie inside the
# trial sample window for the L cycle to be emitted. 0.80 keeps the
# slice long enough to capture stance + most of swing (the gait phases
# where the joint-range maxima live) while excluding trials that would
# only contribute a sub-stance fragment. Empirically (cph#28 α run),
# the archive yields 57/60 trials with coverage ≥ 0.80 (mean coverage
# 0.86, min 0.79, max 0.94) — the three trials below threshold are
# the shortest in the archive.
DEFAULT_MIN_COVERAGE = 0.80


@dataclass
class ContralateralMetadata:
    """Per-trial diagnostic for the contralateral L inference."""

    trial: str
    n_r_hs: int
    cycle_estimate_samples: int
    cycle_estimate_source: str  # "R_HS_spacing" | "population_fallback_1.06s"
    n_l_hs_inferred: int
    n_l_cycles_emitted: int
    n_l_cycles_full: int
    n_l_cycles_partial: int
    coverage_of_first_l_cycle: float  # 0..1, fraction of T inside trial
    offset_fraction: float
    note: str = ""


def estimate_cycle_samples(
    r_hs: np.ndarray,
    fs: float,
    fallback_cycle_s: float = DEFAULT_CYCLE_S,
) -> tuple[int, str]:
    """Estimate cycle duration in samples from R HS spacing, or fall back.

    Median of consecutive R HS differences when ≥2 HS exist; the
    population-mean fallback (1.06 s) otherwise. Returns (samples, source).
    """
    if len(r_hs) >= 2:
        return int(np.median(np.diff(r_hs))), "R_HS_spacing"
    return int(round(fallback_cycle_s * fs)), f"population_fallback_{fallback_cycle_s}s"


def infer_contralateral_heel_strikes(
    r_hs: np.ndarray,
    n_samples: int,
    fs: float,
    l_heel_y: np.ndarray | None = None,
    offset_fraction: float = DEFAULT_OFFSET_FRACTION,
    fallback_cycle_s: float = DEFAULT_CYCLE_S,
    search_window_s: float = DEFAULT_SEARCH_WINDOW_S,
) -> tuple[np.ndarray, int]:
    """Infer L heel-strike sample indices from R HS by contralateral offset.

    For each R HS at sample r, predicts L HS at r + (offset_fraction *
    cycle_samples) — i.e., the L stride that runs in counter-phase to
    the R stride starting at r. Predictions outside [0, n_samples-1]
    are dropped. When `l_heel_y` is provided, each prediction is
    optionally refined to the local minimum of `LHEE_Y` within
    ±search_window_s (weak validity check that the predicted HS lands
    near a local low point of the L heel trace).

    Returns (l_hs, cycle_samples). The two-direction (±) form used in
    an earlier draft is collapsed to a single (+) direction since the
    matched-duration L cycle defined by `segment_trial_with_contralateral_l`
    only consumes the *forward* L HS (the L HS that starts the L cycle
    paired with one R cycle); the (−) direction predictions are the
    same L HS shifted by one cycle.
    """
    if len(r_hs) == 0:
        return np.array([], dtype=int), 0

    cycle_samples, _src = estimate_cycle_samples(r_hs, fs, fallback_cycle_s)
    offset_samples = int(round(offset_fraction * cycle_samples))
    if offset_samples <= 0:
        return np.array([], dtype=int), cycle_samples

    raw: list[int] = []
    for r in r_hs:
        l_pred = int(r) + offset_samples
        if 0 <= l_pred < n_samples:
            raw.append(l_pred)

    if not raw:
        return np.array([], dtype=int), cycle_samples

    predicted = sorted(set(raw))

    if (l_heel_y is not None and len(l_heel_y) == n_samples
            and search_window_s > 0):
        search_n = max(1, int(round(search_window_s * fs)))
        refined: list[int] = []
        for p in predicted:
            lo = max(0, p - search_n)
            hi = min(n_samples, p + search_n + 1)
            window = l_heel_y[lo:hi]
            finite_mask = np.isfinite(window)
            if finite_mask.any():
                local_min = int(lo + int(np.argmin(np.where(finite_mask, window, np.inf))))
                refined.append(local_min)
            else:
                refined.append(p)
        predicted = sorted(set(refined))

    return np.array(predicted, dtype=int), cycle_samples


def segment_trial_with_contralateral_l(
    df: pd.DataFrame,
    subject: str,
    trial_id: str,
    condition: str,
    fs: float,
    offset_fraction: float = DEFAULT_OFFSET_FRACTION,
    fallback_cycle_s: float = DEFAULT_CYCLE_S,
    search_window_s: float = DEFAULT_SEARCH_WINDOW_S,
    min_coverage: float = DEFAULT_MIN_COVERAGE,
) -> tuple[list[Cycle], ContralateralMetadata]:
    """Segment a trial with R via the standard detector, L via contralateral inference.

    R-side cycles come from `scripts.segmentation.segment_trial` exactly as
    they did before cph#28 (detection_method="measured"). L-side cycles are
    constructed using the matched-duration partial-clip rule: for each R
    cycle starting at r_i with duration T, the matched L cycle starts at
    l_0 = r_i + T/2 and runs for T samples, clipped to the trial sample
    window. When the clipped slice covers at least `min_coverage` of T,
    the L cycle is emitted with `detection_method="inferred_contralateral"`
    (full coverage, l_0 + T ≤ N-1) or
    `detection_method="inferred_contralateral_partial"` (clipped, slice
    covers ≥ min_coverage × T but < T).
    """
    r_cycles = segment_trial(
        df, subject, trial_id, condition, fs,
        side_marker_col={"R": "RHEE_Y"},
    )
    # segment_trial returns cycles with the default detection_method="measured"
    # already; no further annotation needed for R.

    trial_label = f"{subject}/{trial_id}"
    N = len(df)

    if "RHEE_Y" not in df.columns:
        meta = ContralateralMetadata(
            trial=trial_label,
            n_r_hs=0,
            cycle_estimate_samples=0,
            cycle_estimate_source="no_R_marker",
            n_l_hs_inferred=0,
            n_l_cycles_emitted=0,
            n_l_cycles_full=0,
            n_l_cycles_partial=0,
            coverage_of_first_l_cycle=float("nan"),
            offset_fraction=offset_fraction,
            note="RHEE_Y missing — no L inference attempted",
        )
        return r_cycles, meta

    r_heel = df["RHEE_Y"].to_numpy()
    r_hs = detect_heel_strikes(r_heel, fs)
    cycle_samples, cycle_src = estimate_cycle_samples(r_hs, fs, fallback_cycle_s)

    l_heel = df["LHEE_Y"].to_numpy() if "LHEE_Y" in df.columns else None
    l_hs, _ = infer_contralateral_heel_strikes(
        r_hs=r_hs,
        n_samples=N,
        fs=fs,
        l_heel_y=l_heel,
        offset_fraction=offset_fraction,
        fallback_cycle_s=fallback_cycle_s,
        search_window_s=search_window_s,
    )

    l_cycles: list[Cycle] = []
    n_full = 0
    n_partial = 0
    first_coverage = float("nan")
    cycle_number = 0
    for l0 in l_hs:
        l0 = int(l0)
        if l0 >= N - 1:
            continue
        l1_target = l0 + cycle_samples
        l1_actual = min(N - 1, l1_target)
        available = l1_actual - l0
        coverage = available / cycle_samples if cycle_samples > 0 else 0.0
        if cycle_number == 0:
            first_coverage = float(coverage)
        if coverage < min_coverage:
            continue
        cycle_number += 1
        is_full = l1_actual == l1_target
        if is_full:
            n_full += 1
            method = "inferred_contralateral"
        else:
            n_partial += 1
            method = "inferred_contralateral_partial"
        t0 = float(df["time"].iloc[l0])
        t1 = float(df["time"].iloc[l1_actual])
        duration = t1 - t0
        sub_df = df.iloc[l0:l1_actual + 1].copy().reset_index(drop=True)
        # quality_flag follows the same duration tri-value as the R-side
        # cycles; "ok" keeps the cycle in feature extraction (consumers
        # filter on detection_method when they need to distinguish
        # inferred from measured cycles).
        if duration <= 0.5:
            quality = "short"
        elif duration >= 1.8:
            quality = "long"
        else:
            quality = "ok"
        l_cycles.append(Cycle(
            subject=subject, trial_id=trial_id, condition=condition,
            side="L", cycle_number=cycle_number,
            start_idx=l0, end_idx=l1_actual,
            start_time=t0, end_time=t1, duration_s=duration,
            df=sub_df,
            quality_flag=quality,
            detection_method=method,
        ))

    meta = ContralateralMetadata(
        trial=trial_label,
        n_r_hs=int(len(r_hs)),
        cycle_estimate_samples=int(cycle_samples),
        cycle_estimate_source=cycle_src,
        n_l_hs_inferred=int(len(l_hs)),
        n_l_cycles_emitted=int(len(l_cycles)),
        n_l_cycles_full=int(n_full),
        n_l_cycles_partial=int(n_partial),
        coverage_of_first_l_cycle=float(first_coverage),
        offset_fraction=offset_fraction,
    )
    return r_cycles + l_cycles, meta


def calibrate_against_measured_l(
    ik_path: Path,
    offset_fraction: float = DEFAULT_OFFSET_FRACTION,
    fallback_cycle_s: float = DEFAULT_CYCLE_S,
    search_window_s: float = DEFAULT_SEARCH_WINDOW_S,
) -> dict:
    """Compare contralateral-inferred L HS against measured L HS for one trial.

    The lone trial with a measured L cycle on this archive is
    `subject9/walkingTS3` (per `reports/field-report-01-existing-data-zeroth-pilot.md`
    §"Per-side cycle yield"). This routine loads that trial, runs the
    contralateral inference, and reports the per-HS offset between
    inferred and measured L HS. If the inference is consistent with the
    measured L cycle, the per-HS offset should be small relative to one
    stance phase (≈0.5 s).
    """
    from scripts.io_opencap import load_paired_trial

    trial = load_paired_trial(ik_path)
    df, fs = trial.df, trial.sample_rate_hz
    r_hs = detect_heel_strikes(df["RHEE_Y"].to_numpy(), fs)
    measured_l_hs = detect_heel_strikes(df["LHEE_Y"].to_numpy(), fs)
    l_hs_inferred, cycle_samples = infer_contralateral_heel_strikes(
        r_hs=r_hs, n_samples=len(df), fs=fs,
        l_heel_y=df["LHEE_Y"].to_numpy(),
        offset_fraction=offset_fraction,
        fallback_cycle_s=fallback_cycle_s,
        search_window_s=search_window_s,
    )
    out = {
        "trial": f"{trial.subject}/{trial.trial_id}",
        "fs_hz": float(fs),
        "n_samples": int(len(df)),
        "r_hs_samples": r_hs.tolist(),
        "measured_l_hs_samples": measured_l_hs.tolist(),
        "inferred_l_hs_samples": l_hs_inferred.tolist(),
        "cycle_estimate_samples": int(cycle_samples),
        "cycle_estimate_s": cycle_samples / fs,
    }
    if len(measured_l_hs) and len(l_hs_inferred):
        # Per-measured-L closest inferred-L sample offset
        diffs = []
        for m in measured_l_hs:
            d = int(min(abs(int(m) - int(p)) for p in l_hs_inferred))
            diffs.append(d)
        out["per_measured_offset_samples"] = diffs
        out["max_offset_samples"] = int(max(diffs))
        out["max_offset_s"] = max(diffs) / fs
    return out


def main(argv: list[str] | None = None) -> int:
    """Standalone diagnostic: report per-trial L inference yield.

    Iterates Mocap walking IK trials, runs the contralateral wrapper, and
    prints a per-trial table plus an archive-level summary. Optionally
    runs the calibration against subject9/walkingTS3 first.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--calibrate", action="store_true",
                        help="run calibration against the one measured L cycle")
    parser.add_argument("--csv-out", type=Path, default=None,
                        help="optional path to write per-trial diagnostics CSV (outside repo)")
    args = parser.parse_args(argv)

    from scripts.io_opencap import (
        get_opencap_extracted_root, discover_walking_ik, load_paired_trial,
    )

    root = get_opencap_extracted_root()
    if not root.exists():
        print(f"ERROR: data root not found at {root}", file=sys.stderr)
        return 2

    ik_paths = discover_walking_ik(root, ik_source="Mocap")
    if not ik_paths:
        print(f"ERROR: no walking IK paths under {root}", file=sys.stderr)
        return 2

    if args.calibrate:
        # The lone trial yielding a measured L cycle on this archive is
        # subject8/walkingTS1 (N=197 samples, the longest trial; R HS at
        # [19, 155], L HS at [0, 84] from `detect_heel_strikes`). The
        # L HS at sample 0 is a boundary artifact (trial starts in L
        # stance, depth/length gate fires at sample 0). The measured L
        # HS at sample 84 is the real anchor for offset-fraction
        # calibration: phase = (84 − 19) / (155 − 19) = 0.478, which
        # matches the half-stride contralateral assumption (0.500)
        # within one stance-bandwidth and validates DEFAULT_OFFSET_FRACTION.
        cal_path = None
        for p in ik_paths:
            if "subject8" in str(p) and "walkingTS1" in p.stem:
                cal_path = p
                break
        if cal_path is None:
            print("ERROR: subject8/walkingTS1 not found for calibration", file=sys.stderr)
        else:
            print("=== calibration: subject8/walkingTS1 (the one measured L cycle) ===")
            cal = calibrate_against_measured_l(cal_path)
            for k, v in cal.items():
                print(f"  {k}: {v}")
            print()

    rows = []
    for p in ik_paths:
        trial = load_paired_trial(p)
        cycles, meta = segment_trial_with_contralateral_l(
            trial.df, trial.subject, trial.trial_id, trial.condition,
            trial.sample_rate_hz,
        )
        n_r = sum(1 for c in cycles if c.side == "R")
        n_l = sum(1 for c in cycles if c.side == "L")
        rows.append({
            "trial": meta.trial,
            "n_r_cycles": n_r,
            "n_l_cycles": n_l,
            "n_l_full": meta.n_l_cycles_full,
            "n_l_partial": meta.n_l_cycles_partial,
            "first_l_coverage": meta.coverage_of_first_l_cycle,
            "n_r_hs": meta.n_r_hs,
            "cycle_est_samples": meta.cycle_estimate_samples,
        })
    df = pd.DataFrame(rows)
    n_r_total = int(df["n_r_cycles"].sum())
    n_l_total = int(df["n_l_cycles"].sum())
    n_trials_with_l = int((df["n_l_cycles"] > 0).sum())
    print("=== archive summary (contralateral L inference) ===")
    print(f"  trials: {len(df)}")
    print(f"  R cycles total: {n_r_total}")
    print(f"  L cycles total (inferred): {n_l_total}")
    print(f"  trials with ≥1 inferred L cycle: {n_trials_with_l} / {len(df)} "
          f"({100.0 * n_trials_with_l / max(len(df), 1):.1f}%)")
    print("\n=== per-trial table (first 20 rows) ===")
    print(df.head(20).to_string(index=False))

    if args.csv_out is not None:
        args.csv_out.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(args.csv_out, index=False)
        print(f"\nwrote {len(df)} rows to {args.csv_out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
