# Features

This file owns the candidate features extracted from gait-cycle data.

## Governing question

Which measurable traces might support or reject a support-path hypothesis?

## Feature principle

Extract features that can be tied to a gait cycle, side, condition, and interpretable movement question.

Do not extract features only because they are available.
Do not train on participant identity.
Do not use labels from visual type lists as ground truth.

## Required indexing

Every feature row should include:

- subject (anonymous subject identifier; column `subject`)
- session (column `session`; currently hardcoded to `"S01"` per `analysis/feature-table-schema.md` §"Single-session note")
- trial id (column `trial_id`)
- condition (column `condition`)
- side (column `side`; values `L`/`R`)
- cycle number (column `cycle_number`)
- quality flag (column `quality_flag`; values `ok`/`short`/`long` per `analysis/feature-table-schema.md` §"quality_flag")
- exclusion flag (column `exclusion_flag`; derived as `quality_flag != "ok"`)
- detection method (column `detection_method`; values `measured`/`inferred_contralateral`/`inferred_contralateral_partial` per `analysis/feature-table-schema.md` §"detection_method"; carries the path-(a) honesty caveat at the data-row level — `measured` is the default on `scripts/segmentation.py::Cycle` and the only value emitted on the R-side / standard detector path, while `inferred_contralateral` / `inferred_contralateral_partial` are emitted by `scripts/segmentation_contralateral.py::segment_trial_with_contralateral_l` for L-side cycles built via half-stride offset from the contralateral heel-strike, with `_partial` marking matched-duration windows clipped at the trial end. Excluded from per-feature aggregation by `analysis/r3_subject_aggregate_tests.py::NON_FEATURE_COLS`.)

Column names match what `scripts/features.py::extract_features` emits and what `analysis/feature-table-schema.md` §"Identification" / §"Detection provenance" prescribe. Without this indexing, feature values cannot be interpreted.

## First-pass set (currently implemented)

The realized feature set emitted by `scripts/features.py::extract_features`. Each item below names the function in `scripts/features.py` that produces it. Reproduce the list with:

```bash
grep -nE '^\s+out\["[a-z_]+\.?[a-z_]*"\]|^def extract_' scripts/features.py
```

### Timing — `extract_timing`

- `cycle_duration_s` — gait-cycle duration in seconds (from `Cycle.duration_s`)
- `stance_duration_s` — stance phase duration (estimated from contralateral heel minimum, or fallback 60% of cycle)
- `swing_duration_s` — swing phase duration (complement of stance)
- `stance_pct_cycle` — stance as percentage of cycle
- `timing_estimate_method` — `contralateral_HS` (when contralateral heel is in the dataframe) or `fallback_60pct` (population-mean estimate)
- `peak_knee_flexion_phase` — timing (% of cycle) of peak knee flexion on the cycle's side

### Range / amplitude — `extract_range`

For each joint with available columns (`hip_flexion_{side}`, `hip_adduction_{side}`, `knee_angle_{side}`, `ankle_angle_{side}`):
- `{joint}_range_deg` — max − min over the cycle
- `{joint}_peak_deg` — max
- `{joint}_min_deg` — min

For each pelvis axis present (`pelvis_tilt`, `pelvis_list`, `pelvis_rotation`):
- `{axis}_range_deg` — max − min over the cycle

For each trunk axis present (`lumbar_bending`, `lumbar_rotation`, `lumbar_extension`):
- `{axis}_range_deg` — max − min over the cycle

### Shape — `extract_shape_sentinel`

- `normalized_curve_available` — boolean placeholder; the actual 101-point time-normalized curves are persisted to a private parquet outside the repo and consumed by the notebook's aggregate PCA cell (see notebook §7 "Known debt" for the PCA-on-curves status)

### Coordination — `extract_coordination`

- `hip_knee_lag_samples` — integer lag (samples) of the cross-correlation peak between hip and knee flexion on the cycle's side
- `hip_knee_lag_pct_cycle` — same lag, expressed as percentage of cycle length

