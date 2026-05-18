<!--
sections_planned: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness]
sections_completed: [Gap, Skills]
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

## Skills

**Tier 1 — canonical lifecycle and α role:**

- `CDD.md` — lifecycle, role contract, artifact-location matrix.
- `cdd/alpha/SKILL.md` — α algorithm (load order, dispatch intake, artifact order, peer enumeration, harness audit, self-coherence, pre-review gate, request review, close-out).

α lifecycle sub-skills were *not* additionally loaded for this cycle:

- `cdd/design/SKILL.md` — not loaded; **design not required**. The TSC target-manifest format (`tsc-target-registry/0.1`), the four-target slicing (hypothesis / method / evidence / repo), and the `measure-coherence.sh` shape are all specified in master cph#11 §"Required changes" items 6–7. PROJECT.md repartition is mechanical given the AC-PROJECT invariant. No impact graph to design.
- `cdd/plan/SKILL.md` — not loaded; **plan not required**. The eight file touches are independent of each other except for one forward reference (`targets/repo.tsc` → `CHANGELOG.md`, resolved by introducing `CHANGELOG.md` in the same diff). Sequencing was trivial.
- `cdd/issue/SKILL.md` — not loaded; the issue body is the AC contract and the wave manifest pins the forward-reference paths.

**Tier 2 — always-applicable engineering skills:**

- No cph-local `eng/*` skill tree exists in this repo (`ls .cdd` shows `iterations/` and `unreleased/` only; no `skills/eng/`). Tier 2 in this dispatch reduces to the implicit Tier-2 conventions from the cph codebase itself (set -euo pipefail in shell, Python module style for sibling scripts, Markdown table-and-section style from Sub A/B authoring).

**Tier 3 — issue-specific:**

- Bash discipline applied directly (no cph-local `eng/bash` skill present): `#!/usr/bin/env bash`, `set -euo pipefail`, `command -v` for the missing-tool guard, explicit exit codes (127 for missing executable, 2 for missing registry file), `bash -n` syntax check before commit.
- Markdown discipline applied directly (no cph-local `eng/markdown` skill present): table-and-section style consistent with the merged Sub A / Sub B surfaces; one-line ledger row + multi-section detail per CHANGELOG.md baseline entry; intra-doc forward references via `[text](path)`.

**Generation constraints loaded from the wave manifest (binding):**

1. `.tsc/**` must not appear as a canonical source in any target — applied in all five `targets/*.tsc` files; comment preambles in `registry.tsc` and `repo.tsc` make the exclusion explicit; `.gitignore` carries the same exclusion to keep mechanical-mode output out of the index.
2. `CHANGELOG.md` C_Σ cell carries `pending — coh unavailable` if mechanical-mode cannot run — applied; `coh` is not installed in the dispatch environment, the ledger row carries that literal string, and §Coherence delta says `pending — coh unavailable` per axis.
3. "Coherence score is not empirical validation" must appear under Known limits in the baseline entry — applied verbatim as the first §Known limits bullet of the 0.1.0-cdr entry.
4. `PROJECT.md` must not become a second roadmap surface — applied; the seven fields named in AC-PROJECT are the only sections in the new `PROJECT.md`; roadmap content has been removed; `PROJECT.md` points to `ROADMAP.md` and `CHANGELOG.md` rather than restating their content.
5. No empirical overclaim — applied; CHANGELOG and PROJECT preserve REVISE; no validation language anywhere in the diff.

**Forward-reference contract from the wave manifest:**

- `targets/hypothesis.tsc` must reference exactly: `README.md`, `CDR.md`, `ROADMAP.md`, `docs/concepts/coherence-path-hypothesis.md`, `docs/concepts/support-path.md`, `docs/concepts/gait-cycle-as-unit.md` (only if present), `docs/concepts/failure-conditions.md` (only if present), and Sub A's chosen seven-gait-families path. Verified: all eight files present on disk (`ls docs/concepts/` returns the four concept docs; `ls docs/articles/seven-ways-people-walk.md` resolves); the `sources` array in `targets/hypothesis.tsc` lists exactly these eight paths in this order.
- `PROJECT.md` must point to `ROADMAP.md` and `CHANGELOG.md` but must not duplicate them — verified by reading the rewritten `PROJECT.md` end-to-end.
