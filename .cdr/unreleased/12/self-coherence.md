# Self-Coherence — Sub A — CDR charter docs

<!--
section-manifest:
  planned: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness]
  completed: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness]
-->

## Gap

**Issue:** usurobor/cph#12 — Sub A — CDR charter docs (README + hypothesis + seven-families + CDR.md + source-of-truth init)
**Master:** usurobor/cph#11
**Wave:** `.cdd/waves/cdr-refactor-2026-05-18/`
**Mode:** design-and-build
**Version:** Sub-issue under master #11; this cycle delivers the charter-layer docs (ACs 1, 2, 4, and the initial form of AC10) and does not touch ROADMAP / TSC infra / CHANGELOG (Sub B/C scope).

The cph repo carries methods discipline but no public charter that names the Coherence Path Hypothesis as the project's governing question. Sub A creates that charter: a README rewritten around the hypothesis, a dedicated hypothesis-authority doc, a CDR doctrine doc, an observational-vocabulary bridge for the seven gait families, and the source-of-truth table that disambiguates which doc owns which question.

Sub A does **not** change empirical state. The latest merged field report (`reports/field-report-01-existing-data-zeroth-pilot.md`, 2026-05-17) governs the empirical-state language across every new file; the posture remains REVISE.

## Skills

**Tier 1** (lifecycle / role):
- `cdd/CDD.md` — canonical lifecycle and role contract
- `cnos.cdd/skills/cdd/alpha/SKILL.md` — α role surface
- `cnos.cdd/skills/cdd/issue/SKILL.md` — AC interpretation (loaded implicitly to read ACs)

**Tier 2** (always-applicable engineering bundles): none loaded — Sub A is docs-only authoring with no code, no schema, no tests, no CLI surface. No `eng/*` bundle from `cnos.eng/skills/eng/` applies as a generation constraint here.

**Tier 3** (issue-specific):
- `cnos.core/skills/write/SKILL.md` — prose authoring discipline; one governing question per file, lead with the point, say a stable fact once
- *cph-local `eng/markdown`* — not present in the cph repo; the wave manifest names this as conditional ("plus any cph-local eng/markdown skill if present"). The cnos-side eng tree under `/tmp/cnos/src/packages/cnos.eng/skills/eng/` does not carry a `markdown` skill either, so no markdown-specific skill is loaded.

The `write` skill is the only generation-constraint skill that fired during authoring. It is reflected in the surface choices: each new file opens with the point (README sentence one names cph + the hypothesis; CDR.md sentence one names the discipline; coherence-path-hypothesis.md sentence one names what the doc defines; seven-ways-people-walk.md sentence one names the seven families and where they sit under the hypothesis). Stable facts each have one home (hypothesis text in `coherence-path-hypothesis.md`; support-path operational definition preserved in `support-path.md` and only cross-referenced from the hypothesis doc; seven family names in the article and only listed by name in README + hypothesis doc).

## ACs

### AC1 — README identity is clear

**Invariant:** README answers all eight reader questions from master #11 §"Required changes" item 1, in order.
**Status:** met.

Evidence — `grep -n "^## " README.md` returns the headings in the expected order:

| # | Question (AC1) | README heading | Line |
|---|----------------|----------------|------|
| 1 | What is this project? | `## What is this project?` | 7 |
| 2 | What is the hypothesis? | `## What is the hypothesis?` | 13 |
| 3 | Why is this worth testing? | `## Why is this worth testing?` | 26 |
| 4 | What is not being claimed? | `## What is not being claimed` | 37 |
| 5 | How does this connect to the seven gait families? | `## How does this connect to the seven gait families?` | 54 |
| 6 | Current empirical state | `## Current empirical state` | 66 |
| 7 | How CDR works in this repo | `## How CDR works in this repo` | 77 |
| 8 | Where to go next | `## Where to go next` | 111 |

Source-of-truth table sits between §How CDR works (Q7) and §Where to go next (Q8) at line 93 — it is part of the README's job per AC10 but is not one of the eight reader questions.

**Negative-claim check** (AC1 negative oracle):
- README does **not** state the hypothesis is validated. §Current empirical state names REVISE and lists the segmentation blocker that prevents the hypothesis from being testable yet.
- README does **not** state any of the seven families is proven. §How does this connect... explicitly says "If measurement supports three families, twelve, or none, the hypothesis can still survive."
- README does **not** recommend "your gait type." §What is not being claimed lists `not "you are this gait type"` and §Safety boundary forbids "this is who you are."

