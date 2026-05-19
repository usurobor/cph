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

**GO with bounded scope on R1; partial GO on R-side construct (R3)** (2026-05-19 cph#28 L-cycle recovery, per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md)). The Coherence Path Hypothesis is not validated; it is also not refuted. cph#28's contralateral-anchored L-cycle inference (path (a)) recovers 57 L cycles via the matched-duration partial-clip rule (R HS plus half-stride offset, calibrated against the lone measured-L-cycle trial: 30 ms drift); bilateral (subject, trial, cycle_number) pair count is 57; `lr_asymmetry` features compute on 60 non-empty rows. R-side detector and R cycle distribution are unchanged (60 / 60, mean 1.06 s, R-only range 0.89–1.37 s). The cph#28 AC5 GO criterion fires: AC1 ≥ 80% on R (100%) and L (95%); L ≥ 10 (57 cycles). R1 transitions REVISE → GO with bounded scope: all 57 L cycles are partial-clip (coverage 0.80–0.94) and inferred not measured, so bilateral asymmetry features carry an inference layer that R-vs-R features do not. cph#27 R3 partial GO on R-side stands; full R3 bilateral and R4 condition-3 evaluations are now unblocked on the inferred surface.

## Current blocker

R1 transition gate satisfied (with bounded scope); the next blocker is downstream — R3 bilateral extension on the inferred surface and R4 full falsification re-evaluation. The optional measured-bilateral upgrade path (path (b): operator-side OpenSim IK rerun on the reachable TRC files in `/opt/gait-data/opencap-lab-validation/extracted/` with extended time windows) remains available if the inferred-bilateral analyses surface ambiguities that need measurement to resolve. No in-container blocker remains for R3 / R4 work.

## Next action

R1 closes GO with bounded scope per cph#28. R3 has a bilateral extension surface ready: re-run `analysis/r3_subject_aggregate_tests.py` against the post-cph#28 feature table to include L-side rows + R-vs-L subject-paired deltas (the script already excludes `detection_method` from per-feature aggregation). R4 has a full 6-condition re-evaluation surface ready: condition 3 transitions from "not testable" to "evaluable on inferred-bilateral surface". Triage of R3-bilateral vs R4-falsification ordering is the operator's call.

Held in scope: no friend captures, no clustering, no new empirical claims. See [`ROADMAP.md`](ROADMAP.md) §"Phase R5" and §"Phase R6" for why those are blocked.

## Open issues

- [cph#28](https://github.com/usurobor/cph/issues/28) — L-cycle recovery (contralateral-anchored detection or wider IK windows). **Path (a) shipped; R1 transitions REVISE → GO with bounded scope**; pending β merge.

cph#27 (R3 R-side aggregate) merged 2026-05-19. cph#28 (this cycle) is the active R1-transition cycle.

## Last field report

[`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) — 2026-05-19 cph#28 L-cycle recovery run (60 R measured + 57 L inferred-partial cycles across 10 subjects × 2 conditions). Verdict: R1 → GO with bounded scope (path (a) inferred bilateral); R-side regression preserved; 57 bilateral pairs; `lr_asymmetry` computable on 60 rows; path (a) honesty caveat in place (inferred L HS + partial-clip coverage 0.80–0.94).
