<!--
sections_planned: [Verdict, Contract Integrity, Issue Contract, Diff Context, Architecture, Findings, CI Status, Artifact Completeness]
sections_completed: [Verdict, Contract Integrity, Issue Contract, Diff Context, Architecture, Findings, CI Status, Artifact Completeness]
-->

# beta-review — cph#14 (Sub C — TSC targets + measure-coherence.sh + CHANGELOG baseline + PROJECT.md repartition)

## Round 1

**Verdict:** APPROVED

**Round:** 1
**Review SHA:** `b4a5569` (cycle/14 HEAD)
**Base SHA:** `f13164d` (`origin/main`, re-fetched synchronously at β intake)
**Implementation SHA:** `d77aac4` (last α implementation commit before the self-coherence sequence)
**Branch CI state:** n/a — no CI configured (`ls .github/workflows/` returns "No such file or directory")
**Merge instruction:** `git merge --no-ff origin/cycle/14` into `main` with `Closes #14` in the merge commit.
**Findings:** zero (no D / C / B / A).

**Search-space closure (rule 3.7):** No remaining blocker found across AC5 / AC6 / AC7 / AC-PROJECT, the wave-manifest forward-reference contract, the empirical-overclaim sweep, the `.tsc/**` exclusion invariant, or the diff-context audit. APPROVED is unconditional per rule 3.4a.

## §2.0.0 Contract Integrity

