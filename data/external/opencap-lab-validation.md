# OpenCap Lab Validation Dataset

## Dataset Information

**Dataset name:** OpenCap Lab Validation (Stanford NMBL)
**Source URL:** https://simtk.org/projects/opencap (SimTK project 2385)
**Source paper:** Uhlrich SD, Falisse A, Kidziński Ł, et al. "OpenCap: Human movement dynamics from smartphone videos." PLOS Computational Biology 19(10): e1011462 (2023). https://doi.org/10.1371/journal.pcbi.1011462
**Access date:** 2026-05-15 (dataset identified; download pending — see §Acquisition status)
**Data type:** Publicly documented validation dataset, Apache 2.0
**License/Terms:** Apache License 2.0 (SimTK download confirm page).
  Per Apache 2.0: free to use, modify, distribute with attribution.
  No clinical/IRB restrictions stated.

## Acquisition status

**Download status: BLOCKED — SimTK account registration required.**

The dataset is licensed Apache 2.0 (permissive, no usage restrictions). However, the file download endpoint at SimTK (`/frs/download_confirm.php/file/{id}/...zip?group_id=2385`) requires an authenticated SimTK user session — the SimTK platform enforces a login wall in front of all file downloads regardless of license. Probing the endpoint returns a JavaScript redirect to `/account/login.php`.

The OpenCap public S3 bucket (`mc-opencap-public.s3.us-west-2.amazonaws.com`) hosts processed/derivative assets (OpenSim geometries, etc.) but is configured to deny anonymous listing and does not host the Lab Validation archive at a guessable key.

The `opencap-processing` Python client (Stanford NMBL) also requires an OpenCap API token (`API_TOKEN`) and is therefore blocked under the same gate.

**Escalation:** This is an access-mechanism block, not a license block. Operator credentials (SimTK account) are required to complete the download. Reported in `.cdd/unreleased/5/self-coherence.md §Debt` and surfaced to wave operator.

The protocol's treatment of credential-gated datasets — what counts as "publicly accessible," credential-gate examples, the unauthenticated-`curl` probe, and the operator-credential preconditions for proceeding with a licensed-permissive-but-gated candidate — is at [`protocols/existing-data-zeroth-pilot.md` §Dataset Selection Rules → Access mechanism](../../protocols/existing-data-zeroth-pilot.md#access-mechanism). The broadened wave-manifest escalation rule (escalate on EITHER non-permissive license OR access-mechanism gate) is at [`data/external/README.md` §Wave-manifest escalation rule](README.md#wave-manifest-escalation-rule-external-data). OpenCap Lab Validation falls into the second category and is the empirical case that motivated the broadening.

## Files (per SimTK project 2385 downloads page)

| File | SimTK file id | Purpose |
|---|---|---|
| `LabValidation_withoutVideos.zip` | 6688 | Mocap + force-plate + EMG + processed OpenSim outputs for 10 subjects performing 4 activities (squat, sit-to-stand, drop vertical jump, walking). Excludes video. Smaller. |
| `LabValidation_withVideos.zip` | 6689 | Full archive including RGB videos for OpenCap input. Larger. |
| `FieldStudy.zip` | 6667 | Field-study dataset (separate, not used by this cycle). |

The walking-relevant archive is `LabValidation_withoutVideos.zip` if we trust the published processed kinematics; `LabValidation_withVideos.zip` if the project wants to re-run OpenCap from raw video.

**Local private storage path:** `/opt/gait-data/opencap-lab-validation/` (outside the repo). The path is created and listed in `.gitignore` (project-wide rule: `data/external/**/*.zip`, `data/external/**/*.csv` etc. — see §Storage policy below). No data has yet been downloaded to the path.

## Data Contents Assessment (from paper)

### Population
- **Number of participants:** 10 healthy adults
- **Sex:** 6 female, 4 male
- **Age:** 27.7 ± 3.8 years (range 23–35)
- **Body mass:** 69.2 ± 11.6 kg (range 59.0–92.9)
- **Height:** 1.74 ± 0.12 m (range 1.60–1.96)

### Activities
- **Walking (relevant to this project)**
- Squat
- Sit-to-stand
- Drop vertical jump

The cycle uses only walking trials per protocol §Dataset Selection Rules and §Methodological Constraints ("Boring first").

### Walking conditions (from paper §Methods)
- **Natural walking** (no instruction beyond "walk naturally")
- **Trunk-sway modification** (instructed lateral trunk lean over stance leg)

Number of walking trial repetitions per participant is not stated in the paper; will be inventoried after acquisition.

### Reference measurements
- **Optical motion capture:** 8-camera Motion Analysis system (Motion Analysis Corp., Santa Rosa, CA, USA) tracking 31 retroreflective markers
- **Ground reaction force:** 3 in-ground force plates (Bertec Corp., Columbus, OH, USA) at 2000 Hz
- **Surface EMG:** Wireless Delsys electrodes (Delsys Corp., Natick, MA, USA) on vastus lateralis and vastus medialis, 2000 Hz
- **OpenCap-derived:** smartphone-video kinematics + OpenSim inverse kinematics + OpenSim residual reduction algorithm dynamics

### Raw Data Availability (planned, pending download)
- **Raw video:** Yes in `LabValidation_withVideos.zip`; not in `LabValidation_withoutVideos.zip`
- **Marker data:** Yes (gold-standard reference)
- **Ground reaction forces (GRF):** Yes
- **EMG data:** Yes (vastus lateralis + vastus medialis only)
- **Processed OpenSim outputs:** Yes (scaled model, IK, ID, RRA dynamics)

## Selection-Rules Check

Verified against `protocols/existing-data-zeroth-pilot.md` §"Dataset Selection Rules":

