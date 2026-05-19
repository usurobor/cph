# β review — Sub B — cph#23 — F8 + F9 PROJECT.md §Active branch + ROADMAP.md R0 de-staling

## Round 1

**Verdict:** APPROVE

**Round:** 1
**Wave:** `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/`
**Master:** usurobor/cph#21
**Sub:** usurobor/cph#23
**Base SHA (Sub B parent):** `3bc4242` (Sub A self-coherence commit)
**Implementation SHA:** `c3e0ee8`
**Self-coherence SHA:** `b4ac08d`
**Branch CI state:** N/A (no `.github/workflows/`)
**Branching:** single-branch dispatch on `claude/review-repo-coherence-PNbjQ` per wave manifest §"Branching deviation"

## Identity-audit

| Commit | Expected author | Observed | Pass |
|---|---|---|---|
| `c3e0ee8` (impl) | `α-as-agent <alpha@cph.cdd.cnos>` | `α-as-agent <alpha@cph.cdd.cnos>` | ✓ |
| `b4ac08d` (self-coherence) | `α-as-agent <alpha@cph.cdd.cnos>` | `α-as-agent <alpha@cph.cdd.cnos>` | ✓ |
| this review commit | `β-as-agent <beta@cph.cdd.cnos>` | will be authored as `β-as-agent <beta@cph.cdd.cnos>` | ✓ (pre-commit) |

Identity-isolation invariant (α ≠ β within Sub B) preserved.

## AC-by-AC

### AC1 — PROJECT.md §"Active branch / issue" describes the live state

**β-side oracle (re-run):**

```text
$ grep -nE 'cph#1[12345]' PROJECT.md
(no matches)
```

Empty. No in-flight-state assertion of cph#11, cph#12, cph#13, cph#14, or cph#15 anywhere in PROJECT.md. The section §"Active branch / issue" no longer names the closed cdr-refactor wave's master or subs as in-flight.

**β-side direct read of the post-patch section (L32–38):**

```text
$ sed -n '32,38p' PROJECT.md
## Active branch / issue

- **Review branch:** `claude/review-repo-coherence-PNbjQ` — review surface for two coherence-drift-sweep waves landed against R0 (`cdr-refactor-2026-05-18` is closed; `coherence-drift-sweep-2026-05-18` and the follow-up `coherence-drift-sweep-followup-2026-05-18` are reviewing here). Merge to main is an operator gate per each wave's manifest §"Branching deviation".
- **In-flight waves on the review branch:**
  - [`coherence-drift-sweep-2026-05-18`](.cdd/waves/coherence-drift-sweep-2026-05-18/manifest.md) — master [cph#16](https://github.com/usurobor/cph/issues/16); all four subs (cph#17–20) closed APPROVE; master close is an ε/operator gate.
  - [`coherence-drift-sweep-followup-2026-05-18`](.cdd/waves/coherence-drift-sweep-followup-2026-05-18/manifest.md) — master [cph#21](https://github.com/usurobor/cph/issues/21); four subs (cph#22–25) in flight on this branch.
- **Unmerged orthogonal branch:** `origin/cycle/segmentation-real-data-fix` (tip `a95415c`) — R2 segmentation fix; merge is a separate operator decision per the precursor cdr-refactor wave's manifest.
```

Three bullets describing live state. Header §"Active branch / issue" preserved (b-1 direction). The closed-wave reference `cdr-refactor-2026-05-18` appears once in the first bullet's parenthetical, explicitly labeled "closed" — that's factual historical statement, not an in-flight assertion. The cph#16 and cph#21 references are correctly named as live state (master close = ε gate, four subs in flight respectively). cph#17–20 are named as "closed APPROVE" — also factual closed-state, not in-flight. The grep regex `cph#1[12345]` does not match cph#16, cph#17, cph#20, cph#21, cph#22, etc. — it matches only `cph#11–15`. None appear in PROJECT.md (post-patch).

**β-side cross-check of live facts named:**

| Claim in post-patch §"Active branch / issue" | Verification |
|---|---|
| Review branch is `claude/review-repo-coherence-PNbjQ` | ✓ `git branch --show-current` returns `claude/review-repo-coherence-PNbjQ` |
| cdr-refactor wave is closed | ✓ per issue body §"Source of truth"; cph#11 closed 2026-05-18 16:35 |
| Precursor `coherence-drift-sweep-2026-05-18` has subs cph#17–20 closed APPROVE | ✓ `git log --format='%s' -30` shows `β #17/18/19/20: review APPROVE + close-out` |
| Master close on cph#16 is an ε/operator gate | ✓ matches wave manifest §"Branching deviation" pattern |
| Follow-up wave (this one) has subs cph#22–25 | ✓ wave manifest §Issues table; β is currently reviewing these |
| Segmentation branch tip `a95415c` | preserved verbatim from pre-patch text; not a new claim |

**Verdict:** AC1 met.

### AC2 — ROADMAP R0 §"Next action" no longer names `cdr-refactor-2026-05-18` as gate

