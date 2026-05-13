# Existing-Data Zeroth Pilot

## Governing Question

Can the project process existing OpenCap validation walking data into segmented gait cycles, feature tables, plots, and support-path hypotheses before collecting new participant data?

## Purpose

This zeroth pilot validates the analysis pipeline using publicly available OpenCap Lab Validation data rather than collecting new participant data. Success here proves the technical foundation is sound before engaging friends or other participants.

## Dataset Selection Rules

**Primary target:** OpenCap Lab Validation dataset from SimTK
- Must include walking trials at multiple speeds
- Must include both OpenCap estimates and reference measurements (force plates, optical motion capture)
- Must be publicly available with clear licensing terms
- Must include sufficient trial repetitions for left-right comparison

**Backup datasets:** Other validated OpenCap datasets with walking data if primary target is insufficient

**Exclusion criteria:**
- Datasets without walking trials
- Datasets without reference validation measurements
- Datasets with unclear licensing or access restrictions
- Datasets with only single-trial recordings

## Required Outputs

The existing-data zeroth pilot must produce:

### 1. Dataset Manifest
- Dataset name, source URL, access date
- License terms and usage permissions  
- Files downloaded and local storage location
- Available data types (video, markers, GRF, EMG, OpenCap estimates)
- Walking trials identified with speeds and conditions

### 2. Walking-Trial Inventory
- Trial naming convention and organization
- Number of walking trials per participant
- Speed conditions and duration of each trial
- Quality assessment of each trial (complete gait cycles, clean data)

### 3. OpenCap/OpenSim Output Inventory  
- Available time series (joint angles, segment positions, timing events)
- Data quality indicators and processing flags
- Missing or corrupted output identification
- Comparison with reference measurements where available

### 4. Gait-Cycle Segmentation Notes
- Heel-strike detection methods and results
- Number of complete gait cycles extracted per trial
- Left-right gait cycle matching
- Segmentation quality assessment and failure cases

### 5. Feature Table
- Features extracted per gait cycle as defined in [analysis/features.md](../analysis/features.md)
- Left-right feature comparison statistics
- Cross-trial repeatability assessment
- Feature distribution summaries

### 6. First-Pass Plots
- Time-normalized gait cycle traces (hip, knee, ankle angles)
- Left-right overlay comparisons
- Speed condition comparisons
- Feature distribution visualizations

### 7. OpenCap-vs-Reference Comparison
- Comparison statistics where reference data available
- Agreement measures and discrepancy patterns
- Assessment of OpenCap reliability for intended analysis
- Identification of systematic biases or limitations

### 8. Support-Path Inference Memo
- Initial observations of coordination patterns
- Candidate support path hypotheses based on extracted features
- Assessment of whether data contains sufficient structure for clustering
- Recommendations for feature refinement

### 9. Failure Report
- Technical failures in data processing pipeline
- Data quality issues that prevented analysis
- Pipeline bottlenecks or limitations discovered
- Recommendations for protocol revision

## Go/No-Go Criteria

**GO Conditions:**
- Successfully segment ≥80% of walking trials into clean gait cycles
- Extract interpretable feature tables with <20% missing data
- Achieve reasonable agreement with reference measurements where available
- Generate ≥3 candidate support-path hypotheses from coordination patterns
- Complete pipeline runs without major technical failures

**NO-GO Conditions:**
- <60% of trials successfully segmented into gait cycles
- Feature extraction fails on >30% of segmented cycles
- Systematic disagreement with reference measurements
- No discernible coordination patterns in extracted features
- Multiple pipeline failures preventing analysis completion

**REVISE Conditions:**
- Partial success requiring protocol or analysis adjustments
- Technical issues solvable with minor pipeline modifications
- Data quality sufficient but requiring refined feature selection

## Methodological Constraints

**No clustering yet:** This phase focuses on data processing and feature extraction only. Clustering analysis is reserved for later phases after technical validation.

**No UMAP yet:** Dimensionality reduction and visualization techniques are reserved for after feature validation.

**Boring first:** Prioritize download→manifest→segment→plot→extract→compare→write over sophisticated analysis.

**Reference validation required:** Where possible, compare OpenCap estimates against gold-standard measurements to establish confidence bounds.

## Success Definition

**Technical validation achieved:** The analysis pipeline can reliably process existing OpenCap walking data and extract meaningful gait-cycle features.

**Analysis readiness confirmed:** Extracted features contain sufficient structure and interpretability to justify proceeding with clustering and support-path classification.

**Method confidence established:** OpenCap-derived data quality is adequate for the intended research questions.

## Timeline

**Duration:** 2-3 weeks
- Week 1: Dataset acquisition, inventory, and initial processing
- Week 2: Feature extraction, plotting, and comparison analysis  
- Week 3: Support-path inference, failure analysis, and reporting

## Outputs Location

- Dataset manifest: `data/external/opencap-lab-validation.md`
- Processing results: `notebooks/existing-data-processing.ipynb`
- Field report: `reports/field-report-01-existing-data-zeroth-pilot.md`

## Next Phase Gate

Upon successful completion, the project proceeds to friend pre-pilot as defined in [friend-pre-pilot.md](friend-pre-pilot.md).

Upon failure, the project revises methods or reconsiders core assumptions as documented in failure report.