# Feature Table Schema

This file defines the column structure for gait feature extraction tables.

## Purpose

Feature tables store extracted measurements from gait cycles. Each row represents one feature value from one gait cycle under one condition.

## Required Columns

### Identification
| Column | Type | Description | Null | Example |
|--------|------|-------------|------|---------|
| `participant_code` | string | Anonymous participant identifier | No | "P001" |
| `session_id` | string | Session identifier within participant | No | "S01" |
| `trial_id` | string | Trial identifier within session | No | "T01_normal_shod" |
| `condition` | string | Walking condition tested | No | "normal_shod" |
| `side` | string | Body side for cycle | No | "left", "right" |

### Cycle Definition
| Column | Type | Description | Null | Example |
|--------|------|-------------|------|---------|
| `cycle_number` | integer | Cycle number within trial | No | 3 |
| `cycle_start_frame` | integer | Video frame where cycle begins | No | 120 |
| `cycle_end_frame` | integer | Video frame where cycle ends | No | 180 |

### Quality Control
| Column | Type | Description | Null | Example |
|--------|------|-------------|------|---------|
| `quality_flag` | string | Data quality assessment | No | "good", "poor", "unusable" |
| `exclusion_flag` | boolean | Should cycle be excluded from analysis | No | true, false |
| `exclusion_reason` | string | Reason for exclusion if flagged | Yes | "incomplete_cycle", "marker_loss" |

### Feature Data
| Column | Type | Description | Null | Example |
|--------|------|-------------|------|---------|
| `feature_name` | string | Name of extracted feature | No | "stance_duration" |
| `feature_value` | float | Numerical value of feature | Yes | 0.62 |
| `feature_unit` | string | Unit of measurement | Yes | "seconds" |
| `feature_method` | string | Extraction method used | No | "heel_strike_to_toe_off" |
| `source_file` | string | OpenCap output file used | No | "P001_S01_T01_ik.mot" |

## Allowed Values

### condition
- `normal_shod`: Normal walking speed with shoes
- `normal_barefoot`: Normal walking speed barefoot  
- `slow_shod`: Slow walking speed with shoes
- `slow_barefoot`: Slow walking speed barefoot
- `fast_shod`: Fast walking speed with shoes
- `fast_barefoot`: Fast walking speed barefoot

### side
- `left`: Left stance phase
- `right`: Right stance phase

### quality_flag
- `good`: Clean data, no visible artifacts
- `fair`: Usable data with minor artifacts
- `poor`: Questionable data quality
- `unusable`: Should not be analyzed

### feature_method
- `heel_strike_to_toe_off`: Full stance phase timing
- `opencap_ik`: Inverse kinematics from OpenCap
- `opencap_id`: Inverse dynamics from OpenCap
- `joint_angle_range`: Min-max joint angle calculation
- `asymmetry_index`: Left-right comparison ratio

## Data Rules

1. **One row per feature per cycle**: Each gait cycle can produce multiple features, each gets its own row
2. **No missing identifiers**: participant_code, session_id, trial_id, condition, side, cycle_number must never be null
3. **Quality gates**: Any cycle with quality_flag="unusable" should have exclusion_flag=true
4. **Exclusion reasons**: If exclusion_flag=true, exclusion_reason must be provided
5. **Feature completeness**: feature_name and feature_method are required; feature_value can be null if extraction failed
6. **Units consistency**: If feature_value is provided, feature_unit should be provided unless dimensionless

## Example Rows

```csv
participant_code,session_id,trial_id,condition,side,cycle_number,cycle_start_frame,cycle_end_frame,quality_flag,exclusion_flag,exclusion_reason,feature_name,feature_value,feature_unit,feature_method,source_file
P001,S01,T01_normal_shod,normal_shod,right,3,120,180,good,false,,stance_duration,0.62,seconds,heel_strike_to_toe_off,P001_S01_T01_ik.mot
P001,S01,T01_normal_shod,normal_shod,right,3,120,180,good,false,,hip_flexion_max,35.2,degrees,joint_angle_range,P001_S01_T01_ik.mot
P001,S01,T01_normal_shod,normal_shod,right,4,181,240,poor,true,incomplete_cycle,,,,,P001_S01_T01_ik.mot
```

## Implementation Notes

- Use this schema for all gait feature extraction
- Validate data against these rules before analysis
- Store tables as CSV with UTF-8 encoding
- Include schema version in table metadata