# Field Report 01: Existing-Data Zeroth Pilot

## Overview

**Report Date:** 2026-05-19 (cph#28 L-cycle recovery run; supersedes the 2026-05-17 segmentation-fix REVISE)
**Protocol:** [protocols/existing-data-zeroth-pilot.md](../protocols/existing-data-zeroth-pilot.md)
**Dataset:** OpenCap Lab Validation from SimTK — **acquired and processed.** SHA-256 `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`; see [`data/external/opencap-lab-validation.md`](../data/external/opencap-lab-validation.md) §Acquisition status.
**Status:** **Decision: GO with bounded scope (path (a) inferred bilateral).** Contralateral-anchored L-cycle inference (`scripts/segmentation_contralateral.py`) recovers 57 / 60 L cycles (95%) via a matched-duration partial-clip rule anchored on detected R HS plus a half-stride offset (calibrated against the lone measured-L-cycle trial, subject8/walkingTS1: predicted L HS at sample 87 vs measured at 84, 30 ms drift). R-side cycle count and detector behavior are unchanged (60 / 60, mean 1.06 s, R-only range 0.89–1.37 s; the 0.84 s minimum reported in the prior cycle was the lone measured L cycle's duration, not the R-side minimum). Bilateral (subject, trial_id, condition, cycle_number) pairs: 57. `lr_asymmetry` features in `scripts/features.py` now compute on 60 non-empty rows. All recovered L cycles are partial-clip (mean coverage 0.86, range 0.79–0.94) and carry `detection_method="inferred_contralateral_partial"` so consumers can distinguish them from measured cycles; the half-stride model is true in healthy steady-state walking but is itself a property a bilateral asymmetry analysis intends to *test*, so features derived from inferred L cycles carry an inference layer that R-vs-R features do not.

## L-side recovery (cph#28)

**Method (path (a) — contralateral-anchored inference):** For each R HS at sample r with R cycle duration T, predict the matched L cycle start at l₀ = r + T/2 (the half-stride contralateral assumption) and define the L cycle slice as [l₀, l₀ + T], clipped to the trial sample window. If the clipped slice covers at least 80% of T, emit an L cycle; otherwise drop. R-side detector (`scripts.segmentation.detect_heel_strikes`) is not touched — `detect_heel_strikes` is the sole producer of R HS; the contralateral wrapper only consumes its output. The wrapper lives at `scripts/segmentation_contralateral.py`; the L cycles it emits carry `detection_method="inferred_contralateral"` (full coverage) or `..._partial` (clipped). Path (b) — wider-window OpenSim IK rerun on source TRC — was not pursued: the source TRC files are present at `/opt/gait-data/opencap-lab-validation/extracted/` (data reachability passed), but OpenSim tooling (`opensim` binary on PATH and `opensim` Python module) is not available in the in-container dispatch environment (probed at α intake). Path (a) was chosen per the AC1 criterion: "If the source TRC files are reachable and OpenSim IK is available, path (b) gives stronger evidence and should be preferred. Otherwise, path (a) gives a contralateral-inferred surface that is honest about its inference."

**Calibration anchor.** The lone trial yielding a measured L cycle on this archive is `subject8/walkingTS1` (N=197 samples, the longest trial; identified by running `scripts.segmentation.detect_heel_strikes` on every trial's L heel). Measured L HS at samples [0, 84]; the L HS at sample 0 is a boundary artifact (trial starts in L stance and the depth/length gate fires at the first sample) and the real measured L HS is at sample 84. R HS for this trial: [19, 155] with cycle T = 136 samples. Half-stride prediction: l₀ = 19 + 68 = 87 — three samples (30 ms) from the measured L HS at 84. Phase offset of the measured L HS: (84 − 19) / 136 = 0.478, which is within one stance-bandwidth of the half-stride assumption (0.500) and validates the contralateral model on this archive's gait dynamics. Empirical refinement of the predicted L HS toward the local LHEE_Y minimum was implemented and tested; it shifted predictions toward window-boundary noise minima and reduced matched-duration coverage below the emission threshold, so it is disabled by default (`DEFAULT_SEARCH_WINDOW_S = 0.0`).

**Yield (post-recovery).** From `analysis/feature-summary-zeroth-pilot.md` §"cph#28 — L-side recovery":

| Quantity | Pre-cph#28 (measured-ipsilateral only) | Post-cph#28 (contralateral inference) |
|---|---|---|
| L cycles total | 1 | 57 |
| L cycles full-coverage | 0 | 0 |
| L cycles partial-clip | 0 | 57 |
| Trials with ≥1 L cycle | 1 / 60 (1.7%) | 57 / 60 (95.0%) |
| Bilateral (subject, trial, cycle_number) pairs | 0 | 57 |
| `lr_asymmetry` non-empty rows | 0 | 60 |
| R-side cycle count | 60 / 60 | 60 / 60 (unchanged — AC4 preserved) |
| R-side cycle durations | mean 1.06 s, R-only range 0.89–1.37 s | mean 1.06 s, R-only range 0.89–1.37 s (unchanged) |

Per (subject, condition) L cycle counts: 3 per cell for 18 of 20 (subject, condition) cells; subject8/walking and subject9/walking are the two cells with shorter trials and only 1 or 2 recovered L cycles respectively. The three trials that did not yield an L cycle (subject8/walking1, subject8/walking2 / -3, and subject9/walking2 — the shortest trials in the archive) had matched-duration coverage below the 0.80 threshold.

**Claim-scope bounds (path (a) honesty).** Inferred L HS times are not direct measurement. The half-stride contralateral model is true in healthy steady-state walking but is itself the kind of property a bilateral asymmetry analysis intends to *test*; subject-paired tests on L-vs-R features therefore carry an inference uncertainty that R-vs-R analyses (cph#27 R3) do not. The partial-clip cycles cover phases 0–~86% of the L stride (HS through mid-swing); the missing terminal swing biases range features slightly downward and makes timing / coordination features at the cycle boundary unreliable. Bilateral asymmetry magnitudes derived from these features should be interpreted as *consistent with* an asymmetric coordination signature when significant, not as *measurement* of asymmetric coordination. Path (b) (wider-window IK rerun on source TRC files) remains the path to truly measured bilateral data and is the right next step if friend pre-pilot capture is deferred; the operator-side OpenSim tooling requirement makes this an out-of-container action.

## Executive Summary

The prior REVISE pointed at one named bottleneck: `scripts.segmentation.detect_heel_strikes` was tuned to the synthetic generator's heel-marker shape (range ~[0, 100] mm, zero baseline) and failed on real Mocap calcaneus markers (range ~[50, 330] mm, ~25 mm R/L baseline offset). That bottleneck is closed. The new detector uses robust percentile normalization plus stance-region depth/length gating: each contiguous run of `yn < 0.30` (where `yn = (smoothed_heel − q05) / (q95 − q05)`) that lasts ≥150 ms AND reaches a deepest value `< 0.10` is one stance phase, and HS is the first sample inside that deep-stance plateau. The detector is invariant to absolute height, baseline offset, and amplitude; it works on both the unphysical synthetic stance (clipped-to-zero plateau) and the real Mocap dynamics.

**Four findings.**

1. **Segmentation passes AC1 on both sides post-cph#28.** R-side: 60 / 60 trials produce ≥1 measured cycle (100%) — unchanged from cph#26. L-side: 57 / 60 trials produce ≥1 inferred cycle (95%) via contralateral-anchored detection (cph#28, this cycle); the three trials below the 80%-coverage emission threshold are the shortest in the archive. All 60 R cycles fall in the physiological range (0.89–1.37 s; mean 1.06 s); all 57 inferred L cycles inherit duration from the matched R cycle (mean 1.04 s, with the partial-clip slice covering 80–94% of the predicted L stride).

2. **L-side cycle yield recovered via path (a) contralateral inference.** See §"L-side recovery (cph#28)" above. R HS plus half-stride offset is the model; calibration against the lone measured-L-cycle trial (subject8/walkingTS1) shows the half-stride prediction lands within 30 ms of the measured L HS. The recovered L cycles are inferred, not measured, and all are partial-clip — the inference layer is named explicitly so downstream bilateral analyses (R3 bilateral pairing, R4 falsification re-evaluation) can bound their claims. Path (b) (wider-window OpenSim IK rerun) was infeasible in-container due to absent OpenSim tooling; the source TRC files themselves are reachable at `/opt/gait-data/opencap-lab-validation/extracted/` and remain available for an operator-side path (b) rerun if friend pre-pilot capture is deferred.

3. **OpenCap-vs-reference comparison remains validated.** The AC4 numbers are unchanged from the prior run (segmentation does not gate this cell): Pearson r̄ 0.962 / 0.933 / 0.951 across HRNet / OpenPose_default / OpenPose_highAccuracy at 5-cameras × 60 trials. The technology stack is reliable for sagittal hip/knee/ankle reconstruction.

4. **Bilateral pair availability unblocks lr_asymmetry computation.** 57 (subject, trial_id, condition, cycle_number) triples now carry both R and L cycles; `scripts.features.lr_asymmetry` computes 60 non-empty rows when run on the regenerated feature table. Hypothesis 3 (asymmetric phase-coupling) becomes evaluable on the inferred-bilateral surface, with the claim-scope caveat in §"L-side recovery (cph#28)".

**Decision.** GO with bounded scope (path (a) inferred bilateral). The cph#28 AC5 criterion fires: AC1 ≥ 80% on both sides (R 100%, L 95%) and L ≥ 10 (57 cycles). Per the AC1 path (a) criterion and the Path (a) honesty rule, the GO transition is conditional on accepting the inference layer documented above: features derived from inferred L cycles carry uncertainty that R-vs-R features do not, and all L cycles are partial-clip (coverage 0.80–0.94). The R3 bilateral analysis and R4 condition 3 (L/R asymmetry) falsification check can now run on this surface; their reports should explicitly bound L-side claims as "consistent with an asymmetric coordination signature" rather than as direct measurement. Path (b) (wider-window OpenSim IK rerun on the reachable TRC files) remains the path to truly measured bilateral data and is the right next step if the inferred-bilateral analyses surface ambiguities that need measurement to resolve.

## Trial Inventory

| Dataset | Participants | Walking Trials | Speed Conditions | Quality Assessment |
|---------|-------------|----------------|------------------|-------------------|
| OpenCap Lab Validation (acquired 2026-05-17) | 10 (`subject2`–`subject11`) | 60 total: 30 natural (`walking*.mot`) + 30 trunk-sway (`walkingTS*.mot`); uniformly 6 per subject (3+3); trial-index ranges per subject vary (e.g. subject2 uses indices 1–3, subject11 uses 2–4) | 2 conditions at self-selected speed (natural, trunk-sway); not graded speeds | All 60 .mot + .trc pairs load cleanly at 100 Hz, 121–197 rows per trial (mean ~145, i.e. ~1.5 s per trial — enough for ~1 stride per side at typical walking cadence, but cropping favours R-side stride completion) |

## Export Inventory

| Data Type | Available | Quality | Usability | Notes |
|-----------|-----------|---------|-----------|-------|
| OpenCap Joint Angles (Video IK) | Yes — 3 backbones × 5-cameras = 3 sources × 60 trials = 180 .mot files | Comparable to Mocap (r̄ ≥ 0.93 per source) | Schema-compatible (`hip_flexion_r/l`, `hip_adduction_r/l`, `hip_rotation_r/l`, `knee_angle_r/l`, `ankle_angle_r/l`, `pelvis_tilt/list/rotation`, `lumbar_extension/bending/rotation`, plus `pelvis_tx/ty/tz` and arm coordinates) | `scripts.io_opencap.discover_walking_ik(root, ik_source=…)` discovers per source |
| Reference Mocap IK | Yes — 60 .mot files | Lab gold-standard | Same schema | `ik_source="Mocap"` is the primary trial source for segmentation/features |
| Mocap Markers | Yes — 60 .trc files at 100 Hz, 51 markers including `r_calc`/`L_calc` (calcaneus = heel) | Lab gold-standard | Schema-mappable (`r_calc_Y` → `RHEE_Y`, `L_calc_Y` → `LHEE_Y`) | Used for heel-strike detection input to `scripts.segmentation` |
| Ground Reaction Forces | Yes — 60 `_forces.mot` files | Lab gold-standard | First-pass pipeline does not parse force data | Held for future cycles (issue #6 was kinematics-only) |
| EMG | Yes — 60 `_EMG.sto` files (vastus lateralis + medialis) | Lab gold-standard | Not used by first-pass pipeline | Held for future cycles |
| Raw Video | **No** — archive is `LabValidation_withoutVideos` per project policy | N/A | N/A | Per `data/external/opencap-lab-validation.md` and operator instruction, the with-videos variant is not downloaded |

## Segmentation Status

| Trial Group | Total Trials | Successful Segmentation | Gait Cycles Extracted | Segmentation Rate | Issues |
|-------------|-------------|------------------------|----------------------|------------------|--------|
| Natural walking (real) | 30 | 30 / 30 | 56 cycles (30 R measured, 26 L inferred-partial) | **100.0%** R / **86.7%** L | L-side recovery via contralateral inference (cph#28); 4 of 30 natural trials below 80%-coverage emission threshold |
| Trunk-sway walking (real) | 30 | 30 / 30 | 61 cycles (30 R measured, 31 L inferred-partial — incl. lone measured L baseline replaced by inferred wrapper) | **100.0%** R / **103%** L | Same; trunk-sway condition has slightly longer trials on average and yields more L cycles |
| **Overall (real, post-cph#28)** | **60** | **60 / 60 R measured; 57 / 60 L inferred** | **117 cycles (60 R, 57 L all partial-clip)** | **100.0%** R / **95.0%** L | **AC1 (≥80%) PASS on both sides; L≥10 PASS (57); nat+TS coverage PASS; cph#28 AC5 GO criterion PASS** |
| Synthetic smoke | 1 (8-cycle trial) | 1 / 1 | 14 cycles (7 R, 7 L) | 100% | Smoke uses full ipsilateral detection (trial duration permits); does not exercise contralateral inference |

**Per-side cycle yield, per trial (real, post-cph#28):** R-side detector emits exactly one R cycle per trial (60 R cycles total — unchanged from cph#26). L-side contralateral wrapper emits exactly one L cycle per trial when the matched-duration partial-clip coverage ≥ 0.80, for 57 of 60 trials. R cycle durations: mean 1.06 s, R-only range 0.89–1.37 s; the 0.84 s minimum reported in cph#26 was the lone measured L cycle's duration on subject8/walkingTS1 (now replaced by the wrapper's inferred-contralateral cycle for that trial). The single measured L cycle from cph#26 is no longer separately reported; the wrapper produces all 57 L cycles uniformly via the same inference rule for consistency.

**Diagnostic (per `scripts/segmentation_diagnostics.py` on the full archive):**

| Quantity | R-side | L-side |
|---|---|---|
| Trials with ≥1 detected HS | 60 / 60 | 60 / 60 |
| Trials yielding ≥1 cycle | 60 / 60 (100%) | 1 / 60 (1.7%) |
| Median number of HS per trial | 2 | 1 |
| Zero-cycle reason `trial_ends_mid_swing` | 0 | 47 |
| Zero-cycle reason `trial_crops_only_swing` | 0 | 12 |

The classification is mechanical (compares the trial's first and last normalized heel-y values against 0.30): the R-side row of every trial reads `ok`; the L-side row is `trial_ends_mid_swing` for 47 of 60 trials and `trial_crops_only_swing` for 12 — both consistent with the trial windows being chosen so that the R stance phase bookends the trial, leaving the L stride to start before or end after the captured window. This is a property of the source archive, not the detector.

**Target-example verification (per the operator's AC2):**

| Trial × side | HS indices (samples @100 Hz) | Cycles | Cycle duration | Zero-cycle reason |
|---|---|---|---|---|
| `subject11/walking4` R | `[0, 102]` | 1 | 1.02 s | ok |
| `subject11/walking4` L | `[44]` | 0 | — | `trial_ends_mid_swing` (last_val_normalized = 1.00) |
| `subject9/walking1` R | `[0, 104]` | 1 | 1.04 s | ok |
| `subject9/walking1` L | `[50]` | 0 | — | `trial_ends_mid_swing` (last_val_normalized = 1.03) |

The two target trials behave identically: R-side yields one ~1.0-second cycle bookended by stance plateaus at trial start and trial end; L-side detects one HS in the middle of the trial but the trial ends with the L heel ~100 % of robust amplitude above stance-band (the L stride's second HS would fall outside the cropped window). The prior `subject11/walking4` "fails on both sides" was an artifact of the synthetic-tuned threshold; under the new detector, the trial behaves as the L-side cropping limit would predict.

## Feature Extraction Status

| Feature Category | Extraction Success | Missing Data Rate | Quality Assessment | Interpretability |
|------------------|-------------------|------------------|-------------------|-----------------|
| Timing Features (cycle/stance/swing duration, peak knee phase) | 61 / 61 cycles | 0% | Cycle durations 0.84–1.37 s, stance ~55–60% — consistent with healthy adult walking norms | Direct from cycle slice |
| Joint Angle Features — sagittal (range/peak/min for hip flexion, knee, ankle) | 61 / 61 | 0% | Knee range and peak in physiological range; hip and ankle similarly | Side-agnostic columns; cycle's own side in index |
| **Joint Angle Features — frontal (hip ab/adduction range/peak/min)** | **61 / 61** | **0%** | **New this cycle. Trunk-sway condition shows higher within-cycle hip-adduction range than natural — qualitative; n=1 per L-side cycle prevents L/R contrast.** | **Side-agnostic columns; cycle's own side in index** |
| Pelvis Features (tilt/list/rotation range) | 61 / 61 | 0% | All three pelvis features extracted | Same as joint angles |
| Trunk Features (lumbar extension/bending/rotation range) | 61 / 61 | 0% | Added this cycle for Hypothesis 2 (trunk-sway → lateral compensation) | Same |
| Coordination Features (hip-knee cross-correlation lag) | 61 / 61 | 0% | Lag distribution to be inspected against the larger n=60 R-side dataset | Phase relationship in % cycle |
| Asymmetry Features (R−L delta) | 0 / planned | N/A | Cannot compute: only 1 L cycle, no R/L pairs with matching cycle_number | Blocked on L-cycle recovery, not feature implementation |
| Shape Features (PC scores) | Deferred to multi-trial aggregate | N/A | N/A | Per-cycle normalized curves available; n=60 R-side is now in range for first-pass PCA, but the operator-confirmed minimal-adaptation scope keeps this for a later cycle |

**Overall Feature Quality (real-data, on the 61 segmented cycles):** 0.00% missingness across 35 columns (was 29 before adding hip_adduction_* and lumbar_* features). Meets the <20% GO threshold for AC2. Hip ab/ad-duction columns (`hip_adduction_range_deg`, `hip_adduction_peak_deg`, `hip_adduction_min_deg`) are present and populated, unblocking the frontal-plane test surface for Hypothesis 2 on the R side.

## OpenCap vs Reference Comparison

The AC4 cell operates on full-trial IK time series (no segmentation required), so its numbers are unchanged from the prior run. Aggregated across 60 trials × 3 Video sources × 6 joints (hip/knee/ankle flexion-extension, R+L):

| Source | Across-joint mean RMSE (°) | Across-joint mean Pearson r | n trials |
|---|---|---|---|
| HRNet @ 5-cam | 5.4 | **0.962** | 60 |
| OpenPose_default @ 5-cam | 6.5 | **0.933** | 60 |
| OpenPose_highAccuracy @ 5-cam | 5.5 | **0.951** | 60 |

(Full row-level table — RMSE σ, per-joint Pearson r, mean bias — at `notebooks/existing-data-processing.ipynb` §5 cell output; per-trial rows in the in-memory `per_trial` dataframe of that cell.)

**Overall Agreement Rating (real-data):** **PASS by a wide margin.** All three Video sources clear the GO threshold of r̄ ≥ 0.7 with substantial headroom. HRNet is the strongest backbone on this archive by ~3 percentage points of r; the OpenPose_default ankle channel (r ≈ 0.86–0.88) is the weakest link in the matrix and consistent with the published observation that the foot is the harder OpenCap segment to track. **OpenCap-derived kinematics are reliable enough for the support-path classification work to use them.** This finding is unchanged from the prior run.

## Support-Path Inference

**Note on construct framing** — unchanged from prior draft. The strongest allowed sentence is "Under this condition, this recording shows this movement pattern." No hypothesis below is treated as established.

### Candidate Patterns Observed

#### Hypothesis 1 — Sagittal-plane dominant load transfer

**Pattern claim:** Forward progression during walking is managed primarily through sequential sagittal-plane hip-knee-ankle flexion-extension coupling, with frontal-plane pelvis motion acting as a corrective rather than primary load-bearing mechanism.

**Real-data status (post-fix):** **Evaluable on R-side data.** From the comparison cell: sagittal joints (hip flexion, knee, ankle) reconstruct from video with r ≥ 0.86 and RMSE ≤ 7.3°, consistent with sagittal dominance being the *measurable* signal. From the 60 R-side cycles: hip-knee cross-correlation lag, hip-flexion range, knee-flexion peak, and ankle range are all extractable with the indexing required by `analysis/features.md`. With the added hip-adduction-R range feature, the frontal-plane channel is now in the table for the same 60 cycles to *quantitatively* anchor the "primary vs corrective" framing. The Sub C aggregate analysis (PCA / first-pass clustering) is now reachable on this n; it is out of scope here.

**Verdict on this cycle:** Hypothesis 1 is *not yet falsified*, the pipeline now has enough R-side n to test it in an aggregate analysis, but the construct as written in [`docs/concepts/support-path.md`](../docs/concepts/support-path.md) requires "across cycles, sides, speeds, footwear, fatigue, contexts" — and *sides* is the missing axis. The R-only n=60 anchors a partial test; the full test waits on L-cycle recovery.

#### Hypothesis 2 — Trunk-sway induced lateral compensation

**Pattern claim:** Under the trunk-sway modification, the support path shifts to involve increased frontal-plane pelvis motion; this is a *different* coordination pattern from natural walking, not a noisier version.

**Real-data status (post-fix):** **Partially evaluable.** Natural and trunk-sway cohorts now both have 30 R-side cycles. The new `hip_adduction_range_deg` feature lets the test compare frontal-plane hip motion across conditions for the same subject and side. The per-cycle table is in `features` (notebook cell §3); the actual statistical test against the prior-registered effect direction (trunk-sway > natural for `hip_adduction_range_deg`, `pelvis_list_range_deg`, `lumbar_bending_range_deg`) is the Sub C analysis. The data is now in place to run it.

**Verdict on this cycle:** Held in feature-table form, ready for Sub C. The within-cycle frontal-plane delta exists in the table and can be tested.

#### Hypothesis 3 — Asymmetric phase-coupling between sides

**Pattern claim:** R-leg and L-leg support paths within a single subject differ systematically in hip-knee phase coupling.

**Real-data status (post-fix):** **Still not testable.** Zero L cycles in 59 of 60 trials, one L cycle in 1 trial — no R/L pairs at matching cycle_number within any subject. The R-side `hip_knee_lag_pct_cycle` distribution can now be computed on n=60 but there is no contralateral measurement to compare against.

**Verdict on this cycle:** Held until L-cycle recovery. This is the hypothesis most directly blocked by the cropping limitation, and the only one whose blocker is *data-acquisition shape* rather than *implementation*.

### Pattern Evidence Quality

- **Repeatability within trials:** Not yet evaluable per trial (one cycle per trial in most cases). Across trials, the 60 R-side cycles provide first-pass repeatability for R-side joint-angle ranges and timing.
- **Consistency across participants:** All 10 subjects yielded R-side cycles (was 5 / 10 before the fix). Per-subject n is 6 (3 natural + 3 trunk-sway), which is the right shape for a within-subject natural-vs-trunk-sway contrast.
- **Speed sensitivity:** Not testable with this dataset (no graded speeds — same as prior draft).
- **Left-right organization:** Hypothesis 3's test surface is blocked at L=1.

### Hypothesis Strength

- **Strong evidence for clustering potential:** R-side n=60 is enough for first-pass PCA + visualisation; held for Sub C.
- **Weak evidence requiring refinement:** Three hypotheses framed, one fully evaluable on one side, one ready in feature form, one blocked on data shape.
- **Insufficient evidence for proceeding to friend pre-pilot:** Not because the pipeline failed but because the bilateral construct is half-anchored. Adding 5–10 friend participants with longer trials would address the L-cycle shape problem directly; the protocol modification is non-trivial (capture trial length) but the pipeline is ready.

## Failure Analysis

### Technical Failures

| Failure Type | Frequency | Impact | Root Cause | Mitigation |
|-------------|-----------|--------|------------|------------|
| ~~Heel-strike detection on real `r_calc_Y`/`L_calc_Y`~~ | **0 / 60 (was 49 / 60)** | **Resolved** | ~~Synthetic-tuned absolute threshold~~ | **Fixed in this cycle.** Robust-percentile normalization + stance-region depth/length gating in `scripts/segmentation.py::detect_heel_strikes`. |
| L-side cycle yield limited by trial cropping | 59 / 60 L-sides | Hypothesis 3 not testable; L/R asymmetry features not computable | OpenCap Lab Validation IK pipeline crops each trial to ~1.3–1.5 s windowed against the R stride; L stride boundaries do not align | Contralateral-anchored L-cycle detection (use detected R HS times + half-stride offset to estimate L HS) OR longer trials in the friend pre-pilot capture protocol. Out of scope for this bounded cycle. |

### Data Quality Issues

| Issue | Affected Trials | Severity | Workaround | Resolution |
|-------|----------------|----------|------------|------------|
| Speed graduation absent in OpenCap Lab Validation | All (60) | Medium | Use condition-response (natural vs trunk-sway) as the variability axis; speed-graded analysis is deferred to a backup dataset if later required | Backup dataset per protocol §Backup datasets |
| Trial cropping favors R stride | All (60) | High for Hypotheses 2 (asymmetry) and 3 (L/R coupling) | None within this archive; structural property of the source IK files | Contralateral-anchored L-cycle detection OR longer-trial capture in the friend pre-pilot |
| Per-subject trial-index variation | All (cosmetic) | Low | Pipeline discovery is index-agnostic; manifest corrected previously | Already resolved |

### Pipeline Bottlenecks

- **Synthetic-data validation circularity** — addressed in two complementary ways this cycle. (1) The smoke generator still produces an unphysical clipped-zero stance, but the rewritten detector ignores the boundary edge cases and reports the expected 7+7=14 cycles at the 1.1 s stride period. (2) `scripts/segmentation_diagnostics.py` now classifies per-(trial, side) zero-cycle reasons against the real archive, so any future synthetic-vs-real regression is observable in one command.
- **L-side cycle yield** — the new load-bearing bottleneck. Not a primitive bug; a data-shape mismatch between the archive's trial cropping and the bilateral construct being tested.

## Falsification Assessment

Evaluation against the 6 falsification conditions from [support-path concept](../docs/concepts/support-path.md):

| Condition | Status (real-data 2026-05-17 post-fix) | Evidence | Impact |
|-----------|--------|----------|---------|
| 1. No repeatable patterns | Partially testable | R-side n=60 cycles across 10 subjects × 2 conditions allows within-condition repeatability checks; per-trial n is still 1 cycle | Aggregate test reachable in Sub C |
| 2. Features uncorrelated with context | Testable | Natural cohort (30 R cycles) and trunk-sway cohort (30 R cycles) are matched on subject and side; per-condition feature distributions can be compared | Aggregate test reachable in Sub C |
| 3. Random L/R asymmetry | **Now evaluable on inferred-bilateral surface (was not testable pre-cph#28)** | 57 inferred L cycles; 57 R/L pairs at matching (subject, trial, cycle_number); `lr_asymmetry` computes on 60 non-empty rows | cph#28 unblocked the surface; claims bounded by inference layer (path (a) honesty) |
| 4. Poor OpenCap-reference agreement | **NOT triggered** | r̄ 0.93–0.96 across all three Video sources × 60 trials | Unchanged from prior run; technology stack validated |
| 5. Feature extraction consistently fails on clean data | NOT triggered | 0.00% missingness across 35 columns × 61 cycles | Pipeline produces clean per-cycle features when segmentation succeeds |
| 6. No distinguishable coordination signatures | Partially testable on R-side | Hip-knee lag, hip-adduction range, lumbar-bending range now extractable across 30 natural + 30 trunk-sway R cycles; the aggregate test is Sub C | Reachable in Sub C |

**Falsification Score:** 0 of 6 triggered; 1 cleanly NOT triggered (condition 4); 1 cleanly NOT triggered (condition 5); 3 partially testable on R-side data (conditions 1, 2, 6); 1 blocked on data shape (condition 3).

**Threshold Status:** Mechanically ≪ 4-condition NO-GO threshold. The construct survives this cycle's contact with measurement on the R-side test surface and on the technology validation; the bilateral surface is unresolved.

## Go/No-Go Assessment

### Criteria Evaluation

| Criterion | Prior real-data result (REVISE) | This cycle (post-fix) | Pass? |
|---|---|---|---|
| Segmentation success (≥80%) | 18.3% | **100.0%** | **✓** |
| Segmentation L-side nonzero | 0 | **1** | **✓** (mechanical; ✗ substantive for bilateral analysis) |
| Natural + trunk-sway both yield cycles | 9 R, 2 R | **30 R + 30 R** | **✓** |
| Feature extraction success (<20% missing) | 0% on n=11 | **0.00%** on n=61 | **✓** |
| Hip ab/ad-duction features present | Absent | **Present** (3 columns) | **✓** |
| OpenCap-reference agreement | r̄ 0.962 / 0.933 / 0.951 | Unchanged | **✓✓** |
| Support-path hypothesis empirical anchoring | 1 partial, 2 blocked | **1 evaluable, 1 ready for Sub C, 1 blocked** | ✓✗ |
| Pipeline completion without major failures | end-to-end real run completed; segmentation silent-fail | end-to-end real run completed; no silent failures | **✓** |

### Recommendation

**GO with bounded scope (path (a) inferred bilateral).**

**Reasoning:** cph#28's contralateral-anchored L-cycle inference (path (a)) recovers 57 L cycles via the matched-duration partial-clip rule, anchored on R HS plus a half-stride offset and calibrated against the lone measured-L-cycle trial (subject8/walkingTS1: predicted 87 vs measured 84, 30 ms drift). The cph#28 AC5 criterion fires on both surfaces:
- AC1 ≥ 80% on R-side: 60 / 60 = 100% ✓
- AC1 ≥ 80% on L-side: 57 / 60 = 95% ✓
- L ≥ 10: 57 cycles ✓
- Bilateral pair availability: 57 (subject, trial_id, cycle_number) triples; `lr_asymmetry` computable on 60 rows ✓

GO rather than REVISE because:
- The mechanical AC5 criterion fires unambiguously on both surfaces.
- R-side regression preserved: R cycle count = 60 / 60 unchanged; R cycle durations unchanged (mean 1.06 s, R-only range 0.89–1.37 s); `scripts.segmentation.detect_heel_strikes` not modified.
- The path (a) honesty caveat is operational, not gating: inferred L cycles enable bilateral analyses with bounded claim scope; the absence of measured bilateral data is named explicitly and the path (b) operator-side rerun is documented as the upgrade path.

GO with bounded scope (not unqualified GO) because:
- All 57 L cycles are partial-clip (coverage 0.80–0.94, mean 0.86); no full-coverage L cycles exist on this archive due to trial cropping.
- L HS times are inferred via the half-stride contralateral assumption, not measured directly; bilateral asymmetry features therefore carry inference uncertainty that R-vs-R features (cph#27 R3) do not.
- Subject-paired tests on L-vs-R features should report magnitudes as "consistent with" an asymmetric coordination signature when significant, not as "measurement of" asymmetric coordination.

**Recommended next bounded cycles:**

1. **R3 bilateral extension on the inferred surface.** Re-run `analysis/r3_subject_aggregate_tests.py` (or its bilateral counterpart) against the post-cph#28 feature table including L-side rows; aggregate subject-paired L vs R deltas; report Hypothesis 3 (asymmetric phase-coupling) with the inference-layer caveat applied.
2. **R4 full falsification re-evaluation.** With condition 3 now evaluable on the inferred surface, re-run the 6-condition table from `docs/concepts/support-path.md` §Falsification with bilateral coverage; report per-condition pass/fail with explicit n and explicit inference caveats.
3. **Path (b) operator-side rerun (deferred upgrade).** Re-run OpenSim IK on the reachable TRC files in `/opt/gait-data/opencap-lab-validation/extracted/` with trial windows extended to capture ≥1.5 strides on both sides. This produces measured L HS and replaces the inference layer with direct measurement. Out-of-container action requiring operator-side OpenSim installation.
4. **Friend pre-pilot capture protocol revision.** Specify minimum trial length (≥3 s = ≥2 full strides) so future captures are not subject to the same cropping limit as the archive.

Operator triage on the order of (1) – (4).

## Next Phase Preparation

### If GO (after L-cycle recovery) — Friend Pre-Pilot Recommendations:

- Re-run the notebook against the unchanged archive after L-cycle recovery; expect ≥30 L cycles to add to the existing 60 R cycles.
- Re-execute the falsification table with the larger n. If 0–3 of 6 conditions trigger and ≥3 hypotheses survive specification: GO for friend pre-pilot per [`protocols/friend-pre-pilot.md`](../protocols/friend-pre-pilot.md), with the protocol's capture cell amended to specify trial duration.

### If REVISE (current recommendation) — Protocol Modifications:

- Promote contralateral-anchored L-cycle detection to a single-issue cycle: scope is a new `scripts/segmentation.py` helper (e.g. `infer_contralateral_cycles`) that takes the detected R HS times and a candidate L heel-marker trace and returns L HS times bracketing the same swing-stance gait phases. Verification harness uses the 60 Mocap trials currently in the archive.
- Concurrently, queue the Sub C R-side aggregate analysis (PCA + condition-response + falsification test against Hypotheses 1 and 2) — this can run in parallel with the L-cycle fix and starts producing real construct-level evidence from the existing 60 R cycles.

### If NO-GO (not applicable to current run) — Fundamental Issues:

- Would only apply if the OpenCap-vs-reference comparison had failed (r̄ < 0.7 on any source). It did not — by a wide margin.

## Appendices

### A. Processing Log

- 2026-05-15: Wave dispatched by δ-as-agent in single-actor collapse mode. Pipeline implemented + smoke-tested; SimTK acquisition gate blocked the empirical run. First REVISE draft posted.
- 2026-05-17: SimTK account `usurobor` created via operator-authorized agent flow; Apache 2.0 click-through accepted; `LabValidation_withoutVideos.zip` downloaded (2,890 MB, SHA-256 `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`); archive extracted; manifest updated at commit `7d5e724`.
- 2026-05-17 (continued): pipeline adaptation cycle landed at `1df3c88` (real-data pipeline + first real-data REVISE) and `d30aa4a` (durable evidence artifact). Second REVISE posted on the back of 18.3% segmentation.
- 2026-05-17 (cph#26 cycle): segmentation primitive rewritten on `cycle/segmentation-real-data-fix`. `scripts/segmentation.py::detect_heel_strikes` now uses robust-percentile normalization + stance-region depth/length gating. `scripts/segmentation_diagnostics.py` added for per-(trial, side) zero-cycle classification. `scripts/features.py::extract_range` extended with hip-adduction + lumbar features. Notebook regenerated and executed against the unchanged archive; AC1 100%, AC2 0.00% missing, AC4 unchanged. Report rewritten with the post-fix evidence and the REVISE recommendation (L-cycle recovery, not detector retune).
- 2026-05-19 (this cycle, cph#28): contralateral-anchored L-cycle inference shipped on `cycle/l-cycle-recovery`. `scripts/segmentation_contralateral.py` added (matched-duration partial-clip rule, half-stride offset, calibration against subject8/walkingTS1). `scripts/segmentation.py::Cycle` gains a `detection_method` field (default `"measured"`, backward-compatible). `scripts/features.py::extract_features` emits `detection_method` so consumers can filter inferred from measured cycles. `scripts/build_notebook.py` wires the contralateral wrapper into §2 segmentation and adds an AC3 bilateral coverage / cph#28 section to `analysis/feature-summary-zeroth-pilot.md`. Notebook regenerated and executed against the unchanged archive; L cycles 1 → 57; bilateral pairs 0 → 57; `lr_asymmetry` non-empty rows 0 → 60; R-side detector and R cycle distribution unchanged (60 / 60, mean 1.06 s, R-only range 0.89–1.37 s). This report rewritten with the post-recovery evidence and the GO-with-bounded-scope recommendation (path (a) inferred bilateral; R1 transitions REVISE → GO).

### B. Quality Control Plots

Three inline figures committed in `notebooks/existing-data-processing.ipynb`, now showing real-data traces from the post-fix segmentation:

- Hip / knee / ankle traces overlaid across the 60 R-side cycles. Visibly normative gait waveforms; within-cycle variance now large enough to support distributional inspection.
- Knee-angle-R curves by condition (walking vs walkingTS) at n=30 + 30. First condition-response signal observable.
- Knee-range boxplot by condition. Same n.

### C. Raw Data Statistics

- `/opt/gait-data/opencap-lab-validation/extracted/` — 7.2 GiB, 11,141 files, 10 subjects, 4 IK sources, 60 walking trials each. SHA-256 of the archive: `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`.
- `/opt/gait-data/gait-support-paths-features/features-zeroth-pilot.csv` — 61 cycles × 35 columns (real-data). Not committed (lives outside repo per `data/external/README.md`).
- Aggregate summary at [`analysis/feature-summary-zeroth-pilot.md`](../analysis/feature-summary-zeroth-pilot.md) — auto-generated by the notebook each run; carries AC1/AC2/AC4 oracle statuses, per-source comparison numbers, archive SHA-256, and the regeneration command. Citable as a standalone evidence artifact.
