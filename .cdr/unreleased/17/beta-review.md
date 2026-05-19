# β review — Sub A — cph#17 — F1 + F6

## Round 1

**Verdict:** APPROVE

**Round:** 1
**Wave:** `.cdd/waves/coherence-drift-sweep-2026-05-18/`
**Master:** usurobor/cph#16
**Sub:** usurobor/cph#17
**Base SHA (wave-open):** `dcd0d50` (δ wave-open on `claude/review-repo-coherence-PNbjQ`)
**Implementation SHA:** `72c3845` (α impl)
**Self-coherence SHA:** `7893ee9` (α self-coherence)
**Intermediate δ commit:** `91fd2e5` (`.gitignore` for `.claude/`; δ-authored; does not touch Sub A surface — corroborates α §Debt 2)
**Branch CI state:** N/A (no `.github/workflows/` in repo; wave manifest §"Known constraints" names `coh not on PATH`)
**Branching:** single-branch dispatch on `claude/review-repo-coherence-PNbjQ` per wave manifest §"Branching deviation"

## Identity-audit

| Commit | Expected author | Observed | Pass |
|---|---|---|---|
| `72c3845` (impl) | `alpha@cph.cdd.cnos` | `α-as-agent <alpha@cph.cdd.cnos>` | ✓ |
| `7893ee9` (self-coherence) | `alpha@cph.cdd.cnos` | `α-as-agent <alpha@cph.cdd.cnos>` | ✓ |
| this review commit | `beta@cph.cdd.cnos` | will be authored as `β-as-agent <beta@cph.cdd.cnos>` per dispatcher's identity contract | ✓ (pre-commit) |
| `91fd2e5` (intermediate) | δ-side scaffolding | `δ-as-agent <delta@cph.cdd.cnos>` | not an α/β surface — accepted |

Identity-isolation invariant (α ≠ β within Sub A) preserved.

## AC-by-AC

### AC1 — F1 closed

