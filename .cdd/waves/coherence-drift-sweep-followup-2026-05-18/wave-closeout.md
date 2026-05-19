# Wave Close-out: Coherence drift sweep follow-up (master cph#21)

**Wave:** `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/`
**Date opened:** 2026-05-18
**Date closed:** 2026-05-18 (same-day wave, like the precursor)
**Dispatcher:** δ-as-agent (γ=δ permitted at this scale per `cdd/operator/SKILL.md` §5.2)
**Master:** usurobor/cph#21 — *open* at wave close (master closure deferred to ε per the precedent set by `cdr-refactor-2026-05-18` §"Master closure" and `coherence-drift-sweep-2026-05-18` §"Master closure"; see §Master closure below)
**Configuration:** single-branch dispatch on `claude/review-repo-coherence-PNbjQ` via two paired `Agent` invocations (one α-session implementing all four subs serially; one β-session reviewing all four subs serially). Identity-isolation invariant preserved by Agent-session boundaries: α and β are independent context windows.

## Summary

Patched five coherence-drift findings (F7–F11) surfaced by the post-`coherence-drift-sweep-2026-05-18` re-audit on `claude/review-repo-coherence-PNbjQ`. F7 is the new HIGH-severity β-axis bug the precursor wave missed. F8–F11 are confirmed cross-sub debt items the precursor wave explicitly named as out-of-scope. F12 was held back from the wave as a policy decision for ε/operator. Wave was a four-sub split per the five-factor heuristic on master cph#21: F7 (Sub A, cph#22), F8+F9 (Sub B, cph#23), F11 (Sub C, cph#24), F10 (Sub D, cph#25). Every sub APPROVED round 1, zero β findings across the wave, zero fix-rounds.