| Check | Result | Notes |
|---|---|---|
| Status truth preserved | yes | REVISE empirical posture preserved verbatim across CHANGELOG.md (§Empirical state) and PROJECT.md (§Current empirical decision); both cite `reports/field-report-01-existing-data-zeroth-pilot.md` by name; the literal phrase `not validated; it is also not refuted` is used consistently. |
| Canonical sources/paths verified | yes | All `targets/registry.tsc` manifest paths resolve (`targets/{hypothesis,method,evidence,repo}.tsc` all `EXISTS`); all 33 glob entries across the four per-target manifests resolve to ≥1 match each on the merge tree. |
| Scope/non-goals consistent | yes | Diff touches exactly the eight files the issue scopes (8 file touches per AC; `.gitignore` adds the `.tsc/` exclusion the issue mandates implicitly via "exclude generated output"). No Sub A / Sub B file modified. No `requirements.txt` touch. |
| Constraint strata consistent | yes | Wave-manifest standing permissions honored: no Python install, no `requirements.txt` modification, mechanical-mode `coh` best-effort (script's missing-tool branch exercised and verified). |
| Exceptions field-specific/reasoned | yes | The `coh`-unavailable path is explicitly named in CHANGELOG.md, in the script's install-instruction block, and in PROJECT.md's §Last coherence measurement — three surfaces in agreement, each with its own framing (ledger / runtime / status). |
| Path resolution base explicit | yes | Per-target manifest glob resolution measured from repo root; `scripts/measure-coherence.sh` requires `REGISTRY=targets/registry.tsc` (line 18) and exits 2 with explicit guidance if run from elsewhere. |
| Proof shape adequate | yes | Every AC has positive + negative oracle named in `self-coherence.md §ACs`; verified independently by β: TOML parse (5/5), glob resolution (all entries), `bash -n` (clean), missing-`coh` run (exit 127, install-instruction block printed), `grep`-based intra-doc invariants. |
| Cross-surface projections updated | yes | README.md (Sub A's surface) already names `targets/`, `CHANGELOG.md`, and `PROJECT.md` rows in the source-of-truth table; this sub makes those rows resolve to real artifacts. Reverse check on merge tree: README's "What changed over time? \| `CHANGELOG.md`" row now resolves. |
| No witness theater / false closure | yes | CHANGELOG carries `pending — coh unavailable` honestly across four occurrences (ledger row, §Coherence delta C_Σ bullet, §Known limits, §Next gate); no false-baseline numeric is fabricated. |
| PR body matches branch files | n/a | No PR; β merges directly per wave-manifest standing-permission "Push merges to main: yes". The cycle-issue body (cph#14) lists exactly the eight file touches in the diff plus the implicit `.gitignore` addition. |
| γ artifacts present (gamma-scaffold.md) | exempt — note in §Artifact Completeness | Per cph-repo-canonical γ-at-wave model; rule 3.11b exemption discussed in §Artifact Completeness below. |

## §2.0 Issue Contract

### AC Coverage

| # | AC | In diff? | Status | Notes |
|---|----|----------|--------|-------|
| AC5 | TSC targets exist | yes | met | Registry: `format = "tsc-target-registry/0.1"`, `default_target = "repo"`, four `[target.*]` blocks. All four manifest paths resolve. Per-target `sources` arrays: hypothesis (8 paths — all eight forward-reference paths from the wave manifest, in pinned order); method (6 globs — 7+4+5+6+1+1 matches); evidence (3 globs — 3+1+2 matches); repo (16 globs — all resolve including `CHANGELOG.md` and `scripts/**/*.sh` from this same diff). `.tsc/**` does not appear in any `sources` array — only in comment-block exclusions in `registry.tsc` and `repo.tsc`. |
| AC6 | Coherence measurement can run | yes | met | `scripts/measure-coherence.sh`: shebang `#!/usr/bin/env bash` line 1; `set -euo pipefail` line 16; mode `-rwxr-xr-x` (executable). `bash -n` clean. Missing-`coh` branch: `./scripts/measure-coherence.sh` in dispatch env (no `coh`) exits 127 with install-instruction block to stderr; mechanical-mode-only invocation (no LLM credentials referenced anywhere). Loop over `TARGETS=(repo hypothesis method evidence)` produces exactly four `coh --mode mechanical --target $target` invocations against `targets/registry.tsc`. |
| AC7 | Changelog records CDR baseline | yes | met | `CHANGELOG.md` ledger header carries all nine required columns. Baseline row: `0.1.0-cdr \| 2026-05-18 \| REVISE \| pending \| pending \| pending \| pending — coh unavailable \| not measured \| ...`. §Coherence delta names α/β/γ/C_Σ explicitly with `pending — coh unavailable` and qualitative observations. §Known limits opens with the verbatim string `Coherence score is not empirical validation` (line 45). §Next gate names R0 closure (Sub D conformance sweep) and the conditions for the first numeric C_Σ baseline. No empirical overclaim. |
| AC-PROJECT | PROJECT.md repartition (supports AC10) | yes | met | `PROJECT.md` has exactly seven `## ` headings matching the AC invariant: Current stage, Current empirical decision, Current blocker, Next action, Active branch / issue, Last field report, Last coherence measurement. No R0–R6 phase blocks (roadmap content removed). No ledger table (CHANGELOG content not duplicated). Points to `ROADMAP.md` and `CHANGELOG.md` for delegated concerns. Pre-diff content (Implementation Status, Realization Sequence, Implementation Timeline, Friend Pre-Pilot Overview, Risk Management, Source-of-truth table, Success Criteria, Decision Points) removed cleanly. |

### Named Doc Updates

| Doc / File | In diff? | Status | Notes |
|------------|----------|--------|-------|
| `targets/registry.tsc` | yes (new) | met | TOML parses; `default_target = "repo"`; four `[target.*]` blocks; each manifest path resolves. |
| `targets/hypothesis.tsc` | yes (new) | met | Eight pinned paths from wave-manifest forward-reference contract, all resolve. |
| `targets/method.tsc` | yes (new) | met | Six globs; all resolve. |
| `targets/evidence.tsc` | yes (new) | met | Three globs; all resolve. |
| `targets/repo.tsc` | yes (new) | met | Sixteen globs aggregating all major canonical surfaces; all resolve on merge tree. |
| `scripts/measure-coherence.sh` | yes (new) | met | Executable; `bash -n` clean; missing-`coh` exit 127 with install instructions verified by direct run. |
| `CHANGELOG.md` | yes (new) | met | Ledger header + baseline row + 0.1.0-cdr entry with all required fields. |
| `PROJECT.md` | yes (modified) | met | Repartitioned to seven AC-PROJECT fields; pre-diff roadmap/realization/risk/source-of-truth content removed; points to ROADMAP.md and CHANGELOG.md. |
| `.gitignore` | yes (modified) | met (implicit) | `.tsc/` added at line 27. Keeps mechanical-mode output out of the index; consistent with `.tsc/**`-excluded-from-canonical-sources invariant. |

### CDD Artifact Contract

| Artifact | Required? | Present? | Notes |
|----------|-----------|----------|-------|
| `.cdd/unreleased/14/self-coherence.md` | yes (α) | yes | Section manifest `[Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness]` all completed; CDD-Trace covers steps 1–7; Review-readiness signal at `b4a5569` with all 14 pre-review gate rows satisfied or explicitly n/a. |
| `.cdd/unreleased/14/beta-review.md` | yes (β, this file) | yes | This file. |
| `.cdd/unreleased/14/gamma-scaffold.md` | per cph-repo-canonical model: n/a | n/a | See §Artifact Completeness — wave-manifest serves the γ scaffold role for this wave (γ = δ permitted per sub-issue body and wave manifest); sibling cycles 12 and 13 of this same wave merged without it. Not a 3.11b RC for cph. |

### Active Skill Consistency

| Skill | Required by | Loaded by α | Applied? | Notes |
|-------|-------------|---------|----------|-------|
| `CDD.md` | lifecycle | yes (§Skills Tier 1) | yes | α's CDD Trace covers steps 1–7. |
| `cdd/alpha/SKILL.md` | role contract | yes (§Skills Tier 1) | yes | Self-coherence section structure, pre-review gate (14 rows), incremental commit discipline (one section per commit) all applied. |
| `cdd/design/SKILL.md` | conditional | no (justified) | n/a | α's §Skills records: not loaded because TSC target-manifest format, four-target slicing, script shape, and AC-PROJECT field list are pinned in master cph#11 §"Required changes" items 6–9 and the wave manifest; no impact graph to design. β concurs. |
| `cdd/plan/SKILL.md` | conditional | no (justified) | n/a | α's §Skills records: not loaded because the eight file touches have only one forward reference (`targets/repo.tsc` → `CHANGELOG.md`, resolved in same diff); sequencing trivial. β concurs. |
| `cdd/issue/SKILL.md` | conditional | no (justified) | n/a | Issue body and wave manifest carry the AC contract directly. β concurs. |
| `eng/bash` (cph-local) | per issue §Skills to load | no skill tree present | applied directly | β verified: no `.cdd/skills/eng/` tree exists in cph; bash discipline is applied without a loaded skill — `#!/usr/bin/env bash`, `set -euo pipefail`, `command -v` guard, explicit exit codes (127 / 2), `bash -n` validation. β-side syntax check on merge tree is clean. |
| `eng/markdown` (cph-local) | per issue §Skills to load | no skill tree present | applied directly | Same — no skill tree; Markdown discipline (tables, intra-doc links, section structure) is consistent with merged Sub A / Sub B surfaces. β-side cross-reference resolution is clean. |

## §2.1 Diff Context

**Diff stat against `origin/main` at review SHA `b4a5569`:**

```
 .cdd/unreleased/14/self-coherence.md | 325 +++++++++++++++++++++++++++++++++++
 .gitignore                           |   5 +
 CHANGELOG.md                         |  54 ++++++
 PROJECT.md                           | 172 +++---------------
 scripts/measure-coherence.sh         |  65 +++++++
 targets/evidence.tsc                 |  24 +++
 targets/hypothesis.tsc               |  26 +++
 targets/method.tsc                   |  24 +++
 targets/registry.tsc                 |  28 +++
 targets/repo.tsc                     |  35 ++++
 10 files changed, 611 insertions(+), 147 deletions(-)
```

**Structural closure:** every file in the diff stat is owned by exactly one AC (or is the α-process artifact). No orphan files. No leftover diff.

**Multi-format parity (rule polyglot re-audit):**

- TOML (5 files): all five parse via Python `tomllib.load`. Schema is consistent across the four per-target manifests (`format`, `name`, `description`, `sources`); registry uses the distinct `tsc-target-registry/0.1` format string per master cph#11 §"Required changes" item 6 example. β-verified independently on the merge tree.
- Bash (1 file): `bash -n` clean. `command -v coh` guard runs first (line 22). `set -euo pipefail` at the top (line 16). `mkdir -p .tsc` (line 55) creates the output directory after both guards pass. Loop over `TARGETS=()` produces exactly four invocations. β-verified by direct run in dispatch env (exit 127, install-instruction block printed) and by reading the script line-by-line.
- Markdown (3 files modified or added — CHANGELOG.md, PROJECT.md, self-coherence.md): tables render; intra-doc cross-references resolve; `grep -nF "pending — coh unavailable" CHANGELOG.md` returns four occurrences, all consistent. PROJECT.md heading audit returns exactly the seven AC-PROJECT fields.
- gitignore (1 file modified): `.tsc/` appended at line 27; consistent with the directory-prefix pattern used by other entries.

**Snapshot consistency (rule 3.13a — honest-claim reproducibility):**

- The `pending — coh unavailable` claim in CHANGELOG.md is reproducible: `command -v coh` in the dispatch env returns no path; `./scripts/measure-coherence.sh` exits 127. β re-verified at review time.
- The "Pearson r̄ 0.93–0.96" number cited in PROJECT.md §Current empirical decision is sourced from `reports/field-report-01-existing-data-zeroth-pilot.md` (pre-existing on `origin/main`; not modified by this diff). β spot-checked: the field report carries the matching language for the OpenCap-vs-reference comparison verdict; the citation chain holds.
- The "(60 walking trials × 10 subjects, SHA-256 `3290d485...`)" number in PROJECT.md §Last field report is sourced from the same field report; β spot-checked: provenance chain intact.
- No new measurements introduced by this diff (it's a repo-identity refactor); reproducibility is reduced to citation chains, all of which hold.

**Stale paths:** none. β-verified by full `find`-style resolution across the diff (every path mentioned in CHANGELOG.md / PROJECT.md / self-coherence.md / targets/*.tsc resolves on the merge tree).

**Authority conflicts (rule 3 keep-stale-references-as-findings):**

- CHANGELOG.md `## 0.1.0-cdr — CDR refactor` §Empirical state and PROJECT.md §Current empirical decision: both REVISE, both cite field-report-01, both use the literal `not validated; it is also not refuted`. No drift.
- README.md (Sub A merged surface) source-of-truth table row "What is current operational status? | `PROJECT.md`": PROJECT.md now actually carries that and only that. No drift.
- README.md row "What changed over time? | `CHANGELOG.md`": CHANGELOG.md now exists with the ledger header + baseline entry. No drift.
- README.md row "What TSC targets are measured? | `targets/`": `targets/` now exists with five manifests. No drift.

## §2.2 Architecture

| # | Question | Answer | Evidence |
|---|----|----|----|
| A | Does the diff respect module boundaries? | yes | Eight file touches across `targets/` (new), `scripts/` (new entry alongside existing `.py` scripts), repo-root status surfaces (CHANGELOG.md new, PROJECT.md modified), and `.gitignore` (modified). No cross-cutting module change. |
| B | Are new dependencies justified? | n/a | No new dependencies. Diff is TOML + shell + Markdown + gitignore only. `requirements.txt` not touched. |
| C | Are public surfaces shaped right? | yes | Five TSC manifests are the public surfaces this sub introduces; schema is consistent and aligned with the master-issue example. Script is a single entrypoint exposing one verb (measure-coherence) with mechanical-mode-only semantics. CHANGELOG.md and PROJECT.md follow the wave's source-of-truth partitioning. |
| D | Are error / failure paths handled? | yes | Script: explicit missing-`coh` branch (exit 127 + install instructions) and missing-registry branch (exit 2 + cwd guidance). Both paths verified by reading; missing-`coh` branch verified by direct run. Mechanical-mode invocation does not require credentials, so no auth-failure path applies. |
| E | Are concurrency / state assumptions sound? | n/a | No concurrent state. Script is a single-process sequential loop over four targets. TOML manifests are pure data. |
| F | Are tests / proofs adequate for the change-shape? | yes (structural-only justified) | α §CDD-Trace step 4 records: no automated tests apply; structural validation via `tomllib.load`, `bash -n`, glob resolution, and a one-shot run of the missing-`coh` branch. β-replicated all four checks independently. The present-`coh` branch is named as known debt (§Debt item 2 + 3); the missing-CLI is an environment concern, not a diff concern. |
| G | Are operational projections (dashboards, status surfaces, runbooks) updated? | yes | PROJECT.md (live status) is repartitioned and points at CHANGELOG.md (history) and ROADMAP.md (gates). The wave-manifest forward-reference contract is satisfied without back-edits to Sub A or Sub B. |

## §2.2a Honest-Claim Verification (rule 3.13)

**(a) Reproducibility (rule 3.13a):** β-verified every measurement claim in the diff:

- "`coh` is not installed" → β re-ran `command -v coh` → no path. ✓
- "exit code 127, install-instruction block printed" → β re-ran `./scripts/measure-coherence.sh` → exit 127, install block printed to stderr. ✓
- "all five `.tsc` files parse as TOML" → β re-ran `tomllib.load` on each — no errors. ✓
- "every glob entry resolves to ≥1 match" → β re-resolved every glob in each manifest — all 33 entries return ≥1 match. ✓
- "`bash -n` clean" → β re-ran. ✓
- "PROJECT.md contains exactly seven `## ` headings matching the AC invariant" → β-verified by `grep -E "^## " PROJECT.md`. ✓
- "Pearson r̄ 0.93–0.96 / 60 trials × 10 subjects" → traces to `reports/field-report-01-existing-data-zeroth-pilot.md` (pre-existing canonical source). ✓

**(b) Source-of-truth alignment (rule 3.13b):** every term used in the new docs traces to its canonical owner:

- `Coherence Path Hypothesis` → `docs/concepts/coherence-path-hypothesis.md` (Sub A, merged) — owned and referenced consistently in CHANGELOG.md §0.1.0-cdr and PROJECT.md.
- `support path` → `docs/concepts/support-path.md` (pre-existing, named in Sub A merged surfaces) — operational-term reference in CHANGELOG.md §Known limits.
- `C_Σ` / `coherence ledger` → `CDR.md` (Sub A) §"C_Σ in this repo" — CHANGELOG.md preamble cites it; PROJECT.md doesn't redefine.
- `REVISE / GO / STOP` → `CDR.md` (Sub A) and `ROADMAP.md` (Sub B) — referenced in PROJECT.md without redefinition.
- `field-report-01` → `reports/field-report-01-existing-data-zeroth-pilot.md` (pre-existing) — cited consistently by full filename.

No drift between informal and normative usage in any of the three doc surfaces.

**(c) Wiring claims (rule 3.13c):** every wiring claim grep-verified:

- "`scripts/measure-coherence.sh` reads `targets/registry.tsc`" → script line 18 `REGISTRY="targets/registry.tsc"` + line 61 `--registry "$REGISTRY"`. ✓
- "Script loops over four targets (`repo`, `hypothesis`, `method`, `evidence`)" → script line 20 `TARGETS=(repo hypothesis method evidence)` + line 57 `for target in "${TARGETS[@]}"`. The four names exactly match the four `[target.*]` blocks in `targets/registry.tsc`. ✓
- "`targets/hypothesis.tsc` references the eight forward-reference paths from the wave manifest" → β re-parsed and listed the `sources` array: 8 entries in pinned order, all resolve. ✓
- "`PROJECT.md` points to `ROADMAP.md` and `CHANGELOG.md`" → β-verified `grep -nE "ROADMAP\.md|CHANGELOG\.md" PROJECT.md` returns 5 matches across §Current stage, §Next action, §Last coherence measurement, and the preamble. ✓

**(d) Gap claims (rule 3.13d):** every "X does not exist" claim grep-verified:

- "No `targets/` on `origin/main`" → β-verified `git ls-tree --name-only origin/main targets/ 2>&1` is empty / does not list a `targets` entry — confirmed via diff-stat (`targets/*.tsc` all marked `A` for added). ✓
- "No `scripts/measure-coherence.sh` on `origin/main`" → β-verified same way; the file is `A` in the diff stat. ✓
- "No `CHANGELOG.md` on `origin/main`" → β-verified — `A` in the diff stat. ✓
- "`PROJECT.md` doubled as a roadmap (R1 status + implementation timeline + ...)" → β-verified by reading `git show origin/main:PROJECT.md | head -40` against the current `PROJECT.md`; the pre-diff file did carry the named sections that the new file has removed. ✓

## §2.3 Findings

| # | Finding | Evidence | Severity | Type |
|---|---------|----------|----------|------|

(no findings — table is empty)

## §2.4 CI Status (rule 3.10)

**No CI configured for this repo.** β-verified by `ls .github/workflows/` returning "No such file or directory". The wave-manifest standing permissions explicitly contemplate this for cph: "best-effort" `coh` run; structural validation performed locally via β's toolchain (Python `tomllib`, `bash -n`, glob resolution). Rule 3.10's "CI-green gate" is satisfied vacuously — no required workflow exists for there to be a missing green run. The wave-manifest also pins `Push merges to main: yes`. β does not block on rule 3.10.

## §2.5 Artifact Completeness (rule 3.11b)

**γ-scaffold status:** `.cdd/unreleased/14/gamma-scaffold.md` is **not present** on `origin/cycle/14`. Per rule 3.11b strict reading, this would be a D-severity RC. However β reads 3.11b's exemption discoverability against the cph-canonical model:

1. **Sub-issue body exemption signal.** Issue cph#14's body closes with the line `α ≠ β as identities. γ = δ permitted.` This invokes the `cdd/operator/SKILL.md` §5.2 standing rule that at this scale γ and δ are a single role-actor and the γ scaffolding consolidates to the wave-manifest level rather than per-cycle. The wave-manifest dispatch comment on master cph#11 (comment id `IC_kwDOSb05z88AAAABCus9BQ`) names this explicitly: "δ-as-agent (γ=δ permitted at this scale per `cdd/operator/SKILL.md` §5.2)".

2. **Repo-canonical pattern.** β confirmed by inspection that sibling cycles of this same wave — `cph#12` (Sub A) and `cph#13` (Sub B), both merged — carry `self-coherence.md`, `beta-review.md`, `beta-closeout.md`, and `alpha-closeout.md` but **no** `gamma-scaffold.md`. Older closed cycles in `.cdd/unreleased/{5,6,7,8}/` (closeable cycles still in the unreleased dir per cph release cadence) likewise carry no `gamma-scaffold.md` — they carry `gamma-closeout.md` from the PRA phase only. The wave-manifest at `.cdd/waves/cdr-refactor-2026-05-18/manifest.md` (commits `317779c`, `06341a4` on `delta/wave-cdr-refactor-2026-05-18`) is the γ artifact for this wave; it carries the five-factor heuristic outcome, the file-disjointness check, the pinned forward-reference contract, the standing permissions, the timeout budgets, and the resumption / failure handling — i.e. every coordination concern a per-cycle `gamma-scaffold.md` would carry.

3. **γ artifact resolution.** β treats the wave-manifest as the γ artifact of record for cph#14 and records its location for audit: `.cdd/waves/cdr-refactor-2026-05-18/manifest.md`. This is not a 3.11b exemption claim *against* a missing artifact — it is an artifact-path resolution under cph's wave-dispatched model.

**Verdict on 3.11b:** satisfied. The γ coordination contract is present; the canonical location is the wave manifest, not a per-cycle scaffold file. β notes this read so a future reviewer of cph cycles can confirm the precedent without re-deriving it.

## §2.6 Notes

- α's §Self-check polyglot re-audit grep-count correction at `1dde070` (`6 → 4` occurrences of `pending — coh unavailable` in CHANGELOG.md) was an internal-doc self-correction by α before signaling review-readiness. β re-counted independently: `grep -nF "pending — coh unavailable" CHANGELOG.md` returns 4 lines (13, 27, 46, 52). α's corrected count is right.
- α used `Alpha` as `user.name` and `alpha@cph.cdd.cnos` as `user.email` across all 12 cycle commits — canonical pattern per `operator/SKILL.md` §Git identity; β-side identity is `Beta` / `beta@cph.cdd.cnos`; α ≠ β as the dispatch prompt requires.
- The pre-merge gate non-destructive merge test (β SKILL.md row 3) ran clean: automatic merge resolved without conflict, zero unmerged paths, all five `.tsc` files re-parse on the merge tree, `scripts/measure-coherence.sh` re-passes `bash -n` on the merge tree.

---

**Closing:** APPROVED. β proceeds to `git merge --no-ff origin/cycle/14` into `main` with `Closes #14`, then writes `.cdd/unreleased/14/beta-closeout.md`. Tag / release / branch deletion remain δ's release-boundary concerns; γ owns the PRA.
