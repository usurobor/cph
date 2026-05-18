# β Close-out — cycle/12 — Sub A — CDR charter docs

<!--
section-manifest:
  planned: [Review Summary, Implementation Assessment, Technical Review, Process Observations, Wave Position]
  completed: [Review Summary, Implementation Assessment, Technical Review, Process Observations, Wave Position]
-->

**Issue:** usurobor/cph#12 — Sub A — CDR charter docs (README + hypothesis + seven-families + CDR.md + source-of-truth init)
**Master:** usurobor/cph#11
**Wave:** `.cdd/waves/cdr-refactor-2026-05-18/`
**Mode:** design-and-build (docs-only)
**Branch (deleted after merge):** `cycle/12`
**Merge commit:** `c3c274a` on `main`
**Base SHA (origin/main at review):** `06341a4`
**Review SHA at APPROVE:** `9b291d3` (cycle/12 head before merge)
**Disconnect type:** part-of-wave; no tag, no version bump, no `.cdd/unreleased/12/` move yet — wave terminal state under δ at Sub D close.

## Review Summary

One round, one verdict, zero findings.

α's self-coherence carried the §CDD-Trace through step 7 with grep-level evidence reproduced for every claimed AC. The four authored docs (README rewrite, `CDR.md`, `docs/concepts/coherence-path-hypothesis.md`, `docs/articles/seven-ways-people-walk.md`) all opened with their governing point, kept stable facts single-homed, and bound their claims. The cross-reference graph from the new docs back into the pre-existing `support-path.md` / `failure-conditions.md` / `analysis/features.md` set resolves cleanly.

β reviewed under `cdd/review/SKILL.md` Phases 1–3, with sub-skills for contract integrity (§2.0.0), issue contract (§2.0), diff/context (§2.1), and architecture (§2.2 — N/A for docs-only). Rule 3.13 honest-claim checks ran clean for reproducibility (a), source-of-truth alignment (b), wiring (c), and gap claims (d). Rule 3.10 (CI green) is vacuous in cph today — no `.github/workflows/` directory. Rule 3.11b (γ artifact completeness) was handled substantively in §3.11b of `beta-review.md`: the wave manifest at `.cdd/waves/cdr-refactor-2026-05-18/manifest.md` carries the substantive γ coordination that rule 3.11b protects against losing. The path-vs-substance gap was named for γ as a non-binding skill-patch observation.

Pre-merge gate (β/SKILL.md §Pre-merge gate):

| Row | Item | Result |
|---|---|---|
| 1 | Identity truth — `beta@cph.cdd.cnos` | ✓ verified at session start and pre-merge |
| 2 | Canonical-skill freshness — `origin/main` unchanged since intake | ✓ `06341a4` at intake, `06341a4` at pre-merge |
| 3 | Non-destructive merge-test — worktree at `/tmp/cph-merge-test`, `merge --no-ff --no-commit origin/cycle/12` | ✓ "Automatic merge went well"; 0 unmerged paths; all 6 expected files present in merge tree; worktree torn down |
| 4 | γ artifact completeness — `.cdd/unreleased/12/gamma-scaffold.md` literal absence; wave manifest substantive coverage | ✓ marked yes-wave-scoped per `beta-review.md` §3.11b reasoning |

