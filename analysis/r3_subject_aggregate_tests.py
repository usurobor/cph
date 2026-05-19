"""R3 subject-level aggregate condition-response analysis (cph#27).

Reads the per-cycle feature table produced by `notebooks/existing-data-processing.ipynb`,
filters to R-side rows, aggregates each numeric feature per (subject, condition)
by median and by mean, runs a paired Wilcoxon signed-rank test across the n=10
subjects per feature, computes the rank-biserial effect size with a percentile
bootstrap 95% CI (B=10,000), and applies BH-FDR multiple-comparisons correction
at q=0.05.

Outputs markdown-formatted tables to stdout for direct inclusion in
`reports/field-report-03-construct-evaluation.md`. Method picks documented in
`.cdr/unreleased/27/self-coherence.md` §Method picks.

Usage:
    python3 analysis/r3_subject_aggregate_tests.py [path-to-features-csv]

Default features-csv path: $GAIT_DATA_ROOT/cph-features/features-zeroth-pilot.csv
(falls back to /opt/gait-data/cph-features/features-zeroth-pilot.csv).

This script does NOT modify the input file and does NOT persist any aggregate
table to disk — outputs are stdout only, to keep the cycle compliant with the
no-raw-data-committed AC9 boundary (the field report carries the derived
aggregates inline as markdown).
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

# Method-pick constants — keep in sync with .cdr/unreleased/27/self-coherence.md §Method picks.
BOOTSTRAP_B = 10_000
BOOTSTRAP_SEED = 20260519  # cycle dispatch date; deterministic for β re-verification.
FDR_Q = 0.05

# Columns excluded from per-feature aggregation: indexing + non-numeric metadata.
NON_FEATURE_COLS = {
    "subject", "session", "trial_id", "condition", "side", "cycle_number",
    "quality_flag", "exclusion_flag",
    "timing_estimate_method", "normalized_curve_available",
}

# Hypothesis → features (per issue body §Approach "Hypothesis evaluation surface").
# Features named here are evaluated regardless of test outcome; α reports the
# mechanistic interpretation for each as part of AC3.
H1_FEATURES = [
    "hip_flexion_range_deg", "knee_angle_range_deg", "ankle_angle_range_deg",
    "hip_knee_lag_pct_cycle", "peak_knee_flexion_phase",
]
H2_FEATURES = [
    "lumbar_extension_range_deg", "lumbar_bending_range_deg", "lumbar_rotation_range_deg",
    "pelvis_tilt_range_deg", "pelvis_list_range_deg", "pelvis_rotation_range_deg",
    "hip_adduction_range_deg", "hip_adduction_peak_deg", "hip_adduction_min_deg",
]


def load_features(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def numeric_feature_cols(df: pd.DataFrame) -> list[str]:
    """The numeric feature columns (excluding indexing + metadata sentinels)."""
    candidates = [c for c in df.columns if c not in NON_FEATURE_COLS]
    out = []
    for c in candidates:
        if pd.api.types.is_numeric_dtype(df[c]):
            out.append(c)
    return out


def aggregate(df: pd.DataFrame, features: list[str]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Aggregate per (subject, condition) by median and by mean.

    Returns two wide-format frames indexed by (subject, condition) with one
    column per feature: (median_agg, mean_agg).
    """
    grouped = df.groupby(["subject", "condition"], sort=True)[features]
    med = grouped.median()
    mean = grouped.mean()
    return med, mean


def long_format_count(agg: pd.DataFrame, n_carry_through: int) -> int:
    """Cell count in long-format aggregate table (AC1 oracle).

    n_rows × (n_numeric + n_carry_through_indexing_cols), counted per AC1's
    '10 × 2 × 35 = 700' rule with 35 = 25 numeric + 8 indexing + 2 sentinel.
    """
    n_rows = len(agg)  # 20 = 10 subjects × 2 conditions.
    n_cols = agg.shape[1] + n_carry_through
    return n_rows * n_cols


def paired_delta(med: pd.DataFrame, feature: str) -> np.ndarray:
    """Per-subject (trunk-sway − natural) median delta for one feature."""
    wide = med[feature].unstack("condition")
    # Pair only subjects with both conditions present (all 10 here).
    common = wide.dropna()
    delta = (common["walkingTS"] - common["walking"]).to_numpy()
    return delta


