# Self-coherence — Sub A — cph#17 — F1 + F6

## Gap

**Issue:** usurobor/cph#17 — Sub A — F1 (broken realization ref in `ROADMAP.md`) + F6 (PROJECT.md R0 wording one transition behind state).
**Master:** usurobor/cph#16 (coherence drift sweep).
**Wave:** `.cdd/waves/coherence-drift-sweep-2026-05-18/manifest.md`.
**Branch:** `claude/review-repo-coherence-PNbjQ` (single-branch dispatch per manifest §"Branching deviation").
**Mode:** docs-only (small).

**F1 — broken realization citation in ROADMAP.md.**
`ROADMAP.md:85` (R5 §Coherence risk paragraph) cited the parenthetical realization filename `` `05-friends-are-not-validation.md` ``. That file does not exist on this branch. `ls docs/realizations/` enumerates five realizations: `01-walking-is-not-a-style.md`, `02-the-type-list-is-not-the-object.md`, `03-opencap-is-the-translation-layer.md`, `04-friends-are-a-pre-pilot.md`, `05-what-broke.md`. The realization that owns the "friends are a pre-pilot, not validation" claim is realization #04 — `04-friends-are-a-pre-pilot.md` — verified by reading the file's §Decision and §Coherence risk sections. The ROADMAP citation was off-by-one and the suffix string didn't match either of the candidate adjacent files (`04-friends-are-a-pre-pilot.md` is the substantive match; `05-what-broke.md` is a different realization entirely).

**F6 — PROJECT.md R0 wording one transition behind state.**
`PROJECT.md:16` (§"Current stage") said R0 was "ACTIVE pending the close of master [usurobor/cph#11](...)". Verified via `mcp__github__issue_read(11)`: cph#11 is `state: closed`, `state_reason: completed`, `closed_at: 2026-05-18T16:35:52Z`. The PROJECT.md wording was authored when cph#11 was open and was not updated when it closed. The next outstanding gate per the wave manifest §"Standing permissions" ("Run `coh` (TSC CLI) in CI: best-effort — `coh` is not on PATH...") and §"Known constraints" ("`coh` not on PATH. ... The first numeric C_Σ baseline lands when `coh` is on PATH...") is the first numeric C_Σ baseline. R0's `Status:` field stays `ACTIVE` per the issue body — the fix is wording-only on the pending-gate clause, not on the status word.

## Skills

**Tier 1 (CDD core):**
- `cdd/CDD.md` — lifecycle / role contract (α loaded, β explicitly excluded by identity isolation).
- `cdd/alpha/SKILL.md` — α role surface; this cycle exercises §2.5 (self-coherence authoring) and §2.6 (pre-review gate).
- `cdd/issue/SKILL.md` — AC interpretation; loaded implicitly to parse Sub A's AC1/AC2/AC3 oracles.

**Tier 3 (issue-specific):**
- `cnos.core/skills/write/SKILL.md` — short prose discipline; sub-A self-coherence is short prose; one governing question per section, state facts once, name the file+line that the fix touched.

**Not loaded:** no `eng/*` bundle. Sub A is two single-line surgical edits — no schema, no parser, no code path. No design or planning artifact required; the issue body fully specifies the patch (file + line + new text). No `cdd/design/SKILL.md` or `cdd/plan/SKILL.md` load.

## ACs

Sub A carries three ACs (AC1 F1, AC2 F6, AC3 no empirical drift). Oracle evidence per AC below.

### AC1 — F1 closed

**Negative oracle** (verbatim from issue body, scoped to exclude `.cdd/**` historical artifacts per issue text):

```text
$ grep -rn "05-friends-are-not-validation" . --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude
(no output)
```

Zero matches across the live tree. The dead reference is gone.

**Positive oracle** (issue body §Proof plan):

