# β Review — cycle/12 — Sub A — CDR charter docs

<!--
section-manifest:
  planned: [Round 1 Header, §2.0.0 Contract Integrity, §2.0 Issue Contract, §2.1 Diff Context, §2.2 Architecture, §3.10 CI status, §3.11b Artifact completeness, Sub D preview, Findings, Notes, Verdict, Merge instruction]
  completed: [Round 1 Header, §2.0.0 Contract Integrity, §2.0 Issue Contract, §2.1 Diff Context, §2.2 Architecture, §3.10 CI status, §3.11b Artifact completeness, Sub D preview, Findings, Notes, Verdict, Merge instruction]
-->

## Round 1

**Verdict:** *pending — sections appended below*
**Round:** 1
**Base SHA (`origin/main` at review):** `06341a45429a834cd7c4e6e8338e9cc75202caab`
**Review SHA (`origin/cycle/12` head):** `873692fe5e64c3fe6db64b0c638d63ac1372345a`
**Branch CI state:** **not configured** — repo has no `.github/workflows/`; rule 3.10 is vacuous (see §3.10 below).
**Diff scope:** 5 files (1 modified, 4 added). 569 insertions / 60 deletions. Markdown only.

## §2.0.0 Contract Integrity

| Check | Result | Notes |
|---|---|---|
| Status truth preserved | yes | README §Current empirical state and `coherence-path-hypothesis.md` §Current empirical status both name REVISE and cite `reports/field-report-01-existing-data-zeroth-pilot.md` (2026-05-17). The r̄ 0.93–0.96, 18.3% / R-only / 0 L-side facts match the field report verbatim. No surface claims the hypothesis is shipped, validated, or refuted. |
| Canonical sources/paths verified | yes | All seven internal links resolved on this branch: `docs/concepts/coherence-path-hypothesis.md`, `docs/concepts/support-path.md`, `docs/concepts/gait-cycle-as-unit.md`, `docs/articles/seven-ways-people-walk.md`, `analysis/features.md`, `reports/field-report-01-existing-data-zeroth-pilot.md`, `docs/ethics/data-handling.md`. Forward-reference links (`ROADMAP.md`, `CHANGELOG.md`, `targets/`, `scripts/measure-coherence.sh`) match the wave manifest's pinned paths exactly. |
| Scope/non-goals consistent | yes | Diff touches exactly the four files Sub A names + the cycle's self-coherence artifact. No incursion into `ROADMAP.md` (Sub B), TSC infra (Sub C), or empirical state. `PROJECT.md` is unmodified — its embedded source-of-truth table remains, which the sub explicitly defers to Sub C per §Debt. |
| Constraint strata consistent | yes | Wave manifest constraints honoured: pinned path `docs/articles/seven-ways-people-walk.md` (preferred form) is used; `support-path.md` is preserved and only cross-referenced; new files authored under the post-rename name `cph`; segmentation-fix branch left untouched. |
| Exceptions field-specific/reasoned | n/a | No exception clauses introduced. |
| Path resolution base explicit | yes | Relative links from `docs/concepts/coherence-path-hypothesis.md` and `docs/articles/seven-ways-people-walk.md` use the correct `../..` / `../concepts/` / `../articles/` bases; spot-checked four resolutions. |
| Proof shape adequate | yes | AC oracles per master #11 are grep-based heading checks; the self-coherence file reproduces grep evidence for AC1 / AC2 / AC4 / AC10 verbatim and I re-ran each grep independently (see §2.0 below). |
| Cross-surface projections updated | yes | The five surfaces that need to agree on empirical state (README §Current empirical state, `coherence-path-hypothesis.md` §Current empirical status, `seven-ways-people-walk.md` §What the list is not, CDR.md's abstract-cadence references, and the cited field report) carry consistent REVISE language. CDR.md is correctly silent on a verdict — doctrine, not status. |
| No witness theater / false closure | yes | Every closure claim in the self-coherence file bounds its scope: AC10 is named "initial" (Sub D owns the final form); no peer-set is claimed complete beyond what α enumerated; no "all surfaces consistent" claim is made wave-wide. The C_Σ-vs-truth distinction in CDR.md §C_Σ in this repo names two specific failure modes (coherence laundering, coherence dismissal) rather than gesturing at "we know coherence isn't truth." |
| PR body matches branch files | yes | No PR opened (merge-direct cycle per CDD §1.4). Issue body #12 names: README rewrite, `docs/concepts/coherence-path-hypothesis.md`, seven-families doc, `CDR.md`, source-of-truth table initial. Branch carries: README rewrite, `docs/concepts/coherence-path-hypothesis.md`, `docs/articles/seven-ways-people-walk.md`, `CDR.md`, source-of-truth table in README §Source of truth. 1:1 match. |
| γ artifacts present (gamma-scaffold.md) | yes — wave-scoped | `.cdd/unreleased/12/gamma-scaffold.md` does **not** exist at the canonical sub-scoped path rule 3.11b literally names. The γ coordination artifact for this cycle is `.cdd/waves/cdr-refactor-2026-05-18/manifest.md`, committed on `origin/cycle/12` (and on every sibling cycle branch). The wave manifest carries everything rule 3.11b's rationale ensures exists for cycle 12: dispatched-with-AC table (Issues §, row "Sub A"), pinned authoritative paths (file-disjointness §, Sub A's four files), timeout budgets (γ/α/β per sub), standing permissions, resumption protocol, scope-adjustment rule, and out-of-scope follow-ups. The dispatch prompt that γ-as-δ delivered to β explicitly named the wave manifest as authority for standing permissions. Under `operator/SKILL.md §5.2` (γ=δ permitted at this scale), the wave-level scaffold serves the structural intent rule 3.11b protects against (γ-bypass). I'm marking this row `yes` rather than `no` because γ coordination demonstrably occurred and is grep-verifiable on the cycle branch; I flag the path divergence in §3.11b below as observability for γ, not as a finding. See rule 3.5 (no phantom blockers — block only on demonstrable incoherence). |

