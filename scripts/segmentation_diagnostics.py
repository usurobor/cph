"""Heel-strike detector diagnostics for the OpenCap Lab Validation archive.

Produces per-trial × side numeric summaries: marker stats, robust amplitude,
detected HS event indices, cycle counts, and a "stance bookend" classification
that explains why some trials yield 0 cycles on one side.

The script is read-only against the data root; it writes diagnostic tables
to stdout (and optionally to a CSV outside the repo). It does not modify
the segmentation primitive.

Usage:
    GAIT_DATA_ROOT=/opt/gait-data python3 scripts/segmentation_diagnostics.py
    GAIT_DATA_ROOT=/opt/gait-data python3 scripts/segmentation_diagnostics.py \\
        --target subject11/walking4 subject9/walking1
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.io_opencap import (  # noqa: E402
    get_opencap_extracted_root,
    discover_walking_ik,
    load_paired_trial,
)
from scripts.segmentation import detect_heel_strikes  # noqa: E402


SIDE_COLS = {"R": "RHEE_Y", "L": "LHEE_Y"}


def _trial_label(ik_path: Path) -> str:
    # ik_path = .../subject<NN>/OpenSimData/Mocap/IK/<trial>.mot
    subject = ik_path.parents[3].name
    return f"{subject}/{ik_path.stem}"


def diagnose_trial(ik_path: Path) -> list[dict]:
    """One row per (side) describing the heel-marker stats and detector output."""
    trial = load_paired_trial(ik_path)
    df, fs = trial.df, trial.sample_rate_hz
    rows: list[dict] = []
    for side, col in SIDE_COLS.items():
        row = {
            "trial": _trial_label(ik_path),
            "side": side,
            "fs_hz": float(fs),
            "n_samples": int(len(df)),
            "duration_s": float(df["time"].iloc[-1] - df["time"].iloc[0])
            if "time" in df.columns and len(df) > 1 else float("nan"),
        }
        if col not in df.columns:
            row.update({"status": "marker_missing"})
            rows.append(row)
            continue
        v = df[col].to_numpy()
        finite = v[np.isfinite(v)]
        if len(finite) == 0:
            row.update({"status": "all_nan"})
            rows.append(row)
            continue
        row.update({
            "min_mm": float(np.min(finite)),
            "q05_mm": float(np.percentile(finite, 5)),
            "q50_mm": float(np.percentile(finite, 50)),
            "q95_mm": float(np.percentile(finite, 95)),
            "max_mm": float(np.max(finite)),
            "robust_amp_mm": float(np.percentile(finite, 95)
                                    - np.percentile(finite, 5)),
        })
        hs = detect_heel_strikes(v, fs)
        n_cycles = max(0, len(hs) - 1)
        cycle_durations = np.diff(hs) / fs if len(hs) > 1 else np.array([])
        row.update({
            "n_hs_events": int(len(hs)),
            "hs_indices": ",".join(str(int(h)) for h in hs),
            "n_cycles": int(n_cycles),
            "cycle_durations_s": ",".join(f"{d:.2f}" for d in cycle_durations),
            "first_val_normalized": _normalized_value(v, 0),
            "last_val_normalized": _normalized_value(v, len(v) - 1),
            "status": "ok",
        })
        rows.append(row)
    return rows


def _normalized_value(v: np.ndarray, idx: int) -> float:
    finite = v[np.isfinite(v)]
    if len(finite) < 2:
        return float("nan")
    q05 = float(np.percentile(finite, 5))
    q95 = float(np.percentile(finite, 95))
    if q95 - q05 < 1e-3:
        return float("nan")
    return float((v[idx] - q05) / (q95 - q05))


def _stance_bookend_class(row: dict) -> str:
    """Why does this side yield 0 cycles? Classification based on boundary normalised values."""
    if row.get("status") != "ok":
        return row.get("status", "unknown")
    if row["n_cycles"] >= 1:
        return "ok"
    first = row.get("first_val_normalized", float("nan"))
    last = row.get("last_val_normalized", float("nan"))
    if np.isnan(first) or np.isnan(last):
        return "no_amplitude"
    starts_in_stance = first < 0.30
    ends_in_stance = last < 0.30
    if starts_in_stance and ends_in_stance:
        # Both endpoints in stance but only 1 HS reported = stance regions failed
        # the depth/length gate.
        return "shallow_stance_endpoints"
    if not starts_in_stance and not ends_in_stance:
        return "trial_crops_only_swing"
    if starts_in_stance:
        return "trial_ends_mid_swing"
    return "trial_starts_mid_swing"


def summarize_archive(extracted_root: Path) -> tuple[pd.DataFrame, dict]:
    """Run diagnostics across all Mocap walking IK files."""
    ik_paths = discover_walking_ik(extracted_root, ik_source="Mocap")
    rows: list[dict] = []
    for p in ik_paths:
        rows.extend(diagnose_trial(p))
    df = pd.DataFrame(rows)
    df["zero_cycle_reason"] = df.apply(_stance_bookend_class, axis=1)
    summary = {
        "trials": int(len(ik_paths)),
        "trials_with_any_cycle": int(
            df.groupby("trial")["n_cycles"].max().gt(0).sum()
        ),
        "R_cycles_total": int(df.loc[df["side"] == "R", "n_cycles"].sum()),
        "L_cycles_total": int(df.loc[df["side"] == "L", "n_cycles"].sum()),
        "natural_trials_with_cycle": int(
            df[~df["trial"].str.contains("TS", case=False)]
            .groupby("trial")["n_cycles"].max().gt(0).sum()
        ),
        "trunk_sway_trials_with_cycle": int(
            df[df["trial"].str.contains("TS", case=False)]
            .groupby("trial")["n_cycles"].max().gt(0).sum()
        ),
    }
    return df, summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", nargs="*", default=None,
                        help="subject<NN>/<trial> labels to print in detail")
    parser.add_argument("--csv-out", type=Path, default=None,
                        help="write full per-trial-side diagnostics to this CSV")
    args = parser.parse_args(argv)

    root = get_opencap_extracted_root()
    if not root.exists():
        print(f"ERROR: data root not found at {root}", file=sys.stderr)
        return 2

    df, summary = summarize_archive(root)
    print("=== archive summary ===")
    for k, v in summary.items():
        print(f"  {k}: {v}")
    pct = 100.0 * summary["trials_with_any_cycle"] / max(summary["trials"], 1)
    print(f"  trials_with_cycle_pct: {pct:.1f}%")

    print("\n=== zero-cycle-reason distribution (side rows) ===")
    print(df["zero_cycle_reason"].value_counts().to_string())

    target_labels = args.target or ["subject11/walking4", "subject9/walking1"]
    print(f"\n=== target trial detail: {target_labels} ===")
    cols = ["trial", "side", "fs_hz", "n_samples", "duration_s",
            "robust_amp_mm", "n_hs_events", "hs_indices",
            "n_cycles", "cycle_durations_s",
            "first_val_normalized", "last_val_normalized",
            "zero_cycle_reason"]
    sub = df[df["trial"].isin(target_labels)]
    if len(sub):
        print(sub[cols].to_string(index=False))
    else:
        print("(no rows match)")

    if args.csv_out is not None:
        args.csv_out.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(args.csv_out, index=False)
        print(f"\nwrote {len(df)} rows to {args.csv_out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
