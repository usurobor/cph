# Changelog

Project changelog: what shipped, what changed, what's still open. Empirical state lives in the latest merged field report; live operational status lives in [PROJECT.md](PROJECT.md); the gate-based roadmap lives in [ROADMAP.md](ROADMAP.md).

## 0.3.2 — R1 GO with bounded scope via cph#28 L-cycle recovery (2026-05-19)

**Where we were.** R1 was REVISE. R3 was partial GO on R-side post-cph#27. L-side cycle yield was 1/60 trials (subject8/walkingTS1 only) — a property of the source archive's R-aligned ~1.3–1.5 s trial cropping rather than of `scripts/segmentation.py::detect_heel_strikes`, which fired HS on all 60 L sides but lacked the second L HS needed for cycle bracketing in 59/60 trials. cph#28's open question: can L-side cycles be recovered well enough to satisfy R1's bilateral gate without requiring new captures?

**What this version unblocked.** Yes — contralateral-anchored L-cycle inference recovers 57/60 L cycles via a matched-duration partial-clip rule (R HS plus half-stride offset, calibrated against the lone measured-L-cycle trial to 30 ms drift). R1 transitions REVISE → GO with bounded scope (path (a) inferred bilateral). The cph#28 AC5 GO criterion fires: AC1 ≥ 80% on R (100%) and L (95%); L ≥ 10 (57 cycles). Bilateral (subject, trial_id, cycle_number) pair count: 57; `scripts.features.lr_asymmetry` computes on 60 non-empty rows. R-side detector and R cycle distribution are unchanged (60/60, mean 1.06 s, R-only range 0.89–1.37 s) — `scripts/segmentation.py::detect_heel_strikes` not modified, AC4 regression preserved.

**What is now testable on the inferred-bilateral surface.**

- **R3 bilateral extension** — re-run `analysis/r3_subject_aggregate_tests.py` against the post-cph#28 feature table; aggregate subject-paired L-vs-R deltas; report H3 (asymmetric phase-coupling) with the path (a) honesty caveat applied (inferred not measured; partial-clip coverage 0.80–0.94).
- **R4 condition 3 (L/R asymmetry)** — transitions from "not testable" to "evaluable on inferred-bilateral surface"; full 6-condition substantive falsification verdict now reachable.
- **lr_asymmetry features** — `(hip_flexion / knee_angle / ankle_angle / pelvis_* / lumbar_*)_range_deg_lr_diff` and `hip_knee_lag_pct_cycle_lr_diff` columns computable across the 60 R/L paired rows.

**What is still bounded / blocked.**