### Derived (aggregate phase) — `lr_asymmetry`

`scripts/features.py::lr_asymmetry` produces left/right difference columns by pivoting the wide feature table on `side` and subtracting `R − L` for each requested feature in `key_cols`. The emitted columns are named `{feature}_lr_diff`. This is a derived view over the first-pass table, not a per-cycle extraction.

## Candidate set (not yet implemented)

The features below appear in earlier drafts and operator notes as desirable but are not realized in code yet. Each item names a near-term gating constraint. The notebook §7 "Known debt" cell (per `scripts/build_notebook.py:400` / `notebooks/existing-data-processing.ipynb` §7) acknowledges a subset of these; this section is the union with full traceability to the gating constraint.

### Candidate timing features (not implemented)

- step-to-step timing variability — requires multi-cycle per trial; blocked by trial cropping (each Lab Validation trial yields exactly 1 R cycle bookended by the cropping window, per `reports/field-report-01-existing-data-zeroth-pilot.md` §Segmentation Status — post-segmentation-fix state)
- right-left duration difference per trial — blocked by L-side cycle yield (1 L-cycle across 60 trials post-fix; trial cropping favors R-stride completion)
- timing of peak hip extension — requires extraction parallel to `peak_knee_flexion_phase`; trivial extension
- timing of peak ankle plantarflexion — same; trivial extension
- timing of pelvis rotation extrema — same; trivial extension

### Candidate range/amplitude features (not implemented)

- stance-phase-only range for each joint — requires the stance-end timestamp from `extract_timing` to subset; gated on multi-cycle segmentation
- peak values *and* their timing as a joint emission — currently `*_peak_deg` and `peak_knee_flexion_phase` are emitted but not paired in a single timing-and-magnitude shape; gated on a downstream consumer requiring the pair

