# Self-coherence — Sub B — cph#23 — F8 + F9 PROJECT.md §Active branch + ROADMAP.md R0 de-staling

## Gap

**Issue:** usurobor/cph#23 — Sub B — F8 (PROJECT.md §Active branch / issue stale) + F9 (ROADMAP.md R0 §Next action + §Owning files stale).
**Master:** usurobor/cph#21.
**Wave:** `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/manifest.md`.
**Branch:** `claude/review-repo-coherence-PNbjQ`.
**Mode:** docs-only (small).

**F8 — PROJECT.md §"Active branch / issue" describes a closed wave as in-flight.**

Pre-patch state (verified by `git show 8981e96:PROJECT.md | sed -n '32,36p'` — the wave-open baseline):

```text
## Active branch / issue

- **Master:** [usurobor/cph#11](...) — CDR refactor wave (open until A+B+C+D close).
- **In-flight wave:** [`cdr-refactor-2026-05-18`](...) — Sub A merged ([cph#12](...)), Sub B merged ([cph#13](...)), Sub C in cycle ([cph#14](...)), Sub D pending (cph#15, dispatched when A+B+C reach terminal state).
- **Unmerged orthogonal branch:** `origin/cycle/segmentation-real-data-fix` (tip `a95415c`) ...
```

cph#11 is closed (closed 2026-05-18 16:35); the cdr-refactor wave closed; cph#14 and cph#15 are both closed. The section described state from before 2026-05-18 16:35; by the wave-open commit (`8981e96`, 2026-05-19) the section was stale by ≥ one full day and one full wave (the `coherence-drift-sweep-2026-05-18` wave, master cph#16, closed on the review branch).

**F9 — ROADMAP.md R0 §"Next action" + §"Owning files" stale.**

Pre-patch state at ROADMAP.md L36–37:

