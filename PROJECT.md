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

**REVISE** (2026-05-17 segmentation-fix run, per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md)). The Coherence Path Hypothesis is not validated; it is also not refuted. The OpenCap-vs-reference comparison passes (Pearson r̄ 0.93–0.96). Gait-cycle segmentation now passes AC1 on R-side (60/60 trials, 100%; 61 cycles total = 60 R + 1 L), but the L-side cycle yield is structurally limited by trial cropping to 1/60. This blocks Hypothesis 3 (asymmetric phase-coupling) and constrains the bilateral construct to a half-anchored test; Hypothesis 1 (sagittal-dominant load transfer) is now evaluable on R-side data with n=60 cycles.

## Current blocker

L-side cycle yield from trial cropping in the OpenCap Lab Validation archive — each trial is cropped to ~1.3–1.5 s (≈1 stride), R-aligned, leaving 47/60 L sides ending in mid-swing and 12/60 starting in mid-swing. This is a property of the source archive, not the detector: `scripts/segmentation.py::detect_heel_strikes` now uses robust-percentile normalization + stance-region depth/length gating, fires HS on all 60 L-side trials, and passes AC1 cleanly on the R-side. `scripts/segmentation_diagnostics.py` reports the per-(trial, side) zero-cycle reasons mechanically.

## Next action

Recover L-side cycles via one of the two paths named in [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md): (a) contralateral-anchored L-cycle detection (use detected R HS times + half-stride offset to seed L cycle bounds), or (b) re-run OpenSim IK on the source TRC files with wider time windows. Both are out of scope for the current bounded cycle. While L-cycle recovery is pending, R3 (subject-level condition-response analysis) can proceed on R-side n=60 across 10 subjects × 2 conditions; R4 (falsification-table re-evaluation) can proceed on the R-side surfaces that are now anchored.

Held in scope: no friend captures, no clustering, no new empirical claims. See [`ROADMAP.md`](ROADMAP.md) §"Phase R5" and §"Phase R6" for why those are blocked.

## Open issues

- [cph#27](https://github.com/usurobor/cph/issues/27) — R3 R-side aggregate condition-response analysis (n=60 R cycles × 10 subjects × 2 conditions).
- [cph#28](https://github.com/usurobor/cph/issues/28) — L-cycle recovery (contralateral-anchored detection or wider IK windows).

Both runnable in parallel (disjoint file surfaces). The [cph#26](https://github.com/usurobor/cph/issues/26) §"Post-port decision" recommendation was R-side aggregate first; the L-cycle recovery cycle is the sharper next gate for bilateral CPH testability.

## Last field report

[`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) — 2026-05-17 segmentation-fix re-run against the OpenCap Lab Validation archive (60 walking trials × 10 subjects, SHA-256 `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`). Verdict: REVISE on R1 (bilateral construct half-anchored at n=1 L-cycle); pass on the OpenCap-vs-reference comparison; AC1 segmentation passes on R-side (60/60 trials, 100%); L-side cycle yield structurally limited to 1/60 by trial cropping.