```text
$ grep -n "04-friends-are-a-pre-pilot" ROADMAP.md
85:- **Coherence risk:** Friend data is read as validation of the hypothesis rather than as a pipeline-robustness test (the realization the project owns as [`docs/realizations/04-friends-are-a-pre-pilot.md`](docs/realizations/04-friends-are-a-pre-pilot.md)). Adjacent risks: body-typing or labeling participants, eroding the "object is the step under a condition, not the person" boundary; the safety-boundary sentence in [`README.md`](README.md) ("Under this condition, this recording shows this movement pattern") drifting toward typology language in protocol or report drafts.
```

The R5 §Coherence risk paragraph cites `04-friends-are-a-pre-pilot.md` with a working markdown link. The realization file exists (verified by `ls docs/realizations/`).

**Adjacent check** — no other "05-friends-..." string variant slipped in:

```text
$ grep -rn "friends-are-not-validation" . --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude
(no output)
```

Zero matches on the substring without the `05-` prefix either.

**Verdict:** AC1 met.

### AC2 — F6 closed

**Positive oracle** (issue body §Proof plan):

PROJECT.md §"Current stage" no longer cites cph#11 as the pending gate. New wording at L16 (verbatim from the file at HEAD):

```text
**R1 — Existing-data zeroth pilot.** R0 (charter and operationalization) is ACTIVE pending the first numeric C_Σ baseline against this branch (the [`scripts/measure-coherence.sh`](scripts/measure-coherence.sh) entrypoint runs once `coh` is on PATH in an operator environment — see §"Last coherence measurement" below); R2–R6 are gated behind R1 and R2. See [`ROADMAP.md`](ROADMAP.md) for each phase's gate and status.
```

**Status word preserved.** "ACTIVE" survives unchanged — the wording change is on the pending-gate clause only, per the dispatch constraint *"`ACTIVE` is still correct until `coh` runs"*.

**Pending-gate alignment.** The new pending-gate clause names the same outstanding item the wave manifest itself names in §"Standing permissions" (`coh` not on PATH → first numeric C_Σ baseline deferred) and §"Out-of-scope follow-ups" first bullet ("First mechanical `coh --mode mechanical` run + recording the numeric α/β/γ/C_Σ baseline into `CHANGELOG.md` (still gated on `coh` being on PATH; this is the same deferred item the cph#11 wave named).").

**Negative oracle** — closed master is no longer referenced as a pending gate:

```text
$ grep -n "pending the close of master" PROJECT.md
(no output)
```

```text
$ grep -nE "cph#11|usurobor/cph#11" PROJECT.md
(no output)
```

Zero residual references to cph#11 in PROJECT.md.

