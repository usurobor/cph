# Self-coherence — Sub B — cph#18 — F2 field-report-02 collision

## Gap

**Issue:** usurobor/cph#18 — Sub B — F2 (`field-report-02` identifier collision in `ROADMAP.md` between R3's future construct-evaluation report and R5's future friend-pre-pilot report).
**Master:** usurobor/cph#16.
**Wave:** `.cdd/waves/coherence-drift-sweep-2026-05-18/manifest.md`.
**Branch:** `claude/review-repo-coherence-PNbjQ` (single-branch dispatch).
**Mode:** docs-only, small (design call: which identifier scheme to apply).

**The collision.** `ROADMAP.md` (pre-patch) referenced `field-report-02` at three lines for two distinct future reports:

- L66 (R3 §Next action): "Produce field-report-02 with the construct evaluation…"
- L67 (R3 §Owning files): "future field-report-02."  ← issue body lists L66/L83/L87 but the R3 §Owning files line at L67 also names "future field-report-02"; covering it here for AC2 consistency
- L83 (R5 §Gate): "field-report-02 documents what survived…"
- L87 (R5 §Owning files): "future field-report-02 (friend pre-pilot)"

R3 and R5 cannot both produce `field-report-02`. The first to ship takes the number, the second has to be something else.

**Scheme decision (forced by the filesystem).** The issue body §Source of truth instructs α to verify whether `reports/field-report-02-friend-pre-pilot.md` already exists. It does:

```text
$ ls reports/
field-report-00-plan.md
field-report-01-existing-data-zeroth-pilot.md
field-report-02-friend-pre-pilot.md
```

The R5 friend-pre-pilot report has already claimed identifier `02` with a stub file on disk (verified with `head -20 reports/field-report-02-friend-pre-pilot.md` — file exists as a template, awaiting data). This pre-determines the scheme: **R5 keeps `field-report-02-friend-pre-pilot`**, R3's forthcoming construct-evaluation report must take a different identifier.

**Identifier chosen for R3.** `field-report-03-construct-evaluation.md`. Rationale:

