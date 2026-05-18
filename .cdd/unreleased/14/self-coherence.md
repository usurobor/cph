<!--
sections_planned: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness]
sections_completed: [Gap]
-->

# self-coherence — cph#14 (Sub C — TSC targets + measure-coherence.sh + CHANGELOG baseline + PROJECT.md repartition)

## Gap

**Issue:** [usurobor/cph#14](https://github.com/usurobor/cph/issues/14) — Sub C of master [cph#11](https://github.com/usurobor/cph/issues/11). Wave [`cdr-refactor-2026-05-18`](../../waves/cdr-refactor-2026-05-18/manifest.md).

**Version / mode:** MCA-eligible (the TSC target-manifest registry format string `tsc-target-registry/0.1` is pinned in master cph#11 §"Required changes" item 6; `scripts/measure-coherence.sh` shape is fully specified in item 7; PROJECT.md repartition is mechanical given Sub A's and Sub B's merged surfaces).

**What was missing on `origin/main`:**

- No `targets/` directory. No TSC target manifests. Without them, `coh` has nothing to measure and CDR.md's required cadence is non-runnable.
- No `scripts/measure-coherence.sh`. The C_Σ cadence CDR.md prescribes has no entrypoint.
- No `CHANGELOG.md`. The research coherence ledger has no baseline. Without it, future waves have nothing to delta from.
- `PROJECT.md` doubled as a roadmap (R1 status + implementation timeline + realizations narrative + friend pre-pilot overview + risk management + source-of-truth table) and a status surface. With `ROADMAP.md` now owning gates (Sub B) and the source-of-truth table now owned by `README.md` (Sub A), `PROJECT.md` carrying that content is duplication.

**What this sub adds:**

- `targets/registry.tsc` + `targets/{hypothesis,method,evidence,repo}.tsc` — TSC target manifests with `.tsc/**` excluded from canonical sources.
- `scripts/measure-coherence.sh` — executable, mechanical-mode entrypoint with clear missing-`coh` failure.
- `CHANGELOG.md` — baseline 0.1.0-cdr entry; α/β/γ/C_Σ = `pending — coh unavailable`; explicit "Coherence score is not empirical validation".
- `PROJECT.md` repartitioned to current-operational-status only (seven fields per AC-PROJECT invariant).
- `.gitignore` — `.tsc/` excluded so mechanical-mode output does not pollute the index.

**Boundary:** this sub does not touch the empirical posture (REVISE, per the latest merged field report), does not run clustering, does not modify `requirements.txt`, and does not edit Sub A / Sub B surfaces (`README.md`, `CDR.md`, hypothesis doc, seven-families article, `ROADMAP.md`).
