# Wave: Protocol patches from zeroth-pilot

**Date:** 2026-05-15
**Dispatcher:** δ-as-agent
**Repo:** usurobor/gait-support-paths
**Origin:** `.cdd/waves/zeroth-pilot-2026-05-15/wave-closeout.md` (Patterns 1, 2; #6 portability debt)

## Issues (parallelizable; no inter-dependency)

| Order | # | Title | Type |
|-------|---|-------|------|
| 1 | 8  | Protocol revision — add «Access mechanism» subsection | docs |
| 2 | 9  | Concept patch — falsification table needs empirical-data preamble | docs |
| 3 | 10 | Pipeline portability — make data path configurable (env var / notebook param) | enhancement |

Issues are independent — no data or artifact dependency between them. Order in the table is by author preference, not by constraint. A wave runner may execute them in any order or in parallel sessions.

## Standing permissions

- Push to cycle/{N} branches: yes
- Push merges to main: yes
- Auto-dispatch α fix rounds on β REQUEST CHANGES: yes (max 3)
- Tag/release: NO — operator gate
- Branch delete after merge: yes
- Install Python packages: NO — `requirements.txt` does not change in this wave
- Modify `requirements.txt`: NO

## Timeout budgets

- α: 600s per cycle (small docs / small code patch)
- β: 600s per cycle

## Known constraints

- This wave inherits the **broadened escalation rule** lifted from zeroth-pilot Pattern 1: escalate on EITHER "non-permissive license" OR "access-mechanism gate that requires unsupplied credentials." (No data acquisition this wave, so the rule is vacuous here, but the broader convention applies to all future waves.)
- An empty findings list at wave close is acceptable per ε convention — the close-out file should say so explicitly rather than be omitted.
- All three issues are docs-only or small code; if any cycle exceeds 3 fix-rounds, escalate to operator before continuing.
- `claude/add-support-paths-readme-t5ZW3` is unrelated to this wave; leave untouched.

## Cycle ordering note

Issues #8 and #9 touch disjoint files (`protocols/existing-data-zeroth-pilot.md` + `data/external/README.md` + `data/external/opencap-lab-validation.md` for #8; `docs/concepts/support-path.md` + possibly the field-report template for #9). Issue #10 touches `scripts/io_opencap.py`, `notebooks/existing-data-processing.ipynb`, and `notebooks/README.md`.

No two cycles touch the same file. Parallel execution is safe for a wave runner that supports it; serial execution is fine too.

## Out-of-scope follow-ups (named, not in this wave)

- Credentialled re-run of the zeroth-pilot pipeline (separate wave, gated on operator-supplied SimTK credentials or a backup dataset choice).
- Hip ab/ad-duction feature extension (referenced by zeroth-pilot Hypothesis 2; needs real-data column confirmation).
- Upstream PR to `usurobor/cnos` lifting Pattern 2 (empirical-data preamble) into the cnos skill bundle (operator decision).
