# Self-Coherence — Sub B — CDR roadmap

<!--
section-manifest:
  planned: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness]
  completed: [Gap, Skills]
-->

## Gap

**Issue:** usurobor/cph#13 — Sub B — CDR roadmap (ROADMAP.md, phases R0–R6)
**Master:** usurobor/cph#11
**Wave:** `.cdd/waves/cdr-refactor-2026-05-18/`
**Mode:** design-and-build
**Version:** Sub-issue under master #11; this cycle delivers AC3 of the master (ROADMAP.md). Sub A is merged on `main` (charter docs). Sub C (TSC infra + CHANGELOG + PROJECT.md repartition) and Sub D (sweep) remain in flight; ROADMAP.md forward-references their pending deliverables without depending on their merge.

The cph repo has no gate-based view of the research path. `PROJECT.md` doubles as roadmap and status ledger; gates are implicit; no surface tracks coherence risk per phase. Sub B authors a single file — `ROADMAP.md` — that names phases R0–R6, each carrying Goal / Current evidence / Gate / Status / Coherence risk / Next action / Owning files, with phase status fields grounded in the latest merged field report.

Sub B does **not** change empirical state. The latest merged field report (`reports/field-report-01-existing-data-zeroth-pilot.md`, 2026-05-17) governs the empirical-state language in ROADMAP.md; the posture remains REVISE on R1 and R2. R5 is "Blocked until earlier gates pass" (mandated by master + dispatch constraint); R6 is "Not started." (same).

## Skills

**Tier 1** (lifecycle / role):
- `cdd/CDD.md` — canonical lifecycle and role contract
- `cnos.cdd/skills/cdd/alpha/SKILL.md` — α role surface (load order, artifact order, pre-review gate)
- `cnos.cdd/skills/cdd/issue/SKILL.md` — AC interpretation (loaded implicitly to read ACs)

**Tier 2** (always-applicable engineering bundles): none loaded — Sub B is docs-only authoring of a single Markdown file. No code, no schema, no tests, no CLI surface. No `eng/*` bundle from `cnos.eng/skills/eng/` applies as a generation constraint.

**Tier 3** (issue-specific):
- `cnos.core/skills/write/SKILL.md` — prose authoring discipline; one governing question per file, lead with the point, say a stable fact once
- *cph-local `eng/markdown`* — not present in the cph repo; the dispatch prompt names it conditionally ("plus any cph-local eng/markdown skill if present"). The cnos-side eng tree under `/tmp/cnos/src/packages/cnos.eng/skills/eng/` does not carry a `markdown` skill either, so no markdown-specific skill is loaded. This matches Sub A's loaded-skill set.

The `write` skill is the only generation-constraint skill that fired during authoring. It is reflected in surface choices: ROADMAP.md opens with the governing question (the gates by which the hypothesis is validated, revised, or abandoned); the first paragraph commits to the file's job; each phase opens with `**Goal:**` first, then current evidence, then gate, then status. Stable facts each have one home — empirical state is cited from `reports/field-report-01-existing-data-zeroth-pilot.md`, hypothesis language is cited from `docs/concepts/coherence-path-hypothesis.md` and `docs/concepts/support-path.md`, doctrine is cited from `CDR.md`. ROADMAP does not restate stable facts; it links to their owning files.
