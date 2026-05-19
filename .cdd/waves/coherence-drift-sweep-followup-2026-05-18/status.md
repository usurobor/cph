# Wave Status: Coherence drift sweep follow-up (master cph#21)

**Last updated:** 2026-05-18 by δ (wave opened)
**Wave manifest:** `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/manifest.md`
**Wave close-out:** `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/wave-closeout.md` (pending)
**Working branch:** `claude/review-repo-coherence-PNbjQ` (single-branch dispatch per manifest §"Branching deviation")

| # | Issue | Findings | Status | Rounds | β SHA | Notes |
|---|-------|----------|--------|--------|-------|-------|
| 22 | Sub A — quality_flag schema↔code vocabulary alignment | F7 (HIGH, β-axis) | ⬜ queued | — | — | Lift code to schema; α picks a-1/a-2/a-3; F7-class anchoring discipline AC |
| 23 | Sub B — PROJECT.md §Active branch + ROADMAP.md R0 de-staling | F8, F9 (MEDIUM, γ-axis) | ⬜ queued | — | — | Two-file docs-only patch |
| 24 | Sub C — field-report-02 stub H1 number mismatch | F11 (LOW, γ-axis) | ⬜ queued | — | — | One-line H1 fix |
| 25 | Sub D — rename `extract_shape` placeholder | F10 (MEDIUM, β-axis) | ⬜ queued | — | — | α picks d-1/d-2/d-3; F7-class anchoring discipline AC |

**Wave totals:** 0 / 4 subs in terminal state. Wave OPEN.

**Master cph#21:** OPEN — master closure deferred to ε per `coherence-drift-sweep-2026-05-18` precedent. AC1–AC8 pending sub closure.

## Status legend

- `⬜ queued` — not started
- `🔄 dispatched` / `🔄 in-progress` — γ/α/β active
- `✅ completed` — β APPROVED + close marker committed on dispatch branch
- `❌ failed` — sub abandoned
- `⏸️ blocked` — waiting on dependency
- `⭕ deferred` — explicitly moved out of wave

## Closure conditions

Wave is closed when:
1. All four sub-issues are in terminal state (4 × completed or any combination of completed/deferred/failed with the wave-closeout naming the terminal mix).
2. `wave-closeout.md` written naming aggregate stats, cross-sub findings, and out-of-scope follow-ups.
3. `receipt.md` written naming wave-level decision and authority bounds.
4. Master cph#21 remains OPEN at wave close — closure is ε's action.
