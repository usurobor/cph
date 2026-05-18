# Bootstrap cnos.cdr — research protocol package
Labels: tracking, P2, cdd, package

Priority: P2 — Enables coherent research-cycle discipline for downstream research projects (the canonical empirical case is `usurobor/gait-support-paths`). Not release-blocking; enables new capability.
Status: cnos.cdr package not started. `ROLES.md §7` reserves the letter `cdr` for the research instantiation; no package, skills, or doctrine exist yet.
Mode: docs-only (master/tracking issue — emits the wave envelope; implementation modes are declared per sub-issue).

## Problem

What exists:
- `ROLES.md §7` reserves cdr — "research (investigation, synthesis, citation)" — as a planned sibling protocol alongside cdw / cda.
- `cnos.cdd` ships and instantiates the role ladder for software-development matter.
- `src/packages/cnos.cdd/skills/cdd/COHERENCE-CELL.md` is the in-flight refactor surface positioning cdd as the role-cell skeleton, with software-engineering specifics planned to move to a separate package (`cnos.cds`).
- No package exists for research-protocol matter. Research projects (canonical empirical case: `usurobor/gait-support-paths`) reach for cdd as the closest analog and override informally — load-bearing claims (hypothesis pre-registration, falsifiability, diagnostic-oracle pattern, GO/REVISE/NO-GO closeout, dataset datasheet, reproduction-from-clean recipe) currently live as project-local convention rather than as ratified protocol.

What is expected:
- `cnos.cdr` ships as a sibling to `cnos.cdd`, instantiating the role ladder for research matter.
- All six instantiation-contract fields (`ROLES.md §3`) are declared for cdr.
- cdr is consistent with the `COHERENCE-CELL.md` structural prediction (roles / runtime substrate / validation / boundary effection are separate surfaces; receipts, not seniority, carry trust).
- cdr v0.1 covers the minimum surface to operate a research cycle: instantiation contract, canonical `CDR.md` + `SKILL.md`, role overlays. Lifecycle artifacts (issue/design/plan/review/release/post-release) intentionally deferred until the cdd→cds refactor lands and that surface stabilises.

Where they diverge: `cnos.cdr` does not exist; `usurobor/gait-support-paths` is operating research work under cdd-with-overrides, accumulating informal conventions that should be ratified protocol.

## Impact

- **Research projects cannot declare protocol compliance.** A research cycle that says "we followed cdr" today resolves to nothing checkable.
- **No β oracle for research matter.** β reviewing a research cycle today reviews against project-local rubric (the gait-support-paths field-report convention), not a ratified oracle.
- **No receipt schema for research cells.** The `COHERENCE-CELL.md` receipt model has no research-shaped instantiation, so research cells cannot emit transmissible matter to parent scopes.
- **Skill drift across research projects.** Each new research project re-invents (or partially re-invents) the falsifiability / pre-registration / diagnostic-oracle / GO–REVISE–NO-GO pattern.

Empirical anchor: `usurobor/gait-support-paths` zeroth-pilot wave (2026-05-15) and segmentation-fix cycle (2026-05-17) both produced material on top of cdd-with-overrides. The conventions converging across cycles (field-report template, dataset datasheet at `data/external/<name>.md`, diagnostic-oracle pattern per algorithmic primitive, GO/REVISE/NO-GO closeout, manifest-hash-pinned external data) are the candidate cdr surface.

## Status truth

Today (2026-05-18):
- `cnos.cdr`: does not exist.
- `ROLES.md §7`: cdr is named as a reserved letter; no contract declared.
- `COHERENCE-CELL.md`: draft refactor doctrine for cdd; not ratified; will shape cdr's structural design.
- `usurobor/gait-support-paths`: operating under cdd-with-overrides; will be the first cdr adopter.

This issue does not itself create the package. It is the master/tracking issue that envelopes the wave of sub-issues, each delivering part of the `cnos.cdr` v0.1 surface. Subs are filed and dispatched by δ to other agents per the operator's intent.

## Source of truth

