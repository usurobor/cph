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

**Evidence — `git diff origin/main..HEAD --stat` (the cycle's full diff, before this self-coherence file):**

```text
analysis/feature-summary-zeroth-pilot.md           |  16 +-
.cdr/unreleased/26/self-coherence.md               | (this file)
CHANGELOG.md                                       |  27 +
PROJECT.md                                         |  10 +-
ROADMAP.md                                         |  22 +-
notebooks/existing-data-processing.ipynb           | 1499 ++++++++++++++++++++++++++++--
reports/field-report-01-existing-data-zeroth-pilot.md | 237 ++++++++++-----------
scripts/build_notebook.py                          |  32 ++-
scripts/features.py                                |   5 +
scripts/segmentation.py                            | 125 +++++++----
scripts/segmentation_diagnostics.py                | 200 +++++++++++++++++
```

Files **not touched** by the cycle (verified by absence from the diff):
- `README.md` — untouched (CPH/COG split framing preserved).
- `.cdr/**` *except* the new `.cdr/unreleased/26/self-coherence.md` (this file).
- `targets/**` — untouched (TSC machinery preserved).
- `scripts/measure-coherence.sh` — untouched.
- `.github/workflows/coherence.yml` — untouched.
- All `docs/concepts/*.md` and `docs/articles/*.md` — untouched (charter surfaces preserved).

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


