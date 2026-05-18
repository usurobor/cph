# Cross-Repo Lineage: gait-support-paths → cnos (bootstrap-cdr)

## Source

- **Repo:** `usurobor/gait-support-paths`
- **Branch:** `claude/acquire-test-set-model-60jZ2`
- **Commit:** `774427b` (authoring commit that landed the bundle; this SHA fill-in lands in the immediate follow-up commit)
- **Path:** `.cdd/iterations/cross-repo/cnos/bootstrap-cdr/`

## Target

- **Repo:** `usurobor/cnos`
- **Issue:** `cnos#376` (filed 2026-05-18 by cnos γ; master/tracking issue for the cnos.cdr v0.1 wave)
- **Filing commit (cnos branch):** `892a429` on `claude/file-cnos-cdr-issue-fi9Ld`
- **Wave:** TBD (cnos δ assigns when dispatching subs)
- **Patches landed:** N/A on this bundle — this is a master-issue scope envelope; implementation lands across sub-issues authored by cnos γ + α.

## Bilateral trace

This is the source-side lineage at `usurobor/gait-support-paths:.cdd/iterations/cross-repo/cnos/bootstrap-cdr/LINEAGE.md` (filed 2026-05-18). The cnos-side mirror exists at `usurobor/cnos:.cdd/iterations/cross-repo/gait-support-paths/bootstrap-cdr/LINEAGE.md` on branch `claude/file-cnos-cdr-issue-fi9Ld` (cnos commit `892a429`). Per `cdd/post-release/SKILL.md` Step 5.6b, once the cnos-side mirror lands on cnos main + the cnos.cdr wave closes, this source-side copy may be archived.

cnos γ emitted a `FEEDBACK.patch` (cdd/gamma/SKILL.md §"Cross-repo proposal close-out" option (b)) because the cnos session was scoped to `usurobor/cnos` only. The patch is preserved here at `FEEDBACK-from-cnos.patch` for audit; it appended the `accepted` event to source `STATUS`.

## Per-sub confirmation

To be filled by cnos γ once sub-issues are filed and land. The master `ISSUE.md` proposes four non-binding sub shapes; cnos δ has authoring freedom to re-shape, split, or merge.

| Sub | Description | cnos issue # | cnos commit | Status |
|-----|-------------|--------------|-------------|--------|
| 1 | Draft + ratify cdr's 6-field instantiation contract | TBD | TBD | proposed |
| 2 | Bootstrap `cnos.cdr` package skeleton + `CDR.md` + `SKILL.md` | TBD | TBD | proposed |
| 3 | Role overlays (`skills/cdr/{alpha,beta,gamma,operator,epsilon}/SKILL.md`) | TBD | TBD | proposed |
| 4 | Empirical-anchor doc (`cnos.cdr/docs/empirical-anchor-gait-support-paths.md`) | TBD | TBD | proposed |