**ROADMAP-alignment note.** AC2 says "Wording matches `ROADMAP.md` §"Phase R0" §Next action." `ROADMAP.md` R0 §Next action currently reads: "Sub B (this), Sub C, Sub D merge; wave `cdr-refactor-2026-05-18` closes; phase transitions to GO at wave close." That ROADMAP wording is *itself* one transition behind state (the `cdr-refactor-2026-05-18` wave closed; cph#11 closed). It is unchanged by Sub A per issue body §Non-goals ("Editing other ROADMAP phases."). The PROJECT.md wording change tracks the *substantive* current pending gate — the first numeric C_Σ baseline — which is what both files *should* point at once a follow-on cycle refreshes the R0 §Next action language. This judgment call is named in §Debt below so β can disagree if the strict literal-match reading is preferred.

**Verdict:** AC2 met (with the judgment call disclosed).

### AC3 — No empirical drift

**Status fields unchanged across ROADMAP.md.** The Sub A patch touches one line of ROADMAP.md (L85, inside R5 §Coherence risk — a parenthetical citation update only; no status word change, no goal change, no gate change). Verified by `git show 72c3845 -- ROADMAP.md`: the diff is one line changed, removing the broken citation parenthetical and replacing it with the working one. No `Status:` field is touched in the patch.

**README empirical-state language unchanged.** The patch does not touch `README.md`:

```text
$ git show 72c3845 --stat
 PROJECT.md | 2 +-
 ROADMAP.md | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)
```

Two files, two lines, no README touch.

**REVISE posture preserved.** `PROJECT.md` §"Current empirical decision" (next paragraph after §"Current stage") remains `**REVISE** (2026-05-17 real-data run, per [reports/field-report-01-existing-data-zeroth-pilot.md](...))` unchanged. The empirical state continues to trace to `reports/field-report-01-existing-data-zeroth-pilot.md` per master cph#16 AC7 + wave manifest §"Known constraints" first bullet.

**No new field report introduced.** The patch does not add files (`git show 72c3845 --stat` shows 2 modifications, 0 additions).

**Verdict:** AC3 met.

## Self-check

Re-read the diff at `git show 72c3845` looking for mistakes.

**ROADMAP.md L85 patch review.** The original parenthetical was `(the realization the project owns as` followed by an inline-code-styled filename. The new parenthetical preserves the same prose structure but uses a markdown link `` [`docs/realizations/04-friends-are-a-pre-pilot.md`](docs/realizations/04-friends-are-a-pre-pilot.md) `` instead of just a code-styled string. This is a small upgrade in surface quality (the citation is now clickable) and is consistent with the citation style used elsewhere in ROADMAP.md (e.g., L37 cites `[`scripts/measure-coherence.sh`](scripts/measure-coherence.sh)` as a markdown link, not just a code-styled string). No drift introduced; arguably a small coherence improvement.

**PROJECT.md L16 patch review.** The original sentence had a syntactic shape: `R0 (charter and operationalization) is ACTIVE pending the close of master [usurobor/cph#11](...)` — subject + status + pending-gate clause. The new sentence preserves exactly that shape: `R0 (charter and operationalization) is ACTIVE pending the first numeric C_Σ baseline against this branch (the [`scripts/measure-coherence.sh`](scripts/measure-coherence.sh) entrypoint runs once `coh` is on PATH in an operator environment — see §"Last coherence measurement" below)`. Subject unchanged, status unchanged ("ACTIVE"), pending-gate clause replaced. The remainder of the sentence (`; R2–R6 are gated behind R1 and R2. See [`ROADMAP.md`](ROADMAP.md)...`) is unchanged. The §"Last coherence measurement" forward-reference resolves: `grep -n '## Last coherence measurement' PROJECT.md` finds the section header (PROJECT.md carries that section per cph#11 AC7 requirement). No dangling reference introduced.

**Failure mode I checked for:** "the new wording quietly changes R0's status word." Verified it didn't — `Status:` field never appears on PROJECT.md L16 (the §"Current stage" line uses "is ACTIVE" inline, not the field name `Status:`); the substring "ACTIVE" survives verbatim across the diff.

**Failure mode I checked for:** "the citation upgrade in ROADMAP introduces a different filename." Verified the link target string `docs/realizations/04-friends-are-a-pre-pilot.md` matches the actual file via `ls docs/realizations/`. The text of the realization (read via `Read` on `docs/realizations/04-friends-are-a-pre-pilot.md` §Decision) substantively owns the "friends are not validation; they are a pre-pilot" claim that the ROADMAP R5 §Coherence risk paragraph names. Substantive match, not just filename match.

**Failure mode I checked for:** "the patch silently shifts adjacent text." Diff is exactly 2 lines (1 per file), no adjacent prose touched. `git show 72c3845` confirms the unchanged-context lines on either side are unchanged.

**Ambiguity passed to β:**
- AC2's literal "matches `ROADMAP.md` §Phase R0 §Next action" reading vs the substantive "matches the actual outstanding gate" reading (disclosed in §ACs AC2 and §Debt item 1). β may flag this. The fix if β reads literally is a one-paragraph rewrite of PROJECT.md L16 to copy the ROADMAP wording verbatim (which would itself be stale, just stale in the same way as ROADMAP — making them at least drift-consistent).

## Debt

1. **ROADMAP R0 §Next action is itself stale.** `ROADMAP.md:36` (R0 §Next action) reads "Sub B (this), Sub C, Sub D merge; wave `cdr-refactor-2026-05-18` closes; phase transitions to GO at wave close." That `cdr-refactor-2026-05-18` wave closed 2026-05-18 (per `42466ad ε wave-iteration: cdr-refactor-2026-05-18` in git log). PROJECT.md's L16 update implicitly points at a different (substantive) outstanding gate than ROADMAP R0 §Next action's literal wording. Sub A §Non-goals forbids editing other ROADMAP phases. A follow-on cycle (out of this wave's scope per wave manifest §"Out-of-scope follow-ups") should refresh ROADMAP R0 §Next action to also point at the first-numeric-C_Σ baseline, at which point PROJECT.md and ROADMAP fully realign. **Mitigation in scope:** the ROADMAP R5 §Coherence risk citation (which Sub A *does* touch) is fully fixed; the PROJECT.md wording is fixed; the structural drift between ROADMAP R0 and PROJECT.md is named here as wave-scoped debt.

2. **`.gitignore` patch on top of α implementation by δ.** Between α's Sub A implementation commit (`72c3845`) and α's self-coherence write (this file), δ added one commit (`91fd2e5`) that adds `.claude/` to `.gitignore` to silence harness scaffolding. That commit is δ-authored (`δ-as-agent <delta@cph.cdd.cnos>`), not α, so it does not violate α's identity discipline. It does not touch Sub A's surface (ROADMAP.md / PROJECT.md) and does not affect any Sub A AC. Named here only so β's audit of the diff against `dcd0d50` (wave-open) sees the intermediate δ commit and does not flag it as α drift.

3. **Sub A patch authored before this self-coherence write.** Standard CDD ordering writes the self-coherence sections as α goes; here the implementation commit (`72c3845`, 2026-05-18 23:02:12 UTC) preceded this self-coherence write by 12 minutes (initial α work happened in an earlier session; this session resumes to complete the self-coherence artifact). All implementation evidence is re-verified at this self-coherence write time — no claim in §ACs depends on memory of the earlier session.

## CDD-Trace

Per `cdd/alpha/SKILL.md` §2.2 canonical artifact order. Sub A is two-line docs patch; several steps are explicitly `not required` with reason.

1. **Design** — *not required.* The two patches are fully specified in the issue body: which file, which line, which new string. No design space to explore.
2. **Coherence contract** — §Gap above. The contract: (a) ROADMAP.md L85 cites the real `04-friends-are-a-pre-pilot.md` filename; (b) PROJECT.md L16 wording reflects R0's actual outstanding gate (first numeric C_Σ baseline), with status word `ACTIVE` preserved; (c) no empirical state change.
3. **Plan** — *not required.* Linear: read realization dir → verify cph#11 closure via `mcp__github__issue_read` → patch two lines → run AC oracles → write self-coherence.
4. **Tests** — the AC oracles are the tests. Pasted verbatim in §ACs (`grep -rn "05-friends-are-not-validation" .` empty; `grep -n "04-friends-are-a-pre-pilot" ROADMAP.md` hits L85; `git show 72c3845 --stat` 2 files 2 insertions 2 deletions).
5. **Code** — *not applicable.* Sub A is docs-only.
6. **Docs** — two single-line edits across two files: `ROADMAP.md` L85 (R5 §Coherence risk parenthetical citation), `PROJECT.md` L16 (§"Current stage" pending-gate clause). `git diff --stat dcd0d50..72c3845` returns `PROJECT.md | 2 +- ROADMAP.md | 2 +- 2 files changed, 2 insertions(+), 2 deletions(-)` — matches expected surface exactly.
7. **Self-coherence** — this file. Authored single-pass after re-verification of all oracles at HEAD.

Trace status: steps 1–7 covered. Pre-review gate (§2.6) next.

**Step-by-step ledger of this sub's work:**

| # | Step | Evidence |
|---|---|---|
| 1 | Read wave manifest | `.cdd/waves/coherence-drift-sweep-2026-05-18/manifest.md` — confirmed single-branch dispatch on `claude/review-repo-coherence-PNbjQ`, file-disjointness check, REVISE invariant |
| 2 | Read sub-issue body via mcp | `mcp__github__issue_read(17)` — confirmed scope (F1+F6) and the three ACs |
| 3 | Verify cph#11 closure via mcp | `mcp__github__issue_read(11)` — state=closed, state_reason=completed, closed_at=2026-05-18T16:35:52Z |
| 4 | Verify realization filename | `ls docs/realizations/` → `04-friends-are-a-pre-pilot.md` is the substantive match |
| 5 | Implementation commit | `72c3845 α #17: fix broken realization ref (F1) + R0 wording in PROJECT.md (F6)`, authored α-as-agent <alpha@cph.cdd.cnos> |
| 6 | AC1 oracle | `grep -rn "05-friends-are-not-validation" . --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude` → empty |
| 7 | AC2 oracle | `sed -n '12,20p' PROJECT.md` → new wording cites first numeric C_Σ baseline, preserves ACTIVE status word, no cph#11 reference |
| 8 | AC3 oracle | `git show 72c3845 --stat` → 2 files / 2 insertions / 2 deletions, no README touch, no Status: field touched |
| 9 | Self-coherence write | this file at `.cdd/unreleased/17/self-coherence.md` |
| 10 | Self-coherence commit | (next: `α #17: self-coherence`) |
| 11 | Push | (next: `git push origin claude/review-repo-coherence-PNbjQ`) |

## Review-readiness

**Round:** 1.
**Base SHA:** `dcd0d50` (δ wave-open commit on `claude/review-repo-coherence-PNbjQ`).
**Implementation SHA:** `72c3845` (α Sub A implementation commit; stable per `cdd/alpha/SKILL.md` §2.6 SHA convention — name the implementation SHA, not the readiness-signal HEAD).
**Intermediate δ commit:** `91fd2e5` (.gitignore `.claude/`; δ-authored; named in §Debt item 2; does not touch Sub A surface).
**Branch CI:** not configured in this repo (no `.github/workflows/`). Local AC oracles run clean and are pasted in §ACs for β re-run.
**Author email:** `alpha@cph.cdd.cnos` on the Sub A implementation commit (`git log --format='%h %ae' -1 72c3845` → `72c3845 alpha@cph.cdd.cnos`). Matches `alpha@{project}.cdd.cnos` per `cdd/operator/SKILL.md` §Git identity.

**Pre-review gate (`cdd/alpha/SKILL.md` §2.6) row-by-row:**

| # | Row | Status | Evidence |
|---|---|---|---|
| 1 | Branch rebased onto current base | ✅ | Working branch is `claude/review-repo-coherence-PNbjQ`; wave base is `dcd0d50` on same branch; α implementation sits on top |
| 2 | CDD Trace through step 7 | ✅ | §CDD-Trace covers 1–7 |
| 3 | Tests present or "none apply" | ✅ | AC oracles are structural grep + git-show, pasted verbatim in §ACs |
| 4 | Every AC has evidence | ✅ | AC1 (negative + positive oracle), AC2 (positive + negative + alignment note), AC3 (status / README / files-changed evidence) |
| 5 | Known debt explicit | ✅ | §Debt enumerates 3 items |
| 6 | Schema / shape audit when contracts changed | N/A | No schema; ROADMAP.md and PROJECT.md are human-readable docs |
| 7 | Peer enumeration when closure touches a family | ✅ | Peer set = the five `docs/realizations/*.md` files; all five enumerated in §Gap to verify `04-` is the substantive match for the R5 §Coherence risk citation |
| 8 | Harness audit | N/A | No harness; no schema-bearing contract |
| 9 | Post-patch re-audit | N/A | No mid-cycle patch; round 1 single-pass |
| 10 | Branch CI green | N/A | No CI configured in repo |
| 11 | Artifact enumeration matches diff | ✅ | `git diff --stat dcd0d50..72c3845` returns `PROJECT.md \| 2 +- ROADMAP.md \| 2 +-`; both files named in §CDD-Trace step 6 |
| 12 | Caller-path trace for new modules | N/A | No new modules; docs-only |
| 13 | Test assertion count from runner | N/A | AC oracles inline in §ACs |
| 14 | α commit author email canonical | ✅ | `72c3845` author email = `alpha@cph.cdd.cnos` (verified via `git log --format='%ae' -1 72c3845`) |

**Verdict:** ready for β review (round 1).
