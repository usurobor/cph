# Wave: Coherence drift sweep follow-up (master cph#21)

**Date:** 2026-05-18
**Dispatcher:** δ-as-agent (γ=δ permitted at this scale per `cdd/operator/SKILL.md` §5.2)
**Repo:** usurobor/cph
**Master:** cph#21 (8 ACs across F7–F12; kind=review-and-patch; label: cdd) — stays open until subs close
**Origin:** post-`coherence-drift-sweep-2026-05-18` re-audit run on `claude/review-repo-coherence-PNbjQ` 2026-05-18, after the precursor wave (master cph#16) closed all four subs (cph#17–20) at APPROVE round 1. Re-audit verified F1–F6 stayed fixed and surfaced one new HIGH-severity β-axis bug the wave missed (F7) plus several confirmed cross-sub debt items (F8–F12).
**Five-factor heuristic outcome:** split — partial signals on (a) ≥4 files touched per sub, (e) findings ship independently and have distinct review surfaces; weak signals on (b) ≥4 modules touched, (c) lifecycle span. Single-cycle path is viable; split chosen to honor identity-isolation per finding axis (β-axis F7 / γ-axis F8+F9 / γ-axis F11 / β-axis F10), to make per-finding review surface auditable, and — most importantly — to give the F7 sub (cph#22) the β-side anchoring discipline that the precursor wave's bundled review surface obscured.

## Issues (ordered; all four parallelizable by file-disjointness)

| Order | # | Title | Findings from cph#21 | Mode | Type | Depends on |
|-------|---|-------|----------------------|------|------|------------|
| 1 | 22 | Sub A — F7: quality_flag schema↔code vocabulary alignment (lift code to schema) | F7 (HIGH, β-axis) | docs + code | docs + code | — |
| 2 | 23 | Sub B — F8 + F9: PROJECT.md §Active branch + ROADMAP.md R0 §Next action de-staling | F8, F9 (MEDIUM, γ-axis) | docs-only | docs | — |
| 3 | 24 | Sub C — F11: field-report-02 stub H1 number mismatch | F11 (LOW, γ-axis) | docs-only | docs | — |
| 4 | 25 | Sub D — F10: rename `extract_shape` to a placeholder-signaling name | F10 (MEDIUM, β-axis) | docs + code | docs + code | — |

A/B/C/D are parallelizable — they touch disjoint code surfaces (segmentation.py for A, features.py for D, no code for B/C). Sub A and Sub D share two markdown files but on disjoint line ranges (see §"File-disjointness check" below). No sub depends on another's merge. Under α-serial execution, Sub D rebases trivially on Sub A's edits to the shared docs.

**F12 is not a sub.** F12 is a policy decision (CHANGELOG entry for the precursor `coherence-drift-sweep-2026-05-18` wave) and lives as a master-comment item for ε/operator, per cph#21 §"Suggested sub-split" final paragraph. δ's recommendation is named in the wave-closeout §"Cross-sub findings" for ε to act on.

### File-disjointness check (A/B/C/D)

- **Sub A** touches: `scripts/segmentation.py` (line 122 `Cycle(...)` constructor `quality_flag` literal), `analysis/feature-table-schema.md` (§"Quality Control" L32, §"Allowed Values" §quality_flag L64–72, §"Example Rows" L87), `analysis/features.md` (§"Required indexing" L27, §"Quality-flag widening" L132/L137).
- **Sub B** touches: `PROJECT.md` (§"Active branch / issue" L32–36), `ROADMAP.md` (R0 §"Next action" L36, R0 §"Owning files" L37).
- **Sub C** touches: `reports/field-report-02-friend-pre-pilot.md` (L1, single H1 line).
- **Sub D** touches: `scripts/features.py` (function def L97, call site L149), `analysis/feature-table-schema.md` (§"Feature Data" L43), `analysis/features.md` (§Shape header L59).

**Two shared files; no shared lines.**

1. **`analysis/feature-table-schema.md`** is touched by Sub A (L32 / L64–72 / L87 — `quality_flag` rows) and Sub D (L43 — `extract_shape` reference). Lines are disjoint; α-serial execution lands Sub A's commit first, Sub D rebases trivially. Under git's three-way merge: no conflict.
2. **`analysis/features.md`** is touched by Sub A (L27 §"Required indexing" / L132 / L137 §"Quality-flag widening") and Sub D (L59 §Shape header). Lines are disjoint; same rebase-trivial pattern.

No `gamma-coordination.md` is required across the wave; the file-line disjointness is sufficient.

## Pinned file paths (forward-reference contract)

All four subs touch existing files only. No new file is created by this wave. No sub forward-references another sub's deliverable path. No pin required.

The `quality_flag` direction chosen by Sub A's α (a-1 vs a-2 vs a-3) lives entirely inside Sub A's surface — Sub D does not reference quality_flag values. The `extract_shape` rename target chosen by Sub D's α (d-1 vs d-2 vs d-3) lives entirely inside Sub D's surface — Sub A does not reference `extract_shape`.

## Standing permissions

- Push to dispatch branch: **yes** — branch is `claude/review-repo-coherence-PNbjQ` (see §"Branching deviation" below)
- Push merges to main: **NO** — operator gate (this wave lands on the review branch first, not main)
- Auto-dispatch α fix rounds on β REQUEST CHANGES: yes (max 3 per sub)
- Tag/release: NO — operator gate
- Branch delete after merge: N/A (no per-cycle branches under §"Branching deviation")
- **Install Python packages: only to satisfy existing pinned versions in `requirements.txt`.** No new dependency. No version drift. This phrasing codifies the ε-recommended clarification from cph#21 §F12 / `coherence-drift-sweep-2026-05-18` cross-sub debt 4 (the precursor wave's Sub D installed `nbformat==5.10.4` to match an existing pin; β read as install-to-match-spec; ε debate on the wording was deferred). For this wave, Sub D's rename does not require notebook regeneration in a code sense (the notebook references `extract_features`, not `extract_shape`), so no `pip install` should be needed; the standing-permission line is here for clarity and future-wave precedent.
- Modify `requirements.txt`: NO
- Run `coh` (TSC CLI) in CI: best-effort — `coh` is not on PATH in this environment per `CHANGELOG.md` `0.1.0-cdr` baseline; the C_Σ baseline gate remains the same as the precursor wave's
- Cross-repo touches (`usurobor/cnos`): NO — out of scope; no cnos-side bundle paths need updating for this wave

## Branching deviation (this wave only)

The cph harness on `claude/review-repo-coherence-PNbjQ` restricts pushes to a single named branch. The standard wave dispatch model uses `cycle/{N}` branches per `cdd/operator/SKILL.md` §5.1 with `git merge --no-ff` into main per sub. This wave deviates as follows — verbatim continuation of the precursor `coherence-drift-sweep-2026-05-18` deviation:

- All four sub-issues land their patches on a single working branch: `claude/review-repo-coherence-PNbjQ`.
- Per-sub artifacts under `.cdd/unreleased/{22,23,24,25}/` follow the standard structure (`self-coherence.md`, `beta-review.md`, `beta-closeout.md`).
- Each sub's "merge" is a commit-marker rather than a merge commit (e.g., a commit titled `β #22: review APPROVE + close-out` after β approves).
- Master closure happens via PR review on `claude/review-repo-coherence-PNbjQ` (operator gate); per the `cdr-refactor-2026-05-18` / `coherence-drift-sweep-2026-05-18` precedent, master close is ε's authority, not δ's.

**Identity-isolation invariant (`α ≠ β within a single sub`)** is preserved by using separate `Agent` subagent invocations for α and β. The precursor wave realized this via "α-session implementing all four subs serially; β-session reviewing all four subs serially" — and the invariant held cleanly across all four subs. This wave inherits that pattern: one Agent invocation for α (all four subs serially); a separate Agent invocation for β (all four subs serially). δ-as-agent orchestrates and writes the wave-closeout but does not perform α or β work within any sub.

If a future cph harness restores `cycle/{N}` push permissions, follow-on waves return to the standard model. This branching deviation is named in the wave-closeout §"Out-of-scope follow-ups" — identical to the precursor wave's posture.

## Timeout budgets

| Role | Sub A (F7) | Sub B (F8+F9) | Sub C (F11) | Sub D (F10) | Rationale |
|------|------------|---------------|-------------|-------------|-----------|
| γ (=δ) | 600s | 600s | 300s | 600s | C is one-line; others are short multi-surface patches |
| α | 900s | 600s | 300s | 600s | Sub A's segmentation patch + 3-surface doc alignment is the heaviest authoring load (still small) |
| β | 600s | 300s | 200s | 400s | Review surface scales with α output; Sub A carries the F7-class anchoring oracle so β gets extra time |

All subs are scoped tightly (docs-only or docs + small code patches). No sub is MCA-eligible — no new spec / no clustering / no new feature is in scope.

## Known constraints

- **Empirical REVISE posture (master cph#21 AC7 + cph#11 §10).** No sub may overclaim the Coherence Path Hypothesis. The latest merged field report (`reports/field-report-01-existing-data-zeroth-pilot.md`, 2026-05-17) governs README / ROADMAP / PROJECT / CHANGELOG empirical-state language. README is not in scope for any sub; Sub B's PROJECT.md / ROADMAP.md edits are bounded to §"Active branch / issue" and R0 §"Next action" / §"Owning files" respectively, and must not touch any empirical-state field.
- **No new features.** cph#22 (Sub A) lifts code labels to match the schema and may add at most one new emitted literal (`"short"` minimum; possibly `"long"`); this is *vocabulary alignment*, not a new feature. cph#25 (Sub D) renames a function but does not change its return value. cph#21 AC8 is the structural backstop.
- **Frozen field reports.** `reports/field-report-01-existing-data-zeroth-pilot.md` content remains frozen. Sub C touches only the H1 of the R5 stub (`field-report-02-friend-pre-pilot.md`), which is *not* a merged field report — it is a template stub that fills in when R5 ships.
- **`coh` not on PATH.** No mechanical TSC measurement is run during or after this wave. The C_Σ baseline lands when `coh` is on PATH in an operator environment, per the cph#11 wave's deferred follow-up.
- **Identity-isolation invariant.** α ≠ β within a single sub (hard rule per `cdd/CDD.md` §1.4). Realized via Agent-session boundaries — each Agent call produces an independent context window and thus an independent identity. γ = δ permitted at this scale per `cdd/operator/SKILL.md` §5.2.

## β anchoring discipline (load-bearing for this wave)

The precursor wave (`coherence-drift-sweep-2026-05-18`) closed with 4 × APPROVE round 1 and zero β findings — and missed F7. The miss was structural, not careless: both α and β anchored their AC1 verification on the *schema doc* (which prescribes the value vocabulary) rather than on `scripts/segmentation.py` (which emits the actual literals). The schema doc had been freshly rewritten by Sub C and was self-consistent; β read the post-patch schema, verified internal consistency, and concluded alignment. The code-side check never happened.

cph#21 §"Review mode" names the structural fix: **"When an AC verification rides on code-doc alignment, β must re-grep the code side independently of α's reported grep results. β-side rule for this wave: for any AC of form 'doc matches code', β reads the code first and verifies the doc matches what the code emits — never the inverse."**

This wave enforces that discipline at the sub-issue AC level (AC5 of Sub A and AC7 of Sub D both name code-first anchoring as a closure condition; β's `beta-review.md` for those subs must record the code-side grep as the *first* oracle output, with the doc-side cross-check as the second). The β-as-agent invocation receives this rule as a hard constraint in its dispatch prompt.

The wave-closeout will record an F7-class observation as a `cdd-protocol-gap` candidate for ε's `cdd-iteration.md`: **β-side oracle anchoring discipline**. Worth a skill patch on `cdd/beta/SKILL.md` if ε agrees, per cph#21 §"Wave-level retrospective hook".

## Resumption / failure handling

- An α or β session that hits the Agent timeout follows `cdd/operator/SKILL.md` §8 timeout-recovery: γ reads the partial artifact, re-dispatches if recoverable, marks the sub `failed` if not.
- A sub closed as **failed** triggers γ to write a master-comment naming the failure.
- A sub closed as **deferred** is named in master cph#21's closure comment as tracked debt; the master does not auto-close until all subs are terminal (master close is ε's authority).
- If β REQUEST CHANGES on any sub, α takes one fix-round (max 3 per sub). The α-session is re-dispatched scoped to that sub only; β re-reviews after α pushes the fix-round.
- **Sub D specific:** if α determines the `extract_shape` rename touches surfaces α cannot inspect without re-grepping (e.g. a notebook-generated cell referencing the function by name), α surfaces the finding in `self-coherence.md` and may take a fix-round to rename in those surfaces. If those surfaces are forbidden by §Non-goals (e.g. the notebook itself; per cph#21 "Re-executing the notebook" is out), α marks Sub D `⭕ deferred` and names the deferral in the wave-closeout — the wave continues without Sub D.

## Out-of-scope follow-ups (named, not in this wave)

- **First mechanical `coh --mode mechanical` run + recording the numeric α/β/γ/C_Σ baseline into `CHANGELOG.md`** — still gated on `coh` being on PATH; same deferred item the cph#11 and cph#16 waves named.
- **Restoration of `cycle/{N}` push permissions** on the cph harness — harness-side, not in this wave's scope.
- **F12 (CHANGELOG entry for the precursor wave)** — policy decision for ε/operator; δ's recommendation is in the wave-closeout §"Cross-sub findings".
- **Cycle.subject → Cycle.participant_code (cph#19 deferred direction-(a))** — out of scope; orthogonal to F7 vocabulary alignment.
- **Real `extract_shape` implementation** — out of scope; this wave only renames the placeholder. Replacing the always-`True` boolean with an informative signal (parquet path? sample count?) is a future cycle.
- **Notebook re-execution** to re-bake analytic outputs — operator-side; gated on data availability.
- **Merge of the two coherence-drift-sweep waves to main** — operator gate; both the precursor and this follow-up land on `claude/review-repo-coherence-PNbjQ` first.
- **Master cph#16 closure** — still ε's authority (the precursor wave's master remains OPEN at the time of this wave's open).
- **Body edit of master cph#21** — left as-filed; sub-issue links live in cph#21 comments + this manifest.
- **`cdd/beta/SKILL.md` patch** for β-anchoring discipline — proposed in cph#21 §"Wave-level retrospective hook"; ε's call after wave-level review.
