# OpenCap Export Manifest

This file defines expected outputs from OpenCap processing and quality assessment criteria.

## Expected Exports per Trial

For each trial video processed through OpenCap, expect the following output files:

### Core Biomechanical Files
| File Type | Extension | Description | Required |
|-----------|-----------|-------------|----------|
| Inverse Kinematics | `.ik.mot` | Joint angles over time | Yes |
| Inverse Dynamics | `.id.sto` | Joint moments and forces | Yes |
| Muscle Analysis | `.muscle.sto` | Muscle activations and forces | No |
| Body Kinematics | `.body.sto` | Segment positions and orientations | Yes |

### Marker and Model Files
| File Type | Extension | Description | Required |
|-----------|-----------|-------------|----------|
| Marker Trajectories | `.trc` | 3D marker positions | Yes |
| Model File | `.osim` | Scaled OpenSim model | Yes |
| Setup Files | `.xml` | Processing configuration | No |

### Analysis Files
| File Type | Extension | Description | Required |
|-----------|-----------|-------------|----------|
| Gait Events | `.txt` or `.csv` | Heel strikes and toe offs | Yes |
| Gait Analysis | `.sto` | Stride time, step length, etc. | Yes |
| Summary Report | `.pdf` or `.html` | Processing summary | No |

## File Naming Convention

Expected pattern: `{ParticipantCode}_{SessionID}_{TrialID}_{FileType}.{Extension}`

Example:
- `P001_S01_T01_normal_shod_ik.mot`
- `P001_S01_T01_normal_shod_id.sto`
- `P001_S01_T01_normal_shod_body.sto`
- `P001_S01_T01_normal_shod_scaled.osim`

## Quality Checklist

For each processed trial, verify:

### Processing Completion
- [ ] All required files generated
- [ ] File sizes reasonable (not empty, not impossibly large)
- [ ] No processing error messages in logs
- [ ] Processing time reasonable for video length

### Marker Tracking Quality
- [ ] Markers visible throughout most of trial
- [ ] No obvious tracking jumps or discontinuities
- [ ] Left and right markers distinguishable
- [ ] Minimal occlusions during stance phases
- [ ] Marker trajectories smooth and physiologically plausible

### Inverse Kinematics Quality
- [ ] Joint angles within physiological range
- [ ] No impossible joint combinations
- [ ] Smooth angle progression over time
- [ ] Left-right symmetry reasonable
- [ ] No obvious artifacts or spikes

### Gait Event Detection
- [ ] Heel strikes clearly identified
- [ ] Toe offs clearly identified
- [ ] Event timing consistent with video
- [ ] Stride times physiologically reasonable (0.8-1.4 seconds typical)
- [ ] Step lengths physiologically reasonable

### Model Scaling
- [ ] Model scale factors reasonable (0.7-1.5 typical range)
- [ ] Segment lengths match apparent body proportions
- [ ] Mass properties appropriately scaled
- [ ] No negative scale factors

## Common Failure Modes

### Video Quality Issues
- **Poor lighting**: Markers not consistently visible
- **Motion blur**: Fast movements cause tracking loss
- **Occlusion**: Body parts block marker visibility
- **Background clutter**: Interferes with marker detection

### Marker Setup Issues
- **Missing markers**: Required markers not placed
- **Wrong marker labels**: Left/right confusion
- **Loose markers**: Movement during trial
- **Insufficient marker contrast**: Poor visibility against clothing

### Processing Issues
- **Incomplete trials**: Video too short for full gait cycles
- **Multiple people**: Additional people in camera view
- **Camera motion**: Unstable camera during recording
- **Calibration failure**: OpenCap cannot establish coordinate system

## Minimum Usable Criteria

A trial is considered usable if:

1. **Duration**: At least 6 complete gait cycles captured
2. **Quality**: At least 4-6 middle cycles are clean (exclude first/last cycles)
3. **Tracking**: >90% of critical markers visible during stance phases
4. **Events**: Heel strikes and toe offs clearly detectable
5. **Kinematics**: Joint angles physiologically reasonable throughout

## Quality Ratings

Rate each export on this scale:

### Excellent (A)
- All markers tracked perfectly
- No missing data or artifacts  
- Clear gait events
- 8+ usable cycles
- Ready for immediate analysis

### Good (B)
- Minor tracking issues that don't affect analysis
- 6-8 usable cycles
- Gait events clear
- May need minor data cleaning

### Fair (C)
- Moderate tracking issues
- 4-6 usable cycles
- Some gait events unclear
- Requires careful data cleaning
- Marginal for analysis

### Poor (D)
- Significant tracking failures
- <4 usable cycles
- Unclear gait events
- Extensive data cleaning needed
- Consider re-recording

### Unusable (F)
- Processing failed
- No usable cycles
- Must re-record with improved setup

## Export Validation Steps

1. **File Check**: Verify all required files present and properly named
2. **Size Check**: Confirm file sizes reasonable (not empty/corrupted)
3. **Visual Inspection**: Plot key joint angles, check for artifacts
4. **Event Validation**: Compare detected events with video timestamps
5. **Symmetry Check**: Compare left and right side measurements
6. **Range Check**: Verify all values within physiological bounds
7. **Documentation**: Record quality rating and any issues in session notes

## Troubleshooting

### If exports are missing:
1. Check OpenCap processing logs for errors
2. Verify input video format and quality
3. Confirm marker setup meets OpenCap requirements
4. Re-process with adjusted settings if needed

### If quality is poor:
1. Review video for the specific failure modes listed above
2. Consider re-recording with improved setup
3. Document issues for protocol refinement
4. Flag low-quality data appropriately in analysis

## Integration with Analysis Pipeline

Exports from this manifest feed into:
- [Feature extraction](../../analysis/features.md) using the [feature table schema](../../analysis/feature-table-schema.md)
- [Session notes](../session-notes-template.md) for quality documentation
- [Field reporting](../../reports/field-report-01-friend-pre-pilot.md) for pipeline assessment