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

## Self-check

**Did α's work push ambiguity onto β?** No. The sweep is a closed verification: oracle expressions are given in the issue body, oracle outputs are pasted verbatim, broader paraphrase greps are written out, and the AC10 row-by-row check is enumerable from `README.md` alone. β does not need to re-derive what was swept or what counts as a violation — every verdict is backed by evidence in the diff or in the swept files.

**Is every claim backed by evidence in the diff?** Yes. The diff at HEAD adds only `.cdd/unreleased/15/self-coherence.md` (this file) on top of the merged A+B+C state. Every verdict in §ACs references either (a) merged content under `git show`-able SHAs (`c3c274a`, `49cd888`, `f6ad183`), (b) tree state under `HEAD` paths, or (c) an oracle whose command is pasted in §ACs so β can re-run it.

**One oracle false-positive disclosed (AC8, `ROADMAP.md:3`):** the regex literal in the issue body matches `Hypothesis is validated` even when the validation verb is the first item in a disjunctive list of outcomes (`validated, revised, or abandoned`). I considered three responses:

1. **Mechanical rephrase of L3 on cycle/15** (e.g., `tested, revised, or abandoned`). Rejected: the dispatch constraint explicitly forbids silent rewrite of A+B+C charter content; the change is *paraphrase*, not typo / table correction. The issue's own §"Definition of done" uses the same `Validate, revise, or abandon` phrasing — rewriting it on a sweep cycle would introduce divergence between the master charter and Sub B's deliverable.
2. **File as deferred debt and modify nothing.** Chosen for the substantive resolution: the sentence is process language, not a positive empirical claim; AC8 is substantively met; the oracle is a structural approximation and the substantive AC must govern.
3. **Modify the oracle.** Rejected: the issue's oracle is part of the charter; modifying it on cycle/15 would be silent rewrite of issue-as-spec.

The disclosure pattern follows `alpha/SKILL.md` §2.3 (intra-doc / commit-message peer enumeration) — every occurrence of the oracle's trigger phrase across the swept files was grepped; only `ROADMAP.md:3` produces a string-match without a substantive violation, and the §Debt entry below names it explicitly so any future re-sweep that re-runs the literal oracle has the prior judgment in hand.

**Polyglot re-audit (`alpha/SKILL.md` §2.6 row 9):** the diff at α's HEAD is single-language (Markdown). No shell, YAML, or Go surfaces. The pre-A+B+C diff covered Bash (`scripts/measure-coherence.sh`) and TOML-ish manifests (`targets/*.tsc`); those were audited by Sub C's α and β rounds. Sub D does not re-author them; it grep-sweeps them for AC8 strings (all clean — no matches).

**Peer enumeration applied to AC8:** the issue body names 5 forbidden claim families. Each was swept across the full A+B+C surface:

| Family | Searched terms (case-insensitive) | Hits | Verdict |
|--------|------------------------------------|------|---------|
| hypothesis validated/proven/confirmed | `hypothesis is (now )?(validated\|proven\|confirmed)` | 1 (oracle false-positive, ROADMAP.md:3) | substantively clean |
| seven families validated/proven/confirmed | `seven families (are\|have been) (validated\|proven\|confirmed)` | 0 | clean |
| AI can classify gait strategies | `AI (can\|is able to) classif` | 0 | clean |
| support paths directly visible/observed/seen | `support path(s)? (are\|is) (directly )?(visible\|observed\|seen)` | 0 | clean |
| gait implies identity/personality/diagnosis/pathology | `fascia line\|personality\|diagnos\|...\|body-typ\|typology of people` | 16 across 12 files | all disclaimers (negations); no positive claim |

**Intra-doc repetition check on AC10 owners:** the 9 owners in the table are all referenced elsewhere in `README.md`. §"Where to go next" L113–119 explicitly links 5 owners (`coherence-path-hypothesis.md`, `support-path.md`, `CDR.md`, `PROJECT.md`, `reports/field-report-01-...`). The remaining 4 are: `README.md` itself (self-referential); `ROADMAP.md`, `CHANGELOG.md`, and `targets/` each explicitly named in `README.md:109` (`ROADMAP.md, CHANGELOG.md, and targets/ are delivered by sibling sub-issues in the same wave`). No owner is mentioned only in the table; no intra-doc owner-path drift detected.