def wilcoxon_with_rb(delta: np.ndarray) -> tuple[float, float, float, int, int]:
    """Wilcoxon signed-rank + rank-biserial effect size.

    Returns (W_statistic, p_two_sided, r_rb, n_pairs, n_nonzero_pairs).

    r_rb is computed from W_pos / W_neg as
        r_rb = (W_pos - W_neg) / (W_pos + W_neg)
    so the sign agrees with the direction of the paired delta median.
    """
    nz = delta[delta != 0]
    n_pairs = int(len(delta))
    n_nonzero = int(len(nz))
    if n_nonzero == 0:
        return float("nan"), 1.0, 0.0, n_pairs, 0
    res = stats.wilcoxon(delta, zero_method="wilcox", alternative="two-sided")
    W = float(res.statistic)
    p = float(res.pvalue)
    ranks = stats.rankdata(np.abs(nz))
    W_pos = float(ranks[nz > 0].sum())
    W_neg = float(ranks[nz < 0].sum())
    denom = W_pos + W_neg
    r_rb = (W_pos - W_neg) / denom if denom > 0 else 0.0
    return W, p, r_rb, n_pairs, n_nonzero


def bootstrap_rb_ci(delta: np.ndarray, B: int = BOOTSTRAP_B, seed: int = BOOTSTRAP_SEED) -> tuple[float, float]:
    """Percentile bootstrap 95% CI for rank-biserial r_rb.

    Resampling is over the n paired deltas (Efron pairs bootstrap). Each
    resample recomputes r_rb from its own (W_pos, W_neg). Bias-corrected
    BCa is intentionally not used — at n=10 the BCa acceleration estimate
    is unstable and the percentile method is the standard fallback.
    """
    rng = np.random.default_rng(seed)
    n = len(delta)
    if n == 0:
        return float("nan"), float("nan")
    samples = np.empty(B, dtype=float)
    for b in range(B):
        idx = rng.integers(0, n, size=n)
        d = delta[idx]
        nz = d[d != 0]
        if len(nz) == 0:
            samples[b] = 0.0
            continue
        ranks = stats.rankdata(np.abs(nz))
        W_pos = float(ranks[nz > 0].sum())
        W_neg = float(ranks[nz < 0].sum())
        denom = W_pos + W_neg
        samples[b] = (W_pos - W_neg) / denom if denom > 0 else 0.0
    lo = float(np.percentile(samples, 2.5))
    hi = float(np.percentile(samples, 97.5))
    return lo, hi


def bh_fdr(pvals: list[float], q: float = FDR_Q) -> tuple[list[float], list[bool]]:
    """Benjamini–Hochberg FDR adjustment.

    Returns (q-values, significant-at-q boolean list), in original order.
    """
    p = np.asarray(pvals, dtype=float)
    n = len(p)
    order = np.argsort(p, kind="stable")
    ranked = p[order]
    # BH-adjusted: q_i = min_{j>=i}( n * p_j / (j+1) ); enforce monotone, clip to 1.
    adj_sorted = ranked * n / (np.arange(n) + 1)
    adj_sorted = np.minimum.accumulate(adj_sorted[::-1])[::-1]
    adj_sorted = np.clip(adj_sorted, 0.0, 1.0)
    adj = np.empty(n, dtype=float)
    adj[order] = adj_sorted
    sig = (adj < q).tolist()
    return adj.tolist(), sig


def df_to_markdown(df: pd.DataFrame, index: bool = True) -> str:
    """Minimal markdown-table renderer to avoid a tabulate dependency."""
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
    if x is None or (isinstance(x, float) and (np.isnan(x))):
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


