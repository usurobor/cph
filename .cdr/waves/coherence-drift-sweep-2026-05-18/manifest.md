# Wave: Coherence drift sweep (master cph#16)

**Date:** 2026-05-18
**Dispatcher:** δ-as-agent (γ=δ permitted at this scale per `cdd/operator/SKILL.md` §5.2)
**Repo:** usurobor/cph
**Master:** cph#16 (8 ACs across F1–F6; kind=review-and-patch; label: cdd) — stays open until subs close
**Origin:** post-CDR-refactor coherence review (master cph#11 wave `cdr-refactor-2026-05-18` shipped 2026-05-18; sweep run same day on `claude/review-repo-coherence-PNbjQ` flagged six findings)
**Five-factor heuristic outcome:** split — partial signals on (a) ≥4 files touched per sub, (e) findings ship independently and have distinct review surfaces; weak signals on (b) ≥4 modules touched, (c) lifecycle span. Single-cycle path is viable; split chosen to honor identity-isolation per finding axis (α / β / γ) and to make per-finding review surface auditable.

## Issues (ordered; D depends on nothing; all four parallelizable by file-disjointness)

| Order | # | Title | Findings from #16 | Mode | Type | Depends on |
|-------|---|-------|-------------------|------|------|------------|
| 1 | 17 | Sub A — F1 + F6: broken realization ref + PROJECT.md R0 wording | F1, F6 | docs-only | docs | — |
| 2 | 18 | Sub B — F2: field-report-02 name collision in ROADMAP.md | F2 | docs-only (design call) | docs | — |
| 3 | 19 | Sub C — F3 + F5: schema/code column alignment + features.md first-pass vs candidate | F3, F5 | docs + code | docs + code | — |
| 4 | 20 | Sub D — F4: rename legacy `gait-support-paths-features/` path in live surfaces | F4 | docs + code | docs + code | — |

A/B/C/D are parallelizable — they touch disjoint file sets (see below). No sub depends on another's merge.

### File-disjointness check (A/B/C/D)

- **Sub A** touches: `ROADMAP.md` (one-line edit at L85), `PROJECT.md` (§"Current stage" wording).
- **Sub B** touches: `ROADMAP.md` (L66, L83, L87 — three references to `field-report-02`).
- **Sub C** touches: `analysis/feature-table-schema.md`, `analysis/features.md`, `scripts/features.py`, possibly `scripts/build_notebook.py`.
- **Sub D** touches: `scripts/io_opencap.py` (comment), `scripts/build_notebook.py` (two lines), `notebooks/README.md`, `analysis/feature-summary-zeroth-pilot.md`, regenerated `notebooks/existing-data-processing.ipynb`.

**Two conflict surfaces:**

1. **`ROADMAP.md`** is touched by both Sub A and Sub B. Edits are on disjoint lines (Sub A at L85, Sub B at L66 / L83 / L87) — non-conflicting under git's three-way merge. Sub A and Sub B may proceed in parallel; whichever lands second rebases trivially.
2. **`scripts/build_notebook.py`** is touched by Sub D (paths) and potentially Sub C if the F3 choice renames columns that appear in the generated code. If Sub C's direction is "rename code columns," Sub C touches the *column-name strings* (lines defining the dataframe columns) and Sub D touches the *path strings* (lines L307 + L382). These are disjoint lines and conflict-free. If Sub C's direction is "shrink the schema doc," Sub C does not touch `scripts/build_notebook.py` at all.

No `gamma-coordination.md` write is required across the wave; the file-line disjointness is sufficient.

## Pinned file paths (forward-reference contract)

All four subs touch existing files only. No new file is created by this wave. There are therefore no forward-referenced paths to pin.

The new directory name chosen by Sub D's α is **not** pinned in this manifest because it lives entirely inside Sub D's surface — no other sub references the on-disk feature output path. Sub D's α picks freely from the two recommendations in cph#20 §"Source of truth" (`cph-features/` or `gait-cycle-features/`) and records the choice in `self-coherence.md` §ACs.

The F3 direction chosen by Sub C's α (column rename vs schema shrink) similarly lives inside Sub C's surface. β verifies whichever direction was chosen against the AC1 oracle.

## Standing permissions

- Push to dispatch branch: **yes** — branch is `claude/review-repo-coherence-PNbjQ` (see §"Branching deviation" below)
- Push merges to main: **NO** — operator gate (this wave lands on a review branch first, not main)
- Auto-dispatch α fix rounds on β REQUEST CHANGES: yes (max 3 per sub)
- Tag/release: NO — operator gate
- Branch delete after merge: N/A (no per-cycle branches under §"Branching deviation")
- Install Python packages: NO (this wave does not touch `requirements.txt`)
- Modify `requirements.txt`: NO
- Run `coh` (TSC CLI) in CI: best-effort — `coh` is not on PATH in this environment per cph#11's CHANGELOG `0.1.0-cdr` baseline; sweep is qualitative
- Cross-repo touches (`usurobor/cnos`): NO — out of scope; no cnos-side bundle paths need updating for this wave

## Branching deviation (this wave only)

The cph harness on `claude/review-repo-coherence-PNbjQ` restricts pushes to a single named branch. The standard wave dispatch model uses `cycle/{N}` branches per `cdd/operator/SKILL.md` §5.1 with `git merge --no-ff` into main per sub. This wave deviates as follows:

- All four sub-issues land their patches on a single working branch: `claude/review-repo-coherence-PNbjQ`.
- Per-sub artifacts under `.cdd/unreleased/{17,18,19,20}/` follow the standard structure (`self-coherence.md`, `beta-review.md`, `alpha-closeout.md`, `beta-closeout.md`).
- Each sub's "merge" is a commit-marker rather than a merge commit (e.g., a commit titled `Sub A close — cph#17` after β approves).
- Master closure happens via PR review on `claude/review-repo-coherence-PNbjQ` (operator gate).

Identity-isolation invariant (`α ≠ β within a single sub`) is preserved by using separate `Agent` subagent invocations with `isolation: "worktree"` for α and β within each sub. δ-as-agent orchestrates and writes the wave-closeout but does not perform α or β work within any sub.

If a future cph harness restores `cycle/{N}` push permissions, follow-on waves return to the standard model. This branching deviation is named in the wave-closeout's §"Out-of-scope follow-ups."

## Timeout budgets

| Role | Sub A | Sub B | Sub C | Sub D | Rationale |
|------|-------|-------|-------|-------|-----------|
| γ (=δ) | 600s | 600s | 900s | 900s | Sub C and Sub D touch code + docs; A and B are pure docs |
| α | 600s | 600s | 1500s | 1200s | Sub C's column-name decision + features.md cleanup is the heaviest authoring load |
| β | 300s | 300s | 600s | 600s | Review surface scales with α output |

All subs are scoped tightly (docs-only or docs + small code patches). No sub is MCA-eligible — no new spec / no clustering / no new feature is in scope.

## Known constraints

- **Empirical REVISE posture (master cph#16 AC7 + cph#11 §10).** No sub may overclaim the Coherence Path Hypothesis. The latest merged field report (`reports/field-report-01-existing-data-zeroth-pilot.md`, 2026-05-17) governs README / ROADMAP / PROJECT / CHANGELOG empirical-state language. None of these files is in scope for content edits this wave; only the F6 wording fix touches PROJECT.md §"Current stage" (and must not change empirical state).
- **No new features.** cph#19 (Sub C) cleans up the feature-table schema/code mismatch and the features.md catalog distinction; it does **not** add any new feature. cph#16 AC8 is the structural backstop.
- **Frozen field reports.** Historical references in `reports/field-report-01-existing-data-zeroth-pilot.md` (in particular L270 citing `gait-support-paths-features/`) are not edited by any sub. cph#20 (Sub D) explicitly scopes this out.
- **`coh` not on PATH.** No mechanical TSC measurement is run during or after this wave. The first numeric C_Σ baseline lands when `coh` is on PATH in an operator environment per the cph#11 wave's deferred follow-up. This wave's findings are qualitative.
- **Identity-isolation invariant.** α ≠ β within a single sub (hard rule per `cdd/CDD.md` §1.4). Realized via `Agent(isolation: "worktree")` invocations — each Agent call produces an independent context window and thus an independent identity. γ = δ permitted at this scale per `cdd/operator/SKILL.md` §5.2.

## Resumption / failure handling

- An α or β session that hits the Agent timeout follows `cdd/operator/SKILL.md` §8 timeout-recovery: γ reads the partial artifact, re-dispatches if recoverable, marks the sub `failed` if not.
- A sub closed as **failed** triggers γ to write a master-comment naming the failure; Sub D's scope adjusts only if F4 itself fails (the other subs are independent).
- A sub closed as **deferred** is named in master cph#16's closure comment as tracked debt; the master does not auto-close until all subs are terminal.

## Out-of-scope follow-ups (named, not in this wave)

- First mechanical `coh --mode mechanical` run + recording the numeric α/β/γ/C_Σ baseline into `CHANGELOG.md` (still gated on `coh` being on PATH; this is the same deferred item the cph#11 wave named).
- Migration of operator-side on-disk data from `gait-support-paths-features/` to whatever name Sub D's α chooses. Operators continue to override via `GAIT_DATA_ROOT` until they switch.
- Restoration of `cycle/{N}` push permissions (harness-side, not in this wave's scope).
- Body edit of master cph#16 (left as as-filed; sub-issue links are tracked in cph#16 comments + this manifest).
- Any new feature implementation gated by cph#19 AC3 (out of scope of this wave; eligible for a future cycle).
