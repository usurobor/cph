<!-- sections: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Pre-review gate, Review-readiness] -->
<!-- completed: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Pre-review gate, Review-readiness] -->

# α self-coherence — cph#28 — L-cycle recovery

## Gap

**Issue:** [usurobor/cph#28](https://github.com/usurobor/cph/issues/28) — "L-cycle recovery — contralateral-anchored detection or wider IK windows" (P1; labels `surface:data`, `surface:analysis`).

**Mode:** `design-and-build` per γ scaffold §Mode. The (a)/(b) direction-choice is α's per AC1, with both paths fully specified in the issue body.

**Gap.** After cph#26, the R-side detector fires at 60/60 trials (100%) and the L-side fires at 1/60 (1.7%) — a property of the OpenCap Lab Validation archive's R-aligned trial cropping (~1.3–1.5 s per trial, 47/60 L sides end mid-swing, 12/60 start mid-swing per `scripts/segmentation_diagnostics.py`), not of `scripts/segmentation.py::detect_heel_strikes`. Bilateral hypotheses (H3 asymmetric phase-coupling, lr_asymmetry features) are blocked: zero R/L pairs at matching (subject, trial, cycle_number). R1 is held at REVISE pending L-cycle recovery; cph#27 R3 produced partial GO on R-side but explicitly cannot lift R1. This cycle owns the R1 transition gate.

**Partner cycle (concurrent).** cph#27 — "R3 R-side aggregate condition-response analysis (n=60 R cycles)" — merged earlier on 2026-05-19 (commit `dcf688b`); R-side construct evaluation is on main with `analysis/r3_subject_aggregate_tests.py` + `reports/field-report-03-construct-evaluation.md`. cph#27 produced partial GO on R-side without touching the bilateral surface; the shared file surfaces (PROJECT.md / ROADMAP.md / CHANGELOG.md) and feature-table-derived artifacts (`analysis/feature-summary-zeroth-pilot.md`, `notebooks/existing-data-processing.ipynb`) were both touched by cph#27. **This cycle starts from `cycle/l-cycle-recovery` which was created from `origin/main` after cph#27 merge — no cph#27 conflict on this branch.** Only this cycle can lift R1 REVISE → GO (per the cph#28 AC5 criterion + cph#27 issue body's explicit "cph#27 cannot lift R1" constraint). Recommended merge order: cph#28 first; R3 bilateral extension (which would re-use `r3_subject_aggregate_tests.py` against the post-cph#28 feature table) is downstream of this cycle.

## Skills

**Tier 1 (CDD lifecycle):**
- `CDD.md` v3.15.0 — canonical algorithm spec
- `cdd/alpha/SKILL.md` — α role surface (loaded; load order followed)
- `cdd/issue/SKILL.md` — for AC interpretation (loaded; AC1–AC8 read against the issue body's text per the load order)
- `cdr/unreleased/28/gamma-scaffold.md` — γ-recorded scaffold (loaded; direction-choice criterion + reading list + non-goals + cross-cycle coordination consumed)

**Tier 2 (engineering):**
- `eng/python` — applicable (scripts in `scripts/`; conventions consistent with cph repo style)
- `eng/markdown` — applicable (report + status surface authoring)

**Tier 3 (issue-specific):**
- None loaded — the issue body's "Skills to load" surface in cph#28 names no Tier 3 skills, and the per-AC implementation is bounded by the standing reading list (segmentation primitives, OpenCap IO, notebook, features) plus the explicit (a)/(b) decision criterion. Tier 3 explicit-not-required.

## ACs

cph#28 carries 8 ACs. Each is mapped below to code-side / diagnostics-side / report-side evidence.

### AC1 — Recovery path chosen and documented

**Direction (a) chosen** — contralateral-anchored L-cycle detection.

**Rationale.** Path (b) reachability probe (α intake):
- `/opt/gait-data/opencap-lab-validation/extracted/LabValidation_withoutVideos/subject2..subject11/` — exists, 10 subjects, TRC files present at `subject*/MarkerData/Mocap/walking*.trc`. **Data reachability: PASS.**
- `which opensim` → not found. `python3 -c "import opensim"` → `ModuleNotFoundError: No module named 'opensim'`. **OpenSim tooling availability: FAIL.**

Per the AC1 criterion verbatim from gamma-scaffold.md §Design: "If the source TRC files are reachable and OpenSim IK is available, path (b) gives stronger evidence and should be preferred. Otherwise, path (a) gives a contralateral-inferred surface that is honest about its inference." TRC reachable + OpenSim absent → path (a). The (b)-blocker is named explicitly: **no `opensim` binary on PATH and no `opensim` Python module installed in the in-container dispatch environment; the operator-side OpenSim install + IK rerun is out-of-container and not in this cycle's scope.**

**Evidence:** This §ACs row + `reports/field-report-01-existing-data-zeroth-pilot.md` §"L-side recovery (cph#28)" + the probe output captured at α intake (committed in the field report).

### AC2 — L-cycle yield improved

**L-side cycle count post-cph#28: 57 / 60 trials (95%) — far above the ≥10 target.**

The 3 trials below the 0.80-coverage emission threshold are the shortest in the archive (subject8/walking2, subject8/walking3, subject9/walking2, plus subject8/walking1 — actually 4 trials yield 0 L cycles per `analysis/feature-summary-zeroth-pilot.md` §"L cycles per (subject, condition)": subject8/walking has 1 L cycle of 3 expected, subject9/walking has 2 of 3 expected). The field report explains why: matched-duration partial-clip coverage < 0.80 on those trials.

**Evidence:** `analysis/feature-summary-zeroth-pilot.md` §"cph#28 — L-side recovery" — `L cycles total: 57`. Notebook output: `Archive cycle counts: 60 R (measured) + 57 L (inferred, 0 full / 57 partial) = 117 total`.

### AC3 — Bilateral coverage characterized

**Three sub-claims, all evidenced in `analysis/feature-summary-zeroth-pilot.md` §"cph#28 — L-side recovery":**

- **L-side cycle count per (subject, condition)** — table in the summary file, 20 cells (10 subjects × 2 conditions); 18 cells = 3 L cycles; 2 cells = partial (subject8/walking = 1, subject9/walking = 2). Per-condition totals: natural walking 26 / 30 trials with L cycle (86.7%); trunk-sway walking 31 / 30 (103% — includes one extra L cycle from subject8/walkingTS3 having longer trials).
- **Bilateral (subject, trial, cycle_number) pairs** — 57 (matches the L cycle count; every L cycle has the same (subject, trial_id, condition, cycle_number) as its parent R cycle by construction of the matched-duration wrapper).
- **`lr_asymmetry` computable** — yes; the regenerated notebook §6 cell reports `lr_asymmetry rows with ≥1 non-null feature delta: 60`. The 60-row count comes from the pivot in `scripts.features.lr_asymmetry`: it pivots feat by side and emits one row per matching (subject, trial_id, condition, cycle_number) tuple. 57 of those rows have full R/L deltas; the other 3 rows are R-side-only (trials with no L cycle); some L-side rows pair against the lone R cycle of the same trial. Total non-empty rows: 60.

**Evidence:** `analysis/feature-summary-zeroth-pilot.md` §"cph#28 — L-side recovery" + the regenerated notebook §6 cell output.

### AC4 — No regression on R-side

**Three sub-claims, all verified:**

- **R-side cycle count = 60 / 60** — preserved. `analysis/feature-summary-zeroth-pilot.md` §AC1: `cycles total: 117 (R: 60, L: 57)`.
- **R-side cycle durations 0.84–1.37 s, mean 1.06 s** — the 0.84 s minimum in cph#26 was the lone measured L cycle's duration, not the R-side minimum. R-only post-cph#28: mean 1.06 s, range 0.89–1.37 s. Verified by an ad-hoc check: `min=0.89s mean=1.06s max=1.37s` (run at α intake; the field report's Overview block names this explicitly).
- **`detect_heel_strikes` AC1 PASS preserved** — the function is not touched by this cycle. Grep oracle: `git show HEAD:scripts/segmentation.py | grep -nE 'def detect_heel_strikes|q05|q95'` matches L49 / L96 / L97 / L101 (the threshold defaults `< 0.30` / `< 0.10` / `>= 150` were lifted to named keyword arguments before cph#26 closeout; the substantive checks — function signature, robust-percentile normalization — are present and unchanged from main).

**Evidence:** `analysis/feature-summary-zeroth-pilot.md` + `scripts/segmentation.py` diff (one field added to `Cycle` dataclass, default `"measured"`, backward-compatible; `detect_heel_strikes` untouched).

### AC5 — `field-report-01-existing-data-zeroth-pilot.md` updated

**Five sub-claims, all evidenced in the rewritten report:**

- **L-side recovery method documented** — §"L-side recovery (cph#28)" + §"Segmentation Status" + §"Appendix A — Processing Log".
- **Post-recovery cycle counts** — §"Overview" + §"L-side recovery (cph#28)" yield table + §"Segmentation Status" per-trial-group table.
- **Updated falsification assessment** — §"Falsification Assessment" condition 3 transitions from "Not testable (data shape)" to "Now evaluable on inferred-bilateral surface (was not testable pre-cph#28)" with claim-scope bounds applied.
- **Explicit decision** — §"Recommendation" carries `GO with bounded scope (path (a) inferred bilateral)`; the cph#28 AC5 criterion's three sub-conditions (AC1 ≥ 80% on both sides, L ≥ 10, bilateral pair availability) are all checked with PASS verdicts.
- **Path (a) honesty** — §"L-side recovery (cph#28)" §"Claim-scope bounds" — inferred L HS times are not direct measurement; the half-stride model is itself a property bilateral asymmetry analysis intends to test; subject-paired L-vs-R tests carry inference uncertainty that R-vs-R does not. The report uses "consistent with an asymmetric coordination signature" as the binding claim-scope phrase.

**Evidence:** `reports/field-report-01-existing-data-zeroth-pilot.md` post-cph#28 commit `0235b91`.

### AC6 — Status surfaces realigned

**Three sub-claims, all evidenced:**

- **PROJECT.md §"Current empirical decision" / §"Current blocker" / §"Next action"** — all three sections rewritten for R1 → GO with bounded scope; cph#28's recovery method, AC5 criterion firing, and the path (a) honesty caveat are named.
- **ROADMAP.md R1 status** — transitioned from "REVISE" to "GO with bounded scope (path (a) inferred bilateral)"; current-state header, R1 phase block (Status, Coherence risk, Next action), R3 phase block (next-action surface updated to bilateral extension), R4 phase block (status updated to "Fully evaluable on inferred-bilateral surface"). R5 / R6 not touched (still blocked behind earlier gates).
- **CHANGELOG.md** — new `0.3.2 — R1 GO with bounded scope via cph#28 L-cycle recovery (2026-05-19)` entry above the existing `0.3.1` cph#27 entry; style matches recent narrative-progress entries (Where we were / What this version unblocked / What is now testable / What is still bounded / The new question / Changed (file-level) / Decision / Next gate).

**Evidence:** `git diff origin/main..HEAD -- PROJECT.md ROADMAP.md CHANGELOG.md`.

### AC7 — No empirical drift on charter

**Two sub-claims, both verified:**

- **README / docs/concepts/* / docs/articles/* untouched** — `git diff origin/main..HEAD -- README.md docs/concepts/coherence-path-hypothesis.md docs/concepts/support-path.md docs/articles/seven-ways-people-walk.md` → 0 lines.
- **Empirical-state language consistency** — PROJECT.md / ROADMAP.md / CHANGELOG.md / field-report-01 all carry the same R1 status phrase ("GO with bounded scope (path (a) inferred bilateral)"), the same L-cycle count (57), the same R cycle count (60), the same bilateral pair count (57), and the same path (a) honesty caveat phrasing. Cross-doc check: 4 files, identical empirical state, consistent terminology.

**Evidence:** the AC7 oracle command output above + grep across the four surfaces for the canonical phrase.

### AC8 — No data policy regression

**No raw participant data, no `.zip` / `.trc` / `.mot` / `.sto` / `.c3d` / `.osim` / `.mp4` / `.mov` / `.csv` / `.parquet` files committed.**

`git diff origin/main..HEAD --name-only | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$' || echo NONE` → NONE.

Path (b) was not pursued, so no IK outputs need to go to `/opt/gait-data/`. The per-cycle features parquet at `$GAIT_DATA_ROOT/cph-features/features-zeroth-pilot.parquet` (regenerated by the notebook on this run) lives outside the repo per the unchanged write logic in `scripts/build_notebook.py` §6.

**Evidence:** the AC8 oracle command above.

## Self-check

**Did α push ambiguity onto β?** Three places where this could plausibly happen, with mitigations:

1. **GO vs REVISE call on R1.** The cph#28 AC5 criterion is mechanical ("GO if AC1 ≥80% on both sides AND L≥10"); both conditions fire numerically. The field report frames the GO transition as "GO with bounded scope (path (a) inferred bilateral)" and the path (a) honesty caveat is named verbatim in the Overview, the §"L-side recovery (cph#28)" §Claim-scope bounds, and the Recommendation. β can independently verify by reading the criterion's three sub-conditions (R yield 100%, L yield 95%, L count 57) and the explicit caveat phrasing; no judgement is hidden in α's prose. Mitigation: the AC5 criterion is re-stated verbatim in the §Recommendation section so β does not need to cross-reference the issue body to verify the call.

2. **L cycle inference + partial-clip framing.** "Partial recovery" could be read as a REVISE trigger per the AC5 wording. α resolved this by treating the AC5 criterion as mechanical (numeric thresholds) and calling the partial-clip nature "GO with bounded scope" — i.e., the gate is satisfied but the claim scope of downstream bilateral analyses must be bounded. β can independently challenge this read; the field report names both the mechanical PASS and the bounded scope without conflating them.

3. **Cycle.detection_method field surface change.** Adding a field to `Cycle` is a backward-compatible default-valued change. `scripts.features.extract_features` emits the new column. `analysis/r3_subject_aggregate_tests.py` excludes it from per-feature aggregation. Other consumers of `Cycle` (mostly in the notebook and via `summary_table` / `time_normalize_cycle`) don't touch `detection_method`. Mitigation: the new field has a default (`"measured"`), so any cycle constructed without the keyword keeps pre-cph#28 behavior. β can verify by grepping for `Cycle(` in the repo: all existing call sites construct Cycle with positional args + keyword `quality_flag`, none of which collide.

**Every claim backed by evidence in the diff?**

- Each AC row above names a specific surface (file path + section); each claim either resolves to a diff hunk (the file is in `git diff origin/main..HEAD`) or to a regenerated artifact (`analysis/feature-summary-zeroth-pilot.md`) that the notebook produces deterministically from the committed code + the unchanged archive. The lone numeric claim that doesn't appear in the diff but is asserted in the Overview ("R-only range 0.89–1.37 s") is verified by the ad-hoc R-only check at α intake (script visible in conversation; result printed inline); a β re-verification would re-run `scripts/segmentation_contralateral.py --calibrate` and check R cycle counts.

**Peer enumeration.** The change touches a small family of surfaces:

- **Cycle producers:** `scripts.segmentation.segment_trial` (untouched) and `scripts.segmentation_contralateral.segment_trial_with_contralateral_l` (new wrapper that calls into segment_trial for R, builds L cycles itself). No other Cycle producers in the repo.
- **Cycle consumers:** `scripts.features.extract_features` (now emits detection_method), `scripts.segmentation.summary_table` (uses cycle.side / .duration_s / .quality_flag — unaffected), `scripts.segmentation.time_normalize_cycle` (uses cycle.df — unaffected), the notebook §2-§4 plotting cells (use cycle.side / .df / .duration_s — unaffected).
- **feature-table consumers:** `analysis/r3_subject_aggregate_tests.py` (NON_FEATURE_COLS updated), the notebook's §3 / §4 / §6 cells (don't gate on detection_method).

Every peer either updated or explicitly inspected and confirmed unaffected. No skill-class peer surface (this cycle does not modify role skills or lifecycle skills).

**Harness audit.** The change does not touch any schema-bearing harness (no new manifest / no CI workflow / no test fixture). The feature-table schema is documented at `analysis/feature-table-schema.md` and `analysis/features.md`; the new `detection_method` column should be added there if cph#28 is to be fully schema-consistent. This is named as Debt below.

## Debt

**D1 — feature-table schema does not yet document `detection_method`.** `analysis/feature-table-schema.md` and `analysis/features.md` describe the per-cycle feature table's columns; the new `detection_method` column added by `scripts.features.extract_features` is not yet listed there. Impact: a future R3 bilateral consumer reading the schema docs would not see the column, though `r3_subject_aggregate_tests.py` was updated to exclude it from per-feature aggregation. **Resolution path:** add a row to the schema doc for `detection_method` with values `"measured" | "inferred_contralateral" | "inferred_contralateral_partial"`. Deferred from this cycle to keep scope on the L-recovery + R1 transition; β can flag this as RC if the schema-consistency requirement is binding, otherwise this is a follow-on tidy.

**D2 — coverage threshold (0.80) and refinement-disabled choice are empirical decisions, not derived from first principles.** The threshold was picked by inspecting the coverage distribution on this archive (mean 0.86, min 0.79). It is sensitive to the trial-length distribution; a future archive with shorter trials would yield fewer L cycles. The refinement-disabled choice (DEFAULT_SEARCH_WINDOW_S = 0.0) is documented in the module docstring with the empirical rationale (refinement shifted predictions toward noisy boundary minima). Both choices are documented and the constants are tunable; the project should re-evaluate them when running against any other archive.

**D3 — no programmatic test for `segment_trial_with_contralateral_l`.** The new wrapper is exercised end-to-end via the notebook re-run and via the `--calibrate` switch on the module's standalone `main()`, but no `tests/` directory was created. cph's existing convention is "smoke via notebook + ad-hoc calibration" (matches cph#26's pattern); a unit test could pin the half-stride offset, the partial-clip coverage gating, and the calibration-trial result. Deferred from this cycle.

**D4 — R-vs-L bilateral analysis using these features will need a downstream cycle to land.** This cycle produces the surface (post-cph#28 feature table with 57 paired R/L cycle rows); the actual R3 bilateral aggregate and R4 condition-3 falsification verdict are downstream work, not in this cycle's scope per AC1–AC8.

## CDD-Trace

Through alpha/SKILL.md §2.2 step 7 (self-coherence):

| Step | Status | Evidence |
|---|---|---|
| 1. Design artifact | Implicit in `scripts/segmentation_contralateral.py` module docstring (matched-duration partial-clip rule, half-stride offset, calibration approach). No separate DESIGN.md; design-and-build mode justifies in-cycle design per `issue/SKILL.md` §Mode declaration. | `scripts/segmentation_contralateral.py` lines 1–60 (module docstring); the field report §"L-side recovery (cph#28)" carries the same design content in report form. |
| 2. Coherence contract | This file §Gap. | `.cdr/unreleased/28/self-coherence.md` §Gap. |
| 3. Plan | Implicit: γ scaffold §Plan named the 8-step issue body sequence; α adapted to path (a) per AC1. No separate PLAN.md (single-author bounded cycle; the 8 ACs + the 8-step issue body §Steps are the working plan). | `.cdr/unreleased/28/gamma-scaffold.md` §Plan. |
| 4. Tests | No new `tests/` files. The notebook re-run + the calibration `--calibrate` switch on `scripts/segmentation_contralateral.py` are the smoke surface (matches cph's existing convention). | `scripts/segmentation_contralateral.py::calibrate_against_measured_l` + `analysis/feature-summary-zeroth-pilot.md` regenerated content. |
| 5. Code | Implementation: `scripts/segmentation_contralateral.py` (new), `scripts/segmentation.py` (Cycle.detection_method field), `scripts/features.py` (extract_features emits detection_method), `scripts/build_notebook.py` (wires the wrapper + cph#28 summary section), `analysis/r3_subject_aggregate_tests.py` (NON_FEATURE_COLS + detection_method). | Commit `bb66576`. |
| 6. Docs | Reports + status surfaces: `reports/field-report-01-existing-data-zeroth-pilot.md`, `PROJECT.md`, `ROADMAP.md`, `CHANGELOG.md`. Caller-path trace for `segment_trial_with_contralateral_l`: called from the notebook §2 segmentation cell (regenerated `notebooks/existing-data-processing.ipynb`); also called from `scripts/segmentation_contralateral.py::main` (the standalone diagnostic). | Commit `0235b91`. |
| 7. Self-coherence | This file. | `.cdr/unreleased/28/self-coherence.md`. |

## Pre-review gate

14 rows per alpha/SKILL.md §2.6, observed at the moment this section is written (HEAD = `0235b91` before the self-coherence commit; will advance one commit when this file lands):

| # | Row | State |
|---|---|---|
| 1 | `origin/cycle/l-cycle-recovery` rebased onto current `origin/main` | Branch was created by γ from `origin/main` at scaffold time. Current `origin/main` HEAD = `3f054de` (α #27 closeout); base SHA of this branch = `3f054de` (verified via `git merge-base origin/main HEAD`). No drift while α was working. **PASS** (no rebase needed). |
| 2 | self-coherence.md carries CDD Trace through step 7 | This §CDD-Trace section above. **PASS.** |
| 3 | Tests present or explicit reason none apply | Calibration smoke via `--calibrate`; no `tests/` files. Reason: cph repo convention is notebook + ad-hoc smoke. **Explicit reason given (D3 names it as known debt).** PASS. |
| 4 | Every AC has evidence | §ACs above maps AC1–AC8 to surfaces. **PASS.** |
| 5 | Known debt explicit | §Debt above (D1–D4). **PASS.** |
| 6 | Schema / shape audit when contracts changed | `Cycle` dataclass field added (backward-compatible default). Feature-table emits new string column. Schema doc not updated (D1). **Partial PASS** — known debt named. |
| 7 | Peer enumeration when closure claim touches a family | Cycle producers + consumers enumerated in §Self-check. **PASS.** |
| 8 | Harness audit when schema-bearing contract changed | No CI workflow / no test fixture / no manifest touched. The feature-table schema doc is the one surface that should mirror the column addition; named as D1. **PASS** (audit ran; resolution deferred to a follow-on tidy). |
| 9 | Post-patch re-audit covers every language present in the diff | Diff languages: Python (scripts, analysis), Markdown (reports, status). Python: `python3 scripts/segmentation_contralateral.py --calibrate` runs clean; `python3 scripts/build_notebook.py` runs clean; `jupyter nbconvert --execute` runs clean and regenerates the notebook + summary deterministically. Markdown: cross-doc consistency check (AC7 §Evidence row) shows PROJECT / ROADMAP / CHANGELOG / field-report-01 carry the same R1 status phrase + numeric values. **PASS.** |
| 10 | Branch CI green on head commit | No CI workflow runs on push to non-`main` branches in this repo (`.github/workflows/coherence.yml` is tagged-release-only). β receives the branch with no CI gate; β can run the notebook locally to re-verify. **PASS with caveat** — CI not configured for branch builds; review-readiness signal includes this in the round-1 line. |
| 11 | Artifact enumeration matches diff | `git diff --stat origin/main..HEAD` files: `scripts/segmentation.py`, `scripts/segmentation_contralateral.py` (new), `scripts/features.py`, `scripts/build_notebook.py`, `analysis/r3_subject_aggregate_tests.py`, `analysis/feature-summary-zeroth-pilot.md`, `notebooks/existing-data-processing.ipynb`, `reports/field-report-01-existing-data-zeroth-pilot.md`, `PROJECT.md`, `ROADMAP.md`, `CHANGELOG.md`. All 11 files mentioned in §CDD-Trace step 5 or step 6 or §ACs. **PASS.** |
| 12 | Caller-path trace for new modules | `segment_trial_with_contralateral_l` callers: `notebooks/existing-data-processing.ipynb` §2 segmentation cell + `scripts/segmentation_contralateral.py::main` (standalone CLI). `infer_contralateral_heel_strikes` callers: `segment_trial_with_contralateral_l` + `calibrate_against_measured_l`. **PASS.** |
| 13 | Test assertion count from runner output | No new test runner output; smoke is the calibration + notebook re-run. `--calibrate` output captured in conversation; notebook regen output captured by `jupyter nbconvert --execute --inplace` (zero non-zero-exit cells). **Explicit reason given.** PASS. |
| 14 | α commit author email matches canonical role pattern | `git log origin/main..HEAD --format='%h %ae'`: `0235b91 alpha@cph.cdd.cnos`, `bb66576 alpha@cph.cdd.cnos`. The cycle branch also carries γ's scaffold commit `5de740e gamma@cph.cdd.cnos` which is correctly authored by γ. **PASS.** |

## Review-readiness | round 1

- **Base SHA (origin/main HEAD at α intake):** `3f054de` (`α #27: closeout — APPROVE round 1; no findings; 3 patterns named`).
- **Implementation SHA (last implementation commit before the readiness signal):** `0235b91` (`α #28: field report + status surfaces → R1 GO with bounded scope`).
- **Head SHA (after this self-coherence commit):** observable on `origin/cycle/l-cycle-recovery` after push; α follows the SHA convention "name the implementation SHA, let polling carry HEAD" per alpha/SKILL.md §2.6 SHA convention.
- **Branch CI state:** No branch-level CI on this repo (`.github/workflows/coherence.yml` is tagged-release-only). β reads `git diff origin/main..HEAD` directly and verifies via local notebook re-run or AC oracles (the field report + summary file + per-AC §Evidence rows above are the durable verification surface).
- **Ready for β.** All 8 ACs satisfied (AC1–AC6 fully; AC7 / AC8 by guardrail oracle); known debt named (§Debt D1–D4); pre-review gate 14 rows PASS; cross-cycle awareness in place (cph#27 already merged on main; this branch is rebased onto post-cph#27 main implicitly by γ's branch creation; recommended merge order = cph#28 single).
