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

### Access mechanism

A permissive license (Apache 2.0, MIT, CC-BY, public domain) is necessary but not sufficient: the project also requires that the chosen dataset be **acquireable in the cycle's actual execution environment**. The four selection rules above cover license; this subsection covers the access channel.

**What counts as "publicly accessible" in this project's sense:**

A dataset is publicly accessible if **all** of the following hold:
1. The license permits the project's intended use without per-user agreement (the four rules above).
2. The download endpoint serves the archive to an unauthenticated HTTP client (no login wall, no API token, no per-user agreement click-through that issues a session cookie).
3. The archive can be fetched and verified (SHA-256 or equivalent) without operator-supplied credentials.

A dataset that satisfies (1) but not (2) or (3) is **licensed-permissive-but-gated**. It is still a valid candidate; it just requires explicit operator credentials before the cycle can proceed.

**Authentication / credential gates to check before selection:**

- Account-required download portals (SimTK, Figshare-private, OSF-private, Synapse, PhysioNet credentialed tier).
- API tokens (e.g., the OpenCap API `API_TOKEN`, dataset-specific service tokens).
- Click-through Data Use Agreements that bind a named user.
- IRB-style restricted-access tiers, even when the underlying data is de-identified.
- Captcha or human-verification walls on the file endpoint.

The probe is concrete: attempt an unauthenticated `curl -L -o /dev/null` against the file URL. A 200 with the archive bytes means "open access mechanism"; a redirect to a login page, a 401/403, or an HTML login form means "gated access mechanism."

**Operator-supplied credential expectations:**

If the chosen dataset is licensed-permissive-but-gated, the cycle proceeds only if **all** of the following are arranged before the wave's α cycle starts:
- The operator commits to supplying the credentials (account, API token, signed DUA) for the cycle's execution environment.
- The wave manifest's standing permissions explicitly include the credential channel (e.g., "operator will export `SIMTK_USER` / `SIMTK_PASS` into the cycle environment").
- The dataset manifest (`data/external/<dataset>.md`) documents the acquisition procedure step-by-step so the credential exchange is auditable.

If any of the three is missing, the candidate must be **escalated to the wave operator** before selection is finalized. Escalation is not rejection — the operator may supply the gap, or may direct the cycle to fall back to a backup dataset (see §Backup datasets above). Escalation is the same loop used for non-permissive license: a one-line note in the manifest's §Acquisition status, plus a follow-up entry in the wave's escalation log.

The result: a reader of this protocol can answer "is this candidate dataset acquireable in our environment?" *before* selection is finalized, without consulting the wave manifest.

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