The merge-test worktree-local config was set with `extensions.worktreeConfig=true` + `git config --worktree user.{name,email}` so identity did not leak to the shared repo config (per β/SKILL.md row 1 cycle #301 incident). Post-test, `git config --get user.email` still returns `beta@cph.cdd.cnos`.

## Implementation Assessment

α's narrative authoring discipline held across all four files:

- **One governing point per file.** README sentence one names cph + the hypothesis. CDR.md sentence one names the discipline. `coherence-path-hypothesis.md` sentence one names what the doc defines. `seven-ways-people-walk.md` sentence one names the seven families and where they sit under the hypothesis.
- **Stable facts single-homed.** The hypothesis text lives in `coherence-path-hypothesis.md` and is *quoted* (not redefined) in README and CDR.md. The support-path operational definition lives in the preserved `support-path.md` and is only cross-referenced. The seven family names appear in three places (authoritative list in the article, name-only list in the hypothesis doc, single-sentence inline list in README); CDR.md is intentionally absent from this peer set because doctrine should not reproduce vocabulary.
- **Empirical-state language consistent across five touchpoints.** REVISE, r̄ 0.93–0.96, 18.3% / R-only / 0 L-side, bounded fix to `detect_heel_strikes`, hypothesis not yet testable — all sourced to `reports/field-report-01-existing-data-zeroth-pilot.md` and named consistently in README, the hypothesis doc, the seven-families article, and in α's self-coherence's peer enumeration. CDR.md correctly carries no empirical verdict (doctrine, not status).
- **Failure-mode discipline.** CDR.md §C_Σ explicitly names "coherence laundering" (using high C_Σ to support a substantive claim) and "coherence dismissal" (ignoring low C_Σ on the grounds the data still looks fine) — this is the kind of negative-oracle naming that prevents the C_Σ-vs-truth conflation from creeping back in over future cycles.

The four docs read together as one charter: the project's reason-to-exist is named, the research claim is bounded, the operational surface is preserved, the seven-families vocabulary is placed under the hypothesis as candidate surface expressions (not theory), and the source-of-truth table makes the doc boundaries explicit. A new reader can land on README and answer all eight master-#11 reader questions without click-through, with click-through pointers to the authority docs for depth.

## Technical Review

| Verification surface (β prompt) | Status | Evidence |
|---|---|---|
| README answers all eight reader questions from #11 §"Required changes" item 1, in order | met | `grep -n "^## " README.md` returns the headings at lines 7 / 13 / 26 / 37 / 54 / 66 / 77 / 111 in order; cold-read each question answerable from README alone |
| `docs/concepts/coherence-path-hypothesis.md` carries every required heading | met | `grep -F "## "` returns the 11 master-#11-item-2 headings in order |
| `CDR.md` C_Σ section explicitly says high C_Σ does NOT mean the hypothesis is correct | met | line 54: "C_Σ measures project coherence, not the truth of the Coherence Path Hypothesis"; line 56: "A high C_Σ ... does **not** mean the hypothesis is correct" |
| Source-of-truth table forward references (ROADMAP.md, CHANGELOG.md, targets/) are typed correctly | met | README §Source of truth rows 5, 7, 9 use exactly the wave-manifest-pinned paths; line 109 caveat states the forward-reference status |
| No empirical overclaim (preview of Sub D AC8) | met | scan returned zero hits across all four authored files |
| No committed raw data (preview of Sub D AC9) | met | `git ls-files \| grep -iE '\.(csv\|trc\|mot\|sto\|c3d\|osim\|mp4\|mov\|mkv\|webm\|png\|jpg\|jpeg\|pkl\|npz\|h5\|hdf5\|parquet\|feather)$'` returns zero hits across the tree |

`beta-review.md` §2.0 AC ledger carries the AC1 / AC2 / AC4 / AC10-initial verdicts with the same grep evidence.

## Process Observations

These are for γ's wave-level assessment and for the next γ-skill patch. Naming them here so they don't get lost between Sub A close and Sub D close.

1. **Wave-mode γ scaffold pattern (first observation).** This is cph's first wave-mode dispatch and my first wave-mode review. The wave manifest at `.cdd/waves/cdr-refactor-2026-05-18/manifest.md` substantively carries the γ coordination that rule 3.11b protects, but lives at a wave-scoped path rather than the rule's literal sub-scoped path. β read this substantively (see `beta-review.md` §3.11b) and did not fire a finding. The next γ-skill patch should canonicalize either (a) a per-cycle `gamma-scaffold.md` stub that points at the wave manifest, or (b) explicit recognition of `.cdd/waves/{slug}/manifest.md` as a valid γ artifact under wave-mode dispatch. This is rule-patch territory per rule 3.12 (review divergence is a skill gap), not a finding against this cycle.
2. **Incremental commits worked cleanly.** α wrote 7 self-coherence sections in 7 commits (`f39715d` → `873692f`); β wrote `beta-review.md` in 3 commits (`4b9d5b5` → `2bf52ac` → `9b291d3`). No stream-timeout losses, no resumption needed. The α §2.5 / `review/SKILL.md` §Output Format incremental-write pattern is doing what it was designed to do.
3. **CI absence is structural, not a gap.** cph has no `.github/workflows/`. Rule 3.10 falls back to "every workflow that runs on cycle branch" — none run, the gate is vacuous. Whether cph should grow CI is a separate question (likely yes — Sub C's `scripts/measure-coherence.sh` is a natural CI candidate); β did not raise it here because (a) it's wave-out-of-scope, (b) rule 3.10's vacuous-fallback path is intentional, (c) cph is a docs-and-research repo where CI value is different from code repos.
4. **Pre-existing tech debt named, not fixed.** PROJECT.md cites `docs/realizations/04-existing-data-comes-first.md` and `docs/realizations/06-what-broke.md`; the actual filesystem carries `04-friends-are-a-pre-pilot.md` and `05-what-broke.md`. Not Sub A's scope; Sub C repartitions PROJECT.md. Named in `beta-review.md` §Notes so Sub C's reviewer doesn't miss it.
5. **Dual source-of-truth tables transient.** README now carries the 9-row CDR-era source-of-truth table; PROJECT.md still carries its pre-CDR 10-row table. The two are not in conflict (disjoint question sets) but the transient is worth flagging — Sub C will resolve when it shrinks PROJECT.md to operational-status-only.
6. **β did not invoke release/SKILL.md §2.5a or §2.5b.** This is a sub of a wave, not a disconnect on its own. `.cdd/unreleased/12/` stays at `.cdd/unreleased/12/` after this merge — δ will run the wave-level disconnect after Sub D closes per `release/SKILL.md` §2.5b (docs-only wave). β explicitly does not move directories on individual sub merges within a wave.

## Wave Position

Sub A is the first of four subs to close in wave `cdr-refactor-2026-05-18`. Status table:

| Sub | Issue | Branch | Status after this β close-out |
|---|---|---|---|
| Sub A | #12 | `cycle/12` (deleted after merge) | **merged**, this artifact |
| Sub B | #13 | `cycle/13` | in flight (parallel) |
| Sub C | #14 | `cycle/14` | in flight (parallel) |
| Sub D | #15 | not yet created | blocked on A + B + C terminal state |

Forward-reference rows in the source-of-truth table this sub shipped — `ROADMAP.md` (Sub B), `CHANGELOG.md` / `targets/` (Sub C) — resolve when Subs B and C merge. Sub D's AC10 final sweep verifies the table end-to-end after all three merge. The path commitments this sub made are pinned in the wave manifest and are stable across the parallel work.

γ-as-δ next steps: γ writes the wave-level Post-Release Assessment after all four subs close (per `release/SKILL.md` §2.5b docs-only flow, PRA at `docs/gamma/cdd/docs/{ISO-date}/POST-RELEASE-ASSESSMENT.md`). α writes `.cdd/unreleased/12/alpha-closeout.md` for Sub A specifically.

β's work on Sub A ends here.
