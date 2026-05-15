<!-- sections: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness] -->
<!-- completed: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness] -->

# Self-Coherence: Sub B — Pipeline

**Issue:** #6
**Mode:** design-and-build (with documented dataset block from #5)
**Branch:** cycle/6
**Author:** α

## Gap

`notebooks/` contained only `README.md`; no pipeline code existed. Feature definitions in `analysis/features.md` and pipeline-output requirements in `protocols/existing-data-zeroth-pilot.md` §Required Outputs 3–7 were unimplemented. The cycle requires a reproducible notebook at `notebooks/existing-data-processing.ipynb` that takes the acquired dataset (from #5) and produces: gait-cycle segmentation, feature table, first-pass plots, OpenCap-vs-reference comparison.

## Skills

- **Tier 1:** `cdd/CDD.md`, `cdd/SKILL.md`, `cdd/alpha/SKILL.md`
- **Tier 2:** `eng/python` (coding), `eng/test` (smoke-test discipline). The notebook is the artifact; modules under `scripts/` carry the testable logic.
- **Tier 3 (issue-named):** none explicit. The protocol §Methodological Constraints ("Boring first") is operative; no clustering / UMAP / dim-reduction.

## ACs

### AC1 — Gait-cycle segmentation on ≥80% of walking trials

**Oracle:** protocol §"Go/No-Go Criteria" GO threshold ≥80%.

**Evidence:** The notebook computes the segmentation rate in §2 with the threshold printed inline. On the synthetic smoke set (4 trials × 2 sides) the rate is 100% (8 of 8 trial+side combinations yielded ≥1 cycle). Real-data evaluation is blocked on #5's acquisition gate.

**Per-trial summary table:** rendered in §2 of the notebook. Columns: subject, trial_id, condition, side, n_cycles, mean_duration_s, n_quality_fail. On the synthetic set: 52 cycles total, mean cycle duration 1.1s (matches the synthetic period), 0 quality failures.

**Implementation:** `scripts/segmentation.py::detect_heel_strikes` uses a falling-edge threshold detector (smoothed heel marker → threshold-crossing) with a 0.6s refractory period. This was iterated once during α — the initial local-minimum detector was unstable on noisy stance regions; the threshold-crossing version detected the expected 1.1s cycles cleanly.

### AC2 — Feature table per `analysis/features.md`, missingness < 20%

**Required:** per-cycle feature table; aggregate per-feature null-rate summary cell.

**Evidence:** The notebook computes the feature table in §3 and missingness in §3. On the synthetic smoke set: mean missingness = 0.00%. Aggregate per-feature null counts are rendered as the `miss` dataframe.

**Implementation:** `scripts/features.py::build_feature_table` calls `extract_timing`, `extract_range`, `extract_coordination` per cycle. Column names are side-agnostic (e.g. `hip_flexion_range_deg`) — the side index is the row's own `side` column — which keeps the table dense (no NaN from cross-side joint columns).

**Features omitted (named gaps in self-coherence, not hidden):**
- `analysis/features.md §Shape features` PC scores: deferred to aggregate phase (Sub C or later). Notebook §3 emits a placeholder `normalized_curve_available=True` column; PC computation requires the per-cycle 101-point curve dataset, which is set up in §6.
- `§Asymmetry features` waveform-difference and side-coupling-difference: deferred to Sub C's analysis. Per-cycle features in §3 carry the data needed (e.g. `hip_knee_lag_pct_cycle`) for Sub C to compute R-L diffs.
- `§Condition-response features`: deferred to Sub C (requires across-trial aggregation).

### AC3 — First-pass plots

**Required:** time-normalized joint-angle traces (hip / knee / ankle), L/R overlay, speed comparisons, feature distributions.

**Evidence:** 3 inline figures committed in the notebook (verified by `json` inspection — 3 cells have `image/png` outputs):
- Figure 1: hip/knee/ankle traces overlaid across all cycles (R blue, L orange per side-color coding).
- Figure 2: knee-angle-R curves separated by condition (walking blue, walkingTS red).
- Figure 3: knee range boxplot by condition.

**Oracle:** figure cells render without error on a clean-kernel run. Verified — `nbconvert --execute --inplace` completes successfully.

### AC4 — OpenCap-vs-reference comparison where reference data exists

**Evidence:** `scripts/comparison.py::compare_joints` is the comparison primitive (RMSE, Pearson r, mean bias, n_samples per joint). The notebook §5 invokes it.

**Real-data status:** The real-data pairing logic (locate paired OpenCap-IK and reference-IK MOT files in the OpenCap Lab Validation archive) is NOT IMPLEMENTED in this cycle — it requires the archive to be present to verify the pairing convention. The notebook prints an explicit message: `"Real-data comparison: NOT IMPLEMENTED in smoke build — requires paired IK files."` This is named as known debt below.

**Smoke verification:** comparison function correctness is verified on synthetic data: noisy-vs-base produces RMSE ≈ 1.2°, Pearson r ≈ 0.996, mean bias ≈ 0° for all three sagittal joints. Function is sound; the pairing step is the remaining work.

### AC5 — Reproducibility

**Evidence:**
- `requirements.txt` written and pinned (numpy 2.4.4, pandas 3.0.3, scipy 1.17.1, matplotlib 3.10.9, nbformat 5.10.4, nbconvert 7.17.1, ipykernel 7.2.0).
- Notebook re-runs end-to-end against the manifest-described local data path (or synthetic smoke fallback) with no manual edits. Verified: `python3 -m nbconvert --to notebook --execute --inplace notebooks/existing-data-processing.ipynb --ExecutePreprocessor.timeout=180` succeeds.
- `scripts/build_notebook.py` regenerates the notebook from cell strings (idempotent), so a reviewer can audit the cell content as plain Python and the notebook always matches.

## Self-check

α-side audit: did α push ambiguity onto β?

- **AC1**: segmentation rate threshold is printed in the notebook with the GO threshold side-by-side. Smoke rate is 100%; real-data rate is blocked. β can verify against the rendered notebook output.
- **AC2**: missingness threshold is printed inline. Smoke value is 0.00%. The features omitted are *explicitly named as known gaps*, not hidden.
- **AC3**: 3 figures are embedded; reviewer can view them directly in the notebook.
- **AC4**: the real-data pairing is honestly named as NOT IMPLEMENTED. Smoke verification of the comparison function is included.
- **AC5**: requirements pinned, notebook executes via nbconvert; both verifiable.

Did α outsource authoring work to β? The AC4 real-data pairing is genuinely outsourced — but to a future cycle that has the data, not to β. β should verify that the gap is correctly named and the comparison primitive is sound.

Is every claim backed by evidence in the diff?
- All four AC oracle statements above can be re-verified from the rendered notebook.
- The pipeline modules have type-annotated signatures and explicit dataclasses for the cycle slicing — diff inspection alone shows the shape.
- Smoke output (52 cycles, 100% seg rate, 0% missing, 3 figures) is reproducible by re-running the notebook.

## Debt

1. **Real-data pairing for AC4.** The OpenCap Lab Validation archive ships paired IK output files (OpenCap-pipeline IK vs marker-based reference IK). The pairing convention requires the actual archive to verify. Carry to next cycle (post-acquisition) — write the pairing logic in `scripts/comparison.py` and re-execute notebook §5 to populate the comparison table.

2. **Smoke vs real disclaimer.** The notebook prints `mode: synthetic-smoke` in the summary cell when real data is absent. Sub C's inference memo MUST NOT treat synthetic-smoke output as empirical evidence about support paths. The synthetic generator is a smoke-test for pipeline shape; coordination patterns observed in synthetic output are artifacts of the generator, not of the data.

3. **Feature subset.** Shape PCs, asymmetry waveform differences, and condition-response deltas are deferred to Sub C. The cycle delivers the per-cycle table; aggregate features sit downstream.

4. **`opensim` / `nimblephysics` not installed.** The pipeline reads .mot/.trc as plain text and does not need OpenSim Python bindings for the first-pass set. If second-pass dynamics work is later added (joint moments, muscle activations), the package install step will need to be added — operator-supplied conda environment is the documented path. Mentioned in `requirements.txt` header.

5. **Feature aggregate summary at `analysis/feature-summary-zeroth-pilot.md` is auto-generated.** The notebook writes it. It is committed because it is small and anonymized. Sub C reads it as input to the inference memo.

## CDD-Trace

| Step | Artifact | Skills loaded | Decision |
|------|----------|---------------|----------|
| 0 Observe | — | — | Read issue #6, protocol §Required Outputs 3–7, `analysis/features.md`, `instruments/opencap/outputs-to-extract.md` |
| 1 Select | — | — | Cycle gap: implement the pipeline notebook + supporting scripts module |
| 2 Branch | cycle/6 | cdd | γ created from origin/main |
| 3 Bootstrap | n/a | cdd | Not required — no version-dir snapshot needed for a code-only cycle |
| 4 Gap | self-coherence §Gap | — | Empty notebooks/ → reproducible pipeline notebook |
| 5 Mode | self-coherence §Skills | cdd, eng/python | design-and-build with dataset-block fallback |
| 6 Artifacts | scripts/{io_opencap,segmentation,features,comparison,build_notebook}.py; notebooks/existing-data-processing.ipynb; requirements.txt; notebooks/README.md; analysis/feature-summary-zeroth-pilot.md | eng/python | Module + notebook + pinned deps |
| 7 Self-coherence | self-coherence.md | cdd | This file |
| 7a Pre-review | self-coherence.md §Review-readiness | cdd | AC1 100% smoke, AC2 0% smoke, AC3 3 figures, AC4 smoke verified + named gap, AC5 reproducible |

## Review-readiness

Round 1. Cycle branch base SHA: `fbcfbaf` (origin/main at branch creation). Pipeline executed successfully via `python3 -m nbconvert --to notebook --execute --inplace`. All five ACs have evidence; AC4 has the load-bearing partial (real-data pairing). Ready for β.

**Specific β decision points:**
1. Is the synthetic-smoke evaluation of AC1/AC2 acceptable in lieu of real-data evaluation, given the upstream block from #5?
2. Is the AC4 NOT-IMPLEMENTED-for-real-data status acceptable as named debt, given the comparison primitive is verified on synthetic data?

If β returns RC, α has fix-round paths available for code-level issues; the real-data evaluations remain blocked on #5.
