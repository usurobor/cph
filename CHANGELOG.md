# Changelog

Project changelog: what shipped, what changed, what's still open. Empirical state lives in the latest merged field report; live operational status lives in [PROJECT.md](PROJECT.md); the gate-based roadmap lives in [ROADMAP.md](ROADMAP.md).

## 0.2.0 — Coherence drift sweep + docs refactor (2026-05-18)

- **Empirical state:** REVISE — unchanged from [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md). The active blocker is gait-cycle segmentation on real Mocap heel-marker data (R2 in [`ROADMAP.md`](ROADMAP.md)).
- **Decision:** Two coherence-drift-sweep waves landed against R0 (masters cph#16 and cph#21). Documentation refactor consolidated process artifacts under `.cdr/` and removed the public doctrine doc; coherence measurement runs as operational machinery (`scripts/measure-coherence.sh`, `targets/*.tsc`, `.github/workflows/coherence.yml`).

### Changed

- **F1–F6 (master cph#16, four subs cph#17–20):** broken realization ref fixed; `field-report-02` name collision resolved (R5 stub kept at -02, construct evaluation renamed to -03); schema/code column alignment in `analysis/feature-table-schema.md` + `analysis/features.md` against `scripts/features.py`; first-pass vs candidate feature distinction made explicit; legacy `gait-support-paths-features/` path renamed to `cph-features/` in live surfaces.
- **F7–F11 (master cph#21, four subs cph#22–25):** `scripts/segmentation.py` `quality_flag` literals now emit `"ok"`/`"short"`/`"long"` (was only `"ok"`/`"out_of_range"` while schema claimed three values); `analysis/feature-table-schema.md` + `analysis/features.md` realigned to the code; PROJECT.md §"Active branch / issue" + ROADMAP.md R0 §"Next action" / §"Owning files" de-staled; `reports/field-report-02-friend-pre-pilot.md` H1 number prefix matches filename; `scripts/features.py::extract_shape` renamed to `extract_shape_sentinel` (placeholder semantics signaled in the name).
- **Docs refactor:** `CDR.md` removed; `.cdd/` renamed to `.cdr/` (project history preserved); PROJECT.md / ROADMAP.md / CHANGELOG.md reframed. Coherence machinery (`scripts/measure-coherence.sh`, `targets/*.tsc`) preserved as operational infrastructure. `.github/workflows/coherence.yml` added — runs coherence measurement on every tagged release; reports upload as a workflow artifact for the operator to read when appending the row to `.cdr/coherence-log.md`.

### Known limits

- **No new empirical claims.** Two qualitative waves and one docs refactor. No clustering, no participant data, no field-report content edits. Empirical state remains REVISE per the latest merged field report.
- **R2 segmentation remains the empirical blocker.** The existing-data zeroth pilot is REVISE pending a bounded fix to `scripts/segmentation.py::detect_heel_strikes`. The branch `origin/cycle/segmentation-real-data-fix` is unmerged; that merge decision is orthogonal to this wave.

### Next gate

R2 — segmentation reliability on real Mocap heel-marker data (see [`ROADMAP.md`](ROADMAP.md) §"Phase R2"). The next changelog entry should land at the close of that bounded cycle.

## 0.1.0 — Initial charter (2026-05-18)

Initial repo refactor establishing the charter, hypothesis doc, support-path doc, failure-conditions doc, seven-families article, and ROADMAP. Historical wave artifacts live under `.cdr/waves/cdr-refactor-2026-05-18/` and `.cdr/unreleased/{12,13,14,15}/`.

- **Empirical state:** REVISE — per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) (2026-05-17 real-data run). Preserved verbatim by the refactor.
- **Decision:** Repo refactored into a charter + roadmap + changelog + gates project. Hypothesis, methods, evidence, and process surfaces partitioned into single owners.

### Changed

- [`README.md`](README.md) states the Coherence Path Hypothesis explicitly, distinguishes it from `support path`, names the seven gait families as observational vocabulary, and carries the source-of-truth table.
- [`docs/concepts/coherence-path-hypothesis.md`](docs/concepts/coherence-path-hypothesis.md) introduced as the hypothesis authority.
- [`docs/articles/seven-ways-people-walk.md`](docs/articles/seven-ways-people-walk.md) introduced as the seven-families observational reference.
- [`ROADMAP.md`](ROADMAP.md) introduced with gate-based phases R0–R6.
- `CHANGELOG.md` introduced (this file).
- [`PROJECT.md`](PROJECT.md) repartitioned to current operational status only.
