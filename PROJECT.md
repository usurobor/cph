# Project status

This file carries cph's **current operational status only** — the snapshot a reader needs to answer "what is the project doing right now?" without scrolling through history or roadmap.

It is one of four status-bearing surfaces, each with a single concern:

- [`README.md`](README.md) — public charter, hypothesis, source-of-truth table.
- [`ROADMAP.md`](ROADMAP.md) — gate-based research phases (R0–R6), where each phase stands, what closes it.
- [`CHANGELOG.md`](CHANGELOG.md) — project changelog across waves.
- `PROJECT.md` (this file) — live operational status; updated when status changes, not on a schedule.

Do not duplicate roadmap content here. Do not duplicate ledger content here. If a fact lives in `ROADMAP.md` or `CHANGELOG.md`, point to it.

## Current stage

**R1 — Existing-data zeroth pilot.** R0 (charter coherence) is closed: README, hypothesis doc, support-path doc, failure-conditions doc, and the seven-families article describe one project. R2–R6 are gated behind R1 and R2. See [`ROADMAP.md`](ROADMAP.md) for each phase's gate and status.

## Current empirical decision

**GO with bounded scope on R1; partial GO on R-side construct (R3 R-side); indeterminate on R3 bilateral (path (a)); construct survives R4 contact subject to anchor caveats** (2026-05-20 cph#30 R3 bilateral extension, per [`reports/field-report-03-construct-evaluation.md`](reports/field-report-03-construct-evaluation.md) §"R3 bilateral extension (cph#30, 2026-05-20)"; integrated with cph#31 [`reports/field-report-04-falsification-evaluation.md`](reports/field-report-04-falsification-evaluation.md)). The Coherence Path Hypothesis is not validated; it is also not refuted. cph#30 ran the bilateral L-vs-R lr-diff analysis on the post-cph#28 inferred-bilateral feature table (60 R measured + 57 L inferred-partial cycles; 57 paired (subject, trial_id, condition, cycle_number) rows; 10 subjects × 2 conditions × 25 lr_diff features). 21 of 50 (feature × condition) lr-diff tests cleared BH q<0.05, all 21 in the positive direction (R > L). The positive-direction pattern on every joint range feature and every trunk/pelvis range feature is *consistent with* the partial-clip geometric bias predicted by cph#28's matched-duration L-cycle recovery (L cycles cover 0.80–0.94 of the L stride; missing terminal swing biases L range features systematically downward) AND *consistent with* a true asymmetric coordination signature; the two surfaces cannot be distinguished on the inferred-bilateral data alone. The cleanest H3 probe (coordination-lag lr_diff features — timing-based, not biased by amplitude truncation) returns a BH-non-significant null. **H3 verdict: indeterminate** on the inferred-bilateral surface. **Falsification condition 3: evaluable; indeterminate; bounded scope** — neither triggered nor cleanly NOT-triggered. cph#31's wave-level verdict reading carries through unchanged (condition 3 = indeterminate is non-contributory to the threshold tally just as cph#31's "evaluable, verdict pending" was; 0 of 6 triggered, 5 of 6 NOT triggered, 1 of 6 indeterminate → still in "0–1 triggered → construct survives" bucket). H1 and H2 verdicts from cph#27 R-side stand unchanged.

## Current blocker

R1 closed GO with bounded scope (cph#28). R4 closed survives-subject-to-caveats (cph#31). R3 R-side closed partial GO (cph#27). R3 bilateral closed indeterminate on inferred-bilateral surface (cph#30, this cycle). The active blocker is **path (b) measured-bilateral upgrade** — owner of the decisive H3 verdict. Operator-side OpenSim IK rerun on the reachable TRC files at `/opt/gait-data/opencap-lab-validation/extracted/` with extended trial windows would produce measured L HS times and full-coverage L cycles, replacing the inference layer; once measured-bilateral data exists, re-run `analysis/r3_bilateral_tests.py` against the new feature table to substitute the indeterminate H3 verdict for a decisive one. R4 condition 3 row would re-read at that point per cph#31 §"Open issues from cph#31"'s deterministic update rule.

## Next action

R3 bilateral closes indeterminate on the inferred-bilateral surface; the decisive next gate is path (b) measured-bilateral upgrade (out of cph#30 scope; requires operator-side OpenSim install). In the interim, R5 (friend pre-pilot) is technically unblocked at the gate level (R3 closure is recorded on both R-side and bilateral surfaces; R4 survives) but the capture-protocol-revision step (≥3 s trial length so future archives do not recur the partial-clip geometric bias) is the remaining R5 prerequisite. R6 stays blocked; R3-bilateral indeterminate does not unblock R6.

Held in scope: no friend captures, no clustering, no new empirical claims. See [`ROADMAP.md`](ROADMAP.md) §"Phase R5" and §"Phase R6" for why those are blocked.

## Open issues

- [cph#30](https://github.com/usurobor/cph/issues/30) — R3 bilateral extension on the inferred-bilateral surface (post-cph#28). **R3 bilateral closes indeterminate; H3 indeterminate; falsification condition 3 indeterminate; bounded scope**; pending β merge.

cph#27 (R3 R-side aggregate) merged 2026-05-19. cph#28 (R1 L-cycle recovery) merged 2026-05-19. cph#31 (R4 full falsification) merged 2026-05-20. cph#30 (this cycle) is the R3 bilateral extension run after cph#31 landed; cph#31's "condition 3 evaluable, verdict pending cph#30" deferral re-reads as "condition 3 indeterminate" per cph#30's path (a) honesty caveat.

## Last field report

[`reports/field-report-03-construct-evaluation.md`](reports/field-report-03-construct-evaluation.md) §"R3 bilateral extension (cph#30, 2026-05-20)" — 2026-05-20 cph#30 R3 bilateral extension run on the post-cph#28 inferred-bilateral surface (60 R measured + 57 L inferred-partial; 57 paired bilateral rows; 25 lr_diff features × 2 conditions = 50 paired tests; 21 BH-significant at q<0.05, all in positive direction R > L; coordination-lag probes return BH-non-sig null). Verdict: R3 bilateral = indeterminate (path (a) inferred-bilateral surface; partial-clip geometric bias and real asymmetric coordination indistinguishable without measured-bilateral data); H1 / H2 cph#27 R-side verdicts preserved unchanged; cph#31 R4 wave-level "construct survives" verdict carries through unchanged (condition 3 indeterminate = non-contributory to threshold tally). The cycle's direction-of-evidence finding (BH-significant positive lr_diff on every range feature with zero injected asymmetric signal under surrogate substitution) is structural and survives surrogate-vs-canonical substitution; β re-runs the bilateral script against the persisted CSV to substitute canonical effect-size magnitudes.
