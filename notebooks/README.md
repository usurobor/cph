# Notebooks

Analysis notebooks for gait-cycle data exploration.

## existing-data-processing.ipynb

Pipeline for `protocols/existing-data-zeroth-pilot.md`. Produces:

1. Gait-cycle segmentation (per-trial × side summary)
2. Feature table per `analysis/features.md` (private — written outside the repo)
3. Time-normalized joint-angle traces (hip / knee / ankle, L/R overlay)
4. Speed / condition comparisons
5. OpenCap-vs-reference comparison stats

The pipeline auto-detects whether the OpenCap Lab Validation archive is available at `<GAIT_DATA_ROOT>/opencap-lab-validation/extracted/` (default `GAIT_DATA_ROOT=/opt/gait-data/`; see `data/external/opencap-lab-validation.md` §Acquisition procedure and §Overriding the data root below). When the archive is absent, the notebook synthesizes a small smoke-test trial set to verify pipeline shape. Smoke-test output is NOT a valid empirical claim about support paths; it is a pipeline integrity check.

Helper modules live under `../scripts/`:
- `io_opencap.py` — read OpenSim .mot / .trc files; synthesize trials for smoke testing.
- `segmentation.py` — heel-strike detection and per-cycle slicing.
- `features.py` — per-cycle timing / range / coordination / asymmetry features per `../analysis/features.md`.
- `comparison.py` — OpenCap-vs-reference RMSE / Pearson r per joint.
- `build_notebook.py` — regenerate this notebook from cell strings (idempotent).

## Running

```bash
pip install -r ../requirements.txt
python3 -m nbconvert --to notebook --execute --inplace existing-data-processing.ipynb --ExecutePreprocessor.timeout=180
```

Rendered outputs (tables, plots) are committed inline so a reviewer reads the result without re-running.

## Overriding the data root

The pipeline reads its data root from the `GAIT_DATA_ROOT` environment variable, defaulting to `/opt/gait-data/` when the variable is unset or empty. The OpenCap Lab Validation archive is expected at `<GAIT_DATA_ROOT>/opencap-lab-validation/extracted/`; the persisted feature table is written to `<GAIT_DATA_ROOT>/cph-features/`. Operators running the credentialled re-run from a different filesystem layout override the path without editing source — the resolution helpers (`get_data_root`, `get_opencap_extracted_root`) live in `../scripts/io_opencap.py` so calling code that imports the module directly inherits the same override behavior, and the notebook's configuration cell reads through the same helpers. Tilde (`~`) expansion is honored for home-relative paths.

```bash
GAIT_DATA_ROOT=~/my-data/ python3 -m nbconvert --to notebook --execute --inplace existing-data-processing.ipynb
```

## Future notebooks

- clustering / dim-reduction (separate cycle, after technical validation)
- left-right comparison deep-dive (`analysis/left-right-comparison.md`)
- friend pre-pilot processing (separate protocol)
