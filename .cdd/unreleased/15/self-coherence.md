# Self-coherence — cycle/15 — Sub D CDR refactor conformance sweep

## Gap

**Issue:** usurobor/cph#15 — Sub D CDR refactor conformance sweep (AC8 / AC9 / AC10 across A+B+C).
**Master:** usurobor/cph#11.
**Wave:** `.cdd/waves/cdr-refactor-2026-05-18/` — Sub D is the final terminal sub, gated behind Subs A/B/C (all merged).
**Mode:** docs-only (conformance sweep — verifies; does not author charter / roadmap / infra content).
**Surface swept:** every non-`.cdd/` path touched by the three merged subs:

- Sub A (`c3c274a`): `README.md`, `CDR.md`, `docs/concepts/coherence-path-hypothesis.md`, `docs/articles/seven-ways-people-walk.md`.
- Sub B (`49cd888`): `ROADMAP.md`.
- Sub C (`f6ad183`): `CHANGELOG.md`, `PROJECT.md`, `targets/{registry,hypothesis,method,evidence,repo}.tsc`, `scripts/measure-coherence.sh`, `.gitignore`.

Pre-wave baseline = `317779c^1` = `d30aa4a` (last `main` commit before δ opened the wave). The A+B+C diff against that baseline is the swept surface; `.cdd/**` and `.tsc/**` are excluded per wave manifest and `.gitignore`.

**ACs in scope:**

- AC8 — no empirical overclaim (hypothesis validated; seven families proven; AI can classify; support paths directly visible; gait implies identity/personality/diagnosis/pathology).
- AC9 — no data policy regression (no raw `*.trc *.mot *.sto *.c3d *.osim *.mp4 *.mov`, no new payload under `data/external/**`).
- AC10 (final) — every source-of-truth row in `README.md` resolves; the question→owner mapping is injective; Sub A/B/C-authored files match their declared owners.

**Out of scope:** authoring new charter / roadmap / infra content (Subs A/B/C did that); running `scripts/measure-coherence.sh` (operator gate); modifying empirical state.

## Skills

**Tier 1 (CDD core):**
- `cdd/CDD.md` — canonical lifecycle and role contract.
- `cdd/alpha/SKILL.md` — α role surface; this cycle exercises §2.6 (pre-review gate) and §2.7 (review-readiness), with the additional sweep-specific load order in the dispatch (verification, not authoring).

**Tier 3 (issue-specific):**
- `cnos.core/skills/write/SKILL.md` — self-coherence is a short prose artifact: one governing question per section, stable facts pointed to once, sweep verdicts stated positively (state what passes, not just what was checked).
- `eng/bash` is named in the issue but is not present as a discrete skill in the local tree; the sweep oracles are short one-liners (`git grep`, `git diff --name-only`, path-existence loop) and do not require a dedicated skill load.

**Not loaded (out of scope for sweep):** `cdd/design/SKILL.md`, `cdd/plan/SKILL.md` — no design or planning artifact required; the sweep is a verification with all rules supplied by the issue body. β and γ role skills are explicitly excluded by §2.1 step 6.

## ACs

### AC8 — No empirical overclaim — substantively MET

**Oracle (verbatim from issue body):**

```bash
git grep -nE '(hypothesis is (now )?(validated|proven|confirmed)|seven families (are|have been) (validated|proven|confirmed)|AI (can|is able to) classif|support path(s)? (are|is) (directly )?(visible|observed|seen))' -- ':!.cdd/*'
```

**Oracle output (1 match):**

```
ROADMAP.md:3:This file tracks the gates by which the Coherence Path Hypothesis is validated, revised, or abandoned.
```

**Verdict on the oracle hit:** the matched substring is `Hypothesis is validated`, but the surrounding clause is `the gates by which the Coherence Path Hypothesis is validated, revised, or abandoned` — a disjunctive list of *possible outcomes the roadmap tracks*, not a positive claim that the hypothesis is validated. The sentence parallels master `cph#11` §"Definition of done" (which uses `Validate, revise, or abandon`) and `ROADMAP.md` L9 (`Validate, revise, or abandon the Coherence Path Hypothesis through gates...`). Three lines down at `ROADMAP.md:11`, the file states the empirical posture unambiguously: `R1 is REVISE`. AC8 reads on positive claims; the oracle hit is not a positive claim. Documented as a structural-vs-substantive distinction in §Self-check; not modified per dispatch constraint *do not silently rewrite charter content*.

**Broader sweep (paraphrases beyond the issue regex):**

```bash
git grep -niE '(fascia line|personality|diagnos|identif(ying|y) (your|the) gait type|gait type tells|reveals (your|the) (identity|personality|pathology)|body-typ|typology of people)' -- ':!.cdd/*'
```

Every match across `README.md`, `ROADMAP.md`, `docs/articles/seven-ways-people-walk.md`, `docs/concepts/coherence-path-hypothesis.md`, `docs/concepts/support-path.md`, `CHANGELOG.md`, and `PROJECT.md` is in the *disclaimer direction* — `not diagnosis`, `not personality inference`, `not a typology of people`, `not a fascia line`, `body-typing` named as a coherence risk to avoid. No positive claim of the forbidden form.

