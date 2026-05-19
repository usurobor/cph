# Project status

This file carries cph's **current operational status only** — the snapshot a reader needs to answer "what is the project doing right now?" without scrolling through history or roadmap.

It is one of four status-bearing surfaces, each with a single concern:

- [`README.md`](README.md) — public charter, hypothesis, source-of-truth table.
- [`ROADMAP.md`](ROADMAP.md) — gate-based research phases (R0–R6), where each phase stands, what closes it.
- [`CHANGELOG.md`](CHANGELOG.md) — research coherence ledger across waves.
- `PROJECT.md` (this file) — live operational status; updated when status changes, not on a schedule.

Do not duplicate roadmap content here. Do not duplicate ledger content here. If a fact lives in `ROADMAP.md` or `CHANGELOG.md`, point to it.

## Current stage

**R1 — Existing-data zeroth pilot.** R0 (charter and operationalization) is ACTIVE pending the first numeric C_Σ baseline against this branch (the [`scripts/measure-coherence.sh`](scripts/measure-coherence.sh) entrypoint runs once `coh` is on PATH in an operator environment — see §"Last coherence measurement" below); R2–R6 are gated behind R1 and R2. See [`ROADMAP.md`](ROADMAP.md) for each phase's gate and status.

## Current empirical decision

**REVISE** (2026-05-17 real-data run, per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md)). The Coherence Path Hypothesis is not validated; it is also not refuted. The OpenCap-vs-reference comparison passes (Pearson r̄ 0.93–0.96). Gait-cycle segmentation fails on real Mocap heel-marker data (18.3% R-side, 0% L-side), blocking 4 of 6 falsification conditions on cycle scarcity.

## Current blocker

`scripts/segmentation.py::detect_heel_strikes` — parameters fit to the synthetic generator do not tolerate the ~25 mm R/L mean offset on real calcaneus markers. Bounded revision named: per-side baseline subtraction + percentile-of-range threshold.

## Next action

Open a single-issue cycle scoped to `scripts/segmentation.py::detect_heel_strikes` plus a verification harness against the 60 Mocap heel-marker trials already in `/opt/gait-data/opencap-lab-validation/extracted/`. Merge the fix; re-run [`notebooks/existing-data-processing.ipynb`](notebooks/existing-data-processing.ipynb) on the unchanged archive; re-evaluate the falsification table in field-report-01.

Held in scope: no friend captures, no clustering, no new empirical claims. See [`ROADMAP.md`](ROADMAP.md) §"Phase R5" and §"Phase R6" for why those are blocked.

## Active branch / issue

- **Review branch:** `claude/review-repo-coherence-PNbjQ` — review surface for two coherence-drift-sweep waves landed against R0 (`cdr-refactor-2026-05-18` is closed; `coherence-drift-sweep-2026-05-18` and the follow-up `coherence-drift-sweep-followup-2026-05-18` are reviewing here). Merge to main is an operator gate per each wave's manifest §"Branching deviation".
- **In-flight waves on the review branch:**
  - [`coherence-drift-sweep-2026-05-18`](.cdd/waves/coherence-drift-sweep-2026-05-18/manifest.md) — master [cph#16](https://github.com/usurobor/cph/issues/16); all four subs (cph#17–20) closed APPROVE; master close is an ε/operator gate.
  - [`coherence-drift-sweep-followup-2026-05-18`](.cdd/waves/coherence-drift-sweep-followup-2026-05-18/manifest.md) — master [cph#21](https://github.com/usurobor/cph/issues/21); four subs (cph#22–25) in flight on this branch.
- **Unmerged orthogonal branch:** `origin/cycle/segmentation-real-data-fix` (tip `a95415c`) — R2 segmentation fix; merge is a separate operator decision per the precursor cdr-refactor wave's manifest.

## Last field report

[`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) — 2026-05-17 real-data run against the OpenCap Lab Validation archive (60 walking trials × 10 subjects, SHA-256 `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`). Verdict: REVISE on R1; pass on the OpenCap-vs-reference comparison; fail on segmentation.

## Last coherence measurement

`pending — coh unavailable` per the [`CHANGELOG.md`](CHANGELOG.md) 0.1.0-cdr baseline entry. The mechanical entrypoint [`scripts/measure-coherence.sh`](scripts/measure-coherence.sh) is in place; the first numeric C_Σ baseline lands the first time `coh` runs against this branch (or a successor).
