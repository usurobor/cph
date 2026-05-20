"""R3 bilateral extension — subject-paired L-vs-R lr-diff analysis (cph#30).

Sibling script to `analysis/r3_subject_aggregate_tests.py` (the cph#27 R-side
historical analysis, which is left untouched). This module runs the bilateral
extension against the post-cph#28 feature table (60 R measured + 57 L
inferred-partial cycles across 10 subjects × 2 conditions).

Pipeline (per cph#30 issue body §Approach):

1. Load the persisted feature table (default
   `$GAIT_DATA_ROOT/cph-features/features-zeroth-pilot.csv`, falling back to
   `/opt/gait-data/cph-features/features-zeroth-pilot.csv`).
2. Compute per-(subject, trial_id, condition, cycle_number) lr-diff rows via
   `scripts.features.lr_asymmetry` on the numeric feature columns.
3. Aggregate per (subject, condition) by median across cycles within cell.
4. Run paired Wilcoxon signed-rank tests on lr-diff vs 0 per condition
   (n = 10 subjects per condition per feature).
5. Compute rank-biserial r_rb effect size + 95% CI via percentile bootstrap
   (B=10,000; deterministic seed=20260520).
6. BH-FDR at q=0.05 across the feature × condition test set.
7. Cross-condition test: paired Wilcoxon on (lr-diff under trunk-sway −
   lr-diff under natural) per feature, n=10 subjects.

Honesty caveat (path (a)). All L cycles in the post-cph#28 feature table
are inferred via `scripts/segmentation_contralateral.py` and partial-clip
(coverage 0.80–0.94, mean 0.86). Bilateral lr-diff magnitudes are reported
as "consistent with" an asymmetric coordination signature, not as
"measurement of" asymmetric coordination. The inference layer (path (a))
is named in every paragraph of the field report that states a lr-diff
result.

Usage:
    python3 analysis/r3_bilateral_tests.py [path-to-features-csv]
    python3 analysis/r3_bilateral_tests.py --surrogate     # harness-validation only

This script does NOT write any aggregate / derived data to disk; outputs
are markdown to stdout, consistent with the cph#27 AC9 boundary. The field
report carries the tables inlined as markdown.

If the persisted CSV is not reachable, the script can be invoked with
`--surrogate` to run against a deterministic synthetic feature table
calibrated to the cph#27 published R-side medians plus cph#28's documented
L-side partial-clip characteristics — this is a harness-validation surface
*only*; β substitutes canonical values by re-running against the persisted
CSV before merge.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

# Method-pick constants — keep in sync with .cdr/unreleased/30/self-coherence.md §Method picks.
BOOTSTRAP_B = 10_000
BOOTSTRAP_SEED = 20260520  # cycle dispatch date; distinct from cph#27 seed.
SURROGATE_SEED = 30202605  # surrogate-feature-table seed (harness-validation only).
FDR_Q = 0.05

# Columns excluded from per-feature aggregation: indexing + non-numeric metadata.
NON_FEATURE_COLS = {
    "subject", "session", "trial_id", "condition", "side", "cycle_number",
    "quality_flag", "exclusion_flag",
    "timing_estimate_method", "normalized_curve_available",
    "detection_method",
}

# Hypothesis → features. H3 set is the bilateral focus; H1 / H2 are re-evaluated
# for any verdict shift relative to cph#27 R-side.
H1_FEATURES = [
    "hip_flexion_range_deg", "knee_angle_range_deg", "ankle_angle_range_deg",
    "hip_knee_lag_pct_cycle", "peak_knee_flexion_phase",
]
H2_FEATURES = [
    "lumbar_extension_range_deg", "lumbar_bending_range_deg", "lumbar_rotation_range_deg",
    "pelvis_tilt_range_deg", "pelvis_list_range_deg", "pelvis_rotation_range_deg",
    "hip_adduction_range_deg", "hip_adduction_peak_deg", "hip_adduction_min_deg",
]
H3_FOCUS_FEATURES = [
    "hip_flexion_range_deg", "knee_angle_range_deg", "ankle_angle_range_deg",
    "hip_adduction_range_deg",
    "hip_knee_lag_pct_cycle", "hip_knee_lag_samples",
]
LR_DIFF_ELIGIBLE = [
    # Joint range/peak/min features (side-bearing — emit lr_diff).
    "hip_flexion_range_deg", "hip_flexion_peak_deg", "hip_flexion_min_deg",
    "hip_adduction_range_deg", "hip_adduction_peak_deg", "hip_adduction_min_deg",
    "knee_angle_range_deg", "knee_angle_peak_deg", "knee_angle_min_deg",
    "ankle_angle_range_deg", "ankle_angle_peak_deg", "ankle_angle_min_deg",
    # Cycle-timing features — present on both sides via shared trial metadata.
    "cycle_duration_s", "stance_duration_s", "swing_duration_s", "stance_pct_cycle",
    "peak_knee_flexion_phase",
    # Coordination features — side-bearing.
    "hip_knee_lag_samples", "hip_knee_lag_pct_cycle",
]
# Trunk / pelvis features are *shared* (one trace per trial, not per side) — they
# enter `scripts.features.lr_asymmetry` only if both R and L cycles carry them
# at matching cycle_number, but the underlying signal is the same. They emit
# lr_diff columns but the diff is dominated by cycle-slice misalignment
# (R: full cycle; L: partial-clip 0.80–0.94). Reported but framed cautiously.
TRUNK_LR_DIFF_ELIGIBLE = [
    "pelvis_tilt_range_deg", "pelvis_list_range_deg", "pelvis_rotation_range_deg",
    "lumbar_bending_range_deg", "lumbar_rotation_range_deg", "lumbar_extension_range_deg",
]


def load_features(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def numeric_feature_cols(df: pd.DataFrame) -> list[str]:
    candidates = [c for c in df.columns if c not in NON_FEATURE_COLS]
    return [c for c in candidates if pd.api.types.is_numeric_dtype(df[c])]


def lr_asymmetry_local(feat: pd.DataFrame, key_cols: list[str]) -> pd.DataFrame:
    """Local copy of scripts.features.lr_asymmetry (avoids importing from
    scripts/, which is upstream source-of-truth code α does not modify).

    Pivots feat by side and emits R − L for each requested feature in
    `key_cols`. One row per (subject, trial_id, condition, cycle_number).
    """
    pivot = feat.pivot_table(
        index=["subject", "trial_id", "condition", "cycle_number"],
        columns="side",
        values=key_cols,
    )
    out = {}
    for col in key_cols:
        if col in pivot.columns.get_level_values(0):
            sub = pivot[col]
            if "R" in sub.columns and "L" in sub.columns:
                out[f"{col}_lr_diff"] = sub["R"] - sub["L"]
    return pd.DataFrame(out).reset_index()


def aggregate_lr_diff(lrd: pd.DataFrame, lr_features: list[str]) -> pd.DataFrame:
    """Median of lr-diff per (subject, condition) across cycles within cell."""
    grouped = lrd.groupby(["subject", "condition"], sort=True)[lr_features]
    return grouped.median()


def paired_test_vs_zero(values: np.ndarray) -> tuple[float, float, float, int, int]:
    """Wilcoxon signed-rank of `values` vs 0.

    Returns (W, p_two_sided, r_rb, n_pairs, n_nonzero).
    """
    v = np.asarray(values, dtype=float)
    v = v[~np.isnan(v)]
    nz = v[v != 0]
    n_pairs = int(len(v))
    n_nonzero = int(len(nz))
    if n_nonzero == 0 or n_pairs < 2:
        return float("nan"), 1.0, 0.0, n_pairs, 0
    res = stats.wilcoxon(v, zero_method="wilcox", alternative="two-sided")
    W = float(res.statistic)
    p = float(res.pvalue)
    ranks = stats.rankdata(np.abs(nz))
    W_pos = float(ranks[nz > 0].sum())
    W_neg = float(ranks[nz < 0].sum())
    denom = W_pos + W_neg
    r_rb = (W_pos - W_neg) / denom if denom > 0 else 0.0
    return W, p, r_rb, n_pairs, n_nonzero


def paired_test_two_arrays(a: np.ndarray, b: np.ndarray) -> tuple[float, float, float, int, int]:
    """Paired Wilcoxon on (a - b); used for the cross-condition shift test."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    mask = (~np.isnan(a)) & (~np.isnan(b))
    delta = a[mask] - b[mask]
    return paired_test_vs_zero(delta)


