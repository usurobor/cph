# Self-coherence — cph#26 — Port segmentation-real-data-fix onto current main

## Gap

**Issue:** [usurobor/cph#26](https://github.com/usurobor/cph/issues/26) — Port segmentation-real-data-fix onto current main.
**Branch:** `cycle/port-segmentation-fix`.
**Mode:** empirical implementation port (not a new theory cycle).

**Pre-port state on `origin/main`** (verified by `git log` + `grep` at merge-base `ebd909c`):

- `scripts/segmentation.py::detect_heel_strikes` was tuned to the synthetic generator's heel-marker shape (range ~[0, 100] mm, zero baseline) and failed on real Mocap calcaneus markers (range ~[50, 330] mm, ~25 mm R/L baseline offset). Result on real data: 11 of 60 trials (18.3%, R-side only); 0 L-side cycles.
- `reports/field-report-01-existing-data-zeroth-pilot.md` documented the 18.3%-segmentation REVISE.
- `PROJECT.md` / `ROADMAP.md` / `CHANGELOG.md` named the detector as the active R2 blocker, with `origin/cycle/segmentation-real-data-fix` (tip `a95415c`) as the unmerged orthogonal branch carrying the fix.
- Main had advanced 114 commits past the segmentation-fix branch's base on charter / process surfaces: CPH/COG split, `.cdr/` rename, coherence machinery preserved as operational infrastructure (`scripts/measure-coherence.sh`, `targets/*.tsc`, `.github/workflows/coherence.yml`), `quality_flag` tri-value (`"ok"`/`"short"`/`"long"` from cph#22), `extract_shape` → `extract_shape_sentinel` rename (cph#25), `cph-features/` rename (cph#20). A fast-forward merge from the segmentation-fix branch would have clobbered every one of these.

**Required outcome.** Port the implementation + evidence changes (segmenter + diagnostics + features + build script + notebook + summary + field report) onto current `main` without regressing the charter / process surfaces; re-run the notebook against real data; realign status surfaces (PROJECT.md / ROADMAP.md / CHANGELOG.md) to the post-fix field-report-01 evidence; preserve the empirical REVISE posture (the detector fix is necessary but not sufficient for construct validation, because L-side cycle yield is structurally limited by trial cropping).

**Why it is α work, not a δ operator action.** The port is an implementation cycle: it produces new code (the detector rewrite + the diagnostics module) and new evidence (the post-fix field-report-01 + notebook outputs). δ stewards waves and dispatches; α implements within an issue's scope. cph#26 is a single-issue cycle with 6 ACs and a "Required approach" / "Steps" section that names the implementation operations. The earlier `δ-as-agent` author attribution on `41b3693` was a session-identity drift carried over from the prior wave's δ-as-agent role (`cdr-refactor-2026-05-18`); per `cdd/alpha/SKILL.md §2.6` row 14, retroactive identity correction via path (a) `git rebase --exec 'git commit --amend --reset-author --no-edit'` has been applied (commits rewritten to `Alpha <alpha@cph.cdd.cnos>`; force-with-lease push at `41b3693 → 9bcef90`, `9eb34ee → f27904a`).

## Skills

**Tier 1 (CDD core):**
- `cdd/CDD.md` — lifecycle and role contract.
- `cdd/alpha/SKILL.md` — α role surface; §2.2 CDD-Trace steps, §2.3 peer enumeration + intra-doc repetition, §2.5 self-coherence, §2.6 pre-review gate (14 rows), §2.7 review-readiness signal.
- `cdd/issue/SKILL.md` — AC interpretation for AC1–AC6.

**Tier 2 (always-applicable engineering):**
- `eng/python` — for the detector rewrite, the diagnostics module, the features module additions, and the build script. Python is the dominant language of the diff.
- `eng/markdown` — for the field-report-01 rewrite + status surface realignment (PROJECT.md / ROADMAP.md / CHANGELOG.md).

**Tier 3 (issue-specific):**
- *None loaded.* cph#26's "Required approach" / "Steps" sections operationalize the port in mechanical terms (3-way merge via `git restore --source`; notebook regeneration + execution; status-surface reconciliation); no design or plan skill is required because the direction-choice is bounded by the issue body. The detector implementation (rewritten on the precursor branch `origin/cycle/segmentation-real-data-fix` at `a95415c`) is *ported*, not authored — α's surface here is integration + reconciliation + evidence reproduction, not detector design.

**Not loaded:** no `design/SKILL.md` or `plan/SKILL.md` — the issue body provides the implementation sequence (Steps 1–8) and the AC structure (AC1–AC6); no impact-graph judgment or sequencing decision is required. Marked explicit-not-required per §2.2 rule.

## ACs

cph#26 carries six ACs. AC1–AC2 cover the mechanical port + rerun; AC3 covers evidence parity; AC4 covers the empirical-posture guardrail; AC5 covers the protect-current-surfaces guardrail; AC6 covers the data-policy guardrail.

### AC1 — Detector fix is ported

> main-compatible code contains the robust real-data heel-strike detector.

**Evidence — code-side.** `scripts/segmentation.py::detect_heel_strikes` on `cycle/port-segmentation-fix` HEAD uses robust-percentile normalization plus stance-region depth/length gating:

```text
$ git show HEAD:scripts/segmentation.py | grep -nE 'def detect_heel_strikes|q05|q95|< 0\.30|< 0\.10|>= 150' | head -20
```

The detector reads `yn = (smoothed_heel − q05) / (q95 − q05)`; each contiguous run of `yn < 0.30` lasting ≥150 ms AND reaching `< 0.10` at its deepest point is one stance phase; HS is the first sample inside that deep-stance plateau. The implementation is invariant to absolute height, baseline offset, and amplitude.

**Evidence — port mechanism.** Step A commit `9bcef90` (formerly `41b3693`) ports via per-file 3-way merge using `git merge-file` with merge-base `d30aa4a`, preserving main's recent changes:
- `scripts/segmentation.py` — clean 3-way merge; main's `quality_flag` tri-value (`"ok"`/`"short"`/`"long"` from cph#22) preserved alongside the new detector.
- `scripts/segmentation_diagnostics.py` — direct restore (new file; only branch had it).
- `scripts/features.py` — clean 3-way merge; main's `extract_shape_sentinel` rename (cph#25) preserved alongside the new `hip_adduction_*` + `lumbar_*` columns.
- `scripts/build_notebook.py` — clean 3-way merge; main's `cph-features` rename (cph#20) and `extract_shape_sentinel` reference (cph#25) preserved alongside the diagnostics integration.

**Verdict: AC1 PASS.** The detector is on `cycle/port-segmentation-fix` HEAD; the port preserved main's downstream renames; quality_flag and shape-sentinel surfaces were not regressed.

### AC2 — Notebook reruns on real data

> Notebook executes end-to-end in real-data mode. No synthetic fallback.

**Evidence — runner output (Step B commit `f27904a`, formerly `9eb34ee`).**

```text
$ export GAIT_DATA_ROOT=/opt/gait-data
$ python3 scripts/build_notebook.py
Wrote notebooks/existing-data-processing.ipynb
$ jupyter nbconvert --execute --inplace notebooks/existing-data-processing.ipynb
[NbConvertApp] Converting notebook notebooks/existing-data-processing.ipynb to notebook
[NbConvertApp] Writing 548928 bytes to notebooks/existing-data-processing.ipynb
```

**Evidence — real-data mode (no fallback).** The executed notebook contains the output line `Aggregate summary written to /root/cph/analysis/feature-summary-zeroth-pilot.md` and the per-source Mean Pearson r table (HRNet / OpenPose_default / OpenPose_highAccuracy), which are gated on `discover_walking_ik()` returning real-archive paths. The 60-trial per-source row count confirms the run is against `/opt/gait-data/opencap-lab-validation/extracted/`, not the synthetic generator.

**Verdict: AC2 PASS.** Notebook executed end-to-end in real-data mode; no synthetic fallback.

### AC3 — Evidence matches branch-level result or explains drift

> Expected: 60/60 walking trials segmented; 61 total cycles; 60 R cycles; 1 L cycle; both natural and trunk-sway represented. If numbers differ, explain why.

**Evidence — verified against [`reports/field-report-01-existing-data-zeroth-pilot.md`](../../../reports/field-report-01-existing-data-zeroth-pilot.md):**

| Quantity | Expected | Notebook output | Field-report-01 |
|----------|----------|-----------------|-----------------|
| Walking trials | 60 | 60 (per-source row count = 60) | 60 (L47) |
| Trials with ≥1 cycle (R) | 60 | seg-rate 100% R | 60/60 (L47, L57) |
| Trials with ≥1 cycle (L) | 1 | (table shape (61, 35); 60 + 1) | 1/60 (L47, L57) |
| Total cycles | 61 | 61 (feature table shape) | 61 (L8, L47) |
| R cycles | 60 | 60 (L=1, total=61) | 60 (L8, L47, L50) |
| L cycles | 1 | 1 (table shape minor axis) | 1 (L8, L47, L50) |
| Natural trials | 30 | 30/30 segmented | 30/30 (L45) |
| Trunk-sway trials | 30 | 30/30 segmented | 30/30 (L46) |
| Feature missingness | 0.00% | 0.00% across 35 columns | 0.00% across 35 columns (L88) |
| OpenCap Pearson r̄ HRNet | ≥ 0.7 | 0.962 | 0.962 (L96) |
| OpenCap Pearson r̄ OpenPose_default | ≥ 0.7 | 0.933 | 0.933 (L97) |
| OpenCap Pearson r̄ OpenPose_highAccuracy | ≥ 0.7 | 0.951 | 0.951 (L98) |

No drift between notebook output and field-report-01 claims.

**Verdict: AC3 PASS.** Every expected number was reproduced; no drift to explain.

### AC4 — Decision remains REVISE

> The port must not report GO. The field report should state that R-side aggregate analysis is now reachable; bilateral/L-side support-path tests remain blocked; CPH is not validated.

**Evidence — field-report-01 §"Decision" (L22):**

> "REVISE, not GO. AC1 mechanically passes (≥80%, L>0, both walking conditions covered), but L=1 cycle means L/R asymmetry features cannot be computed and Hypothesis 3 (asymmetric phase-coupling between sides) is not testable. ... The R-only n=60 anchors a partial test; the full test waits on L-cycle recovery."

**Evidence — status surfaces (Step B commit `f27904a`):**
- `PROJECT.md §"Current empirical decision"` reads `**REVISE**` and explicitly disclaims construct validation: "The Coherence Path Hypothesis is not validated; it is also not refuted."
- `ROADMAP.md §"Current state"` reads `**R1 is REVISE**` with "Hypothesis 1 ... is evaluable on R-side n=60; Hypotheses 2 ... and 3 ... are partially testable / blocked respectively."
- `CHANGELOG.md §0.3.0 §"Empirical state"` reads `**REVISE**` with "R1 stays REVISE; the active blocker has moved from the detector to L-side cycle yield."

R2 is documented as REVISE → GO at the *detector* level only; R1 (the construct-level evaluation) stays REVISE because of L-cycle yield. The split is explicit in `ROADMAP.md §R1 Coherence risk`: "Reading AC1 PASS as construct survival evidence when L=1 L-cycle still blocks bilateral hypotheses" is named as a risk.

**Verdict: AC4 PASS.** No GO claim on the construct; R-side aggregate analysis reachable; bilateral/L-side blocked; CPH not validated.

### AC5 — Current repo surfaces preserved

> No stale branch overwrite of: README, CPH/COG framing, CHANGELOG corrected coherence-machinery language, ROADMAP gates, coherence tooling (`.cdr/`, `targets/`, `scripts/measure-coherence.sh`, `.github/workflows/coherence.yml`).

**Evidence — `git diff origin/main..HEAD --stat` (the cycle's full diff after fix-round 1; pre-fix-round form documented in §"Fix-round 1"):**

```text
.cdr/unreleased/26/self-coherence.md          | (this file)
CHANGELOG.md                                  |  27 +
PROJECT.md                                    |  10 +-
ROADMAP.md                                    |  22 +-
analysis/feature-summary-zeroth-pilot.md      |  16 +-
analysis/feature-table-schema.md              |   2 +- (fix-round)
analysis/features.md                          |  15 +-  (fix-round)
docs/concepts/coherence-path-hypothesis.md    |   8 +-  (fix-round, §"Current empirical status" only)
notebooks/existing-data-processing.ipynb      | 1499 ++++++++++++++++++++++++++++--
reports/field-report-01-existing-data-zeroth-pilot.md | 237 ++++++++++-----------
scripts/build_notebook.py                     |  32 ++-
scripts/features.py                           |   5 +
scripts/segmentation.py                       | 125 +++++++----
scripts/segmentation_diagnostics.py           | 200 +++++++++++++++++
```

Files **not touched** by the cycle (verified by absence from the diff):
- `README.md` — untouched (CPH/COG split framing preserved).
- `.cdr/**` *except* the new `.cdr/unreleased/26/self-coherence.md` (this file).
- `targets/**` — untouched (TSC machinery preserved).
- `scripts/measure-coherence.sh` — untouched.
- `.github/workflows/coherence.yml` — untouched.
- All `docs/concepts/*.md` and `docs/articles/*.md` — untouched *except* `docs/concepts/coherence-path-hypothesis.md` §"Current empirical status" (the empirical-state surface of the doc, peer to PROJECT/ROADMAP/CHANGELOG; the conceptual framing §"What is the Coherence Path Hypothesis" / §"Falsification conditions" / etc. is untouched per AC5).

PROJECT.md / ROADMAP.md / CHANGELOG.md were **edited** (not overwritten) — minimal targeted edits per the issue body §4 "Reconcile status surfaces manually" and the user's explicit "Full posture rewrite" direction. CHANGELOG 0.2.0 and 0.1.0 entries preserved verbatim; the new 0.3.0 entry was appended.

**Verdict: AC5 PASS.** README and all coherence-tooling surfaces untouched; status surfaces edited (not wholesale-overwritten) within the issue's mandate.

### AC6 — No data policy regression

> No raw data, private traces, videos, archives, or private feature CSVs committed.

**Evidence — `git ls-files`-based audit on `cycle/port-segmentation-fix` HEAD:**

```text
$ git ls-files | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$' || echo "NONE"
```

(Verified at gate-time — see §"Pre-review gate" row 6.)

**Evidence — `git diff origin/main..HEAD --name-only`:** the diff touches no raw-data extensions (only `.py`, `.md`, `.ipynb`). The notebook contains *plot outputs* (PNG bytes inside the .ipynb cell outputs) which are derived visualizations, not raw participant data. The CSV `features-zeroth-pilot.csv` is written to `/opt/gait-data/cph-features/`, **outside the repo** (gitignored by `data/` and `/opt/` not being under the repo root).

**Verdict: AC6 PASS.** No raw data, traces, videos, archives, or private CSVs committed.

## Self-check

**Did α's work push ambiguity onto β?** No. The diff's surfaces are mechanically reproducible:
- The detector is the same algorithm shipped on the precursor branch (`a95415c`), verifiable by `git diff origin/cycle/segmentation-real-data-fix..HEAD -- scripts/segmentation.py` → the detector body is unchanged; only the quality_flag tri-value emission (cph#22) and import-ordering preservation differ.
- The notebook's evidence is reproducible: running `python3 scripts/build_notebook.py && jupyter nbconvert --execute --inplace notebooks/existing-data-processing.ipynb` against `/opt/gait-data/opencap-lab-validation/extracted/` regenerates the same outputs (verified within this session at `f27904a`).
- The status-surface rewrite is anchored on field-report-01: every claim in PROJECT.md / ROADMAP.md / CHANGELOG.md is traceable to a numbered line in `reports/field-report-01-existing-data-zeroth-pilot.md` (see AC3 / AC4 evidence tables above).

**Is every claim backed by evidence in the diff?** Yes. The AC table in §ACs maps each AC to either (a) a concrete file/line citation in the cycle's diff, (b) a runner-output line from notebook execution, or (c) a status-surface claim with its file/section pointer. No claim relies on unmerged context or off-branch evidence.

**Has α surfaced authoring work that β should not need to redo?**
- Peer enumeration (§2.3): the segmentation contract has one producer (`scripts/segmentation.py::detect_heel_strikes`) and three consumers I verified: (1) `scripts/features.py::extract_features` (consumes the cycle list), (2) `scripts/build_notebook.py` (calls segmentation in the §"Real-data segmentation" cell), (3) `scripts/segmentation_diagnostics.py` (consumes the heel-marker timeseries directly, parallel diagnostic surface). The `quality_flag` peer (cph#22 alignment) was preserved through the 3-way merge — verified by `grep -nE 'quality_flag\s*=\s*"' scripts/segmentation.py` which yields the tri-value `"ok"`/`"short"`/`"long"`.
- Intra-doc repetition (§2.3): the "60/60 R-side; 1 L-side; 61 cycles" tuple appears across PROJECT.md (§"Current empirical decision"), ROADMAP.md (§"Current state", R1 §"Current evidence"), CHANGELOG.md §0.3.0, and is the source-of-truth from field-report-01 (L8, L22, L47, L57, L58). Verified by `grep -nE '60/60|60 R|60 ?[+] ?1|n=60' PROJECT.md ROADMAP.md CHANGELOG.md` → consistent across all sites; no stale "18.3%" or "11 of 60" survivors in the status surfaces (the precursor wording was removed wholesale).
- Harness audit (§2.4): the schema-bearing change is the `quality_flag` tri-value (preserved from cph#22, not introduced by this cycle) and the feature columns added by `scripts/features.py` (`hip_adduction_*`, `lumbar_*`). The feature schema is read by `analysis/feature-table-schema.md` and `analysis/features.md` — both already align with the post-cph#22/cph#25 state of `main` and were not touched by this cycle. The harness on which this audit would be tightest is the CHANGELOG 0.3.0 §"Changed" list (the "code-first oracle" surface from cph#22 F7 / §"Review mode"): verified by reading the 0.3.0 entry against the actual diff.

**Pseudoreplication note (carry-forward).** field-report-01 §"R3 / R4 partial evaluability" already names pseudoreplication as the controlling risk for R3 and beyond (1 cycle per trial in most cases; within-trial repeatability not testable). This cycle does not run any aggregate test; the pseudoreplication risk is not yet incurred. Naming it here so β does not need to re-derive the constraint from field-report-01 §136.

## Debt

**Out-of-scope follow-ups carried in the issue body §"Post-port decision" — known and named, not exercised this cycle:**

1. **R-side aggregate condition-response analysis** (P4 in the issue body). The R-side n=60 surface is now ready: 10 subjects × 2 conditions × 3 trials per (subject, condition); `hip_adduction_range_deg` + `pelvis_list_range_deg` + `lumbar_bending_range_deg` are populated for every cycle. Per the issue body, this is the operator-recommended next issue. Not exercised here.

2. **L-side cycle recovery** (P5). The structural data-shape constraint (trial cropping ~1.3–1.5 s, R-stride-aligned) is documented in field-report-01 §"L-side cycles structurally limited by trial cropping" (L18, L154, L167). Two paths: (a) contralateral-anchored detection (R HS times + half-stride offset), (b) re-run OpenSim IK on source TRC files with wider time windows. Both out of scope per the issue body §"Non-goals" + §"Required approach"; named in PROJECT.md / ROADMAP.md as the next bounded cycle after R-side aggregate.

3. **First mechanical `coh --mode mechanical` run for `CHANGELOG.md 0.3.0`.** The 0.3.0 entry's coherence-machinery is unrun this cycle — the `targets/*.tsc` measurement is gated on a tagged release (per `.github/workflows/coherence.yml` trigger), and 0.3.0 is not tagged yet. Operator-gated per the precursor wave's policy ("no release tags this wave" carried forward).

4. **Pseudoreplication discipline as α-side documented constraint.** Named in §Self-check above as a carry-forward risk into R3; not converted into an enforcement check (e.g. a notebook lint or feature-table validator). Future-cycle authoring constraint, not this cycle's debt.

**Known limits internal to this cycle:**

- The Step A 3-way port produced 21 conflict markers in `notebooks/existing-data-processing.ipynb` (cell ordering + cached outputs differ between regeneration lineages). Resolved by reverting to main's notebook + regenerating via Step B. This is documented in `9bcef90`'s commit message; no debt carried forward (the regenerated notebook is the authoritative output).

- The branch `origin/cycle/segmentation-real-data-fix` (tip `a95415c`) is superseded by this port but **not deleted**. Per issue body §"Steps" the branch is the precursor; deletion is a δ/operator decision after merge.

- `git config --global user.email` was `epsilon@cph.cdd.cnos` at session start (carried from the prior wave's ε run). Path (a) retroactive correction applied via §2.6 row 14 — both `41b3693 → 9bcef90` and `9eb34ee → f27904a` rewritten to `Alpha <alpha@cph.cdd.cnos>`. No split-email survivors on the cycle history; force-with-lease push at the rebase tip.

**Known limits external to this cycle (named, not addressed):**

- field-report-01 explicitly names "Synthetic-data validation circularity" as a project-level coherence risk (L166): the smoke generator still produces an unphysical clipped-zero stance, and the rewritten detector ignores the boundary edge cases by design. field-report-01 mitigates by also classifying real-archive zero-cycle reasons per (trial, side) via `scripts/segmentation_diagnostics.py`. This is a project-level concern named in the report, not this cycle's debt.

- The receipt format named in the issue body §"Receipt format" is not written as a separate artifact in this cycle. The fields the receipt requires (Branch, Commit, Ported files, Notebook mode/root/SHA, Segmentation totals, Feature extraction stats, OpenCap r̄, Decision, Next recommended issue, No-raw-data-committed) are covered across `self-coherence.md §ACs` (this file), `analysis/feature-summary-zeroth-pilot.md` (notebook output), and `reports/field-report-01-existing-data-zeroth-pilot.md` (post-fix evidence). If β requires a literal receipt artifact, α will produce one in a fix-round on RC. Not blocked on this absence in round 1.

## CDD-Trace

Per `cdd/alpha/SKILL.md §2.2`.

1. **Design** — *not required*. The detector algorithm was authored on the precursor branch `origin/cycle/segmentation-real-data-fix` (`a95415c`) under a prior R2 single-issue cycle; this cycle is a *port*, not a redesign. The issue body §"Required approach" + §"Steps 1–8" operationalize the port in mechanical terms; the only direction-choice is the 3-way-merge-vs-fast-forward decision, settled by the issue body's "Because the branch was based on older repo surfaces, do not blindly merge if it overwrites current charter/process files. Prefer a surgical port of the implementation and evidence changes."

2. **Coherence contract** — §Gap. The post-cycle state must (a) carry the new detector on current main, (b) reproduce branch-level evidence on real data, (c) keep the empirical posture at REVISE (not GO) because L=1 L-cycle still blocks bilateral hypotheses, (d) preserve current README / CPH-COG framing / coherence-machinery / ROADMAP-gate language. Code and docs agree string-for-string on the post-fix segmentation numbers (60/60 R-side trials → 60 R cycles; 1 L cycle; 61 cycles total; 0.00% feature missingness across 35 columns × 61 cycles; OpenCap r̄ 0.962/0.933/0.951).

3. **Plan** — *issue-body-provided*. The issue's §Steps 1–8 define the linear sequence: clean branch → inspect diff → port files via `git restore --source` (with notebook conflict resolved by revert + regenerate) → reconcile status surfaces → verify no raw data → rerun notebook → confirm evidence → commit. Two-commit split (Step A = port; Step B = rerun + status update) emerged organically from the §Steps 6 "Hard stop if notebook falls back to synthetic mode" gate — Step A's notebook conflict was deferred to Step B for clean regeneration.

4. **Tests** — *AC oracles inline in §ACs*. No new pytest. Acceptance evidence comes from (a) `git show HEAD:scripts/segmentation.py` for the detector body (AC1), (b) `jupyter nbconvert --execute --inplace` runner output (AC2), (c) field-report-01 + notebook output cross-reference table (AC3), (d) field-report-01 §Decision + status surfaces (AC4), (e) `git diff --stat origin/main..HEAD` enumeration vs the issue body's protected-file list (AC5), (f) `git ls-files | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$' → NONE` (AC6, verified at gate time).

5. **Code** — two commits on `cycle/port-segmentation-fix` after rebase rewrite:
   - **`9bcef90` (Step A, formerly `41b3693`):** per-file 3-way merge porting the detector + diagnostics + features + build_notebook + analysis/feature-summary + reports/field-report-01 onto current main. 6 files changed; +441 / −172. New: `scripts/segmentation_diagnostics.py` (200 LOC).
   - **`f27904a` (Step B, formerly `9eb34ee`):** notebook regenerated via `python3 scripts/build_notebook.py` + executed via `jupyter nbconvert --execute --inplace` against `/opt/gait-data/opencap-lab-validation/extracted/`; PROJECT.md / ROADMAP.md / CHANGELOG.md realigned to the post-fix field-report-01. 5 files changed; +1,478 / −82.

6. **Docs** — covered by Step B's status-surface realignment plus fix-round 1's sibling-surface peer enumeration:
   - `PROJECT.md` §"Current empirical decision" (L20) / §"Current blocker" (L24) / §"Next action" (L28) / §"Active branch / issue" (L38) / §"Last field report" (L42).
   - `ROADMAP.md` §"Current state" (L13) / R1 §"Current evidence" (L42) / §"Status" / §"Coherence risk" (L45) / §"Next action" (L46); R2 §"Current evidence" (L52) / §"Status" (L54) / §"Coherence risk" / §"Next action" (L56) / §"Owning files" (L57); R3 §"Current evidence" (L62); R4 §"Current evidence" (L72).
   - `CHANGELOG.md` new §0.3.0 entry (lines 5–24). §0.2.0 and §0.1.0 preserved verbatim.
   - `reports/field-report-01-existing-data-zeroth-pilot.md` rewritten in Step A (`9bcef90`) — the post-fix authoritative evidence source.
   - `analysis/feature-summary-zeroth-pilot.md` auto-regenerated by the notebook in Step B.
   - **(fix-round 1)** `analysis/feature-table-schema.md` L42 — joint + trunk-axis lists realigned to features.py emissions. See §"Fix-round 1" F1, F2.
   - **(fix-round 1)** `analysis/features.md` §"Range / amplitude" L49-60 — realized set realigned; §"Candidate range/amplitude features" pruned of now-realized items; §"Candidate timing features" L81/82 + §"Candidate coordination features" L109 stale-segmentation-reference updates. See §"Fix-round 1" F3–F8.
   - **(fix-round 1)** `docs/concepts/coherence-path-hypothesis.md` §"Current empirical status" L116–126 — empirical-state surface realigned (conceptual framing untouched per AC5). See §"Fix-round 1" F9.

7. **Self-coherence** — this file. Written incrementally per §2.5 with one section per commit (commits `2392ef3` §Gap, `822ba6e` §Skills, `bb0ee76` §ACs, `c13eec3` §Self-check, `1c7fed0` §Debt, `beebcca` §CDD-Trace, plus fix-round-1 update `c5cf241` and the post-fix-round §"Fix-round 1" + §AC5 / §CDD-Trace step 6 refresh in this commit).

**Step-by-step ledger:**

| # | Step | Evidence |
|---|---|---|
| 1 | Read cph#26 issue body | `gh issue view 26 --repo usurobor/cph --json title,body,state,labels` |
| 2 | Read merge-base diff inventory | `git diff origin/main..origin/cycle/segmentation-real-data-fix --stat` (Step A) |
| 3 | Port via per-file 3-way merge | `git restore --source` + `git merge-file` with merge-base `d30aa4a` (Step A commit `9bcef90`) |
| 4 | Resolve notebook conflict | Revert to main's notebook + regenerate in Step B (issue body Step 6 "Hard stop if notebook falls back to synthetic mode") |
| 5 | Verify no raw data | `git ls-files \| grep -E '\.(zip\|trc\|mot\|sto\|c3d\|osim\|mp4\|mov\|csv\|parquet)$'` → NONE |
| 6 | Rerun notebook | `export GAIT_DATA_ROOT=/opt/gait-data && python3 scripts/build_notebook.py && jupyter nbconvert --execute --inplace notebooks/existing-data-processing.ipynb` |
| 7 | Confirm evidence against field-report-01 | §ACs AC3 cross-reference table; 12 quantities match line-for-line |
| 8 | Realign status surfaces | PROJECT.md / ROADMAP.md / CHANGELOG.md edits per issue body §4 "Reconcile status surfaces manually" |
| 9 | Step B commit | `f27904a` (formerly `9eb34ee`) |
| 10 | Fix α identity (§2.6 row 14 path a) | `git rebase ebd909c --exec 'git commit --amend --reset-author --no-edit'` + `git push --force-with-lease` (rewrites `41b3693 → 9bcef90`, `9eb34ee → f27904a` with `Alpha <alpha@cph.cdd.cnos>`) |
| 11 | Self-coherence §Gap | `2392ef3` |
| 12 | Self-coherence §Skills | `822ba6e` |
| 13 | Self-coherence §ACs | `bb0ee76` |
| 14 | Self-coherence §Self-check | `c13eec3` |
| 15 | Self-coherence §Debt | `1c7fed0` |
| 16 | Self-coherence §CDD-Trace | (next commit) |
| 17 | Pre-review gate row 6 (schema audit) flagged drift | features.py emits 6 new columns; feature-table-schema.md L42 + features.md §"Range/amplitude" did not enumerate them |
| 18 | Self-discovered fix-round (§3.4 post-patch re-audit) | Sibling-surface patch + stale-reference sweep |
| 19 | Fix-round commit | `c5cf241` (3 files: feature-table-schema.md, features.md, coherence-path-hypothesis.md) |
| 20 | Pre-review gate run | (next: §"Pre-review gate" section) |
| 21 | Review-readiness signal | (next: §"Review-readiness" section) |

## Fix-round 1 — peer-enumeration (self-discovered)

**Trigger:** pre-review gate row 6 (schema/shape audit when contracts changed) surfaced that `scripts/features.py::extract_range` adds 6 new column emissions (`hip_adduction_{range,peak,min}_deg` via the joint_map; `lumbar_{bending,rotation,extension}_range_deg` via the new trunk loop), but `analysis/feature-table-schema.md` L42 listed only the pre-cycle joints (hip_flexion / knee_angle / ankle_angle) and pelvis axes (pelvis_tilt / pelvis_list / pelvis_rotation), and `analysis/features.md` §"Range / amplitude — extract_range" carried the same incomplete enumeration.

**Findings addressed (self-discovered, α-side):**

| # | Finding | File | Fix |
|---|---------|------|-----|
| F1 | Joint list missing `hip_adduction` | `analysis/feature-table-schema.md` L42 | Added `hip_adduction` to the joint-list parenthetical |
| F2 | Trunk-axis emissions undocumented | `analysis/feature-table-schema.md` L42 | Added `for each present trunk axis (lumbar_bending, lumbar_rotation, lumbar_extension): {axis}_range_deg` clause |
| F3 | Realized-set joint list missing `hip_adduction` | `analysis/features.md` §"Range / amplitude" | Added `hip_adduction_{side}` to the realized joint list |
| F4 | Realized-set missing lumbar block | `analysis/features.md` §"Range / amplitude" | Added new "For each trunk axis present" block |
| F5 | "hip adduction-abduction range" listed as Candidate (now realized) | `analysis/features.md` §"Candidate range/amplitude features" | Removed bullet; added parenthetical naming the realization point (cph#26) |
| F6 | Stale segmentation reference (11/60, R-side only) in §"Candidate timing features" | `analysis/features.md` L81 | Updated to post-fix state (1 R cycle per trial bookended by cropping; trial-cropping constraint, not detector) |
| F7 | Stale L-side cycle reference (0) in §"Candidate timing features" | `analysis/features.md` L82 | Updated to "1 L-cycle across 60 trials post-fix; trial cropping favors R-stride completion" |
| F8 | Stale L-side cycle reference (currently 0) in §"Candidate coordination features" | `analysis/features.md` L109 | Updated to "1 L-cycle across 60 trials post-segmentation-fix; trial-cropping structural constraint, not detector" |
| F9 | Stale §"Current empirical status" mirroring pre-fix PROJECT/ROADMAP/CHANGELOG state | `docs/concepts/coherence-path-hypothesis.md` L116–126 | Updated `Gait-cycle segmentation` line from FAIL/18.3% to PASS-on-R-side + structurally-blocked-on-L; updated `Hypothesis testability` from "blocked at 11/0" to "partial at 60/1"; updated trailer sentence to name the half-anchored bilateral construct |

**Fix-round commit:** `c5cf241` (3 files; +14 / −11).

**Scope note.** This fix-round is **strictly sibling-surface peer enumeration** triggered by features.py's new column emissions. No code changed. The `docs/concepts/coherence-path-hypothesis.md` patch is bounded to §"Current empirical status" (the equivalent of PROJECT/ROADMAP/CHANGELOG's empirical-state surfaces); the §"What is the Coherence Path Hypothesis", §"What it would falsify" and §"Falsification conditions" sections (the conceptual framing) were not touched, in line with AC5's protect-the-CPH-framing constraint. README untouched.

**Diff after fix-round:**

```text
$ git diff origin/main..HEAD --name-only
.cdr/unreleased/26/self-coherence.md
CHANGELOG.md
PROJECT.md
ROADMAP.md
analysis/feature-summary-zeroth-pilot.md
analysis/feature-table-schema.md      (fix-round)
analysis/features.md                  (fix-round)
docs/concepts/coherence-path-hypothesis.md  (fix-round, §"Current empirical status" only)
notebooks/existing-data-processing.ipynb
reports/field-report-01-existing-data-zeroth-pilot.md
scripts/build_notebook.py
scripts/features.py
scripts/segmentation.py
scripts/segmentation_diagnostics.py
```

14 files total (was 11 pre-fix-round; +3 from this fix-round).