### AC2 — Hypothesis authority exists

**Invariant:** `docs/concepts/coherence-path-hypothesis.md` carries each required heading from master #11 item 2.
**Status:** met.

Evidence — `grep -F "## " docs/concepts/coherence-path-hypothesis.md`:

```
## Governing question
## Definition
## What counts as evidence
## What does not count as evidence
## Relationship to support path
## Relationship to the seven gait families
## Operationalization
## Current empirical status
## Falsification conditions
## Practical consequences if supported
## What would still remain unproven
```

All 11 required headings present in the order listed in master #11 item 2.

**Measured-vs-inferred distinction** (AC2 positive oracle): the doc distinguishes measured quantities (kinematics, timing, segment coupling, asymmetry, condition response, reference comparisons) from inferred constructs (path organization, load-transfer interpretation, gait-family meaning). The split appears in §What counts as evidence and is reinforced by the cross-reference into `support-path.md` §Measured vs Inferred.

**Negative oracle:** the doc does not assert a coherence path is directly visible / measured. §Definition opens "A coherence path is an *inferred* coordination pattern" and §What counts as evidence opens "Evidence for the hypothesis is built from measured quantities and reaches the hypothesis only through interpretation."

### AC4 — CDR doctrine exists

**Invariant:** `CDR.md` carries each required heading from master #11 item 5.
**Status:** met.

Evidence — `grep -F "## " CDR.md`:

```
## What CDR is
## What CDR is not
## Research TSC axes
### α — Hypothesis pattern coherence
### β — Evidence relation coherence
### γ — Process coherence
## C_Σ in this repo
## Required cadence
## Changelog rule
```

All required headings present.

**C_Σ-vs-truth distinction** (AC4 positive oracle): §C_Σ in this repo opens "C_Σ measures project coherence, not the truth of the Coherence Path Hypothesis" and names two failure modes — *coherence laundering* (using a high C_Σ to support a substantive claim) and *coherence dismissal* (ignoring a low C_Σ on the grounds the data still looks fine). The negative-oracle conflation between project coherence and hypothesis truth is named and forbidden in-doc.

### AC10 initial — Source-of-truth boundaries are explicit

**Invariant:** The source-of-truth table maps nine canonical questions to owning files.
**Status:** met for Sub A's initial form.

Evidence — `README.md` §Source of truth carries the table; row paths:

| Question | Owning file | Resolves on this branch? |
|----------|-------------|--------------------------|
| What is this project? | `README.md` | ✓ (rewritten this sub) |
| What is CDR? | `CDR.md` | ✓ (new this sub) |
| What is the hypothesis? | `docs/concepts/coherence-path-hypothesis.md` | ✓ (new this sub) |
| What is a support path? | `docs/concepts/support-path.md` | ✓ (preserved) |
| Where are research gates tracked? | `ROADMAP.md` | forward — Sub B |
| What is current operational status? | `PROJECT.md` | ✓ (preserved; Sub C will repartition) |
| What changed over time? | `CHANGELOG.md` | forward — Sub C |
| What empirical evidence exists? | `reports/` | ✓ (preserved) |
| What TSC targets are measured? | `targets/` | forward — Sub C |

Per the wave manifest (`.cdd/waves/cdr-refactor-2026-05-18/manifest.md` §Pinned file paths), `ROADMAP.md`, `CHANGELOG.md`, and `targets/` are forward references the wave fulfills end-to-end; Sub A's responsibility is the *initial* version. README §Source of truth states this explicitly so that a reader landing on the cycle/12 branch in isolation is not confused by the not-yet-present rows.

**Sub-A path match check:** every Sub-A-created file's path matches the table row that names it.

- `README.md` — table row 1 → matches.
- `CDR.md` — table row 2 → matches.
- `docs/concepts/coherence-path-hypothesis.md` — table row 3 → matches.
- `docs/articles/seven-ways-people-walk.md` — not a table row (the seven-families article is *cited from* the hypothesis-doc row and the README §How does this connect... section, not promoted into the canonical-question table; the doc owns observational vocabulary, not one of the nine canonical questions). This follows the wave manifest, which pins `docs/articles/seven-ways-people-walk.md` as the seven-families file but does not require it to appear as a source-of-truth row.

