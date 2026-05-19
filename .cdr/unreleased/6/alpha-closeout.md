# α Close-out: Sub B — Pipeline

**Cycle:** #6
**Merged:** ced1425

## Cycle summary

Goal: reproducible pipeline notebook + supporting scripts module producing segmentation, features, plots, OpenCap-vs-reference. Result: pipeline implemented, all 5 ACs met on synthetic smoke; AC4 real-data pairing is documented debt (carries forward to post-acquisition cycle); 2 review rounds; one binding β finding (pyc files); cleanly fixed.

## Findings

### F1 — Threshold-crossing vs local-minima for heel-strike detection

α first implemented local-minima detection on `-heel_y`. Smoke output: 114 cycles when expected ~64, mean cycle duration 0.6s vs 1.1s expected. Root cause: synthetic heel marker is flat-with-noise during stance, so local minima find noise peaks. Fixed by switching to falling-edge threshold detector with a refractory period. Pattern: physiology-derived signals have flat regions where local-extremum detection is unstable; threshold-crossing of a smoothed signal is more robust. Surfaces: `scripts/segmentation.py`; this is general gait-analysis knowledge but worth recording for the wave's records.

### F2 — Side-agnostic vs side-suffixed feature column names

α first wrote `extract_range` to emit side-suffixed columns (e.g. `hip_flexion_r_range_deg`). Result: ~50% missingness on the feature table because L-side cycles had NaN in R columns and vice versa. Switched to side-agnostic names (e.g. `hip_flexion_range_deg`) since the cycle's side is already in the row's `side` index column. Pattern: when a row already carries an index for a dimension, suffixing the same dimension into column names creates sparsity. Surfaces: `scripts/features.py::extract_range`.

### F3 — `__pycache__` not in `.gitignore`

β round-1 finding. α's first commit added .pyc files because `git add -A` swept them and `.gitignore` did not exclude `__pycache__/`. Pattern: standard Python repo hygiene; the existing `.gitignore` covered project-specific exclusions but not language-default ones. Surfaces: `.gitignore`.

## Friction log

- Initial heel-strike detector iteration: ~2 minutes of debugging when smoke cycle counts were off.
- Side-suffix missingness fix: ~3 minutes when missingness was 23.68% vs target <20%.
- Pyc files: 1 fix-round (β-caught).

## Engineering level reading

L6: cross-surface coherence held (notebook + scripts + requirements + ignore + summary doc all stayed aligned across the fix-round). L5 had one miss (pyc commit); L7 not pursued.

L6 with one L5 miss → cycle level L5. The next cycle should retain the cycle-iteration discipline of "checking what `git add -A` swept before committing".

## Patterns for the wave

The pyc-files-committed pattern is a generic Python-repo hygiene gap. The wave-level fix could be a pre-commit hook or a check in any future commit-quality gate. Marked as wave-level note, not a per-cycle MCA.
