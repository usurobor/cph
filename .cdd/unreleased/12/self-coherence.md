# Self-Coherence — Sub A — CDR charter docs

<!--
section-manifest:
  planned: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness]
  completed: [Gap, Skills]
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
