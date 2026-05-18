# Cross-repo proposal: Bootstrap cnos.cdr

**Source:** `usurobor/gait-support-paths`
**Target:** `usurobor/cnos`
**Slug:** `bootstrap-cdr`
**Type:** master/tracking issue draft for a new c-d-X protocol package
**Bundle state:** converging (master `cnos#376` filed + accepted; waiting on cnos sub-issues + wave close)

## Purpose

Propose creation of `cnos.cdr` — the research-protocol sibling to `cnos.cdd` — instantiating the role ladder (`ROLES.md §1`) for research matter. The bundle carries the ready-to-file master issue body for the cnos.cdr v0.1 wave.

## Bundle contents

- `ISSUE.md` — master/tracking issue body, ready to file in `usurobor/cnos`. Conforms to `src/packages/cnos.cdd/skills/cdd/issue/SKILL.md` minimal output pattern; labels `tracking, P2, cdd, package`; mode `docs-only` (master-shaped — implementation modes are declared per sub-issue).
- `STATUS` — event ledger; current event: `submitted`.
- `LINEAGE.md` — bilateral trace. Source side filled in here; target side to be added once cnos lands work, per the existing pattern at `cnos:.cdd/iterations/cross-repo/tsc/cdd-supercycle/LINEAGE.md`.

## Why source-proposal rather than direct file

`usurobor/gait-support-paths` is the empirical research project that surfaced the gap: it has been operating under cdd-with-overrides (load-bearing claims like hypothesis pre-registration, falsifiability hooks, diagnostic-oracle pattern, GO/REVISE/NO-GO closeout, dataset datasheet, manifest-hash-pinned external data) because no research-protocol instantiation exists. `cnos.cdr` is the upstream fix. Per `cdd/gamma/SKILL.md §"Cross-repo proposal close-out"`, the correct transport is a cross-repo bundle authored in the source repo; the target repo's γ picks it up and files the target issue with a `## Source Proposal` block citing this bundle.

The session-time alternative — having the operator paste the issue body from a virtual-box-local file — bypasses the lineage trace and produces an issue with no provenance back to its empirical anchor. The bundle is the correct durable artifact.

## Originating context

This proposal originates from the 2026-05-18 session that scoped `cnos.cdr` against:

- `ROLES.md §7` (cdr reserved as research instantiation)
- `ROLES.md §3` (6-field instantiation contract every c-d-X must declare)
- `src/packages/cnos.cdd/skills/cdd/COHERENCE-CELL.md` (in-flight cdd refactor doctrine; cdr design must be consistent with its structural prediction)
- `src/packages/cnos.cdd/skills/cdd/issue/SKILL.md` (issue authoring standard the master issue conforms to)
- Empirical anchor: `usurobor/gait-support-paths` zeroth-pilot wave (2026-05-15) + segmentation-fix cycle (2026-05-17)

## Next action

`usurobor/cnos` γ picks up this bundle (or operator manually files via `gh`), creates target issue with `## Source Proposal` block citing this path + the source commit SHA, and appends `accepted` (or `modified`) event to `STATUS` here.

If `usurobor/cnos` γ cannot write back to this repo, the cnos cycle should emit a feedback patch that updates `STATUS` (per `cdd/gamma/SKILL.md §"Cross-repo proposal close-out"`).

Once the cnos wave lands, the cnos-side mirror at `cnos:.cdd/iterations/cross-repo/gait-support-paths/bootstrap-cdr/LINEAGE.md` is the trigger to archive the source-side copy here (per `cdd/post-release/SKILL.md` Step 5.6b).
