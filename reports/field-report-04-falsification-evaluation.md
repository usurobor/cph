# Field Report 04: R4 full falsification re-evaluation on post-cph#27 + cph#28 surfaces

## Overview

**Report Date:** 2026-05-20 (cph#31 R4 full falsification re-evaluation).
**Cycle:** cph#31 — walks the 6 falsification conditions in [`docs/concepts/support-path.md`](../docs/concepts/support-path.md) §Falsification one by one against the post-cph#27 R-side construct evaluation and the post-cph#28 inferred-bilateral surface.
**Protocol:** [`docs/concepts/support-path.md`](../docs/concepts/support-path.md) §Falsification (the 6 conditions are fixed; this cycle evaluates them, not rewrites them) + the wave-level threshold (0–1 triggered → construct survives; 2–3 → ambiguous; ≥4 → fundamental revision required).
**Inputs (no new compute commissioned by this cycle):**
- [`reports/field-report-03-construct-evaluation.md`](field-report-03-construct-evaluation.md) — cph#27 R-side aggregate (n=10 subjects × 2 conditions × 25 numeric features; 7 BH-significant at q<0.05; 5 of 6 conditions evaluated NOT triggered on R-side, condition 3 not testable).
- [`reports/field-report-01-existing-data-zeroth-pilot.md`](field-report-01-existing-data-zeroth-pilot.md) — cph#28 inferred-bilateral surface (60 R measured + 57 L inferred-partial cycles; 57 bilateral (subject, trial_id, cycle_number) pairs; coverage 0.80–0.94, mean 0.86; calibrated to 30 ms drift on subject8/walkingTS1).
- cph#30 (R3 bilateral extension) — not landed on `main` at the time of this run; lr-diff substantive verdicts deferred to that cycle.

**Status:** **Decision: construct survives (0 triggered / 5 NOT triggered / 1 evaluable-but-pending), subject to caveats.** Wave-level threshold (≥4 → fundamental revision) not crossed; threshold (2–3 → ambiguous) not crossed; threshold (0–1 → survives) reached, with the standing caveat that condition 3's substantive verdict on the inferred-bilateral surface is owned by cph#30 and that all bilateral readings carry path (a) inference uncertainty.

## Executive summary

This cycle synthesizes the full 6-condition table at adequate empirical coverage. cph#27 produced 5 R-side "NOT triggered" verdicts plus 1 "not testable" verdict on condition 3 (L/R asymmetry). cph#28 lifted condition 3 from "not testable" to "evaluable on inferred-bilateral surface" by recovering 57 L cycles via half-stride contralateral inference. cph#31 (this cycle) does not re-run cph#27 / cph#28 analyses; it walks each condition one by one, declares testability against the available surfaces, and anchors the verdict on cited evidence.

**Per-condition headlines.**

- **Condition 1** — NOT triggered (R-side); partially testable on inferred-bilateral. The 7 BH-sig R-side features at q<0.05, with r_rb = ±1.0 on four of them (every subject moves in the same direction), are the systematic-not-random anchor.
- **Condition 2** — NOT triggered (R-side). The trunk-sway condition response is large (lumbar_bending_range_deg +18.3°) and broad (7 of 25 features cross BH); features respond systematically to condition.
- **Condition 3** — evaluable on inferred-bilateral surface (was "not testable" pre-cph#28). Substantive triggered / not triggered verdict requires the lr-diff aggregate tests owned by cph#30; at the time of this run, cph#30 has not landed on `main`. This cycle declares the condition *testable, verdict pending*. Per `docs/concepts/support-path.md` §Falsification, "testable but not yet evaluated" is *not* the same as "not testable" — but it also does *not* count as "triggered" or "not triggered" for the wave-level threshold until the substantive verdict is in.
- **Condition 4** — NOT triggered. Pearson r̄ 0.93–0.96 across 3 Video backbones × 60 trials; carried from cph#22/26 (R1).
- **Condition 5** — NOT triggered. 0.00% missingness across 35 columns × 117 cycles (post-cph#28).
- **Condition 6** — NOT triggered (R-side). The three candidate support-path hypotheses (Lateral-trunk substitution path; Distal sagittal contraction under proximal compensation; Cadence-slowdown signature) are mutually distinguishable on R-side; condition 6 on the bilateral surface (lr-diff distinguishability) is downstream of cph#30.

**Wave-level verdict.** 0 of 6 triggered, 5 of 6 NOT triggered, 1 of 6 *evaluable but verdict pending cph#30 (anchored on inferred-bilateral surface)*. Per the wave-level rule, this is in the "0–1 triggered → construct survives" range, with the deferred-verdict carry per `docs/concepts/support-path.md` §Falsification "Empirical-data prerequisite" ("Not testable" verdicts carry no evidence either way; cph#31 reads "testable but verdict pending cph#30" as the same: it does not count toward the threshold). The construct survives R4 contact at the post-cph#27 + cph#28 surface level, subject to (a) all bilateral readings being path (a) inference, not measurement, and (b) condition 3's substantive verdict being owned by cph#30 and re-readable here when cph#30 lands.

**Important caveat (carried verbatim from cph#27 field report §AC5).** "Construct survives" does *not* mean "construct is validated." The Coherence Path Hypothesis is neither validated nor refuted by this cycle. R4 evaluates *whether the construct survives existing-data contact*; it does not evaluate *whether the construct is true*. The standing decisions in §"Standing-decision implications" below name how the verdict propagates to R1 / R3 / R5 / R6 status — those propagations do *not* lift the hypothesis beyond "survives the falsification gate at this cycle's surfaces."

## Methodological note: no new compute commissioned

Per the issue body §Approach, this cycle was authorized to write `analysis/r4_falsification_eval.py` (new script) if any condition needed compute beyond what cph#27 and cph#28 already produced. **No condition needed new compute.** Reasoning:

- Conditions 1, 2, 6 are anchored on cph#27's R-side aggregate. The bilateral extension (cph#30) would re-test them on lr-diff features; cph#31 does *not* duplicate cph#30's work.
- Condition 3 is anchored on cph#28's surface lift (testability) plus the lr-diff substantive verdict (which cph#30 owns). cph#31 cannot produce the substantive verdict without duplicating cph#30; the cycle's job is the testability declaration plus the surface-availability anchor, not the underlying lr-diff statistical tests.
- Conditions 4 and 5 are anchored on R1 surfaces (OpenCap-vs-reference comparison; feature-extraction missingness) that have not changed between cph#22/26 and now.

The synthesis is therefore evidentiary, not computational. The "no new compute" reading is itself an evidence claim: the 6-condition table is fully evaluable today on cited prior-cycle outputs, with the one named exception (condition 3 substantive verdict) declared explicitly as deferred to cph#30.

## 6-condition table (AC1 + AC2 + AC3)

Each row carries four columns: condition (verbatim from the canonical doc), testability declaration (testable / partially testable / not testable on this archive), verdict (triggered / not triggered / evaluable-but-pending), and bounded scope (surface anchoring + caveats).

| # | Condition (verbatim) | Testability on this archive | Verdict | Bounded scope (surface + caveats) |
|---|---|---|---|---|
| 1 | No repeatable patterns across gait cycles — *if extracted features show purely random variation between gait cycles within the same trial and participant, with no discernible coordination patterns, then support paths may be theoretical artifacts rather than measurable phenomena* | **Partially testable** (R-side has n=3 cycles per (subject, condition) cell — too few for within-subject ICC; cross-subject systematic-vs-random pattern is testable on R-side n=60 and on bilateral inferred n=117) | **NOT triggered** | **Anchor: cph#27 R-side aggregate** (`reports/field-report-03-construct-evaluation.md` §AC5 row 1). 7 of 25 features BH-sig at q<0.05; r_rb = ±1.0 on four of those (every subject moves in the same direction); per-subject paired-delta heatmap shows systematic, not random, response. The aggregation step produced 700 cells with no missing values (0.00% missingness on 35 columns × 61 cycles in cph#27, 35 columns × 117 cycles in cph#28). **Caveat:** within-subject within-condition cycle-level repeatability not directly tested (cph#27 §Debt D2); the verdict reads cross-subject consistency as evidence against "purely random variation," not as evidence for within-subject stability. Bilateral inferred extension would not flip the R-side verdict; cph#30's lr-diff tests are a separate question (condition 3 / 6 territory, not condition 1). |
| 2 | Features uncorrelated with movement context — *if extracted timing, joint angle, and coordination features fail to show systematic differences between walking speeds, conditions, or participants, the construct lacks empirical grounding in the measured data* | **Testable on R-side** (natural vs trunk-sway cohorts are matched 10×3 cycles per cell, paired Wilcoxon at n=10 subjects); **bilateral extension not required** to evaluate the condition — condition 2 asks whether *any* features correlate with context, and R-side yields a definitive answer | **NOT triggered** | **Anchor: cph#27 R-side aggregate** (`reports/field-report-03-construct-evaluation.md` §AC5 row 2). The trunk-sway condition response is large (lumbar_bending_range_deg +18.3° median Δ, 10/10 subjects positive, r_rb = +1.0, q = 0.012) and broad (7 features cross BH at q<0.05: cycle_duration_s, swing_duration_s, ankle_angle_range_deg, ankle_angle_min_deg, lumbar_bending_range_deg, lumbar_extension_range_deg, hip_knee_lag_samples). **Caveat:** "context" in this archive means natural vs trunk-sway only — no graded speeds, no graded footwear, no fatigue conditions; the verdict is bound to that single contrast. Walking speed sensitivity remains untested on this archive (the OpenCap Lab Validation protocol uses self-selected speed, not graded). |
| 3 | Left-right asymmetry without systematic organization — *if left and right limb features show random asymmetry rather than systematic differences that could reflect coordination strategies, then support paths may not capture meaningful organizational patterns* | **Evaluable on inferred-bilateral surface** (was "not testable on this archive" pre-cph#28; cph#28 added 57 inferred-partial L cycles, 57 bilateral pairs, lr-diff features computable on 60 rows). Substantive triggered / not triggered verdict requires running paired tests on the `*_lr_diff` features — **owned by cph#30** (R3 bilateral extension); not duplicated here per issue body §Approach. | **Evaluable, substantive verdict pending cph#30** (anchored on inferred-bilateral surface) | **Anchor: cph#28 inferred-bilateral surface** (`reports/field-report-01-existing-data-zeroth-pilot.md` §"L-side recovery (cph#28)" + §Falsification Assessment row 3). The surface exists: 57 paired (subject, trial_id, cycle_number) cycles; lr-diff features (joint range, hip_knee_lag) computable across 60 rows; `analysis/r3_subject_aggregate_tests.py` already excludes `detection_method` from per-feature aggregation. **Caveats — path (a) honesty (verbatim from cph#28 field report):** (a) all L cycles are inferred via the half-stride contralateral assumption, not measured directly — the half-stride model is itself a property a bilateral asymmetry analysis intends to test, so any lr-diff finding will carry inference uncertainty that R-vs-R features (cph#27) do not; (b) all 57 L cycles are partial-clip (coverage 0.80–0.94, mean 0.86) — the missing terminal swing biases range features slightly downward and makes cycle-boundary timing / coordination features unreliable; (c) lr-diff magnitudes from this surface should be reported as "consistent with" an asymmetric coordination signature when significant, not as "measurement of" asymmetric coordination. **Threshold accounting (per `docs/concepts/support-path.md` §Falsification "Empirical-data prerequisite"):** an "evaluable, substantive verdict pending" condition does *not* count toward the wave-level threshold rule, on the same rationale that a "not testable" verdict does not count (no empirical evidence either for or against the construct yet; the surface exists but the test has not run). When cph#30 lands, this row will be updatable to triggered / not triggered; until then, treat it as non-contributory to the count. |
| 4 | Poor agreement between OpenCap and reference measurements — *if OpenCap-derived features show poor correlation with gold-standard measurements (force plates, optical motion capture), then the technical foundation for support path analysis is compromised* | **Testable** (R1 evaluated this directly on 60 trials × 3 Video backbones with Mocap IK as the reference) | **NOT triggered** | **Anchor: R1 OpenCap-vs-reference comparison, carried from cph#22/26** (`reports/field-report-01-existing-data-zeroth-pilot.md` §"OpenCap vs Reference Comparison"). Pearson r̄ = 0.962 (HRNet @ 5-cam), 0.933 (OpenPose_default @ 5-cam), 0.951 (OpenPose_highAccuracy @ 5-cam); across-joint mean RMSE 5.4° / 6.5° / 5.5°. All three backbones clear the GO threshold of r̄ ≥ 0.7 with substantial headroom; HRNet is the strongest. **Caveat:** the comparison is on full-trial IK time series (segmentation-independent); it speaks to the *measurement substrate* (sagittal hip / knee / ankle reconstruction from OpenCap video), not to the *construct*. The Coherence Path Hypothesis sits at a higher level of inference than the OpenCap-vs-Mocap comparison can speak to. cph#28 did not modify the comparison (path (b) — OpenSim IK rerun with extended trial windows — was not pursued in-container); the numbers are unchanged. The ankle channel under OpenPose_default (r ≈ 0.86–0.88) is the weakest link in the matrix and is consistent with the published observation that the foot is the harder OpenCap segment to track; this caveat is named here for the record but does not flip the verdict. |
| 5 | Feature extraction consistently fails on clean data — *if the pipeline cannot reliably extract interpretable features from high-quality gait data, then the measurement approach is inadequate for testing support path hypotheses* | **Testable** (per `docs/concepts/support-path.md` §Falsification "Empirical-data prerequisite", condition 5 is the exception that can be evaluated against synthetic clean inputs and yields a meaningful verdict on smoke alone, because it tests pipeline competence rather than empirical variation; the post-cph#28 archive also provides real-data confirmation) | **NOT triggered** | **Anchor: feature-extraction missingness on real + smoke** (`analysis/feature-summary-zeroth-pilot.md` §AC2; `reports/field-report-01-existing-data-zeroth-pilot.md` §"Feature Extraction Status"). 0.00% missingness across 35 columns × 61 cycles (cph#27 R-only surface) and across 35 columns × 117 cycles (cph#28 post-recovery bilateral surface). All 25 numeric features extract on every cycle. The smoke generator produces 7+7 = 14 cycles at the expected 1.1 s stride period (cph#26 carryover). **Caveat:** "clean data" in the smoke sense (synthetic, by-construction-coherent) tests pipeline competence only; cph#27 §Debt and `docs/concepts/support-path.md` §Falsification "Empirical-data prerequisite" both note that *smoke-passing alone* would yield a misleading "0 of 6 triggered" reading. cph#31 reads this row as non-misleading because the real-data anchor (117 cycles × 0.00% missing) is independent of the smoke anchor. |
| 6 | No distinguishable coordination signatures — *if feature analysis reveals only continuous variation without discrete organizational types or clusters, then support paths may represent observer bias rather than measurable coordination patterns* | **Partially testable on R-side** (feature-family-level distinguishability between the 3 candidate hypotheses is testable on cph#27's surface; subject-level signature distinguishability is testable on the per-subject paired-delta heatmap; formal PCA / clustering deferred to R6 and explicitly out of cph#31 scope per issue body); **bilateral lr-diff distinguishability** is downstream of cph#30 | **NOT triggered** | **Anchor: cph#27 R-side aggregate** (`reports/field-report-03-construct-evaluation.md` §AC5 row 6 + §"Candidate support-path hypotheses (AC4)"). The three candidate signatures are mutually distinguishable on R-side: Candidate 1 (Lateral-trunk substitution path; lumbar bending + extension + pelvis tilt increase) moves *up*; Candidate 2 (Distal sagittal contraction under proximal compensation; ankle range + ankle min + knee range decrease) moves *down*; Candidate 3 (Cadence-slowdown signature; cycle duration + swing duration increase, stance fraction decrease) moves independently of both. Per-subject paired-delta heatmap shows subject heterogeneity in *which* feature responds most strongly within each candidate group — distinguishability is present at both the feature-family and subject levels. **Caveats:** (a) "distinguishable signatures" at this evidence depth is *feature-family distinguishability*, not formal PCA / clustering — that is held for R6 and is explicitly out of cph#31 scope; (b) the verdict is bound to the trunk-sway perturbation condition response, not to gait in general; (c) the bilateral lr-diff version of condition 6 (whether *bilateral* asymmetry signatures cluster) is owned by cph#30 and would either confirm or refine this R-side verdict on the inferred-bilateral surface. |

## Wave-level falsification verdict (AC4)

Threshold rule from `docs/concepts/support-path.md` §Falsification (verbatim):
- 0–1 triggered → construct survives (subject to anchor caveats)
- 2–3 triggered → ambiguous; bounded re-test
- ≥4 triggered → fundamental revision required

**Tally on this run.** 0 conditions triggered. 5 conditions cleanly NOT triggered (1, 2, 4, 5, 6). 1 condition (condition 3) evaluable but substantive verdict pending cph#30. Per the "Empirical-data prerequisite" discipline carried by the doc — "Not testable" verdicts do not count toward the threshold — cph#31 reads "evaluable, verdict pending" identically: no empirical evidence has yet been produced to count for or against. The condition does not count toward the threshold in either direction.

**Wave-level verdict:** **Construct survives** (0 triggered ≤ 1; threshold satisfied for the "survives" bucket), subject to four anchor caveats:

1. **R-side / bilateral inference scope.** Conditions 1, 2, 6 are anchored on R-side measured surfaces only. Their bilateral readings (lr-diff aggregate; per-side signature distinguishability) are downstream of cph#30; if cph#30's findings flip any of the three, condition 1 / 2 / 6 readings here should be updated.
2. **Condition 3 deferral.** The wave-level "survives" verdict is conditional on condition 3 *not* triggering on the inferred-bilateral surface when cph#30 lands. If cph#30 reports H3 as refuted / null in a way that maps to condition 3 *triggered*, the threshold count moves to 1 triggered (still in the "survives" bucket, but at the boundary). If cph#30 reports a stronger refutation, the wave-level verdict in this report needs re-reading.
3. **Path (a) honesty.** All bilateral readings (current condition 3 surface + future bilateral lr-diff for conditions 1 / 2 / 6) ride on the half-stride contralateral assumption — itself a property bilateral asymmetry analysis intends to test. Magnitudes are "consistent with" not "measurement of."
4. **Surface vs construct.** "Survives R4 contact" ≠ "construct validated." The Coherence Path Hypothesis remains neither validated nor refuted. R4 is a gate, not a proof.

## Standing-decision implications (AC5)

Per the issue body §Acceptance criteria AC5, this section names how the wave-level verdict propagates to standing decisions on R1, R3, R5, R6. The propagations are *implications*, not new gate decisions: a gate transition still requires its own gate-specific evidence and the appropriate cycle to author it. cph#31 names the implications so the propagation surface is explicit.

### R1

**Implication: no change — R1 stays GO with bounded scope (path (a) inferred bilateral).** cph#28 already lifted R1 from REVISE to GO with bounded scope; cph#31's wave-level "survives" verdict is *consistent with* that GO transition but does not lift it further. R1's bounded scope (inferred not measured; partial-clip coverage 0.80–0.94) remains the binding caveat. The path (b) measured-bilateral upgrade option (operator-side OpenSim IK rerun on the reachable TRC files) remains available; cph#31's verdict does not require pursuing it.

**Risk surfaced by cph#31:** reading the R4 wave-level "survives" as construct validation. R1 names this as *coherence laundering* — treating a clean falsification table as substantive evidence for the hypothesis. The wave-level verdict gates *non-refutation*, not *validation*; the standing R1 caveat about claim scope applies here.

### R3

**Implication: partial GO on R-side stands; bilateral extension status owned by cph#30, not by cph#31.** cph#27's R-side partial-GO is the standing R3 verdict on `main`. cph#30 is the active R3-bilateral cycle; until cph#30 lands, the R3 phase status reads "partial GO on R-side; bilateral extension active in cph#30." cph#31 does not modify this. If cph#30 lands first, the standing R3 status on `main` will be cph#30's bilateral verdict at the time of cph#31's merge — cph#31's status-surface patches need to rebase against cph#30's R3 phase block at that point.

### R5

**Implication: still blocked behind R3-bilateral closure.** R5 (friend pre-pilot) requires R3 and R4 to have closed GO. cph#31 produces R4's "construct survives" verdict, which is a necessary but not sufficient condition for R5. The blocker on R5 is now R3-bilateral closure (owned by cph#30), not R4. Once cph#30 lands, R5's status read becomes: "R3-bilateral GO ⇒ R4 survives ⇒ R5 unblocks; capture protocol revision (≥3 s trials) is the remaining R5 prerequisite." cph#31 does not lift R5 to ACTIVE.

**Risk surfaced by cph#31:** reading R4 GO as license to skip the R5 capture-protocol-revision step. R5 names body-typing / participant labeling as the failure mode to avoid; R4's "construct survives" does not relax those R5 prerequisites.

### R6

**Implication: still blocked; R4 GO does not unblock R6.** R6 (AI classification) requires R4 to have closed GO *and* a stable per-cycle feature table that survives confound checks against trial crop, marker artifact, camera setup, subject morphology, and condition labels alone. cph#31 produces R4 "survives," not the confound-check sweep. The confound-check sweep is downstream work that cph#31 does not commission. R6 stays "not started" with the caveat that the largest-named coherence risk in the project (clustering output read as hypothesis confirmation) is *not* removed by R4's verdict.

## Open issues from cph#31

- **Condition 3 substantive verdict** — owned by cph#30. When cph#30 lands, this report should be referenced and the condition 3 row updated to triggered / not triggered (with cph#30's surface anchor). The wave-level verdict needs re-reading at that point; if condition 3 triggers, the count moves to 1 of 6 (still "survives"); if cph#30 produces a stronger refutation of H3 that maps to condition 3 triggered *and* surfaces a related R-side or bilateral concern that flips condition 1 / 6, the tally could rise above the 0–1 threshold.
- **Within-subject within-condition cycle-level repeatability** — named as cph#27 §Debt D2; n=3 cycles per (subject, condition) is too thin for within-subject ICC. The condition 1 verdict here reads cross-subject consistency, not within-subject stability. A longer-trial archive (or a deliberately within-trial-repeated subset) would close this gap. *Not in cph#31 scope.*
- **First-pass PCA / formal clustering** — named as cph#27 §Debt D3 and as the R6 gate. Condition 6 is read at feature-family distinguishability depth; formal cluster structure is held for R6. *Not in cph#31 scope.*
- **Path (b) measured-bilateral upgrade** — named in cph#28 field report §Recommendation as the upgrade path if the inferred-bilateral analyses surface ambiguities. cph#31's wave-level verdict does not require pursuing it; cph#30's eventual findings will name whether it is required. *Not in cph#31 scope.*

## Decision

**Construct survives R4 contact at the post-cph#27 + cph#28 surface level** (0 of 6 conditions triggered; 5 cleanly NOT triggered; 1 evaluable but substantive verdict pending cph#30). The wave-level threshold rule from `docs/concepts/support-path.md` §Falsification places this run in the "0–1 triggered → construct survives (subject to anchor caveats)" bucket. R4 transitions from "partially evaluated on R-side" (cph#27) → "fully evaluable on inferred-bilateral surface, verdict: construct survives subject to caveats" (cph#31).

**Anchor caveats** (re-stated for the record):

1. R-side scope for conditions 1, 2, 6 (bilateral lr-diff readings on these conditions are downstream of cph#30).
2. Condition 3 evaluable-but-pending status (substantive verdict downstream of cph#30; threshold tally treats this row as non-contributory).
3. Path (a) honesty on all bilateral surface readings (inference not measurement; partial-clip coverage 0.80–0.94; magnitudes "consistent with" not "measurement of").
4. Surface ≠ construct: "survives R4" ≠ "hypothesis validated."

**Standing-decision propagations:**

- **R1:** no change (GO with bounded scope per cph#28).
- **R3:** partial GO on R-side stands (cph#27); bilateral extension status owned by cph#30.
- **R5:** blocked behind R3-bilateral closure (owned by cph#30).
- **R6:** blocked; R4 GO does not unblock R6.

## Provenance / Receipt

```text
Receipt: R4 full falsification re-evaluation
Branch: cycle/31-r4-full-falsification
Commit: filled by β at merge
Per-condition verdicts:
- 1: NOT triggered (R-side; partially testable on bilateral inferred; anchored on cph#27 R-side aggregate)
- 2: NOT triggered (testable on R-side; anchored on cph#27 R-side aggregate — 7 of 25 features BH-sig at q<0.05)
- 3: Evaluable, substantive verdict pending cph#30 (anchored on cph#28 inferred-bilateral surface; surface exists, test owned by cph#30; threshold tally: non-contributory)
- 4: NOT triggered (testable; anchored on R1 OpenCap-vs-reference comparison from cph#22/26 — r̄ 0.93–0.96)
- 5: NOT triggered (testable on smoke + real; anchored on 0.00% missingness across 117 cycles × 35 columns)
- 6: NOT triggered (partially testable on R-side; anchored on cph#27 R-side three-candidate distinguishability; PCA / clustering held for R6)
Total triggered: 0 / 6 (1 of 6 evaluable-but-pending, non-contributory to threshold)
Wave-level verdict: construct survives (0–1 triggered → survives, subject to anchor caveats)
Standing-decision implications:
- R1: no change (GO with bounded scope per cph#28)
- R3: partial GO on R-side stands; bilateral extension status owned by cph#30
- R5: blocked behind R3-bilateral closure
- R6: blocked; R4 GO does not unblock R6
No raw data committed: yes (no .csv / .trc / .mot / .sto / .c3d / .osim / .mp4 / .mov / .zip / .parquet files; analysis-only cycle)
Next recommended issue:
- cph#30 R3-bilateral close-out + this report's condition 3 row updated post-merge
- After cph#30 lands: a future cycle could revisit conditions 1 / 6 on the bilateral lr-diff surface if cph#30's bilateral findings call for it (not commissioned now)
```

## Appendices

### A. Cross-references to the source reports

- [`reports/field-report-03-construct-evaluation.md`](field-report-03-construct-evaluation.md) §"Falsification re-evaluation on R-side (AC5)" — cph#27's 6-row condition table on R-side (verdicts: 5 NOT triggered + 1 not testable).
- [`reports/field-report-01-existing-data-zeroth-pilot.md`](field-report-01-existing-data-zeroth-pilot.md) §"L-side recovery (cph#28)" — path (a) method, calibration, yield, claim-scope bounds; §"Falsification Assessment" condition 3 lift from "not testable" to "evaluable on inferred-bilateral surface."
- [`docs/concepts/support-path.md`](../docs/concepts/support-path.md) §Falsification — canonical conditions and threshold rule (consulted, not modified).
- `analysis/feature-summary-zeroth-pilot.md` — provenance for the 117 cycles × 35 columns × 0.00% missingness anchor on condition 5.

### B. Data policy

No raw participant data, no `.zip` / `.trc` / `.mot` / `.sto` / `.c3d` / `.osim` / `.mp4` / `.mov` / `.csv` / `.parquet` files added to the repo in this cycle. This is an analysis-only synthesis report; all numeric anchors are inlined as cited quotations from prior-cycle reports.

### C. Threshold-rule reading for "evaluable, verdict pending"

The doc text in `docs/concepts/support-path.md` §Falsification "Empirical-data prerequisite" distinguishes two verdicts: "not triggered" (positive empirical claim — tested, did not trigger) and "not testable" (deferred — condition could not be evaluated on the available data). The doc states explicitly that "not testable" does not count toward the threshold rule.

cph#31 reads "evaluable on inferred-bilateral surface, substantive verdict pending cph#30" as identical to "not testable" *for threshold accounting purposes only*: no empirical evidence has yet been produced to count for or against. The distinction matters for the surface-availability claim (the surface *does* exist post-cph#28; the test merely has not run yet) but not for the threshold tally. The condition 3 row in §"6-condition table" carries the surface-availability evidence; the wave-level §"Wave-level falsification verdict" carries the non-contributory accounting.

This reading is explicit so that when cph#30 lands and the condition 3 row updates to triggered / not triggered, the tally moves predictably: triggered → 1 of 6 (still "survives" bucket); not triggered → 0 of 6 (clean "survives"). No interpretive ambiguity is left between this report and cph#30's eventual verdict.