## Debt

**No deferred debt blocking AC8, AC9, or AC10 closure.** The sweep finds the substantive invariants intact and the structural invariants intact.

**Disclosed structural finding (non-blocking, AC8):**

- **F1 — AC8 oracle false-positive on `ROADMAP.md:3`.** The issue's verbatim oracle (`hypothesis is (now )?(validated|proven|confirmed)`) matches `the gates by which the Coherence Path Hypothesis is validated, revised, or abandoned`. Substantive verdict: not a violation — disjunctive process language. Cross-reference: `ROADMAP.md:3` (file path + line), merged in commit `49cd888` (Sub B merge). The same phrasing appears in master `cph#11` §"Definition of done" (`Validate, revise, or abandon the Coherence Path Hypothesis`) and `ROADMAP.md:9`, so the phrasing is inherited from the master charter, not a Sub B drift. **Not fixed on cycle/15** per dispatch constraint *do not silently rewrite charter content*. Recommended future handling (γ disposition decision; α does not recommend): either (a) leave as-is and let a future re-sweep apply the same substantive judgment, or (b) tighten the issue's regex to require `\bis (now )?validated\b(?!.*\bor\b)` so it does not match disjunctive lists. Option (b) is a wave-management edit to the spec, not a charter edit.

**Adjacent items (not in scope; named for completeness so γ can carry them forward):**

- The cnos cross-repo bundle path under `cnos:.cdd/iterations/cross-repo/gait-support-paths/bootstrap-cdr/` still uses the pre-rename name (per wave manifest §"Out-of-scope follow-ups"). Sub D does not touch cnos; this is downstream cross-repo work.
- The orthogonal `origin/cycle/segmentation-real-data-fix` branch (tip `a95415c`) is unmerged. Independent of this wave; named in `ROADMAP.md` Phase R2 as the planned next bounded cycle.
- The TSC mechanical baseline run via `scripts/measure-coherence.sh` is an operator gate (per master `cph#11` AC6 / wave manifest standing permissions). Sub D does not execute it.

**Self-check on debt completeness:** none of the items above blocks Sub D's closure. The sweep does not find empirical, data-policy, or source-of-truth violations. The single structural finding is named with file + line + merge SHA + substantive disposition, so β can verify the finding's framing against the merged ROADMAP.md content without re-deriving the sweep.

## CDD-Trace

Per `CDD.md` §5.2 (canonical artifact order). Sub D is verification-only; several steps are explicitly `not required` with reason.

1. **Design** — *not required.* The sweep's rules are pre-specified in `cph#11` ACs 8/9/10 (oracles, surfaces, invariants). No design space to explore; no impact graph to map; the work is a closed verification against a fixed checklist.
2. **Coherence contract** — `.cdd/unreleased/15/self-coherence.md` §Gap (above). The contract is *the swept surface = the non-`.cdd/` diff between pre-wave baseline `317779c^1` and `cf240e1` (post-A+B+C+δ status), under the three ACs*.
3. **Plan** — *not required.* The oracle commands in the issue body provide ordering; the AC10 row-by-row check is enumerable from `README.md` L97–107.
4. **Tests** — the sweep oracles are the tests. They are pasted verbatim in §ACs (one literal oracle per AC, plus paraphrase-broadening greps), so β can re-run them at HEAD:
   - AC8 literal oracle (issue body) → 1 hit (`ROADMAP.md:3`), substantively non-violating; analyzed.
   - AC8 paraphrase greps (identity/personality/diagnosis/typology; validation-claim verbs) → all hits are disclaimers or risk-naming; analyzed.
   - AC9 oracle (`git diff` over data-file globs) → empty; adjacent checks (`data/`, `*.ipynb`, `data/external/` tracked tree) → all consistent with policy.
   - AC10 path-existence loop over the 9 owners → all `OK`; injectivity check by inspection → 9 distinct questions, 9 distinct owners.
