# β Review: Sub B — Pipeline

**Cycle:** #6
**Branch:** cycle/6 (head: 560c38e)
**Base:** main (fbcfbaf)
**Reviewer:** β

## Round 1 — Verdict: REQUEST CHANGES (1 binding finding)

### Contract integrity

α HEAD commit author: `alpha@gait-support-paths.cdd.cnos` — passes. β identity confirmed before this commit.

### AC re-verification

- **AC1 (seg ≥80%):** Smoke = 100%. Real-data deferred to #5 unblock. The 1.1s mean cycle duration matches the synthetic period — the segmenter is working as designed. PASS for the smoke path; named debt for real path.
- **AC2 (missingness <20%):** Smoke = 0.00%. PASS. The side-agnostic column rename (`hip_flexion_range_deg` not `hip_flexion_r_range_deg`) is the right call — it makes the table dense without losing the per-side information (side is an index column).
- **AC3 (plots):** 3 figures embedded inline in the notebook (verified via JSON inspection of `cells[*].outputs[*].data["image/png"]`). PASS.
- **AC4 (OpenCap-vs-reference):** Comparison primitive works on the smoke pair (RMSE 1.2°, r 0.997). Real-data pairing logic is honestly named as NOT IMPLEMENTED in self-coherence §Debt #1. β agrees that pairing the IK files inside the OpenCap Lab Validation archive requires the archive — that work is correctly scoped to a future cycle.
- **AC5 (reproducibility):** `requirements.txt` pinned. Notebook executes end-to-end. PASS.

### Diff review — pipeline modules

- `scripts/io_opencap.py`: clean. The `synthesize_trial()` function is appropriately scoped as a smoke test, not a research surface. Falling-edge heel-strike comment in the segmenter would be clearer if it were also reproduced here.
- `scripts/segmentation.py`: threshold-crossing detector is sound. The 0.6s refractory and 2.0s max-cycle guards are documented and match adult walking physiology.
- `scripts/features.py`: side-agnostic column rename in `extract_range()` is the load-bearing fix that drove missingness to 0%. Good. The `extract_shape` placeholder is honest about deferring PC computation; an explicit comment would help future cycles.
- `scripts/comparison.py`: align_time + per-joint RMSE / r / bias is the standard pattern; clean.
- `notebooks/existing-data-processing.ipynb`: structure follows the AC order. Markdown headings map 1:1 to AC numbers. Inline plots render.

### F1 — Pyc files committed (binding, C-severity)

```
scripts/__pycache__/__init__.cpython-312.pyc     |  Bin 0 -> 146 bytes
scripts/__pycache__/comparison.cpython-312.pyc   |  Bin 0 -> 5268 bytes
scripts/__pycache__/features.cpython-312.pyc     |  Bin 0 -> 9680 bytes
scripts/__pycache__/io_opencap.cpython-312.pyc   |  Bin 0 -> 10896 bytes
scripts/__pycache__/segmentation.cpython-312.pyc |  Bin 0 -> 8666 bytes
```

Five `.pyc` files in `scripts/__pycache__/` were committed. These are Python compile cache, regenerated on every run, and add binary noise to the repo. `.gitignore` does not currently cover them.

**Fix:** add `__pycache__/` and `*.pyc` to `.gitignore`, `git rm -rf --cached scripts/__pycache__/`, commit.

### F2 — Notebook output paths assume `/opt/gait-data/` (informational, not blocking)

The notebook writes the feature parquet to `/opt/gait-data/gait-support-paths-features/` and the smoke-mode summary to `analysis/feature-summary-zeroth-pilot.md`. The hard-coded `/opt/gait-data/` path is fine for this single-agent context but should be parameterized via an environment variable (`GAIT_DATA_ROOT`) for portability. Not blocking; track as friction for a future cycle.

### Merge instruction

After α addresses F1: re-review the fix-round, merge if clean.

```
git merge --no-ff origin/cycle/6 -m "Closes #6: Sub B — Build segmentation + feature-extraction pipeline in existing-data-processing.ipynb"
```

### Verdict: REQUEST CHANGES — one binding (F1).
