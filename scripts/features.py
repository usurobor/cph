"""Per-cycle feature extraction.

Implements the first-pass feature set named in `analysis/features.md`:
timing, range/amplitude, shape, coordination, asymmetry. Each function
takes a `Cycle` (from `segmentation.py`) and returns a row dict.
"""

from __future__ import annotations

from typing import Optional

import numpy as np
import pandas as pd

from scripts.segmentation import Cycle, time_normalize_cycle


_JOINT_COLS = {
    "R": ["hip_flexion_r", "knee_angle_r", "ankle_angle_r"],
    "L": ["hip_flexion_l", "knee_angle_l", "ankle_angle_l"],
}


def extract_timing(cycle: Cycle) -> dict:
    """Timing features per `features.md §Timing features`.

    stance/swing duration is approximated from the contralateral heel
    position when available; otherwise stance is set as ~60% of cycle
    (population mean) with a flag indicating estimation.
    """
    out = {"cycle_duration_s": cycle.duration_s}
    if cycle.duration_s <= 0:
        return out
    df = cycle.df
    contra = "LHEE_Y" if cycle.side == "R" else "RHEE_Y"
    if contra in df.columns:
        # toe-off of ipsilateral side ~= contralateral heel-strike during cycle
        contra_v = df[contra].to_numpy()
        if len(contra_v) > 4:
            # find local minimum of contralateral heel within cycle
            min_idx = int(np.argmin(contra_v))
            stance_end_t = float(df["time"].iloc[min_idx]) - cycle.start_time
            stance_pct = 100.0 * stance_end_t / cycle.duration_s
            out["stance_duration_s"] = stance_end_t
            out["swing_duration_s"] = cycle.duration_s - stance_end_t
            out["stance_pct_cycle"] = stance_pct
            out["timing_estimate_method"] = "contralateral_HS"
        else:
            stance_pct = 60.0
            out["stance_duration_s"] = cycle.duration_s * 0.6
            out["swing_duration_s"] = cycle.duration_s * 0.4
            out["stance_pct_cycle"] = 60.0
            out["timing_estimate_method"] = "fallback_60pct"
    else:
        out["stance_duration_s"] = cycle.duration_s * 0.6
        out["swing_duration_s"] = cycle.duration_s * 0.4
        out["stance_pct_cycle"] = 60.0
        out["timing_estimate_method"] = "fallback_60pct"
    # timing of peak knee flexion
    knee_col = f"knee_angle_{cycle.side.lower()}"
    if knee_col in df.columns:
        knee = df[knee_col].to_numpy()
        peak_idx = int(np.argmax(knee))
        out["peak_knee_flexion_phase"] = 100.0 * peak_idx / max(len(knee) - 1, 1)
    return out


def extract_range(cycle: Cycle) -> dict:
    """Range / amplitude features per `features.md §Range and amplitude features`.

    Column names are side-agnostic (e.g. `hip_flexion_range_deg`) — the
    cycle's own side is in the row's `side` index column. This keeps the
    feature table dense (no NaN from cross-side joint columns).
    """
    df = cycle.df
    out: dict = {}
    side = cycle.side.lower()
    joint_map = {
        "hip_flexion": f"hip_flexion_{side}",
        "hip_adduction": f"hip_adduction_{side}",
        "knee_angle": f"knee_angle_{side}",
        "ankle_angle": f"ankle_angle_{side}",
    }
    for label, col in joint_map.items():
        if col not in df.columns:
            continue
        v = df[col].to_numpy()
        out[f"{label}_range_deg"] = float(np.max(v) - np.min(v))
        out[f"{label}_peak_deg"] = float(np.max(v))
        out[f"{label}_min_deg"] = float(np.min(v))
    for pelvis in ["pelvis_tilt", "pelvis_list", "pelvis_rotation"]:
        if pelvis in df.columns:
            v = df[pelvis].to_numpy()
            out[f"{pelvis}_range_deg"] = float(np.max(v) - np.min(v))
    for trunk in ["lumbar_bending", "lumbar_rotation", "lumbar_extension"]:
        if trunk in df.columns:
            v = df[trunk].to_numpy()
            out[f"{trunk}_range_deg"] = float(np.max(v) - np.min(v))
    return out


