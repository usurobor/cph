# Wave: Existing-data zeroth pilot

**Date:** 2026-05-15
**Dispatcher:** δ-as-agent
**Repo:** usurobor/gait-support-paths
**Parent issue:** #4 (auto-closes when all subs close)

## Issues (run in order)

| Order | # | Title | Depends on |
|-------|---|-------|------------|
| 1 | 5 | Sub A — Acquire OpenCap Lab Validation dataset and complete manifest | — |
| 2 | 6 | Sub B — Build segmentation + feature-extraction pipeline | #5 |
| 3 | 7 | Sub C — Produce support-path inference memo and field report | #5, #6 |

## Standing permissions

- Push to cycle/{N} branches: yes
- Push merges to main: yes
- Auto-dispatch α fix rounds on β REQUEST CHANGES: yes (max 3)
- Tag/release: NO — operator gate
- Branch delete after merge: yes
- Install Python packages and commit `requirements.txt`: yes (Sub B)
- Download public OpenCap Lab Validation data to a local path outside the repo: yes
- Commit raw participant data: NO (hard non-goal)

## Timeout budgets

- α: 1800s (data download in #5; pipeline runs in #6 may take time)
- β: 900s

## Known constraints

- Sub A requires SimTK access and license review. If the candidate
  dataset has a non-permissive license, escalate to operator before
  acquisition.
- Sub B needs OpenSim or nimblephysics. If installation fails, escalate
  before proceeding with degraded features.
- Sub C cannot stub the inference memo. If Sub B yields no usable
  features, close Sub C as NO-GO with rationale per protocol
  §Go/No-Go Criteria — that IS a valid outcome.
- Raw participant data NEVER committed (data/external/README.md,
  docs/ethics/data-handling.md).
- Manifest local storage path lives outside the repo or is .gitignored.