| Claim / surface | Canonical source | Status | Notes |
|---|---|---|---|
| Role ladder (α/β/γ/δ/ε), 6-field instantiation contract | `ROLES.md` | Shipped | The generic doctrine cdr instantiates. |
| Reference instantiation (cdd) | `src/packages/cnos.cdd/skills/cdd/CDD.md` | Shipped (1346 lines; sections 3–10 expected to move to `cnos.cds` per refactor) | Mirror package shape; do NOT depend on its lifecycle artifacts. |
| Refactor structural prediction | `src/packages/cnos.cdd/skills/cdd/COHERENCE-CELL.md` | Draft doctrine | cdr design must be consistent: roles / runtime / validation / boundary as separate surfaces. |
| Empirical research-project case | `usurobor/gait-support-paths` (PROJECT.md, `data/external/opencap-lab-validation.md`, `reports/field-report-01-existing-data-zeroth-pilot.md`, `scripts/segmentation_diagnostics.py`) | Active | Canonical research project; cdr v0.1 must work as an overlay for this project. |
| Naming convention | `ROLES.md §7` ("cdr — research (investigation, synthesis, citation)") | Shipped | Letter is reserved; matter type to be declared in `CDR.md`. |
| Issue authoring standard | `src/packages/cnos.cdd/skills/cdd/issue/SKILL.md` | Shipped | This issue conforms to that standard. |

## Scope

In scope (master + subs together):
- `src/packages/cnos.cdr/` package created with `cn.package.json`, `README.md`, `skills/cdr/CDR.md`, `skills/cdr/SKILL.md`.
- All six instantiation-contract fields declared for cdr in `CDR.md`.
- Role overlays for α / β / γ / operator(δ) / ε in `skills/cdr/{alpha,beta,gamma,operator,epsilon}/SKILL.md`.
- Empirical alignment check: the cdr v0.1 surface is sufficient to retroactively describe the `usurobor/gait-support-paths` zeroth-pilot wave + segmentation-fix cycle without contradiction.

Out of scope:
- Lifecycle sub-skills (`issue/`, `design/`, `plan/`, `review/`, `release/`, `post-release/`). Defer until cdd→cds refactor lands and the cdd lifecycle is stable.
- Commands (`cdr-verify`, `cdr-status`). Defer until at least one research cycle has run under cdr v0.1 to surface the CLI need.
- cdw / cda / other c-d-X siblings. Reserved letters; out of scope for this wave.
- Migration of `usurobor/gait-support-paths` from cdd-with-overrides to cdr. Tracked as a separate downstream cycle in that repo after cdr v0.1 ships.
- ε's first iteration over cdr (`cdr-iteration.md`). ε is finding-triggered; no findings until cycles ship.

Deferred:
- `cnos.cds` package — software-specific logic extracted from cdd. Tracked as a separate cnos issue; cdr does NOT depend on cds existing first.

## Cycle scope sizing

This is a master/tracking issue. The five-factor heuristic applied to the wave-as-a-whole:

| Factor | Reading | Splitting signal? |
|---|---|---|
| (a) New code surface | New package `cnos.cdr` with ≥7 new skill files | Yes (≥2 new modules) |
| (b) Cross-module breadth | Touches no existing packages directly; references `ROLES.md` and `cnos.cdd` doctrine read-only | No |
| (c) Lifecycle span | Design (contract fields) + docs (skills) + verification (empirical-anchor check) | Borderline |
| (d) MCA preconditions | Design not yet stable — contract fields are draft below; must converge per-sub | No (design-and-build at the master level) |
| (e) Independent shippability of AC groups | Yes — instantiation contract can ship without role overlays; package skeleton can ship without contract finalised; empirical-anchor check is independent | Strong yes |

Decision: **split into master + subs.** This master + ≥4 sub-issues (final shape decided by dispatching γ; the proposed shapes below are non-binding):

- *Proposed Sub 1.* Draft + ratify cdr's six-field instantiation contract. Mode: `design-and-build`.
- *Proposed Sub 2.* Bootstrap `cnos.cdr` package skeleton + `CDR.md` + `SKILL.md`. Mode: `MCA` (cites Sub 1 design once stable).
- *Proposed Sub 3.* Role overlays in `skills/cdr/{alpha,beta,gamma,operator,epsilon}/SKILL.md`. Mode: `design-and-build`.
- *Proposed Sub 4.* Empirical-anchor doc — `cnos.cdr/docs/empirical-anchor-gait-support-paths.md` showing the gait zeroth-pilot wave + segmentation-fix cycle are describable under cdr v0.1 without contradiction. Mode: `docs-only`.

Sub creation is δ-dispatched to other agents. This master is the scope envelope; subs declare their own ACs, modes, and sizing.

## Acceptance criteria

### AC1: Master scope envelope is closeable

Invariant: This master is closeable when all sub-issues filed under it are closed and their close-out receipts validate, OR any deferred sub is explicitly carried as named debt in this master's closure comment.
Oracle: `gh issue list --label tracking --state closed` includes this issue's number after the last sub closes; the master's closure comment names each sub's `#` and its receipt path under `.cdd/releases/<version>/<sub-#>/`.
Positive: Subs close in order; this master closes after the last sub with all receipts cited.
Negative: A sub closes with a non-PASS validator verdict and no override block. This master MUST NOT close until either the sub is fixed or the deferral is explicit and named.
Surface: GitHub issue state + close-out comment on this issue.

