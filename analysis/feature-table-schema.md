# Feature Table Schema

This file defines the column structure for gait feature extraction tables.

## Purpose

Feature tables store extracted measurements from gait cycles. The realized table emitted by `scripts/features.py::build_feature_table` is **wide-format**: one row per cycle, with each feature occupying its own column. The earlier draft of this schema described a long-format table (one row per `(cycle, feature)` pair with `feature_name`/`feature_value` columns); that shape was never realized in code. The §"Feature Data" section below describes the wide format that is actually emitted; the long-format alternative is named as deferred work in `analysis/features.md` §"Candidate set" and would land if a future cycle materializes per-feature metadata (units, method) as separate columns.

## Required Columns

### Identification
| Column | Type | Description | Null | Example |
|--------|------|-------------|------|---------|
| `subject` | string | Anonymous subject identifier | No | "subject2" |
| `session` | string | Session identifier within subject (currently hardcoded to `"S01"` — see *Single-session note* below) | No | "S01" |
| `trial_id` | string | Trial identifier within session | No | "walking1" |
| `condition` | string | Walking condition tested | No | "walking" |
| `side` | string | Body side for cycle | No | "L", "R" |

**Single-session note.** The existing-data zeroth pilot (per [`reports/field-report-01-existing-data-zeroth-pilot.md`](../reports/field-report-01-existing-data-zeroth-pilot.md)) operates on a single capture session per subject from the OpenCap Lab Validation archive. `scripts/features.py::extract_features` therefore emits `session = "S01"` as a fixed literal. When the project moves to multi-session captures (R5 onward, per [`ROADMAP.md`](../ROADMAP.md) §Phase R5), the column needs to be derived from trial metadata and the literal removed. This widening is named as deferred work in `analysis/features.md` §"Candidate set" and is gated on the R5 friend pre-pilot beginning.

### Cycle Definition
| Column | Type | Description | Null | Example |
|--------|------|-------------|------|---------|
| `cycle_number` | integer | Cycle number within trial | No | 3 |

(`cycle_start_frame` / `cycle_end_frame` columns are not currently emitted. The `Cycle` dataclass carries `start_time` / `end_time` in seconds; frame-index columns require a `sample_rate_hz` round-trip that is not implemented. Listed as deferred work in `analysis/features.md` §"Candidate set" → indexing widening.)

### Detection provenance
| Column | Type | Description | Null | Example |
|--------|------|-------------|------|---------|
| `detection_method` | string | How the cycle's endpoints were obtained: ipsilateral marker detection vs. contralateral inference (see *Allowed Values* below) | No | "measured", "inferred_contralateral", "inferred_contralateral_partial" |

This column was added in cph#28 to carry the path-(a) honesty caveat at the data-row level: inferred bilateral (L-side) cycles are tagged separately from measured (R-side) cycles so downstream consumers can filter or condition on detection provenance. The producer of `"inferred_contralateral"` and `"inferred_contralateral_partial"` is `scripts/segmentation_contralateral.py::segment_trial_with_contralateral_l`; the default value `"measured"` is set on `scripts/segmentation.py::Cycle.detection_method` and emitted by `scripts/segmentation.py::segment_trial` (R-side / standard detector path). Realized values are enumerated in *Allowed Values* §`detection_method` below; `analysis/r3_subject_aggregate_tests.py` excludes this column from per-feature aggregation via `NON_FEATURE_COLS`.

### Quality Control
| Column | Type | Description | Null | Example |
|--------|------|-------------|------|---------|
| `quality_flag` | string | Data quality assessment | No | "ok", "short", "long" |
| `exclusion_flag` | boolean | Should cycle be excluded from analysis (derived: `quality_flag != "ok"`) | No | True, False |

(`exclusion_reason` is not currently emitted as a separate column; the reason is implicit in `quality_flag` ("short", "long"). Materializing it as a dedicated string column is named in `analysis/features.md` §"Candidate set" → indexing widening.)

### Feature Data

The realized table is wide-format. Feature columns are emitted by the `extract_*` functions in `scripts/features.py`:

- `extract_timing` → `cycle_duration_s`, `stance_duration_s`, `swing_duration_s`, `stance_pct_cycle`, `timing_estimate_method`, `peak_knee_flexion_phase`
- `extract_range` → for each present joint (`hip_flexion`, `hip_adduction`, `knee_angle`, `ankle_angle`): `{joint}_range_deg`, `{joint}_peak_deg`, `{joint}_min_deg`; for each present pelvis axis (`pelvis_tilt`, `pelvis_list`, `pelvis_rotation`): `{axis}_range_deg`; for each present trunk axis (`lumbar_bending`, `lumbar_rotation`, `lumbar_extension`): `{axis}_range_deg`
- `extract_shape_sentinel` → `normalized_curve_available`
- `extract_coordination` → `hip_knee_lag_samples`, `hip_knee_lag_pct_cycle`

The exact feature column set is enumerated against the code in `analysis/features.md` §"First-pass set (currently implemented)".

## Allowed Values

### condition
- `normal_shod`: Normal walking speed with shoes
- `normal_barefoot`: Normal walking speed barefoot  
- `slow_shod`: Slow walking speed with shoes
- `slow_barefoot`: Slow walking speed barefoot
- `fast_shod`: Fast walking speed with shoes
- `fast_barefoot`: Fast walking speed barefoot