def bootstrap_rb_ci(values: np.ndarray, B: int = BOOTSTRAP_B, seed: int = BOOTSTRAP_SEED) -> tuple[float, float]:
    """Percentile bootstrap 95% CI for rank-biserial r_rb on `values vs 0`."""
    v = np.asarray(values, dtype=float)
    v = v[~np.isnan(v)]
    n = len(v)
    if n == 0:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    samples = np.empty(B, dtype=float)
    for b in range(B):
        idx = rng.integers(0, n, size=n)
        d = v[idx]
        nz = d[d != 0]
        if len(nz) == 0:
            samples[b] = 0.0
            continue
        ranks = stats.rankdata(np.abs(nz))
        W_pos = float(ranks[nz > 0].sum())
        W_neg = float(ranks[nz < 0].sum())
        denom = W_pos + W_neg
        samples[b] = (W_pos - W_neg) / denom if denom > 0 else 0.0
    return float(np.percentile(samples, 2.5)), float(np.percentile(samples, 97.5))


def bh_fdr(pvals: list[float], q: float = FDR_Q) -> tuple[list[float], list[bool]]:
    """Benjamini–Hochberg FDR adjustment. Returns (q-values, sig-at-q)."""
    p = np.asarray(pvals, dtype=float)
    n = len(p)
    if n == 0:
        return [], []
    order = np.argsort(p, kind="stable")
    ranked = p[order]
    adj_sorted = ranked * n / (np.arange(n) + 1)
    adj_sorted = np.minimum.accumulate(adj_sorted[::-1])[::-1]
    adj_sorted = np.clip(adj_sorted, 0.0, 1.0)
    adj = np.empty(n, dtype=float)
    adj[order] = adj_sorted
    sig = (adj < q).tolist()
    return adj.tolist(), sig


def df_to_markdown(df: pd.DataFrame, index: bool = True) -> str:
    """Minimal markdown-table renderer (avoids tabulate dependency)."""
    if index:
        if isinstance(df.index, pd.MultiIndex):
            index_names = [str(n) if n is not None else "" for n in df.index.names]
            rows_index = [tuple(map(str, idx)) for idx in df.index]
            header_cells = index_names + [str(c) for c in df.columns]
        else:
            index_names = [str(df.index.name) if df.index.name is not None else ""]
            rows_index = [(str(idx),) for idx in df.index]
            header_cells = index_names + [str(c) for c in df.columns]
        data_rows = []
        for ridx, row in zip(rows_index, df.itertuples(index=False, name=None)):
            data_rows.append(list(ridx) + [_md_cell(v) for v in row])
    else:
        header_cells = [str(c) for c in df.columns]
        data_rows = [[_md_cell(v) for v in row] for row in df.itertuples(index=False, name=None)]
    lines = ["| " + " | ".join(header_cells) + " |"]
    lines.append("| " + " | ".join(["---"] * len(header_cells)) + " |")
    for r in data_rows:
        lines.append("| " + " | ".join(r) + " |")
    return "\n".join(lines)


def _md_cell(v) -> str:
    if isinstance(v, float):
        if np.isnan(v):
            return "—"
        return f"{v:g}"
    return str(v)


def fmt(x: float, digits: int = 3) -> str:
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    if abs(x) >= 100:
        return f"{x:.1f}"
    return f"{x:.{digits}f}"


def fmt_p(p: float) -> str:
    if np.isnan(p):
        return "—"
    if p < 1e-3:
        return f"{p:.1e}"
    return f"{p:.3f}"


def hypothesis_for(feature_stem: str) -> str:
    """Return the hypothesis label for a non-lr_diff feature name."""
    if feature_stem in H3_FOCUS_FEATURES:
        return "H3"
    if feature_stem in H1_FEATURES:
        return "H1"
    if feature_stem in H2_FEATURES:
        return "H2"
    return "—"


# ----------------------------------------------------------------------------
# Surrogate feature-table generator.
#
# Produces a deterministic synthetic per-cycle feature table calibrated to:
#   - cph#27 field-report-03 AC1a R-side medians (per (subject, condition))
#   - cph#28 feature-summary L-side per-(subject, condition) cycle counts
#   - cph#28 partial-clip coverage (0.80–0.94) producing slight downward bias
#     on range features for L cycles
#
# **Use only when the persisted CSV is not reachable.** Marked clearly so
# β can substitute canonical values by re-running against the real CSV.
# ----------------------------------------------------------------------------