### AC2: Subs are independently shippable

Invariant: Every sub-issue is shippable on its own — no sub chains on another sub's merge (per `issue/SKILL.md` master+subs pattern).
Oracle: Each sub's "Cycle scope sizing" table on filing shows factor (e) = "yes — ships independently." A sub failing this on filing must be re-shaped before dispatch.
Positive: All subs ship without mutual blocking.
Negative: Sub 2's α blocks on Sub 1's merge — that's the chain anti-pattern. δ rescopes before dispatch.
Surface: Each sub's issue body.

### AC3: cdr v0.1 surface is sufficient for the empirical anchor

Invariant: The cdr v0.1 surface (all subs landed) is sufficient to retroactively describe the `usurobor/gait-support-paths` zeroth-pilot wave + segmentation-fix cycle (2026-05-15 / 2026-05-17) without contradiction.
Oracle: Sub 4's deliverable produces `cnos.cdr/docs/empirical-anchor-gait-support-paths.md` mapping every artifact class in those two waves (PROJECT.md, dataset manifest, field-report, diagnostic-oracle, GO/REVISE/NO-GO, dataset hash pinning, multi-agent attribution) to its corresponding cdr v0.1 surface element. Zero "no cdr surface for this" rows.
Positive: The mapping table is complete; no contradictions surface during the read.
Negative: A load-bearing gait artifact class has no cdr v0.1 surface — that's an unfilled hole; Sub 1 must be reopened.
Surface: `cnos.cdr/docs/empirical-anchor-gait-support-paths.md`.

### AC4: cdr is consistent with COHERENCE-CELL.md structural prediction

Invariant: cdr v0.1 MUST NOT fuse roles + runtime substrate + validation + boundary effection into a single skill. (Inherits the AC2 invariant of the cdd refactor.)
Oracle: Inspection of `skills/cdr/*/SKILL.md` shows role skills name what the role does; no role skill authors runtime-mechanic concerns (dispatch, polling, git/CI plumbing) or release-driver effection.
Positive: Role skills declare role function only; runtime and release concerns are out of scope for v0.1.
Negative: An `operator/SKILL.md` (δ) that bundles "publish to OSF + run notebook + tag" is a fused skill — fails AC4.
Surface: `rg` on `skills/cdr/*/SKILL.md` for runtime-mechanic and release-driver tokens; should not appear in v0.1.

### AC5: cdr declares all six instantiation-contract fields

Invariant: `CDR.md` declares all six fields per `ROLES.md §3` — matter type, review oracle, γ close-out artifact, δ cadence, ε iteration cadence, actor collapse rule. No field may be "TBD."
Oracle: `rg "^### Field" src/packages/cnos.cdr/skills/cdr/CDR.md | wc -l` returns 6; `rg -c "TBD" src/packages/cnos.cdr/skills/cdr/CDR.md` returns 0.
Positive: All six fields present with concrete declarations.
Negative: Any field declared as "TBD" or omitted is incoherent — Sub 1 reopened.
Surface: `src/packages/cnos.cdr/skills/cdr/CDR.md`.

## Proof plan

Invariant: cdr v0.1 ships as a coherent sibling protocol to cdd, with all six instantiation-contract fields declared, role overlays present, empirical-anchor validated, and consistent with the `COHERENCE-CELL.md` structural prediction.

Surface: `src/packages/cnos.cdr/` (created by Subs 1–3) + `cnos.cdr/docs/empirical-anchor-gait-support-paths.md` (created by Sub 4).

Oracle:
- `ls src/packages/cnos.cdr/` returns the expected file set;
- `rg "^### Field" src/packages/cnos.cdr/skills/cdr/CDR.md | wc -l` = 6;
- `rg -c "TBD" src/packages/cnos.cdr/skills/cdr/CDR.md` = 0;
- Empirical-anchor doc maps every load-bearing gait artifact class to a cdr surface element (zero unmapped rows);
- No `skills/cdr/*/SKILL.md` mixes role concerns with runtime/release concerns (AC4 grep).

Positive case: All subs close; all five ACs pass on their respective oracles; the empirical-anchor doc reads coherent.

Negative case: A sub closes with `Field 5 — ε iteration cadence: TBD` — that's incomplete; Sub 1 reopened. Master MUST NOT close until resolved.