**β-side oracle (re-run):**

```text
$ grep -n 'cdr-refactor-2026-05-18' ROADMAP.md
(no matches)
```

Empty. No `cdr-refactor-2026-05-18` references anywhere in ROADMAP.md post-patch.

**β-side direct read of post-patch R0 §"Next action" (L36):**

```text
$ sed -n '36p' ROADMAP.md
- **Next action:** Land the first numeric C_Σ baseline against this branch via [`scripts/measure-coherence.sh`](scripts/measure-coherence.sh), gated on `coh` being on PATH in an operator environment (per [`CHANGELOG.md`](CHANGELOG.md) 0.1.0-cdr §"Deferred items"). The mechanical entrypoint is in place; the baseline lands the first time `coh --mode mechanical` runs against this branch and gets recorded in `CHANGELOG.md`. Phase transitions to GO at that recording.
```

The new §"Next action" describes the actually-outstanding gate (first C_Σ baseline, gated on `coh` PATH availability). This matches:
- `PROJECT.md:44` "The mechanical entrypoint `scripts/measure-coherence.sh` is in place; the first numeric C_Σ baseline lands the first time `coh` runs against this branch (or a successor)." (live state, unchanged)
- `CHANGELOG.md` 0.1.0-cdr §"Deferred items" naming `coh` PATH availability as the gating constraint (β spot-checked via `grep -n 'Deferred items' CHANGELOG.md` — present)
- Wave manifest §"Known constraints" 4th bullet: "`coh` not on PATH. No mechanical TSC measurement is run during or after this wave."

**Verdict:** AC2 met.

### AC3 — ROADMAP R0 §"Owning files" carries no `(pending Sub C)` qualifiers

**β-side oracle (re-run):**

```text
$ grep -n '(pending Sub C)' ROADMAP.md
(no matches)
```

Empty. All three `(pending Sub C)` qualifiers stripped.

**β-side direct read of post-patch R0 §"Owning files" (L37):**

