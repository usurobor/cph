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

**GO with bounded scope on R1; partial GO on R-side construct (R3); construct survives R4 contact subject to anchor caveats** (2026-05-20 cph#31 R4 full falsification re-evaluation, per [`reports/field-report-04-falsification-evaluation.md`](reports/field-report-04-falsification-evaluation.md), anchored on cph#27 + cph#28). The Coherence Path Hypothesis is not validated; it is also not refuted. cph#31 walks the 6 falsification conditions in [`docs/concepts/support-path.md`](docs/concepts/support-path.md) §Falsification one by one: 5 of 6 cleanly NOT triggered (conditions 1, 2, 4, 5, 6 — anchored on cph#27 R-side aggregate + R1 OpenCap-vs-reference comparison + 0.00% missingness on 117 cycles × 35 columns); 1 of 6 (condition 3, L/R asymmetry) is evaluable on the inferred-bilateral surface but the substantive triggered / not triggered verdict is owned by cph#30 (R3 bilateral extension, not yet merged) and is non-contributory to the threshold tally per the doc's "Empirical-data prerequisite" reading. Wave-level verdict: 0 of 6 triggered → construct survives (subject to caveats: R-side scope for conditions 1/2/6; condition 3 deferral to cph#30; path (a) honesty on bilateral surface; survives ≠ validated).

## Current blocker

R1 closed GO with bounded scope (cph#28). R4 closed survives-subject-to-caveats (cph#31). The active blocker is cph#30 (R3 bilateral extension) — the substantive lr-diff verdict on the inferred-bilateral surface, which (a) closes the R3 bilateral gate and (b) provides the substantive condition 3 verdict that cph#31 deferred. The optional measured-bilateral upgrade path (path (b): operator-side OpenSim IK rerun) remains available if cph#30's findings surface measurement-vs-inference ambiguity that path (a) cannot resolve.

## Next action

cph#30 R3 bilateral extension is the active cycle and the next gate. After cph#30 lands, cph#31's condition 3 row updates to triggered / not triggered with cph#30's surface anchor; the wave-level verdict re-reads predictably (0 of 6 if cph#30 returns "consistent with asymmetric signature" mapping to condition 3 NOT triggered; 1 of 6 if cph#30 returns refutation mapping to condition 3 triggered — either way still in the "survives" bucket at the boundary). R5 stays blocked behind R3-bilateral closure. R6 stays blocked; R4 GO does not unblock R6 (confound-check sweep is a separate gate).

Held in scope: no friend captures, no clustering, no new empirical claims. See [`ROADMAP.md`](ROADMAP.md) §"Phase R5" and §"Phase R6" for why those are blocked.

## Open issues

- [cph#30](https://github.com/usurobor/cph/issues/30) — R3 bilateral extension on the inferred-bilateral surface (post-cph#28). Active in parallel with cph#31; not yet landed on `main` at cph#31 run time. Owner of the substantive condition 3 verdict.
- [cph#31](https://github.com/usurobor/cph/issues/31) — R4 full falsification re-evaluation. **Walked all 6 conditions; wave-level verdict = construct survives subject to caveats**; pending β merge.

cph#27 (R3 R-side aggregate) merged 2026-05-19. cph#28 (R1 L-cycle recovery) merged 2026-05-19. cph#30 (R3 bilateral) and cph#31 (R4 full falsification — this cycle) ran in parallel.

## Last field report

[`reports/field-report-04-falsification-evaluation.md`](reports/field-report-04-falsification-evaluation.md) — 2026-05-20 cph#31 R4 full falsification re-evaluation (synthesis report; no new compute commissioned). Verdict: construct survives R4 contact (0 of 6 triggered, 5 of 6 NOT triggered, 1 of 6 evaluable-but-pending cph#30). Anchored on cph#27 R-side aggregate (7 of 25 features BH-sig at q<0.05; three candidate support-path hypotheses) + cph#28 inferred-bilateral surface (57 inferred-partial L cycles; 57 bilateral pairs). Standing-decision implications: R1 no change; R3 partial GO on R-side stands (bilateral extension owned by cph#30); R5 blocked behind R3-bilateral; R6 blocked, R4 GO does not unblock.
