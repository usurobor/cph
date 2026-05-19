<!-- sections: [Issue, Mode, Design, Plan, ACs, Cycle scope sizing, Cross-cycle coordination, α dispatch surface, β dispatch surface] -->
<!-- completed: [Issue, Mode, Design, Plan, ACs, Cycle scope sizing, Cross-cycle coordination, α dispatch surface, β dispatch surface] -->

# γ scaffold — cph#28 — L-cycle recovery

## Issue

**Issue:** [usurobor/cph#28](https://github.com/usurobor/cph/issues/28) — "L-cycle recovery — contralateral-anchored detection or wider IK windows" (P1; labels `surface:data`, `surface:analysis`).
**Fetch full body:** `gh issue view 28 --repo usurobor/cph --json title,body,labels`.

**Body summary (one paragraph).** Recover L-side gait cycles from the OpenCap Lab Validation archive. After cph#26, R-side cycles fire at 60/60 trials but L-side fires at 1/60 — a property of the source archive (each trial cropped to ~1.3–1.5s, R-aligned; 47/60 L sides end mid-swing, 12/60 start mid-swing per `scripts/segmentation_diagnostics.py`), not of the detector. Recovery unblocks bilateral hypotheses (H3 asymmetric phase-coupling, L/R asymmetry features) and is the only path that can lift R1 out of REVISE. The issue body names two implementation paths — (a) contralateral-anchored L-cycle detection (new function / module that seeds L bounds from detected R HS + half-stride offset, calibrated against the one existing L cycle; inferred, not measured) or (b) re-run OpenSim IK with wider time windows (requires source TRC files in `/opt/gait-data/opencap-lab-validation/` + OpenSim tooling on PATH + operator-side rerun; produces real measurement) — and an explicit decision criterion. The 8 ACs span: direction-choice + rationale (AC1), L-cycle yield improvement (AC2), bilateral coverage characterization (AC3), no R-side regression (AC4), field-report-01 update with empirical-decision outcome (AC5), status-surface realignment (AC6), no charter empirical drift (AC7), no data-policy regression (AC8).

## Mode

**Mode:** `design-and-build` (per `issue/SKILL.md` mode declaration table).

**Mode-precondition rationale.** This cycle is not MCA: the issue body describes both candidate paths (a) and (b) and the decision criterion between them, but **no DESIGN.md is committed** at a stable path and **no PLAN.md** is committed with a sequenced step ordering specific to the chosen path. The 8 step bullets in the issue body §Steps are scaffold-level (rerun diagnostics → decide path → implement → rerun notebook → verify → update report → update status → commit/push); the implementation steps *depend on* whether α picks (a) or (b), and that direction-choice is itself a real design call that is α's to make in-cycle per the AC1 criterion. Per `issue/SKILL.md` §"MCA preconditions": "If any of the three [design committed / plan committed / both stable] fails, γ declares the cycle as `explore` or `design-and-build`". Both design (the direction-choice + the resulting algorithm or pipeline-configuration shape) and the path-specific plan need to converge during this cycle — `design-and-build` is the correct mode-label and γ does not pre-commit either artifact upstream.

This is not `explore`: the gap is bounded (recover L cycles; AC1–AC8 fixed; non-goals fixed; success criterion fixed at AC5 — GO if AC1 ≥80% on both sides AND L≥10, REVISE if partial recovery, NO-GO if conclusively unusable). It is also not MCA: α must make the (a)/(b) call and the implementation shape follows from that call. `design-and-build` matches.

## Design

**Direction-choice surface.** α picks path (a) or path (b) per the decision criterion from the issue body §"Decision criterion for (a) vs (b)" — recorded here **verbatim**:

> If the source TRC files are reachable and OpenSim IK is available, path (b) gives stronger evidence and should be preferred. Otherwise, path (a) gives a contralateral-inferred surface that is honest about its inference. α records the criterion outcome in self-coherence.

**Path summaries (from issue body §Approach — not re-derived here):**

- **(a) Contralateral-anchored L-cycle detection.** New function (e.g. `detect_heel_strikes_contralateral`) in `scripts/segmentation.py`, or a new module `scripts/segmentation_contralateral.py`, that consumes detected R HS times + a per-trial cycle-duration estimate and emits L cycle boundaries seeded from R HS + ½-stride offset. Calibrated against the one detected L cycle (subject?, trial? — see `scripts/segmentation_diagnostics.py` output). Stays in-container; no upstream IK rerun. Cons: L HS times are inferred, not measured — claim scope for L vs R features must reflect that inference layer.
- **(b) Wider OpenSim IK windows.** Re-run the OpenSim IK pipeline (`scripts/io_opencap.py` or upstream) on source TRC files with longer time windows so each trial captures ≥1.5 strides on both sides. Requires source TRC files reachable in `/opt/gait-data/opencap-lab-validation/`, OpenSim tooling on PATH, and an operator-side rerun. Pros: real L-side measurement. Cons: may not be reproducible in the dispatch container.

**γ note on the direction-choice surface.** The criterion is bounded (reachability + tooling availability); it is mechanical to evaluate at α's intake. γ records the criterion verbatim above so β can independently verify in round 1 that α's documented outcome in `self-coherence.md` §ACs (AC1) matches what an independent reachability probe would conclude. **γ does not pre-commit either path** — that is α's call per AC1, with the rationale documented in `self-coherence.md` and verified at β round 1 against AC1's plain-text requirement: "Direction (a) or (b) named in `self-coherence.md` §ACs with rationale. If (a) is chosen because (b) is infeasible in-container, the (b)-blocker is named explicitly."

## Plan

**Not pre-committed.** Per the mode declaration above, the converged implementation plan is not in this scaffold and is not in a separate upstream `PLAN.md`. The 8 step bullets in the issue body §Steps are α's working plan; the *actual* per-step implementation depends on whether α picks (a) or (b). For reference, the issue-body Steps section is:

1. Read `reports/field-report-01-existing-data-zeroth-pilot.md` §"L-side cycle yield" + run `scripts/segmentation_diagnostics.py` against the archive; record per-(trial, side) cropping classifications.
2. Decide path (a) or (b); document criterion outcome.
3. Implement the chosen path:
   - **(a)** New function in `scripts/segmentation.py` (or new module `scripts/segmentation_contralateral.py`) that consumes detected R HS times and emits L cycle boundaries.
   - **(b)** Configure wider-window IK rerun; document data-path and tooling requirements; run; persist outputs alongside existing IK results.
4. Rerun the notebook against the recovered cycles: `python3 scripts/build_notebook.py && jupyter nbconvert --execute --inplace notebooks/existing-data-processing.ipynb`.
5. Verify per-subject L cycle counts; flag any trials where recovery still fails.
6. Update `reports/field-report-01-existing-data-zeroth-pilot.md` (recovery method documented; post-recovery cycle counts; updated falsification assessment; GO/REVISE/NO-GO decision; path-(a) honesty if inferred L HS times are used).
7. Update status surfaces (PROJECT.md, ROADMAP.md, CHANGELOG.md) to reflect post-recovery state.
8. Commit + push to `cycle/l-cycle-recovery`.

α may adapt these steps as the (a)/(b) call dictates; the AC ledger (AC1–AC8) is the binding success contract.

## ACs

cph#28 carries 8 ACs, lifted verbatim from the issue body. AC text below; γ adds no AC interpretation here — that belongs in `self-coherence.md` per the α load order.

### AC1 — Recovery path chosen and documented

> Direction (a) or (b) named in `self-coherence.md` §ACs with rationale. If (a) is chosen because (b) is infeasible in-container, the (b)-blocker is named explicitly.

### AC2 — L-cycle yield improved

> L-side cycle count improves from the current 1 cycle. Target: ≥10 L cycles across the 60 trials. If the target is not met, the field report explains *why* (e.g., "path (a) yielded N L cycles, but K trials still have insufficient L-stance coverage for any HS-based method").

### AC3 — Bilateral coverage characterized

> Post-recovery report names:
> - L-side cycle count per (subject, condition)
> - Number of (subject, trial, cycle_number) triples with both R and L cycles
> - Whether `lr_asymmetry` features in `scripts/features.py` are now computable on >0 pairs

### AC4 — No regression on R-side

> - R-side cycle count remains 60/60 trials
> - R-side cycle distribution unchanged (60 R cycles, durations 0.84–1.37 s, mean 1.06 s)
> - `scripts/segmentation.py::detect_heel_strikes` AC1 PASS preserved

### AC5 — `field-report-01-existing-data-zeroth-pilot.md` updated

> - L-side recovery method documented
> - Post-recovery cycle counts
> - Updated falsification assessment if pair availability changes the verdict
> - Decision: GO if AC1 ≥80% on both sides AND L≥10; REVISE if partial recovery; NO-GO if recovery fails and the archive is conclusively unusable for bilateral analysis
> - Path (a) honesty: if inferred L HS times are used, the report names this as inference and bounds the claim scope

### AC6 — Status surfaces realigned

> - `PROJECT.md` §"Current empirical decision" / §"Current blocker" / §"Next action" updated
> - `ROADMAP.md` R1 status updated (potentially → GO if bilateral coverage achieved); R3 / R4 status reflects new evaluation surface
> - `CHANGELOG.md` entry for this cycle

### AC7 — No empirical drift on charter

> - `README.md` / `docs/concepts/coherence-path-hypothesis.md` / `docs/concepts/support-path.md` / `docs/articles/seven-ways-people-walk.md` untouched
> - Empirical-state language consistent across PROJECT.md / ROADMAP.md / CHANGELOG.md / field-report-01

### AC8 — No data policy regression

> No raw participant data, no `.zip`/`.trc`/`.mot`/`.sto`/`.c3d`/`.osim`/`.mp4`/`.mov`/`.csv`/`.parquet` files committed. If path (b) is taken, IK outputs go to `/opt/gait-data/` (gitignored), not the repo.

## Cycle scope sizing

cph#28 has 8 ACs → "At-edge (8–10)" band per `issue/SKILL.md` §"Soft AC-count guideline". The five-factor heuristic applies:

| Factor | Reading for cph#28 | Splitting signal? |
|---|---|---|
| (a) New code surface | Path (a) adds 1 new function (or 1 new module `scripts/segmentation_contralateral.py`); path (b) adds 0 new code (configuration + rerun). Either way: ≤1 new module. | **No** (≤1 new module) |
| (b) Cross-module breadth | Touches `scripts/segmentation.py` (path (a)) or `scripts/io_opencap.py` / upstream IK config (path (b)); `notebooks/existing-data-processing.ipynb` (rerun); `analysis/feature-summary-zeroth-pilot.md` (rerun output); `reports/field-report-01-…` (update); `PROJECT.md` / `ROADMAP.md` / `CHANGELOG.md` (status). The scripts/notebook/analysis trio is 1 logical surface (segmentation + downstream rerun); status surfaces are a 2nd logical surface; field-report-01 is a 3rd. So 3 logical surfaces, but they are *sequenced* (segment → rerun → report → status) rather than independent — not a true cross-module breadth load. | **No** (sequenced, not parallel) |
| (c) Lifecycle span | Spans implementation (scripts), evidence reproduction (notebook + analysis output), report update (field-report-01), and status realignment (PROJECT/ROADMAP/CHANGELOG). All four phases are required but α's context flows naturally segment → rerun → report → status. No serialization-of-context problem (this is the same shape as cph#26 which converged in 1 RC + 1 fix-round). | **No** |
| (d) MCA-precondition stability | Design is *not* yet stable — the (a)/(b) call is α's to make and the resulting implementation shape follows from that call. But the gap is bounded (8 ACs fixed; non-goals fixed; success criterion fixed at AC5) and the criterion for (a)/(b) is mechanical. Mid-cycle design discovery is bounded to the (a)/(b) call itself, not to scope. | **No** (bounded design, mode = design-and-build correctly absorbs it) |
| (e) Independent shippability of AC groups | AC1 (direction) → AC2/AC3 (implementation + bilateral coverage) → AC4 (R-side regression) → AC5/AC6 (report + status) → AC7/AC8 (charter + data-policy guardrails). Could split AC5/AC6/AC7/AC8 (status + guardrails) into a separate "realign status surfaces" sub-cycle, but the field report + status realignment is what makes the recovery decision-relevant — without them, R1 cannot move and the bilateral hypotheses remain blocked. The ACs are tightly coupled around the empirical decision. | **No** (coupled around the empirical decision) |

**Decision: keep whole** — no factor fires a splitting signal. The 8-AC count puts this at the at-edge band but the cycle is end-to-end coherent around a single empirical decision (recover L → re-evaluate R1).

**γ comment on the AC1 internal branch point.** This cycle has a hard branch between paths (a) and (b) at AC1. γ considered whether that warrants splitting — e.g., a parent issue "decide direction" → child "(a) implement contralateral detection" or "(b) rerun wider-window IK". γ concluded **no**: the branch resolves mechanically at α's intake (reachability probe of `/opt/gait-data/opencap-lab-validation/` + OpenSim PATH check), and the rest of the cycle (AC2–AC8) is structurally identical under either path. Splitting would add a coordination hop (γ scaffold → α reachability probe → γ scaffold-2 → α implementation) for no judgment-quality gain — the criterion is already named in the issue body verbatim. α-side direction-choice in `self-coherence.md` §AC1 is the right shape.

## Cross-cycle coordination

**Partner cycle:** cph#27 — "R3 — R-side aggregate condition-response analysis (n=60 R cycles)". Partner branch: `cycle/r3-rside-aggregate-analysis`. Partner mode: `explore` / analysis (R-side aggregate condition-response on the existing feature table; no new code surface). Both new P1 issues (cph#27 and cph#28) are explicitly named as parallel partners in each other's issue body and **run concurrently**.

**Shared file surfaces (both cycles touch these — NOT file-disjoint):**

- `PROJECT.md` — §"Current empirical decision" / §"Current blocker" / §"Next action"
- `ROADMAP.md` — **this cycle may flip R1 REVISE → GO** if bilateral coverage is achieved (AC1 ≥80% on both sides AND L≥10); cph#27 explicitly **cannot** flip R1
- `CHANGELOG.md` — both cycles add an entry
- `analysis/feature-summary-zeroth-pilot.md` + `notebooks/existing-data-processing.ipynb` — **this cycle reruns the notebook** after L-recovery; cph#27 builds aggregates from the rerun-produced feature table if this cycle merges first

**R1 binding.** Only this cycle (cph#28) can lift R1 out of REVISE; cph#27 explicitly cannot (per its own issue body). The R1 decision criterion lives at AC5 of this cycle: "Decision: GO if AC1 ≥80% on both sides AND L≥10; REVISE if partial recovery; NO-GO if recovery fails and the archive is conclusively unusable for bilateral analysis." α may transition R1 REVISE → GO **only if** AC1 ≥80% on both sides AND L≥10; otherwise R1 stays at REVISE with documented recovery method.

**Recommended merge order (convention; not a γ-enforced gate — that is a future δ decision).** cph#28 merges first if it achieves AC1; this either lifts R1 → GO (cph#27 then runs on the updated empirical state) or holds R1 at REVISE with documented recovery method (cph#27 runs on the existing REVISE state). cph#27's α will need to rebase onto post-cph#28 main if cph#28 merges first.

α and β prompts for this cycle name the partner cycle + shared files + merge-order convention up front so they see it before they begin work.

## α dispatch surface

**Mode:** `design-and-build` (per §Mode).
**Branch:** `cycle/l-cycle-recovery` (γ-created at `5b6...` of `origin/main` HEAD; α `git switch`es, never creates).
**Identity:** `Alpha <alpha@cph.cdd.cnos>` (configure as first action: `git config user.name "Alpha" && git config user.email "alpha@cph.cdd.cnos"`).
**ACs to satisfy:** AC1–AC8 (per §ACs above).
**Direction-choice (binding):** α picks (a) or (b) per the criterion recorded verbatim in §Design. **The direction-choice and rationale go in `self-coherence.md` §ACs (AC1)**. If α picks (a) because (b) is infeasible in-container, the (b)-blocker (e.g., "no `/opt/gait-data/opencap-lab-validation/`", "no OpenSim on PATH", "operator-side rerun out of scope for in-container session") must be named explicitly.

**Standing reading list (α loads these first):**
- Issue body — `gh issue view 28 --repo usurobor/cph --json title,body,labels`
- `reports/field-report-01-existing-data-zeroth-pilot.md` §"L-side cycle yield" — names the two recovery paths + the cropping evidence
- `scripts/segmentation_diagnostics.py` — characterizes per-(trial, side) zero-cycle reasons (`trial_ends_mid_swing`, `trial_crops_only_swing`, `ok`); run it as Step 1 to record per-(trial, side) cropping classifications
- `scripts/segmentation.py::detect_heel_strikes` — current R-side detector (post-cph#26 robust-percentile + stance-region gating); path (a) implementation builds alongside, must not regress this
- `scripts/io_opencap.py` — IK ingest; path (b) implementation modifies upstream of this (TRC → IK rerun → outputs at `/opt/gait-data/`)
- `notebooks/existing-data-processing.ipynb` — rerun target; α regenerates via `python3 scripts/build_notebook.py && jupyter nbconvert --execute --inplace notebooks/existing-data-processing.ipynb`
- `scripts/features.py` `lr_asymmetry`-family features — verify AC3 ("Whether `lr_asymmetry` features in `scripts/features.py` are now computable on >0 pairs")
- The existing 1 L cycle from the post-cph#26 run — calibration anchor for path (a) (identify subject + trial via diagnostics output)

**Non-goals carried verbatim from issue body:**
- Detector retune in `scripts/segmentation.py::detect_heel_strikes` (R2 closed; the detector is correct, the archive is cropped)
- Friend pre-pilot recruitment
- Clustering or ML
- Charter surface edits (README, `docs/concepts/coherence-path-hypothesis.md`, `docs/concepts/support-path.md`)
- Raw data commits
- New empirical claims on CPH itself
- Changing R-side detector behavior

**Output contract:** α writes `.cdr/unreleased/28/self-coherence.md` with §Gap / §Skills / §ACs (AC1–AC8 each with code-side + diagnostics-side evidence; AC1 carries the direction-choice + rationale + (b)-blocker if (a) chosen) / §Self-check / §Debt / §CDD-Trace (through step 7) / §Pre-review gate (14 rows per `alpha/SKILL.md §2.6`) / §Review-readiness (round 1: base SHA, head SHA, branch CI state, "ready for β" line). α signals review-readiness on `origin/cycle/l-cycle-recovery` and exits — δ re-dispatches for fix-rounds if β returns RC.

**Cross-cycle coordination (binding awareness up front):** partner cycle cph#27 (`cycle/r3-rside-aggregate-analysis`) is running concurrently and shares the same status surfaces (PROJECT.md / ROADMAP.md / CHANGELOG.md) + the same feature-table-derived artifacts (`analysis/feature-summary-zeroth-pilot.md`, `notebooks/existing-data-processing.ipynb`). Recommended merge order is **cph#28 first** if AC1 is achieved; cph#27 rebases. **Only this cycle can lift R1 REVISE → GO** (AC1 ≥80% on both sides AND L≥10).

## β dispatch surface

**Branch:** `cycle/l-cycle-recovery` (β polls; never creates).
**Identity:** `Beta <beta@cph.cdd.cnos>` (configure as first action: `git config user.name "Beta" && git config user.email "beta@cph.cdd.cnos"`).
**Merge authority:** β `git merge`s `cycle/l-cycle-recovery` → main on APPROVE (`git checkout main && git pull --ff-only && git merge --no-ff cycle/l-cycle-recovery -m "Merge cycle/l-cycle-recovery — cph#28 L-cycle recovery"`). If β cannot push, δ may execute the push on β's request (β's integration authority, not δ approval).
**Fix-round protocol:** per `CDD.md` §1.6a — RC verdict in `beta-review.md`, α re-dispatched by δ, α appends fix-round to `self-coherence.md`, β re-reviews next round.

**ACs to verify independently (one subsection per AC in `beta-review.md`):**

- **AC1.** Read α's `self-coherence.md` §AC1 for the direction-choice + rationale. Independently probe: (b) reachability — does `/opt/gait-data/opencap-lab-validation/` exist with TRC files? does `which opensim` / OpenSim Python bindings resolve in the cycle environment? Confirm α's documented criterion outcome matches the independent probe.
- **AC2.** Verify L-side cycle count from the rerun notebook output (parse `.ipynb` JSON cell outputs or read `analysis/feature-summary-zeroth-pilot.md`). Target: ≥10 L cycles across 60 trials. If not met, verify field-report-01 explains *why*.
- **AC3.** Verify `reports/field-report-01-existing-data-zeroth-pilot.md` post-recovery section names L-side cycle count per (subject, condition), the (subject, trial, cycle_number) triple count for bilateral pairs, and whether `lr_asymmetry` features are computable on >0 pairs. Cross-check against notebook outputs.
- **AC4 (R-side regression check — high importance).** Independently verify R-side cycle count = 60/60 trials, R-side cycle durations remain 0.84–1.37 s with mean 1.06 s, and `scripts/segmentation.py::detect_heel_strikes` AC1 PASS preserved (re-run the AC1 grep oracle from cph#26: `git show HEAD:scripts/segmentation.py | grep -nE 'def detect_heel_strikes|q05|q95|< 0\.30|< 0\.10|>= 150'`).
- **AC5.** Read `reports/field-report-01-existing-data-zeroth-pilot.md` and verify: L-side recovery method documented; post-recovery cycle counts; updated falsification assessment; explicit GO / REVISE / NO-GO decision matching the AC5 criterion ("GO if AC1 ≥80% on both sides AND L≥10; REVISE if partial recovery; NO-GO if recovery fails and the archive is conclusively unusable for bilateral analysis"); path-(a) honesty (if inferred L HS times are used, the report names this as inference and bounds the claim scope).
- **AC6.** Verify status surface updates: `git diff origin/main..HEAD -- PROJECT.md ROADMAP.md CHANGELOG.md` shows the §"Current empirical decision" / §"Current blocker" / §"Next action" patches on PROJECT.md; R1 status patch on ROADMAP.md (matching the AC5 decision — REVISE held or GO transition); CHANGELOG.md entry for this cycle.
- **AC7 (charter-drift check).** `git diff origin/main..HEAD -- README.md docs/concepts/coherence-path-hypothesis.md docs/concepts/support-path.md docs/articles/seven-ways-people-walk.md` must be empty. Cross-doc consistency check: empirical-state language (e.g., L cycle count, R1 status, decision) consistent across PROJECT.md / ROADMAP.md / CHANGELOG.md / field-report-01.
- **AC8 (data-policy regression).** `git diff origin/main..HEAD --name-only | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$' || echo NONE` must return NONE. If path (b) was taken, verify IK outputs landed in `/opt/gait-data/` (gitignored), not the repo.

**β additional verification (beyond AC ledger):**
- **Self-coherence completeness.** Verify `.cdr/unreleased/28/self-coherence.md` carries: §Gap, §Skills, §ACs (AC1–AC8 each with evidence), §Self-check, §Debt, §CDD-Trace (through step 7), §Pre-review gate (14 rows), §Review-readiness (round 1).
- **α identity discipline.** Confirm all cycle commits author as `alpha@cph.cdd.cnos`: `git log origin/main..origin/cycle/l-cycle-recovery --format='%h %ae' | grep -v 'alpha@cph.cdd.cnos' || echo CLEAN`.
- **Cross-cycle awareness.** Verify α's `self-coherence.md` names the partner cycle (cph#27 / `cycle/r3-rside-aggregate-analysis`) + the R1-binding rule + the recommended merge order.

**Output:** `.cdr/unreleased/28/beta-review.md` with: **Round 1** header (SHA reviewed / verdict); §3.11b γ-artifact presence observation (this scaffold exists at `.cdr/unreleased/28/gamma-scaffold.md`); per-AC subsection with independent oracle output; β additional verification; **Findings** (numbered F1, F2, … if any; otherwise "None"); **Verdict:** APPROVE | REQUEST CHANGES (RC). On APPROVE: merge to main, write `beta-closeout.md` (SHA of merge commit; ACs verified; findings; files merged), push main, delete cycle branch on origin. On RC: do not merge, name each finding with source surface + AC affected + specific patch direction + blocking vs non-binding, stay alive for re-review.