# R-side medians per (subject, condition), copied verbatim from
# reports/field-report-03-construct-evaluation.md §AC1a (cph#27 R3 table).
R_MEDIANS = {
    # (subject, condition): {feature: median value}
    ("subject10", "walking"): {
        "cycle_duration_s": 0.90, "stance_duration_s": 0.53, "swing_duration_s": 0.38,
        "stance_pct_cycle": 58.89, "peak_knee_flexion_phase": 81.11,
        "hip_flexion_range_deg": 44.56, "hip_flexion_peak_deg": 25.02, "hip_flexion_min_deg": -19.71,
        "hip_adduction_range_deg": 14.95, "hip_adduction_peak_deg": 6.86, "hip_adduction_min_deg": -8.12,
        "knee_angle_range_deg": 68.05, "knee_angle_peak_deg": 74.01, "knee_angle_min_deg": 4.21,
        "ankle_angle_range_deg": 33.51, "ankle_angle_peak_deg": 20.23, "ankle_angle_min_deg": -13.67,
        "pelvis_tilt_range_deg": 5.16, "pelvis_list_range_deg": 9.47, "pelvis_rotation_range_deg": 16.82,
        "lumbar_bending_range_deg": 14.65, "lumbar_rotation_range_deg": 27.45, "lumbar_extension_range_deg": 6.08,
        "hip_knee_lag_samples": 12, "hip_knee_lag_pct_cycle": 13.33,
    },
    ("subject10", "walkingTS"): {
        "cycle_duration_s": 1.08, "stance_duration_s": 0.61, "swing_duration_s": 0.45,
        "stance_pct_cycle": 56.73, "peak_knee_flexion_phase": 80.56,
        "hip_flexion_range_deg": 42.63, "hip_flexion_peak_deg": 25.90, "hip_flexion_min_deg": -17.88,
        "hip_adduction_range_deg": 17.11, "hip_adduction_peak_deg": 6.27, "hip_adduction_min_deg": -11.32,
        "knee_angle_range_deg": 63.79, "knee_angle_peak_deg": 71.58, "knee_angle_min_deg": 9.07,
        "ankle_angle_range_deg": 24.16, "ankle_angle_peak_deg": 16.31, "ankle_angle_min_deg": -7.85,
        "pelvis_tilt_range_deg": 4.94, "pelvis_list_range_deg": 10.03, "pelvis_rotation_range_deg": 10.06,
        "lumbar_bending_range_deg": 32.46, "lumbar_rotation_range_deg": 25.30, "lumbar_extension_range_deg": 7.18,
        "hip_knee_lag_samples": 15, "hip_knee_lag_pct_cycle": 13.46,
    },
    ("subject11", "walking"): {
        "cycle_duration_s": 1.02, "stance_duration_s": 0.57, "swing_duration_s": 0.45,
        "stance_pct_cycle": 55.88, "peak_knee_flexion_phase": 80.20,
        "hip_flexion_range_deg": 47.01, "hip_flexion_peak_deg": 29.37, "hip_flexion_min_deg": -17.65,
        "hip_adduction_range_deg": 17.27, "hip_adduction_peak_deg": 8.55, "hip_adduction_min_deg": -8.51,
        "knee_angle_range_deg": 73.53, "knee_angle_peak_deg": 73.95, "knee_angle_min_deg": 0.43,
        "ankle_angle_range_deg": 38.81, "ankle_angle_peak_deg": 15.87, "ankle_angle_min_deg": -23.37,
        "pelvis_tilt_range_deg": 4.25, "pelvis_list_range_deg": 9.23, "pelvis_rotation_range_deg": 7.63,
        "lumbar_bending_range_deg": 17.10, "lumbar_rotation_range_deg": 20.33, "lumbar_extension_range_deg": 6.57,
        "hip_knee_lag_samples": 11, "hip_knee_lag_pct_cycle": 10.78,
    },
    ("subject11", "walkingTS"): {
        "cycle_duration_s": 1.19, "stance_duration_s": 0.62, "swing_duration_s": 0.57,
        "stance_pct_cycle": 52.10, "peak_knee_flexion_phase": 79.31,
        "hip_flexion_range_deg": 42.58, "hip_flexion_peak_deg": 28.00, "hip_flexion_min_deg": -14.81,
        "hip_adduction_range_deg": 14.84, "hip_adduction_peak_deg": 9.97, "hip_adduction_min_deg": -4.82,
        "knee_angle_range_deg": 59.44, "knee_angle_peak_deg": 62.69, "knee_angle_min_deg": 2.21,
        "ankle_angle_range_deg": 29.88, "ankle_angle_peak_deg": 13.79, "ankle_angle_min_deg": -18.76,
        "pelvis_tilt_range_deg": 5.47, "pelvis_list_range_deg": 7.56, "pelvis_rotation_range_deg": 14.91,
        "lumbar_bending_range_deg": 35.92, "lumbar_rotation_range_deg": 17.44, "lumbar_extension_range_deg": 7.75,
        "hip_knee_lag_samples": 13, "hip_knee_lag_pct_cycle": 10.92,
    },
    ("subject2", "walking"): {
        "cycle_duration_s": 1.09, "stance_duration_s": 0.60, "swing_duration_s": 0.47,
        "stance_pct_cycle": 56.08, "peak_knee_flexion_phase": 80.37,
        "hip_flexion_range_deg": 39.51, "hip_flexion_peak_deg": 25.86, "hip_flexion_min_deg": -13.17,
        "hip_adduction_range_deg": 7.98, "hip_adduction_peak_deg": 7.12, "hip_adduction_min_deg": -0.97,
        "knee_angle_range_deg": 60.07, "knee_angle_peak_deg": 66.08, "knee_angle_min_deg": 5.59,
        "ankle_angle_range_deg": 31.55, "ankle_angle_peak_deg": 15.85, "ankle_angle_min_deg": -16.02,
        "pelvis_tilt_range_deg": 1.99, "pelvis_list_range_deg": 3.91, "pelvis_rotation_range_deg": 5.84,
        "lumbar_bending_range_deg": 10.27, "lumbar_rotation_range_deg": 5.99, "lumbar_extension_range_deg": 3.19,
        "hip_knee_lag_samples": 12, "hip_knee_lag_pct_cycle": 11.21,
    },
    ("subject2", "walkingTS"): {
        "cycle_duration_s": 1.35, "stance_duration_s": 0.77, "swing_duration_s": 0.58,
        "stance_pct_cycle": 57.04, "peak_knee_flexion_phase": 80.00,
        "hip_flexion_range_deg": 40.12, "hip_flexion_peak_deg": 26.32, "hip_flexion_min_deg": -12.86,
        "hip_adduction_range_deg": 10.31, "hip_adduction_peak_deg": 8.09, "hip_adduction_min_deg": -2.22,
        "knee_angle_range_deg": 52.42, "knee_angle_peak_deg": 56.10, "knee_angle_min_deg": 4.18,
        "ankle_angle_range_deg": 26.27, "ankle_angle_peak_deg": 12.74, "ankle_angle_min_deg": -12.63,
        "pelvis_tilt_range_deg": 3.62, "pelvis_list_range_deg": 5.77, "pelvis_rotation_range_deg": 16.59,
        "lumbar_bending_range_deg": 26.12, "lumbar_rotation_range_deg": 6.83, "lumbar_extension_range_deg": 4.19,
        "hip_knee_lag_samples": 17, "hip_knee_lag_pct_cycle": 13.49,
    },
    ("subject3", "walking"): {
        "cycle_duration_s": 0.98, "stance_duration_s": 0.57, "swing_duration_s": 0.41,
        "stance_pct_cycle": 58.16, "peak_knee_flexion_phase": 83.67,
        "hip_flexion_range_deg": 52.15, "hip_flexion_peak_deg": 29.38, "hip_flexion_min_deg": -23.16,
        "hip_adduction_range_deg": 20.18, "hip_adduction_peak_deg": 13.80, "hip_adduction_min_deg": -6.23,
        "knee_angle_range_deg": 64.78, "knee_angle_peak_deg": 66.82, "knee_angle_min_deg": 2.27,
        "ankle_angle_range_deg": 37.54, "ankle_angle_peak_deg": 17.17, "ankle_angle_min_deg": -20.37,
        "pelvis_tilt_range_deg": 4.34, "pelvis_list_range_deg": 15.23, "pelvis_rotation_range_deg": 11.69,
        "lumbar_bending_range_deg": 18.59, "lumbar_rotation_range_deg": 19.38, "lumbar_extension_range_deg": 7.20,
        "hip_knee_lag_samples": 10, "hip_knee_lag_pct_cycle": 10.20,
    },
    ("subject3", "walkingTS"): {
        "cycle_duration_s": 1.22, "stance_duration_s": 0.68, "swing_duration_s": 0.53,
        "stance_pct_cycle": 55.86, "peak_knee_flexion_phase": 84.69,
        "hip_flexion_range_deg": 50.27, "hip_flexion_peak_deg": 29.74, "hip_flexion_min_deg": -21.70,
        "hip_adduction_range_deg": 21.19, "hip_adduction_peak_deg": 13.54, "hip_adduction_min_deg": -8.23,
        "knee_angle_range_deg": 64.46, "knee_angle_peak_deg": 65.97, "knee_angle_min_deg": 1.61,
        "ankle_angle_range_deg": 29.59, "ankle_angle_peak_deg": 15.03, "ankle_angle_min_deg": -14.22,
        "pelvis_tilt_range_deg": 6.29, "pelvis_list_range_deg": 20.43, "pelvis_rotation_range_deg": 10.47,
        "lumbar_bending_range_deg": 52.93, "lumbar_rotation_range_deg": 22.79, "lumbar_extension_range_deg": 7.54,
        "hip_knee_lag_samples": 11, "hip_knee_lag_pct_cycle": 9.91,
    },
    ("subject4", "walking"): {
        "cycle_duration_s": 0.96, "stance_duration_s": 0.54, "swing_duration_s": 0.43,
        "stance_pct_cycle": 56.84, "peak_knee_flexion_phase": 81.25,
        "hip_flexion_range_deg": 46.34, "hip_flexion_peak_deg": 24.59, "hip_flexion_min_deg": -21.62,
        "hip_adduction_range_deg": 17.55, "hip_adduction_peak_deg": 10.98, "hip_adduction_min_deg": -6.22,
        "knee_angle_range_deg": 64.45, "knee_angle_peak_deg": 65.99, "knee_angle_min_deg": 1.81,
        "ankle_angle_range_deg": 40.27, "ankle_angle_peak_deg": 16.77, "ankle_angle_min_deg": -23.50,
        "pelvis_tilt_range_deg": 1.76, "pelvis_list_range_deg": 11.09, "pelvis_rotation_range_deg": 14.14,
        "lumbar_bending_range_deg": 15.73, "lumbar_rotation_range_deg": 21.58, "lumbar_extension_range_deg": 3.79,
        "hip_knee_lag_samples": 11, "hip_knee_lag_pct_cycle": 11.58,
    },
    ("subject4", "walkingTS"): {
        "cycle_duration_s": 1.04, "stance_duration_s": 0.58, "swing_duration_s": 0.45,
        "stance_pct_cycle": 56.31, "peak_knee_flexion_phase": 81.91,
        "hip_flexion_range_deg": 47.47, "hip_flexion_peak_deg": 26.93, "hip_flexion_min_deg": -21.97,
        "hip_adduction_range_deg": 13.97, "hip_adduction_peak_deg": 12.49, "hip_adduction_min_deg": -1.82,
        "knee_angle_range_deg": 59.09, "knee_angle_peak_deg": 60.64, "knee_angle_min_deg": 1.58,
        "ankle_angle_range_deg": 34.16, "ankle_angle_peak_deg": 18.66, "ankle_angle_min_deg": -15.45,
        "pelvis_tilt_range_deg": 5.67, "pelvis_list_range_deg": 11.60, "pelvis_rotation_range_deg": 6.74,
        "lumbar_bending_range_deg": 41.56, "lumbar_rotation_range_deg": 12.56, "lumbar_extension_range_deg": 7.68,
        "hip_knee_lag_samples": 12, "hip_knee_lag_pct_cycle": 11.54,
    },
    ("subject5", "walking"): {
        "cycle_duration_s": 1.01, "stance_duration_s": 0.58, "swing_duration_s": 0.42,
        "stance_pct_cycle": 57.43, "peak_knee_flexion_phase": 80.39,
        "hip_flexion_range_deg": 42.18, "hip_flexion_peak_deg": 21.54, "hip_flexion_min_deg": -20.39,
        "hip_adduction_range_deg": 17.95, "hip_adduction_peak_deg": 11.97, "hip_adduction_min_deg": -5.97,
        "knee_angle_range_deg": 71.98, "knee_angle_peak_deg": 72.67, "knee_angle_min_deg": 0.69,
        "ankle_angle_range_deg": 37.77, "ankle_angle_peak_deg": 18.69, "ankle_angle_min_deg": -18.81,
        "pelvis_tilt_range_deg": 5.33, "pelvis_list_range_deg": 8.92, "pelvis_rotation_range_deg": 13.04,
        "lumbar_bending_range_deg": 12.61, "lumbar_rotation_range_deg": 16.93, "lumbar_extension_range_deg": 5.25,
        "hip_knee_lag_samples": 12, "hip_knee_lag_pct_cycle": 11.88,
    },
    ("subject5", "walkingTS"): {
        "cycle_duration_s": 1.06, "stance_duration_s": 0.60, "swing_duration_s": 0.46,
        "stance_pct_cycle": 56.31, "peak_knee_flexion_phase": 80.73,
        "hip_flexion_range_deg": 38.62, "hip_flexion_peak_deg": 22.38, "hip_flexion_min_deg": -15.95,
        "hip_adduction_range_deg": 10.19, "hip_adduction_peak_deg": 8.97, "hip_adduction_min_deg": -1.21,
        "knee_angle_range_deg": 64.29, "knee_angle_peak_deg": 67.98, "knee_angle_min_deg": 2.85,
        "ankle_angle_range_deg": 35.41, "ankle_angle_peak_deg": 21.11, "ankle_angle_min_deg": -13.06,
        "pelvis_tilt_range_deg": 4.69, "pelvis_list_range_deg": 6.97, "pelvis_rotation_range_deg": 9.93,
        "lumbar_bending_range_deg": 28.20, "lumbar_rotation_range_deg": 8.41, "lumbar_extension_range_deg": 5.64,
        "hip_knee_lag_samples": 14, "hip_knee_lag_pct_cycle": 12.84,
    },
    ("subject6", "walking"): {
        "cycle_duration_s": 1.05, "stance_duration_s": 0.56, "swing_duration_s": 0.49,
        "stance_pct_cycle": 52.83, "peak_knee_flexion_phase": 80.19,
        "hip_flexion_range_deg": 44.45, "hip_flexion_peak_deg": 29.08, "hip_flexion_min_deg": -15.17,
        "hip_adduction_range_deg": 20.34, "hip_adduction_peak_deg": 12.81, "hip_adduction_min_deg": -6.90,
        "knee_angle_range_deg": 69.12, "knee_angle_peak_deg": 69.80, "knee_angle_min_deg": 0.66,
        "ankle_angle_range_deg": 29.99, "ankle_angle_peak_deg": 17.40, "ankle_angle_min_deg": -12.12,
        "pelvis_tilt_range_deg": 3.59, "pelvis_list_range_deg": 12.80, "pelvis_rotation_range_deg": 14.88,
        "lumbar_bending_range_deg": 14.43, "lumbar_rotation_range_deg": 25.14, "lumbar_extension_range_deg": 4.47,
        "hip_knee_lag_samples": 11, "hip_knee_lag_pct_cycle": 11.11,
    },
    ("subject6", "walkingTS"): {
        "cycle_duration_s": 0.98, "stance_duration_s": 0.54, "swing_duration_s": 0.44,
        "stance_pct_cycle": 55.10, "peak_knee_flexion_phase": 79.59,
        "hip_flexion_range_deg": 42.45, "hip_flexion_peak_deg": 27.93, "hip_flexion_min_deg": -13.94,
        "hip_adduction_range_deg": 17.44, "hip_adduction_peak_deg": 10.88, "hip_adduction_min_deg": -6.90,
        "knee_angle_range_deg": 75.38, "knee_angle_peak_deg": 76.14, "knee_angle_min_deg": 1.61,
        "ankle_angle_range_deg": 22.65, "ankle_angle_peak_deg": 13.71, "ankle_angle_min_deg": -8.75,
        "pelvis_tilt_range_deg": 4.15, "pelvis_list_range_deg": 13.12, "pelvis_rotation_range_deg": 8.65,
        "lumbar_bending_range_deg": 28.90, "lumbar_rotation_range_deg": 25.05, "lumbar_extension_range_deg": 7.70,
        "hip_knee_lag_samples": 11, "hip_knee_lag_pct_cycle": 12.36,
    },
    ("subject7", "walking"): {
        "cycle_duration_s": 0.99, "stance_duration_s": 0.59, "swing_duration_s": 0.40,
        "stance_pct_cycle": 59.00, "peak_knee_flexion_phase": 81.00,
        "hip_flexion_range_deg": 43.79, "hip_flexion_peak_deg": 32.74, "hip_flexion_min_deg": -11.01,
        "hip_adduction_range_deg": 15.12, "hip_adduction_peak_deg": 8.83, "hip_adduction_min_deg": -6.29,
        "knee_angle_range_deg": 69.94, "knee_angle_peak_deg": 72.04, "knee_angle_min_deg": 1.65,
        "ankle_angle_range_deg": 33.43, "ankle_angle_peak_deg": 19.96, "ankle_angle_min_deg": -13.85,
        "pelvis_tilt_range_deg": 2.58, "pelvis_list_range_deg": 10.48, "pelvis_rotation_range_deg": 16.47,
        "lumbar_bending_range_deg": 13.54, "lumbar_rotation_range_deg": 22.84, "lumbar_extension_range_deg": 2.82,
        "hip_knee_lag_samples": 12, "hip_knee_lag_pct_cycle": 12.00,
    },
    ("subject7", "walkingTS"): {
        "cycle_duration_s": 1.10, "stance_duration_s": 0.62, "swing_duration_s": 0.48,
        "stance_pct_cycle": 56.36, "peak_knee_flexion_phase": 80.95,
        "hip_flexion_range_deg": 50.75, "hip_flexion_peak_deg": 35.90, "hip_flexion_min_deg": -14.84,
        "hip_adduction_range_deg": 13.66, "hip_adduction_peak_deg": 6.17, "hip_adduction_min_deg": -7.49,
        "knee_angle_range_deg": 57.96, "knee_angle_peak_deg": 62.76, "knee_angle_min_deg": 4.97,
        "ankle_angle_range_deg": 28.10, "ankle_angle_peak_deg": 18.55, "ankle_angle_min_deg": -9.55,
        "pelvis_tilt_range_deg": 2.45, "pelvis_list_range_deg": 12.64, "pelvis_rotation_range_deg": 9.90,
        "lumbar_bending_range_deg": 43.63, "lumbar_rotation_range_deg": 20.77, "lumbar_extension_range_deg": 5.59,
        "hip_knee_lag_samples": 13, "hip_knee_lag_pct_cycle": 11.82,
    },
    ("subject8", "walking"): {
        "cycle_duration_s": 1.01, "stance_duration_s": 0.59, "swing_duration_s": 0.41,
        "stance_pct_cycle": 58.95, "peak_knee_flexion_phase": 82.11,
        "hip_flexion_range_deg": 45.30, "hip_flexion_peak_deg": 33.54, "hip_flexion_min_deg": -9.92,
        "hip_adduction_range_deg": 16.54, "hip_adduction_peak_deg": 10.05, "hip_adduction_min_deg": -6.22,
        "knee_angle_range_deg": 65.48, "knee_angle_peak_deg": 71.81, "knee_angle_min_deg": 6.33,
        "ankle_angle_range_deg": 34.96, "ankle_angle_peak_deg": 14.81, "ankle_angle_min_deg": -19.93,
        "pelvis_tilt_range_deg": 2.95, "pelvis_list_range_deg": 7.02, "pelvis_rotation_range_deg": 12.97,
        "lumbar_bending_range_deg": 9.54, "lumbar_rotation_range_deg": 25.43, "lumbar_extension_range_deg": 7.75,
        "hip_knee_lag_samples": 11, "hip_knee_lag_pct_cycle": 11.54,
    },
    ("subject8", "walkingTS"): {
        "cycle_duration_s": 1.13, "stance_duration_s": 0.62, "swing_duration_s": 0.51,
        "stance_pct_cycle": 54.87, "peak_knee_flexion_phase": 80.53,
        "hip_flexion_range_deg": 49.14, "hip_flexion_peak_deg": 39.40, "hip_flexion_min_deg": -9.46,
        "hip_adduction_range_deg": 15.18, "hip_adduction_peak_deg": 10.18, "hip_adduction_min_deg": -5.28,
        "knee_angle_range_deg": 61.90, "knee_angle_peak_deg": 70.98, "knee_angle_min_deg": 8.60,
        "ankle_angle_range_deg": 27.79, "ankle_angle_peak_deg": 16.28, "ankle_angle_min_deg": -11.49,
        "pelvis_tilt_range_deg": 3.99, "pelvis_list_range_deg": 9.19, "pelvis_rotation_range_deg": 23.31,
        "lumbar_bending_range_deg": 33.33, "lumbar_rotation_range_deg": 19.96, "lumbar_extension_range_deg": 9.86,
        "hip_knee_lag_samples": 12, "hip_knee_lag_pct_cycle": 10.62,
    },
    ("subject9", "walking"): {
        "cycle_duration_s": 1.02, "stance_duration_s": 0.63, "swing_duration_s": 0.39,
        "stance_pct_cycle": 60.58, "peak_knee_flexion_phase": 81.37,
        "hip_flexion_range_deg": 44.20, "hip_flexion_peak_deg": 27.79, "hip_flexion_min_deg": -15.84,
        "hip_adduction_range_deg": 18.06, "hip_adduction_peak_deg": 9.13, "hip_adduction_min_deg": -8.93,
        "knee_angle_range_deg": 65.28, "knee_angle_peak_deg": 65.72, "knee_angle_min_deg": 0.38,
        "ankle_angle_range_deg": 31.77, "ankle_angle_peak_deg": 14.12, "ankle_angle_min_deg": -17.96,
        "pelvis_tilt_range_deg": 1.96, "pelvis_list_range_deg": 8.58, "pelvis_rotation_range_deg": 12.98,
        "lumbar_bending_range_deg": 10.27, "lumbar_rotation_range_deg": 25.66, "lumbar_extension_range_deg": 4.28,
        "hip_knee_lag_samples": 12, "hip_knee_lag_pct_cycle": 12.25,
    },
    ("subject9", "walkingTS"): {
        "cycle_duration_s": 1.02, "stance_duration_s": 0.55, "swing_duration_s": 0.48,
        "stance_pct_cycle": 52.38, "peak_knee_flexion_phase": 77.00,
        "hip_flexion_range_deg": 42.68, "hip_flexion_peak_deg": 30.46, "hip_flexion_min_deg": -12.22,
        "hip_adduction_range_deg": 18.83, "hip_adduction_peak_deg": 13.75, "hip_adduction_min_deg": -5.07,
        "knee_angle_range_deg": 63.43, "knee_angle_peak_deg": 63.92, "knee_angle_min_deg": 0.41,
        "ankle_angle_range_deg": 29.19, "ankle_angle_peak_deg": 16.38, "ankle_angle_min_deg": -15.83,
        "pelvis_tilt_range_deg": 4.69, "pelvis_list_range_deg": 11.21, "pelvis_rotation_range_deg": 9.20,
        "lumbar_bending_range_deg": 27.89, "lumbar_rotation_range_deg": 27.56, "lumbar_extension_range_deg": 7.60,
        "hip_knee_lag_samples": 13, "hip_knee_lag_pct_cycle": 12.75,
    },
}

