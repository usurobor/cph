# Cross-Repo Lineage: cph → cnos (bootstrap-cdr)

Bilateral-trace anchor on cph main confirming the cross-repo proposal has landed on cnos main. The full original bundle lives on the dormant cph branch + on cnos main; this file is the cph-main-side discoverability anchor.

## Source

- **Repo:** `usurobor/cph` (renamed 2026-05-18 from `usurobor/gait-support-paths`; bundle authored under the prior name)
- **Branch:** `claude/acquire-test-set-model-60jZ2` (intentionally on-branch-only; never merged to cph main — this LINEAGE.md is the cph-main-side trace, not the bundle)
- **Authoring commit:** `774427b` (initial bundle filing, under prior repo name)
- **Latest mirror-state commit:** `333dbeb` (rename-event update; predicts canonical `cph/`-named cnos-side path)
- **Branch bundle path:** `.cdd/iterations/cross-repo/cnos/bootstrap-cdr/` (full bundle: `ISSUE.md`, `LINEAGE.md`, `README.md`, `STATUS`, `FEEDBACK-from-cnos.patch`)

## Target

- **Repo:** `usurobor/cnos`
- **Issue:** [#376](https://github.com/usurobor/cnos/issues/376) — Bootstrap cnos.cdr — research protocol package
- **Mode:** master/tracking issue (`docs-only`); sub-issues to be filed and dispatched separately by cnos δ + γ
- **Disposition:** accepted (body filed verbatim from source `ISSUE.md` @ `774427b`; `## Source Proposal` block inserted at canonical position per `cdd/issue/SKILL.md`)
- **First filing branch:** `claude/file-cnos-cdr-issue-fi9Ld` (cnos commit `892a429`; stale-named, superseded)
- **Canonical landing on main:** `cnos:.cdd/iterations/cross-repo/cph/bootstrap-cdr/` @ cnos commit `7a7f7152` (γ-as-δ direct-to-main; 2026-05-18)
- **Canonical-side LINEAGE.md:** `cnos:.cdd/iterations/cross-repo/cph/bootstrap-cdr/LINEAGE.md` @ `7a7f7152`

## Bilateral trace

The branch-side source lineage at `usurobor/cph:.cdd/iterations/cross-repo/cnos/bootstrap-cdr/LINEAGE.md` (commit `333dbeb`, branch `claude/acquire-test-set-model-60jZ2`) named the target as `cnos#376` and predicted the canonical cnos-side path as `cnos:.cdd/iterations/cross-repo/cph/bootstrap-cdr/`. cnos commit `7a7f7152` fulfilled that prediction.

This cph-main-side file is the post-closure bilateral-trace anchor — symmetric to the cnos-main-side LINEAGE.md, minimal-shape per the `cnos:.cdd/iterations/cross-repo/tsc/cdd-supercycle/LINEAGE.md` precedent. The cph wave `cdr-refactor-2026-05-18` (closed at cph commit `42466ad`) listed cnos-side ingestion under §"Out of scope" as cross-repo work owned by cnos δ; that work is now complete, and this commit closes the cph-side complement.

## Repository rename event

On 2026-05-18, the source repo was renamed `usurobor/gait-support-paths` → `usurobor/cph` (pre-`cph#11` chore; Coherence Path Hypothesis acronym, matching cnos / tsc convention). GitHub auto-redirect resolves historical URLs under both names.

The branch-side `LINEAGE.md` @ `333dbeb` documents the rename consequences for the bundle in full; this anchor preserves the pointer rather than restating them.

## Per-sub confirmation

Master is a scope envelope; subs land independently as the cnos.cdr v0.1 wave subs close.

| Sub | Proposed shape | cnos issue # | cnos commit | Status |
|---|---|---|---|---|
| Sub 1 | Draft + ratify cdr's six-field instantiation contract (`design-and-build`) | TBD | TBD | not yet filed |
| Sub 2 | Bootstrap `cnos.cdr` package skeleton + `CDR.md` + `SKILL.md` (`MCA`, cites Sub 1) | TBD | TBD | not yet filed |
| Sub 3 | Role overlays in `skills/cdr/{alpha,beta,gamma,operator,epsilon}/SKILL.md` (`design-and-build`) | TBD | TBD | not yet filed |
| Sub 4 | Empirical-anchor doc mapping the cph zeroth-pilot wave + segmentation-fix cycle to cdr v0.1 surface (`docs-only`); proposed filename `cnos.cdr/docs/empirical-anchor-cph.md` | TBD | TBD | not yet filed |

Proposed shapes are non-binding; cnos δ has authoring freedom to re-shape, split, or merge.

## Archival

Per `cdd/post-release/SKILL.md` Step 5.6b: once cnos.cdr v0.1 wave closes (all four subs landed on cnos main), the dormant cph branch + this cph-main-side anchor may both be archived. Until then, both remain as the durable cph-side trace of the cross-repo handshake.

Authored by δ on 2026-05-18 (cph-main-side bilateral closure for the bootstrap-cdr cross-repo proposal).
