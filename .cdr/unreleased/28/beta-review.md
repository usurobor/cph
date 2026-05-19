<!-- sections: [Round 1, γ-artifact presence, AC verification, β additional verification, Findings, Verdict] -->
<!-- completed: [Round 1, γ-artifact presence, AC verification, β additional verification, Findings, Verdict] -->

# β review — cph#28 — L-cycle recovery

## Round 1

- **Round:** 1
- **Base SHA (origin/main at β intake):** `3f054de` (`α #27: closeout — APPROVE round 1; no findings; 3 patterns named`)
- **Head SHA (origin/cycle/l-cycle-recovery):** `39fdd83` (`α #28: self-coherence + review-readiness (round 1)`)
- **Linearity:** origin/main is an ancestor of origin/cycle/l-cycle-recovery → fast-forwardable
- **Non-destructive merge test:** auto-merge succeeded in throwaway worktree, 0 unmerged paths, 13 files modified/added (worktree torn down)
- **Branch CI state:** No branch-level CI configured on this repo (`.github/workflows/coherence.yml` is tagged-release-only per α's review-readiness signal); β verified via direct AC oracles and notebook output cross-check
- **Verdict:** **APPROVE**

## §3.11b — γ-artifact presence

`.cdr/unreleased/28/gamma-scaffold.md` exists on origin/cycle/l-cycle-recovery at commit `5de740e` (author `gamma@cph.cdd.cnos`). 186 lines; contains Issue / Mode / Design / Plan / ACs / Cycle scope sizing / Cross-cycle coordination / α dispatch surface / β dispatch surface sections. α's `self-coherence.md` §Skills explicitly cites it: "cdr/unreleased/28/gamma-scaffold.md — γ-recorded scaffold (loaded; direction-choice criterion + reading list + non-goals + cross-cycle coordination consumed)". Pre-merge gate row 4 (γ artifact completeness): **PASS**.

## AC verification

### AC1 — Recovery path chosen and documented

α picked path (a). Independent reachability probe at β intake:

```
$ ls /opt/gait-data/opencap-lab-validation/extracted/LabValidation_withoutVideos/
desktop.ini subject10 subject11 subject2 subject3 subject4 subject5 subject6 subject7 subject8 subject9
$ which opensim
(not on PATH)
$ python3 -c "import opensim"
ModuleNotFoundError: No module named 'opensim'
```

TRC reachability PASS; OpenSim tooling availability FAIL. Per the AC1 criterion verbatim ("If the source TRC files are reachable and OpenSim IK is available, path (b) gives stronger evidence and should be preferred. Otherwise, path (a) gives a contralateral-inferred surface that is honest about its inference"), α's choice of (a) is mechanically correct. The (b)-blocker is named explicitly in `self-coherence.md` §AC1 and in `reports/field-report-01-existing-data-zeroth-pilot.md` §"L-side recovery (cph#28)": "OpenSim tooling (`opensim` binary on PATH and `opensim` Python module) is not available in the in-container dispatch environment".

**PASS.**

### AC2 — L-cycle yield improved

Target: ≥10 L cycles across 60 trials. Observed:

- `analysis/feature-summary-zeroth-pilot.md` §"cph#28 — L-side recovery": `L cycles total: 57 (0 full / 57 partial / 0 measured-ipsilateral)`
- Notebook §6 cell output (cross-check): `Archive cycle counts: 60 R (measured) + 57 L (inferred, 0 full / 57 partial) = 117 total`
- 57 / 60 trials = 95.0% yield; 57 cycles ≫ 10 target

Three trials below the 0.80-coverage emission threshold (subject8/walking2, subject8/walking3, subject9/walking2 — the shortest trials in the archive) are documented as `subject8/walking = 1 of 3 expected`, `subject9/walking = 2 of 3 expected` in the per-(subject, condition) table. Field report explains why.

**PASS.**

### AC3 — Bilateral coverage characterized

Three sub-claims, all evidenced in `analysis/feature-summary-zeroth-pilot.md` §"cph#28 — L-side recovery":

- L-side cycle count per (subject, condition): 20-cell table (10 subjects × 2 conditions); 18 cells at 3, subject8/walking at 1, subject9/walking at 2.
- Bilateral (subject, trial, cycle_number) pairs: 57 (matches L count by construction of the matched-duration wrapper).
- `lr_asymmetry` features computable: 60 non-empty rows. Notebook §6 cell output corroborates.

Cross-check against the notebook .ipynb JSON: the printed `Archive cycle counts` line is the deterministic regenerated output and matches the summary file.

**PASS.**

### AC4 — No regression on R-side (high importance)

Independent grep oracle on the post-cph#28 detector:

```
$ git show HEAD:scripts/segmentation.py | grep -nE 'def detect_heel_strikes|q05|q95'
49:def detect_heel_strikes(heel_y: np.ndarray, fs: float,
96:    q05 = float(np.percentile(smooth, 5))
97:    q95 = float(np.percentile(smooth, 95))
```

`git diff origin/main..HEAD -- scripts/segmentation.py`: only an 8-line backward-compatible addition to the `Cycle` dataclass (new field `detection_method: str = "measured"`). The `detect_heel_strikes` function body and signature are byte-identical to the post-cph#26 form on `origin/main`. `quality_flag` tri-value (`"ok" | "short" | "long"`) preserved at line 173 (was line 165 on main). The threshold defaults (`stance_thr: float = 0.30`, etc.) are present as named keyword arguments per α's note in self-coherence §AC4 — the substantive checks are unchanged.

R-side cycle count = 60/60 (`feature-summary-zeroth-pilot.md` §AC1: `cycles total: 117 (R: 60, L: 57)`); R-side durations preserved (R-only range 0.89–1.37 s, mean 1.06 s — the 0.84 s minimum from cph#26 was the lone measured L cycle, not the R-side minimum, and the field report §Overview names this explicitly).

**PASS.**

### AC5 — `field-report-01-existing-data-zeroth-pilot.md` updated

Five sub-claims:

- **L-side recovery method documented:** §"L-side recovery (cph#28)" + §"Segmentation Status" + §"Appendix A — Processing Log" (2026-05-19 entry).
- **Post-recovery cycle counts:** §"Overview" + §"L-side recovery (cph#28)" yield table + §"Segmentation Status" per-trial-group table.
- **Updated falsification assessment:** §"Falsification Assessment" condition 3 row transitions to "Now evaluable on inferred-bilateral surface (was not testable pre-cph#28)".
- **Explicit decision:** §"Recommendation" carries "GO with bounded scope (path (a) inferred bilateral)" with all four AC5 sub-conditions checked (R 100% ✓, L 95% ✓, L count 57 ✓, bilateral pair availability 57 ✓).
- **Path (a) honesty:** §"L-side recovery (cph#28)" §"Claim-scope bounds" + §"Overview" + §"Recommendation". Binding phrase "consistent with an asymmetric coordination signature" used uniformly.

**PASS** with one non-binding observation flagged below (O1) — Falsification §Score paragraph and Go/No-Go §Criteria Evaluation table carry stale pre-cph#28 text that is not contract-bearing (the binding contract surfaces — the per-condition table row 3 and the Recommendation prose — are updated).

### AC6 — Status surfaces realigned

```
$ git diff --stat origin/main..HEAD -- PROJECT.md ROADMAP.md CHANGELOG.md
 CHANGELOG.md | 40 ++++++++++++++++++++++++++++++++++++++++
 PROJECT.md   | 13 ++++++-------
 ROADMAP.md   | 24 ++++++++++++------------
```

- PROJECT.md: §"Current empirical decision" + §"Current blocker" + §"Next action" + §"Open issues" + §"Last field report" all rewritten for R1 GO with bounded scope.
- ROADMAP.md: §"Current state" + R1 phase block (Status: "GO with bounded scope (path (a) inferred bilateral)") + R3 phase block (next-action surface updated to bilateral extension) + R4 phase block (status updated to "Fully evaluable on inferred-bilateral surface"). R5 / R6 untouched (still blocked behind earlier gates).
- CHANGELOG.md: new `0.3.2 — R1 GO with bounded scope via cph#28 L-cycle recovery (2026-05-19)` entry, narrative-progress form, file-level Changed list, Decision, Next gate.

**PASS.**

### AC7 — No empirical drift on charter

```
$ git diff origin/main..HEAD -- README.md docs/concepts/coherence-path-hypothesis.md docs/concepts/support-path.md docs/articles/seven-ways-people-walk.md | wc -l
0
```

Charter docs untouched. Cross-doc consistency: PROJECT.md / ROADMAP.md / CHANGELOG.md / field-report-01 all carry the same R1 status phrase ("GO with bounded scope (path (a) inferred bilateral)"), the same L cycle count (57), the same R cycle count (60), the same bilateral pair count (57), and the same path (a) honesty caveat phrasing. No stale "L=1" / "60 R + 1 L" / "REVISE" survivors in the in-scope surfaces.

**PASS.**

### AC8 — No data policy regression

```
$ git diff origin/main..HEAD --name-only | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$'
NONE
$ git ls-files | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$'
NONE
```

Path (a) was taken; no IK rerun outputs need to land. The per-cycle features CSV at `$GAIT_DATA_ROOT/cph-features/features-zeroth-pilot.csv` is regenerated outside the repo per the unchanged write logic.

**PASS.**

## β additional verification

1. **γ-artifact presence:** PASS (§3.11b above).
2. **Self-coherence completeness:** `.cdr/unreleased/28/self-coherence.md` carries §Gap, §Skills, §ACs (AC1–AC8 each with code-side and report-side evidence), §Self-check (3 plausibility-of-ambiguity items + peer enumeration + harness audit), §Debt (D1–D4), §CDD-Trace (7 rows through step 7), §Pre-review gate (14 rows), §Review-readiness (round 1 with base SHA `3f054de` / implementation SHA `0235b91` / branch CI state caveat / "Ready for β" line). **PASS.**
3. **α identity discipline:** `git log origin/main..origin/cycle/l-cycle-recovery --format='%h %ae' --invert-grep --author='gamma@cph.cdd.cnos' | grep -v 'alpha@cph.cdd.cnos'` → CLEAN. All α commits author as `alpha@cph.cdd.cnos`; γ scaffold at `5de740e` correctly authors as `gamma@cph.cdd.cnos`. **PASS.**
4. **Cross-cycle awareness in self-coherence:** §Gap explicitly names the partner cycle ("cph#27 — R3 R-side aggregate condition-response analysis"), the partner branch (`cycle/r3-rside-aggregate-analysis`), the R1-binding rule ("Only this cycle can lift R1 REVISE → GO"), and the recommended merge order. α updates the original dispatch context with the observed state: cph#27 has already merged on 2026-05-19 (commit `dcf688b`); β confirmed via `git log origin/main` (`dcf688b` present, branch deleted from origin). The merge-order coordination question is therefore moot. **PASS** (non-binding observation per scaffold).
5. **R1 transition discipline (high importance):** AC5 binding precondition for R1 REVISE → GO = AC1 ≥80% on both sides AND L≥10. Independently verified:
   - R-side AC1: 60/60 = 100.0% ≥ 80% ✓
   - L-side AC1: 57/60 = 95.0% ≥ 80% ✓
   - L count: 57 ≥ 10 ✓

   The R1 GO transition is **licit**. The field-report Recommendation, PROJECT.md "Current empirical decision", and ROADMAP.md R1 phase block all correctly apply the bounded-scope qualifier (path (a) inferred bilateral) to the GO call. **PASS.**

## Findings

**Binding findings:** None.

**Non-binding observations:**

- **O1 — stale text drift in `reports/field-report-01-existing-data-zeroth-pilot.md`.** The Recommendation subsection (the AC5 binding contract) is updated and consistent with the cph#28 outcome. Three cosmetic remnants of the prior REVISE state remain in the report and could mislead a casual reader:
  1. §"Falsification Assessment" §"Falsification Score" paragraph still reads "1 blocked on data shape (condition 3)" though the per-condition table row 3 above was updated to "Now evaluable on inferred-bilateral surface".
  2. §"Go/No-Go Assessment" §"Criteria Evaluation" table column "This cycle (post-fix)" still references cph#26-era state (e.g., "Segmentation L-side nonzero: 1") rather than cph#28-era state (L=57); the Recommendation subsection immediately below correctly cites L=57.
  3. §"Next Phase Preparation" §"If REVISE (current recommendation) — Protocol Modifications" labels REVISE as "current recommendation" though the actual Recommendation is GO with bounded scope.

  Classification: cosmetic / docs-coherence drift. The AC5 binding contract is satisfied (the per-condition falsification table, the Recommendation prose, the cycle-count tables in Overview and Segmentation Status, and the path (a) honesty caveat are all updated coherently). Naming as observation not finding because: (a) the contract surfaces are updated, (b) the cross-doc consistency check (PROJECT/ROADMAP/CHANGELOG/field-report-01 Recommendation) is coherent on the binding empirical state, (c) AC7 cross-doc check passes — no stale empirical-state language in the surfaces named by AC7. β does not block merge on prose tidy; the operator or a follow-on docs cycle may refresh these subsections.

## Verdict

**APPROVE — Round 1.**

All 8 ACs pass on independent oracles. R1 GO transition precondition is mechanically satisfied (AC1 100% R, 95% L, L count 57). Path (a) honesty caveat is operational across all in-scope surfaces. R-side detector is preserved (byte-identical function body). No data files committed; no charter drift; γ scaffold artifact present; α identity clean. Non-destructive merge test against `origin/main` succeeded with 0 unmerged paths.

Proceeding to merge.
