# Field Report 01: Existing-Data Zeroth Pilot

## Overview

**Report Date:** 2026-05-17 (real-data run; supersedes the 2026-05-15 blocked-on-acquisition draft)
**Protocol:** [protocols/existing-data-zeroth-pilot.md](../protocols/existing-data-zeroth-pilot.md)
**Dataset:** OpenCap Lab Validation from SimTK — **acquired and processed.** SHA-256 `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`; see [`data/external/opencap-lab-validation.md`](../data/external/opencap-lab-validation.md) §Acquisition status.
**Status:** **Decision: REVISE.** Pipeline ran end-to-end against the real archive. The OpenCap-vs-reference comparison passes its threshold by a large margin (Pearson r̄ 0.93–0.96 across all three Video backbones), validating the OpenCap technology on the same population. The gait-cycle segmentation primitive is the load-bearing failure: it fires on only 18.3% of trials, never on the left side. That is the specific gap to close before this pilot can render a clean GO/NO-GO.

## Executive Summary

The 2026-05-15 draft of this report stopped at the SimTK acquisition gate. That gate has now cleared. The archive (60 walking trials, 10 subjects, 2 conditions — see `data/external/opencap-lab-validation.md`) was downloaded, extracted, and run through the existing pipeline with minimal adaptation: the discovery layer was rewritten to find `OpenSimData/Mocap/IK/*.mot` paired with `MarkerData/Mocap/*.trc`, calcaneus marker columns `r_calc_Y`/`L_calc_Y` were renamed to the `RHEE_Y`/`LHEE_Y` convention the segmentation code expects, and the OpenCap-vs-reference comparison cell now pairs each Mocap IK against the three Video IK backbones (HRNet, OpenPose_default, OpenPose_highAccuracy) at the 5-camera setup headlined by Uhlrich et al. 2023.

**Three findings.**

1. **OpenCap validation reproduces.** Pearson r̄ across hip/knee/ankle is 0.962 (HRNet), 0.933 (OpenPose_default), 0.951 (OpenPose_highAccuracy); mean RMSE 4.7–7.3° per joint per source, well inside the paper's 3–8° headline range. AC4 passes its threshold (r̄ ≥ 0.7) for every source. **The OpenCap technology works as the paper claims on the same population this project would use.**

