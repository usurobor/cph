# Wave Status: CDR refactor (master #11)

**Last updated:** 2026-05-18 by δ
**Wave manifest:** `.cdd/waves/cdr-refactor-2026-05-18/manifest.md`

| # | Issue | Status | Rounds | Branch | Tag | Notes |
|---|-------|--------|--------|--------|-----|-------|
| 12 | Sub A — CDR charter docs | 🟢 ready | 0 | `cycle/12` | — | Cycle branch created from `origin/main`; α/β dispatch prompts emitted; awaiting `claude -p` invocation by operator |
| 13 | Sub B — CDR roadmap | 🟢 ready | 0 | `cycle/13` | — | Cycle branch created from `origin/main`; α/β dispatch prompts emitted; awaiting `claude -p` invocation by operator |
| 14 | Sub C — TSC infra + CHANGELOG + PROJECT.md repartition | 🟢 ready | 0 | `cycle/14` | — | Cycle branch created from `origin/main`; α/β dispatch prompts emitted; awaiting `claude -p` invocation by operator |
| 15 | Sub D — CDR refactor conformance sweep | ⏸️ blocked | 0 | (pending A+B+C close) | — | Cycle branch not yet created — created at A+B+C terminal-state transition |

## Status legend

- `⬜ queued` — not started
- `🔄 dispatched` / `🔄 in-progress` — γ/α/β active
- `✅ completed` — merged to main
- `❌ failed` — cycle abandoned
- `⏸️ blocked` — waiting on dependency
- `⭕ deferred` — explicitly moved out of wave

## Closure conditions

Wave is closed when:
1. All four sub-issues are in terminal state (completed / failed / deferred).
2. Master `cph#11` has been closed (by a separate δ comment / γ close-out — not by this wave's automatic action).
3. `wave-closeout.md` is written naming aggregate stats, cross-sub findings, and any deferred items.