| Rule | Met? | Evidence |
|---|---|---|
| Walking trials at multiple speeds | **Partial** | Two walking *conditions* (natural + trunk-sway), not a graded speed range. Acceptable for L/R comparison + condition-response questions; speed-graded comparison is degraded. Documented in §Debt of self-coherence. |
| Both OpenCap estimates AND reference measurements | **Met** | OpenCap kinematics + 8-camera Motion Analysis mocap + 3 Bertec force plates + Delsys EMG, all per paper §Methods. |
| Clear license | **Met** | Apache 2.0, stated on the SimTK download page and on the source paper. |
| Sufficient trial repetitions for L/R comparison | **Met (provisionally)** | 10 subjects × 2 conditions × multiple repetitions per condition. Exact repetitions per condition will be confirmed at inventory after download. Conservatively ≥1 walking trial per condition per subject = ≥20 walking trials, with full L/R cycle data per trial. |

Selection decision: **OpenCap Lab Validation passes the selection rules with one partial (speed range)**. Speed-range degradation is documented as known debt and does not block the cycle — `protocols/existing-data-zeroth-pilot.md` §Backup datasets is not invoked, but it remains the explicit fallback if multi-speed analysis is required later.

## Walking Trials Identified

**Inventory pending acquisition.** From documentation alone:

- **Number of participants:** 10
- **Walking conditions:** 2 (natural, trunk-sway modification)
- **Speed variations:** Not graded — both conditions performed at self-selected speed. (See §Selection-Rules Check.)
- **Trial repetitions:** Not stated in paper. Estimated multiple repetitions per condition per subject (≥1, conservatively); to be confirmed at file inventory.
- **Gait cycle count estimate:** Lower bound: 10 subj × 2 cond × 1 trial × ~3 cycles/trial = ~60 cycles. Upper bound (typical lab protocols at 3–5 repetitions per condition): ~300–500 cycles.

A row-level inventory will be appended once the archive is downloaded.

## Processing Status

**Download status:** Blocked on operator-credentialed acquisition (SimTK account).
**Inventory status:** Documentation-derived inventory above. Row-level inventory blocked on download.
**Quality assessment:** Documentation-derived only. Per-trial quality assessment blocked on download.
**Pipeline compatibility:** Reference output structure (TRC marker files, MOT force plate files, OSIM model, IK MOT outputs) is the OpenSim-standard set documented at `instruments/opencap/outputs-to-extract.md`. Pipeline at `notebooks/existing-data-processing.ipynb` (Sub B) expects exactly this set, so format compatibility is expected.

## Storage policy

Raw archive (`*.zip`), extracted raw files (`*.trc`, `*.mot`, `*.c3d`, `*.sto`, `*.osim`, `*.mp4`, `*.avi`, per-participant directories), and any derived per-cycle feature tables containing raw participant time-series are **never committed**. The repo-level `.gitignore` covers:

- `data/external/**/*.zip`
- `data/external/**/*.trc`
- `data/external/**/*.mot`
- `data/external/**/*.c3d`
- `data/external/**/*.sto`
- `data/external/**/*.osim`
- `data/external/**/*.mp4`
- `data/external/**/*.avi`
- `data/external/**/*.csv`
- `/opt/gait-data/**` (absolute path inside the canonical local storage)

Only this manifest and small aggregate summaries (selection-rules check, anonymized counts) live in git. See `docs/ethics/data-handling.md` and `data/external/README.md`.

## Usage Notes

This dataset serves as the primary validation source for the existing-data zeroth pilot. It provides:

1. Reference standard for OpenCap processing validation (8-camera mocap is the comparison gold-standard).
2. Known-quality data for pipeline testing (Stanford NMBL processing chain is documented and reproducible).
3. Two walking *conditions* for condition-response feature questions (`analysis/features.md` §Condition-response features).
4. Reference measurements (GRF, EMG, mocap) for accuracy assessment.

## Processing Timeline

- **Download and inventory:** Week 1 of existing-data protocol — **blocked** on operator SimTK credentials at the time of this manifest.
- **Quality assessment:** Week 1–2 of existing-data protocol — pending download.
- **Gait cycle segmentation:** Week 2 of existing-data protocol — Sub B (#6).
- **Feature extraction:** Week 2–3 of existing-data protocol — Sub B (#6).

## Integration with Analysis Pipeline

This dataset will be processed according to:
- [protocols/existing-data-zeroth-pilot.md](../../protocols/existing-data-zeroth-pilot.md)
- Feature extraction as defined in [analysis/features.md](../../analysis/features.md)
- Output documentation in [reports/field-report-01-existing-data-zeroth-pilot.md](../../reports/field-report-01-existing-data-zeroth-pilot.md)

## Compliance Notes

Dataset usage follows ethics guidelines in [docs/ethics/data-handling.md](../../docs/ethics/data-handling.md) even though this is publicly available, Apache-2.0-licensed existing data. No raw participant data will be committed to this repository.

## Acquisition procedure (for the operator with credentials)

```text
1. Log in to https://simtk.org/account/login.php
2. Navigate to https://simtk.org/projects/opencap → Downloads
3. Accept Apache 2.0 use agreement
4. Download LabValidation_withoutVideos.zip (file id 6688) to /opt/gait-data/opencap-lab-validation/
5. unzip -d /opt/gait-data/opencap-lab-validation/extracted/ LabValidation_withoutVideos.zip
6. Update this manifest §Walking Trials Identified with row-level inventory
7. Mark §Acquisition status as Downloaded with SHA-256 of the archive
```

Step 7's archive SHA-256 is the lineage record that future cycles cite when this manifest is in scope.
