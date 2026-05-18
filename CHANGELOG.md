# Changelog

This changelog records research coherence deltas, not software releases. It is the project's **coherence ledger**: each entry names whether the project still describes one coherent research system as it changes, and what moved across the three TSC axes (α pattern, β evidence relation, γ process — see [CDR.md](CDR.md)).

A high C_Σ here does **not** validate the [Coherence Path Hypothesis](docs/concepts/coherence-path-hypothesis.md). It means the repo currently describes one coherent research project. A low C_Σ blocks empirical claims until the project re-coheres. See [CDR.md](CDR.md) §"C_Σ in this repo" for the full distinction.

Empirical state lives in the latest merged field report; live operational status lives in [PROJECT.md](PROJECT.md); the gate-based roadmap lives in [ROADMAP.md](ROADMAP.md). This file records the deltas between those surfaces over time.

## Research coherence ledger

| Entry | Date | Empirical state | α | β | γ | C_Σ | Bottleneck | Decision |
|---|---|---|---:|---:|---:|---:|---|---|
| 0.1.0-cdr | 2026-05-18 | REVISE | pending | pending | pending | pending — coh unavailable | not measured | refactor merged; baseline measurement deferred until `coh` is installed |

## 0.1.0-cdr — CDR refactor

- **Date:** 2026-05-18
- **Level:** repo-identity refactor (no empirical change)
- **Empirical state:** REVISE — unchanged from [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) (2026-05-17 real-data run). The Coherence Path Hypothesis is not validated; it is also not refuted. The active blocker is gait-cycle segmentation on real Mocap heel-marker data (R2 in [`ROADMAP.md`](ROADMAP.md)).
- **Decision:** Repo refactored into a model CDR project. Hypothesis, methods, evidence, and process surfaces re-partitioned into single owners. The Coherence Path Hypothesis is now explicit in the public charter. Empirical posture is preserved verbatim.

### Coherence delta

- **α (hypothesis pattern):** pending — `coh` not installed in this environment. Qualitatively, this wave establishes the first stable α surface: the hypothesis authority doc owns the claim, the support-path doc owns the operational term, and the seven-families article owns the observational vocabulary. The α-axis distinction the project most depends on — `Coherence Path Hypothesis` (the claim) vs `support path` (the operationalized pattern) — is now explicit in [`README.md`](README.md) and [`CDR.md`](CDR.md).
- **β (evidence relation):** pending — `coh` not installed. Qualitatively, the README empirical-state language matches [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md); [`ROADMAP.md`](ROADMAP.md) cites field-report-01 by name for R1 / R2 status; the analysis target manifest names the durable feature summary that the notebook actually emits.
- **γ (process):** pending — `coh` not installed. Qualitatively, this wave introduces the process surfaces CDR.md prescribes — ROADMAP gates, this CHANGELOG ledger, TSC target manifests, and a measurement entrypoint — none of which existed before the wave. [`PROJECT.md`](PROJECT.md) is repartitioned to current-status-only so that it no longer duplicates roadmap content.
- **C_Σ:** `pending — coh unavailable`. Baseline measurement deferred until `coh` is installed; the entrypoint is in place ([`scripts/measure-coherence.sh`](scripts/measure-coherence.sh)) and runs against the four targets registered in [`targets/registry.tsc`](targets/registry.tsc) once the CLI is on PATH.
- **Bottleneck:** not measured (no axis scores). The current empirical bottleneck remains R2 segmentation, but that is not a coherence-axis bottleneck.

### Changed

- [`README.md`](README.md) now states the Coherence Path Hypothesis explicitly, distinguishes it from `support path`, names the seven gait families as observational vocabulary rather than authority, and carries the source-of-truth table for the wave (Sub A).
- [`docs/concepts/coherence-path-hypothesis.md`](docs/concepts/coherence-path-hypothesis.md) introduced as the hypothesis authority (Sub A).
- [`docs/articles/seven-ways-people-walk.md`](docs/articles/seven-ways-people-walk.md) introduced as the seven-families observational reference (Sub A).
- [`CDR.md`](CDR.md) introduced as the coherence-driven-research doctrine (Sub A).
- [`ROADMAP.md`](ROADMAP.md) introduced with gate-based phases R0–R6 and current status per phase (Sub B).
- `targets/registry.tsc` and `targets/{hypothesis,method,evidence,repo}.tsc` introduced as the TSC target manifests for mechanical coherence measurement (this sub, Sub C).
- [`scripts/measure-coherence.sh`](scripts/measure-coherence.sh) introduced as the mechanical TSC measurement entrypoint (this sub, Sub C). Exits with installation instructions when `coh` is not on PATH.
- `CHANGELOG.md` (this file) introduced as the research coherence ledger (this sub, Sub C).
- [`PROJECT.md`](PROJECT.md) repartitioned to current operational status only; the implementation timeline, realizations narrative, friend pre-pilot overview, risk-management section, and source-of-truth table moved out of `PROJECT.md`. Roadmap content now lives in `ROADMAP.md`; coherence-ledger content lives in this file; the source-of-truth table is owned by `README.md` (this sub, Sub C).
- `.gitignore` excludes `.tsc/` (this sub, Sub C). Mechanical-mode output is the measurement record, not a canonical source.

### Known limits

- **Coherence score is not empirical validation.** A high C_Σ does not validate the Coherence Path Hypothesis. It only certifies that the repo currently describes one coherent research project. Empirical validation lives in field reports against the falsification table in [`docs/concepts/support-path.md`](docs/concepts/support-path.md) §Falsification and [`docs/concepts/failure-conditions.md`](docs/concepts/failure-conditions.md).
- **`coh` is not installed in the cycle dispatch environment.** This baseline entry carries `pending — coh unavailable` for α / β / γ / C_Σ. The first numeric C_Σ baseline lands the first time `coh` runs against this branch (or a successor of it).
- **No new empirical claims.** This wave is a repo-identity refactor. No clustering was run, no participants were recruited, no field report was rewritten. The empirical state remains REVISE per the latest merged field report. The seven gait families remain observational vocabulary, not proven categories.
- **R2 segmentation remains the empirical blocker.** The existing-data zeroth pilot is REVISE pending a bounded fix to `scripts/segmentation.py::detect_heel_strikes`. The branch `origin/cycle/segmentation-real-data-fix` is unmerged; that merge decision is orthogonal to this wave.

### Next gate

R0 (charter and operationalization) closes when the AC8 / AC9 / AC10 conformance sweep (Sub D of master cph#11) passes against the merged A+B+C surfaces. The first numeric C_Σ baseline lands when `coh` is available; until then, the entrypoint and target manifests are in place and the ledger row carries `pending — coh unavailable`.

After R0 closes, the next gate is R2 — segmentation reliability on real Mocap heel-marker data (see [`ROADMAP.md`](ROADMAP.md) §"Phase R2"). The next changelog entry should land at the close of that bounded cycle.
