# Self-Coherence — Sub B — CDR roadmap

<!--
section-manifest:
  planned: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness]
  completed: [Gap, Skills, ACs]
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

## ACs

Sub B carries one AC of master #11 (AC3). The oracle structure is the master-issue AC3 spec.

### AC3 — Roadmap exists and is gate-based

**Invariant:** Every phase contains Goal / Current evidence / Gate / Status / Coherence risk / Next action / Owning files.
**Status:** met.

**Structural oracle 1** — phase enumeration:

```text
$ grep -cE '^## Phase R[0-6]' ROADMAP.md
7
$ grep -nE '^## Phase R[0-6]' ROADMAP.md
29:## Phase R0 — Charter and operationalization
39:## Phase R1 — Existing-data zeroth pilot
49:## Phase R2 — Contact-event and segmentation reliability
59:## Phase R3 — First construct-level evidence
69:## Phase R4 — Support/coherence-path inference
79:## Phase R5 — New capture / friend pre-pilot
89:## Phase R6 — AI classification
```

**Structural oracle 2** — per-field completeness (one count per field across all 7 phases):

```text
$ for f in Goal 'Current evidence' Gate Status 'Coherence risk' 'Next action' 'Owning files'; \
    do printf '%-18s %s\n' "$f" "$(grep -c "\*\*${f}:\*\*" ROADMAP.md)"; done
Goal               7
Current evidence   7
Gate               7
Status             7
Coherence risk     7
Next action        7
Owning files       7
```

Each field present once per phase, exactly. 7 fields × 7 phases = 49 field instances, all accounted for.

**Positive oracle 1** — R0 owner files cite the charter-doc set:

R0 §Owning files names `README.md`, `CDR.md`, `docs/concepts/coherence-path-hypothesis.md`, `docs/concepts/support-path.md`, `docs/concepts/failure-conditions.md`, `docs/articles/seven-ways-people-walk.md`, `ROADMAP.md` (this), `PROJECT.md`, and the Sub C deliverables (`CHANGELOG.md`, `targets/*.tsc`, `scripts/measure-coherence.sh`). All five charter-doc paths from the master AC3 positive oracle are present.

**Positive oracle 2** — R5 / R6 status phrasings:

```text
$ grep -nE 'Status:\*\*' ROADMAP.md
34:- **Status:** ACTIVE.
44:- **Status:** REVISE.
54:- **Status:** REVISE.
64:- **Status:** NOT STARTED.
74:- **Status:** NOT STARTED.
84:- **Status:** Blocked until earlier gates pass.
94:- **Status:** Not started.
```

R5 = "Blocked until earlier gates pass." (line 84). R6 = "Not started." (line 94). Both match the master-mandated phrasings exactly and the binding dispatch constraint.

**Negative oracle 1** — no phase claims GO without citing evidence:

No phase carries Status: GO. R0 is ACTIVE; R1 and R2 are REVISE; R3 and R4 are NOT STARTED; R5 and R6 carry their mandated phrasings. No phase asserts the gate is met. The empirical-state language traces to `reports/field-report-01-existing-data-zeroth-pilot.md` for R1 (REVISE), R2 (segmenter blocker), R3 (n=11 R-side, hypothesis 1 partially evaluable, 2/3 blocked), and R4 (falsification table: 0/6 cleanly triggered, 4 not testable).

**Negative oracle 2** — AI clustering is gated future, not current activity:

R6 §Goal frames AI classification as conditional on stable feature surfaces from R3/R4. R6 §Current evidence states "No clustering has been run. `analysis/clustering-plan.md` exists as a plan-only document." R6 §Status is "Not started." R6 §Next action is "Hold. Do not run clustering against existing or future data until R4 closes GO." No phase elsewhere in ROADMAP references clustering as in-progress or imminent.

**Constraint check — binding dispatch constraints:**

| Constraint | Surface | Verification |
|---|---|---|
| Phase status fields match latest merged field report | R1, R2, R3, R4 statuses | R1=REVISE / R2=REVISE / R3=NOT STARTED / R4=NOT STARTED match `field-report-01-existing-data-zeroth-pilot.md` decision + §Falsification Assessment + §Support-Path Inference |
| R5 status is "Blocked until earlier gates pass" | R5 line 84 | Verbatim match |
| R6 status is "Not started" | R6 line 94 | Verbatim match (with trailing period for sentence form) |
| Coherence risk is project-coherence, not empirical | every phase | Each §Coherence risk names a project-coherence failure mode (terminology drift, source-of-truth drift, claim-inflation, identity erosion); none name an empirical risk (data-collection failure, instrument error, etc., which would be empirical) |
| No empirical overclaim | every phase | No phase claims the Coherence Path Hypothesis is supported. R4 explicitly states "neither validated nor refuted." R3 explicitly states "empirical claim is held in reserve." R1 cites the comparison passing but flags it as the *technology stack*, not the construct. |