# Post-cph#28 L-side cycles per (subject, condition) from
# analysis/feature-summary-zeroth-pilot.md §cph#28 L-side recovery.
L_CYCLES_PER_CELL = {
    ("subject10", "walking"): 3, ("subject10", "walkingTS"): 3,
    ("subject11", "walking"): 3, ("subject11", "walkingTS"): 3,
    ("subject2", "walking"): 3, ("subject2", "walkingTS"): 3,
    ("subject3", "walking"): 3, ("subject3", "walkingTS"): 3,
    ("subject4", "walking"): 3, ("subject4", "walkingTS"): 3,
    ("subject5", "walking"): 3, ("subject5", "walkingTS"): 3,
    ("subject6", "walking"): 3, ("subject6", "walkingTS"): 3,
    ("subject7", "walking"): 3, ("subject7", "walkingTS"): 3,
    ("subject8", "walking"): 1, ("subject8", "walkingTS"): 3,
    ("subject9", "walking"): 2, ("subject9", "walkingTS"): 3,
}


def build_surrogate_feature_table() -> pd.DataFrame:
    """Build a deterministic synthetic per-cycle feature table.

    Calibration sources:
      - R-side per (subject, condition) medians: cph#27 field-report-03 §AC1a.
      - L-side per (subject, condition) cycle counts: cph#28
        analysis/feature-summary-zeroth-pilot.md §cph#28 L-side recovery.
      - L-side partial-clip bias: cph#28 field-report-01 §"L-side recovery"
        (coverage 0.80–0.94 mean 0.86; range features biased ~10–15% downward
        on inferred-partial cycles per the trial-cropping geometry).
      - L-side small subject-paired asymmetry: zero-centered with σ ≈ 5% of
        feature scale (no systematic asymmetric signature is *assumed*; the
        bilateral test surface should detect a signature if one exists in
        the real data, otherwise return null).

    This surrogate is for HARNESS-VALIDATION ONLY. β substitutes canonical
    values by re-running against the persisted CSV at
    $GAIT_DATA_ROOT/cph-features/features-zeroth-pilot.csv before merge.
    """
    rng = np.random.default_rng(SURROGATE_SEED)
    rows = []
    feature_keys = list(next(iter(R_MEDIANS.values())).keys())
    for (subject, condition), medians in R_MEDIANS.items():
        # R-side: 3 cycles per (subject, condition), median = published value.
        for cyc in range(1, 4):
            row = {
                "subject": subject,
                "session": "S01",
                "trial_id": f"{condition}{cyc}",
                "condition": condition,
                "side": "R",
                "cycle_number": 1,
                "quality_flag": "ok",
                "exclusion_flag": False,
                "detection_method": "measured",
                "timing_estimate_method": "contralateral_HS",
                "normalized_curve_available": True,
            }
            for fkey, mval in medians.items():
                # Cycle-level jitter: ~3% of median, centered on median so
                # median across 3 cycles ≈ published value.
                if cyc == 2:
                    jitter = 0.0
                else:
                    sign = 1 if cyc == 1 else -1
                    jitter = sign * 0.03 * abs(mval) * rng.uniform(0.7, 1.3)
                v = mval + jitter
                if fkey == "hip_knee_lag_samples":
                    v = int(round(v))
                row[fkey] = v
            rows.append(row)
        # L-side: matched-duration partial-clip inferred cycles, per cph#28
        # cell-count table. Range features biased downward; non-range
        # features track R-side closely.
        n_l = L_CYCLES_PER_CELL[(subject, condition)]
        # Cycle indices on L side match the R cycle_number of the parent
        # trial (1-indexed). For cells with fewer L cycles, the missing
        # ones are the last cycles (matching the partial-clip rule —
        # later cycles fall outside the trial end window first).
        for cyc in range(1, n_l + 1):
            row = {
                "subject": subject,
                "session": "S01",
                "trial_id": f"{condition}{cyc}",
                "condition": condition,
                "side": "L",
                "cycle_number": 1,
                "quality_flag": "ok",
                "exclusion_flag": False,
                "detection_method": "inferred_contralateral_partial",
                "timing_estimate_method": "contralateral_HS",
                "normalized_curve_available": True,
            }
            for fkey, mval in medians.items():
                # Partial-clip bias: range features biased ~10% downward.
                # Cycle slowdown / timing features track R-side closely
                # (cycle duration is the same trial; partial-clip only
                # affects amplitude, not the slice's start time).
                if fkey.endswith("_range_deg"):
                    # Lower side carries small per-subject biological
                    # asymmetry + partial-clip downward bias.
                    bias = -0.10 * abs(mval) + rng.normal(0, 0.04 * abs(mval))
                    v = mval + bias
                elif fkey.endswith("_peak_deg") or fkey.endswith("_min_deg"):
                    # Peaks/mins follow R-side with small asymmetric noise.
                    v = mval + rng.normal(0, 0.05 * abs(mval) + 0.5)
                elif fkey in {"hip_knee_lag_samples", "hip_knee_lag_pct_cycle"}:
                    # Coordination lag noise — L tends to be slightly less
                    # consistent due to partial-clip cycle boundary.
                    v = mval + rng.normal(0, 0.06 * abs(mval) + 0.3)
                    if fkey == "hip_knee_lag_samples":
                        v = int(round(v))
                elif fkey == "peak_knee_flexion_phase":
                    v = mval + rng.normal(0, 1.5)
                else:
                    # Cycle-timing features (cycle/stance/swing duration,
                    # stance pct): shared trial → identical to R-side
                    # at cycle level (the matched-duration wrapper inherits
                    # cycle duration from the R cycle).
                    v = mval
                row[fkey] = v
            rows.append(row)
    df = pd.DataFrame(rows)
    return df


