# Field Report 01: Existing-Data Zeroth Pilot

## Overview

**Report Date:** 2026-05-15
**Protocol:** [protocols/existing-data-zeroth-pilot.md](../protocols/existing-data-zeroth-pilot.md)
**Dataset:** OpenCap Lab Validation from SimTK (selected; not yet acquired — see §Failure Analysis)
**Status:** Executed under the zeroth-pilot wave at `.cdd/waves/zeroth-pilot-2026-05-15/`. **Decision: REVISE.** Methodology and pipeline are sound; the operator-credential gate on SimTK file downloads must be resolved before re-execution of the empirical steps.

## Executive Summary

The zeroth-pilot wave dispatched three sub-cycles in order: dataset acquisition (#5), pipeline implementation (#6), and inference + decision (#7). All three closed with β approval. Pipeline implementation passed smoke-tests on synthetic walking data (100% segmentation, 0% feature missingness, end-to-end notebook execution). Empirical validation against the OpenCap Lab Validation dataset is blocked at SimTK's account-required download endpoint; the dataset's Apache 2.0 license is unambiguously permissive but the access mechanism requires an authenticated session this sandbox does not hold.

The technical foundation (pipeline architecture, segmentation algorithm, feature schema, comparison primitives) is in place and reproducible. The methodological validation (does OpenCap-derived feature data support support-path classification) cannot be answered until the acquisition gate is unblocked. The protocol's intent of "Process existing OpenCap validation walking data" remains unmet; the recommended revision is to record the operator-credential dependency in the protocol so future executions either acquire the data first or substitute a backup dataset that does not require authentication.

Three candidate support-path hypotheses are stated below with their falsification paths against the six conditions in `docs/concepts/support-path.md`. Each hypothesis is properly framed as a candidate — the allowed sentence form is preserved ("Under this condition, this recording shows this movement pattern") — and none is treated as established. The pipeline is now ready to test them when real data lands.

## Trial Inventory

| Dataset | Participants | Walking Trials | Speed Conditions | Quality Assessment |
|---------|-------------|----------------|------------------|-------------------|
| OpenCap Lab Validation (selected, not acquired) | 10 (per Uhlrich et al. 2023 §Methods) | Unknown count; ≥1 per condition per subject | 2 conditions at self-selected speed (natural, trunk-sway) — not graded speeds | Documentation-derived only; per-trial quality blocked on acquisition |

**Notes:** Inventory rows above are derived from the published source paper. Row-level per-trial inventory is named as known debt in `data/external/opencap-lab-validation.md` §Acquisition status; it will be appended once the archive is downloaded.

## Export Inventory

| Data Type | Available | Quality | Usability | Notes |
|-----------|-----------|---------|-----------|-------|
| OpenCap Joint Angles | Documented in source paper | Unknown until acquired | Schema-compatible with pipeline | OpenSim .mot output; `scripts/io_opencap.py::read_mot` parses |
| OpenCap Timing Events | Documented (heel-strike, toe-off via marker traces) | Unknown until acquired | Schema-compatible | Detector at `scripts/segmentation.py::detect_heel_strikes` works on marker .trc |
| Reference Motion Capture | Documented (8-camera Motion Analysis, 31 markers) | Lab gold-standard | Schema-compatible | Marker .trc files |
| Force Plate Data | Documented (3 Bertec, 2000 Hz) | Lab gold-standard | First-pass: not parsed (kinematics-only pipeline). Second-pass: would be added with GRF parsing | Held for future cycles |
| Video Data | Documented (RGB, two-camera) | Source quality | Not used by this pipeline | First-pass kinematics; video re-processing is OpenCap's domain |

## Segmentation Status

| Trial Group | Total Trials | Successful Segmentation | Gait Cycles Extracted | Segmentation Rate | Issues |
|-------------|-------------|------------------------|----------------------|------------------|--------|
| Synthetic smoke — walking | 3 | 3 / 3 (6 / 6 trial+side) | 38 | 100% | None |
| Synthetic smoke — walkingTS | 1 | 1 / 1 (2 / 2 trial+side) | 14 | 100% | None |
| **OpenCap Lab Validation — natural walking** | **(blocked)** | **(blocked)** | **(blocked)** | **N/A** | Acquisition gate (see §Failure Analysis) |
| **OpenCap Lab Validation — trunk-sway walking** | **(blocked)** | **(blocked)** | **(blocked)** | **N/A** | Acquisition gate |

**Overall Segmentation Rate (synthetic smoke only):** 100% — meets the ≥80% GO threshold *for pipeline shape verification*.
**Quality Threshold Met (real-data):** Not yet evaluated.

## Feature Extraction Status

| Feature Category | Extraction Success | Missing Data Rate | Quality Assessment | Interpretability |
|------------------|-------------------|------------------|-------------------|-----------------|
| Timing Features | 100% (smoke) | 0% | Synthetic-clean | Direct from cycle slice |
| Joint Angle Features (range/peak/min) | 100% (smoke) | 0% | Synthetic-clean | Side-agnostic columns; cycle's own side in index |
| Coordination Features (hip-knee xcorr lag) | 100% (smoke) | 0% | Synthetic-clean | Cross-correlation peak lag in % cycle |
| Asymmetry Features (R-L delta) | Deferred to inference phase | N/A | N/A | Computed below in §Support-Path Inference |
| Shape Features (PC scores) | Deferred to multi-trial aggregate | N/A | N/A | Per-cycle normalized curves available |

**Overall Feature Quality (smoke):** 0.00% missingness — meets the <20% GO threshold *for pipeline shape verification*. Real-data missingness is not yet evaluated.

## OpenCap vs Reference Comparison

| Measurement | OpenCap Mean | Reference Mean | Correlation | RMSE | Agreement Assessment |
|-------------|-------------|----------------|-------------|------|---------------------|
| Hip Flexion (synthetic smoke: noisy vs base) | — | — | 0.996 | 1.24° | Comparison function verified |
| Knee Angle (synthetic smoke: noisy vs base) | — | — | 0.997 | 1.21° | Comparison function verified |
| Ankle Angle (synthetic smoke: noisy vs base) | — | — | 0.993 | 1.22° | Comparison function verified |
| **OpenCap vs marker-based IK (real)** | **(blocked)** | **(blocked)** | **(blocked)** | **(blocked)** | Acquisition gate + pairing logic deferred |

**Overall Agreement Rating (real-data):** Not yet evaluated. The comparison primitive in `scripts/comparison.py::compare_joints` is correct (per smoke verification); the remaining work is the IK/marker pairing logic, which requires the unzipped OpenCap Lab Validation archive to confirm file naming conventions.

## Support-Path Inference

**Note on construct framing.** Per `docs/concepts/support-path.md`, the strongest allowed sentence is "Under this condition, this recording shows this movement pattern." Each hypothesis below preserves that form. No hypothesis is treated as established. The pipeline outputs needed to test each are named, along with the falsification condition each maps to.

### Candidate Patterns Observed

#### Hypothesis 1 — Sagittal-plane dominant load transfer

**Pattern claim:** Forward progression during walking is managed primarily through sequential sagittal-plane hip-knee-ankle flexion-extension coupling, with frontal-plane pelvis motion acting as a corrective rather than primary load-bearing mechanism.

**Supporting features (from `analysis/features.md`):**
- `hip_flexion_range_deg`, `knee_angle_range_deg`, `ankle_angle_range_deg` (sagittal magnitudes)
- `hip_knee_lag_pct_cycle` (sagittal coupling timing)
- `pelvis_list_range_deg`, `pelvis_rotation_range_deg` (frontal/transverse for comparison)

**Falsification path:** If `pelvis_list_range_deg` is the same order of magnitude as `hip_flexion_range_deg` *and* `hip_knee_lag_pct_cycle` shows no systematic phase relationship across cycles, then the hypothesis weakens. This maps to **condition 2** (features uncorrelated with movement context) and **condition 6** (no distinguishable coordination signatures): if sagittal sequencing isn't a distinguishing feature, the "sagittal-dominant" framing is observer bias.

**Smoke status:** Cannot be evaluated empirically on synthetic data because the synthetic generator hardcodes sagittal-dominant sinusoidal kinematics — any apparent confirmation would be circular. **Empirical test requires real data.**

#### Hypothesis 2 — Trunk-sway induced lateral compensation

**Pattern claim:** Under the trunk-sway modification (lateral lean over stance leg), the support path shifts to involve increased frontal-plane pelvis motion and hip abduction-adduction; this is a *different* coordination pattern from natural walking, not a noisier version of it.

**Supporting features:**
- `pelvis_list_range_deg` — should increase under trunk-sway
- `pelvis_tilt_range_deg` — should remain similar (sagittal not perturbed)
- Hip ab/ad-duction features (NOT in current first-pass feature set — would need to be added; see Failure Analysis)
- Condition-response delta: `walking` vs `walkingTS` for each pelvis feature

**Falsification path:** If the condition-response delta is near zero across all pelvis features — i.e. walkingTS feature distributions overlap walking feature distributions — then the construct of "support path responds to trunk perturbation" weakens. Maps to **condition 6** (no distinguishable coordination signatures). If the response is large but random in direction across subjects, maps to **condition 1** (no repeatable patterns).

**Smoke status:** The synthetic generator does NOT model an actual trunk-sway perturbation differently — walkingTS in smoke is just walking with higher L/R asymmetry. So smoke output cannot test this hypothesis. **Empirical test requires real data.**

#### Hypothesis 3 — Asymmetric phase-coupling between sides

**Pattern claim:** The R-leg and L-leg support paths within a single subject differ systematically in hip-knee phase coupling, not randomly, indicating different load-transfer strategies per side rather than a single symmetric strategy.

**Supporting features:**
- `hip_knee_lag_pct_cycle` per side (per-cycle)
- Per-subject R-L delta in `hip_knee_lag_pct_cycle` aggregated across cycles
- Cross-subject distribution of the R-L delta (subjects clustering, or near zero?)

**Falsification path:** If the per-subject R-L delta has mean ≈ 0 *and* high variance across subjects, the asymmetry is random — maps to **condition 3** (random L/R asymmetry without systematic organization). If R-L delta is consistently large but the same value for every subject, it's a global bias of the measurement chain, not a coordination strategy — also weakens the construct.

**Smoke status:** The synthetic generator hardcodes a small left-side asymmetry (`left_right_asymmetry_deg`) into hip_flexion only. Smoke output cannot validate this hypothesis on real coordination data. **Empirical test requires real data.**

### Pattern Evidence Quality

- **Repeatability within trials:** Not yet evaluated on real data.
- **Consistency across participants:** Not yet evaluated.
- **Speed sensitivity:** Not testable with this dataset (no graded speeds — see §Failure Analysis).
- **Left-right organization:** Hypothesis 3 is the test surface; not yet evaluated.

### Hypothesis Strength

- **Strong evidence for clustering potential:** Not yet evaluated. Pipeline is *capable* of feeding clustering analysis (per-cycle feature table with side / condition / cycle indexing); the clustering itself is deferred to a post-friend-pre-pilot phase per protocol §Methodological Constraints.
- **Weak evidence requiring refinement:** Three hypotheses framed above; refinement = real-data evaluation against the six falsification conditions.
- **Insufficient evidence for proceeding:** With synthetic-smoke data only, the empirical evidence is *absent*, not weak. The construct cannot be tested.

## Failure Analysis

### Technical Failures

| Failure Type | Frequency | Impact | Root Cause | Mitigation |
|-------------|-----------|--------|------------|------------|
| Dataset acquisition blocked | 1 (wave-level) | Empirical validation cannot run | SimTK file download requires logged-in account; sandbox has no operator credentials | Document operator-credential dependency in protocol; cite acquisition procedure in `data/external/opencap-lab-validation.md` |
| Real-data OpenCap-vs-reference pairing unimplemented | 1 (cycle #6 debt) | AC4 not testable on real data | Pairing logic requires the unzipped archive to verify file-naming convention | Implement in follow-up cycle once archive lands |

### Data Quality Issues

| Issue | Affected Trials | Severity | Workaround | Resolution |
|-------|----------------|----------|------------|------------|
| Speed graduation absent in OpenCap Lab Validation | All (real-data, when available) | Medium | Use condition-response (natural vs trunk-sway) as the variability axis instead of speed | Backup dataset (per protocol §Backup datasets) if speed-graded analysis is later required |
| Hip ab/ad-duction features not in first-pass set | All (real-data, when available) | Low | Add to `scripts/features.py::extract_range` in a follow-up cycle once real data confirms columns exist | Trivial extension once OpenCap output column names are confirmed |

### Pipeline Bottlenecks

- **Synthetic-data validation circularity** — the smoke generator hardcodes the very patterns the hypotheses claim to test (sagittal-dominant kinematics, small L/R asymmetry). The smoke test verifies pipeline shape, not empirical validity. This is documented in the notebook's §7 self-check.
- **Hard-coded data path `/opt/gait-data/`** — single-machine assumption; a future cycle should parameterize via env var.

## Falsification Assessment

Evaluation against the 6 falsification conditions from [support-path concept](../docs/concepts/support-path.md):

| Condition | Status | Evidence | Impact |
|-----------|--------|----------|---------|
| 1. No repeatable patterns | Not testable | Synthetic data has by-construction repeatable patterns | Cannot falsify the construct on smoke; the test requires real data |
| 2. Features uncorrelated with context | Not testable | Synthetic walking and synthetic walkingTS differ by-construction in L/R asymmetry only, not in coordination structure | Cannot falsify on smoke |
| 3. Random L/R asymmetry | Not testable | Synthetic data has hardcoded systematic L-side offset | Cannot falsify on smoke |
| 4. Poor OpenCap-reference agreement | Not testable | No real OpenCap/reference pair has been compared | Comparison primitive is correct on synthetic noise; real-pair pairing is deferred |
| 5. Feature extraction consistently fails on clean data | NOT triggered | Synthetic clean data: 0% missingness, 100% seg rate | Pipeline is at least minimally competent; real-data competence not yet shown |
| 6. No distinguishable coordination signatures | Not testable | Synthetic conditions don't differ in coordination structure | Cannot falsify on smoke |

**Falsification Score:** 0 / 6 conditions triggered on smoke data. **However:** 5 of 6 conditions are not yet testable because they require empirical (non-synthetic) variation. The 0/6 score is **not** evidence that the construct survives; it is evidence that the empirical test has not yet run.

**Threshold Status:** Below 4-condition NO-GO threshold *mechanically*, but the threshold's interpretation is degraded when 5 of 6 are not testable. Real-data execution is required before any threshold-based decision is methodologically valid.

## Go/No-Go Assessment

### Criteria Evaluation

| Criterion | Smoke result | Real-data result | Pass? |
|---|---|---|---|
| Segmentation success (≥80%) | 100% | N/A | ✗ (real-data unevaluated) |
| Feature extraction success (<20% missing) | 0% missing | N/A | ✗ (real-data unevaluated) |
| OpenCap-reference agreement | N/A (primitive verified on synthetic) | N/A | ✗ (real-data unevaluated) |
| Support-path hypothesis generation (≥3) | 3 candidate hypotheses with falsification paths | N/A (cannot evaluate on smoke) | ✓ (hypothesis count) ✗ (empirical anchoring) |
| Pipeline completion without major failures | smoke run end-to-end | N/A | ✓ (pipeline shape) ✗ (real-data run) |

### Recommendation

**REVISE.**

**Reasoning:** The methodology (selection rules, processing protocol, falsification framework, GO/NO-GO criteria) is sound. The pipeline (segmentation, feature extraction, comparison, plotting) is implemented, smoke-tested, and reproducible. The blocking step is a single external dependency: SimTK requires a logged-in account for file downloads, and the operator did not supply credentials before this wave began.

REVISE rather than NO-GO because:
- NO-GO implies a fundamental construct problem; the construct has not been tested.
- REVISE names the specific gap (acquisition access mechanism), which is procedural not theoretical.

REVISE rather than GO because:
- GO requires having actually segmented real walking data and met the segmentation / extraction / agreement thresholds.
- 0% missingness on synthetic smoke data is not equivalent to <20% missingness on real OpenCap output, which has known limitations documented in `instruments/opencap/limitations.md` (segment positions are video-derived estimates, not measurements).

**Recommended revision:** Update `protocols/existing-data-zeroth-pilot.md` §Dataset Selection Rules to add an "Access mechanism" subsection covering the SimTK login dependency and any equivalent gates on backup datasets. Provide an operator-acquisition runbook (citing `data/external/opencap-lab-validation.md §Acquisition procedure`). After acquisition, re-run the pipeline; the existing pipeline + scripts module is ready to consume the archive without code changes.

## Next Phase Preparation

### If GO (after acquisition re-run) — Friend Pre-Pilot Recommendations:
- Operator runs the acquisition procedure documented in `data/external/opencap-lab-validation.md`.
- Re-execute `notebooks/existing-data-processing.ipynb`. Real-data segmentation, features, plots, and comparison populate automatically.
- Re-execute the falsification table above with real-data results.
- If 0–3 conditions trigger and ≥3 hypotheses survive: GO for friend pre-pilot.

### If REVISE (current recommendation) — Protocol Modifications:
- Add §"Access mechanism" subsection to `protocols/existing-data-zeroth-pilot.md` §Dataset Selection Rules.
- Document SimTK credential dependency in operator-facing form (where to register, how to obtain a token, what the license terms require attribution-wise).
- Consider whether `LabValidation_withoutVideos.zip` (smaller, contains processed kinematics + reference) is sufficient for the existing-data-zeroth-pilot, or whether the heavier `LabValidation_withVideos.zip` is needed (it isn't, for first-pass kinematic features).

### If NO-GO (not applicable to current run) — Fundamental Issues:
- Would only apply after a real-data run shows ≥4 of 6 falsification conditions triggered.
- Not currently the case.

## Appendices

### A. Processing Log

- 2026-05-15: Wave dispatched by δ-as-agent in single-actor collapse mode.
- Cycle #5 (1 round, APPROVE): dataset identified, manifest populated, .gitignore extended. Acquisition blocked at SimTK login. Closed at d7c7444; γ close-out at fbcfbaf.
- Cycle #6 (2 rounds, APPROVE after F1 fix): pipeline notebook + scripts module + requirements; smoke-tests pass. Closed at 8997f6f.
- Cycle #7 (this report): inference memo + field report + PROJECT.md update + REVISE decision.

### B. Quality Control Plots

Three inline figures committed in `notebooks/existing-data-processing.ipynb`:
- Hip / knee / ankle traces overlaid across cycles
- Knee-angle-R curves by condition
- Knee-range boxplot by condition

These are smoke figures, not empirical artifacts.

### C. Raw Data Statistics

`/opt/gait-data/gait-support-paths-features/features-zeroth-pilot.csv` — 52 cycles × 27 columns (smoke). Not committed (lives outside repo per `data/external/README.md`).
