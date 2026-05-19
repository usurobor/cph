"""Read OpenCap / OpenSim-format trial files into numpy/pandas.

The OpenCap Lab Validation archive ships processed kinematics as OpenSim
.mot / .sto plain-text files plus marker .trc files. Both formats have a
header block ending in `endheader` followed by tab- or space-separated
columns whose names are listed in a `time   col1   col2 ...` line.

This module reads those files without an opensim dependency by parsing
the plain-text headers directly.

When the actual OpenCap dataset is unavailable, `synthesize_trial()`
produces a synthetic walking trial with the same column schema so the
rest of the pipeline can be smoke-tested.
"""

from __future__ import annotations

import io
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

import numpy as np
import pandas as pd


# Documented default. The OpenCap Lab Validation archive is expected at
# `<DEFAULT_DATA_ROOT>/opencap-lab-validation/extracted/`; the persisted
# feature table is written to `<DEFAULT_DATA_ROOT>/cph-features/`.
# Operators with a different filesystem layout override via the
# `GAIT_DATA_ROOT` environment variable (see notebooks/README.md §Overriding
# the data root). Stdlib only — no python-dotenv, no config libraries.
DEFAULT_DATA_ROOT = Path("/opt/gait-data/")
GAIT_DATA_ROOT_ENV = "GAIT_DATA_ROOT"


def get_data_root() -> Path:
    """Return the data root directory.

    Resolution order:
    1. `GAIT_DATA_ROOT` environment variable (if set and non-empty).
    2. `DEFAULT_DATA_ROOT` (`/opt/gait-data/`).

    The returned path is NOT required to exist — callers downstream
    (`discover_trials`, the notebook's `USE_REAL_DATA` check) decide what
    to do when it is missing. This keeps the override mechanism orthogonal
    to the smoke-test fallback.
    """
    override = os.environ.get(GAIT_DATA_ROOT_ENV, "").strip()
    if override:
        return Path(override).expanduser()
    return DEFAULT_DATA_ROOT


def get_opencap_extracted_root() -> Path:
    """Return the expected OpenCap Lab Validation `extracted/` directory.

    Convenience wrapper for the pipeline's canonical subpath under
    `get_data_root()`.
    """
    return get_data_root() / "opencap-lab-validation" / "extracted"


@dataclass
class Trial:
    """One walking trial. Time-series rows × labelled columns.

    `df` columns include `time` plus per-quantity columns (joint angles,
    marker XYZ, or force-plate channels depending on the source file).
    `condition` is the trial-level label (e.g. `walking`, `walkingTS`)
    pulled from the file name. `subject` is the participant code.
    """

    subject: str
    trial_id: str
    condition: str
    sample_rate_hz: float
    df: pd.DataFrame
    source_path: Optional[Path] = None


def read_mot(path: Path) -> pd.DataFrame:
    """Parse an OpenSim .mot/.sto file. Returns dataframe with time + columns.

    Header format:
        <name>
        version=1
        nRows=...
        nColumns=...
        inDegrees=yes
        endheader
        time   pelvis_tilt   pelvis_list  ...
        0.000  ...           ...
    """
    raw = Path(path).read_text()
    parts = raw.split("endheader", 1)
    if len(parts) != 2:
        raise ValueError(f"no endheader in {path}")
    header, body = parts
    body = body.lstrip("\n")
    df = pd.read_csv(io.StringIO(body), sep=r"\s+", engine="python")
    return df


def read_trc(path: Path) -> pd.DataFrame:
    """Parse an OpenSim .trc marker file.

    Header format (5 lines):
        PathFileType  4  (X/Y/Z)  <filename>
        DataRate  CameraRate  NumFrames  NumMarkers  Units  OrigDataRate  OrigDataStartFrame  OrigNumFrames
        <data row 1>
        Frame#  Time  M1     M2     M3   ...
                      X1 Y1 Z1  X2 Y2 Z2  X3 Y3 Z3 ...
        <numbers>
    """
    raw = Path(path).read_text().splitlines()
    if len(raw) < 6:
        raise ValueError(f"trc too short: {path}")
    meta = raw[2].split()
    marker_names = [m for m in raw[3].split() if m and m not in ("Frame#", "Time")]
    cols: list[str] = ["Frame", "Time"]
    for m in marker_names:
        cols.extend([f"{m}_X", f"{m}_Y", f"{m}_Z"])
    body = "\n".join(raw[6:])
    df = pd.read_csv(io.StringIO(body), sep=r"\s+", engine="python",
                     header=None, names=cols)
    return df