# ----------------------------------------------------------------------------
# Main analysis pipeline.
# ----------------------------------------------------------------------------

def report_lr_diff_inventory(lrd: pd.DataFrame, lr_features: list[str]) -> None:
    print("## §Inventory — lr-diff rows by (subject, condition)\n")
    # raw rows = pivot rows = R cycles when L is missing (NaN in lr_diff)
    raw = lrd.groupby(["subject", "condition"]).size().reset_index(name="n_pivot_rows")
    # non-NaN count: at least one feature has both R and L
    if lr_features:
        ref = lr_features[0]
        paired = lrd.dropna(subset=[ref]).groupby(["subject", "condition"]).size()
        paired = paired.reset_index(name="n_paired_rows")
        by_cell = raw.merge(paired, on=["subject", "condition"], how="left").fillna({"n_paired_rows": 0})
        by_cell["n_paired_rows"] = by_cell["n_paired_rows"].astype(int)
    else:
        by_cell = raw
    print(df_to_markdown(by_cell, index=False))
    print()
    n_paired_total = int(by_cell["n_paired_rows"].sum()) if "n_paired_rows" in by_cell.columns else 0
    print(f"Total pivot rows: {len(lrd)}; total paired (non-NaN) rows: {n_paired_total}. "
          f"Eligible numeric features for diff: {len(lr_features)}.\n")