**Negative oracle:** README does not contain the project status (PROJECT.md's row) and does not contain the hypothesis definition (coherence-path-hypothesis.md's row). README §Current empirical state names REVISE and the latest field report path, but does not duplicate PROJECT.md's current-stage / current-action narrative; it ends with "[PROJECT.md] carries the live operational status." README §What is the hypothesis? quotes the hypothesis in one sentence and immediately points to the authority doc for the full definition.

## Self-check

**Did α's work push ambiguity onto β?** No specific load. The wave's pinned paths are honoured (the preferred `docs/articles/seven-ways-people-walk.md` path was chosen, so no manifest update or Sub C coordination note was needed). The README source-of-truth table includes forward-reference rows for Sub B/C files, and the table's own caveat sentence ("`ROADMAP.md`, `CHANGELOG.md`, and `targets/` are delivered by sibling sub-issues in the same wave...") makes the forward-reference status legible without requiring β to reconstruct the wave structure. The single judgement call β may want to re-examine is the *placement* of the source-of-truth table inside README (between Q7 and Q8) rather than in a separate file linked from README — this is permitted by AC10 ("the table itself lives in README; this sub creates the initial version") and explicitly allowed by the AC10 surface ("`README.md` (and any doc it forwards the table to)").

**Is every claim backed by evidence in the diff?**