_TRIAL_NAME_RE = re.compile(r"(?P<subject>[Ss]ubject\d+|S\d+)[_-]?(?P<trial>.+)")


def parse_trial_filename(stem: str) -> tuple[str, str, str]:
    """Infer (subject, trial_id, condition) from an OpenCap file stem.

    OpenCap Lab Validation file naming convention follows
    `Subject01/MarkerData/walking1.trc` — subject comes from the parent
    directory, trial_id and condition from the file stem.
    """
    base = stem.lower()
    if base.startswith("walking"):
        condition = "walking"
        if "ts" in base or "trunksway" in base:
            condition = "walkingTS"
        elif re.match(r"walking[a-z]?\d", base):
            condition = "walking"
        return ("UNKNOWN", stem, condition)
    return ("UNKNOWN", stem, "unknown")


def synthesize_trial(subject: str = "Synth01",
                     trial_id: str = "walking1",
                     condition: str = "walking",
                     n_cycles: int = 8,
                     fs: float = 100.0,
                     cycle_period_s: float = 1.1,
                     noise_std: float = 0.5,
                     left_right_asymmetry_deg: float = 1.5,
                     rng: Optional[np.random.Generator] = None) -> Trial:
    """Generate a synthetic walking trial for smoke-testing the pipeline.

    The synthetic trial has:
    - hip / knee / ankle flexion-extension curves with biomechanically
      plausible shape (sinusoidal approximations of normative gait waveforms),
    - left/right legs offset by 50% of cycle period,
    - small added asymmetry on left,
    - vertical marker positions for heel-strike detection,
    - small white-noise additive at `noise_std` degrees.
    """
    rng = rng or np.random.default_rng(42)
    n_samples = int(n_cycles * cycle_period_s * fs)
    t = np.arange(n_samples) / fs
    phase = (t % cycle_period_s) / cycle_period_s  # 0..1 within cycle

    def hip_curve(p: np.ndarray) -> np.ndarray:
        # peak flexion ~30° at swing (phase 0.8), peak extension ~-10° at terminal stance (phase 0.5)
        return 10.0 + 20.0 * np.sin(2 * np.pi * (p - 0.25))

    def knee_curve(p: np.ndarray) -> np.ndarray:
        # primary peak in swing (~60°), small stance peak (~15°)
        stance = 15.0 * np.exp(-((p - 0.15) / 0.08) ** 2)
        swing = 55.0 * np.exp(-((p - 0.75) / 0.10) ** 2)
        return stance + swing

    def ankle_curve(p: np.ndarray) -> np.ndarray:
        # dorsiflexion at heel-strike, plantarflexion at push-off
        return -5.0 + 15.0 * np.sin(2 * np.pi * (p - 0.55))

    def vertical_heel(p: np.ndarray) -> np.ndarray:
        # vertical heel marker: 0 during stance, rises in swing
        # heel-strike is detected at the falling edge (negative-to-positive zero crossing of velocity)
        return np.maximum(0.0, 100.0 * np.sin(np.pi * np.clip(p - 0.6, 0, 0.4) / 0.4))

    hip_r = hip_curve(phase) + rng.normal(0, noise_std, n_samples)
    knee_r = knee_curve(phase) + rng.normal(0, noise_std, n_samples)
    ankle_r = ankle_curve(phase) + rng.normal(0, noise_std, n_samples)
    heel_r_y = vertical_heel(phase) + rng.normal(0, noise_std, n_samples)

    phase_l = (phase + 0.5) % 1.0
    hip_l = hip_curve(phase_l) + left_right_asymmetry_deg + rng.normal(0, noise_std, n_samples)
    knee_l = knee_curve(phase_l) + rng.normal(0, noise_std, n_samples)
    ankle_l = ankle_curve(phase_l) + rng.normal(0, noise_std, n_samples)
    heel_l_y = vertical_heel(phase_l) + rng.normal(0, noise_std, n_samples)

    df = pd.DataFrame({
        "time": t,
        "hip_flexion_r": hip_r,
        "knee_angle_r": knee_r,
        "ankle_angle_r": ankle_r,
        "hip_flexion_l": hip_l,
        "knee_angle_l": knee_l,
        "ankle_angle_l": ankle_l,
        "RHEE_Y": heel_r_y,
        "LHEE_Y": heel_l_y,
        "pelvis_tilt": 5.0 + 3.0 * np.sin(2 * np.pi * 2 * t / cycle_period_s) + rng.normal(0, noise_std/2, n_samples),
        "pelvis_list": 2.0 * np.sin(2 * np.pi * t / cycle_period_s) + rng.normal(0, noise_std/2, n_samples),
        "pelvis_rotation": 4.0 * np.sin(2 * np.pi * t / cycle_period_s) + rng.normal(0, noise_std/2, n_samples),
    })
    return Trial(subject=subject, trial_id=trial_id, condition=condition,
                 sample_rate_hz=fs, df=df, source_path=None)