```text
$ sed -n '37p' ROADMAP.md
- **Owning files:** [`README.md`](README.md), [`CDR.md`](CDR.md), [`docs/concepts/coherence-path-hypothesis.md`](docs/concepts/coherence-path-hypothesis.md), [`docs/concepts/support-path.md`](docs/concepts/support-path.md), [`docs/concepts/failure-conditions.md`](docs/concepts/failure-conditions.md), [`docs/articles/seven-ways-people-walk.md`](docs/articles/seven-ways-people-walk.md), `ROADMAP.md` (this), [`PROJECT.md`](PROJECT.md), [`CHANGELOG.md`](CHANGELOG.md), `targets/*.tsc`, [`scripts/measure-coherence.sh`](scripts/measure-coherence.sh).
```

`CHANGELOG.md`, `targets/*.tsc`, `scripts/measure-coherence.sh` all listed without qualifier. `CHANGELOG.md` and `scripts/measure-coherence.sh` now have markdown-link wrapping consistent with the rest of the list; `targets/*.tsc` stays unlinked (it's a glob, not a single file).

**Verdict:** AC3 met.

### AC4 — No empirical drift

**β-side oracle (re-run):**

```text
$ git show c3e0ee8 -- README.md CHANGELOG.md reports/
(empty)
```

No README / CHANGELOG / reports/ touch.

**REVISE posture check:**

```text
$ grep -n REVISE PROJECT.md | head -2
20:**REVISE** (2026-05-17 real-data run, per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md)). ...
42:[`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) — 2026-05-17 real-data run ...
```

PROJECT.md §"Current empirical decision" L20 still REVISE, citing field-report-01 (2026-05-17). No new field report (no new file under `reports/` from the impl diff).

**R0 §Status check:**

```text
$ grep -n 'Status:' ROADMAP.md | head -3
34:- **Status:** ACTIVE.
44:- **Status:** REVISE.
54:- **Status:** REVISE.
```

R0 status remains `ACTIVE` (L34). Issue body L75 prescribes status stays `ACTIVE` until the gate (first C_Σ baseline) closes; α did not transition the status. ✓.

**Verdict:** AC4 met.

### AC5 — Surface scope held

**β-side oracle (re-run):**

```text
$ git show c3e0ee8 --stat
commit c3e0ee80bdb776e60420e2c1e1f24a1d820f07fd
Author: α-as-agent <alpha@cph.cdd.cnos>
Date:   Tue May 19 02:50:19 2026 +0000

    α #23: de-stale PROJECT.md §Active branch + ROADMAP.md R0 §Next action (F8 + F9)

 PROJECT.md | 8 +++++---
 ROADMAP.md | 4 ++--
 2 files changed, 7 insertions(+), 5 deletions(-)
```

Exactly two files. PROJECT.md and ROADMAP.md. No other file touched.

**Hunk-localization spot check:**

```text
$ git diff c3e0ee8~1 c3e0ee8 -- PROJECT.md | grep '^@@'
@@ -32,5 +32,7 @@ Held in scope: no friend captures, no clustering, no new empirical claims. See [`ROADMAP.md`](ROADMAP.md) §"Phase R5" and §"Phase R6" for why those are blocked.
```

Single hunk at L32–36 → L32–38 (§"Active branch / issue" block). No other section touched.

```text
$ git diff c3e0ee8~1 c3e0ee8 -- ROADMAP.md | grep '^@@'
@@ -36,2 +36,2 @@ ...
```

Single hunk at L36–37 (R0 §Next action + §Owning files). R1–R6 untouched.

**Verdict:** AC5 met.

## Notes

**N1 (b-1 direction defensible).** α picked direction b-1 (keep §"Active branch / issue" with live-state content). β concurs: dropping the section (b-2) would lose useful pointers (review branch identity, in-flight wave list, unmerged segmentation branch) that PROJECT.md's contract treats as a status-bearing surface. The chosen direction is more informative than b-2.

**N2 (link wrapping in R0 §Owning files).** α's mistake-check 5 names the link-wrapping addition on `CHANGELOG.md` and `scripts/measure-coherence.sh` as not strictly required by AC3. β reads: the wrapping restores style consistency with the rest of the list (which already linked README.md, CDR.md, etc.) and adds zero ambiguity. Accept.

**N3 (segmentation branch tip `a95415c`).** Preserved verbatim from pre-patch text. β did not re-verify the tip SHA — it's not in this sub's scope and the segmentation branch lives outside the review branch's history. If the tip has advanced since the pre-patch text was written, that's a separate finding for a future cycle, not Sub B.

**N4 (parenthetical "closed" in first bullet).** The post-patch first bullet's parenthetical says "`cdr-refactor-2026-05-18` is closed; ...". The AC1 regex `cph#1[12345]` does not match `cdr-refactor-2026-05-18` (no `cph#` in the wave name). The mention is factual historical state, not an in-flight assertion. β reads as acceptable: it clarifies what the review branch's history holds.

## Scope-drift check

| Surface | Expected per wave manifest §"Issues" + cph#23 §Scope | Touched in diff? |
|---|---|---|
| `PROJECT.md` §"Active branch / issue" L32–36 (now L32–38) | yes | yes (single hunk) |
| `PROJECT.md` §"Current stage" L16 | no (cph#17 surface) | no |
| `PROJECT.md` §"Current empirical decision" L20 | no | no |
| `PROJECT.md` §"Current blocker", §"Next action", §"Last field report", §"Last coherence measurement" | no | no |
| `ROADMAP.md` R0 §"Next action" L36 | yes | yes |
| `ROADMAP.md` R0 §"Owning files" L37 | yes | yes |
| `ROADMAP.md` R0 §Status L34 | no (per issue body L75: status stays ACTIVE) | no |
| `ROADMAP.md` R1–R6 | no | no |
| README / CHANGELOG / reports/ | no | no |
| `targets/*.tsc` / `scripts/measure-coherence.sh` | no | no |
| `.cdd/**` historical artifacts | no | no |

No scope-drift. Two-file impl-diff exactly matches the wave manifest §"File-disjointness check" §Sub B prediction.

## Cross-sub debt (for δ wave-closeout)

1. **F12 (CHANGELOG entry for the precursor wave) — policy decision for ε/operator.** Named in cph#21 §F12, wave manifest §"Out-of-scope follow-ups", and α §Debt 1. δ recommends ε land a CHANGELOG entry for `coherence-drift-sweep-2026-05-18` in the wave-closeout §"Cross-sub findings". Sub B did not land this (out of scope).

2. **Master cph#16 and cph#21 closure are both ε/operator gates.** PROJECT.md now names this state; the actual close is not in α's authority. α §Debt 2; β concurs.

3. **`coh` not on PATH — first numeric C_Σ baseline still deferred.** R0 §"Next action" now names the gate explicitly. Same deferred item the cph#11 / cph#16 waves named. α §Debt 3; β concurs.

4. **Carry-over: field-report-02 stub H1 mismatch** (this wave's Sub C / cph#24; α §Debt 4 cross-sub trace).

5. **Carry-over: `extract_shape` always-`True` placeholder** (this wave's Sub D / cph#25; α §Debt 5 cross-sub trace).

## Round 1 close

AC1 (PROJECT.md §"Active branch / issue" no longer asserts cph#11–15 in-flight; live-state text correctly names review branch + two in-flight waves + unmerged segmentation branch), AC2 (R0 §"Next action" names the actually-outstanding C_Σ baseline gate, no `cdr-refactor-2026-05-18` mention anywhere in ROADMAP.md), AC3 (no `(pending Sub C)` strings in ROADMAP.md), AC4 (zero touches to README/CHANGELOG/reports; REVISE posture intact at PROJECT.md L20; R0 §Status still ACTIVE per issue-body authorization), AC5 (exactly PROJECT.md + ROADMAP.md in diff, single hunk per file at expected line range) all met under independent β re-run. No scope-drift. No identity-isolation breach. Sub B APPROVE.