- AC1 evidence is the `grep -n "^## "` output reproduced above; each of the eight reader questions maps to a heading at a numbered line.
- AC2 / AC4 evidence is the `grep -F "## "` output reproduced above; each required heading appears in-file.
- AC10 evidence is the rendered table (9 rows, each with a path) plus the file-existence check (3 of the 4 Sub-A-created files match their row's path; `docs/articles/seven-ways-people-walk.md` does not occupy a table row by design and the rationale is named in §ACs above).
- The empirical-state REVISE language across README, CDR.md, and `coherence-path-hypothesis.md` matches `reports/field-report-01-existing-data-zeroth-pilot.md` §Status — the OpenCap-vs-reference PASS finding (r̄ 0.93–0.96), the 18.3% R-only segmentation failure, the bounded revision scope, and the REVISE verdict are all sourced to that report and named consistently in each document.

**Peer enumeration — empirical-state surfaces.** The new files that carry empirical-state language are:

- `README.md` §Current empirical state → REVISE, r̄ 0.93–0.96 PASS, 18.3% / R-only / no L-side, bounded fix.
- `CDR.md` — does not carry an empirical-state claim (CDR.md is doctrine); §Required cadence names "empirical gate transitions" abstractly without committing a verdict.
- `docs/concepts/coherence-path-hypothesis.md` §Current empirical status → REVISE, same four facts as README, same field-report citation.
- `docs/articles/seven-ways-people-walk.md` — does not carry detailed empirical claims; §What the list is not states "None of the seven has been tested against gait-cycle data as of the current empirical posture (REVISE — see [reports/field-report-01-existing-data-zeroth-pilot.md])" and points to the report.

All four touchpoints either name REVISE explicitly or refrain from claiming a verdict, and all four point to the same field-report file as the canonical source. The peer set is consistent.

**Peer enumeration — seven-family naming.** The seven family names appear in three places:

- `docs/articles/seven-ways-people-walk.md` §The seven names — authoritative list (one paragraph per family).
- `docs/concepts/coherence-path-hypothesis.md` §Relationship to the seven gait families — bullet list of names only, with cross-reference into the article.
- `README.md` §How does this connect to the seven gait families? — single-sentence inline list of names, with cross-reference into the article.

`grep -F "Pendular Carrier" README.md CDR.md docs/concepts/coherence-path-hypothesis.md docs/articles/seven-ways-people-walk.md` returns the names in exactly the three expected files. CDR.md is intentionally absent — doctrine should not reproduce vocabulary.

**Authority surface check.** Before authoring, the existing `docs/concepts/support-path.md` was identified as the canonical owner of the operational `support path` term (per master #11 §Terms and the wave manifest constraint "Existing docs/concepts/support-path.md is preserved"). The new `coherence-path-hypothesis.md` §Relationship to support path explicitly names support-path.md as the authority and does not redefine the term:

> `support path` is the repo's operational term for the measurable surface of this hypothesis. [docs/concepts/support-path.md](support-path.md) owns the operational definition; this document does not redefine it.

No re-statement of support-path's operational definition appears in any new file; only cross-references.

## Debt

Sub A leaves the following debt explicit. None of it is in-scope for this sub.

**Forward-reference rows in the source-of-truth table.** Three rows — `ROADMAP.md` (Sub B), `CHANGELOG.md` and `targets/` (Sub C) — point to files that do not exist on the cycle/12 branch in isolation. The wave manifest licenses this ("the table is a forward declaration the wave fulfills end-to-end"; AC10 oracle for Sub A allows it explicitly), and README §Source of truth states the situation in-doc, but **Sub D's AC10 final sweep must verify each forward-reference row resolves after Sub B and Sub C merge**. If either Sub B or Sub C is deferred rather than merged, Sub D will need to either rewrite the table to drop the unresolved row or note the deferral in-doc per the wave's scope-adjustment rule.

**PROJECT.md not repartitioned.** PROJECT.md currently carries both operational status and an embedded source-of-truth table (its own, scoped to the pre-CDR file set). Sub C is the issue that will shrink PROJECT.md to operational-status-only and remove its embedded source-of-truth table; until that happens, the README and PROJECT.md will each carry a source-of-truth table. They are not in conflict (README's lists nine canonical questions across the CDR-era doc set; PROJECT.md's lists the pre-CDR file set scoped to friend-pre-pilot work) but they will need reconciliation in Sub C. This is named in the wave manifest's pinned-paths table and is **not Sub A's job**.

**Empirical-state language re-sync if the field report is republished.** The REVISE posture and the four facts cited from `field-report-01-existing-data-zeroth-pilot.md` (PASS at r̄ 0.93–0.96, 18.3% / R-only, bounded fix to `detect_heel_strikes`, hypothesis not yet testable) are duplicated across README.md and `coherence-path-hypothesis.md` by necessity — both files need to state empirical state to do their jobs. If the field report is amended or superseded by a later merged report, both touchpoints (and CDR.md §Required cadence, which lists the trigger conditions but not the verdict) will need updating together. The CDR β-axis (evidence relation coherence) is designed to catch this drift; Sub C's TSC measurement will be the first surface to surface it mechanically.

**No `eng/markdown` skill loaded.** The wave manifest names this as conditional ("plus any cph-local eng/markdown skill if present"). Neither cph nor cnos carries a markdown skill at the loaded tier. Heading conventions, link discipline, and table syntax were enforced from the `write` skill's rules and from existing-doc patterns (mirroring `support-path.md`'s heading style). If a future cycle authors `eng/markdown`, the four files this sub created are candidates for retroactive linting; this is not blocking and the diff is small.

**Closure-overclaim self-check fired clean.** AC1, AC2, AC4, and AC10-initial all map to grep-level evidence reproduced above. The closure claims are bounded: AC10 is *initial*, not final (the wave manifest assigns the *final* sweep to Sub D). No "all empirical surfaces are now consistent" claim is made — that is Sub D's job.

## CDD-Trace

CDD canonical artifact order per `cdd/CDD.md` §5.2, traced through step 7.

### 1. Design

Not required for Sub A. The design is carried by master #11 and the Sub-A issue body (cph#12): the eight reader questions for README, the 11 required headings for the hypothesis doc, the required sections for CDR.md, the seven-families article framing, and the nine-row source-of-truth table are all pre-specified in the issues. The wave manifest also pins the file paths in advance to make A/B/C parallelism work.

Mode is `design-and-build`, but the *design* phase ran at sub-issue authoring time, not during this α dispatch. α's job was to render the pre-specified shape into prose.

### 2. Coherence contract

§Gap above. Issue scope, mode, and the empirical-state constraint (REVISE per the latest merged field report) are stated.

### 3. Plan

Not required for Sub A. Implementation sequencing is dependency-driven and trivial:

1. hypothesis doc (no dependencies; later docs cite it)
2. seven-families article (cites the hypothesis doc)
3. CDR.md (cites the hypothesis doc; defines C_Σ ≠ truth)
4. README rewrite (cites all of the above; carries the source-of-truth table)
5. self-coherence (this file, incremental per α §2.5)

Each step depended only on its predecessors. No branch-points, no contention, no parallel work that needed scheduling.

### 4. Tests

Not applicable. Sub A is docs-only authoring; there is no executable surface, no schema, no parser, no CLI. The AC oracles per master #11 / sub-issue body are grep-based heading checks; those are reproduced in §ACs above as evidence rather than packaged as tests. (If the wave wanted these as CI checks, that would be Sub C / Sub D scope — `targets/hypothesis.tsc` will reference these files mechanically.)

### 5. Code

Not applicable. No code touched.

### 6. Docs

Four files authored or rewritten:

| File | Action | AC | Implementation SHA |
|------|--------|----|--------------------|
| `docs/concepts/coherence-path-hypothesis.md` | new (144 lines) | AC2 | 753092d |
| `docs/articles/seven-ways-people-walk.md` | new (59 lines) | AC1 (Q5 support), AC10 (article cited but not a table row) | 036bcd0 |
| `CDR.md` | new (89 lines) | AC4 | 5193877 |
| `README.md` | rewrite (+88 / −60 lines) | AC1, AC10 (table) | 32defc5 |

Plus the artifact tracking the cycle:

| File | Action | Purpose |
|------|--------|---------|
| `.cdd/unreleased/12/self-coherence.md` | new (incremental, this file) | α tracking artifact per `cdd/alpha/SKILL.md` §2.5 |

`git diff --stat origin/main..HEAD` returns exactly these five files — every file in the diff is enumerated above (pre-review gate row 11 satisfied):

```
 .cdd/unreleased/12/self-coherence.md       | 189 +++++++++++++++++++++++++++++
 CDR.md                                     |  89 ++++++++++++++
 README.md                                  | 148 +++++++++++++---------
 docs/articles/seven-ways-people-walk.md    |  59 +++++++++
 docs/concepts/coherence-path-hypothesis.md | 144 ++++++++++++++++++++++
 5 files changed, 569 insertions(+), 60 deletions(-)
```

(The 189-line count for `self-coherence.md` predates this CDD-Trace section's append; the file will be larger by the time β reads it. This is expected per α §2.5 incremental authoring — the self-coherence file is the only artifact that grows across self-coherence commits.)

**Caller-path trace for new modules (pre-review gate row 12).** Not applicable — no new modules or functions. The new docs are referenced from existing surfaces:

- `coherence-path-hypothesis.md` — linked from `README.md` §What is the hypothesis? + §Where to go next; linked from `CDR.md` opening; linked from `docs/articles/seven-ways-people-walk.md` §Why this list exists.
- `docs/articles/seven-ways-people-walk.md` — linked from `README.md` §How does this connect to the seven gait families? + §Where to go next; linked from `coherence-path-hypothesis.md` §Relationship to the seven gait families.
- `CDR.md` — linked from `README.md` §How CDR works + §Where to go next; linked from `coherence-path-hypothesis.md` §What does not count as evidence (the C_Σ ≠ evidence sentence).

Every new doc has at least one non-self caller; no orphaned-doc state.

### 7. Self-coherence

This file (`.cdd/unreleased/12/self-coherence.md`), committed incrementally per α §2.5: one section per commit, pushed to `origin/cycle/12` so that a stream timeout cannot lose partial work.

Section commit chain on this branch:
- `f39715d` — §Gap
- `d02f00e` — §Skills
- `d452516` — §ACs
- `7562d01` — §Self-check
- `c985141` — §Debt
- (this commit) — §CDD-Trace

§Review-readiness will be appended as a separate commit after §2.6 pre-review-gate checks pass (§2.7).

## Review-readiness

**Round:** 1
**Base SHA (origin/main at observation):** `06341a45429a834cd7c4e6e8338e9cc75202caab`
**Implementation SHA:** `f20949e` (last α implementation commit before the readiness-signal commit; per `cdd/alpha/SKILL.md` §2.6 SHA convention)
**Branch CI:** **not configured.** This repo carries no `.github/workflows/` directory; `gh run list --branch cycle/12 --limit 5` returns no rows. Per α §2.6 row 10, this is the "local CI unavailable" path — β should not wait for green CI because none can run, and the explicit absence is recorded here so that β can confirm the situation and proceed.
**Observation time (UTC):** `2026-05-18T13:44:42Z`
**Verdict:** ready for β.

### Pre-review-gate checklist (α §2.6)

| Row | Item | Status | Evidence |
|-----|------|--------|----------|
| 1 | `origin/cycle/12` rebased onto current `origin/main` | ✓ | `git merge-base origin/cycle/12 origin/main` = `06341a4` = current `origin/main` HEAD at observation time |
| 2 | self-coherence.md carries CDD Trace through step 7 | ✓ | §CDD-Trace above; steps 1–7 each named |
| 3 | tests present, or explicit reason none apply | ✓ (none) | §CDD-Trace step 4 — docs-only authoring; no executable surface |
| 4 | every AC has evidence | ✓ | §ACs — AC1 / AC2 / AC4 / AC10-initial each map to grep-level evidence |
| 5 | known debt explicit | ✓ | §Debt — four debt items named |
| 6 | schema / shape audit completed when contracts changed | ✓ (N/A) | no contracts changed |
| 7 | peer enumeration completed when closure claim touches a family of surfaces | ✓ | §Self-check — empirical-state surfaces (4 touchpoints) and seven-family naming (3 expected files; CDR.md correctly absent) |
| 8 | harness audit completed when schema-bearing contract changed | ✓ (N/A) | no schema-bearing contract changed |
| 9 | post-patch re-audit completed after any mid-cycle patch | ✓ (N/A) | no patches in this round |
| 10 | branch CI green on the head commit | ✓ (explicit absence) | no CI configured in repo; reasoning above |
| 11 | artifact enumeration matches diff | ✓ | §CDD-Trace step 6 lists exactly the 5 files in `git diff --stat origin/main..HEAD` |
| 12 | caller-path trace for new modules | ✓ (N/A) | no new modules; doc-callers traced in §CDD-Trace step 6 |
| 13 | test assertion count from runner output | ✓ (N/A) | no tests |
| 14 | α's commit author email matches canonical pattern | ✓ | all 10 α commits on this branch use `alpha@cph.cdd.cnos`; verified by `git log origin/main..HEAD --pretty=format:'%h %ae %s'` |

### Polyglot re-audit (row 9, supplementary)

Diff languages: Markdown only (5 files). Re-audit checks:

- heading shape: `grep "^## " <file>` returns the expected heading set for each AC2 / AC4 file (reproduced in §ACs above); README question-order verified line-by-line in §ACs.
- cross-reference check: every internal link in the four new docs resolves to a file on this branch *or* to a wave-pinned forward-reference path (`ROADMAP.md`, `CHANGELOG.md`, `targets/`, `scripts/measure-coherence.sh`); the README §Source of truth caveat sentence makes the forward-reference situation legible in-doc.
- table-shape check: source-of-truth table is 9 rows × 2 columns, well-formed; the AC1 evidence table in §ACs and the AC10 table in §ACs are well-formed.
- empirical-state grep — `grep -n "REVISE\|r̄\|18.3%\|2026-05-17" README.md CDR.md docs/concepts/coherence-path-hypothesis.md docs/articles/seven-ways-people-walk.md` returns only references that match `reports/field-report-01-existing-data-zeroth-pilot.md` §Status: 2026-05-17 real-data run, REVISE, r̄ 0.93–0.96 PASS, 18.3% / R-only segmentation. No claim outruns the field report. CDR.md does not carry a numeric or verdict claim and is correctly silent.

### β reviewer entry point

β should read in this order:

1. `.cdd/unreleased/12/self-coherence.md` (this file) — §Gap → §ACs → §Self-check → §Debt.
2. `README.md` — verify the eight reader questions are answerable from the README cold.
3. `docs/concepts/coherence-path-hypothesis.md` — verify the 11 required headings and the measured-vs-inferred distinction.
4. `CDR.md` — verify the required headings and the C_Σ ≠ truth distinction.
5. `docs/articles/seven-ways-people-walk.md` — verify the bridge framing (observational vocabulary, not core theory) and the seven names.
6. Spot-check empirical-state language against `reports/field-report-01-existing-data-zeroth-pilot.md` §Status.

β should write findings (or APPROVE) into `.cdd/unreleased/12/beta-review.md`. α is now polling `origin/cycle/12` and `.cdd/unreleased/12/beta-review.md` per α §2.7.
