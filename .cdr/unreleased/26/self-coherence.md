# Self-coherence — cph#26 — Port segmentation-real-data-fix onto current main

## Gap

**Issue:** [usurobor/cph#26](https://github.com/usurobor/cph/issues/26) — Port segmentation-real-data-fix onto current main.
**Branch:** `cycle/port-segmentation-fix`.
**Mode:** empirical implementation port (not a new theory cycle).

**Pre-port state on `origin/main`** (verified by `git log` + `grep` at merge-base `ebd909c`):

- `scripts/segmentation.py::detect_heel_strikes` was tuned to the synthetic generator's heel-marker shape (range ~[0, 100] mm, zero baseline) and failed on real Mocap calcaneus markers (range ~[50, 330] mm, ~25 mm R/L baseline offset). Result on real data: 11 of 60 trials (18.3%, R-side only); 0 L-side cycles.
- `reports/field-report-01-existing-data-zeroth-pilot.md` documented the 18.3%-segmentation REVISE.
- `PROJECT.md` / `ROADMAP.md` / `CHANGELOG.md` named the detector as the active R2 blocker, with `origin/cycle/segmentation-real-data-fix` (tip `a95415c`) as the unmerged orthogonal branch carrying the fix.
- Main had advanced 114 commits past the segmentation-fix branch's base on charter / process surfaces: CPH/COG split, `.cdr/` rename, coherence machinery preserved as operational infrastructure (`scripts/measure-coherence.sh`, `targets/*.tsc`, `.github/workflows/coherence.yml`), `quality_flag` tri-value (`"ok"`/`"short"`/`"long"` from cph#22), `extract_shape` → `extract_shape_sentinel` rename (cph#25), `cph-features/` rename (cph#20). A fast-forward merge from the segmentation-fix branch would have clobbered every one of these.

**Required outcome.** Port the implementation + evidence changes (segmenter + diagnostics + features + build script + notebook + summary + field report) onto current `main` without regressing the charter / process surfaces; re-run the notebook against real data; realign status surfaces (PROJECT.md / ROADMAP.md / CHANGELOG.md) to the post-fix field-report-01 evidence; preserve the empirical REVISE posture (the detector fix is necessary but not sufficient for construct validation, because L-side cycle yield is structurally limited by trial cropping).

**Why it is α work, not a δ operator action.** The port is an implementation cycle: it produces new code (the detector rewrite + the diagnostics module) and new evidence (the post-fix field-report-01 + notebook outputs). δ stewards waves and dispatches; α implements within an issue's scope. cph#26 is a single-issue cycle with 6 ACs and a "Required approach" / "Steps" section that names the implementation operations. The earlier `δ-as-agent` author attribution on `41b3693` was a session-identity drift carried over from the prior wave's δ-as-agent role (`cdr-refactor-2026-05-18`); per `cdd/alpha/SKILL.md §2.6` row 14, retroactive identity correction via path (a) `git rebase --exec 'git commit --amend --reset-author --no-edit'` has been applied (commits rewritten to `Alpha <alpha@cph.cdd.cnos>`; force-with-lease push at `41b3693 → 9bcef90`, `9eb34ee → f27904a`).
