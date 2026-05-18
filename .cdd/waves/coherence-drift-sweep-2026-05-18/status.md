# Wave Status: Coherence drift sweep (master cph#16)

**Last updated:** 2026-05-18 by δ (wave closed)
**Wave manifest:** `.cdd/waves/coherence-drift-sweep-2026-05-18/manifest.md`
**Wave close-out:** `.cdd/waves/coherence-drift-sweep-2026-05-18/wave-closeout.md`
**Working branch:** `claude/review-repo-coherence-PNbjQ` (single-branch dispatch per manifest §"Branching deviation")

| # | Issue | Findings | Status | Rounds | β SHA | Notes |
|---|-------|----------|--------|--------|-------|-------|
| 17 | Sub A — broken realization ref + R0 wording | F1, F6 | ✅ completed | 1 (APPROVE) | `b32bde2` | Two single-line patches; ROADMAP R0 §Next action staleness named as out-of-scope debt |
| 18 | Sub B — field-report-02 name collision | F2 | ✅ completed | 1 (APPROVE) | `a69a863` | Scheme forced by existing stub `field-report-02-friend-pre-pilot.md`: R5 = -02, R3 = -03 |
| 19 | Sub C — schema/code column alignment + features.md | F3, F5 | ✅ completed | 1 (APPROVE) | `399bfd8` | Direction (b) — shrunk schema doc to match code; F5 first-pass list verified bijective with `scripts/features.py::extract_features` |
| 20 | Sub D — rename legacy `gait-support-paths-features/` | F4 | ✅ completed | 1 (APPROVE) | `040ed3c` | Renamed to `cph-features/`; notebook regenerated; cached outputs stripped |

**Wave totals:** 4 / 4 subs in terminal state. **4 × APPROVE round 1 / 0 RC rounds / 0 β findings.**

**Master cph#16:** OPEN — master closure deferred to ε per `cdr-refactor-2026-05-18` precedent. All 8 ACs (AC1–AC8) met; recommended closure named in wave-closeout §"Master closure".

## Status legend

- `⬜ queued` — not started
- `🔄 dispatched` / `🔄 in-progress` — γ/α/β active
- `✅ completed` — β APPROVED + close marker committed on dispatch branch
- `❌ failed` — sub abandoned
- `⏸️ blocked` — waiting on dependency
- `⭕ deferred` — explicitly moved out of wave

## Closure conditions (met)

Wave is closed when:
1. ✅ All four sub-issues are in terminal state (4 × completed).
2. Master cph#16 OPEN — closure is a separate δ/ε action per wave manifest.
3. ✅ `wave-closeout.md` written naming aggregate stats, cross-sub findings, and out-of-scope follow-ups.
