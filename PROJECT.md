# Project Status and Implementation

This file owns project status, current stage, and implementation progress.

## Current Stage

**Stage:** Methods design and documentation complete
**Phase:** Ready for field testing
**Next action:** Execute friend pre-pilot protocol

## Implementation Status

### Documentation Complete ✓

All 24 content files have been written and organized:

- 5 realization documents in `docs/realizations/`
- 4 concept documents in `docs/concepts/`
- 3 ethics documents in `docs/ethics/`
- 4 protocol documents in `protocols/`
- 3 instrument documents in `instruments/opencap/`
- 3 analysis documents in `analysis/`
- 2 report templates in `reports/`

### Next Phase: Field Testing

**Immediate next step:** Execute the friend pre-pilot protocol defined in [protocols/friend-pre-pilot.md](protocols/friend-pre-pilot.md)

**Goals for pre-pilot:**
- Test whether the pipeline can capture usable OpenCap data
- Validate gait cycle segmentation
- Extract interpretable movement curves
- Compare left and right stance phases
- Test whether blind observation can be compared with kinematic data

**Success condition:** Methodological clarity about whether OpenCap-derived gait-cycle data contains enough structure to pursue support-path classification.

## Current Realization Sequence

The project moves through five realizations. Each realization should answer one question and produce one artifact.

### Realization 01 — Walking Is Not a Style

Walking is a recurring whole-body load-transfer strategy, not a visual aesthetic.

**Status:** Complete ✓
**Artifact:** `docs/realizations/01-walking-is-not-a-style.md`

### Realization 02 — The Type List Is Not the Object

Visible walking categories are provisional language. The object is the step, the support path, and the gait-cycle data.

**Status:** Complete ✓
**Artifact:** `docs/realizations/02-the-type-list-is-not-the-object.md`

### Realization 03 — OpenCap Is the Translation Layer

OpenCap converts video into biomechanical time series. It is not the classifier.

**Status:** Complete ✓
**Artifact:** `docs/realizations/03-opencap-is-the-translation-layer.md`

### Realization 04 — Friends Are a Pre-Pilot

The first friend cohort exists to break the pipeline, not to validate the theory.

**Status:** Complete ✓
**Artifact:** `docs/realizations/04-friends-are-a-pre-pilot.md`

### Realization 05 — What Broke

The first field report documents what survived, what failed, what was visible, and what was not.

**Status:** Pending field testing
**Artifact:** `docs/realizations/05-what-broke.md` (template ready)

## Implementation Timeline

### Completed
- Methods design and theory documentation
- Protocol development
- Ethics framework
- Analysis plan
- Instrument selection and documentation

### In Progress
- Preparation for friend pre-pilot execution

### Upcoming
- Friend pre-pilot execution (5-10 participants)
- Pipeline testing and validation
- Field report generation
- Theory revision based on empirical results

## Friend Pre-Pilot Overview

The first cohort tests pipeline coherence, not theory validation.

**Purpose:** Test whether the pipeline can capture, process, segment, and compare walking data well enough to decide whether a larger pilot is worth designing.

**Target outcome:** Discrepancy analysis between blind observation and processed data.

**Implementation details:** See [protocols/friend-pre-pilot.md](protocols/friend-pre-pilot.md)

## Risk Management

**Methodological risks:**
- OpenCap outputs may be too noisy for intended analysis
- Proposed categories may remain only visual impressions
- Pipeline may fail at gait cycle segmentation

**Mitigation:** Pre-pilot designed to reveal these failures early

**Ethical risks:**
- Identifiable biometric data mishandling
- Participant pressure or inappropriate labeling

**Mitigation:** Explicit consent protocols and data handling guidelines in [docs/ethics/](docs/ethics/)

## Source of truth

| Question | Owning file |
|----------|-------------|
| What is this repo? | `README.md` |
| What is a support path? | `docs/concepts/support-path.md` |
| What is the unit of analysis? | `docs/concepts/gait-cycle-as-unit.md` |
| How is the friend pre-pilot run? | `protocols/friend-pre-pilot.md` |
| How are recordings captured? | `protocols/capture-setup.md` |
| What does OpenCap provide? | `instruments/opencap/outputs-to-extract.md` |
| What are OpenCap's limits? | `instruments/opencap/limitations.md` |
| Which features are extracted? | `analysis/features.md` |
| How are clusters tested? | `analysis/clustering-plan.md` |
| How is data handled? | `docs/ethics/data-handling.md` |

Do not duplicate stable facts across files. State the fact once in its owning file and point to it elsewhere.

## Success Criteria

**Primary success condition:** Methodological clarity, not classification accuracy.

After the pre-pilot, the project should know whether OpenCap-derived gait-cycle data contains enough structure to pursue support-path classification.

**Specific success indicators:**
- Usable gait cycles extracted from video data
- Interpretable movement curves generated
- Left-right stance phase comparison possible
- Blind observation comparable with kinematic traces
- Repeatable data across trials

## Decision Points

**Go/No-Go after pre-pilot:**
- **Go:** If pipeline produces interpretable, repeatable gait-cycle data
- **Revise:** If method needs adjustment but concept remains viable  
- **Stop:** If fundamental assumptions fail measurement test

**Failure conditions:** See [docs/concepts/failure-conditions.md](docs/concepts/failure-conditions.md)

The goal is to find out what survives contact with measurement, not to protect the theory.