5. **Code** — *not required.* No code authored; the sweep modifies no swept file. `scripts/measure-coherence.sh` is referenced as a swept surface, not edited.
6. **Docs** — only `.cdd/unreleased/15/self-coherence.md` is authored on cycle/15. Per `alpha/SKILL.md` §2.6 row 11 (artifact enumeration matches diff): `git diff --stat origin/main..HEAD` returns one file, `.cdd/unreleased/15/self-coherence.md`, and that file is the entire α surface for this cycle. No new modules, no new functions, no new callers — row 12 (caller-path trace) is vacuous and met.
7. **Self-coherence** — this file. The CDD Trace lands here; the file is published incrementally to `origin/cycle/15` one section per commit per `alpha/SKILL.md` §2.5; the §Review-readiness section will be appended as a separate commit after the pre-review gate (§2.6) passes against HEAD.

## Review-readiness

**Round:** 1.
**Base SHA:** `cf240e1` (origin/main HEAD; re-verified at signal time — `git log --oneline HEAD..origin/main` empty).
**Implementation SHA:** `627191e` (last α commit before this readiness-signal commit; per `alpha/SKILL.md` §2.6 SHA convention "name the implementation SHA, not the readiness-signal HEAD").
**Branch CI:** not configured in this repo (`.github/workflows/` does not exist). Local sweep ran clean against the merged A+B+C state; oracles pasted in §ACs for β re-run.
**Author email:** `alpha@cph.cdd.cnos` on all 7 α commits (`git log --format='%h %ae' origin/main..HEAD` audited — uniform).
**Branch rebase status:** `cycle/15` rebased onto `origin/main` at intake (`e22108b → cf240e1` fast-forward), re-verified at signal time.

**Pre-review gate (`alpha/SKILL.md` §2.6):**

1. Cycle branch rebased onto current `origin/main` — ✅ (verified at intake and at signal).
2. CDD Trace through step 7 — ✅ (§CDD-Trace above).
3. Tests present — ✅ (oracles pasted verbatim in §ACs; sweep mode does not produce a test runner artifact).
4. Every AC has evidence — ✅ (AC8 oracle output + paraphrase greps; AC9 diff command + adjacent checks; AC10 path-existence loop + injectivity check).
5. Known debt explicit — ✅ (§Debt F1 + named adjacent items).
6. Schema/shape audit — N/A (no contract change; sweep does not touch parsers, manifests, or runtime types).
7. Peer enumeration — ✅ (§Self-check table enumerates the 5 AC8 claim families against the full A+B+C surface).
8. Harness audit — N/A (no schema-bearing contract changed).
9. Post-patch re-audit — ✅ (one mid-cycle correction at commit `6a430a3` to the §Self-check intra-doc owner-reference count; re-audited; single-language Markdown diff).
10. Branch CI green on head commit — N/A (no CI workflow; declared explicitly above; β may merge without waiting).
11. Artifact enumeration matches diff — ✅ (`git diff --stat origin/main..HEAD` → 1 file; named in §Gap, §CDD-Trace step 6, and §Debt; matches exactly).
12. Caller-path trace for new modules — N/A (no new modules; sweep authors no code).
13. Test assertion count from runner output — N/A (sweep does not produce runner output; oracle outputs pasted verbatim in §ACs).
14. Author email canonical — ✅ (all 7 α commits authored as `alpha@cph.cdd.cnos`).

**Transient row re-validation (§2.7):**

- Row 1 (rebase) observed at signal time: HEAD = `627191e`, origin/main = `cf240e1`, `HEAD..origin/main` empty. No drift since pre-review gate write.
- Row 10 (CI) declared N/A at write time; state cannot drift between write and signal.

**Verdict:** ready for β review.

Polling for β response begins immediately, every 60s, on `.cdd/unreleased/15/beta-review.md` and the issue per `alpha/SKILL.md` §Tracking.