Operator-visible projection: GitHub issue thread (this issue) shows all subs cited, closed, and receipts linked; `cnos.cdr/` directory visible in tree; `cnos.cdr` listed in `src/packages/` alongside `cnos.cdd`, `cnos.core`, `cnos.eng`, `cnos.kata`.

Known gap: cdr v0.1 deliberately omits lifecycle sub-skills (`issue/`, `design/`, `plan/`, `review/`, `release/`, `post-release/`). Those are expected to move to `cnos.cds` in the cdd refactor; cdr will reference cds (or its successor) when stable. This is named debt, not a hole in v0.1.

## Skills to load

Tier 3:
- `cdd/issue` — issue authoring standard
- `cdd/issue/labels` — label taxonomy
- `ROLES.md` (read-only doctrine — upstream contract)
- `cdd/COHERENCE-CELL.md` (read-only — structural prediction cdr must be consistent with)

Why:
- Issue + labels: this issue conforms to cdd issue authoring standard.
- `ROLES.md`: the upstream doctrine cdr instantiates. The six-field instantiation contract lives here.
- `COHERENCE-CELL.md`: the structural prediction cdr must be consistent with (no surface fusion; receipt-not-seniority trust).

## Active design constraints

- **Hat collapse rule (`ROLES.md §4`).** α≠β within any single sub cycle. γ=δ permitted (operator-as-coordinator). β=γ permitted with explicit acknowledgment in the receipt.
- **6-field instantiation contract (`ROLES.md §3`).** Mandatory for any c-d-X protocol. cdr must declare all six.
- **Receipt-not-seniority trust (`COHERENCE-CELL.md §"Trust Boundary"`).** cdr's γ close-out emits a receipt that validates against the contract; γ approval alone does not establish trust.
- **No surface fusion (`COHERENCE-CELL.md` AC2 invariant).** cdr v0.1 must NOT fuse role + runtime + validation + boundary in one skill. cdr authors role skills only; runtime substrate and release effector concerns are out of scope for v0.1.
- **No premature lifecycle bake-in.** cdr v0.1 must not depend on cdd's lifecycle sub-skills (sections 3–10 of `CDD.md`), which are expected to move to `cnos.cds`.

## Related artifacts

- `ROLES.md` (cnos repo root)
- `src/packages/cnos.cdd/README.md`
- `src/packages/cnos.cdd/cn.package.json` (package-shape exemplar)
- `src/packages/cnos.cdd/skills/cdd/SKILL.md` (loader-pattern exemplar)
- `src/packages/cnos.cdd/skills/cdd/CDD.md` (canonical reference instantiation; sections 3–10 expected to refactor to `cnos.cds`)
- `src/packages/cnos.cdd/skills/cdd/COHERENCE-CELL.md` (in-flight refactor doctrine)
- `src/packages/cnos.cdd/skills/cdd/issue/SKILL.md` (issue authoring standard this issue conforms to)
- `usurobor/gait-support-paths` (empirical research project; cdr v0.1's empirical anchor; will adopt cdr after v0.1 ships)

## Non-goals

- This issue does NOT create the `cnos.cdr` package. It scopes the wave; subs implement.
- cdr v0.1 does NOT include lifecycle sub-skills. Deferred to `cnos.cds` emergence.
- cdr v0.1 does NOT include CLI commands (no `cdr-verify` / `cdr-status`).
- cdr does NOT redefine `ROLES.md` or the role ladder. cdr instantiates; `ROLES.md` governs.
- cdr does NOT depend on the cdd→cds refactor having landed. cdr designs against `ROLES.md` + `COHERENCE-CELL.md` prediction; if the refactor changes, cdr adjusts in a future cycle.
- Migration of `usurobor/gait-support-paths` from cdd-with-overrides to cdr is NOT in this wave. Separate downstream cycle.

## Success / closure condition

This master issue is closeable when:
- All sub-issues filed under it are closed, each independently shippable, each with declared mode + AC count + sizing decision.
- All subs close with PASS validator verdicts (or explicit override blocks if degraded).
- ACs 1–5 above pass against their oracles.
- The empirical-anchor doc validates that cdr v0.1 covers the gait-support-paths empirical case without contradiction.
- Known gaps (lifecycle sub-skills deferred to `cnos.cds`; CLI commands deferred; migration of gait deferred) are carried as named debt in this master's closure comment.

The master's closure comment must:
- List every sub's `#` and receipt path.
- Name every known gap and its tracking issue `#` (or "tracked as debt, no separate issue yet").
- Declare the cdr v0.1 surface (file list under `src/packages/cnos.cdr/`) as the wave's coherence-delta.