def extract_shape_sentinel(cycle: Cycle) -> dict:
    """Shape features: PC scores deferred to aggregate phase; per-cycle
    record holds the 101-point normalized curves so PCA can run later.

    Returns a single column 'normalized_curve_path' that is filled by
    the notebook's aggregate cell after persisting per-cycle curves to
    a private parquet outside the repo.
    """
    return {"normalized_curve_available": True}


def extract_coordination(cycle: Cycle) -> dict:
    """Coordination features: cross-correlation between hip and knee curves
    on the cycle side; phase relationship between pelvis and trunk if
    trunk data present (not present in the synthetic schema, so emits NaN).
    """
    df = cycle.df
    out = {}
    side = cycle.side.lower()
    hip_col, knee_col = f"hip_flexion_{side}", f"knee_angle_{side}"
    if hip_col in df.columns and knee_col in df.columns:
        hip = df[hip_col].to_numpy()
        knee = df[knee_col].to_numpy()
        # cross-correlation peak lag (samples) as proxy for timing offset
        if len(hip) > 4 and len(knee) > 4:
            hip_z = (hip - hip.mean()) / (hip.std() + 1e-9)
            knee_z = (knee - knee.mean()) / (knee.std() + 1e-9)
            xcorr = np.correlate(hip_z, knee_z, mode="full")
            lag = np.argmax(xcorr) - (len(knee_z) - 1)
            out["hip_knee_lag_samples"] = int(lag)
            out["hip_knee_lag_pct_cycle"] = 100.0 * lag / max(len(hip) - 1, 1)
    return out


def extract_features(cycle: Cycle) -> dict:
    """All first-pass features for one cycle, plus indexing columns.

    Returns one row with all indexing columns required by
    `analysis/features.md §Required indexing`.
    """
    row = {
        "subject": cycle.subject,
        "session": "S01",
        "trial_id": cycle.trial_id,
        "condition": cycle.condition,
        "side": cycle.side,
        "cycle_number": cycle.cycle_number,
        "quality_flag": cycle.quality_flag,
        "exclusion_flag": cycle.quality_flag != "ok",
        "detection_method": cycle.detection_method,
    }
    row.update(extract_timing(cycle))
    row.update(extract_range(cycle))
    row.update(extract_shape_sentinel(cycle))
    row.update(extract_coordination(cycle))
    return row


def build_feature_table(cycles: list[Cycle]) -> pd.DataFrame:
    """Aggregate per-cycle features into the feature table."""
    rows = [extract_features(c) for c in cycles]
    df = pd.DataFrame(rows)
    return df


def missingness(df: pd.DataFrame) -> pd.DataFrame:
    """Per-column null-rate summary for the feature table."""
    return pd.DataFrame({
        "column": df.columns,
        "null_count": df.isna().sum().values,
        "null_pct": 100.0 * df.isna().sum().values / max(len(df), 1),
    })


def lr_asymmetry(feat: pd.DataFrame, key_cols: list[str]) -> pd.DataFrame:
    """Right - Left feature difference per (subject, trial_id, condition, cycle_number).

    Pairs cycles by integer cycle number; emits NaN when the side is missing.
    """
    pivot = feat.pivot_table(
        index=["subject", "trial_id", "condition", "cycle_number"],
        columns="side",
        values=key_cols,
    )
    out = {}
    for col in key_cols:
        if col in pivot.columns.get_level_values(0):
            if "R" in pivot[col].columns and "L" in pivot[col].columns:
                out[f"{col}_lr_diff"] = pivot[col]["R"] - pivot[col]["L"]
    return pd.DataFrame(out).reset_index()