### side
- `L`: Left stance phase
- `R`: Right stance phase

(Single-character codes match what `scripts/segmentation.py::Cycle.side` emits and what `scripts/features.py::extract_features` propagates into the table. Earlier drafts of this schema used the long forms `"left"`/`"right"`; those were not realized in code. The widening to long forms is named as deferred work in `analysis/features.md` §"Candidate set" and would land alongside the multi-session widening.)

### detection_method

Realized values emitted by `scripts/segmentation.py::segment_trial` (default) and `scripts/segmentation_contralateral.py::segment_trial_with_contralateral_l` (L-side inference), propagated through `scripts/features.py::extract_features`:

- `measured`: cycle endpoints come from ipsilateral heel-marker detection (`scripts/segmentation.py::detect_heel_strikes`); the default value on `scripts/segmentation.py::Cycle.detection_method` and the only value emitted on the R-side / standard detector path.
- `inferred_contralateral`: L-side cycle whose start was inferred from the opposite-side (R) heel-strike plus a half-stride offset, and whose matched-duration window `[l_0, l_0 + T]` fits fully inside the trial sample range (full coverage). Produced by `scripts/segmentation_contralateral.py::segment_trial_with_contralateral_l`.
- `inferred_contralateral_partial`: same as `inferred_contralateral`, but the matched-duration window is clipped at the trial end. The clipped slice covers at least `min_coverage` (default 0.80) of the cycle duration `T` but strictly less than `T`. Produced by `scripts/segmentation_contralateral.py::segment_trial_with_contralateral_l`.

Consumers that need to distinguish measured cycles from inferred cycles (for the path-(a) honesty caveat — see `reports/field-report-01-existing-data-zeroth-pilot.md` §"L-side recovery (cph#28)") filter on this column; aggregate analyses that treat both detection paths uniformly leave it alone (excluded from per-feature aggregation by `analysis/r3_subject_aggregate_tests.py::NON_FEATURE_COLS`).

### quality_flag

Realized values emitted by `scripts/segmentation.py::segment_trial` and propagated through `scripts/features.py::extract_features`:

- `ok`: cycle duration in `(0.5, 1.8)` seconds; cycle passes segmenter QC
- `short`: cycle duration `<= 0.5` seconds (below typical adult walking range); `exclusion_flag=True`
- `long`: cycle duration `>= 1.8` seconds (above typical adult walking range, includes detector dropouts that produced a heel-strike-to-next-heel-strike interval that is too long to be a single cycle); `exclusion_flag=True`

(An earlier draft of this schema listed `good` / `fair` / `poor` / `unusable`, and a later draft listed `low_contact_gap` as a third realized label. Neither set is realized in code today — the segmenter only inspects cycle duration, not contact-gap structure. Finer-grained quality labels (e.g. `low_contact_gap` to distinguish a detector miss from a genuinely slow cycle) require segmenter changes and are named as deferred work in `analysis/features.md` §"Candidate set" → quality-flag widening.)

## Data Rules

1. **One row per cycle (wide format)**: each gait cycle produces one row; features occupy distinct columns. (The long-format alternative — one row per `(cycle, feature)` pair — is named as deferred work in `analysis/features.md` §"Candidate set".)
2. **No missing identifiers**: `subject`, `session`, `trial_id`, `condition`, `side`, `cycle_number` must never be null.
3. **Quality gates**: `exclusion_flag` is derived as `quality_flag != "ok"` by `scripts/features.py::extract_features`. No row should carry `quality_flag="ok"` with `exclusion_flag=True` (the derivation makes this impossible by construction).
4. **Feature completeness**: feature columns are NaN-tolerant. When a joint column is absent from the source data, the corresponding `{joint}_range_deg` / `{joint}_peak_deg` / `{joint}_min_deg` columns are simply omitted from the row dict (and become NaN after `pd.DataFrame(rows)`).

## Example Rows

```csv
subject,session,trial_id,condition,side,cycle_number,quality_flag,exclusion_flag,detection_method,cycle_duration_s,stance_duration_s,swing_duration_s,stance_pct_cycle,hip_flexion_range_deg,knee_angle_range_deg,hip_knee_lag_pct_cycle
subject2,S01,walking1,walking,R,3,ok,False,measured,1.05,0.65,0.40,61.9,38.4,55.2,12.5
subject2,S01,walking1,walking,L,3,ok,False,inferred_contralateral_partial,1.04,0.63,0.41,60.6,37.9,54.8,13.1
subject4,S01,walking2,walking,R,1,short,True,measured,0.42,0.25,0.17,59.5,18.2,28.3,
```

The first-row-of-table schema is the actual output of `scripts/features.py::build_feature_table` on the merged feature table. The full set of feature columns (timing / range / shape / coordination, ~21 columns when all joints are present) is enumerated in `analysis/features.md` §"First-pass set (currently implemented)".

## Implementation Notes

- Use this schema for all gait feature extraction
- Validate data against these rules before analysis
- Store tables as CSV with UTF-8 encoding
- Include schema version in table metadata