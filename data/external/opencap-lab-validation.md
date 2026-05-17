# OpenCap Lab Validation Dataset

## Dataset Information

**Dataset name:** OpenCap Lab Validation (Stanford NMBL)
**Source URL:** https://simtk.org/projects/opencap (SimTK project 2385)
**Source paper:** Uhlrich SD, Falisse A, Kidziński Ł, et al. "OpenCap: Human movement dynamics from smartphone videos." PLOS Computational Biology 19(10): e1011462 (2023). https://doi.org/10.1371/journal.pcbi.1011462
**Access date:** 2026-05-15 (dataset identified); **2026-05-17** (archive downloaded — see §Acquisition status)
**Data type:** Publicly documented validation dataset, Apache 2.0
**License/Terms:** Apache License 2.0 (SimTK download confirm page).
  Per Apache 2.0: free to use, modify, distribute with attribution.
  No clinical/IRB restrictions stated.

## Acquisition status

**Download status: Downloaded (2026-05-17).**

| Field | Value |
|---|---|
| Archive filename | `LabValidation_withoutVideos.zip` |
| SimTK file id | 6688 |
| Download date | 2026-05-17 |
| Local private storage path | `/opt/gait-data/opencap-lab-validation/LabValidation_withoutVideos.zip` (absolute; outside the repo) |
| Archive size | 3,029,832,907 bytes (≈ 2.82 GiB / 2,890 MB) — matches the SimTK-listed approximate size of 2889 MB |
| SHA-256 | `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187` (also persisted as `LabValidation_withoutVideos.zip.sha256` next to the archive) |
| Zip integrity | `unzip -t` reported no errors |
| Extraction status | Extracted to `/opt/gait-data/opencap-lab-validation/extracted/` (≈ 7.2 GiB, 11,141 files) |
| Top-level extracted directory | single dir `LabValidation_withoutVideos/` containing subjects `subject2` … `subject11` (10 subjects; numbering skips `subject1`) |

**Acquisition channel:** SimTK account registered and license click-through (Apache 2.0) accepted by the operator-authorized agent flow on 2026-05-17 against `https://simtk.org/frs/download_start.php/file/6688/LabValidation_withoutVideos.zip?group_id=2385`. The license click-through was the canonical Apache 2.0 boilerplate; no separate DUA or restricted-access agreement. The optional inventory file `extracted-file-inventory.txt` is kept next to the archive (outside git) per protocol §Optional inventory.

**Historical escalation (resolved):** The earlier `Download status: BLOCKED` state — driven by the SimTK login wall in front of all file downloads (the endpoint returns a JS redirect to `/account/login.php` when unauthenticated; the OpenCap public S3 bucket does not host this archive; `opencap-processing` requires an `API_TOKEN` under the same gate) — was the empirical case that motivated the broadened wave-manifest escalation rule covering access-mechanism gates as well as non-permissive licenses. That rule, and the protocol-side definition of "access mechanism," remain at [`data/external/README.md` §Wave-manifest escalation rule](README.md#wave-manifest-escalation-rule-external-data) and [`protocols/existing-data-zeroth-pilot.md` §Dataset Selection Rules → Access mechanism](../../protocols/existing-data-zeroth-pilot.md#access-mechanism); they are unchanged by this resolution. The block was cleared by operator-supplied credentials per the documented acquisition procedure.

## Files (per SimTK project 2385 downloads page)

| File | SimTK file id | Purpose |
|---|---|---|
| `LabValidation_withoutVideos.zip` | 6688 | Mocap + force-plate + EMG + processed OpenSim outputs for 10 subjects performing 4 activities (squat, sit-to-stand, drop vertical jump, walking). Excludes video. Smaller. |
| `LabValidation_withVideos.zip` | 6689 | Full archive including RGB videos for OpenCap input. Larger. |
| `FieldStudy.zip` | 6667 | Field-study dataset (separate, not used by this cycle). |

The walking-relevant archive is `LabValidation_withoutVideos.zip` if we trust the published processed kinematics; `LabValidation_withVideos.zip` if the project wants to re-run OpenCap from raw video.

**Local private storage path:** `/opt/gait-data/opencap-lab-validation/` (outside the repo). The path is listed in `.gitignore` (project-wide rule: `data/external/**/*.zip`, `data/external/**/*.csv` etc. — see §Storage policy below).

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

### Walking conditions (from paper §Methods, confirmed at inventory 2026-05-17)
- **Natural walking** (no instruction beyond "walk naturally") — 3 trials per subject (`walking1`, `walking2`, `walking3`)
- **Trunk-sway modification** (instructed lateral trunk lean over stance leg) — 3 trials per subject (`walkingTS1`, `walkingTS2`, `walkingTS3`)

Repetitions confirmed uniform across all 10 subjects: 3 natural + 3 trunk-sway = 6 walking trials per subject = **60 walking trials total**.

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

Inventoried 2026-05-17 from extracted archive at `/opt/gait-data/opencap-lab-validation/extracted/LabValidation_withoutVideos/`.

- **Number of participants:** 10 (directory names `subject2`, `subject3`, …, `subject11`; archive numbering skips `subject1`).
- **Per-subject directory layout:** `EMGData/`, `ForceData/`, `MarkerData/`, `OpenSimData/`, `sessionMetadata.yaml`, `desktop.ini`.
- **Walking conditions:** 2 (natural, trunk-sway modification).
- **Walking trials per subject:** 6 (3 natural: `walking1`, `walking2`, `walking3`; 3 trunk-sway: `walkingTS1`, `walkingTS2`, `walkingTS3`). Uniform across all 10 subjects (EMG-file count check).
- **Walking trials total:** 60.
- **Speed variations:** Not graded — both conditions performed at self-selected speed. (See §Selection-Rules Check.)
- **Gait cycle count estimate (revised after inventory):** 60 trials × ~3 cycles/trial ≈ 180 cycles lower bound; ~300–500 cycles plausible if trials run longer. Per-trial cycle count to be measured at segmentation stage (Sub B of `notebooks/existing-data-processing.ipynb`).
- **File types present per subject (subject11 sample):** `.mot` (OpenSim Motion, joint trajectories), `.sto` (OpenSim Storage, EMG/forces/IK), `.trc` (TRC marker trajectories), `.osim` (OpenSim model), `.xml`, `.npy`, `.yaml`, `.ini`. All file formats are pipeline-compatible per `instruments/opencap/outputs-to-extract.md`.
- **Total file count across archive:** 11,141 files; ≈ 7.2 GiB on disk extracted.

A row-level per-trial inventory (e.g., trial duration, marker dropouts, force-plate hits) lives in the outside-git `extracted-file-inventory.txt` alongside the archive and will be summarized in Sub B's quality assessment.

## Processing Status

**Download status:** Downloaded 2026-05-17 (see §Acquisition status for archive size, SHA-256, extraction).
**Inventory status:** Directory- and file-type-level inventory complete (see §Walking Trials Identified). Per-trial quality (e.g., marker dropouts, force-plate hits, EMG saturation) deferred to Sub B's quality assessment.
**Quality assessment:** Pending — Sub B of `notebooks/existing-data-processing.ipynb`.
**Pipeline compatibility:** Confirmed at inventory — archive contains the OpenSim-standard set (`.trc`, `.mot`, `.sto`, `.osim`) plus `.npy` and `.yaml` session metadata, matching the format set expected by `instruments/opencap/outputs-to-extract.md` and consumed by the notebook's Sub B.

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

- **Download and inventory:** Complete (2026-05-17).
- **Quality assessment:** Week 1–2 of existing-data protocol — Sub B (#6).
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
