# Cross-Repo Lineage: cph (formerly gait-support-paths) → cnos (bootstrap-cdr)

## Source

- **Repo:** `usurobor/cph` (renamed 2026-05-18 from `usurobor/gait-support-paths`; bundle was authored under the prior name)
- **Branch:** `claude/acquire-test-set-model-60jZ2`
- **Commit:** `774427b` (authoring commit that landed the bundle; SHA fill-in landed in immediate follow-up commit `c8121ec`)
- **Path:** `.cdd/iterations/cross-repo/cnos/bootstrap-cdr/`

## Target

- **Repo:** `usurobor/cnos`
- **Issue:** `cnos#376` (filed 2026-05-18 by cnos γ; master/tracking issue for the cnos.cdr v0.1 wave)
- **Filing commit (cnos branch):** `892a429` on `claude/file-cnos-cdr-issue-fi9Ld`
- **Wave:** TBD (cnos δ assigns when dispatching subs)
- **Patches landed:** N/A on this bundle — this is a master-issue scope envelope; implementation lands across sub-issues authored by cnos γ + α.

## Bilateral trace

This is the source-side lineage at `usurobor/cph:.cdd/iterations/cross-repo/cnos/bootstrap-cdr/LINEAGE.md` (filed 2026-05-18; repo was named `gait-support-paths` at filing time and renamed to `cph` the same day, so historical commit references resolve under both names via GitHub's automatic redirect). The cnos-side mirror exists at `usurobor/cnos:.cdd/iterations/cross-repo/gait-support-paths/bootstrap-cdr/LINEAGE.md` on branch `claude/file-cnos-cdr-issue-fi9Ld` (cnos commit `892a429`) — that path is now stale-named and should be `cnos:.cdd/iterations/cross-repo/cph/bootstrap-cdr/` once cnos γ amends the branch or lands a follow-up. Per `cdd/post-release/SKILL.md` Step 5.6b, once the cnos-side mirror lands on cnos main + the cnos.cdr wave closes, this source-side copy may be archived.

cnos γ emitted a `FEEDBACK.patch` (cdd/gamma/SKILL.md §"Cross-repo proposal close-out" option (b)) because the cnos session was scoped to `usurobor/cnos` only. The patch is preserved here at `FEEDBACK-from-cnos.patch` for audit; it appended the `accepted` event to source `STATUS`.

## Repository rename event

On 2026-05-18 (same day as bundle filing + cnos#376 acceptance), the source repo was renamed `usurobor/gait-support-paths` → `usurobor/cph`. The rename is a pre-`cph#11` chore aligning the repo name with its identity as a reference cnos.cdr (Coherence Path Hypothesis) project, matching the cnos / tsc compact-acronym style.

Consequences for this bundle:

- **Bundle path is unchanged** (`.cdd/iterations/cross-repo/cnos/bootstrap-cdr/` under the source repo); only the source repo's name changed.
- **`ISSUE.md` is preserved verbatim** as filed at `774427b` under the prior name — modifying it would diverge from cnos's filed copy of `cnos#376`'s body. The text inside still reads `usurobor/gait-support-paths` in several places; those references are historical and resolve under both names via GitHub's automatic redirect.
- **`README.md` + `LINEAGE.md` updated** to reflect the new name in go-forward references; rename event annotated.
- **`STATUS` untouched** — the rename is not a proposal-lifecycle event (not one of `submitted | accepted | modified | rejected | landed`).
- **Cnos-side mirror path is stale** at `cnos:.cdd/iterations/cross-repo/gait-support-paths/bootstrap-cdr/` on branch `claude/file-cnos-cdr-issue-fi9Ld`. Either cnos γ amends the branch (`git mv`) before merging, or the cnos-side bundle moves to `…/cph/bootstrap-cdr/` in a follow-up. Not a blocker — the bundle's contents are intact.
- **`cnos#376` body** references `usurobor/gait-support-paths`; GitHub redirects cover the URLs and the references stand as historical for the issue's filing time.

## Per-sub confirmation

To be filled by cnos γ once sub-issues are filed and land. The master `ISSUE.md` proposes four non-binding sub shapes; cnos δ has authoring freedom to re-shape, split, or merge.

| Sub | Description | cnos issue # | cnos commit | Status |
|-----|-------------|--------------|-------------|--------|
| 1 | Draft + ratify cdr's 6-field instantiation contract | TBD | TBD | proposed |
| 2 | Bootstrap `cnos.cdr` package skeleton + `CDR.md` + `SKILL.md` | TBD | TBD | proposed |
| 3 | Role overlays (`skills/cdr/{alpha,beta,gamma,operator,epsilon}/SKILL.md`) | TBD | TBD | proposed |
| 4 | Empirical-anchor doc (`cnos.cdr/docs/empirical-anchor-cph.md`; proposed filename was `…-gait-support-paths.md` pre-rename — cnos γ chooses the final filename when filing Sub 4) | TBD | TBD | proposed |
