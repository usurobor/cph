"""Build `notebooks/existing-data-processing.ipynb` programmatically.

Generates a fully-runnable notebook from cell strings so the file in the
repo always matches the latest pipeline implementation. Running this
script regenerates the notebook (idempotent).

Usage:
    python3 scripts/build_notebook.py
"""

from __future__ import annotations

import json
from pathlib import Path

import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell


def build() -> nbformat.NotebookNode:
    nb = new_notebook()
    nb.cells = []

    nb.cells.append(new_markdown_cell("""# Existing-data zeroth pilot — pipeline

This notebook is the canonical pipeline for issue #6. It produces:

1. Gait-cycle segmentation (per-trial × side summary table)
2. Feature table per `analysis/features.md`
3. Time-normalized joint-angle traces (hip / knee / ankle, L/R overlay)
4. Speed / condition comparisons
5. OpenCap-vs-reference comparison stats

The notebook re-runs end-to-end against:
- **Real data** when `<GAIT_DATA_ROOT>/opencap-lab-validation/extracted/` is populated (default `GAIT_DATA_ROOT=/opt/gait-data/`; see `data/external/opencap-lab-validation.md` §Acquisition procedure and `notebooks/README.md` §Overriding the data root).
- **Synthetic data** otherwise — a smoke-test of pipeline shape using `scripts.io_opencap.synthesize_trial()`. The smoke-test produces real figures and a feature table but the support-path inference from synthetic data is *not* a valid empirical claim.

**Active design constraints** (from issue #6):
- Boring first: no clustering, no UMAP, no dim-reduction this cycle.
- No raw participant data committed.
- Each numerical claim in the notebook traces to a cell that produced it.

**Reproducibility (AC5):** dependencies pinned in `requirements.txt`; notebook re-runs against the manifest-described local data path with no manual edits. The data root is overridable via the `GAIT_DATA_ROOT` environment variable (default `/opt/gait-data/`).
"""))

    nb.cells.append(new_code_cell("""# Configuration
%matplotlib inline
from pathlib import Path
import os
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

REPO_ROOT = Path(os.getcwd()).resolve()
if REPO_ROOT.name == "notebooks":
    REPO_ROOT = REPO_ROOT.parent
sys.path.insert(0, str(REPO_ROOT))

# Data root resolution: GAIT_DATA_ROOT env var overrides the documented
# default `/opt/gait-data/`. See notebooks/README.md §Overriding the data
# root. The helpers live in scripts/io_opencap.py so calling code that
# imports the module directly gets the same override behavior.
from scripts.io_opencap import (
    DEFAULT_DATA_ROOT, GAIT_DATA_ROOT_ENV,
    get_data_root, get_opencap_extracted_root,
)

DATA_ROOT = get_data_root()
DATA_PATH = get_opencap_extracted_root()
USE_REAL_DATA = DATA_PATH.exists() and any(DATA_PATH.iterdir())

print(f"REPO_ROOT: {REPO_ROOT}")
print(f"DATA_ROOT: {DATA_ROOT}  (default {DEFAULT_DATA_ROOT}; override env {GAIT_DATA_ROOT_ENV})")
print(f"DATA_PATH: {DATA_PATH}  (exists: {DATA_PATH.exists()})")
print(f"USE_REAL_DATA: {USE_REAL_DATA}")
"""))

    nb.cells.append(new_markdown_cell("## 1. Discover trials"))

    nb.cells.append(new_code_cell("""from scripts.io_opencap import (
    discover_trials, read_mot, read_trc, parse_trial_filename, synthesize_trial, Trial
)

trials: list[Trial] = []
if USE_REAL_DATA:
    # Canonical OpenCap Lab Validation layout:
    # Subject<NN>/IKResults/<trial>_ik.mot
    mot_files = discover_trials(DATA_PATH, pattern="*_ik.mot", walking_only=True)
    print(f"Found {len(mot_files)} walking IK files under {DATA_PATH}")
    for p in mot_files:
        subject = p.parents[1].name if p.parents[1].name.lower().startswith("subject") else "UNKNOWN"
        _, trial_id, condition = parse_trial_filename(p.stem.replace("_ik", ""))
        df = read_mot(p)
        fs = 1 / np.mean(np.diff(df["time"]))
        # mock heel-marker columns if not present (would come from .trc file)
        if "RHEE_Y" not in df.columns:
            print(f"  {p.name}: no marker columns in MOT — need paired TRC, skipping for segmentation")
        trials.append(Trial(subject=subject, trial_id=trial_id, condition=condition,
                            sample_rate_hz=fs, df=df, source_path=p))
else:
    print("No real data found — synthesizing 4 trials for smoke test")
    trials.append(synthesize_trial(subject="Synth01", trial_id="walking1", condition="walking", n_cycles=8))
    trials.append(synthesize_trial(subject="Synth01", trial_id="walking2", condition="walking", n_cycles=8,
                                   rng=np.random.default_rng(43)))
    trials.append(synthesize_trial(subject="Synth01", trial_id="walkingTS1", condition="walkingTS", n_cycles=7,
                                   rng=np.random.default_rng(44), left_right_asymmetry_deg=3.0))
    trials.append(synthesize_trial(subject="Synth02", trial_id="walking1", condition="walking", n_cycles=9,
                                   rng=np.random.default_rng(45)))

print(f"Total trials: {len(trials)}")
for t in trials:
    print(f"  subject={t.subject}  trial={t.trial_id}  condition={t.condition}  n_samples={len(t.df)}  fs={t.sample_rate_hz:.1f} Hz")
"""))

    nb.cells.append(new_markdown_cell("## 2. Gait-cycle segmentation (AC1)"))

    nb.cells.append(new_code_cell("""from scripts.segmentation import segment_trial, summary_table

all_cycles = []
for trial in trials:
    cycles = segment_trial(trial.df, trial.subject, trial.trial_id, trial.condition, trial.sample_rate_hz)
    all_cycles.extend(cycles)
    print(f"  {trial.subject}/{trial.trial_id}/{trial.condition}: {len(cycles)} cycles ({sum(1 for c in cycles if c.side=='R')} R, {sum(1 for c in cycles if c.side=='L')} L)")

seg_summary = summary_table(all_cycles)
seg_summary
"""))

    nb.cells.append(new_code_cell("""# AC1 oracle: ≥80% of walking trials yielded ≥1 cycle.
n_walking_trials = sum(1 for t in trials if 'walk' in t.condition.lower())
trials_with_cycles = seg_summary.groupby(['subject', 'trial_id', 'condition']).size().shape[0] if len(seg_summary) else 0
seg_rate = trials_with_cycles / max(n_walking_trials, 1) * 100.0
print(f"Walking trials: {n_walking_trials}")
print(f"Trials with ≥1 cycle: {trials_with_cycles}")
print(f"Segmentation rate: {seg_rate:.1f}%   (GO ≥80%, NO-GO <60%)")
"""))

    nb.cells.append(new_markdown_cell("## 3. Feature table (AC2)"))

    nb.cells.append(new_code_cell("""from scripts.features import build_feature_table, missingness

features = build_feature_table(all_cycles)
print(f"Feature table shape: {features.shape}")
features.head(8)
"""))

    nb.cells.append(new_code_cell("""miss = missingness(features)
miss
"""))

    nb.cells.append(new_code_cell("""# AC2 oracle: missingness < 20% across feature columns
overall_miss = miss['null_pct'].mean()
print(f"Mean missingness across feature columns: {overall_miss:.2f}%  (target <20%)")
"""))

    nb.cells.append(new_markdown_cell("## 4. First-pass plots (AC3)"))

    nb.cells.append(new_code_cell("""from scripts.segmentation import time_normalize_cycle

def overlay_cycles(cycles, columns, title):
    fig, axes = plt.subplots(1, len(columns), figsize=(4*len(columns), 3.5), sharex=True)
    if len(columns) == 1:
        axes = [axes]
    side_color = {"R": "tab:blue", "L": "tab:orange"}
    for col, ax in zip(columns, axes):
        for c in cycles:
            norm = time_normalize_cycle(c, columns=[col])
            if not norm.empty:
                ax.plot(norm["phase_pct"], norm[col], color=side_color.get(c.side, "k"), alpha=0.3)
        ax.set_xlabel("% gait cycle")
        ax.set_ylabel(f"{col} (deg)")
        ax.set_title(col)
        ax.axvline(60, color='gray', ls=':', alpha=0.5, label='toe-off (typical)')
    fig.suptitle(title)
    plt.tight_layout()
    return fig

r_cycles = [c for c in all_cycles if c.side == "R" and c.quality_flag == "ok"]
l_cycles = [c for c in all_cycles if c.side == "L" and c.quality_flag == "ok"]

fig = overlay_cycles(r_cycles + l_cycles,
                     ["hip_flexion_r", "knee_angle_r", "ankle_angle_r"],
                     "Right-leg cycles overlaid (R blue, L orange — mapping uses side-specific cols)")
plt.show()
"""))

    nb.cells.append(new_code_cell("""# Condition comparison: walking vs walkingTS
def by_condition_plot(cycles, joint_col, title):
    cond_color = {"walking": "tab:blue", "walkingTS": "tab:red"}
    fig, ax = plt.subplots(figsize=(6, 3.5))
    for c in cycles:
        if c.side != "R":
            continue
        norm = time_normalize_cycle(c, columns=[joint_col])
        if not norm.empty:
            ax.plot(norm["phase_pct"], norm[joint_col],
                    color=cond_color.get(c.condition, "k"), alpha=0.4,
                    label=c.condition if c.cycle_number == 1 else "")
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys())
    ax.set_xlabel("% gait cycle")
    ax.set_ylabel(f"{joint_col} (deg)")
    ax.set_title(title)
    plt.tight_layout()
    return fig

fig = by_condition_plot(all_cycles, "knee_angle_r", "Knee angle (R) by condition")
plt.show()
"""))

    nb.cells.append(new_code_cell("""# Feature distribution: knee range across cycles
fig, ax = plt.subplots(figsize=(7, 3.5))
if "knee_angle_range_deg" in features.columns:
    by_cond = {cond: features.loc[features["condition"] == cond, "knee_angle_range_deg"].dropna()
               for cond in features["condition"].unique()}
    ax.boxplot(by_cond.values(), tick_labels=list(by_cond.keys()))
    ax.set_ylabel("knee_angle range (deg)")
    ax.set_title("Knee range distribution by condition")
plt.tight_layout()
plt.show()
"""))

    nb.cells.append(new_markdown_cell("## 5. OpenCap-vs-reference comparison (AC4)"))

    nb.cells.append(new_code_cell("""from scripts.comparison import compare_joints

if USE_REAL_DATA:
    # When real data is present, this cell will load paired (opencap, reference)
    # IK results and compute RMSE / r / bias per joint. The OpenCap Lab
    # Validation archive ships both — see README inside the archive.
    print("Real-data comparison: NOT IMPLEMENTED in smoke build — requires paired IK files.")
    print("Once data is available, populate `opencap_df` and `reference_df` here and call compare_joints().")
    comparison = pd.DataFrame()
else:
    # Smoke: compare a synthetic trial against itself + noise to verify the function shape.
    rng = np.random.default_rng(99)
    base = trials[0].df.copy()
    noisy = base.copy()
    for col in ["hip_flexion_r", "knee_angle_r", "ankle_angle_r"]:
        noisy[col] = noisy[col] + rng.normal(0, 1.5, len(noisy))
    comparison = compare_joints(noisy, base, joints=["hip_flexion_r", "knee_angle_r", "ankle_angle_r"])
    print("Smoke comparison (synthetic vs synthetic+noise):")
comparison
"""))

    nb.cells.append(new_markdown_cell("## 6. Persist feature table (private — not committed)"))

    nb.cells.append(new_code_cell("""PRIVATE_OUT = DATA_ROOT / "gait-support-paths-features"
PRIVATE_OUT.mkdir(parents=True, exist_ok=True)

feature_path = PRIVATE_OUT / "features-zeroth-pilot.parquet"
try:
    features.to_parquet(feature_path, index=False)
    print(f"Feature table written to {feature_path}")
except ImportError:
    # pyarrow not available — fall back to CSV but still outside the repo
    feature_path = PRIVATE_OUT / "features-zeroth-pilot.csv"
    features.to_csv(feature_path, index=False)
    print(f"pyarrow unavailable; wrote CSV instead: {feature_path}")

# Aggregate summary IS committed (small, anonymized)
summary_path = REPO_ROOT / "analysis" / "feature-summary-zeroth-pilot.md"
if len(features):
    n_cycles = len(features)
    n_subjects = features["subject"].nunique()
    n_trials = features.groupby(["subject", "trial_id", "condition"]).size().shape[0]
    summary_md = (f"# Feature Summary (auto-generated)\\n\\n"
                  f"- cycles total: {n_cycles}\\n"
                  f"- subjects: {n_subjects}\\n"
                  f"- trials: {n_trials}\\n"
                  f"- mean missingness across feature columns: {miss['null_pct'].mean():.2f}%\\n"
                  f"- mode: {'real-data' if USE_REAL_DATA else 'synthetic-smoke'}\\n")
    summary_path.write_text(summary_md)
    print(f"Aggregate summary written to {summary_path}")
"""))

    nb.cells.append(new_markdown_cell("""## 7. Notebook self-check

Maps notebook outputs to issue #6 ACs:

- **AC1** — Gait-cycle segmentation ≥80%: printed in cell §2 with explicit threshold.
- **AC2** — Feature table + missingness <20%: printed in cell §3 with explicit threshold.
- **AC3** — First-pass plots (time-normalized hip/knee/ankle, L/R overlay, speed/condition comparisons, feature distributions): cells in §4.
- **AC4** — OpenCap-vs-reference comparison: cell §5. Currently NOT IMPLEMENTED for real data; smoke comparison only.
- **AC5** — Reproducibility: dependencies pinned in `../requirements.txt`; this notebook re-runs end-to-end against `<GAIT_DATA_ROOT>/opencap-lab-validation/extracted/` (default `GAIT_DATA_ROOT=/opt/gait-data/`) when populated.

**Known debt (carried into Sub C):**

- AC4 real-data comparison stub: complete pairing logic for IK/marker files in the OpenCap Lab Validation layout once the archive is acquired.
- The feature table omits some `analysis/features.md` features (asymmetry shape-correlation, condition-response deltas) — they require multi-trial aggregation that lives in Sub C's analysis, not Sub B's per-cycle extraction.
"""))

    return nb


def main() -> int:
    nb = build()
    out = Path("notebooks/existing-data-processing.ipynb")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as fh:
        nbformat.write(nb, fh)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