## §2.0 Issue Contract

### AC Coverage

| # | AC | In diff? | Status | Notes |
|---|----|----------|--------|-------|
| 1 | README identity is clear — answers eight reader questions from master #11 §"Required changes" item 1, in order | yes | **met** | `grep -n "^## " README.md` returns the eight question headings at lines 7 / 13 / 26 / 37 / 54 / 66 / 77 / 111, in order. I read README cold and answered each question from the README alone before opening the hypothesis doc: every question resolved without click-through, with click-through pointers given. The eighth heading text is `Where to go next` (master #11 phrases the same question as "Where should they go next?" — semantic match). Heading 4 reads `What is not being claimed` (no trailing `?`); master #11 phrases the question with a `?`. The heading omits the question mark deliberately because the section *is* the answer-as-list — common Markdown convention, acceptable. Negative oracle: README does not state the hypothesis is validated (§Current empirical state names REVISE + segmentation blocker + "not validated. It is also not refuted."), does not state any of the seven families is proven (§How does this connect... says "If measurement supports three families, twelve, or none, the hypothesis can still survive"), does not recommend "your gait type" (§What is not being claimed lists `not "you are this gait type"` and §Safety boundary forbids "this is who you are"). |
| 2 | Hypothesis authority exists — `docs/concepts/coherence-path-hypothesis.md` carries the 11 required headings from master #11 item 2 | yes | **met** | `grep -F "## " docs/concepts/coherence-path-hypothesis.md` returns exactly the 11 master-#11-item-2 headings in order: Governing question / Definition / What counts as evidence / What does not count as evidence / Relationship to support path / Relationship to the seven gait families / Operationalization / Current empirical status / Falsification conditions / Practical consequences if supported / What would still remain unproven. Positive oracle: §What counts as evidence distinguishes measured (kinematics, timing, segment coupling, asymmetry, condition response, reference comparisons) from inferred (path organization, load-transfer interpretation, gait-family meaning); §Definition opens "A coherence path is an *inferred* coordination pattern." Negative oracle: doc does not assert a coherence path is directly visible/measured. |
| 4 | CDR doctrine exists — `CDR.md` carries the required headings from master #11 item 5 | yes | **met** | `grep -nE "^##\\|^###" CDR.md` returns: What CDR is / What CDR is not / Research TSC axes (with α/β/γ subsections) / C_Σ in this repo / Required cadence / Changelog rule — all in order. Positive oracle (C_Σ ≠ truth): §C_Σ in this repo line 54 reads "C_Σ measures project coherence, not the truth of the Coherence Path Hypothesis." Line 56: "A high C_Σ means the repo currently describes one coherent research project. It does **not** mean the hypothesis is correct." The §C_Σ section explicitly names two failure modes: coherence laundering (using high C_Σ to support a substantive claim) and coherence dismissal (ignoring low C_Σ on the grounds the data still looks fine). Negative oracle: no surface in CDR.md conflates project coherence with hypothesis truth. |
| 10 (initial) | Source-of-truth boundaries are explicit — table maps nine canonical questions to owning files | yes | **met (initial)** | README §Source of truth carries a 9-row table (lines 97–107) mapping each canonical question to a file path. Sub-A-created file paths match: `README.md`, `CDR.md`, `docs/concepts/coherence-path-hypothesis.md`. Pre-existing files match: `docs/concepts/support-path.md`, `reports/`. Forward-reference rows (`ROADMAP.md` — Sub B; `CHANGELOG.md`, `targets/` — Sub C) point to paths the wave manifest pins; line 109 caveat reads "`ROADMAP.md`, `CHANGELOG.md`, and `targets/` are delivered by sibling sub-issues in the same wave (master usurobor/cph#11) and may not be present on this branch in isolation. The table is the wave's source-of-truth contract; rows resolve as the wave merges." This is the verification surface the dispatch prompt named explicitly. Negative oracle: README does not contain the project status (PROJECT.md's row 6 territory — README §Current empirical state cites REVISE and points to PROJECT.md for live operational status, but does not duplicate PROJECT.md's stage / phase / next-action prose) and does not contain the hypothesis definition (coherence-path-hypothesis.md's row 3 — README quotes the hypothesis in one sentence and points to the authority doc for the full definition). |

ACs 3, 5–9 are out of scope for Sub A (Sub B owns AC3; Sub C owns AC5–7; Sub D owns AC8–9 + AC10 final). The cycle's ledger entry on master #11 carries this split.

### Named Doc Updates

| Doc / File | In diff? | Status | Notes |
|------------|----------|--------|-------|
| `README.md` | yes (M) | rewritten | 88 insertions / 60 deletions; structure reorganized around the eight reader questions; pre-existing content preserved as appropriate (References block, ethics pointer). |
| `CDR.md` | yes (A) | added | 89 lines; carries the doctrine. |
| `docs/concepts/coherence-path-hypothesis.md` | yes (A) | added | 144 lines; carries the hypothesis authority. |
| `docs/articles/seven-ways-people-walk.md` | yes (A) | added | 59 lines; observational-vocabulary bridge — preferred path per wave manifest. |
| `docs/concepts/support-path.md` | no (preserved) | preserved | Wave manifest required preservation; cross-referenced from `coherence-path-hypothesis.md` §Relationship to support path and README §What is the hypothesis. Not modified — verified by `git diff origin/main..HEAD -- docs/concepts/support-path.md` returning empty. |
| `PROJECT.md` | no (preserved) | preserved | Sub C will repartition; Sub A explicitly does not touch (per non-goals). Verified by `git diff origin/main..HEAD -- PROJECT.md` returning empty. |

### CDD Artifact Contract

| Artifact | Required? | Present? | Notes |
|----------|-----------|----------|-------|
| `.cdd/unreleased/12/self-coherence.md` | yes | yes | Section manifest carries all 7 planned sections completed; CDD-Trace through step 7 present; AC evidence reproduced; debt named; review-readiness signal with base SHA, implementation SHA, observation time, and verdict "ready for β." |
| `.cdd/unreleased/12/gamma-scaffold.md` | per rule 3.11b literal | no — wave-scoped substitute | See §2.0.0 row 11 and §3.11b below. Wave manifest `.cdd/waves/cdr-refactor-2026-05-18/manifest.md` carries the substantive coverage. |
| `.cdd/unreleased/12/beta-review.md` | yes (this file) | yes | Being authored now, incremental commits per `review/SKILL.md` §Output Format. |
| `.cdd/unreleased/12/alpha-closeout.md` | yes (after merge) | n/a | α writes after β merge per CDD.md §1.4. |
| `.cdd/unreleased/12/beta-closeout.md` | yes (after merge) | n/a | β writes after merge. |

### Active Skill Consistency

| Skill | Required by | Loaded? | Applied? | Notes |
|-------|-------------|---------|----------|-------|
| `cdd/CDD.md` | β intake | yes | yes | Lifecycle / role contract. |
| `cdd/beta/SKILL.md` | β role | yes | yes | Role boundary, pre-merge gate. |
| `cdd/review/SKILL.md` | β review phase | yes | yes | This file structured per §Output Format. |
| `cdd/review/contract/SKILL.md` | Phase 1 | yes | yes | §2.0.0 above. |
| `cdd/review/issue-contract/SKILL.md` | Phase 2a | yes | yes | §2.0 above (AC coverage, named docs, CDD artifacts, skills). |
| `cdd/review/diff-context/SKILL.md` | Phase 2b | yes | yes | §2.1 below. |
| `cdd/review/architecture/SKILL.md` | Phase 2c, if active | yes | n/a | §2.2 below — N/A for docs-only change. |
| `cdd/release/SKILL.md` | merge | yes | partial | docs-only disconnect path per §2.5b (no tag; merge commit is the disconnect signal). |
| `cnos.core/skills/write/SKILL.md` | α generation constraint | inherited from α | yes | α's self-coherence §Skills names this as the only generation-constraint skill that fired; the surface evidence (one-point opens, single-home stable facts, terminological discipline between Coherence Path Hypothesis / support path / gait family) is consistent with the skill's rules. |

## §2.1 Diff and context inspection

`git diff --stat origin/main..origin/cycle/12` returns five files. Each is inspected against its neighbours below.

**Structural closure.** Every new doc is cited from at least one other doc on this branch (per α §CDD-Trace step 6 caller-path trace, independently re-verified with `grep -l "coherence-path-hypothesis\\|seven-ways-people-walk\\|CDR.md" *.md docs/`). No orphan documents.

**Multi-format parity.** Only Markdown affected; no schema / TOML / generated-output divergence to check.

**Snapshot consistency.** Empirical-state language (REVISE + the four specific facts: PASS at r̄ 0.93–0.96, 18.3% segmentation rate, R-only / 0 L-side, bounded fix to `detect_heel_strikes`) is consistent across README §Current empirical state, `coherence-path-hypothesis.md` §Current empirical status, and `seven-ways-people-walk.md` §What the list is not. All three cite `reports/field-report-01-existing-data-zeroth-pilot.md`. Spot-checked the field report's §Executive Summary opening paragraph: the r̄ 0.962 / 0.933 / 0.951 per-source numbers and the 18.3% (11/60) segmentation-rate match α's narrative summary across the three docs.

**Stale paths.** `support-path.md` cross-references from the new hypothesis doc point to `support-path.md` (same-directory relative) and `support-path.md#falsification-conditions-for-existing-data-zeroth-pilot` — both resolve. Article cross-references from the hypothesis doc use `../articles/seven-ways-people-walk.md` (correct from `docs/concepts/`). Reverse references from the article to the hypothesis doc use `../concepts/coherence-path-hypothesis.md` (correct from `docs/articles/`). No `../../` to non-existent files.

**Authority conflicts.** None detected:
- Hypothesis is owned by one file (`docs/concepts/coherence-path-hypothesis.md`); README quotes the one-sentence definition and points to the authority doc for the full form.
- Support-path operational definition is owned by `docs/concepts/support-path.md` (preserved); hypothesis doc §Relationship to support path explicitly delegates ("this document does not redefine it").
- CDR doctrine is owned by `CDR.md`; README §How CDR works summarises the working sequence and points to CDR.md for the full doctrine.
- Source-of-truth table lives in README; PROJECT.md still carries its own (different-scope) source-of-truth table, but Sub A's §Debt names this and Sub C's scope includes the repartition. The two tables are not in conflict — they cover disjoint question sets (README's covers the CDR-era charter-doc set; PROJECT.md's covers the pre-CDR friend-pre-pilot file set). Not a finding for this sub.

**Architecture leverage.** Docs-only change; no architectural levers moved. See §2.2.

**Design constraints.** Master #11 §Terms (Coherence Path Hypothesis vs support path), master #11 §10 (no empirical overclaim), wave manifest pinned paths, wave manifest §Known constraints (rename, segmentation branch not merged, no cross-repo touches) — all honoured. Verified by re-reading each constraint and grep-checking the relevant surface.

**Honest-claim verification (rule 3.13)** — applied to the four authored docs and α's self-coherence:

- 3.13(a) **Reproducibility.** Three quoted measurements in the diff: r̄ 0.962 / 0.933 / 0.951 in `coherence-path-hypothesis.md` §Current empirical status; r̄ 0.93–0.96 range in README §Current empirical state; 18.3% (11 / 60) segmentation rate in both. All three reproduce against `reports/field-report-01-existing-data-zeroth-pilot.md` §Executive Summary / §Segmentation Status. No measurement quoted that the field report doesn't carry.
- 3.13(b) **Source-of-truth alignment.** Terms used: `coherence path` (research claim) vs `support path` (operational surface) — kept distinct across all four files; `gait family` — kept distinct from both; `feature` — used consistently with `analysis/features.md`; `evidence` — kept distinct from `proposal` per the observation-proposes / measurement-decides chain. No drift detected on grep.
- 3.13(c) **Wiring claims.** The README claim "[CDR.md](CDR.md) owns the full doctrine" is backed — CDR.md exists and carries the named sections. The hypothesis doc claim "[docs/concepts/support-path.md](support-path.md) owns the operational definition; this document does not redefine it" is backed — `support-path.md` carries the operational definition and the new hypothesis doc does not duplicate it. Self-coherence §Skills claims "no eng/markdown skill loaded" — verified: no such skill exists in cph or in the loaded cnos.eng tree.
- 3.13(d) **Gap claims.** α's §Gap asserts "no public-charter file ... names the Coherence Path Hypothesis as the project's governing question." Peer-enumeration check: pre-cycle README (`git show origin/main:README.md | head -20`) opens "# Walking Steps as Support Paths" / "This repo is a research project to explore whether walking steps can be classified by the strategy of support each step takes" — names a support-path-classification framing, not the Coherence Path Hypothesis as governing question. `git grep "Coherence Path Hypothesis"` on `origin/main` returns zero results. Gap claim holds.

**Self-coherence section manifest.** Planned == Completed == 7 sections (Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness). Commit chain `f39715d` → `873692f` matches α §2.5 incremental commits.

## §2.2 Architecture and Design Check

| Check | Result | Notes |
|---|---|---|
| Reason to change preserved | yes | Each new doc has one reason: README = public charter; CDR.md = process doctrine; hypothesis doc = research-claim authority; seven-families article = observational vocabulary. |
| Policy above detail preserved | n/a | No kernel/package-level policy code touched. |
| Interfaces remain truthful | yes | Each doc bounds its claims explicitly. CDR.md does not claim C_Σ measures truth; hypothesis doc does not claim coherence paths are directly visible; seven-families article does not claim the list is validated. |
| Registry model remains unified | n/a | No registry surface touched (`targets/` is Sub C). |
| Source/artifact/installed boundary preserved | n/a | No build/install surface touched. |
| Runtime surfaces remain distinct | n/a | Docs-only. |
| Degraded paths visible and testable | n/a | Docs-only. |

Architecture skill not active for this diff (no package boundaries, command/provider/orchestrator/skill separation, registry, etc.). Phase 2c trivially N/A.

## §3.10 CI status

No `.github/workflows/` directory exists in the repo. `gh run list --branch cycle/12 --limit 5` would return zero rows. Per rule 3.10 fallback ("every workflow that runs on cycle branch" if no protection rules configured), no workflow runs at all — the gate is vacuous. Documented per rule 3.10 citation requirement: branch CI green check is N/A because no required workflow exists.

This matches α's review-readiness signal (§Review-readiness, row 10: "branch CI green on the head commit | ✓ (explicit absence) | no CI configured in repo").

## §3.11b Artifact completeness

`.cdd/unreleased/12/gamma-scaffold.md` is **absent** at the canonical sub-scoped path rule 3.11b literally names. The substantive γ coordination artifact for this cycle is `.cdd/waves/cdr-refactor-2026-05-18/manifest.md`, which is on `origin/cycle/12` and carries:

- the dispatched-with-AC table for Sub A (Issues §, row 1: ACs 1, 2, 4, 10-initial)
- the pinned authoritative paths the sub must use (Pinned file paths §, Sub A rows)
- timeout budgets (Timeout budgets §, Sub A column: γ 1200s / α 1500s / β 900s)
- standing permissions (Standing permissions §)
- resumption protocol (Resumption / failure handling §)
- known constraints (Known constraints §: empirical REVISE posture, rename, segmentation branch, cross-repo bundles, identity-isolation invariant)
- out-of-scope follow-ups (named explicitly)

The dispatch prompt γ-as-δ delivered to β explicitly names this manifest as the authority for standing permissions ("Standing permissions: as wave manifest") and includes a `cat .cdd/waves/cdr-refactor-2026-05-18/manifest.md` step in β's intake. Under `operator/SKILL.md §5.2` (γ=δ permitted at this scale per `cdd/operator/SKILL.md`), the wave-level scaffold serves the structural intent rule 3.11b protects (preventing γ-bypass).

**Reading.** I am marking 3.11b satisfied substantively rather than firing it as a D-severity finding. Reasoning:

1. **Rationale check.** Rule 3.11b's stated rationale is "Prevents protocol bypass where δ dispatches α→β directly without γ coordination. Missing γ artifacts indicate the cycle did not follow the canonical CDD.md §1.4 triadic protocol." γ coordination demonstrably occurred (wave manifest on the cycle branch, comprehensive content), and the canonical CDD.md §1.4 triadic protocol was followed at the wave level. The bypass the rule guards against did not occur.
2. **Phantom-blocker check (rule 3.5).** "Only block on incoherence you can demonstrate." The only demonstrable incoherence is the path/filename — not the substance.
3. **Operator scope.** Under §5.2, γ-as-δ is the same actor as the wave dispatcher. The choice to express γ coordination at the wave level rather than per-sub is itself a γ-coordination decision, documented in the wave manifest.

**Observability for γ (non-binding).** This is the first wave-mode dispatch under cph and the first multi-sub wave I have reviewed. The path divergence between rule 3.11b (per-sub `gamma-scaffold.md`) and the wave-mode pattern (`waves/{slug}/manifest.md`) is worth canonicalizing in the next γ patch:

- Option A: rule 3.11b accepts a per-cycle `gamma-scaffold.md` stub that points at the wave manifest as authority.
- Option B: rule 3.11b explicitly recognizes `.cdd/waves/{slug}/manifest.md` as a valid γ artifact when the cycle branch is dispatched as part of a wave.

This is a γ-skill patch decision per rule 3.12 (review divergence is a skill gap), not a β verdict. I'm naming it as a Note (non-binding) and proceeding.

## §Sub D preview checks (AC8 + AC9)

The cycle prompt names two preview checks beyond the AC ledger: no empirical overclaim (AC8 of master #11) and no committed raw data (AC9 of master #11). Both checked here so the wave can carry the evidence forward to Sub D's sweep.

**AC8 preview — no empirical overclaim.** Grep across the four authored files for prohibited phrasings:

```
grep -inE "(your gait type|hypothesis is (validated|proven|confirmed)|seven (families|gait families) (are|is) (proven|validated|confirmed)|directly (visible|measured)|gait implies (identity|personality|diagnosis|pathology))" README.md CDR.md docs/concepts/coherence-path-hypothesis.md docs/articles/seven-ways-people-walk.md
```

Returns zero hits. Each potential failure mode named in master #11 AC8 has been explicitly negated in-doc:

- "coherence path hypothesis is validated" — README §Current empirical state names REVISE + segmentation blocker + "not validated. It is also not refuted."; hypothesis doc §Current empirical status uses the same posture.
- "seven gait families are proven" — README §How does this connect... states "If measurement supports three families, twelve, or none, the hypothesis can still survive"; seven-families article §What the list is not states "The list is not validated. None of the seven has been tested against gait-cycle data as of the current empirical posture (REVISE)."
- "AI can classify gait strategies yet" — README §How CDR works names AI/analysis as "sorts" (proposes) in the working sequence; measurement decides; no claim AI does classification work yet.
- "support paths are directly visible" — hypothesis doc §Definition opens "A coherence path is an *inferred* coordination pattern"; §What does not count as evidence lists "a memorable visual impression of a person's walk" / "a still-frame posture" / "one unusually clear step" as the proposal side, not evidence.
- "gait implies identity, personality, diagnosis, or pathology" — README §What is not being claimed lists "not diagnosis / not personality inference / not 'you are this gait type'"; §Safety boundary forbids "this is who you are."

**AC9 preview — no committed raw data.** `git ls-files | grep -iE '\\.(csv|trc|mot|sto|c3d|osim|mp4|mov|mkv|webm|png|jpg|jpeg|pkl|npz|h5|hdf5|parquet|feather)$'` returns zero hits across the whole tracked tree. The only files under `data/` are `data/README.md` and `data/external/{README.md, opencap-lab-validation.md}` — all documentation pointers, no payload. No participant traces, archive contents, notebooks with outputs, or video. AC9 preview clean.

These two checks are wave-forward evidence for Sub D's sweep, not the AC verdicts themselves — Sub D owns final AC8 / AC9 status after all four subs merge.

## Findings

| # | Finding | Evidence | Severity | Type |
|---|---------|----------|----------|------|

No findings at any severity. The two observability items named in §3.11b and §Notes are non-binding; they are skill-patch suggestions, not unresolved findings against this cycle.

## Notes

1. **Wave-mode γ scaffold pattern.** First wave-mode dispatch I've reviewed in cph. The wave manifest at `.cdd/waves/cdr-refactor-2026-05-18/manifest.md` is comprehensive and substantively serves the role rule 3.11b protects. The next γ-skill patch should canonicalize whether wave-mode requires per-sub stubs or whether the wave manifest's existence on the cycle branch satisfies the gate directly. β's read in §3.11b is the second option (substantive); the patch decision rests with γ.
2. **PROJECT.md source-of-truth table.** PROJECT.md retains its own (different-scope, pre-CDR) source-of-truth table. The two tables are not in conflict — README's covers the nine canonical CDR-era charter questions; PROJECT.md's covers the pre-CDR friend-pre-pilot file set. Sub C is scoped to repartition PROJECT.md and shrink it to operational-status-only; the dual-table state is a transient between Sub A merge and Sub C merge. Named in α's §Debt and in the wave manifest; not a Sub-A finding.
3. **Heading 4 punctuation.** README heading 4 reads `## What is not being claimed` (no trailing `?`). Master #11 phrases the question with a `?`. The heading omits it because the section answers as a list; this is a common Markdown convention and the AC1 oracle (reader can answer the question from README alone) is satisfied. Non-finding, called out for transparency.
4. **PROJECT.md realization-file references.** PROJECT.md cites `docs/realizations/04-existing-data-comes-first.md` and `docs/realizations/06-what-broke.md`; the actual filesystem has `04-friends-are-a-pre-pilot.md` and `05-what-broke.md`. This is pre-existing tech debt on PROJECT.md, unrelated to this sub's diff and outside Sub A's scope (Sub C repartitions PROJECT.md). Named here so Sub C's reviewer doesn't miss it.

## Verdict

**Verdict:** APPROVED

**Round:** 1
**Fixed this round:** n/a (no prior round)
**Branch CI state:** vacuous (no CI configured in repo; rule 3.10 §3.10 above)
**Search-space closure:** No remaining D, C, B, or A findings in the four ACs Sub A owns (1, 2, 4, 10-initial), no remaining findings in §2.0.0 contract integrity, no remaining findings in §2.1 diff/context, no architecture findings (skill N/A), no honest-claim findings (3.13 sub-checks all clean), no Sub D preview violations. The wave-mode γ scaffold pattern (§3.11b) is a non-binding skill-patch observation, not a finding.

**Merge instruction:** `git merge --no-ff cycle/12` into `main`, with `Closes #12` in the merge commit message. Push to `origin main`. Delete `origin/cycle/12` after merge per `release/SKILL.md` §2.6a (mechanical cleanup). β does **not** tag, version-bump, write CHANGELOG release notes, or move the cycle directory — this is a sub of a multi-sub wave; the cycle directory remains under `.cdd/unreleased/12/` until Sub D closes and δ runs the disconnect at wave terminal state per `release/SKILL.md` §2.5b (docs-only disconnect — no version bump on this wave). β will write `.cdd/unreleased/12/beta-closeout.md` after merge.