- **All L cycles are inferred not measured.** Bilateral asymmetry features carry an inference layer that R-vs-R features (cph#27 R3) do not. Subject-paired tests on L-vs-R features should report magnitudes as "consistent with" an asymmetric coordination signature when significant, not as "measurement of" asymmetric coordination.
- **All L cycles are partial-clip** (coverage 0.80–0.94, mean 0.86); the matched L cycle slice extends only to trial end, missing terminal swing (~14% of the L stride on average). Range features are slightly biased downward; timing / coordination features at the cycle boundary are unreliable.
- **Path (b) (measured-bilateral upgrade)** — the source TRC files at `/opt/gait-data/opencap-lab-validation/extracted/` are reachable; an operator-side OpenSim IK rerun with extended trial windows would produce measured L HS and replace the inference layer. Deferred; path (a) suffices for the R1 gate.
- **Friend pre-pilot capture protocol** — should specify minimum trial length (≥3 s = ≥2 full strides) so future captures are not subject to the same cropping limit as the archive.

**The new question.** With R1 closed and a bilateral surface now available (inferred), does the construct survive a full R3 bilateral aggregate + R4 6-condition falsification re-evaluation? cph#27's R3 R-side partial GO + cph#28's inferred-bilateral coverage define the surface; the next cycle answers the bilateral question with the path (a) caveat applied.

### Changed (file-level)

- `scripts/segmentation_contralateral.py` — new module. `infer_contralateral_heel_strikes` (R HS → L HS at r + T/2, validated via local LHEE_Y minimum when refinement is enabled — disabled by default after empirical refinement shifted predictions toward noisy boundary minima). `segment_trial_with_contralateral_l` (R-side unchanged via `scripts.segmentation.segment_trial`; L-side via matched-duration partial-clip rule with `min_coverage=0.80` emission threshold). `calibrate_against_measured_l` (validates half-stride model against subject8/walkingTS1: predicted 87 vs measured 84, 30 ms drift). Standalone `main()` produces per-trial diagnostic with `--calibrate` switch.
- `scripts/segmentation.py` — `Cycle` dataclass gains `detection_method: str = "measured"` (backward-compatible default). `detect_heel_strikes` untouched (R2 closed; AC4 preserved).
- `scripts/features.py` — `extract_features` emits `detection_method` column for downstream filtering.
- `analysis/r3_subject_aggregate_tests.py` — `NON_FEATURE_COLS` adds `detection_method`.
- `scripts/build_notebook.py` — wires `segment_trial_with_contralateral_l` into §2 segmentation; adds an AC3 bilateral coverage characterization to the summary cell (per (subject, condition) L counts, bilateral pair count, `lr_asymmetry` row count) and a cph#28 section to `analysis/feature-summary-zeroth-pilot.md`.
- `notebooks/existing-data-processing.ipynb`, `analysis/feature-summary-zeroth-pilot.md` — regenerated against the unchanged archive on 2026-05-19.
- [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) — rewritten post-cph#28; supersedes the 2026-05-17 segmentation-fix REVISE.
- [`PROJECT.md`](PROJECT.md), [`ROADMAP.md`](ROADMAP.md) — realigned to R1 → GO with bounded scope.

### Decision

R1 transitions REVISE → GO with bounded scope (path (a) inferred bilateral). cph#27 R3 partial GO on R-side stands. The hypothesis is neither validated nor refuted; the project has moved from "can we recover L-side cycles?" to "does the bilateral construct survive on the inferred-bilateral surface, and is the path (b) measured-bilateral upgrade necessary?"

### Next gate

R3 bilateral extension on the post-cph#28 feature table (operator triage on cycle ordering vs R4 full falsification re-evaluation).

## 0.3.1 — R3 R-side construct evaluation; partial GO on R-side (2026-05-19)

**Where we were.** R3 was NOT STARTED. The post-cph#26 R-side feature table was in place (60 R cycles × 25 numeric features × 0% missingness) but no inferential statement existed about whether features actually responded to condition under the protocol's stated comparison (natural vs trunk-sway) at the inferential unit the protocol requires (*subject*, not cycle). The open question was whether the construct survives R-side contact with measurement, with R1 / Hypothesis 3 owned separately by cph#28.

**What this version unblocked.** The R-side construct evaluation now exists. The aggregate analysis (10 subjects × 2 conditions × 25 numeric features, median aggregation, paired Wilcoxon signed-rank, rank-biserial effect size + percentile bootstrap 95% CI, BH-FDR at q=0.05) produced 7 BH-significant condition responses including a textbook-magnitude lumbar bending increase (+18.3°, r_rb = +1.0, all 10 subjects in agreement) and a distal sagittal contraction (ankle range −6.6°, r_rb = −1.0). Three candidate support-path hypotheses surfaced with mechanism and condition-bound scope: *Lateral-trunk substitution path*, *Distal sagittal contraction under proximal compensation*, *Cadence-slowdown signature*. R3 transitions from NOT STARTED to partial GO on R-side.

**What is now testable / supported (R-side surfaces).**

- **H1 (sagittal-dominant load transfer)** — partial: 1/5 features BH-significant (ankle range), 1 trending (knee range). Supported in *distal-contraction-under-proximal-compensation* form; the hip-as-sagittal-driver sub-claim is not supported on R-side.
- **H2 (trunk-sway compensation)** — partial: 2/9 features BH-significant (lumbar bending +18.3°, lumbar extension +1.6°), 1 trending (pelvis tilt). Supported in *trunk-segment-driven* form; the hip-adduction-as-compensation sub-claim is not supported on R-side.
- **Falsification re-evaluation (R-side):** 5 of 6 conditions cleanly NOT triggered (1, 2, 4, 5, 6); 1 not testable (condition 3, L/R asymmetry, owned by cph#28). 0 of 6 triggered. Mechanically ≪ 4-condition NO-GO threshold.

**What is still blocked.**

- **H3 (asymmetric phase-coupling between sides)** — structurally non-testable on this archive (n=1 L-cycle; no R/L pairs at matching (subject, cycle_number)). Owned by [cph#28](https://github.com/usurobor/cph/issues/28).
- **R1 itself stays REVISE** — partial GO on R-side does *not* lift R1. The bilateral construct is still half-anchored; cph#28 owns R1's transition gate.
- **Full R4 falsification re-evaluation** — partially evaluable on R-side (5/6 conditions); condition 3 (L/R asymmetry) transitions from "not testable" to a substantive verdict only after cph#28.

**The new question.** The R-side construct survives — does the bilateral construct? cph#28 owns the answer. Once L-side cycle yield is recovered, the R3 partial-GO can be extended to a full bilateral R3 evaluation and R4 can produce a full 6-condition substantive verdict.

### Changed (file-level)

- `analysis/r3_subject_aggregate_tests.py` — new single-purpose reproducibility harness. Reads `$GAIT_DATA_ROOT/cph-features/features-zeroth-pilot.csv` (read-only; not committed), aggregates per (subject, condition) by median (primary) and mean (robustness), runs paired Wilcoxon signed-rank tests across n=10 subjects, computes rank-biserial effect sizes with percentile bootstrap 95% CI (B=10,000, deterministic seed=20260519), applies BH-FDR at q=0.05, and emits markdown tables to stdout. Does not write any aggregate to disk (AC9 boundary). Method picks documented in `.cdr/unreleased/27/self-coherence.md` §Method picks.
- `reports/field-report-03-construct-evaluation.md` — new R3 field report. Carries the 700-cell aggregate table, the 25-feature paired-test result table, per-hypothesis evidence summaries (H1, H2, H3-not-testable), three candidate support-path hypotheses with mechanism + condition-bound scope, the 6-condition falsification re-evaluation on R-side, and the partial-GO decision per protocol thresholds.
- [`PROJECT.md`](PROJECT.md), [`ROADMAP.md`](ROADMAP.md) — realigned to the partial-GO-on-R-side reading. R3 phase moves from NOT STARTED to partial GO on R-side; R4 phase moves from NOT STARTED to partially evaluable on R-side; R1 holds REVISE (cross-cycle binding to cph#28).

### Decision

R3 = partial GO on R-side. R1 stays REVISE (cross-cycle binding; cph#28 owns the transition gate). The hypothesis is neither validated nor refuted. The project has moved from "can the R-side construct survive contact with measurement?" to "does the bilateral construct survive once cph#28 recovers L-cycle yield?"

### Next gate

[cph#28](https://github.com/usurobor/cph/issues/28) — L-cycle recovery (contralateral-anchored detection or wider IK windows). After cph#28 lands, full R3 bilateral evaluation + full R4 falsification re-evaluation become possible.

## 0.3.0 — R2 segmentation fix ported; bilateral construct half-anchored (2026-05-19)

**Where we were.** R1 was REVISE on a hard blocker: `scripts/segmentation.py::detect_heel_strikes` was tuned to the synthetic generator's heel-marker shape and failed on real Mocap calcaneus markers — only 11/60 trials segmented (18.3%, R-side only), zero L-side cycles. The open question was whether the real-data segmenter could work at all.

**What this version unblocked.** Yes — the real-data segmenter works. The detector has been rewritten with robust-percentile normalization plus stance-region depth/length gating, invariant to absolute height, baseline offset, and amplitude. It now passes AC1 cleanly on R-side: 60/60 trials, 100%, 61 cycles total (60 R + 1 L), 0.00% feature-extraction missingness across 35 columns. R2 transitions from REVISE to GO at the detector level.

**What is now testable.**

- R-side sagittal coordination (hip / knee / ankle range, peak, min, hip-knee lag)
- R-side frontal-plane coordination (new `hip_adduction_*` columns) and trunk dynamics (new `lumbar_*` columns)
- Natural vs trunk-sway condition response on 30 + 30 R-side cycles across 10 subjects
- Subject-level R-side aggregate patterns ([cph#27](https://github.com/usurobor/cph/issues/27))
- OpenCap-vs-reference reliability for this archive (Pearson r̄ 0.962 HRNet, 0.933 OpenPose_default, 0.951 OpenPose_highAccuracy across 60 trials × 3 backbones)

**What is still blocked.**

- Bilateral support-path comparison — L=1 cycle is insufficient
- Left-right phase coupling (Hypothesis 3 in [`docs/concepts/support-path.md`](docs/concepts/support-path.md))
- L/R asymmetry features (`lr_asymmetry` in `scripts/features.py`)
- Full falsification-table evaluation — only R-side-evaluable conditions are reachable
- R1 itself stays REVISE — the bilateral construct is half-anchored, not anchored

The blocker has moved from the detector to the source archive: each trial in OpenCap Lab Validation is cropped to ~1.3–1.5 s and R-aligned, so 47/60 L sides end mid-swing and 12/60 start mid-swing. `scripts/segmentation_diagnostics.py` reports the per-(trial, side) zero-cycle reasons mechanically.

**The new question.** Can we recover enough bilateral structure to test Hypothesis 3, or do we proceed with a bounded R-side construct test? Filed in parallel at [cph#27](https://github.com/usurobor/cph/issues/27) (R-side aggregate, runnable now) and [cph#28](https://github.com/usurobor/cph/issues/28) (L-cycle recovery via contralateral-anchored detection or wider IK windows).

### Changed (file-level)

- `scripts/segmentation.py` — detector rewritten (robust-percentile normalization `yn = (smoothed_heel − q05) / (q95 − q05)` + stance-region depth/length gating `yn < 0.30` for ≥150 ms AND `< 0.10` at deepest). Preserves the `quality_flag` tri-value from cph#22.
- `scripts/segmentation_diagnostics.py` — new per-(trial, side) diagnostic utility classifying zero-cycle reasons (`trial_ends_mid_swing`, `trial_crops_only_swing`, `ok`).
- `scripts/features.py` — adds frontal-plane `hip_adduction_range_deg` / `_peak_deg` / `_min_deg` and trunk `lumbar_extension_range_deg` / `lumbar_bending_range_deg` / `lumbar_rotation_range_deg`. Preserves the `extract_shape_sentinel` name from cph#25.
- `scripts/build_notebook.py` — integrates the diagnostics utility into §"Known debt".
- `notebooks/existing-data-processing.ipynb` — regenerated and executed on real data.
- `analysis/feature-summary-zeroth-pilot.md` — post-fix evidence summary.
- [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) — rewritten post-fix; supersedes the 18.3%-segmentation REVISE.
- [`PROJECT.md`](PROJECT.md), [`ROADMAP.md`](ROADMAP.md) — realigned to the post-fix evidence; R2 → GO at the detector level, R1 holds REVISE.

### Decision

REVISE on R1 (bilateral construct half-anchored). R2 transitions to GO. The hypothesis is neither validated nor refuted; the project has moved from "can the real-data segmenter work?" to "can we recover the missing side, or run a bounded R-side test?"

### Next gate

[cph#27](https://github.com/usurobor/cph/issues/27) — R3 R-side aggregate condition-response analysis. Or [cph#28](https://github.com/usurobor/cph/issues/28) — L-cycle recovery. Runnable in parallel.

## 0.2.0 — Coherence drift sweep + docs refactor (2026-05-18)

- **Empirical state:** REVISE — unchanged from [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md). The active blocker is gait-cycle segmentation on real Mocap heel-marker data (R2 in [`ROADMAP.md`](ROADMAP.md)).
- **Decision:** Two coherence-drift-sweep waves landed against R0 (masters cph#16 and cph#21). Documentation refactor consolidated process artifacts under `.cdr/` and removed the public doctrine doc; coherence measurement runs as operational machinery (`scripts/measure-coherence.sh`, `targets/*.tsc`, `.github/workflows/coherence.yml`).

### Changed

- **F1–F6 (master cph#16, four subs cph#17–20):** broken realization ref fixed; `field-report-02` name collision resolved (R5 stub kept at -02, construct evaluation renamed to -03); schema/code column alignment in `analysis/feature-table-schema.md` + `analysis/features.md` against `scripts/features.py`; first-pass vs candidate feature distinction made explicit; legacy `gait-support-paths-features/` path renamed to `cph-features/` in live surfaces.
- **F7–F11 (master cph#21, four subs cph#22–25):** `scripts/segmentation.py` `quality_flag` literals now emit `"ok"`/`"short"`/`"long"` (was only `"ok"`/`"out_of_range"` while schema claimed three values); `analysis/feature-table-schema.md` + `analysis/features.md` realigned to the code; PROJECT.md §"Active branch / issue" + ROADMAP.md R0 §"Next action" / §"Owning files" de-staled; `reports/field-report-02-friend-pre-pilot.md` H1 number prefix matches filename; `scripts/features.py::extract_shape` renamed to `extract_shape_sentinel` (placeholder semantics signaled in the name).
- **Docs refactor:** `CDR.md` removed; `.cdd/` renamed to `.cdr/` (project history preserved); PROJECT.md / ROADMAP.md / CHANGELOG.md reframed. Coherence machinery (`scripts/measure-coherence.sh`, `targets/*.tsc`) preserved as operational infrastructure. `.github/workflows/coherence.yml` added — runs coherence measurement on every tagged release; reports upload as a workflow artifact for the operator to read when appending the row to `.cdr/coherence-log.md`.

### Known limits

- **No new empirical claims.** Two qualitative waves and one docs refactor. No clustering, no participant data, no field-report content edits. Empirical state remains REVISE per the latest merged field report.
- **R2 segmentation remains the empirical blocker.** The existing-data zeroth pilot is REVISE pending a bounded fix to `scripts/segmentation.py::detect_heel_strikes`. The branch `origin/cycle/segmentation-real-data-fix` is unmerged; that merge decision is orthogonal to this wave.

### Next gate

R2 — segmentation reliability on real Mocap heel-marker data (see [`ROADMAP.md`](ROADMAP.md) §"Phase R2"). The next changelog entry should land at the close of that bounded cycle.

## 0.1.0 — Initial charter (2026-05-18)

Initial repo refactor establishing the charter, hypothesis doc, support-path doc, failure-conditions doc, seven-families article, and ROADMAP. Historical wave artifacts live under `.cdr/waves/cdr-refactor-2026-05-18/` and `.cdr/unreleased/{12,13,14,15}/`.

- **Empirical state:** REVISE — per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) (2026-05-17 real-data run). Preserved verbatim by the refactor.
- **Decision:** Repo refactored into a charter + roadmap + changelog + gates project. Hypothesis, methods, evidence, and process surfaces partitioned into single owners.

### Changed

- [`README.md`](README.md) states the Coherence Path Hypothesis explicitly, distinguishes it from `support path`, names the seven gait families as observational vocabulary, and carries the source-of-truth table.
- [`docs/concepts/coherence-path-hypothesis.md`](docs/concepts/coherence-path-hypothesis.md) introduced as the hypothesis authority.
- [`docs/articles/seven-ways-people-walk.md`](docs/articles/seven-ways-people-walk.md) introduced as the seven-families observational reference.
- [`ROADMAP.md`](ROADMAP.md) introduced with gate-based phases R0–R6.
- `CHANGELOG.md` introduced (this file).
- [`PROJECT.md`](PROJECT.md) repartitioned to current operational status only.