(Hip adduction-abduction range and lumbar bending / rotation / extension range are now realized — see §"Range / amplitude" above. The Lab Validation archive's OpenCap IK output does include `hip_adduction_{side}` and lumbar trunk axes; the segmentation-fix port (cph#26) added the corresponding `_range_deg` / `_peak_deg` / `_min_deg` emissions in `scripts/features.py::extract_range`.)

### Candidate shape features (not implemented)

- normalized waveform samples (101-point) as columns — currently `normalized_curve_available` is a boolean; the curves themselves live outside the table. Materialization as in-table columns would multiply the row width by ~300 and is intentionally deferred until the segmenter produces enough cycles to make PCA meaningful
- first-derivative summaries — gated on segmenter producing enough cycles for derivative noise to be characterizable
- jerk-like / smoothness measures — same
- curve correlation between cycles within a trial — gated on multi-cycle segmentation
- dynamic time warping distance — gated on multi-cycle segmentation
- principal component scores from waveform sets — notebook §7 "Known debt" names this as the aggregate PCA cell; gated on n_cycles ≥ ~30 per condition

### Candidate coordination features (not implemented)

- pelvis-trunk phase relationship — requires trunk data not in the Lab Validation archive
- knee-ankle timing offset — parallel to `hip_knee_lag_*`; trivial extension once a downstream consumer is named
- pelvis rotation relative to stance side — requires both pelvis_rotation and a stance-side phase column
- contralateral arm or trunk relation — requires arm/trunk marker data
- side-specific coupling differences — gated on L-side cycle availability (1 L-cycle across 60 trials post-segmentation-fix; trial-cropping structural constraint, not detector)

### Candidate asymmetry features (not implemented in per-cycle extraction; partly available in aggregate)

`lr_asymmetry` (above) is the only L-R derivation currently emitted, and it operates on pre-existing per-cycle features. The following are not yet implemented:

- right-left waveform difference (point-by-point or summary) — gated on shape-feature materialization
- right-left peak timing difference — gated on `timing of peak {joint}` features being emitted for both sides
- right-left coordination difference — gated on side-specific coordination features (above)
- within-participant side consistency across conditions — gated on multi-trial aggregation; notebook §7 "Known debt" names this as the missing condition-response analysis

### Candidate condition-response features (not implemented)

The notebook §7 "Known debt" cell explicitly names these as "asymmetry shape-correlation, condition-response deltas — require multi-trial aggregation that lives in Sub C's analysis, not Sub B's per-cycle extraction":

- normal-to-slow change — requires multiple speed conditions per subject; the Lab Validation archive currently has only `walking` and `walkingTS` conditions
- normal-to-fast change — same
- shod-to-barefoot change — same; Lab Validation archive does not vary footwear
- first-to-repeat trial change — requires repeat trials per condition per subject
- first-session to repeat-session change — gated on multi-session capture (the same gate as the schema's `session` column widening)

### Indexing widening (not implemented)

The following indexing columns are named in `analysis/feature-table-schema.md` but not realized in code:

- `cycle_start_frame` / `cycle_end_frame` — `Cycle` carries `start_time`/`end_time` in seconds; frame-index columns need a `sample_rate_hz` round-trip
- `exclusion_reason` — currently implicit in `quality_flag` values (`short`, `long`); materializing as a dedicated string column is a small ergonomic improvement
- `source_file` — the trial's source `.mot` filename; not currently propagated through `Cycle`

### Quality-flag widening (not implemented)

The schema doc originally listed `good` / `fair` / `poor` / `unusable`; an interim draft listed `ok` / `short` / `low_contact_gap`. The code emits `ok` / `short` / `long`, where `short` and `long` are derived from cycle duration alone (`duration <= 0.5` and `duration >= 1.8` respectively, in `scripts/segmentation.py::segment_trial`). Finer-grained labels — in particular `low_contact_gap` to distinguish a genuine slow cycle from a detector miss that produced a heel-strike-to-heel-strike interval longer than one cycle — would require the segmenter to inspect contact-gap structure (e.g. swing-time within the cycle, force-plate or contralateral HS hints) rather than the cycle-duration interval alone. Aligning to a longer label set is deferred until a downstream consumer needs the granularity.

### Long-format alternative (not implemented)

The schema's earlier draft described a long-format table (one row per `(cycle, feature)` pair, with `feature_name`/`feature_value`/`feature_unit`/`feature_method` columns). The realized table is wide-format (one row per cycle, one column per feature). Long-format is preferable if a future cycle materializes per-feature metadata (units, method) as separate columns; the conversion is a `pd.melt` away.

### Multi-session widening (not implemented)

`session` is currently hardcoded to `"S01"` in `scripts/features.py::extract_features` because the existing-data zeroth pilot is single-session. When R5 begins (per `ROADMAP.md` §Phase R5), the column needs to be derived from trial metadata and the hardcoded literal removed.

## Features to avoid at first

Avoid first-pass features that are hard to interpret in the pre-pilot:

- black-box embeddings from raw video
- participant identity predictions
- facial or clothing features
- unreviewed automated labels
- diagnosis-like scores
- any feature that cannot be traced back to a cycle and condition

## Output

The feature table should support three questions:

- Do repeated cycles within a condition resemble each other?
- Do right and left sides differ in interpretable ways?
- Do unsupervised structures remain after accounting for speed, footwear, and capture notes?

If the table cannot answer those questions, revise extraction before modeling. The first-pass set is sufficient to support question 2 *when segmentation produces both sides* (currently it does not — see `reports/field-report-01-existing-data-zeroth-pilot.md` §Segmentation Status and `ROADMAP.md` §Phase R2). Questions 1 and 3 are gated on candidate-set features that depend on segmenter throughput; their gating constraints are named per-candidate above.

The method for side-pairing is defined in [Left Right Comparison](left-right-comparison.md).
