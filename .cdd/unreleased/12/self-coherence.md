# Self-Coherence — Sub A — CDR charter docs

<!--
section-manifest:
  planned: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness]
  completed: [Gap, Skills, ACs]
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