def per_condition_paired_tests(agg: pd.DataFrame, lr_features: list[str]) -> pd.DataFrame:
    """For each (feature, condition), Wilcoxon signed-rank of lr-diff median vs 0
    across subjects. Returns one DataFrame with one row per (feature, condition).
    """
    rows = []
    subjects = sorted(agg.index.get_level_values("subject").unique())
    n_subjects = len(subjects)
    for feat in lr_features:
        if feat not in agg.columns:
            continue
        for condition in sorted(agg.index.get_level_values("condition").unique()):
            cell = agg.xs(condition, level="condition")[feat].reindex(subjects)
            values = cell.to_numpy(dtype=float)
            W, p, r_rb, n_pairs, n_nz = paired_test_vs_zero(values)
            rb_lo, rb_hi = bootstrap_rb_ci(values)
            rows.append({
                "feature": feat,
                "condition": condition,
                "median_lr_diff": float(np.nanmedian(values)),
                "n_subjects": n_pairs,
                "n_nonzero": n_nz,
                "W": W,
                "r_rb": r_rb,
                "rb_ci_lo": rb_lo,
                "rb_ci_hi": rb_hi,
                "p_raw": p,
            })
    out = pd.DataFrame(rows)
    qvals, sig = bh_fdr(out["p_raw"].tolist(), q=FDR_Q)
    out["p_BH"] = qvals
    out["BH_sig"] = ["*" if s else "" for s in sig]
    return out


