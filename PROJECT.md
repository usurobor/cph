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

**REVISE on R1; partial GO on R-side construct (R3)** (2026-05-19 cph#27 R3 R-side aggregate analysis, per [`reports/field-report-03-construct-evaluation.md`](reports/field-report-03-construct-evaluation.md)). The Coherence Path Hypothesis is not validated; it is also not refuted. The R-side construct evaluation produced 7 BH-significant condition responses (q<0.05) across 25 numeric features in 10 subjects: H1 (sagittal-dominant load transfer) survives partially in a *distal-contraction-under-proximal-compensation* form (ankle range −6.6°); H2 (trunk-sway compensation) survives partially in a *trunk-segment-driven* form (lumbar bending +18.3°); H3 (asymmetric phase-coupling) remains structurally non-testable on the archive (L=1 cycle). 0 of 6 falsification conditions triggered on R-side surfaces (5 NOT triggered, 1 not testable). R1 stays REVISE because the bilateral construct is still half-anchored; cph#28 owns R1's transition gate.

## Current blocker

L-side cycle yield from trial cropping in the OpenCap Lab Validation archive — each trial is cropped to ~1.3–1.5 s (≈1 stride), R-aligned, leaving 47/60 L sides ending in mid-swing and 12/60 starting in mid-swing. This is a property of the source archive, not the detector: `scripts/segmentation.py::detect_heel_strikes` now uses robust-percentile normalization + stance-region depth/length gating, fires HS on all 60 L-side trials, and passes AC1 cleanly on the R-side. `scripts/segmentation_diagnostics.py` reports the per-(trial, side) zero-cycle reasons mechanically. cph#27 (R3 R-side aggregate, partial GO) does not lift this blocker; cph#28 (L-cycle recovery) owns the gate.

## Next action

After cph#27 merges, R1's remaining gate is cph#28 — L-cycle recovery via one of the two paths named in [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md): (a) contralateral-anchored L-cycle detection, or (b) re-run OpenSim IK on the source TRC files with wider time windows. Once cph#28 lands, a full R4 falsification re-evaluation at bilateral n becomes possible; until then, condition 3 (L/R asymmetry) stays "not testable" and Hypothesis 3 stays unanchored.

Held in scope: no friend captures, no clustering, no new empirical claims. See [`ROADMAP.md`](ROADMAP.md) §"Phase R5" and §"Phase R6" for why those are blocked.

## Open issues

- [cph#27](https://github.com/usurobor/cph/issues/27) — R3 R-side aggregate condition-response analysis (n=60 R cycles × 10 subjects × 2 conditions). **Returned partial GO on R-side** per [`reports/field-report-03-construct-evaluation.md`](reports/field-report-03-construct-evaluation.md); pending β merge.
- [cph#28](https://github.com/usurobor/cph/issues/28) — L-cycle recovery (contralateral-anchored detection or wider IK windows). Owner of R1's transition gate.

Both runnable in parallel (disjoint file surfaces). cph#27 has now produced R-side construct-level evidence; cph#28 remains the sharper next gate for bilateral CPH testability.

## Last field report

[`reports/field-report-03-construct-evaluation.md`](reports/field-report-03-construct-evaluation.md) — 2026-05-19 cph#27 R3 R-side aggregate condition-response analysis (60 R cycles × 10 subjects × 2 conditions × 25 numeric features). Verdict: R3 partial GO on R-side; R1 unchanged REVISE; 7 BH-significant condition responses; 3 candidate support-path hypotheses surfaced; 0/6 falsification conditions triggered on R-side surfaces; H3 (bilateral phase-coupling) deferred to cph#28.