**Oracle 1 (negative, dispatcher's prompt):** `grep -rn "05-friends-are-not-validation" .` excluding `.cdd/`, `.git/`, `.claude/`.

```
$ grep -rn "05-friends-are-not-validation" . --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude
(no output; exit 1)
```

Zero live-tree matches. β also ran the broader form (only excluding `.git` and `.claude`) — the remaining matches are entirely inside α's own `.cdd/unreleased/17/self-coherence.md` (historical references in the §Gap / §ACs / §CDD-Trace prose), which the AC1 carve-out explicitly excludes. Issue body AC1 first bullet says "excluding `.cdd/**` historical artifacts and this issue body" — both carve-outs honored.

**Oracle 2 (positive, dispatcher's prompt):** `grep -n "04-friends-are-a-pre-pilot" ROADMAP.md`.

```
$ grep -n "04-friends-are-a-pre-pilot" ROADMAP.md
85:- **Coherence risk:** Friend data is read as validation of the hypothesis rather than as a pipeline-robustness test (the realization the project owns as [`docs/realizations/04-friends-are-a-pre-pilot.md`](docs/realizations/04-friends-are-a-pre-pilot.md)). ...
```

Hit at L85 inside R5 §Coherence risk, exactly where issue body §Scope said the edit lands.

**Oracle 3 (target-file existence):** `ls docs/realizations/` → `04-friends-are-a-pre-pilot.md` is the 4th entry of a 5-realization peer set (`01-walking-is-not-a-style.md`, `02-the-type-list-is-not-the-object.md`, `03-opencap-is-the-translation-layer.md`, `04-friends-are-a-pre-pilot.md`, `05-what-broke.md`). The link target resolves. The substantive ownership (friends-as-pre-pilot, not validation) was independently spot-checked by reading `docs/realizations/04-friends-are-a-pre-pilot.md` §Decision — α's substantive-match claim holds.

**Verdict:** AC1 met.

### AC2 — F6 closed

**Sub-clause (a) — closed master no longer cited as pending gate:**

```
$ grep -nE "pending the close of master" PROJECT.md
(no output; exit 1)
```

The phrase "pending the close of master" is gone. PROJECT.md still cites cph#11 at L34 (§"Active branch / issue") and L35 (in-flight wave reference text), but neither cite is a *pending-gate* claim — L34 reads "open until A+B+C+D close" (factual wave statement), L35 enumerates sub-issue merge states. Neither says R0 is gated on cph#11. β confirmed by visual inspection of `sed -n '14,20p' PROJECT.md`:

```
**R1 — Existing-data zeroth pilot.** R0 (charter and operationalization) is ACTIVE pending the first numeric C_Σ baseline against this branch (the [`scripts/measure-coherence.sh`](scripts/measure-coherence.sh) entrypoint runs once `coh` is on PATH in an operator environment — see §"Last coherence measurement" below); R2–R6 are gated behind R1 and R2. See [`ROADMAP.md`](ROADMAP.md) for each phase's gate and status.
```

The pending-gate clause now names the first numeric C_Σ baseline. Status word "ACTIVE" preserved verbatim (dispatch constraint: status word unchanged until `coh` runs).

**Sub-clause (b) — "wording matches ROADMAP.md §Phase R0 §Next action":**

β read ROADMAP.md R0 §Next action (L36):

```
- **Next action:** Sub B (this), Sub C, Sub D merge; wave [`cdr-refactor-2026-05-18`](...) closes; phase transitions to GO at wave close.
```

The ROADMAP wording references *the prior wave's* close (`cdr-refactor-2026-05-18`). That wave closed 2026-05-18 (per `42466ad ε wave-iteration` and `0d042d4 δ wave close-out` in git log). So ROADMAP R0 §Next action is *itself one transition behind state* — it names a gate that has already passed.

α chose the substantive read (PROJECT.md should name the *actual* outstanding gate, which is the first numeric C_Σ baseline) rather than the literal-mirror read (PROJECT.md should copy ROADMAP's stale wording verbatim). α disclosed this in §ACs AC2 (alignment note) and §Debt item 1.

β endorses the substantive read for three reasons:
1. F6 is explicitly framed in the issue body §Problem as "PROJECT.md wording is one transition behind state." A literal-mirror to a *second* stale source would inherit the same defect F6 is fixing — fix-by-isomorphism with the broken thing.
2. The substantive outstanding gate (first numeric C_Σ baseline / `coh` first-run) is the same gate the wave manifest itself names in §"Standing permissions" (`coh` not on PATH → best-effort) and §"Out-of-scope follow-ups" first bullet. The wave's own contract treats this as the next gate.
3. Sub A §Non-goals forbids editing other ROADMAP phases — so α could not have fixed ROADMAP R0 §Next action even if α had wanted to. The literal-mirror reading is structurally impossible inside Sub A's scope without scope violation.

The follow-on cycle that refreshes ROADMAP R0 §Next action will produce full re-alignment; the staleness is named as cross-sub debt for the wave-closeout.

**Verdict:** AC2 met (substantive reading endorsed; literal-mirror reading would have required out-of-scope ROADMAP edit).

### AC3 — No empirical drift

**Surface check (files touched):**

```
$ git diff --name-only dcd0d50..72c3845
PROJECT.md
ROADMAP.md
```

Two files, both expected per wave manifest §"Issues" table for Sub A.

**Status-field check:**

```
$ git show 72c3845 -- ROADMAP.md | grep -E "^[+-].*Status:"
(no output; exit 1)
```

No `Status:` field touched in the diff.

**README check:**

```
$ git show 72c3845 -- README.md
(empty)
```

README untouched.

**REVISE posture check:** β read PROJECT.md §"Current empirical decision" (L20) at HEAD:

```
**REVISE** (2026-05-17 real-data run, per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md)). ...
```

REVISE posture intact. Cites `field-report-01-existing-data-zeroth-pilot.md` (2026-05-17), which is the report wave manifest §"Known constraints" first bullet names as governing.

**Verdict:** AC3 met.

## Notes

**N1 (α flag 1 — ROADMAP R0 §Next action staleness).** α self-named this in §Debt 1. β endorses naming it as wave-scoped debt rather than a Sub A defect — fixing it would require editing a ROADMAP phase that Sub A's §Non-goals explicitly excludes, so it's structurally out-of-scope for cph#17. β surfaces this for δ's wave-closeout under §Cross-sub debt below.

**N2 (intermediate δ commit `91fd2e5`).** Between α's impl (`72c3845`) and α's self-coherence (`7893ee9`), δ added `.claude/` to `.gitignore`. β verified `git show 91fd2e5` is δ-authored (`delta@cph.cdd.cnos`) and touches `.gitignore` only — not the Sub A surface. Not an α-identity violation, not a Sub A scope expansion. α correctly named this in §Debt 2.

**N3 (citation style upgrade in ROADMAP.md L85).** The original parenthetical cited the (broken) filename as bare inline code (`` `05-friends-are-not-validation.md` ``). The new parenthetical uses a markdown link with both the code-styled filename *and* the link target (`` [`docs/realizations/04-friends-are-a-pre-pilot.md`](docs/realizations/04-friends-are-a-pre-pilot.md) ``). This is a small surface-quality improvement (clickable cite), matches ROADMAP's prevailing citation style (e.g., L37 cites `[`scripts/measure-coherence.sh`](scripts/measure-coherence.sh)` the same way), and does not change the AC1 verdict. β notes it as a clean read, not a finding.

**N4 (PROJECT.md L16 sentence-shape preservation).** The patch preserves the original sentence's subject-status-pending-gate-clause shape, swapping only the pending-gate clause. Status word "ACTIVE" survives verbatim. The remainder ("; R2–R6 are gated behind R1 and R2. See `ROADMAP.md`...") is byte-for-byte identical. β verified by `git show 72c3845 -- PROJECT.md`. No collateral prose drift.

**N5 (self-coherence ordering, α §Debt 3).** α disclosed that the implementation commit (`72c3845`, 23:02:12 UTC) preceded the self-coherence write by ~12 minutes (resumed earlier session). β re-ran all AC oracles at HEAD independently; the §AC evidence reproduces from the diff and is not memory-of-prior-session-dependent. Disclosure-level item, not a defect.

## Scope-drift check

| Surface | Expected per wave manifest §"Issues" | Touched in diff? |
|---|---|---|
| `ROADMAP.md` (one-line edit at L85) | yes | yes (L85, R5 §Coherence risk parenthetical citation) |
| `PROJECT.md` (§"Current stage" wording) | yes | yes (L16, pending-gate clause) |
| `README.md` | no | no |
| `CDR.md` | no | no |
| `docs/realizations/*.md` | no (issue body §Non-goals: "Editing realization content") | no |
| Other ROADMAP phases | no (issue body §Non-goals: "Editing other ROADMAP phases") | no |
| `analysis/*`, `scripts/*`, `notebooks/*` | no (other subs' surfaces) | no |

No scope-drift. α stayed inside Sub A's surface exactly.

## Cross-sub debt (for δ wave-closeout)

1. **ROADMAP R0 §Next action staleness.** L36 names `cdr-refactor-2026-05-18` wave close as the pending gate, but that wave closed 2026-05-18. PROJECT.md L16 (post-Sub-A) and ROADMAP R0 §Next action no longer mirror each other on the substantive gate. A follow-on cycle outside this wave's scope should refresh ROADMAP R0 §Next action to point at the first numeric C_Σ baseline; PROJECT.md will then mirror ROADMAP literally. Named in α §Debt 1 and the dispatcher prompt's "α flagged for verification" item 1.

2. **`91fd2e5` intermediate δ commit.** Wave-scoped scaffolding (`.gitignore` `.claude/`); not an α/β surface; named for δ's wave-closeout audit trail completeness.

## Round 1 close

AC1 / AC2 / AC3 all met under independent β re-run. No scope-drift. No identity-isolation breach. Sub A APPROVE.