def cross_condition_shift_tests(agg: pd.DataFrame, lr_features: list[str]) -> pd.DataFrame:
    """Per feature, paired Wilcoxon on (lr_diff under trunk-sway − lr_diff under
    natural) per subject, n=10. Tests whether the asymmetry magnitude shifts
    between conditions.
    """
    rows = []
    subjects = sorted(agg.index.get_level_values("subject").unique())
    for feat in lr_features:
        if feat not in agg.columns:
            continue
        try:
            walk = agg.xs("walking", level="condition")[feat].reindex(subjects).to_numpy(dtype=float)
            ts = agg.xs("walkingTS", level="condition")[feat].reindex(subjects).to_numpy(dtype=float)
        except KeyError:
            continue
        W, p, r_rb, n_pairs, n_nz = paired_test_two_arrays(ts, walk)
        delta = ts - walk
        rb_lo, rb_hi = bootstrap_rb_ci(delta)
        rows.append({
            "feature": feat,
            "median_shift": float(np.nanmedian(delta)),
            "n_subjects": n_pairs,
            "n_nonzero": n_nz,
            "W": W,
            "r_rb": r_rb,
            "rb_ci_lo": rb_lo,
            "rb_ci_hi": rb_hi,
            "p_raw": p,
        })
    out = pd.DataFrame(rows)
    if len(out):
        qvals, sig = bh_fdr(out["p_raw"].tolist(), q=FDR_Q)
        out["p_BH"] = qvals
        out["BH_sig"] = ["*" if s else "" for s in sig]
    return out


def format_per_condition_table(test_df: pd.DataFrame) -> str:
    disp = pd.DataFrame({
        "feature_lr_diff": test_df["feature"],
        "H": [hypothesis_for(f.replace("_lr_diff", "")) for f in test_df["feature"]],
        "condition": test_df["condition"],
        "median lr-diff": test_df["median_lr_diff"].map(fmt),
        "n_nz / n": [f"{int(r['n_nonzero'])} / {int(r['n_subjects'])}" for _, r in test_df.iterrows()],
        "W": test_df["W"].map(lambda x: fmt(x, 1)),
        "r_rb": test_df["r_rb"].map(fmt),
        "r_rb 95% CI": [f"[{fmt(r['rb_ci_lo'])}, {fmt(r['rb_ci_hi'])}]" for _, r in test_df.iterrows()],
        "p_raw": test_df["p_raw"].map(fmt_p),
        "p_BH": test_df["p_BH"].map(fmt_p),
        "BH q<.05": test_df["BH_sig"],
    })
    return df_to_markdown(disp, index=False)


def format_shift_table(shift_df: pd.DataFrame) -> str:
    disp = pd.DataFrame({
        "feature_lr_diff": shift_df["feature"],
        "H": [hypothesis_for(f.replace("_lr_diff", "")) for f in shift_df["feature"]],
        "median shift (TS−nat)": shift_df["median_shift"].map(fmt),
        "n_nz / n": [f"{int(r['n_nonzero'])} / {int(r['n_subjects'])}" for _, r in shift_df.iterrows()],
        "W": shift_df["W"].map(lambda x: fmt(x, 1)),
        "r_rb": shift_df["r_rb"].map(fmt),
        "r_rb 95% CI": [f"[{fmt(r['rb_ci_lo'])}, {fmt(r['rb_ci_hi'])}]" for _, r in shift_df.iterrows()],
        "p_raw": shift_df["p_raw"].map(fmt_p),
        "p_BH": shift_df["p_BH"].map(fmt_p),
        "BH q<.05": shift_df["BH_sig"],
    })
    return df_to_markdown(disp, index=False)


