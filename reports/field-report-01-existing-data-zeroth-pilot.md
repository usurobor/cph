# Field Report 01: Existing-Data Zeroth Pilot

## Overview

**Report Date:** 2026-05-17 (segmentation-fix run; supersedes the same-day 18.3%-segmentation REVISE, which superseded the 2026-05-15 acquisition-blocked REVISE)
**Protocol:** [protocols/existing-data-zeroth-pilot.md](../protocols/existing-data-zeroth-pilot.md)
**Dataset:** OpenCap Lab Validation from SimTK — **acquired and processed.** SHA-256 `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`; see [`data/external/opencap-lab-validation.md`](../data/external/opencap-lab-validation.md) §Acquisition status.
**Status:** **Decision: REVISE.** The heel-strike detector has been rewritten to handle real Mocap calcaneus dynamics; segmentation now fires on 60 / 60 walking trials (100%) for the right side. The L-side cycle count is 1 / 60 — *nonzero, AC1 mechanically passes, but a structural constraint*: the archive's IK files are cropped to ~1.3–1.5 s (≈1 stride), and the cropping aligns reliably to the R-side stance pattern but not the L-side. Hypothesis 1 (sagittal-dominant load transfer) is now evaluable on the R-side with n=60 cycles; Hypotheses 2 and 3, which require L/R pairing, are still not testable on this archive without contralateral-anchored cycle detection or a longer-trial dataset.

## Executive Summary

The prior REVISE pointed at one named bottleneck: `scripts.segmentation.detect_heel_strikes` was tuned to the synthetic generator's heel-marker shape (range ~[0, 100] mm, zero baseline) and failed on real Mocap calcaneus markers (range ~[50, 330] mm, ~25 mm R/L baseline offset). That bottleneck is closed. The new detector uses robust percentile normalization plus stance-region depth/length gating: each contiguous run of `yn < 0.30` (where `yn = (smoothed_heel − q05) / (q95 − q05)`) that lasts ≥150 ms AND reaches a deepest value `< 0.10` is one stance phase, and HS is the first sample inside that deep-stance plateau. The detector is invariant to absolute height, baseline offset, and amplitude; it works on both the unphysical synthetic stance (clipped-to-zero plateau) and the real Mocap dynamics.

**Three findings.**

1. **Segmentation now passes AC1 mechanically.** 60 / 60 trials produce ≥1 cycle (100%, R-side); 30 / 30 natural and 30 / 30 trunk-sway. All 61 cycles fall in the physiological range (0.84–1.37 s; mean 1.06 s) — no implausible short cycles, no detector noise. The smoke synthetic regenerates 7+7 = 14 cycles at the expected 1.1 s stride period.