The wave validates the structural fix that motivated it — **β-side code-first oracle anchoring on any AC of form "doc matches code"** — by closing F7 itself (the miss this discipline is designed to prevent) cleanly and using the same discipline on F10 (β's word-boundary regex chosen independently to discriminate `extract_shape_sentinel` from `extract_shape`). The discipline held cleanly on both Sub A AC1 and Sub D AC1; β surfaced one oracle-regex brittleness finding (the dispatcher-prompt regex `quality_flag\s*=\s*"` does not match a multi-line conditional and β widened to `quality_flag` β-side) as a candidate input for ε's `cdd-iteration.md` β-anchoring SKILL patch.

## Aggregate metrics

| Cycle | Mode | Findings | Rounds | α SHA (impl) | α SHA (self-coh) | β SHA (review+closeout) | Direction | Notes |
|---|---|---|---|---|---|---|---|---|
| #22 (Sub A) | docs + code | F7 | 1 (APPROVE) | `a697265` | `3bc4242` | `46be990` | a-1 | code emits `ok`/`short`/`long`; `low_contact_gap` deferred to §Quality-flag widening |
| #23 (Sub B) | docs-only | F8, F9 | 1 (APPROVE) | `c3e0ee8` | `b4ac08d` | `4465d63` | b-1 | PROJECT.md §Active branch rewritten as live-state block; R0 §Next action names C_Σ baseline gate |
| #24 (Sub C) | docs-only | F11 | 1 (APPROVE) | `b06acf6` | `d47a252` | `8a2fd1e` | — | One-line H1 fix; +1/-1 diff |
| #25 (Sub D) | docs + code | F10 | 1 (APPROVE) | `129530b` | `e752ef8` | `24b4335` | d-2 | `extract_shape` → `extract_shape_sentinel`; notebook untouched (transitive call via `extract_features`) |
| **Wave totals** | — | F7–F11 (five findings) | **4 × APPROVE round 1 / 0 RC** | — | — | — | — | — |

### Repository delta (origin/main: 2e503c9 → wave-closeout commit; wave-internal: 8981e96 → 24b4335)

- **21 files changed, +2,294 / −21** in the wave (8981e96^..24b4335).
- Of which:
  - `.cdd/unreleased/{22,23,24,25}/` cycle artifacts: 12 new files (`self-coherence.md` + `beta-review.md` + `beta-closeout.md` per sub).
  - `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/` wave artifacts: 3 new files (manifest, status, this close-out — close-out lands at this commit).
- **Non-`.cdd` delta:** 6 files changed, +21/-21 — small surgical patches:
  - `scripts/segmentation.py` (4 lines reshaped at L122–124 for the `Cycle(...)` constructor `quality_flag` literal)
  - `scripts/features.py` (4 lines — function name + call site renames)
  - `analysis/feature-table-schema.md` (16 lines reshaped for quality_flag rows + the `extract_shape_sentinel` reference)
  - `analysis/features.md` (8 lines reshaped for L27/L132/L137 quality_flag refs + L59 §Shape header)
  - `PROJECT.md` (8 lines reshaped for §Active branch / issue)
  - `ROADMAP.md` (4 lines reshaped for R0 §Next action + §Owning files)
  - `reports/field-report-02-friend-pre-pilot.md` (2 lines — H1 +1/-1)
- **No new top-level files. No new directories.** All non-`.cdd` touches are to existing files.

### Identity audit (commit-author roll-call)

- **α commits (8):** all `α-as-agent <alpha@cph.cdd.cnos>` — `a697265`, `3bc4242`, `c3e0ee8`, `b4ac08d`, `b06acf6`, `d47a252`, `129530b`, `e752ef8`.
- **β commits (4):** all `β-as-agent <beta@cph.cdd.cnos>` — `46be990`, `4465d63`, `8a2fd1e`, `24b4335`.
- **δ commits (1):** `δ-as-agent <delta@cph.cdd.cnos>` — `8981e96` (wave open). δ also authors this wave-closeout commit (next).
- **Identity-isolation invariant:** α ≠ β within every sub, held across the wave. No `git config` operations. No `--amend`. No `--no-verify`.

## Master cph#21 ACs — final state

| AC | Owner sub | Status |
|---|---|---|
| AC1 — F7 closed (quality_flag schema↔code alignment) | #22 | ✅ — direction (a-1); code emits `ok`/`short`/`long`; all doc surfaces match string-for-string |
| AC2 — F8 closed (PROJECT.md §Active branch describes live state) | #23 | ✅ — §Active branch / issue rewritten; no cph#11/14/15 in-flight references |
| AC3 — F9 closed (ROADMAP R0 §Next action and §Owning files de-staled) | #23 | ✅ — R0 §Next action names C_Σ baseline gate; `(pending Sub C)` qualifiers removed |
| AC4 — F10 closed (`extract_shape` renamed) | #25 | ✅ — direction (d-2): `extract_shape_sentinel`; schema doc + features.md updated |
| AC5 — F11 closed (field-report-02 H1 matches filename) | #24 | ✅ — one-line +1/-1 patch |
| AC6 — F12 resolved | — | ⭕ deferred to ε/operator per cph#21 §"Suggested sub-split" final paragraph; δ's recommendation in §"Cross-sub findings" item 4 |
| AC7 — No empirical drift | cross-cutting | ✅ — REVISE posture intact at PROJECT.md L20; no new field report; README unchanged across all four subs |
| AC8 — Identity discipline and β anchoring | cross-cutting | ✅ — all 13 wave commits use project-suffixed identities; α ≠ β within every sub; β code-first anchoring held cleanly on Sub A AC1 and Sub D AC1 |

7 of 8 master ACs met; AC6 (F12 policy) deferred to ε/operator by design per cph#21 §"Suggested sub-split". Empirical REVISE posture preserved per `reports/field-report-01-existing-data-zeroth-pilot.md`.

## Cross-sub findings & cycle iteration

The wave ran cleanly (4× APPROVE round 1; 0 β findings). β surfaced ten cross-sub debt items worth carrying forward for ε's wave-level review:

1. **`low_contact_gap` deferred under §Quality-flag widening** (Sub A α §Debt 1; β concurs). The schema's three-label vocabulary `ok`/`short`/`low_contact_gap` was reduced to `ok`/`short`/`long` because the segmenter can produce `"short"` (duration ≤ 0.5) and `"long"` (duration ≥ 1.8) from `duration` alone; `"low_contact_gap"` requires a contact-gap check the segmenter does not currently implement. Future cycle gated on inspecting heel-strike-to-heel-strike contact-gap structure (likely a swing-time or force-plate-onset signal). **Class:** out-of-scope follow-up; cleanly named in `analysis/features.md` §"Quality-flag widening".

2. **Boundary-notation cosmetic inconsistency between schema `(0.5, 1.8)` and features.md Python `<=` / `>=`** (Sub A α §Debt 2; β concurs). The schema uses set-theoretic open-interval notation; features.md uses Python comparison operators. Both are correct under their respective audiences; the consistency drift is cosmetic. **Class:** wave-internal cosmetic debt; named for transparency.

3. **AC1 regex-oracle phrasing brittleness `quality_flag\s*=\s*"`** (Sub A β N1; candidate for cdd-iteration.md). The dispatcher-prompt's specified AC1 oracle regex did not match `scripts/segmentation.py:122`'s multi-line conditional (`quality_flag=("short" if duration <= 0.5 / ...`). β β-side widened to `quality_flag` and recorded both grep outputs. The brittleness is a regex-craft issue, not a substantive AC failure. **Class:** `cdd-protocol-gap` candidate. **Action:** ε's `cdd-iteration.md` β-anchoring SKILL patch could note that AC1 oracles should specify a regex robust to both single-line and multi-line literal assignments, OR that β widens the regex β-side when the dispatcher-prompt form misses a real literal.

4. **F12 — CHANGELOG entry for the precursor `coherence-drift-sweep-2026-05-18` wave AND this `coherence-drift-sweep-followup-2026-05-18` wave** (named across all subs; cph#21 §"Suggested sub-split" final paragraph). cph#21 §F12 raises two readings: (a) waves that don't change empirical state need no CHANGELOG entry; tighten CDR doctrine accordingly; or (b) both coherence waves moved the repo's coherence surface and merit a `0.1.1-cdr` (precursor wave) plus a `0.1.2-cdr` (this wave) entry. **Class:** policy decision. **δ's recommendation:** (a) — the precursor wave's wave-closeout §"Wave-internal disconnect posture" and this wave's same section both already document the no-release-tag posture; the CDR `Changelog rule` is best read narrowly as "each meaningful *empirical* research wave gets an entry," and a one-line tightening of `CDR.md` §"Changelog rule" to that effect closes F12 without retroactive entries. ε/operator's call.

5. **Master cph#16 + cph#21 closure both ε/operator gates** (Sub B α §Debt 2; precedent inherited from `cdr-refactor-2026-05-18` and `coherence-drift-sweep-2026-05-18`). Both masters remain OPEN at wave close. δ's recommended closure comments are in the precursor wave-closeout §"Master closure" and this wave-closeout §"Master closure" (below). **Class:** standing authority bound. **Action:** ε reads both wave-closeouts, decides whether to close the masters or to surface wave-level findings that block closure.

6. **`coh` not on PATH; first numeric C_Σ baseline still deferred** (named across Subs B and D; precedent from cph#11 wave). The mechanical entrypoint `scripts/measure-coherence.sh` is in place; first numeric baseline lands when `coh` is on PATH in an operator environment. **Class:** out-of-scope follow-up carried verbatim from prior waves. **Action:** operator's call when the TSC CLI becomes available.

7. **Stub-body-remains-stub for `field-report-02`** (Sub C α §Debt 1; β concurs). Sub C fixed only the H1 number prefix; the stub's body remains a stub awaiting R5's actual field report. **Class:** orthogonal stub debt; resolves when R5's report ships per ROADMAP §"Phase R5".

8. **Sub C α §Debt 2 inaccuracy** (Sub C β N1, non-finding). α's self-coherence §Debt 2 lists `field-report-03-construct-evaluation.md` as if it exists; it is a future deliverable per ROADMAP R3 §"Next action". β flagged as non-finding cosmetic record-keeping; no patch. **Class:** β-noted record-keeping precision; not actionable.

9. **`normalized_curve_available` always-True column is unchanged debt** (Sub D α §Debt 1; β concurs; carry-over from precursor wave). The column's value is `True` for every row the function emits, carrying no information. Sub D was a rename-only patch; the column's content remains. Future cycle when real shape extraction is materialized must update both the schema doc and `features.md` in lock-step (Sub D α §Debt 2). **Class:** β-axis debt; eligible for a future wave when the operator stands up the per-cycle parquet pipeline.

10. **β-axis observation: F7 + F10 share the "name reads more than it means" class** (Sub D β cross-sub item 5). Both findings are about a literal/name promising more than the code delivers — `quality_flag="short"` was promised but never emitted (F7); `extract_shape` was named but only marked persistence (F10). The class is *name overpromise*. **Class:** `cdd-protocol-gap` candidate alongside item 3 above. **Action:** ε's potential `cdd/beta/SKILL.md` patch could name "name-overpromise" as a distinct β-axis class worth a checklist line — likely a single sentence under the existing β-axis review surface in `cdd/beta/SKILL.md`.

## Wave-internal disconnect posture

This wave **does not produce a release tag.** No version bump, no `RELEASE.md`, no `scripts/release.sh` invocation. The disconnect signal is the four α-implementation commits + four β-approval commits + this wave-closeout landing on `claude/review-repo-coherence-PNbjQ`. Per the wave manifest's standing permissions, tag/release is operator-gated and was explicitly NO at wave open; the wave honored that. This is the same posture the precursor `coherence-drift-sweep-2026-05-18` wave took; the F12 CHANGELOG-policy question (above, cross-sub debt item 4) is what governs whether either wave eventually gets a CHANGELOG entry.

The `.cdd/unreleased/{22,23,24,25}/` directories remain in `.cdd/unreleased/` — they do **not** move to `.cdd/releases/{X.Y.Z}/{N}/` at this wave's close because the cph repo has no release-cut for this wave. Future release work (if any) inherits these unreleased directories as part of its scope.

## Master closure

Master cph#21 remains **OPEN** at wave close. The wave manifest declared no automatic master-close action (consistent with the precedent set by `cdr-refactor-2026-05-18` and `coherence-drift-sweep-2026-05-18`). 7 of 8 ACs from cph#21 are met; AC6 (F12 policy) is deferred to ε/operator by design. All 4 subs are at β-APPROVE; the wave-closeout is on the dispatch branch. ε (or the operator) holds the master-close decision after wave-level review.

**Recommended closure comment for cph#21:** a one-comment summary linking to this wave-closeout, the per-sub commit pairs, and the four sub-issues; close with `Closes #21` ONLY if AC6 is also resolved (either by writing the CHANGELOG entry inline, or by closing with a "no CHANGELOG entry needed for purely qualitative cross-cut waves" decision plus a one-line `CDR.md` §"Changelog rule" tightening). If AC6 stays open, the master stays open. The same closure comment should reference the ten cross-sub debt items in §"Cross-sub findings" above so they survive master closure as named-debt, not silent-debt.

Precursor master **cph#16 also remains OPEN** at this wave's close. δ-as-agent of this wave did not exercise authority over cph#16 — that wave's master closure was deferred to ε per its own wave-closeout, and remains ε's gate.

## Out-of-scope follow-ups (named, not executed by this wave)

Carried forward from the wave manifest plus items surfaced by α/β during execution:

- **First mechanical `coh --mode mechanical` run** + recording the numeric α/β/γ/C_Σ baseline into `CHANGELOG.md` (still gated on `coh` being on PATH; same deferred item the cph#11, cph#16, and cph#21 waves have all named).
- **Restoration of `cycle/{N}` push permissions** on the cph harness (harness-side, not in this wave's scope; same deviation pattern as the precursor wave).
- **F12 — CHANGELOG entry policy** (cross-sub debt item 4 above); ε/operator call; δ recommends reading (a).
- **`low_contact_gap` segmenter expansion** (cross-sub debt item 1) — future cycle gated on segmenter inspecting contact-gap structure.
- **Real `extract_shape_sentinel` replacement** (cross-sub debt item 9) — future cycle when per-cycle parquet pipeline is materialized; both schema doc and features.md to update in lock-step (cross-sub debt item 2).
- **Master cph#16 closure** — still ε's gate; precursor wave-closeout names the recommended closure comment.
- **Master cph#21 closure** — ε's gate; this wave-closeout's §"Master closure" names the recommended closure comment.
- **`cdd/beta/SKILL.md` patch — β anchoring discipline + name-overpromise β-axis class** (cross-sub debt items 3 and 10 combined) — proposed in cph#21 §"Wave-level retrospective hook" and re-grounded here; ε's `cdd-iteration.md` entry.
- **AC1 oracle-regex brittleness** (cross-sub debt item 3) — likely folded into the same `cdd/beta/SKILL.md` / `cdd-iteration.md` patch above.
- **Notebook re-execution** to re-bake analytic outputs (operator-side; gated on data availability) — unchanged from precursor wave posture.
- **Body edit of master cph#21** (left as as-filed; sub-issue links live in cph#21 comments + this manifest).

## Dispatch infrastructure observations

Three infrastructure observations from this wave's δ-as-agent execution that may inform future waves:

1. **Single-branch dispatch + paired Agent sessions held cleanly for a second wave in succession.** Identity-isolation was realized — for the second time on the same branch — via Agent-session boundaries: α-as-agent ran in one Agent context for all four subs serially; β-as-agent ran in a separate Agent context for all four subs serially. The hard rule `α ≠ β within a single sub` held by construction across both waves; 13 distinct authored commits across the two roles, every author email matching expectation. The pattern is durable for this harness configuration.

2. **β-side code-first oracle anchoring is the structural fix for the F7 class of miss.** The precursor wave's β missed F7 by anchoring AC1 on the freshly-rewritten schema doc rather than on `scripts/segmentation.py`. This wave's β held the code-first discipline cleanly on both Sub A AC1 and Sub D AC1; β re-grepped the code side first and verified the doc matches the code-emitted set, never the inverse. The discipline is durable when β receives it as a hard constraint in the dispatch prompt (this wave) and is named at the sub-issue AC level (Sub A AC5 + Sub D AC7). Recommendation to ε: codify this in `cdd/beta/SKILL.md` so future waves inherit it without per-wave manifest restatement (cross-sub debt items 3 and 10 above).

3. **AC oracle-regex specification is a non-trivial craft surface.** The dispatcher-prompt regex `quality_flag\s*=\s*"` for Sub A AC1 missed the actual emission site at `scripts/segmentation.py:122` because the post-patch code uses a multi-line conditional (`quality_flag=("short" if duration <= 0.5 / ...`). β β-side widened to `quality_flag` and recorded both forms in `beta-review.md`. Specifying AC oracles that survive small code-style variations (single-line vs multi-line; chained ternaries; match-statements) is a small but real craft load on the issue-author. **Class:** `cdd-protocol-gap` candidate; folds into the same β-SKILL patch above.

---
_End of wave close-out._