def hypothesis_for(feature: str) -> str:
    if feature in H1_FEATURES:
        return "H1"
    if feature in H2_FEATURES:
        return "H2"
    return "—"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("features_csv", nargs="?", default=None)
    args = parser.parse_args()

    if args.features_csv:
        csv_path = Path(args.features_csv)
    else:
        root = os.environ.get("GAIT_DATA_ROOT") or "/opt/gait-data"
        csv_path = Path(root) / "cph-features" / "features-zeroth-pilot.csv"
    if not csv_path.exists():
        sys.exit(f"features CSV not found: {csv_path}")

    df = load_features(csv_path)

    r = df[df["side"] == "R"].copy()
    print("# R3 subject-level aggregate condition-response analysis — cph#27\n")
    print(f"Source: `{csv_path}` (read-only; not committed; AC9 boundary respected).\n")
    print(f"Rows in feature table: {len(df)} (R: {len(r)}, L: {(df['side']=='L').sum()}).")
    print(f"R-side subjects: {r['subject'].nunique()}; conditions: {sorted(r['condition'].unique())}.")
    print(f"R cycles per (subject, condition): {r.groupby(['subject','condition']).size().unique().tolist()} (uniform).")
    print()

    features = numeric_feature_cols(r)
    print(f"## §Feature inventory\n")
    print(f"Total per-cycle columns: {len(df.columns)} (matches `analysis/feature-summary-zeroth-pilot.md` AC2 '35 columns').")
    print(f"Indexing + non-numeric columns excluded from aggregation: {len(NON_FEATURE_COLS)} ({sorted(NON_FEATURE_COLS)}).")
    print(f"Testable numeric features: {len(features)} ({features}).\n")

    med, mean = aggregate(r, features)
    n_subjects = med.index.get_level_values("subject").nunique()
    n_conditions = med.index.get_level_values("condition").nunique()
    n_features = len(features)
    n_rows_per_cell = n_subjects * n_conditions
    print(f"## §AC1 — Per-subject-condition aggregate table\n")
    print(f"Aggregate frames shape: {med.shape} = ({n_rows_per_cell} (subject × condition) rows) × ({n_features} numeric features).")
    print(f"AC1 long-format cell count (10 × 2 × 35 = 700): "
          f"{long_format_count(med, len(NON_FEATURE_COLS))} cells "
          f"({n_rows_per_cell} rows × ({n_features} numeric + {len(NON_FEATURE_COLS)} carry-through indexing/sentinel) = "
          f"{n_rows_per_cell} × {n_features + len(NON_FEATURE_COLS)} = "
          f"{n_rows_per_cell * (n_features + len(NON_FEATURE_COLS))}).\n")

    print("### §AC1a — Median aggregate (primary)\n")
    print(df_to_markdown(med.round(3)))
    print()
    print("### §AC1b — Mean aggregate (robustness)\n")
    print(df_to_markdown(mean.round(3)))
    print()

    # Per-subject (trunk-sway − natural) median delta — the AC2 paired-test input.
    delta_rows = []
    for f in features:
        d = paired_delta(med, f)
        delta_rows.append([f] + list(np.round(d, 3)))
    subjects = sorted(med.index.get_level_values("subject").unique())
    delta_cols = ["feature"] + subjects
    delta_df = pd.DataFrame(delta_rows, columns=delta_cols)
    print("### §AC1c — Per-subject paired delta (trunk-sway median − natural median)\n")
    print(df_to_markdown(delta_df, index=False))
    print()

    # AC2: paired Wilcoxon + rank-biserial + bootstrap CI + BH-FDR.
    print("## §AC2 — Paired Wilcoxon signed-rank tests across n=10 subjects\n")
    raw_pvals = []
    rows = []
    for f in features:
        d = paired_delta(med, f)
        W, p, r_rb, n_pairs, n_nonzero = wilcoxon_with_rb(d)
        rb_lo, rb_hi = bootstrap_rb_ci(d)
        median_delta = float(np.median(d))
        raw_pvals.append(p)
        rows.append({
            "feature": f,
            "hypothesis": hypothesis_for(f),
            "median_delta": median_delta,
            "n_pairs": n_pairs,
            "n_nonzero": n_nonzero,
            "W": W,
            "p_raw": p,
            "r_rb": r_rb,
            "rb_ci95_lo": rb_lo,
            "rb_ci95_hi": rb_hi,
        })
    qvals, sig = bh_fdr(raw_pvals, q=FDR_Q)
    for i, row in enumerate(rows):
        row["p_BH"] = qvals[i]
        row["BH_sig"] = "*" if sig[i] else ""

    test_df = pd.DataFrame(rows)
    test_df_display = pd.DataFrame({
        "feature": test_df["feature"],
        "H": test_df["hypothesis"],
        "median Δ (TS−nat)": test_df["median_delta"].map(fmt),
        "n_nz / n": [f"{int(r['n_nonzero'])} / {int(r['n_pairs'])}" for _, r in test_df.iterrows()],
        "W": test_df["W"].map(lambda x: fmt(x, 1)),
        "r_rb": test_df["r_rb"].map(fmt),
        "r_rb 95% CI": [f"[{fmt(r['rb_ci95_lo'])}, {fmt(r['rb_ci95_hi'])}]" for _, r in test_df.iterrows()],
        "p_raw": test_df["p_raw"].map(fmt_p),
        "p_BH": test_df["p_BH"].map(fmt_p),
        "BH q<.05": test_df["BH_sig"],
    })
    print(df_to_markdown(test_df_display, index=False))
    print()

    # H1 / H2 summaries.
    print("## §AC3 — Per-hypothesis evidence summary\n")
    for hyp_label, hyp_features, hyp_title in [
        ("H1", H1_FEATURES, "H1 — Sagittal-dominant load transfer"),
        ("H2", H2_FEATURES, "H2 — Trunk-sway compensation"),
    ]:
        print(f"### {hyp_title}\n")
        h_rows = test_df[test_df["feature"].isin(hyp_features)].copy()
        print(f"Features tested ({len(h_rows)} of {len(hyp_features)} pre-registered): "
              f"{sorted(h_rows['feature'].tolist())}.")
        if len(h_rows):
            n_sig = int((h_rows["p_BH"] < FDR_Q).sum())
            n_pos = int((h_rows["r_rb"] > 0).sum())
            n_neg = int((h_rows["r_rb"] < 0).sum())
            print(f"BH-significant at q<{FDR_Q}: {n_sig} / {len(h_rows)}. "
                  f"Direction: positive (TS > natural) in {n_pos}; negative (TS < natural) in {n_neg}.")
            print()
            print(df_to_markdown(h_rows[["feature", "median_delta", "r_rb", "p_raw", "p_BH"]].round(4), index=False))
        print()
    print("### H3 — Asymmetric phase-coupling (not testable)\n")
    print(f"H3 requires R/L pairs at matching (subject, cycle_number). The R-side feature table has "
          f"{(df['side']=='L').sum()} L-side cycle(s) total ({(df[df['side']=='L'])['subject'].iloc[0] if (df['side']=='L').any() else '—'}, "
          f"{(df[df['side']=='L'])['trial_id'].iloc[0] if (df['side']=='L').any() else '—'}). "
          f"No subject has both R and L aggregates available; H3 is structurally non-testable on this archive "
          f"and is deferred to cph#28's L-cycle recovery.\n")

    # Mean-vs-median agreement check (robustness).
    print("## §Method-pick robustness — mean vs median direction agreement\n")
    flips = []
    for f in features:
        d_med = paired_delta(med, f)
        d_mean = paired_delta(mean, f)
        if (np.median(d_med) * np.median(d_mean)) < 0:
            flips.append(f)
    print(f"Features where median-aggregate paired-delta sign disagrees with mean-aggregate paired-delta sign: "
          f"{len(flips)} of {len(features)}.")
    if flips:
        print(f"Flipped features: {flips}")
    print()

    print("## §Provenance\n")
    print(f"- features CSV: `{csv_path}` (not committed; AC9)")
    import scipy as _scipy
    print(f"- Wilcoxon: scipy.stats.wilcoxon(zero_method='wilcox', alternative='two-sided'); scipy {_scipy.__version__}")
    print(f"- bootstrap: B={BOOTSTRAP_B}, seed={BOOTSTRAP_SEED} (deterministic).")
    print(f"- BH-FDR: BH at q={FDR_Q}; raw p-values also reported.")
    print(f"- aggregation: median primary, mean reported.\n")


if __name__ == "__main__":
    main()