```bash
git grep -niE '\b(validated|proven|confirmed|established|demonstrated)\b' -- '<swept files>'
```

11 matches across the swept set. Categorized:

- 7 matches are explicit negations carrying the REVISE posture (`is not validated`, `not refuted`, `not proven categories`, `The list is not validated`).
- 2 matches name the forbidden read as a coherence *risk to avoid* (`treats the seven gait families as proven by a clustering output`; `the seven gait families being reintroduced as proven categories by automated labels`).
- 1 match is `accepted only after recurrence and distinguishability are demonstrated on data capable of showing them` — a forward condition, not a current claim.
- 1 match is `ROADMAP.md:3` (the oracle hit; already analyzed above).

**AC8 conclusion:** substantively MET. No file claims the hypothesis is validated, the families are proven, AI can classify, support paths are directly visible, or gait implies identity/personality/diagnosis/pathology. The single oracle trigger on `ROADMAP.md:3` is process language about the roadmap's purpose, not a positive claim, and is cross-referenced in §Self-check.

### AC9 — No data policy regression — MET

**Oracle (verbatim from issue body):**

```bash
git diff --name-only 317779c^1...cf240e1 -- '*.trc' '*.mot' '*.sto' '*.c3d' '*.osim' '*.mp4' '*.mov' 'data/external/**'
```

**Output:** empty.

**Adjacent checks:**

- `git diff --name-only 317779c^1...cf240e1 -- 'data/'` → empty (A+B+C did not touch anything under `data/`).
- `git diff --name-only 317779c^1...cf240e1 -- '*.ipynb'` → empty (no notebook output cells committed by A+B+C).
- `git ls-tree -r --name-only HEAD -- data/external/` → `data/external/README.md`, `data/external/opencap-lab-validation.md` (both pre-existing manifests; both within the issue's `manifest / README` allowlist).
- Sub C's `.gitignore` (commit `f6ad183`) adds structural guards: `data/external/**/*.{zip,tar.gz,trc,mot,c3d,sto,osim,csv,parquet}` and `*.mp4 *.mov *.m4v *.avi *.heic` patterns plus `data/raw/`, `data/private/`, `opencap_exports/`, `participants/`, `consent/` directory ignores. The data-policy invariant is now enforced at the gitignore layer in addition to the manifest discipline that already existed.

**AC9 conclusion:** MET. No raw data, no archive payloads, no participant traces, no videos, no `*.trc *.mot *.sto *.c3d *.osim` artifacts, and no private notebook outputs were committed by A+B+C. The `.gitignore` strengthening *reduces* the surface for future regression rather than introducing one.

### AC10 (final) — Source-of-truth boundaries are explicit — MET

**Table parsed from `README.md` L97–107:**

| # | Question | Owning file |
|---|----------|-------------|
| 1 | What is this project? | `README.md` |
| 2 | What is CDR? | `CDR.md` |
| 3 | What is the hypothesis? | `docs/concepts/coherence-path-hypothesis.md` |
| 4 | What is a support path? | `docs/concepts/support-path.md` |
| 5 | Where are research gates tracked? | `ROADMAP.md` |
| 6 | What is current operational status? | `PROJECT.md` |
| 7 | What changed over time? | `CHANGELOG.md` |
| 8 | What empirical evidence exists? | `reports/` |
| 9 | What TSC targets are measured? | `targets/` |

**Path-existence check (`test -e` per row):**

```
OK   README.md
OK   CDR.md
OK   docs/concepts/coherence-path-hypothesis.md
OK   docs/concepts/support-path.md
OK   ROADMAP.md
OK   PROJECT.md
OK   CHANGELOG.md
OK   reports        (contains: field-report-00-plan.md, field-report-01-existing-data-zeroth-pilot.md, field-report-02-friend-pre-pilot.md)
OK   targets        (contains: registry.tsc, hypothesis.tsc, method.tsc, evidence.tsc, repo.tsc)
```

**Injectivity check:** 9 distinct questions, 9 distinct owners — no question shares an owner with another question. The mapping is injective on both sides.

**Sub A/B/C-authored owner alignment:**

- Sub A authored `README.md` (rewrite), `CDR.md` (new), `docs/concepts/coherence-path-hypothesis.md` (new) — owners 1, 2, 3 match.
- Sub A also authored `docs/articles/seven-ways-people-walk.md` (new), which is *not* a table owner; it is a referenced sibling under `README.md` and the seven-families doc in `docs/concepts/coherence-path-hypothesis.md`. The wave manifest treats it as referenced material, not a question-owner. No drift.
- `docs/concepts/support-path.md` (owner 4) is pre-existing; Sub A cross-references it from `README.md` and the hypothesis doc, consistent with the wave-pinned path table.
- Sub B authored `ROADMAP.md` (new) — owner 5 matches.
- Sub C authored `CHANGELOG.md` (new), `targets/*.tsc` (new), and repartitioned `PROJECT.md` — owners 6, 7, 9 match.
- Owner 8 (`reports/`) and owner 4 (`docs/concepts/support-path.md`) are pre-wave surfaces, preserved and referenced.

**AC10 conclusion:** MET. All nine source-of-truth rows resolve to real paths; the mapping is injective; every Sub A/B/C-authored owner file matches its declared row.
