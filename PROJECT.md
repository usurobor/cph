# Project Status and Implementation

This file owns project status, current stage, and implementation progress.

## Current Stage

**Stage:** Existing-data zeroth pilot — REVISE
**Phase:** Pipeline implemented + smoke-tested; empirical run blocked at dataset acquisition (SimTK login).
**Next action:** Operator runs the acquisition procedure in `data/external/opencap-lab-validation.md §Acquisition procedure`; protocol `protocols/existing-data-zeroth-pilot.md` to be revised with an "Access mechanism" subsection (see `reports/field-report-01-existing-data-zeroth-pilot.md` §Recommendation). After acquisition, re-execute `notebooks/existing-data-processing.ipynb` against real data and re-evaluate the GO/NO-GO criteria.

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

### Next Phase: Existing Data Processing

**Immediate next step:** Process existing OpenCap Lab Validation walking data as defined in [protocols/existing-data-zeroth-pilot.md](protocols/existing-data-zeroth-pilot.md)

**Goals for existing-data processing:**
- Test whether the pipeline can process downloaded OpenCap validation data
- Validate gait cycle segmentation on existing datasets  
- Extract interpretable movement curves from known-good data
- Compare OpenCap estimates against reference measurements
- Generate first-pass support-path hypotheses from controlled conditions

**Success condition:** Technical validation that the analysis pipeline can produce meaningful outputs from existing OpenCap data before collecting new participant data.

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

### Realization 04 — Existing Data Comes First

Process existing validation datasets before collecting new participant data.

**Status:** REVISE — pipeline implemented and smoke-tested under the zeroth-pilot wave (2026-05-15); empirical execution blocked at dataset acquisition (SimTK login gate). See `reports/field-report-01-existing-data-zeroth-pilot.md` for the wave's REVISE decision and required protocol revision.
**Artifact:** `docs/realizations/04-existing-data-comes-first.md`

### Realization 05 — Friends Are Not Validation

The friend cohort tests pipeline robustness, not theoretical claims.

**Status:** Complete ✓  
**Artifact:** `docs/realizations/05-friends-are-not-validation.md`

### Realization 06 — What Broke

The first field report documents what survived, what failed, what was visible, and what was not.

**Status:** Pending field testing
**Artifact:** `docs/realizations/06-what-broke.md` (template ready)

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