2. **Gait-cycle segmentation fails on real Mocap heel-marker data.** 11 of 60 walking trials yielded ≥1 cycle (18.3%) — below the 60% NO-GO threshold. Of the 11 successful detections, **all are right-side; zero left-side cycles were extracted across the entire archive.** Smoke synthetic data ran at 100%; the regression is on real data only. Root cause is a fit problem in `scripts.segmentation.detect_heel_strikes` — the real calcaneus marker has a different scale and asymmetric R/L mean than the synthetic generator (real R: range ~[50, 330] mm, mean ~120; real L: same range, mean ~150 — the ~25 mm asymmetric offset is consistent across subjects and interacts with the detector's smoothed-threshold logic to knock out every L attempt).

3. **The construct cannot yet be tested, but the technology can.** Hypothesis 2 (trunk-sway → frontal-plane response) and Hypothesis 3 (asymmetric phase-coupling) both need cycle-level data across many trials and *both* sides. With 11 R-side cycles and no L-side cycles, neither is empirically evaluable. Hypothesis 1 (sagittal-dominant load transfer) can be partially examined from the comparison data alone — the four-source comparison shows sagittal joints (hip flexion, knee, ankle) are well-recovered, which is consistent with sagittal-plane dominance but not a test of it (the comparison is OpenCap vs Mocap, not movement vs predicted load pattern).

REVISE rather than NO-GO because the failure is procedural (a detector primitive) and the rest of the pipeline (loading, IK parsing, feature extraction, comparison, plotting) is real-data-ready. REVISE rather than GO because the construct hasn't been tested. The recommended revision is bounded: tune `detect_heel_strikes` against real Mocap calcaneus dynamics (per-side baseline subtraction, percentile-of-range thresholding, or switching to a derivative-zero-crossing detector). Estimated one cycle.

## Trial Inventory

| Dataset | Participants | Walking Trials | Speed Conditions | Quality Assessment |
|---------|-------------|----------------|------------------|-------------------|
| OpenCap Lab Validation (acquired 2026-05-17) | 10 (`subject2`–`subject11`) | 60 total: 30 natural (`walking*.mot`) + 30 trunk-sway (`walkingTS*.mot`); uniformly 6 per subject (3+3); trial-index ranges per subject vary (e.g. subject2 uses indices 1–3, subject11 uses 2–4) | 2 conditions at self-selected speed (natural, trunk-sway); not graded speeds | All 60 .mot + .trc pairs load cleanly at 100 Hz, 121–197 rows per trial (mean ~145, i.e. ~1.5 s per trial — enough for 1–2 strides per side at typical walking cadence) |

**Notes.** Per-subject trial-index variation was missed in the 2026-05-15 acquisition manifest and corrected in the same commit cycle as this report — see manifest §Walking Trials Identified. The "6 per subject" count was confirmed by counting EMG-data files per subject and is consistent across the 10 subjects.

## Export Inventory

| Data Type | Available | Quality | Usability | Notes |
|-----------|-----------|---------|-----------|-------|
| OpenCap Joint Angles (Video IK) | Yes — 3 backbones × 5-cameras = 3 sources × 60 trials = 180 .mot files | Comparable to Mocap (r̄ ≥ 0.93 per source) | Schema-compatible (`hip_flexion_r/l`, `knee_angle_r/l`, `ankle_angle_r/l`, `pelvis_tilt/list/rotation`, plus `pelvis_tx/ty/tz` and arm/lumbar coordinates) | `scripts.io_opencap.discover_walking_ik(root, ik_source=…)` discovers per source |
| Reference Mocap IK | Yes — 60 .mot files | Lab gold-standard | Same schema | `ik_source="Mocap"` is the primary trial source for segmentation/features |
| Mocap Markers | Yes — 60 .trc files at 100 Hz, 51 markers including `r_calc`/`L_calc` (calcaneus = heel) | Lab gold-standard | Schema-mappable (`r_calc_Y` → `RHEE_Y`, `L_calc_Y` → `LHEE_Y`) | Used for heel-strike detection input to `scripts.segmentation` |
| Ground Reaction Forces | Yes — 60 `_forces.mot` files | Lab gold-standard | First-pass pipeline does not parse force data | Held for future cycles (issue #6 was kinematics-only) |
| EMG | Yes — 60 `_EMG.sto` files (vastus lateralis + medialis) | Lab gold-standard | Not used by first-pass pipeline | Held for future cycles |
| Raw Video | **No** — archive is `LabValidation_withoutVideos` per project policy | N/A | N/A | Per `data/external/opencap-lab-validation.md` and operator instruction, the with-videos variant is not downloaded |

## Segmentation Status

| Trial Group | Total Trials | Successful Segmentation | Gait Cycles Extracted | Segmentation Rate | Issues |
|-------------|-------------|------------------------|----------------------|------------------|--------|
| Natural walking (real) | 30 | 9 / 30 | 9 cycles (all R) | **30.0%** | Heel-strike detector fails on left calcaneus channel across all subjects; right-side detection itself fires only on ~1/3 of trials |
| Trunk-sway walking (real) | 30 | 2 / 30 | 2 cycles (all R) | **6.7%** | Same primitive failure; trunk-sway perturbation does not change the marker dynamics enough to recover detection |
| **Overall (real)** | **60** | **11 / 60** | **11 cycles, R-only** | **18.3%** | **NO-GO threshold (<60%) triggered** |
| Synthetic smoke (historic, for contrast) | 4 | 4 / 4 | 52 cycles | 100% | None — but the smoke generator hardcodes the very heel-marker shape the detector targets, so this is a tautology, not an independent validation |

**Per-subject distribution of the 11 successful detections** (only subjects with ≥1 cycle listed):

| Subject | Natural cycles (R) | Trunk-sway cycles (R) | L-side (any condition) |
|---|---|---|---|
| subject5 | 0 | 1 | 0 |
| subject7 | 3 | 0 | 0 |
| subject8 | 2 | 1 | 0 |
| subject9 | 2 | 0 | 0 |
| subject10 | 1 | 0 | 0 |
| subjects 2, 3, 4, 6, 11 | 0 | 0 | 0 |

**Diagnostic (data evidence supporting the REVISE):**

| Quantity | R-side | L-side |
|---|---|---|
| Calcaneus-Y range (mm, across sampled subjects) | ~[45–63, 295–350] | ~[50–66, 300–347] |
| Calcaneus-Y mean (mm) | ~100–125 | ~130–155 |
| Detector firing rate | 11 / 60 (18%) | 0 / 60 (0%) |

The roughly constant ~25–30 mm R/L mean offset (likely the subject's preferred-leg standing posture and the marker-mount geometry differing slightly between feet) is enough to push the L-side trace past whatever absolute threshold the smoothed-detector cascade is using in `detect_heel_strikes`. The fix is not algorithmically deep — per-side detrending or a percentile-of-range threshold — but it is out of scope for the operator-confirmed minimal-adaptation scope of this cycle, and it is the lone blocker for empirical evaluation of the construct.

## Feature Extraction Status

| Feature Category | Extraction Success | Missing Data Rate | Quality Assessment | Interpretability |
|------------------|-------------------|------------------|-------------------|-----------------|
| Timing Features (cycle/stance/swing duration, peak knee phase) | 11/11 cycles | 0% | Cycle durations 1.01–1.32 s, stance ~55–60% — consistent with healthy adult walking norms | Direct from cycle slice |
| Joint Angle Features (range/peak/min for hip flexion, knee, ankle) | 11/11 cycles | 0% | Knee range and peak in physiological range; hip and ankle similarly | Side-agnostic columns; cycle's own side in index |
| Pelvis Features (tilt/list/rotation range) | 11/11 cycles | 0% | All three pelvis features extracted | Same as joint angles |
| Coordination Features (hip-knee cross-correlation lag) | 11/11 cycles | 0% | Lag 12.5–15.4% of cycle on R side — narrow distribution, plausible normative range | Phase relationship in % cycle |
| Asymmetry Features (R-L delta) | 0 / planned | N/A | Cannot compute: zero L cycles | Blocked on segmenter fix |
| Shape Features (PC scores) | Deferred to multi-trial aggregate | N/A | N/A | Per-cycle normalized curves available but n=11 is too small |

**Overall Feature Quality (real, on the 11 segmented cycles):** 0.00% missingness across 29 columns. Meets <20% GO threshold *on the cycles that segmented*. The unanswered question — does the same hold across the missing 49 trials and the missing left side — depends entirely on the segmenter fix.

## OpenCap vs Reference Comparison

Aggregated across the 60 trials in the archive (no segmentation required for this cell; it operates on full-trial IK time series). Each row is one (Video IK source, joint) pair averaged across 60 trials.

| Source | Joint | Mean RMSE (°) | RMSE σ (°) | Mean Pearson r | r σ | Mean bias (°) | n trials |
|---|---|---|---|---|---|---|---|
| HRNet @ 5-cam | hip_flexion_r | 5.36 | 3.10 | 0.984 | 0.011 | +1.25 | 60 |
| HRNet @ 5-cam | hip_flexion_l | 6.22 | 2.83 | 0.985 | 0.011 | +0.65 | 60 |
| HRNet @ 5-cam | knee_angle_r | 4.67 | 1.98 | 0.983 | 0.013 | −0.11 | 60 |
| HRNet @ 5-cam | knee_angle_l | 4.75 | 1.48 | (similar high) | — | — | 60 |
| HRNet @ 5-cam | ankle_angle_r | 5.20 | 1.76 | — | — | — | 60 |
| HRNet @ 5-cam | ankle_angle_l | 6.06 | 1.62 | — | — | — | 60 |
| **HRNet — across-joint mean** | — | **5.4** | — | **0.962** | — | — | 60 |
| OpenPose_default @ 5-cam | hip_flexion_r | 6.34 | 2.58 | 0.970 | 0.018 | +1.36 | 60 |
| OpenPose_default @ 5-cam | hip_flexion_l | 7.19 | 2.42 | 0.947 | 0.038 | +1.21 | 60 |
| OpenPose_default @ 5-cam | knee_angle_r | 7.31 | 2.30 | 0.967 | 0.025 | −2.71 | 60 |
| OpenPose_default @ 5-cam | knee_angle_l | 6.95 | 1.55 | 0.970 | 0.021 | −1.72 | 60 |
| OpenPose_default @ 5-cam | ankle_angle_r | 5.05 | 1.38 | 0.861 | 0.075 | +2.20 | 60 |
| OpenPose_default @ 5-cam | ankle_angle_l | 6.37 | 1.62 | 0.882 | 0.092 | +3.48 | 60 |
| **OpenPose_default — across-joint mean** | — | **6.5** | — | **0.933** | — | — | 60 |
| OpenPose_highAccuracy @ 5-cam | hip_flexion_l | 5.12 | 1.29 | 0.927 | 0.046 | +3.43 | 60 |
| OpenPose_highAccuracy @ 5-cam | knee_angle_l | (similar to default) | — | — | — | — | 60 |
| OpenPose_highAccuracy @ 5-cam | ankle_angle | (similar) | — | — | — | — | 60 |
| **OpenPose_highAccuracy — across-joint mean** | — | **5.8** | — | **0.951** | — | — | 60 |

(Full row-level table at `notebooks/existing-data-processing.ipynb` §5 cell output; per-trial rows in the in-memory `per_trial` dataframe of that cell.)

**Overall Agreement Rating (real-data):** **PASS by a wide margin.** All three Video sources clear the GO threshold of r̄ ≥ 0.7 with substantial headroom. HRNet is the strongest backbone on this archive by ~3 percentage points of r; the OpenPose_default ankle channel (r ≈ 0.86–0.88) is the weakest link in the matrix and consistent with the published observation that the foot is the harder OpenCap segment to track. **OpenCap-derived kinematics are reliable enough for the support-path classification work to use them.** This is the single most load-bearing real-data finding for the project's go/no-go on the technology stack.

## Support-Path Inference

**Note on construct framing** — unchanged from prior draft. The strongest allowed sentence is "Under this condition, this recording shows this movement pattern." No hypothesis below is treated as established.

### Candidate Patterns Observed

#### Hypothesis 1 — Sagittal-plane dominant load transfer

**Pattern claim:** Forward progression during walking is managed primarily through sequential sagittal-plane hip-knee-ankle flexion-extension coupling, with frontal-plane pelvis motion acting as a corrective rather than primary load-bearing mechanism.

**Real-data status:** **Partially evaluable.** From the comparison cell: the sagittal joints (hip flexion, knee, ankle) all reconstruct from video with r ≥ 0.86 and RMSE ≤ 7.3°, consistent with sagittal dominance being the *measurable* signal. From the 11 successful cycles: hip-knee cross-correlation lag is 12.5–15.4% of cycle, narrow distribution — *suggestive* of repeated sagittal coupling but n=11 is too small to claim. From the falsification side, `pelvis_list_range_deg` was extracted on all 11 cycles; the within-cycle frontal-plane range is small relative to hip flexion range, which is consistent with the construct but does not exclude that the frontal channel carries information at longer time scales.

**Verdict on this cycle:** Hypothesis 1 is *not yet falsified* and *partially consistent* with the comparison and the per-cycle data, but n=11 right-side-only cycles cannot test "across cycles, sides, speeds, footwear, fatigue, contexts" as required by [`docs/concepts/support-path.md`](../docs/concepts/support-path.md). **Empirical claim is held in reserve until the segmenter is fixed.**

#### Hypothesis 2 — Trunk-sway induced lateral compensation

**Pattern claim:** Under the trunk-sway modification, the support path shifts to involve increased frontal-plane pelvis motion; this is a *different* coordination pattern from natural walking, not a noisier version.

**Real-data status:** **Not testable.** Only 2 of 30 trunk-sway trials yielded a cycle (6.7%); both are right-side, both from different subjects. There is no within-subject natural-vs-trunk-sway pairing in the segmented set. Even on the comparison data, there is no evidence the OpenCap pipeline systematically degrades on trunk-sway trials (a separate concern that would have justified a NO-GO if true).

**Verdict on this cycle:** Held until segmenter fix.

#### Hypothesis 3 — Asymmetric phase-coupling between sides

**Pattern claim:** R-leg and L-leg support paths within a single subject differ systematically in hip-knee phase coupling.

**Real-data status:** **Not testable.** Zero L-side cycles extracted across the whole archive. The R-side `hip_knee_lag_pct_cycle` distribution (12.5–15.4%) is plausible but there is no contralateral measurement to compare against.

**Verdict on this cycle:** Held until segmenter fix. This is the hypothesis most directly blocked.

### Pattern Evidence Quality

- **Repeatability within trials:** Not yet evaluable (single cycle per successful trial in most cases).
- **Consistency across participants:** 5 of 10 subjects yielded at least one R-side cycle; 5 yielded none. The 5-vs-5 split appears uncorrelated with subject demographics in the brief check (no obvious height/weight/age pattern in the failed subjects) and is more plausibly explained by trial-by-trial heel-marker noise + the detector's sensitivity to the per-side mean offset described in §Segmentation Status.
- **Speed sensitivity:** Not testable with this dataset (no graded speeds — same as prior draft).
- **Left-right organization:** Hypothesis 3's test surface is blocked at zero L-side cycles.

### Hypothesis Strength

- **Strong evidence for clustering potential:** Cannot evaluate at n=11 cycles. The pipeline is *capable* of feeding clustering analysis (per-cycle feature table with proper subject/side/condition indexing) but the cycle count is insufficient.
- **Weak evidence requiring refinement:** Three hypotheses framed, one partially evaluable, two blocked.
- **Insufficient evidence for proceeding:** With segmenter at 18%, the empirical evidence is *too sparse*, not *absent*. This is a different finding from the 2026-05-15 draft, which had the evidence as *absent*.

## Failure Analysis

### Technical Failures

| Failure Type | Frequency | Impact | Root Cause | Mitigation |
|-------------|-----------|--------|------------|------------|
| Heel-strike detection on real `r_calc_Y`/`L_calc_Y` | 49 / 60 trials on R, 60 / 60 on L | AC1 NO-GO triggered; AC2/AC3 reduced to n=11 | `detect_heel_strikes` uses parameters fit to the synthetic generator (heel marker baseline near 0, peak ~100, no per-side mean offset); real Mocap data has baseline ~50 mm, peak ~330 mm, and ~25 mm R/L mean offset | Tune detector against real heel dynamics: per-side mean subtraction + percentile-of-range threshold + revisit smoothing-window size. Estimated one cycle. |
| Trunk-sway condition particularly affected | 2 / 30 trials | Hypothesis 2 cannot be empirically separated from natural-walking on this run | Same primitive failure; trunk-sway likely makes the heel signal more variable | Same fix as above (the symptom subsides once the underlying detector tolerates real-data variability) |

### Data Quality Issues

| Issue | Affected Trials | Severity | Workaround | Resolution |
|-------|----------------|----------|------------|------------|
| Speed graduation absent in OpenCap Lab Validation | All (60) | Medium | Use condition-response (natural vs trunk-sway) as the variability axis; speed-graded analysis is deferred to a backup dataset if later required | Backup dataset per protocol §Backup datasets |
| Hip ab/ad-duction features not in first-pass set | All (real-data, when available) | Low | Documented as known debt in `notebooks/existing-data-processing.ipynb` §7 Known debt; not in this cycle's minimal-adaptation scope | Add to `scripts/features.py::extract_range` in a follow-up cycle |
| Per-subject trial-index variation (e.g., subject11 uses walking{2,3,4}) | All (cosmetic) | Low | Pipeline discovery is now index-agnostic (looks for `walking*.mot`); manifest §Walking Trials Identified corrected in the same commit cycle | Already resolved |

### Pipeline Bottlenecks

- **Synthetic-data validation circularity** — historical concern. The 2026-05-15 draft flagged this as a debt; the 2026-05-17 real-data run is the resolution evidence. The synthetic smoke result (100% segmentation) being wildly inconsistent with the real-data result (18%) **is precisely the kind of finding that justifies the "boring first" / real-data-first protocol policy.**
- **Heel-strike detector specific to synthetic-marker dynamics** — new bottleneck surfaced by the real-data run; documented above as the load-bearing REVISE target.

## Falsification Assessment

Evaluation against the 6 falsification conditions from [support-path concept](../docs/concepts/support-path.md):

| Condition | Status (real-data 2026-05-17) | Evidence | Impact |
|-----------|--------|----------|---------|
| 1. No repeatable patterns | Not testable | Only 11 cycles, mostly one per trial — cannot test within-trial repeatability | Blocked on segmenter |
| 2. Features uncorrelated with context | Not testable | Trunk-sway cycle count (n=2) too small to compare against natural cycle count (n=9) | Blocked on segmenter |
| 3. Random L/R asymmetry | Not testable | Zero L cycles | Blocked on segmenter |
| 4. Poor OpenCap-reference agreement | **NOT triggered** | r̄ 0.93–0.96 across all three Video sources × 60 trials | **The strongest single positive empirical signal of this cycle.** The comparison primitive works; the OpenCap technology validates on this archive. |
| 5. Feature extraction consistently fails on clean data | **Partially triggered** | On the 49 trials where segmentation gave 0 cycles, feature extraction is by definition 0/0 = vacuous; on the 11 segmented cycles, feature extraction is 0.00% missing. So the failure is segmentation, not feature extraction *per se* — but the practical effect on AC2 is the same | The construct itself is not falsified by this; the *pipeline implementation* is. |
| 6. No distinguishable coordination signatures | Not testable | Same reason as 1–3 | Blocked on segmenter |

**Falsification Score:** 0 of 6 cleanly triggered; 1 partially (condition 5, via the segmenter); 4 not testable due to cycle scarcity; 1 cleanly NOT triggered (condition 4 — the OpenCap-vs-reference, which is the load-bearing technology check).

**Threshold Status:** Below the 4-condition NO-GO threshold mechanically, but the threshold's interpretation is degraded for the same reason as in the 2026-05-15 draft — 4 of 6 conditions are not testable at n=11 cycles. The mechanical "below threshold" is *not* construct-survival evidence. The genuine new evidence is **condition 4 cleanly cleared**, which is necessary but not sufficient for any later GO.

## Go/No-Go Assessment

### Criteria Evaluation

| Criterion | Smoke result (2026-05-15) | Real-data result (2026-05-17) | Pass? |
|---|---|---|---|
| Segmentation success (≥80%) | 100% | **18.3%** | ❌ NO-GO threshold (<60%) triggered |
| Feature extraction success (<20% missing) | 0% missing on n=52 | 0.00% missing on n=11 | ✓ on the segmented cycles; vacuous on the missing trials |
| OpenCap-reference agreement | N/A (smoke compared self-vs-self+noise) | r̄ 0.962 / 0.933 / 0.951 across three Video sources × 60 trials | ✓✓ |
| Support-path hypothesis generation (≥3) | 3 framed | 3 retained; 1 partially evaluable, 2 blocked | ✓ count; ✗ empirical anchoring for 2 of 3 |
| Pipeline completion without major failures | end-to-end smoke ran | end-to-end real run completed without errors; segmentation primitive fails silently (returns 0 cycles, doesn't crash) | ✓ shape; ✗ behaviour |

### Recommendation

**REVISE.**

**Reasoning:** The 2026-05-15 draft of this report was REVISE for *acquisition* reasons. That gap closed: the archive is downloaded, extracted, and the pipeline ran end-to-end. The new REVISE is for a *specific implementation gap* — `scripts.segmentation.detect_heel_strikes` is tuned to the synthetic generator's heel-marker dynamics and does not generalise to real Mocap calcaneus data. The rest of the pipeline (discovery, IK parsing, marker pairing, feature extraction, comparison, plotting, persistence) is real-data-ready.

REVISE rather than NO-GO because:
- NO-GO implies a construct problem; the construct is now *partially* testable (Hypothesis 1) and *blocked but specific* for the other two. The block is not theoretical.
- The OpenCap-vs-reference comparison cleanly validates the technology stack the project is built on. That removes the largest single risk from the 2026-05-15 draft.

REVISE rather than GO because:
- 18.3% segmentation on the right side and 0% on the left is too sparse to credibly evaluate the support-path construct, even though the technology stack is validated.
- The construct has not been tested.

**Recommended revision (bounded; one cycle):**

1. Replace `detect_heel_strikes`'s absolute-threshold/smoothed-crossing detector with a robust per-side approach: subtract per-trial heel-marker baseline (e.g. lowest 5th percentile = stance-foot level), then detect strikes as falling-edge zero-crossings of the residual or as troughs below a percentile-of-range threshold. Verify against `walking4` of subject11 (currently failing on both sides) and `walking1` of subject9 (currently passing on R only). Re-run the notebook; expect ≥80% segmentation across both sides if the diagnosis above is correct.
2. While in this cycle, add hip ab/ad-duction features to `scripts/features.py::extract_range` (the column convention is already known from the OpenSim coordinate set in the real .mot files: `hip_adduction_r`, `hip_adduction_l`). This unblocks Hypothesis 2's falsification path.
3. Re-execute the existing-data zeroth pilot. Re-evaluate the falsification table.

After that, the next phase gate (friend pre-pilot) is reachable if Hypotheses 1–3 stand up.

## Next Phase Preparation

### If GO (after segmenter fix) — Friend Pre-Pilot Recommendations:

- The segmenter fix is the only known blocker. Re-run `notebooks/existing-data-processing.ipynb` against the unchanged archive after the fix; expect 60+ trials × 2 sides ≈ ≥120 cycles (typical ~3 cycles per trial × 60 trials × 2 sides ≈ 360 cycles upper bound).
- Re-execute the falsification table with the larger n. If 0–3 of 6 conditions trigger and ≥3 hypotheses survive specification: GO for friend pre-pilot per `protocols/friend-pre-pilot.md`.

### If REVISE (current recommendation) — Protocol Modifications:

- Promote the segmenter fix to a single-issue cycle: scope is `scripts/segmentation.py::detect_heel_strikes` + verification harness using the 60 Mocap heel-marker trials currently in the archive.
- Add hip ab/ad-duction features (small extension of `scripts/features.py::extract_range`).
- Optionally: parameterize the smoke-test generator to *not* hardcode the easy detection pattern — the most valuable lesson of this real-data run is that the synthetic smoke gave a false-positive on AC1 and a tautological pass on AC4. Smoke that matches the difficulty of real data would catch this class of bug before the real-data cycle.

### If NO-GO (not applicable to current run) — Fundamental Issues:

- Would only apply if the OpenCap-vs-reference comparison had failed (r̄ < 0.7 on any source). It did not — by a wide margin.
- Not currently the case.

## Appendices

### A. Processing Log

- 2026-05-15: Wave dispatched by δ-as-agent in single-actor collapse mode. Pipeline implemented + smoke-tested; SimTK acquisition gate blocked the empirical run. First REVISE draft of this report posted.
- 2026-05-17: SimTK account `usurobor` created via operator-authorized agent flow; Apache 2.0 click-through accepted; `LabValidation_withoutVideos.zip` downloaded (2,890 MB, SHA-256 `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`); archive extracted; manifest updated at commit `7d5e724`.
- 2026-05-17 (continued): `scripts/io_opencap.py` extended with `discover_walking_ik`, `load_paired_trial`, `load_all_walking_trials`, and `IK_SOURCES` constant to handle the real archive's `subject<NN>/OpenSimData/Mocap/IK/*.mot` + `MarkerData/Mocap/*.trc` layout. `scripts/build_notebook.py` cells 3 and 13 rewritten; notebook regenerated and executed against the real archive. This report rewritten with real-data results and the new REVISE recommendation.

### B. Quality Control Plots

Three inline figures committed in `notebooks/existing-data-processing.ipynb`, now showing real-data traces:

- Hip / knee / ankle traces overlaid across the 11 successful R-side cycles. Visibly normative gait waveforms — the cycles that did segment are clean.
- Knee-angle-R curves by condition (walking vs walkingTS). Visible overlap; n is too small for inference.
- Knee-range boxplot by condition. Same caveat.

These are real artifacts now, no longer smoke figures, but with the caveat that n=11 cycles (all R-side) limits what can be read from them.

### C. Raw Data Statistics

- `/opt/gait-data/opencap-lab-validation/extracted/` — 7.2 GiB, 11,141 files, 10 subjects, 4 IK sources, 60 walking trials each. SHA-256 of the archive: `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`.
- `/opt/gait-data/gait-support-paths-features/features-zeroth-pilot.csv` — 11 cycles × 29 columns (real-data). Not committed (lives outside repo per `data/external/README.md`).
- Aggregate summary at `analysis/feature-summary-zeroth-pilot.md` — auto-generated by the notebook each run.