```text
- **Next action:** Sub B (this), Sub C, Sub D merge; wave [`cdr-refactor-2026-05-18`](...) closes; phase transitions to GO at wave close.
- **Owning files:** [`README.md`](README.md), [`CDR.md`](CDR.md), ..., `ROADMAP.md` (this), [`PROJECT.md`](PROJECT.md), `CHANGELOG.md` (pending Sub C), `targets/*.tsc` (pending Sub C), `scripts/measure-coherence.sh` (pending Sub C).
```

Three `(pending Sub C)` qualifiers on files that all landed when cdr-refactor wave Sub C (cph#14) closed. The "Next action" sentence names a closed wave's sub-merges as the next action.

**Post-patch state.** PROJECT.md §"Active branch / issue" describes the live state under pattern (b-1) per the issue body §Scope: names the review branch `claude/review-repo-coherence-PNbjQ` as the active surface, lists the two coherence-drift-sweep waves currently reviewing on it (precursor `coherence-drift-sweep-2026-05-18` closed all subs APPROVE / master close = ε gate; follow-up `coherence-drift-sweep-followup-2026-05-18` in flight with cph#22–25), notes the unmerged segmentation branch. ROADMAP R0 §"Next action" rewritten to name the actually-outstanding gate: the first numeric C_Σ baseline via `scripts/measure-coherence.sh`, gated on `coh` being on PATH (per `CHANGELOG.md` 0.1.0-cdr §"Deferred items"). R0 §"Owning files" has the three `(pending Sub C)` qualifiers stripped; `CHANGELOG.md` and `scripts/measure-coherence.sh` are now linked (the pre-patch text already linked README, CDR, etc., but left `CHANGELOG.md` / `targets/*.tsc` / `scripts/measure-coherence.sh` plain because of the `(pending Sub C)` qualifier — post-patch the consistent link style is restored).

## Skills

**Tier 1 (CDD core):**
- `cdd/CDD.md` — lifecycle and role contract.
- `cdd/alpha/SKILL.md` — α role surface; §2.5 self-coherence, §2.6 pre-review gate.
- `cdd/issue/SKILL.md` — AC interpretation for AC1–AC5.

**Tier 3 (issue-specific):**
- `cnos.core/skills/write/SKILL.md` — short prose; describe live state, not historical state.

**Not loaded:** no design/plan skill — direction-choice is bounded by issue body §Scope (b-1 / b-2 enumerated) and the dispatch recommends b-1.

## ACs

Sub B carries five ACs. AC1 and AC2 are the load-bearing de-staling oracles; AC3–AC5 are scope/no-drift backstops.

### Direction choice

**Direction (b-1).** Describe the in-flight state in §"Active branch / issue": name the review branch, name the two coherence-drift-sweep waves currently reviewing on it, name the unmerged segmentation branch. Direction (b-2) (drop the section entirely) would remove a section that PROJECT.md's contract names as a status-bearing surface; the live state is informative enough to keep the section, just rewritten. Issue body recommends b-1.

### AC1 — PROJECT.md §"Active branch / issue" describes the live state

```text
$ grep -nE 'cph#1[12345]' PROJECT.md
(no matches)
```

No `cph#11`, `cph#12`, `cph#13`, `cph#14`, or `cph#15` mentions in PROJECT.md post-patch. The closed cdr-refactor wave's master and subs are no longer named as in-flight. The new §"Active branch / issue" mentions `cph#16` (precursor wave master, all subs APPROVE) and `cph#21` (current wave master) — both as live state, not as in-flight cph#11–15 assertions.

Post-patch section text (verified by `sed -n '32,38p' PROJECT.md`):

```text
## Active branch / issue

- **Review branch:** `claude/review-repo-coherence-PNbjQ` — review surface for two coherence-drift-sweep waves landed against R0 ...
- **In-flight waves on the review branch:**
  - [`coherence-drift-sweep-2026-05-18`](...) — master [cph#16](...); all four subs (cph#17–20) closed APPROVE; master close is an ε/operator gate.
  - [`coherence-drift-sweep-followup-2026-05-18`](...) — master [cph#21](...); four subs (cph#22–25) in flight on this branch.
- **Unmerged orthogonal branch:** `origin/cycle/segmentation-real-data-fix` (tip `a95415c`) — R2 segmentation fix; merge is a separate operator decision per the precursor cdr-refactor wave's manifest.
```

Three bullets describe the live state. The section header remains §"Active branch / issue" (issue body permits dropping it, but b-1 keeps it).

**Verdict:** AC1 met.

### AC2 — ROADMAP R0 §"Next action" no longer names `cdr-refactor-2026-05-18` as gate

```text
$ grep -n 'cdr-refactor-2026-05-18' ROADMAP.md
(no matches)
```

No `cdr-refactor-2026-05-18` references anywhere in ROADMAP.md post-patch. The §"Next action" sentence now reads: "Land the first numeric C_Σ baseline against this branch via `scripts/measure-coherence.sh`, gated on `coh` being on PATH in an operator environment (per `CHANGELOG.md` 0.1.0-cdr §'Deferred items'). The mechanical entrypoint is in place; the baseline lands the first time `coh --mode mechanical` runs against this branch and gets recorded in `CHANGELOG.md`. Phase transitions to GO at that recording."

This names the actually-outstanding R0 gate — the same gate `PROJECT.md` §"Current stage" L16 / §"Last coherence measurement" L42–44 already describe as outstanding, and the same gate `CHANGELOG.md` 0.1.0-cdr §"Deferred items" names as gated on `coh` being on PATH.

**Verdict:** AC2 met.

### AC3 — ROADMAP R0 §"Owning files" carries no `(pending Sub C)` qualifiers

```text
$ grep -n '(pending Sub C)' ROADMAP.md
(no matches)
```

No `(pending Sub C)` strings anywhere in ROADMAP.md post-patch. The three files (`CHANGELOG.md`, `targets/*.tsc`, `scripts/measure-coherence.sh`) are now listed without qualifier. Two of them (`CHANGELOG.md`, `scripts/measure-coherence.sh`) gained the markdown-link style consistent with the rest of the list; `targets/*.tsc` stays unlinked because it's a glob, not a single file (consistent with how the file is referenced elsewhere in the repo).

**Verdict:** AC3 met.

### AC4 — No empirical drift

```text
$ git show c3e0ee8 -- README.md
(empty)
$ git show c3e0ee8 -- reports/
(empty)
$ git show c3e0ee8 -- CHANGELOG.md
(empty)
```

No README / reports / CHANGELOG touch. PROJECT.md §"Current empirical decision" remains `REVISE` (verified by `grep -n REVISE PROJECT.md` → L20 unchanged in the patch). No new field report. No new empirical claim.

**Verdict:** AC4 met.

### AC5 — Surface scope held

```text
$ git show c3e0ee8 --stat
 PROJECT.md | 8 +++++---
 ROADMAP.md | 4 ++--
 2 files changed, 7 insertions(+), 5 deletions(-)
```

Exactly two files: `PROJECT.md` and `ROADMAP.md`. No other surface touched. ROADMAP edits are bounded to R0 (L36–37 only); R1–R6 untouched. PROJECT.md edits are bounded to §"Active branch / issue" (L32–36 → L32–38 post-patch); §"Current stage", §"Current empirical decision", §"Current blocker", §"Next action", §"Last field report", §"Last coherence measurement" all untouched.

**Verdict:** AC5 met.

## Self-check

Re-read `git show c3e0ee8` looking for mistakes.

**Mistake check 1 — F8 facts.** The new PROJECT.md §"Active branch / issue" claims:
- The review branch is `claude/review-repo-coherence-PNbjQ`. ✓ (`git branch --show-current` returns this).
- The cdr-refactor wave is closed. ✓ (cph#11–15 all closed per the issue body §"Source of truth" and the cdr-refactor wave-closeout in `.cdd/waves/cdr-refactor-2026-05-18/wave-closeout.md`).
- The precursor `coherence-drift-sweep-2026-05-18` wave has all four subs (cph#17–20) closed APPROVE. ✓ (verified by `git log --oneline -30` showing `β #17/18/19/20: review APPROVE + close-out` commits).
- Master close on cph#16 is an ε/operator gate. ✓ (matches the wave manifest §"Branching deviation" pattern: "master close is ε's authority, not δ's").
- The follow-up wave's subs are cph#22–25. ✓ (issue body lists 22, 23, 24, 25; wave manifest §Issues table confirms).
- The unmerged segmentation branch tip is `a95415c`. Preserved verbatim from the pre-patch text; no new fact introduced. ✓.

**Mistake check 2 — F9 facts.** The new ROADMAP.md R0 §"Next action" claims:
- The first C_Σ baseline lands via `scripts/measure-coherence.sh`. ✓ (matches PROJECT.md L44 "The mechanical entrypoint `scripts/measure-coherence.sh` is in place; the first numeric C_Σ baseline lands the first time `coh` runs against this branch").
- The baseline is gated on `coh` being on PATH per `CHANGELOG.md` 0.1.0-cdr §"Deferred items". Verified by `grep -n 'Deferred items\|coh' CHANGELOG.md` returning the 0.1.0-cdr deferred-items block naming `coh` PATH availability as the gating constraint.
- The baseline closes R0 (phase → GO). ✓ (ROADMAP §"How to read this file" L21: "Closes" means status transitions out of ACTIVE / REVISE into GO).

**Mistake check 3 — adjacency creep.** Patch touches only:
- PROJECT.md L32–36 (§"Active branch / issue" block; now L32–38 due to expanded bullet list).
- ROADMAP.md L36 (§"Next action" line) + L37 (§"Owning files" line).

No other sections touched. Verified by `git diff c3e0ee8~1 c3e0ee8 -- PROJECT.md | grep '^@@'` and `git diff c3e0ee8~1 c3e0ee8 -- ROADMAP.md | grep '^@@'` showing exactly one hunk per file at the expected line range. ✓.

**Mistake check 4 — R0 status field unchanged.** ROADMAP R0 §Status (L34) remains `ACTIVE`. The issue body L75 says: "R0 §Status stays ACTIVE unless α has a substantive reason to transition to GO — and per `ROADMAP.md` §'How to read this file' only the gate transitions a phase, so the gate must close (the first C_Σ baseline lands) before status can transition." α did not transition the status field. ✓.

**Mistake check 5 — link consistency in R0 §Owning files.** Pre-patch had `CHANGELOG.md (pending Sub C)`, `targets/*.tsc (pending Sub C)`, `scripts/measure-coherence.sh (pending Sub C)` — three plain-text references (no markdown link). The pre-patch list also had `README.md`, `CDR.md`, etc. as `[README.md](README.md)` markdown-link style. Post-patch I added markdown-link wrapping to `CHANGELOG.md` and `scripts/measure-coherence.sh` for style consistency. `targets/*.tsc` stays unlinked because it's a glob pattern. The wrapping is not strictly required by the AC (the AC only requires the `(pending Sub C)` qualifier be removed), but the cost is one keystroke per file and the result is more consistent. β may push back if they prefer the qualifier removal without link wrapping; the fix is two characters and the AC is unaffected. ✓.

**Mistake check 6 — orthogonal segmentation branch reference.** The pre-patch bullet said "merge is a separate operator decision per the wave manifest" — referring to the cdr-refactor wave manifest. Post-patch I rewrote to "per the precursor cdr-refactor wave's manifest" to make the antecedent explicit now that the surrounding context is no longer the cdr-refactor wave. Same fact; clearer reference. ✓.

**Ambiguity passed to β:**
- The wave manifest's permitted patterns (b-1 vs b-2) — α picked b-1 because the section carries useful live-state pointers (review branch, segmentation branch). β may prefer b-2 (drop the section). The fix is to delete the four lines and move the segmentation-branch pointer elsewhere (probably to PROJECT.md §"Next action" or as a top-level note). If β requests b-2, α can take a fix round.
- The link wrapping in R0 §"Owning files" (mistake-check 5).

## Debt

1. **F12 (CHANGELOG entry for the precursor wave) is named but not landed.** Per the issue body §Non-goals and the wave manifest §"Out-of-scope follow-ups", F12 is a policy decision for ε/operator. This sub does not land a CHANGELOG entry for the coherence-drift-sweep wave. Named here for trace; ε/operator owns the call.

2. **Master cph#16 (precursor wave) and cph#21 (follow-up wave, this wave) close are both ε/operator gates.** PROJECT.md now names this state; the actual close is not in α's authority. Named for trace.

3. **`coh` is not on PATH in this environment.** The R0 §"Next action" now names the gate; the gate's closure (first C_Σ baseline) is still deferred. Same deferred item the cph#11 and cph#16 waves named. Named for trace.

4. **Field-report-02 stub H1 number mismatch (Sub C surface).** Re-noted for serial-review trace; Sub C's α (this session, next step) lands the H1 fix.

5. **`extract_shape` always-`True` placeholder (Sub D surface).** Re-noted for serial-review trace; Sub D's α (this session, two steps from now) lands the rename.

## CDD-Trace

Per `cdd/alpha/SKILL.md` §2.2.

1. **Design** — direction-(b-1) chosen by issue-body recommendation. Single decision point ("keep §Active branch / issue with live-state content, or drop it?" → keep). No separate design artifact.
2. **Coherence contract** — §Gap. PROJECT.md §"Active branch / issue" and ROADMAP R0 §"Next action" + §"Owning files" describe live state. No empirical drift. No CHANGELOG entry. No README touch.
3. **Plan** — implicit. Linear: read PROJECT.md L32–36 → read ROADMAP.md L36–37 → verify cph#11/14/15 closed via issue body §"Source of truth" → write live-state text → AC oracles → self-coherence.
4. **Tests** — AC oracles pasted in §ACs (`grep -nE 'cph#1[12345]' PROJECT.md` empty for AC1; `grep -n 'cdr-refactor-2026-05-18' ROADMAP.md` empty for AC2; `grep -n '(pending Sub C)' ROADMAP.md` empty for AC3; empty `git show -- README/reports/CHANGELOG` for AC4; 2-file `git show --stat` for AC5).
5. **Code** — *not authored*. Sub B is docs-only.
6. **Docs** —
   - `PROJECT.md`: §"Active branch / issue" rewritten as a 3-bullet live-state block (review branch / in-flight waves / unmerged orthogonal branch).
   - `ROADMAP.md`: R0 §"Next action" rewritten to name the C_Σ baseline gate; R0 §"Owning files" stripped of `(pending Sub C)` qualifiers with link-style consistency restored on `CHANGELOG.md` and `scripts/measure-coherence.sh`.
7. **Self-coherence** — this file.

**Step-by-step ledger:**

| # | Step | Evidence |
|---|---|---|
| 1 | Read sub-issue body | `mcp__github__issue_read(23)` |
| 2 | Read PROJECT.md | `Read PROJECT.md` |
| 3 | Read ROADMAP.md | `Read ROADMAP.md` |
| 4 | Verify cph#11/14/15 closed | issue body §"Source of truth"; cdr-refactor wave-closeout |
| 5 | Verify precursor wave's subs all APPROVE | `git log --oneline -30` showing `β #17/18/19/20: review APPROVE + close-out` |
| 6 | Direction choice | b-1 per §"Direction choice" |
| 7 | Edit PROJECT.md §"Active branch / issue" | rewrote 4 bullets → 3 bullets describing live state |
| 8 | Edit ROADMAP.md R0 §"Next action" | rewrote sentence to name C_Σ baseline gate |
| 9 | Edit ROADMAP.md R0 §"Owning files" | stripped `(pending Sub C)`, restored link style |
| 10 | AC1 grep | empty |
| 11 | AC2 grep | empty |
| 12 | AC3 grep | empty |
| 13 | AC4 file-no-touch | empty |
| 14 | AC5 diff stat | exactly PROJECT.md + ROADMAP.md |
| 15 | Implementation commit | `c3e0ee8 α #23: de-stale PROJECT.md §Active branch + ROADMAP.md R0 §Next action (F8 + F9)` |
| 16 | Self-coherence write | this file |
| 17 | Self-coherence commit | (next: `α #23: self-coherence`) |
| 18 | Push | (next) |

## Review-readiness

**Round:** 1.
**Base SHA for this sub:** `3bc4242` (Sub A self-coherence commit).
**Implementation SHA:** `c3e0ee8`.
**Branch CI:** N/A.
**Author email:** `alpha@cph.cdd.cnos` on `c3e0ee8`.

**Pre-review gate row-by-row:**

| # | Row | Status | Evidence |
|---|---|---|---|
| 1 | Branch rebased | ✓ | Sub B sits directly on top of Sub A self-coherence |
| 2 | CDD Trace through step 7 | ✓ | §CDD-Trace |
| 3 | Tests present or "none apply" | ✓ | AC oracles inline (grep + git-show) |
| 4 | Every AC has evidence | ✓ | AC1 (empty `grep cph#1[12345]` + post-patch text), AC2 (empty `grep cdr-refactor-2026-05-18`), AC3 (empty `grep '(pending Sub C)'`), AC4 (empty `git show -- README/reports/CHANGELOG`), AC5 (2-file `git show --stat`) |
| 5 | Known debt explicit | ✓ | §Debt 1–5 |
| 6 | Schema/shape audit | N/A | docs-only de-staling, no schema |
| 7 | Peer enumeration when closure touches a family | ✓ | All three `(pending Sub C)` qualifiers enumerated; both stale references (cph#11/14/15; cdr-refactor-2026-05-18) enumerated |
| 8 | Harness audit | N/A | no harness change |
| 9 | Post-patch re-audit | N/A | single-pass round 1 |
| 10 | Branch CI green | N/A | no CI |
| 11 | Artifact enumeration matches diff | ✓ | `git show c3e0ee8 --stat` returns exactly PROJECT.md + ROADMAP.md |
| 12 | Caller-path trace for new modules | N/A | no new modules |
| 13 | Test assertion count | N/A | grep oracles inline |
| 14 | α commit author canonical | ✓ | `c3e0ee8` author = `alpha@cph.cdd.cnos` |

**Verdict:** ready for β review (round 1).