2. **L-side cycles are structurally limited by trial cropping.** Diagnostic classification of every (trial, side) pair shows 47 sides ending in mid-swing and 12 starting in mid-swing — only one L trial is bookended cleanly enough to extract a complete L stride. This is not a detector failure (`scripts.segmentation_diagnostics.py` confirms each one's stance regions are too short or too shallow at the trial boundary to count as a HS). The OpenCap Lab Validation IK pipeline appears to crop each trial to one R-aligned stride; L strides do not align to those boundaries. Recovering L cycles would require either (a) contralateral-anchored detection (use the detected R HS times + a half-stride offset to seed L cycle bounds), or (b) re-running OpenSim IK on the source TRC files with wider time windows — both are out of scope for this bounded cycle.

3. **OpenCap-vs-reference comparison remains validated.** The AC4 numbers are unchanged from the prior run (segmentation does not gate this cell): Pearson r̄ 0.962 / 0.933 / 0.951 across HRNet / OpenPose_default / OpenPose_highAccuracy at 5-cameras × 60 trials. The technology stack is reliable for sagittal hip/knee/ankle reconstruction.

**Decision.** REVISE, not GO. AC1 mechanically passes (≥80%, L>0, both walking conditions covered), but L=1 cycle means L/R asymmetry features cannot be computed and Hypothesis 3 (asymmetric phase-coupling between sides) is not testable. Hypothesis 1 *is* evaluable on R-side data with n=60 cycles plus the validated OpenCap comparison, but the project's primary value proposition — support paths as a *bilateral* coordination construct — needs more than one side's worth of cycles to be empirically anchored. The next bounded cycle should address contralateral L-cycle recovery, not detector retune.

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
| Natural walking (real) | 30 | 30 / 30 | 30 cycles (30 R, 0 L) | **100.0%** | L-side under-detection is trial-cropping driven, not detector-driven |
| Trunk-sway walking (real) | 30 | 30 / 30 | 31 cycles (30 R, 1 L) | **100.0%** | Same |
| **Overall (real)** | **60** | **60 / 60** | **61 cycles (60 R, 1 L)** | **100.0%** | **AC1 (≥80%) PASS; L>0 PASS; nat+TS coverage PASS** |
| Synthetic smoke | 1 (8-cycle trial) | 1 / 1 | 14 cycles (7 R, 7 L) | 100% | Returns to expected 1.1 s stride period; no false-short cycles |

**Per-side cycle yield, per trial (real):** the detector emits exactly one R cycle per trial (the R stance pattern bookends every trial) and one L cycle in one trial across the whole archive (`subject9/walkingTS3`, the single trial whose L stance phases happen to align to the cropping window). Cycle durations: mean 1.06 s, min 0.84 s, max 1.37 s — all inside the adult walking norm of 0.8–1.4 s.

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
| 3. Random L/R asymmetry | **Not testable (data shape)** | L=1 cycle; no R/L pairs at matching cycle_number | Blocked on L-cycle recovery |
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

**REVISE.**

**Reasoning:** AC1 mechanically passes; the segmenter bottleneck is closed. But the project's primary value proposition (support paths as a *bilateral* coordination construct) is half-anchored: R-side has n=60 cycles ready for aggregate analysis, L-side has n=1. The next bounded blocker is L-cycle recovery — which is a *data shape* problem, not a *detector primitive* problem like the last cycle's.

REVISE rather than NO-GO because:
- AC1, AC2, AC4 all pass cleanly; AC5 reproducibility verified.
- 5 of 6 falsification conditions are not triggered or are reachable on R-side data; only condition 3 (L/R asymmetry) is blocked by data shape.
- The construct survives contact with the R-side test surface and with the technology validation.

REVISE rather than GO because:
- L=1 cycle cannot anchor the bilateral construct.
- The project's stated decision rule ("If AC1 passes and L cycles are nonzero, report whether support-path hypotheses are now testable. Do not automatically declare GO.") explicitly resists auto-GO on mechanical AC1 pass.
- The next blocker (contralateral L-cycle detection OR longer-trial capture) is a different scope from this cycle's segmenter fix; it deserves its own bounded specification.

**Recommended next bounded cycles:**

1. **Sub C aggregate analysis on R-side (n=60).** Boring-first PCA + per-condition feature distribution + Hypothesis 2 falsification test. This is the analysis the existing-data zeroth pilot was *designed* to produce; it is now reachable. If the R-side analysis itself returns clean results, the bilateral block becomes the only remaining gap.
2. **Contralateral-anchored L-cycle detection.** Use the detected R HS times + a half-stride offset to bracket the L cycle even when the L heel signal alone doesn't bookend the trial. Verify on `subject9/walkingTS3` (currently the lone L cycle) plus 5–10 other trials. AC: ≥50% of trials yield ≥1 L cycle without producing implausible cycles.
3. **OR friend pre-pilot capture protocol revision.** Specify minimum trial length (≥3 s = ≥2 full strides) so future captures are not subject to the same cropping limit as the archive.

Operator triage on which of (2) or (3) comes first.

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
- 2026-05-17 (this cycle): segmentation primitive rewritten on `cycle/segmentation-real-data-fix`. `scripts/segmentation.py::detect_heel_strikes` now uses robust-percentile normalization + stance-region depth/length gating. `scripts/segmentation_diagnostics.py` added for per-(trial, side) zero-cycle classification. `scripts/features.py::extract_range` extended with hip-adduction + lumbar features. Notebook regenerated and executed against the unchanged archive; AC1 100%, AC2 0.00% missing, AC4 unchanged. This report rewritten with the post-fix evidence and the new REVISE recommendation (L-cycle recovery, not detector retune).

### B. Quality Control Plots

Three inline figures committed in `notebooks/existing-data-processing.ipynb`, now showing real-data traces from the post-fix segmentation:

- Hip / knee / ankle traces overlaid across the 60 R-side cycles. Visibly normative gait waveforms; within-cycle variance now large enough to support distributional inspection.
- Knee-angle-R curves by condition (walking vs walkingTS) at n=30 + 30. First condition-response signal observable.
- Knee-range boxplot by condition. Same n.

### C. Raw Data Statistics

- `/opt/gait-data/opencap-lab-validation/extracted/` — 7.2 GiB, 11,141 files, 10 subjects, 4 IK sources, 60 walking trials each. SHA-256 of the archive: `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`.
- `/opt/gait-data/gait-support-paths-features/features-zeroth-pilot.csv` — 61 cycles × 35 columns (real-data). Not committed (lives outside repo per `data/external/README.md`).
- Aggregate summary at [`analysis/feature-summary-zeroth-pilot.md`](../analysis/feature-summary-zeroth-pilot.md) — auto-generated by the notebook each run; carries AC1/AC2/AC4 oracle statuses, per-source comparison numbers, archive SHA-256, and the regeneration command. Citable as a standalone evidence artifact.