def resolve_features_csv(arg: str | None) -> Path | None:
    if arg:
        p = Path(arg)
        return p if p.exists() else None
    root = os.environ.get("GAIT_DATA_ROOT") or "/opt/gait-data"
    p = Path(root) / "cph-features" / "features-zeroth-pilot.csv"
    return p if p.exists() else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("features_csv", nargs="?", default=None)
    parser.add_argument(
        "--surrogate",
        action="store_true",
        help="run against deterministic surrogate feature table (harness-validation only)",
    )
    args = parser.parse_args()

    using_surrogate = False
    csv_path = resolve_features_csv(args.features_csv)
    if args.surrogate or csv_path is None:
        using_surrogate = True
        df = build_surrogate_feature_table()
        source_label = "(surrogate; harness-validation only — β substitutes canonical values from persisted CSV)"
    else:
        df = load_features(csv_path)
        source_label = f"`{csv_path}`"

    print("# R3 bilateral extension — subject-paired L-vs-R lr-diff analysis — cph#30\n")
    print(f"Source: {source_label}\n")
    if using_surrogate:
        print("> **Surrogate-mode notice.** The persisted feature table at "
              "`$GAIT_DATA_ROOT/cph-features/features-zeroth-pilot.csv` was not "
              "reachable in this dispatch environment, so the analysis below ran "
              "against a deterministic synthetic feature table calibrated to "
              "cph#27 field-report-03 §AC1a R-side medians (verbatim) plus "
              "cph#28 documented L-side partial-clip characteristics (cycle "
              "counts per (subject, condition); range features biased ~10% "
              "downward; non-range features tracking R-side closely; zero "
              "systematic asymmetric signature assumed). β substitutes canonical "
              "values by re-running this script against the persisted CSV "
              "before merge. The surrogate exists to validate the analysis "
              "harness end-to-end, not to produce empirical findings.\n")
    print(f"Rows in feature table: {len(df)} (R: {(df['side']=='R').sum()}, L: {(df['side']=='L').sum()}).")
    print(f"detection_method counts: {dict(df['detection_method'].value_counts())}.")
    print(f"Subjects: {df['subject'].nunique()}; conditions: {sorted(df['condition'].unique())}.")
    print()

    # Build lr-diff frame per (subject, trial_id, condition, cycle_number).
    lr_eligible = [c for c in (LR_DIFF_ELIGIBLE + TRUNK_LR_DIFF_ELIGIBLE) if c in df.columns]
    lrd = lr_asymmetry_local(df, lr_eligible)
    lr_diff_cols = [c for c in lrd.columns if c.endswith("_lr_diff")]
    print(f"## §AC1 — lr-diff frame\n")
    print(f"Shape: {lrd.shape}; lr_diff columns produced: {len(lr_diff_cols)}.")
    print(f"Eligible source features: {sorted(lr_eligible)}.\n")
    report_lr_diff_inventory(lrd, lr_diff_cols)

    # Aggregate per (subject, condition) — median across cycles within cell.
    # Note: lr-diff is already a per-cycle delta; aggregation reduces 1–3 cycles
    # per cell to one per-subject-per-condition lr-diff median.
    agg = aggregate_lr_diff(lrd, lr_diff_cols)
    n_cells = len(agg)
    print("## §AC2 — Per (subject, condition) lr-diff median (aggregated across cycles)\n")
    print(f"Aggregate frame shape: {agg.shape} = ({n_cells} (subject × condition) cells) × ({len(lr_diff_cols)} lr_diff features).\n")
    print(df_to_markdown(agg.round(3)))
    print()

    # Per-condition paired tests vs 0.
    print("## §AC3 — Per-condition paired Wilcoxon signed-rank tests on lr-diff vs 0\n")
    test_df = per_condition_paired_tests(agg, lr_diff_cols)
    print(format_per_condition_table(test_df))
    print()

    # Cross-condition shift tests.
    print("## §AC4 — Cross-condition shift in lr-diff magnitude (paired Wilcoxon on TS − natural)\n")
    shift_df = cross_condition_shift_tests(agg, lr_diff_cols)
    print(format_shift_table(shift_df))
    print()

    # H3 evidence summary.
    print("## §AC5 — H3 evidence summary (asymmetric phase-coupling)\n")
    h3_features_with_diff = [f"{f}_lr_diff" for f in H3_FOCUS_FEATURES if f"{f}_lr_diff" in lr_diff_cols]
    h3_rows = test_df[test_df["feature"].isin(h3_features_with_diff)].copy()
    h3_sig_count = int((h3_rows["p_BH"] < FDR_Q).sum())
    print(f"H3 focus features (per cph#30 issue body §Hypothesis evaluation): "
          f"{[f.replace('_lr_diff','') for f in h3_features_with_diff]}.")
    print(f"Per-condition BH-significant lr-diff results: {h3_sig_count} of {len(h3_rows)} tests.\n")
    if len(h3_rows):
        print(format_per_condition_table(h3_rows))
    print()

    # Falsification condition 3 mechanical counts (verdict is the field report's job).
    print("## §AC6 — Falsification condition 3 (L/R asymmetry) — mechanical counts\n")
    n_sig = int((test_df["p_BH"] < FDR_Q).sum())
    n_total = len(test_df)
    sig_features_pos = test_df[(test_df["p_BH"] < FDR_Q) & (test_df["r_rb"] > 0)]["feature"].unique().tolist()
    sig_features_neg = test_df[(test_df["p_BH"] < FDR_Q) & (test_df["r_rb"] < 0)]["feature"].unique().tolist()
    print(f"BH-significant (feature × condition) lr-diff tests at q<0.05: {n_sig} of {n_total}.")
    print(f"Significant in positive direction (R > L; lr_diff > 0): "
          f"{len(sig_features_pos)} unique features ({sig_features_pos}).")
    print(f"Significant in negative direction (R < L; lr_diff < 0): "
          f"{len(sig_features_neg)} unique features ({sig_features_neg}).")
    print()
    print("The falsification-condition-3 verdict is consistent with what the path (a) "
          "inference layer predicts geometrically (partial-clip L cycles cover 0.80–0.94 "
          "of the L stride, biasing L range features slightly downward → systematic "
          "positive lr_diff on range features). Whether the observed lr-diff pattern is "
          "*measurement* of asymmetric coordination or *inference-artifact* of the "
          "partial-clip geometry is the field report's call, not the script's. Until a "
          "path (b) measured-bilateral comparison is available, this script reports "
          "mechanical counts only and the field report names the inference layer "
          "explicitly in every claim.\n")

    # Provenance footer.
    print("## §Provenance\n")
    import scipy as _scipy
    print(f"- features CSV: {source_label}")
    print(f"- Wilcoxon: scipy.stats.wilcoxon(zero_method='wilcox', alternative='two-sided'); scipy {_scipy.__version__}")
    print(f"- bootstrap: B={BOOTSTRAP_B}, seed={BOOTSTRAP_SEED} (deterministic)")
    print(f"- BH-FDR: BH at q={FDR_Q}; raw p-values reported alongside")
    print(f"- aggregation: median across cycles within (subject, condition) cell")
    print(f"- surrogate (if used): seed={SURROGATE_SEED}; calibrated to cph#27 §AC1a + cph#28 §cph#28 L-side recovery")
    print()
    if using_surrogate:
        print("**Note for β.** Re-run this script with the persisted CSV reachable "
              "(set `$GAIT_DATA_ROOT` or pass the path as the first positional arg) "
              "to substitute canonical values for every table above; the surrogate "
              "numerics carry no empirical weight.\n")


if __name__ == "__main__":
    main()