def discover_trials(root: Path,
                    pattern: str = "*.mot",
                    walking_only: bool = True) -> list[Path]:
    """Walk `root` for trial files matching `pattern`.

    Generic recursive-glob discovery. For the typed OpenCap Lab Validation
    layout — `subject<NN>/OpenSimData/Mocap/IK/<trial>.mot` paired with
    `subject<NN>/MarkerData/Mocap/<trial>.trc`, plus per-backbone Video
    variants under `OpenSimData/Video/<backbone>/<N>-cameras/IK/<trial>.mot`
    — use `discover_walking_ik` / `load_paired_trial` instead; this function
    is the lower-level primitive they build on.
    """
    root = Path(root)
    if not root.exists():
        return []
    found = sorted(root.rglob(pattern))
    if walking_only:
        found = [p for p in found if "walk" in p.stem.lower()]
    return found


# Subpaths under each `subject<NN>/OpenSimData/` for the four IK sources
# shipped in the LabValidation archive. Mocap is the lab gold-standard
# (8-camera Motion Analysis → marker IK); the three Video sources are the
# OpenCap pipeline run with different pose-estimation backbones at the
# 5-camera setup that the Uhlrich et al. 2023 paper headlines.
IK_SOURCES = {
    "Mocap": "Mocap/IK",
    "HRNet_5cam": "Video/HRNet/5-cameras/IK",
    "OpenPose_default_5cam": "Video/OpenPose_default/5-cameras/IK",
    "OpenPose_highAccuracy_5cam": "Video/OpenPose_highAccuracy/5-cameras/IK",
}


def discover_walking_ik(extracted_root: Path,
                        ik_source: str = "Mocap") -> list[Path]:
    """List walking IK .mot paths across all subjects for one IK source.

    Layout under `extracted_root` is assumed to be
    `LabValidation_withoutVideos/subject<NN>/OpenSimData/<IK_SOURCES[ik_source]>/<trial>.mot`.
    Only files whose stem starts with `walking` (case-insensitive) are
    returned; ancillary `*_setup_ik.xml` and `*_ik_marker_errors.sto` are
    excluded by extension.
    """
    if ik_source not in IK_SOURCES:
        raise ValueError(f"ik_source must be one of {list(IK_SOURCES)}; got {ik_source!r}")
    extracted_root = Path(extracted_root)
    if not extracted_root.exists():
        return []
    # The archive nests one extra dir below `extracted/` — try both shapes
    # so callers can pass either `…/extracted/` or `…/extracted/LabValidation_withoutVideos/`.
    candidate_bases: list[Path] = [extracted_root]
    nested = extracted_root / "LabValidation_withoutVideos"
    if nested.is_dir():
        candidate_bases.append(nested)
    paths: list[Path] = []
    sub_re = re.compile(r"^subject\d+$", re.IGNORECASE)
    for base in candidate_bases:
        for sub in sorted(base.iterdir(), key=lambda p: p.name):
            if not (sub.is_dir() and sub_re.match(sub.name)):
                continue
            ik_dir = sub / "OpenSimData" / IK_SOURCES[ik_source]
            if not ik_dir.is_dir():
                continue
            for p in sorted(ik_dir.glob("*.mot")):
                if p.stem.lower().startswith("walking"):
                    paths.append(p)
        if paths:
            break  # only one candidate base actually holds the archive
    return paths


