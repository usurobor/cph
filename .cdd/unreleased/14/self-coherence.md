<!--
sections_planned: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness]
sections_completed: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace]
-->

# self-coherence — cph#14 (Sub C — TSC targets + measure-coherence.sh + CHANGELOG baseline + PROJECT.md repartition)

## Gap

**Issue:** [usurobor/cph#14](https://github.com/usurobor/cph/issues/14) — Sub C of master [cph#11](https://github.com/usurobor/cph/issues/11). Wave [`cdr-refactor-2026-05-18`](../../waves/cdr-refactor-2026-05-18/manifest.md).

**Version / mode:** MCA-eligible (the TSC target-manifest registry format string `tsc-target-registry/0.1` is pinned in master cph#11 §"Required changes" item 6; `scripts/measure-coherence.sh` shape is fully specified in item 7; PROJECT.md repartition is mechanical given Sub A's and Sub B's merged surfaces).

**What was missing on `origin/main`:**

- No `targets/` directory. No TSC target manifests. Without them, `coh` has nothing to measure and CDR.md's required cadence is non-runnable.
- No `scripts/measure-coherence.sh`. The C_Σ cadence CDR.md prescribes has no entrypoint.
- No `CHANGELOG.md`. The research coherence ledger has no baseline. Without it, future waves have nothing to delta from.
- `PROJECT.md` doubled as a roadmap (R1 status + implementation timeline + realizations narrative + friend pre-pilot overview + risk management + source-of-truth table) and a status surface. With `ROADMAP.md` now owning gates (Sub B) and the source-of-truth table now owned by `README.md` (Sub A), `PROJECT.md` carrying that content is duplication.

**What this sub adds:**

- `targets/registry.tsc` + `targets/{hypothesis,method,evidence,repo}.tsc` — TSC target manifests with `.tsc/**` excluded from canonical sources.
- `scripts/measure-coherence.sh` — executable, mechanical-mode entrypoint with clear missing-`coh` failure.
- `CHANGELOG.md` — baseline 0.1.0-cdr entry; α/β/γ/C_Σ = `pending — coh unavailable`; explicit "Coherence score is not empirical validation".
- `PROJECT.md` repartitioned to current-operational-status only (seven fields per AC-PROJECT invariant).
- `.gitignore` — `.tsc/` excluded so mechanical-mode output does not pollute the index.

**Boundary:** this sub does not touch the empirical posture (REVISE, per the latest merged field report), does not run clustering, does not modify `requirements.txt`, and does not edit Sub A / Sub B surfaces (`README.md`, `CDR.md`, hypothesis doc, seven-families article, `ROADMAP.md`).

## Skills

**Tier 1 — canonical lifecycle and α role:**

- `CDD.md` — lifecycle, role contract, artifact-location matrix.
- `cdd/alpha/SKILL.md` — α algorithm (load order, dispatch intake, artifact order, peer enumeration, harness audit, self-coherence, pre-review gate, request review, close-out).

α lifecycle sub-skills were *not* additionally loaded for this cycle:

- `cdd/design/SKILL.md` — not loaded; **design not required**. The TSC target-manifest format (`tsc-target-registry/0.1`), the four-target slicing (hypothesis / method / evidence / repo), and the `measure-coherence.sh` shape are all specified in master cph#11 §"Required changes" items 6–7. PROJECT.md repartition is mechanical given the AC-PROJECT invariant. No impact graph to design.
- `cdd/plan/SKILL.md` — not loaded; **plan not required**. The eight file touches are independent of each other except for one forward reference (`targets/repo.tsc` → `CHANGELOG.md`, resolved by introducing `CHANGELOG.md` in the same diff). Sequencing was trivial.
- `cdd/issue/SKILL.md` — not loaded; the issue body is the AC contract and the wave manifest pins the forward-reference paths.

**Tier 2 — always-applicable engineering skills:**

- No cph-local `eng/*` skill tree exists in this repo (`ls .cdd` shows `iterations/` and `unreleased/` only; no `skills/eng/`). Tier 2 in this dispatch reduces to the implicit Tier-2 conventions from the cph codebase itself (set -euo pipefail in shell, Python module style for sibling scripts, Markdown table-and-section style from Sub A/B authoring).

**Tier 3 — issue-specific:**

- Bash discipline applied directly (no cph-local `eng/bash` skill present): `#!/usr/bin/env bash`, `set -euo pipefail`, `command -v` for the missing-tool guard, explicit exit codes (127 for missing executable, 2 for missing registry file), `bash -n` syntax check before commit.
- Markdown discipline applied directly (no cph-local `eng/markdown` skill present): table-and-section style consistent with the merged Sub A / Sub B surfaces; one-line ledger row + multi-section detail per CHANGELOG.md baseline entry; intra-doc forward references via `[text](path)`.

**Generation constraints loaded from the wave manifest (binding):**

1. `.tsc/**` must not appear as a canonical source in any target — applied in all five `targets/*.tsc` files; comment preambles in `registry.tsc` and `repo.tsc` make the exclusion explicit; `.gitignore` carries the same exclusion to keep mechanical-mode output out of the index.
2. `CHANGELOG.md` C_Σ cell carries `pending — coh unavailable` if mechanical-mode cannot run — applied; `coh` is not installed in the dispatch environment, the ledger row carries that literal string, and §Coherence delta says `pending — coh unavailable` per axis.
3. "Coherence score is not empirical validation" must appear under Known limits in the baseline entry — applied verbatim as the first §Known limits bullet of the 0.1.0-cdr entry.
4. `PROJECT.md` must not become a second roadmap surface — applied; the seven fields named in AC-PROJECT are the only sections in the new `PROJECT.md`; roadmap content has been removed; `PROJECT.md` points to `ROADMAP.md` and `CHANGELOG.md` rather than restating their content.
5. No empirical overclaim — applied; CHANGELOG and PROJECT preserve REVISE; no validation language anywhere in the diff.

**Forward-reference contract from the wave manifest:**

- `targets/hypothesis.tsc` must reference exactly: `README.md`, `CDR.md`, `ROADMAP.md`, `docs/concepts/coherence-path-hypothesis.md`, `docs/concepts/support-path.md`, `docs/concepts/gait-cycle-as-unit.md` (only if present), `docs/concepts/failure-conditions.md` (only if present), and Sub A's chosen seven-gait-families path. Verified: all eight files present on disk (`ls docs/concepts/` returns the four concept docs; `ls docs/articles/seven-ways-people-walk.md` resolves); the `sources` array in `targets/hypothesis.tsc` lists exactly these eight paths in this order.
- `PROJECT.md` must point to `ROADMAP.md` and `CHANGELOG.md` but must not duplicate them — verified by reading the rewritten `PROJECT.md` end-to-end.

## ACs

### AC5 — TSC targets exist

**Status:** met.

**Evidence:**

- `targets/registry.tsc` (commit `39df3d5`) — `format = "tsc-target-registry/0.1"`, `default_target = "repo"`, `[target.hypothesis|method|evidence|repo]` blocks each pointing to a `.tsc` manifest. Verified parses as TOML via `python3 -c "import tomllib; tomllib.load(open('targets/registry.tsc','rb'))"` → keys `['format', 'default_target', 'target']`.
- `targets/hypothesis.tsc` — eight forward-reference paths verified present on disk: `README.md`, `CDR.md`, `ROADMAP.md`, `docs/concepts/coherence-path-hypothesis.md`, `docs/concepts/support-path.md`, `docs/concepts/gait-cycle-as-unit.md`, `docs/concepts/failure-conditions.md`, `docs/articles/seven-ways-people-walk.md`. Glob resolution: every entry returns ≥1 match.
- `targets/method.tsc` — six glob entries; `protocols/**/*.md` matches 7 files, `instruments/**/*.md` 4, `analysis/**/*.md` 5, `scripts/**/*.py` 6, `notebooks/README.md` 1, `notebooks/existing-data-processing.ipynb` 1.
- `targets/evidence.tsc` — three glob entries; `reports/**/*.md` matches 3, `analysis/feature-summary-zeroth-pilot.md` 1, `data/external/**/*.md` 2.
- `targets/repo.tsc` — sixteen glob entries; every entry resolves except `CHANGELOG.md` (introduced in the same diff, commit `1de1ac5`) and `scripts/**/*.sh` (matches `scripts/measure-coherence.sh` from commit `f868caf`). After the full diff lands, both resolve.

**Oracle (positive):** `targets/hypothesis.tsc` `sources` array includes the eight paths the AC names; verified by `grep -c` on the file (8 entries between the array brackets, exactly).

**Oracle (negative):** `.tsc/**` does *not* appear as a canonical source in any target. Verified by `grep -n "\.tsc/" targets/*.tsc` — two matches total, both inside comment blocks describing the *exclusion* (`registry.tsc:12`, `repo.tsc:11`); zero matches inside any `sources` array.

**Surface:** `targets/registry.tsc`, `targets/hypothesis.tsc`, `targets/method.tsc`, `targets/evidence.tsc`, `targets/repo.tsc`.

### AC6 — Coherence measurement can run

**Status:** met.

**Evidence:**

- `scripts/measure-coherence.sh` (commit `f868caf`) exists with shebang `#!/usr/bin/env bash` and `set -euo pipefail` on the first two non-comment lines.
- File mode is `-rwxr-xr-x` (executable). Verified by `ls -la scripts/measure-coherence.sh`.
- `bash -n scripts/measure-coherence.sh` → no syntax errors.
- The script reads `TARGETS=(repo hypothesis method evidence)` and invokes `coh --mode mechanical --target $target --registry targets/registry.tsc --output .tsc/` for each (four invocations).
- Missing-`coh` path verified by running `./scripts/measure-coherence.sh` in the dispatch environment (`coh` is not installed): exit code 127; install-instruction block printed to stderr naming `pip install tsc-cli` and the source-install path; no silent skip.

**Oracle (positive):** four `coh` invocations driven by a single loop over `TARGETS`, one per target name. Verified by reading the script.

**Oracle (negative):** the script does not source LLM credentials. Verified by reading the script — no references to `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` / equivalents. Mechanical mode is the only mode invoked (`--mode mechanical` on every call).

**Surface:** `scripts/measure-coherence.sh`.

### AC7 — Changelog records CDR baseline

**Status:** met.

**Evidence:**

- `CHANGELOG.md` (commit `1de1ac5`) exists at repo root.
- The ledger header table has the required columns: `Entry | Date | Empirical state | α | β | γ | C_Σ | Bottleneck | Decision`.
- The baseline row (`0.1.0-cdr | 2026-05-18 | REVISE | pending | pending | pending | pending — coh unavailable | not measured | refactor merged; baseline measurement deferred until coh is installed`) is the first and only row.
- The `## 0.1.0-cdr — CDR refactor` heading owns Date, Level, Empirical state, Decision, Coherence delta (α / β / γ / C_Σ / bottleneck), Changed, Known limits, Next gate.
- The C_Σ cell carries `pending — coh unavailable` per the AC7 oracle: `coh` is not installed; the script exists; this is consistent with `scripts/measure-coherence.sh`'s `exit 127` behavior.

**Oracle (positive):** the literal string `Coherence score is not empirical validation` appears under §Known limits. Verified by `grep "Coherence score is not empirical validation" CHANGELOG.md` → one match in the first §Known limits bullet.

**Oracle (negative):** no language claiming the Coherence Path Hypothesis is validated. Verified by inspection — the §Empirical state line says "not validated; it is also not refuted"; §Known limits names "no new empirical claims"; §Coherence delta carries qualitative observations only.

**Surface:** `CHANGELOG.md`.

### AC-PROJECT — PROJECT.md repartition (supports AC10)

**Status:** met.

**Evidence:**

- `PROJECT.md` (commit `d77aac4`) now contains only the seven fields named in the AC invariant: Current stage / Current empirical decision / Current blocker / Next action / Active branch or issue / Last field report / Last coherence measurement. Verified by reading the rewritten file end-to-end.
- The pre-diff `PROJECT.md` content removed: §Implementation Status (Documentation Complete + Next Phase), §Current Realization Sequence (six realizations), §Implementation Timeline, §Friend Pre-Pilot Overview, §Risk Management, the prior §Source of truth table, §Success Criteria, §Decision Points.
- PROJECT.md points to `ROADMAP.md` (current stage / next action / R5 / R6 references) and `CHANGELOG.md` (last coherence measurement), but never restates their content.

**Oracle (positive):** the seven AC-PROJECT fields are present as named sections. Verified by `grep -E "^## " PROJECT.md` → seven `##` headings matching the AC invariant.

**Oracle (negative):** PROJECT.md does not duplicate `ROADMAP.md` phase content (no R0/R1/R2/R3/R4/R5/R6 phase blocks); does not duplicate `CHANGELOG.md` ledger content (no ledger table). Verified by inspection.

**Surface:** `PROJECT.md`.

## Self-check

### Did α push ambiguity onto β?

No. Each AC is mapped to a specific oracle and an explicit evidence chain — file path, commit SHA, content claim, verification method. Where the oracle is a glob resolution or a `grep` invariant, the exact resolution / match count is recorded in §ACs so β does not need to re-derive it.

### Is every claim backed by evidence in the diff?

Each claim, line by line:

- "`coh` is not installed in the dispatch environment" — verified by `command -v coh && coh --version 2>&1 || echo "coh-not-installed"` returning `coh-not-installed`; recorded in commit `f868caf`'s message as well.
- "exit code 127, install-instruction block printed" — verified by running `./scripts/measure-coherence.sh; echo "exit=$?"` and seeing the expected output.
- "`.tsc/**` does not appear as a canonical source in any target" — verified by `grep -n "\.tsc/" targets/*.tsc` → two matches, both in comment blocks.
- "`targets/hypothesis.tsc` includes exactly the eight forward-reference paths" — verified by reading the file and by `python3 -c "import tomllib, glob; ..."` resolution.
- "PROJECT.md contains only the seven AC-PROJECT fields" — verified by reading the file end-to-end; `grep -E "^## " PROJECT.md` returns the seven `##` headings.
- "Empirical posture preserved" — verified by `grep -i "validated" CHANGELOG.md PROJECT.md` returning no validation claim; the only matches are negations ("not validated", "not be allowed to become a second roadmap surface", "not measured").

### Peer enumeration — done?

The peer family for this diff has three classes:

1. **`targets/*.tsc` file family.** The five target manifests (registry, hypothesis, method, evidence, repo) are peers of each other under the same schema. Enumerated: all five exist; all five parse as TOML; all five exclude `.tsc/**` from canonical sources; `registry.tsc` references each of the other four by exact path; each per-target manifest carries `format = "tsc-target/0.1"`, `name`, `description`, `sources` keys consistently.
2. **Source-of-truth surfaces.** The wave touches four source-of-truth files at repo root: `README.md`, `ROADMAP.md`, `CHANGELOG.md`, `PROJECT.md`. README.md (Sub A) owns the source-of-truth table; ROADMAP.md (Sub B) owns gates; CHANGELOG.md (this sub) owns the ledger; PROJECT.md (this sub) owns live status. Enumerated: each file points to the others; no two restate each other's owned facts. Cross-checked: `README.md`'s source-of-truth table row for "What changed over time? | `CHANGELOG.md`" now resolves to a real file; row for "What TSC targets are measured? | `targets/`" now resolves to a real directory; row for "What is current operational status? | `PROJECT.md`" still resolves and the file now actually carries that and only that.
3. **Empirical-state language across surfaces.** README.md, PROJECT.md, ROADMAP.md, CHANGELOG.md all carry an empirical-state phrase. Enumerated: README.md says REVISE per field-report-01 (pre-existing, Sub A); ROADMAP.md says R1 REVISE (Sub B); PROJECT.md says REVISE 2026-05-17 real-data run (this sub, preserving the merged language); CHANGELOG.md says REVISE — unchanged from field-report-01 (this sub). All four agree; all four cite field-report-01 as the source. The phrase `not validated; it is also not refuted` is the canonical hypothesis-status sentence and appears in CHANGELOG.md and PROJECT.md verbatim, consistent with README.md's phrasing.

### Harness audit — done?

This sub's "harness" is the TSC measurement entrypoint. Producers / consumers of the TSC target-manifest shape:

- **Producer:** the five `targets/*.tsc` files. All produce TOML in the same registry-and-target style.
- **Consumer:** `scripts/measure-coherence.sh`. It reads `targets/registry.tsc` (named via `REGISTRY="targets/registry.tsc"`) and passes the registry to `coh` for every target named in `TARGETS=(repo hypothesis method evidence)`. Audit: the four targets named in the script exactly match the four `[target.*]` blocks in `targets/registry.tsc`.
- **Consumer (mental):** the wave manifest forward-reference contract. The eight paths the manifest names for `targets/hypothesis.tsc` exactly match the eight `sources` entries.
- **Generated output:** `.tsc/`. Excluded from `.gitignore` (commit `39df3d5`) so mechanical-mode output does not enter the index; not listed as a canonical source in any target manifest.

No non-primary-language harness drift: there is no shell fixture or CI workflow that produces TSC manifests; the registry is the only producer.

### Polyglot re-audit

The diff touches four languages: TOML (`targets/*.tsc`), Bash (`scripts/measure-coherence.sh`), Markdown (`CHANGELOG.md`, `PROJECT.md`, `self-coherence.md`), and gitignore (`.gitignore`).

- **TOML.** All five `targets/*.tsc` files parse via `python3 -c "import tomllib; tomllib.load(...)"` with no errors.
- **Bash.** `bash -n scripts/measure-coherence.sh` returns clean. Script runs in the missing-`coh` branch and exits 127 with the expected install-instruction output. `shellcheck` is not available in the dispatch environment; the script is small, uses only `command -v`, `cat <<EOF`, `mkdir -p`, and a `for` loop over a literal array, so the absence of shellcheck is low risk.
- **Markdown.** All tables and cross-references resolve. Intra-doc grep checks: `grep -c "pending — coh unavailable" CHANGELOG.md` → 6 occurrences (ledger row, §Coherence delta α/β/γ/C_Σ bullets, §Known limits, §Next gate); all six say the same thing (the literal `pending — coh unavailable`, not a variant). No drift between the ledger row's C_Σ cell and the §Coherence delta C_Σ bullet.
- **gitignore.** New entry `.tsc/` appended to the existing block style; no syntax issue.

### Did α leave β a coherent surface?

Yes. The eight files in the diff (`targets/registry.tsc`, `targets/hypothesis.tsc`, `targets/method.tsc`, `targets/evidence.tsc`, `targets/repo.tsc`, `scripts/measure-coherence.sh`, `CHANGELOG.md`, `PROJECT.md`, plus `.gitignore`) plus the `self-coherence.md` artifact give β a complete, internally consistent surface against four ACs.

## Debt

### Known debt — explicit

1. **`coh` is not installed in the dispatch environment; no numeric C_Σ baseline this wave.** The ledger row and §Coherence delta carry `pending — coh unavailable`. Loaded skill that would have prevented this: none — `coh` install is an environment / standing-permission concern (the wave manifest's `Standing permissions` explicitly says "Run `coh` (TSC CLI) in CI: best-effort"). Tracked debt: the first numeric C_Σ baseline lands the first time `coh` runs against this branch (or a successor of it); when that lands, a follow-up changelog entry replaces the `pending` row with a numeric one.

2. **`coh`'s exact `--target` / `--registry` / `--output` flag spelling is inferred from master cph#11's specification, not verified against the live `coh` CLI.** The script's invocation `coh --mode mechanical --target <name> --registry targets/registry.tsc --output .tsc/` follows the master-issue example verbatim, but the live CLI may use slightly different flag names. The script's missing-`coh` branch is verified; the present-`coh` branch is not. If the CLI's flag names have drifted, the script will fail on first real run and the fix is a one-line patch per flag.

3. **The `tsc-target/0.1` per-target manifest format string is α's choice; master cph#11 only pins the registry format string `tsc-target-registry/0.1`.** The schema (`format`, `name`, `description`, `sources` array of glob strings) is α-chosen but is consistent with the master-issue example structure for the registry. If the live `coh` CLI expects a different per-target schema (e.g. structured `[sources]` sections rather than a flat array), the per-target manifests need a one-pass schema update; the file paths inside the manifests are independent of the schema, so the path-resolution AC content is preserved across any schema fix.

4. **`shellcheck` was not run on `measure-coherence.sh`.** Not installed in the dispatch environment. `bash -n` syntax check is clean; the script is small (≈40 lines of executable shell), uses standard constructs, and was run once in the missing-`coh` branch with the expected output, so the risk of latent shellcheck-level issues is low but nonzero.

5. **`.tsc/` is gitignored, but the existing data exclusions in `.gitignore` (data/raw/, data/external/**/*.zip, etc.) are still scoped to data, not measurement output.** The `.tsc/` addition is the first non-data, non-Python-cache gitignore entry. The pattern is correct (directory prefix); a stricter `.tsc/**` glob would be equivalent given how `git` treats `.tsc/` (any file inside the directory is excluded).

### Debt not introduced

- **No empirical claim.** Verified by grep on the diff — no "validated", "proven", "confirmed", "demonstrated" language for the Coherence Path Hypothesis. The only `validated` matches in the diff are negations (`not validated`).
- **No `requirements.txt` modification.** Verified by `git diff --stat origin/main..HEAD` showing only the eight files this sub touches.
- **No Sub A / Sub B file modification.** Verified by `git diff --stat` — `README.md`, `CDR.md`, `ROADMAP.md`, the hypothesis doc, the seven-families article, and the four support-path / concept docs are unchanged.
- **No Python package install.** None attempted; the diff is shell + TOML + Markdown only.
- **No raw-data commits.** Diff stat shows no new files under `data/raw/`, `data/external/*.zip`, `data/external/*.csv`, etc.

## CDD-Trace

CDD Trace through step 7 per CDD.md §1.4 and `cdd/alpha/SKILL.md` §2.2.

### Step 1 — Receive

Dispatched as α onto `cycle/14` (Sub C of master cph#11). Wave manifest at `.cdd/waves/cdr-refactor-2026-05-18/manifest.md`. ACs declared: 5, 6, 7, AC-PROJECT. Forward-reference contract pinned in the wave manifest. Standing permissions: push to `cycle/14`, no `requirements.txt` modification, no Python install, mechanical-mode coh best-effort. Budget: α 1500s.

### Step 2 — Design (not required)

Design was not authored as a separate artifact. Justification: the AC-bearing structures — target manifest format string, four-target slicing, script shape, AC-PROJECT field list — are pinned in master cph#11 §"Required changes" items 6–9 and the wave manifest. No impact graph to design. Recorded under §Skills.

### Step 3 — Plan (not required)

Plan was not authored. The eight file touches are mutually independent except for one forward reference (`targets/repo.tsc` references `CHANGELOG.md`, resolved by introducing `CHANGELOG.md` in the same diff). Sequencing was trivial.

### Step 4 — Tests

No automated tests apply. The TSC target manifests are validated structurally (TOML parse + glob resolution); `scripts/measure-coherence.sh` is validated structurally (`bash -n`, executable bit) and behaviorally in the missing-`coh` branch (run once, exit=127, install-instruction block printed). The present-`coh` branch is not exercised — `coh` is not installed — and is named as known debt (§Debt item 2 + 3). CHANGELOG.md and PROJECT.md are documentation, not code; their AC oracles are grep / structural checks against §ACs.

### Step 5 — Code

Implementation commits (in order):

- `39df3d5` — `α #14: targets/*.tsc — TSC target manifests (AC5) + .gitignore .tsc/`
- `f868caf` — `α #14: scripts/measure-coherence.sh — mechanical TSC measurement entrypoint (AC6)`
- `1de1ac5` — `α #14: CHANGELOG.md — research coherence ledger baseline (AC7)`
- `d77aac4` — `α #14: PROJECT.md — repartition to current operational status only (AC-PROJECT, supports AC10)`

Diff stat (`git diff --stat origin/main..d77aac4` — last implementation SHA before the self-coherence sequence began): 9 files changed, 286 insertions(+), 147 deletions(-).

### Step 6 — Docs

Documentation surfaces in this diff:

- `CHANGELOG.md` — new; introduces the research coherence ledger.
- `PROJECT.md` — repartitioned; carries current-operational-status only.
- The `targets/*.tsc` comment preambles document each target's role and the `.tsc/**` exclusion.
- `scripts/measure-coherence.sh` carries an inline comment header describing entrypoint scope, missing-`coh` behavior, and mechanical-mode constraint.

**Caller-path trace.** No new modules or functions added; the diff introduces target manifests (TOML data), one shell entrypoint, two Markdown documents, and one `.gitignore` line. The entrypoint's "caller" is the operator running `scripts/measure-coherence.sh` (or a CI step invoking it) — there is no programmatic non-test caller because the script *is* the entrypoint. Its existence is referenced by `CDR.md` §"Required cadence" (Sub A merged surface, pre-existing) and by the `PROJECT.md` §"Last coherence measurement" pointer.

**Artifact enumeration vs diff.** Every file in `git diff --stat origin/main..HEAD` is mentioned in §ACs / §Self-check / §Debt / this step:

- `.gitignore` — §ACs AC5 evidence (`.tsc/` exclusion); §Skills generation-constraint 1.
- `CHANGELOG.md` — §ACs AC7.
- `PROJECT.md` — §ACs AC-PROJECT.
- `scripts/measure-coherence.sh` — §ACs AC6.
- `targets/evidence.tsc`, `targets/hypothesis.tsc`, `targets/method.tsc`, `targets/registry.tsc`, `targets/repo.tsc` — §ACs AC5.
- `.cdd/unreleased/14/self-coherence.md` — this file itself; not part of the diff stat against `origin/main..d77aac4` because it was added after the last implementation commit; will appear in the full diff stat at review-readiness time.

### Step 7 — Self-coherence

Self-coherence written incrementally per `cdd/alpha/SKILL.md` §2.5. Section commits (in order):

- `b5797af` — §Gap
- `0f3a630` — §Skills
- `13bfacc` — §ACs
- `e308685` — §Self-check
- `370aa20` — §Debt
- (this commit) — §CDD-Trace

§Review-readiness will be appended as a separate commit after this one, per §2.7.