- Numbering follows time-of-publication (the convention the wave manifest's `Five-factor heuristic outcome` row and existing reports already use: `00-plan`, then `01-existing-data-zeroth-pilot`, then `02-friend-pre-pilot` once R5 ships).
- Time-of-publication ordering depends on R3 vs R5 ship order. Per ROADMAP.md R3 §Status `NOT STARTED` and R5 §Status `Blocked until earlier gates pass`, R5 is gated behind R3 + R4. R3 ships before R5 *if R3 actually runs first*. But the disk already has `field-report-02-friend-pre-pilot.md` claimed by R5; that fact is the load-bearing one. Even if R3 ships first chronologically, the R5 stub already binds `-02` to friend-pre-pilot — renaming the stub would require editing it, which is forbidden by issue body §Non-goals ("Editing any existing field report").
- The remaining free identifier ≥ 03 that maintains numeric-monotonic readability is `-03-construct-evaluation` (descriptive suffix matching the kind in §Next action prose). Scheme (b) from issue body (`field-report-r3-construct.md`) is also valid, but (a)+phase-suffix-only is *not* in use elsewhere (the existing `02-friend-pre-pilot` carries a content suffix, not a phase suffix), so picking the content-suffix form keeps the existing scheme intact.

**Net edits.** Four lines, all in `ROADMAP.md`:

| Line | Pre-patch | Post-patch |
|---|---|---|
| L66 | `Produce field-report-02 with the construct evaluation…` | `Produce `field-report-03-construct-evaluation` with the construct evaluation…` |
| L67 | `future field-report-02.` (end of R3 §Owning files) | `future `reports/field-report-03-construct-evaluation.md`.` |
| L83 | `field-report-02 documents what survived…` | `` `field-report-02-friend-pre-pilot` documents what survived… `` |
| L87 | `future field-report-02 (friend pre-pilot).` | `` [`reports/field-report-02-friend-pre-pilot.md`](reports/field-report-02-friend-pre-pilot.md) (stub; awaiting data). `` |

L87 changed phrasing more substantively because the stub file already exists — calling it "future" is wrong (it's on disk); naming it as the existing template that R5 will fill in is the accurate statement. This is a small substantive improvement adjacent to the naming fix, and it traces directly to the issue body §Source of truth verification result (the stub exists).

## Skills

**Tier 1 (CDD core):**
- `cdd/CDD.md` — lifecycle / role contract.
- `cdd/alpha/SKILL.md` — α role surface; §2.5 (self-coherence authoring), §2.6 (pre-review gate).
- `cdd/issue/SKILL.md` — AC interpretation for AC1 / AC2 / AC3.

**Tier 3 (issue-specific):**
- `cnos.core/skills/write/SKILL.md` — short prose discipline; name files+lines that change; state the scheme decision once and justify once.

**Not loaded:** no `eng/*` bundle. Sub B is four small markdown edits on one file. No code, no schema, no parser, no test runner. No design or planning skill loaded; the design space (3 schemes) was resolved by a filesystem check.

## ACs

Sub B carries three ACs (AC1 no identifier collision; AC2 scheme is internally consistent; AC3 no empirical drift). Oracle evidence per AC below.

### AC1 — No identifier collision

**Oracle (verbatim from issue body):**

```text
$ grep -nE "field-report-0[0-9]" ROADMAP.md
13:**R1 is REVISE** per [`reports/field-report-01-existing-data-zeroth-pilot.md`]…
42:- **Current evidence:** Per [`reports/field-report-01-existing-data-zeroth-pilot.md`]…
46:- **Next action:** Hold REVISE until R2 closes; then re-run … and re-evaluate the falsification table in field-report-01.
47:- **Owning files:** … [`reports/field-report-01-existing-data-zeroth-pilot.md`]…
52:- **Current evidence:** Per [`reports/field-report-01-existing-data-zeroth-pilot.md`] §Segmentation Status …
57:- **Owning files:** … [`reports/field-report-01-existing-data-zeroth-pilot.md`] (re-evaluation).
62:- **Current evidence:** Per [`reports/field-report-01-existing-data-zeroth-pilot.md`] §Support-Path Inference …
66:- **Next action:** … Produce `field-report-03-construct-evaluation` …
67:- **Owning files:** … future `reports/field-report-03-construct-evaluation.md`.
72:- **Current evidence:** Per [`reports/field-report-01-existing-data-zeroth-pilot.md`] §Falsification Assessment …
83:- **Gate:** … `field-report-02-friend-pre-pilot` documents what survived …
87:- **Owning files:** … [`reports/field-report-02-friend-pre-pilot.md`] (stub; awaiting data).
```

**Identifier accounting:**

| Identifier | Distinct future report? | Lines |
|---|---|---|
| `field-report-01-existing-data-zeroth-pilot` | No — existing merged report | L13, L42, L46, L47, L52, L57, L62, L72 (8 refs, all to the same existing report) |
| `field-report-02-friend-pre-pilot` | One future report (R5) | L83, L87 (2 refs, same R5 future report) |
| `field-report-03-construct-evaluation` | One future report (R3) | L66, L67 (2 refs, same R3 future report) |

Each identifier maps to *one* report (existing or future). No identifier is shared between two distinct reports. **AC1 met.**

### AC2 — Scheme is internally consistent

**Oracle:** R3 §Next action, R3 §Owning files, R5 §Gate, R5 §Owning files all use the chosen scheme.

```text
$ grep -nE "field-report-0[23]" ROADMAP.md
66:- **Next action:** … Produce `field-report-03-construct-evaluation` …
67:- **Owning files:** … future `reports/field-report-03-construct-evaluation.md`.
83:- **Gate:** … `field-report-02-friend-pre-pilot` documents what survived …
87:- **Owning files:** … [`reports/field-report-02-friend-pre-pilot.md`] (stub; awaiting data).
```

R3 references use `field-report-03-construct-evaluation` (with optional `reports/`-prefix when citing the full path); R5 references use `field-report-02-friend-pre-pilot`. The four references split cleanly: 2 R3 references, 2 R5 references, no cross-contamination.

**Reader test (issue body §Proof plan negative case):** "re-reading R3 + R5 in isolation does not give a reader the impression they are reading about the same future report."

- R3 §Next action + §Owning files mention only `field-report-03-construct-evaluation`. No `-02` string.
- R5 §Gate + §Owning files mention only `field-report-02-friend-pre-pilot`. No `-03` string.
- The two reports carry distinct content suffixes (`construct-evaluation` vs `friend-pre-pilot`), making the distinction visible even if a reader skims the identifier number.

**AC2 met.**

### AC3 — No empirical drift

**No empirical state changed.** The patch is four reference-string edits inside R3 §Next action / §Owning files and R5 §Gate / §Owning files. No `Status:` field is touched. No empirical claim is added or removed. The latest merged field report (`reports/field-report-01-existing-data-zeroth-pilot.md`) is unchanged. README is not touched.

```text
$ git show a7684f1 --stat
 ROADMAP.md | 8 ++++----
 1 file changed, 4 insertions(+), 4 deletions(-)
```

One file, four lines changed, no additions of new field reports. The R3 status remains `NOT STARTED`; the R5 status remains `Blocked until earlier gates pass.` (verified by `grep -n "Status:" ROADMAP.md`).

**No new field report referenced as existing.** `reports/field-report-03-construct-evaluation.md` is referenced only as `future` (R3 §Next action: "Produce"; R3 §Owning files: "future"). `reports/field-report-02-friend-pre-pilot.md` is referenced as an existing stub awaiting data — which it is, verified by `ls reports/` and `head -20 reports/field-report-02-friend-pre-pilot.md` (the file states "This is a template. The friend pre-pilot has not happened yet.").

**AC3 met.**

## Self-check

Re-read `git show a7684f1` looking for mistakes.

**Mistake check 1 — did the R3 patch accidentally leave any `field-report-02` reference inside R3?** No. `grep -A1 "## Phase R3" ROADMAP.md | grep "field-report-0"` returns only `-03-construct-evaluation`. R3 is clean.

**Mistake check 2 — did the R5 patch accidentally introduce a `field-report-03` reference inside R5?** No. Same check applied to R5 returns only `-02-friend-pre-pilot`. R5 is clean.

**Mistake check 3 — did the R5 §Owning files edit overreach?** The pre-patch text said "future field-report-02 (friend pre-pilot)". The post-patch text says "[`reports/field-report-02-friend-pre-pilot.md`](reports/field-report-02-friend-pre-pilot.md) (stub; awaiting data)." This changes "future" → "stub; awaiting data" because the stub file does exist on disk. Three sub-mistakes to check:

- *Does the link target resolve?* `ls reports/field-report-02-friend-pre-pilot.md` succeeds. Link works.
- *Does "stub; awaiting data" overclaim?* The stub is a template (`head -20` shows "This is a template. The friend pre-pilot has not happened yet."). "Stub" is the accurate noun; "awaiting data" matches "not started" semantically. No overclaim — the stub explicitly self-identifies as awaiting data.
- *Does this drift across the §Non-goals boundary "Editing R5 §Goal / §Gate substance beyond the naming touch"?* The change is to §Owning files, not §Goal or §Gate. The §Gate edit (L83) is a *naming touch* (changed `field-report-02` → `` `field-report-02-friend-pre-pilot` ``) and nothing else. The §Owning files edit (L87) replaces a "future" parenthetical with an explicit existing-stub citation — adjacent to the naming touch and grounded in the filesystem state the issue body §Source of truth instructed α to verify. Net: justified, scoped, traceable.

**Mistake check 4 — naming convention drift?** Existing reports use the pattern `field-report-NN-content-suffix.md` (`00-plan`, `01-existing-data-zeroth-pilot`, `02-friend-pre-pilot`). The new R3 future report `03-construct-evaluation` fits the same pattern (NN + content-suffix). No new convention introduced; the existing convention is extended by one slot.

**Mistake check 5 — does the scheme decision pass the reader test from the issue body?** Issue body §Proof plan §Negative case: "re-reading R3 + R5 in isolation does not give a reader the impression they are reading about the same future report." Verified by reading R3 §Next action ("`field-report-03-construct-evaluation`") and R5 §Gate ("`field-report-02-friend-pre-pilot`") in isolation: distinct identifier numbers, distinct content suffixes, distinct subject matter (construct evaluation vs friend pre-pilot). A skim-reader sees they are different reports.

**Ambiguity passed to β:**
- The R5 §Owning files phrasing change ("future" → "stub; awaiting data") is slightly outside the literal naming-touch scope. β may want this reverted to "future `reports/field-report-02-friend-pre-pilot.md`." which would also be valid (the stub file exists but contains no data, so "future" is defensible). Fix is a one-line revert if β prefers it.

## Debt

1. **R5 §Owning files phrasing call.** Disclosed above. The change from "future field-report-02 (friend pre-pilot)" to "[`reports/field-report-02-friend-pre-pilot.md`](reports/field-report-02-friend-pre-pilot.md) (stub; awaiting data)" introduces a small accuracy improvement that is adjacent to (not strictly within) the AC1/AC2 naming-touch scope. If β reads this as overreach, the revert is one line.

2. **Identifier-numbering convention is not yet documented.** The issue body §Source of truth row ("Field-report numbering convention: not yet documented (the gap)") still resolves to "not documented" — Sub B picks a convention (time-of-publication + content-suffix) and applies it, but does not document it as a repo-wide rule. A follow-on cycle could land a one-paragraph convention note (e.g., in `reports/README.md` if one exists, or in a `reports/CONVENTIONS.md`). Out of scope for Sub B per issue body §Non-goals ("Writing field-report-02 (or -03, or any new report)"). Named here so β's review surfaces the gap.

3. **`reports/field-report-02-friend-pre-pilot.md` stub will need editing before R5 ships.** The stub's H1 is `# Field Report 01 Friend Pre Pilot` (verified by `head -1 reports/field-report-02-friend-pre-pilot.md`). The filename says `02` but the H1 says `01`. This is pre-existing drift inside the stub itself; Sub B's §Non-goals forbids editing existing field reports, so the H1/filename mismatch is named here as wave-scoped debt. A future R5 cycle that fills in the stub data will correct the H1 in the same edit.

## CDD-Trace

Per `cdd/alpha/SKILL.md` §2.2 canonical artifact order.

1. **Design** — *not required as a separate artifact.* The design space (3 schemes: (a) renumber R3→02 R5→03, (b) content-suffix names, (c) any operator scheme) is enumerated in the issue body. Filesystem check (`ls reports/`) resolved the choice: scheme (b) is half-implemented (the R5 stub exists with content suffix), so extend it. Decision rationale is captured in §Gap.
2. **Coherence contract** — §Gap above. The contract: no identifier collision; scheme is internally consistent across R3 + R5; existing on-disk stub state respected; no empirical drift.
3. **Plan** — *not required.* Four-line patch with predetermined edits.
4. **Tests** — AC oracles pasted in §ACs (the `grep -nE "field-report-0[0-9]"` oracle from the issue body, plus identifier-accounting table, plus the reader-test re-read).
5. **Code** — *not applicable.* Docs-only.
6. **Docs** — `ROADMAP.md` four-line edit. `git diff --stat dcd0d50..a7684f1 -- ROADMAP.md` returns `ROADMAP.md | 8 ++++----`. Net 4 insertions + 4 deletions (one per touched line).
7. **Self-coherence** — this file.

**Step-by-step ledger for Sub B:**

| # | Step | Evidence |
|---|---|---|
| 1 | Read sub-issue body via mcp | `mcp__github__issue_read(18)` — confirmed scope, 4 lines, scheme decision required |
| 2 | Filesystem source-of-truth check | `ls reports/` → `field-report-02-friend-pre-pilot.md` exists; scheme (b) already half-implemented |
| 3 | Stub content check | `head -20 reports/field-report-02-friend-pre-pilot.md` → "This is a template. The friend pre-pilot has not happened yet." |
| 4 | Scheme decision | R5 keeps `-02-friend-pre-pilot`; R3 takes `-03-construct-evaluation` |
| 5 | Patch ROADMAP.md L66, L67, L83, L87 | Four `Edit` tool calls |
| 6 | AC1 oracle | `grep -nE "field-report-0[0-9]" ROADMAP.md` → 12 hits across 3 distinct identifiers, each mapping to one report |
| 7 | AC2 consistency check | R3 references use `-03-construct-evaluation` (2 lines); R5 references use `-02-friend-pre-pilot` (2 lines); zero cross-references |
| 8 | AC3 drift check | `git show a7684f1 --stat` → 1 file 4+/4-; no Status: field, no README touch |
| 9 | Implementation commit | `a7684f1 α #18: rename R3's field-report-02 → field-report-03-construct-evaluation (F2)` |
| 10 | Self-coherence write | this file |
| 11 | Self-coherence commit | (next: `α #18: self-coherence`) |
| 12 | Push | (next: `git push origin claude/review-repo-coherence-PNbjQ`) |

## Review-readiness

**Round:** 1.
**Base SHA for this sub:** `7893ee9` (HEAD before Sub B implementation; previous sub's self-coherence commit).
**Implementation SHA:** `a7684f1` (α Sub B implementation; stable).
**Branch CI:** N/A (no CI configured).
**Author email:** `alpha@cph.cdd.cnos` on `a7684f1` (verified `git log --format='%ae' -1 a7684f1`).

**Pre-review gate row-by-row:**

| # | Row | Status | Evidence |
|---|---|---|---|
| 1 | Branch rebased | ✅ | Working branch is the dispatch branch; Sub B sits on top of Sub A's self-coherence commit |
| 2 | CDD Trace through step 7 | ✅ | §CDD-Trace |
| 3 | Tests present or "none apply" | ✅ | AC1 oracle inline; identifier-accounting table; AC2 split-grep; AC3 git-show |
| 4 | Every AC has evidence | ✅ | AC1 (12-hit grep + table); AC2 (split-grep + reader test); AC3 (stat + Status: invariance) |
| 5 | Known debt explicit | ✅ | §Debt enumerates 3 items |
| 6 | Schema/shape audit | N/A | docs-only |
| 7 | Peer enumeration | ✅ | All 3 distinct future-report identifiers enumerated in AC1 table; all 4 touched lines enumerated in §Gap net-edits table |
| 8 | Harness audit | N/A | no harness |
| 9 | Post-patch re-audit | N/A | single-pass round 1 |
| 10 | Branch CI green | N/A | no CI |
| 11 | Artifact enumeration matches diff | ✅ | `git diff --stat 7893ee9..a7684f1` → `ROADMAP.md \| 8 ++++----`; one file, named in §CDD-Trace step 6 |
| 12 | Caller-path trace | N/A | docs-only |
| 13 | Test assertion count | N/A | grep oracles inline |
| 14 | α commit author email canonical | ✅ | `a7684f1` author = `alpha@cph.cdd.cnos` |

**Verdict:** ready for β review (round 1).
