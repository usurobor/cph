# Changelog

Project changelog: what shipped, what changed, what's still open. Empirical state lives in the latest merged field report; live operational status lives in [PROJECT.md](PROJECT.md); the gate-based roadmap lives in [ROADMAP.md](ROADMAP.md).

## 0.3.0 — R2 segmentation fix ported; status surfaces realigned (2026-05-19)

- **Empirical state:** REVISE — per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) (post-segmentation-fix run). R1 stays REVISE; the active blocker has moved from the detector to L-side cycle yield, which is structurally limited by trial cropping in the OpenCap Lab Validation archive (1/60 L cycles). R-side passes AC1 cleanly (60/60 trials, 100%; 61 cycles total = 60 R + 1 L).
- **Decision:** [cph#26](https://github.com/usurobor/cph/issues/26) ported the R2 detector fix from the precursor branch `origin/cycle/segmentation-real-data-fix` (tip `a95415c`) onto current main via per-file 3-way merge ([`cycle/port-segmentation-fix`](https://github.com/usurobor/cph/tree/cycle/port-segmentation-fix), Step A `41b3693`). Step B regenerated and re-executed [`notebooks/existing-data-processing.ipynb`](notebooks/existing-data-processing.ipynb) against `/opt/gait-data/opencap-lab-validation/extracted/` and realigned the status surfaces (this entry, PROJECT.md, ROADMAP.md) to the post-fix field report. R2 transitions REVISE → GO; R1 holds REVISE.

### Changed

- `scripts/segmentation.py` — detector rewritten: robust-percentile normalization (`yn = (smoothed_heel − q05) / (q95 − q05)`) plus stance-region depth/length gating (`yn < 0.30` for ≥150 ms AND `< 0.10` at deepest). Invariant to absolute height, baseline offset, and amplitude. Works on real Mocap calcaneus markers (range ~[50, 330] mm, ~25 mm R/L baseline offset) and on the synthetic generator's clipped-to-zero plateau. The `quality_flag` tri-value (`"ok"`/`"short"`/`"long"` from cph#22) preserved.
- `scripts/segmentation_diagnostics.py` — new per-(trial, side) diagnostic utility that classifies zero-cycle reasons (`trial_ends_mid_swing`, `trial_crops_only_swing`, `ok`) mechanically against the real archive. Used to characterize the L-side cropping constraint.
- `scripts/features.py` — adds frontal-plane `hip_adduction_range_deg` / `hip_adduction_peak_deg` / `hip_adduction_min_deg` and lumbar `lumbar_extension_range_deg` / `lumbar_bending_range_deg` / `lumbar_rotation_range_deg` columns. The `extract_shape_sentinel` name (from cph#25) preserved.
- `scripts/build_notebook.py` — integrates `scripts/segmentation_diagnostics.py` into the §"Known debt" segmentation cell.
- `notebooks/existing-data-processing.ipynb` — regenerated and executed on real data (60/60 R-side trials at 100% segmentation; 0.00% missingness across 35 columns × 61 cycles).
- `analysis/feature-summary-zeroth-pilot.md` — post-fix evidence summary (60 R cycles, 1 L cycle).
- [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) — rewritten to post-fix REVISE; supersedes the 18.3%-segmentation REVISE.
- [`PROJECT.md`](PROJECT.md) §"Current empirical decision" / §"Current blocker" / §"Next action" / §"Active branch / issue" / §"Last field report" — realigned to the post-fix evidence.
- [`ROADMAP.md`](ROADMAP.md) §"Current state" / R1 / R2 / R3 / R4 — realigned. R2 status transitions REVISE → GO. R1 stays REVISE pending L-cycle recovery.

### Known limits

- **L-side cycle yield is the new load-bearing bottleneck.** 1 L-cycle across 60 trials blocks Hypothesis 3 (asymmetric phase-coupling) and prevents L/R asymmetry features (the central bilateral surface of [`docs/concepts/support-path.md`](docs/concepts/support-path.md)). Recovery requires either (a) contralateral-anchored L-cycle detection (R HS times + half-stride offset) or (b) re-running OpenSim IK on the source TRC files with wider time windows. Both are out of scope for cph#26.
- **R-side n=60 is partial test surface.** Hypothesis 1 is evaluable on R-side data; Hypothesis 2 is partially evaluable on the 30 + 30 natural / trunk-sway R-side cycles; Hypothesis 3 is not testable on this archive.
- **No new empirical claims on the construct.** The hypothesis is still neither validated nor refuted. The R-side n=60 anchor is a partial test, not construct survival.

### Next gate

R3 — first construct-level evidence on R-side data (subject-level condition-response analysis per [`analysis/left-right-comparison.md`](analysis/left-right-comparison.md) and [`analysis/feature-table-schema.md`](analysis/feature-table-schema.md)). The next changelog entry should land at the close of either R3 (R-side construct-level analysis) or an L-cycle recovery cycle, whichever comes first.

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
