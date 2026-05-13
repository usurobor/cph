# Capture Rehearsal

Before recording each friend participant, run one throwaway OpenCap session to verify setup and identify problems.

## Purpose

The rehearsal serves three functions:
1. **Technical verification**: Confirm equipment and setup work correctly
2. **Protocol refinement**: Identify setup problems before participant arrives  
3. **Baseline establishment**: Understand expected data quality for current conditions

## Rehearsal Participant

Use any available person for rehearsal. This can be:
- The researcher conducting the study
- A lab member or colleague
- A friend or family member willing to help with setup

**Important**: Rehearsal data is never analyzed or published. It exists only to test the pipeline.

## Rehearsal Protocol

### Setup Verification
1. **Equipment check**
   - [ ] Camera charged and working
   - [ ] Recording resolution set correctly
   - [ ] Frame rate configured (minimum 30fps, preferably 60fps)
   - [ ] Memory card has sufficient space
   - [ ] Backup storage ready

2. **Environment check**
   - [ ] Walking area clear (minimum 4 meters)
   - [ ] Lighting adequate and consistent
   - [ ] Background relatively clear
   - [ ] Minimal distractions
   - [ ] Surface appropriate for walking

3. **OpenCap setup**
   - [ ] OpenCap app installed and working
   - [ ] Camera calibration completed
   - [ ] Test upload successful
   - [ ] Processing queue functional

### Recording Test
1. **Single trial recording**
   - Record 30-60 seconds of normal walking
   - Capture at least 6-8 complete gait cycles
   - Use shod condition for simplicity
   - Walk at normal, comfortable speed

2. **Immediate assessment**
   - [ ] Video plays without corruption
   - [ ] Both feet clearly visible throughout most of trial
   - [ ] Lighting consistent
   - [ ] No obvious camera shake or movement
   - [ ] Walking path appropriate length

### OpenCap Processing Test
1. **Upload and process**
   - Upload rehearsal video to OpenCap
   - Process through full pipeline
   - Wait for completion (typically 10-30 minutes)
   - Download all output files

2. **Output verification**
   - [ ] All expected files generated (see [export manifest](../instruments/opencap/export-manifest.md))
   - [ ] File sizes reasonable
   - [ ] No processing error messages
   - [ ] Joint angles within physiological range
   - [ ] Gait events detected correctly

## Minimum Usable Cycles

Use these criteria to assess whether the setup will produce usable data:

### Cycle Definition
- **Gait cycle**: Right heel strike to next right heel strike (or left heel strike to next left heel strike)
- **Complete cycle**: Clear heel strike and toe off events detectable
- **Clean cycle**: No obvious tracking failures, occlusions, or artifacts

### Minimum Requirements per Trial
- **Target**: 6-8 complete cycles per side
- **Usable minimum**: 4-6 middle cycles per side  
- **Insufficient**: <3 clean cycles per side
- **Analysis cycles**: Exclude first and last cycles, use middle cycles only

### Quality Gates
1. **Excellent setup**: 8+ clean cycles per side expected
2. **Good setup**: 6-8 clean cycles per side expected
3. **Marginal setup**: 4-6 clean cycles per side expected
4. **Poor setup**: <4 cycles per side expected, requires improvement

## Setup Issues and Solutions

### Common Problems Found During Rehearsal

#### Video Quality Issues
| Problem | Solution |
|---------|----------|
| Poor lighting | Adjust recording time, location, or add lighting |
| Motion blur | Increase frame rate or improve camera stabilization |
| Shaky camera | Use tripod or more stable camera position |
| Cluttered background | Change camera angle or clear background |

#### Tracking Issues  
| Problem | Solution |
|---------|----------|
| Feet not fully visible | Adjust camera position or walking path |
| Clothing interferes | Request different clothing or marker contrast |
| Walking path too short | Extend walking area or change camera position |
| Multiple people in frame | Clear area or change camera angle |

#### OpenCap Processing Issues
| Problem | Solution |
|---------|----------|
| Upload fails | Check internet connection, video format, file size |
| Processing fails | Review video quality, try different camera angle |
| Poor marker tracking | Improve lighting, contrast, clothing choice |
| No gait events detected | Ensure full gait cycles captured, check video quality |

## Go/No-Go Decision

After rehearsal, decide whether to proceed:

### GO: Proceed with participant recording if:
- [ ] Rehearsal produces 4+ clean cycles per side
- [ ] OpenCap processing completes without errors
- [ ] Output files meet quality standards from [export manifest](../instruments/opencap/export-manifest.md)
- [ ] Setup problems identified and resolved
- [ ] Expected data quality sufficient for analysis goals

### NO-GO: Improve setup before participant if:
- [ ] <3 clean cycles per side in rehearsal
- [ ] OpenCap processing fails consistently  
- [ ] Major tracking or technical issues unresolved
- [ ] Video quality insufficient for marker detection
- [ ] Environmental conditions unsuitable

## Setup Refinement

Based on rehearsal results, adjust:

### Camera Position
- Height relative to participant
- Distance from walking path
- Angle to capture both feet clearly
- Stability and mounting

### Environment
- Lighting direction and intensity
- Background simplification
- Walking path length and surface
- Distraction elimination

### Recording Parameters
- Resolution and frame rate
- Recording duration
- Number of trials planned
- Backup procedures

## Documentation

Record rehearsal results in brief notes:

```
Rehearsal Date: ___________
Rehearsal Participant: ___________
Setup Location: ___________
Expected Cycles per Side: ___________
OpenCap Processing: [ ] Success [ ] Failed
Major Issues Found: ___________
Setup Changes Made: ___________
Go/No-Go Decision: [ ] GO [ ] NO-GO
```

## Integration with Friend Protocol

1. **Before participant session**: Complete capture rehearsal
2. **During participant session**: Apply lessons learned from rehearsal
3. **After participant session**: Compare actual data quality with rehearsal predictions
4. **Pipeline refinement**: Update rehearsal protocol based on accumulated experience

The rehearsal is not optional. Every friend recording session should be preceded by a technical rehearsal to maximize the chance of collecting usable data.

## Time Budget

- **Setup and equipment check**: 15 minutes
- **Rehearsal recording**: 10 minutes  
- **OpenCap upload and processing**: 20-30 minutes
- **Results review and setup adjustment**: 15 minutes
- **Total rehearsal time**: ~60-70 minutes

Plan this time before each participant session. The rehearsal investment pays for itself by reducing failed recordings and improving data quality.