def subject_dir_for(ik_path: Path) -> Path:
    """Return the `subject<NN>` directory above an IK or marker file path."""
    for parent in ik_path.parents:
        if re.match(r"^subject\d+$", parent.name, re.IGNORECASE):
            return parent
    raise ValueError(f"no subject<NN> dir above {ik_path}")


# Marker-name remap from the LabValidation .trc files to the column
# convention the segmentation pipeline expects (RHEE_Y / LHEE_Y for the
# vertical heel-marker channel; r_calc / L_calc are the calcaneus markers
# in the Mocap .trc).
_TRC_HEEL_COLS = {
    "r_calc_Y": "RHEE_Y",
    "L_calc_Y": "LHEE_Y",
}


def load_paired_trial(ik_path: Path,
                      ik_source: str = "Mocap",
                      trc_dir: str = "MarkerData/Mocap") -> Trial:
    """Load one trial from a Mocap or Video IK .mot file paired with the
    Mocap marker .trc, merging joint-angle columns and heel-marker columns
    into a single per-row DataFrame.

    The .mot file supplies joint-angle / pelvis coordinates; the .trc file
    supplies the vertical heel-marker channel that `scripts.segmentation`
    uses for heel-strike detection. The .trc is always read from the
    Mocap marker source — heel-strike timing comes from the gold-standard
    markers regardless of which IK source is being analysed.

    Both files are expected at the same sample rate and trial duration;
    they are joined positionally on row index (no resampling). If row
    counts mismatch, the shorter length is used and the trimmed count is
    reflected in the returned DataFrame.
    """
    ik_path = Path(ik_path)
    subject_dir = subject_dir_for(ik_path)
    subject = subject_dir.name
    trial_stem = ik_path.stem  # e.g. "walking4"
    _, _, condition = parse_trial_filename(trial_stem)

    df_ik = read_mot(ik_path)
    trc_path = subject_dir / trc_dir / f"{trial_stem}.trc"
    if trc_path.exists():
        df_trc = read_trc(trc_path)
        # Bring heel-marker columns onto the IK row grid by positional trim.
        n = min(len(df_ik), len(df_trc))
        for src_col, dst_col in _TRC_HEEL_COLS.items():
            if src_col in df_trc.columns:
                df_ik = df_ik.iloc[:n].reset_index(drop=True)
                df_trc_n = df_trc.iloc[:n].reset_index(drop=True)
                df_ik[dst_col] = df_trc_n[src_col].to_numpy()
    # Sample rate from the merged frame; fall back gracefully if `time`
    # is monotonic-but-non-uniform.
    if "time" in df_ik.columns and len(df_ik) > 1:
        dt = float(np.median(np.diff(df_ik["time"].to_numpy())))
        fs = 1.0 / dt if dt > 0 else 100.0
    else:
        fs = 100.0
    return Trial(subject=subject, trial_id=trial_stem, condition=condition,
                 sample_rate_hz=fs, df=df_ik, source_path=ik_path)


def load_all_walking_trials(extracted_root: Path,
                            ik_source: str = "Mocap") -> list[Trial]:
    """Convenience: discover + load all walking trials for one IK source."""
    return [load_paired_trial(p, ik_source=ik_source)
            for p in discover_walking_ik(extracted_root, ik_source=ik_source)]
