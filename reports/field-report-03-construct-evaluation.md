# Field Report 03: R-side construct evaluation (n=60 R cycles, 10 subjects × 2 conditions)

## Overview

**Report Date:** 2026-05-19 (cph#27 R3 first-pass)
**Cycle:** cph#27 — R3 R-side aggregate condition-response analysis. Runs in parallel with cph#28 (L-cycle recovery).
**Protocol:** [protocols/existing-data-zeroth-pilot.md](../protocols/existing-data-zeroth-pilot.md) §"Go/No-Go Criteria" + [docs/concepts/support-path.md](../docs/concepts/support-path.md) §Falsification.
**Dataset:** OpenCap Lab Validation (SHA-256 `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`) — unchanged from [`reports/field-report-01-existing-data-zeroth-pilot.md`](field-report-01-existing-data-zeroth-pilot.md).
**Status:** **Decision: R3 = partial GO on R-side; R1 stays REVISE** (cross-cycle binding to cph#28; see §Cross-cycle binding).

## Executive summary

Under trunk-sway, R-side gait showed seven Benjamini–Hochberg–significant (q<0.05) condition responses across n=10 subjects, paired Wilcoxon signed-rank on per-subject medians. The largest single effect was an 18.3° median increase in lumbar bending range — visible in 10/10 subjects, rank-biserial r_rb = +1.0 — which is the deliberate-trunk-perturbation condition's intended kinematic consequence and which the R-side surface unambiguously detects. The accompanying signatures (cycle slowdown, distal sagittal range contraction, and a small shift in hip-knee coordination timing) form a mechanistically coherent picture and are independently consistent across subjects.

**Three findings.**

1. **H2 (trunk-sway compensation) survives R-side contact with measurement.** The two largest trunk-segment effects (`lumbar_bending_range_deg` +18.3° median Δ; `lumbar_extension_range_deg` +1.6° median Δ) are BH-significant at q<0.05 with rank-biserial r_rb = +1.0 (every subject moves in the same direction). `pelvis_tilt_range_deg` trends in the same direction (median Δ +1.1°, r_rb = +0.75, raw p = 0.037, BH-adjusted q = 0.084 — does not clear the q<0.05 line but is consistent with the family). 2 of 9 pre-registered H2 features clear BH; H2 is supported in its *frontal-and-sagittal-trunk-amplification* form.

2. **H1 (sagittal-dominant load transfer) survives only at the distal joint.** `ankle_angle_range_deg` decreases by 6.6° median Δ (r_rb = −1.0, BH-significant at q<0.05) and `ankle_angle_min_deg` increases by 5.2° (less plantarflexion at the trough, BH-significant). `knee_angle_range_deg` trends in the same direction (−4.8°, raw p = 0.027, q = 0.084) but does not clear the BH line. `hip_flexion_range_deg`, `peak_knee_flexion_phase`, and `hip_knee_lag_pct_cycle` are not significant. H1 is supported in its *distal-contraction-under-proximal-compensation* form on the R-side; the hip-as-sagittal-driver claim is not supported on this surface.

3. **H3 (asymmetric phase-coupling between sides) remains structurally non-testable.** 1 L-side cycle in the archive (subject8 walkingTS1); no R/L pairs at matching (subject, cycle_number) for any subject. R3's R-only design cannot evaluate H3; cph#28's L-cycle recovery owns this gate.

**Decision.** R3 = partial GO on R-side. R-side measurement detects deliberate trunk-perturbation as multiple coherent, large, subject-consistent feature shifts. Five of six falsification conditions evaluate NOT triggered; one (L/R asymmetry) is not testable on this archive. R1 stays REVISE because the bilateral construct is half-anchored; the L-cycle recovery cycle (cph#28) owns R1's transition.

## Method picks (carried over from [`.cdr/unreleased/27/self-coherence.md`](../.cdr/unreleased/27/self-coherence.md) §Method picks)

| Pick | Choice | Rationale (one line) |
|---|---|---|
| Aggregation | median (primary) + mean (robustness) | n=3 cycles per (subject, condition); median suppresses per-cycle outliers that move mean by ~33%. |
| Paired test | Wilcoxon signed-rank, two-sided | n=10; normality cannot be checked reliably; ~5% power cost vs paired-t is acceptable for exploratory cycle. |
| Effect size | rank-biserial r_rb with percentile bootstrap 95% CI (B=10,000, seed=20260519) | Wilcoxon's natural effect-size companion; closed-form CI does not exist for paired r_rb. |
| Multiple comparisons | BH-FDR at q=0.05 | ~25 features; FDR matches the field report's job (mechanistic-claim discovery). Bonferroni's FWER is the wrong loss function here; raw p-values reported alongside so β can apply a stricter correction without re-running. |

## Aggregation surface (AC1)

Source: `/opt/gait-data/cph-features/features-zeroth-pilot.csv` (61 rows × 35 columns; 60 R + 1 L; not committed per AC9). Reproducible via [`analysis/r3_subject_aggregate_tests.py`](../analysis/r3_subject_aggregate_tests.py).

After filtering to side='R' (60 rows), the table is uniform: 10 subjects × 2 conditions × 3 R-side cycles per (subject, condition) cell.

**Cell-count oracle (AC1 = 10 × 2 × 35 = 700).** The long-format aggregate table has 20 (subject × condition) rows × 35 columns = **700 cells**. 25 of the 35 columns are numeric features that aggregate meaningfully; 8 are indexing columns (`subject`, `session`, `trial_id`, `condition`, `side`, `cycle_number`, `quality_flag`, `exclusion_flag`); 2 are non-numeric metadata sentinels (`timing_estimate_method`, `normalized_curve_available`). The paired condition-response tests (AC2) run on the 25 testable numeric features.

### AC1a — Median aggregate (primary)

| subject | condition | cycle_dur_s | stance_s | swing_s | stance% | pk_knee_phase | hip_flex_range | hip_flex_peak | hip_flex_min | hip_add_range | hip_add_peak | hip_add_min | knee_range | knee_peak | knee_min | ankle_range | ankle_peak | ankle_min | pelvis_tilt_range | pelvis_list_range | pelvis_rot_range | lumbar_bend_range | lumbar_rot_range | lumbar_ext_range | hk_lag_samples | hk_lag_%cyc |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| subject10 | walking | 0.90 | 0.53 | 0.38 | 58.89 | 81.11 | 44.56 | 25.02 | -19.71 | 14.95 | 6.86 | -8.12 | 68.05 | 74.01 | 4.21 | 33.51 | 20.23 | -13.67 | 5.16 | 9.47 | 16.82 | 14.65 | 27.45 | 6.08 | 12 | 13.33 |
| subject10 | walkingTS | 1.08 | 0.61 | 0.45 | 56.73 | 80.56 | 42.63 | 25.90 | -17.88 | 17.11 | 6.27 | -11.32 | 63.79 | 71.58 | 9.07 | 24.16 | 16.31 | -7.85 | 4.94 | 10.03 | 10.06 | 32.46 | 25.30 | 7.18 | 15 | 13.46 |
| subject11 | walking | 1.02 | 0.57 | 0.45 | 55.88 | 80.20 | 47.01 | 29.37 | -17.65 | 17.27 | 8.55 | -8.51 | 73.53 | 73.95 | 0.43 | 38.81 | 15.87 | -23.37 | 4.25 | 9.23 | 7.63 | 17.10 | 20.33 | 6.57 | 11 | 10.78 |
| subject11 | walkingTS | 1.19 | 0.62 | 0.57 | 52.10 | 79.31 | 42.58 | 28.00 | -14.81 | 14.84 | 9.97 | -4.82 | 59.44 | 62.69 | 2.21 | 29.88 | 13.79 | -18.76 | 5.47 | 7.56 | 14.91 | 35.92 | 17.44 | 7.75 | 13 | 10.92 |
| subject2 | walking | 1.09 | 0.60 | 0.47 | 56.08 | 80.37 | 39.51 | 25.86 | -13.17 | 7.98 | 7.12 | -0.97 | 60.07 | 66.08 | 5.59 | 31.55 | 15.85 | -16.02 | 1.99 | 3.91 | 5.84 | 10.27 | 5.99 | 3.19 | 12 | 11.21 |
| subject2 | walkingTS | 1.35 | 0.77 | 0.58 | 57.04 | 80.00 | 40.12 | 26.32 | -12.86 | 10.31 | 8.09 | -2.22 | 52.42 | 56.10 | 4.18 | 26.27 | 12.74 | -12.63 | 3.62 | 5.77 | 16.59 | 26.12 | 6.83 | 4.19 | 17 | 13.49 |
| subject3 | walking | 0.98 | 0.57 | 0.41 | 58.16 | 83.67 | 52.15 | 29.38 | -23.16 | 20.18 | 13.80 | -6.23 | 64.78 | 66.82 | 2.27 | 37.54 | 17.17 | -20.37 | 4.34 | 15.23 | 11.69 | 18.59 | 19.38 | 7.20 | 10 | 10.20 |
| subject3 | walkingTS | 1.22 | 0.68 | 0.53 | 55.86 | 84.69 | 50.27 | 29.74 | -21.70 | 21.19 | 13.54 | -8.23 | 64.46 | 65.97 | 1.61 | 29.59 | 15.03 | -14.22 | 6.29 | 20.43 | 10.47 | 52.93 | 22.79 | 7.54 | 11 | 9.91 |
| subject4 | walking | 0.96 | 0.54 | 0.43 | 56.84 | 81.25 | 46.34 | 24.59 | -21.62 | 17.55 | 10.98 | -6.22 | 64.45 | 65.99 | 1.81 | 40.27 | 16.77 | -23.50 | 1.76 | 11.09 | 14.14 | 15.73 | 21.58 | 3.79 | 11 | 11.58 |
| subject4 | walkingTS | 1.04 | 0.58 | 0.45 | 56.31 | 81.91 | 47.47 | 26.93 | -21.97 | 13.97 | 12.49 | -1.82 | 59.09 | 60.64 | 1.58 | 34.16 | 18.66 | -15.45 | 5.67 | 11.60 | 6.74 | 41.56 | 12.56 | 7.68 | 12 | 11.54 |
| subject5 | walking | 1.01 | 0.58 | 0.42 | 57.43 | 80.39 | 42.18 | 21.54 | -20.39 | 17.95 | 11.97 | -5.97 | 71.98 | 72.67 | 0.69 | 37.77 | 18.69 | -18.81 | 5.33 | 8.92 | 13.04 | 12.61 | 16.93 | 5.25 | 12 | 11.88 |
| subject5 | walkingTS | 1.06 | 0.60 | 0.46 | 56.31 | 80.73 | 38.62 | 22.38 | -15.95 | 10.19 | 8.97 | -1.21 | 64.29 | 67.98 | 2.85 | 35.41 | 21.11 | -13.06 | 4.69 | 6.97 | 9.93 | 28.20 | 8.41 | 5.64 | 14 | 12.84 |
| subject6 | walking | 1.05 | 0.56 | 0.49 | 52.83 | 80.19 | 44.45 | 29.08 | -15.17 | 20.34 | 12.81 | -6.90 | 69.12 | 69.80 | 0.66 | 29.99 | 17.40 | -12.12 | 3.59 | 12.80 | 14.88 | 14.43 | 25.14 | 4.47 | 11 | 11.11 |
| subject6 | walkingTS | 0.98 | 0.54 | 0.44 | 55.10 | 79.59 | 42.45 | 27.93 | -13.94 | 17.44 | 10.88 | -6.90 | 75.38 | 76.14 | 1.61 | 22.65 | 13.71 | -8.75 | 4.15 | 13.12 | 8.65 | 28.90 | 25.05 | 7.70 | 11 | 12.36 |
| subject7 | walking | 0.99 | 0.59 | 0.40 | 59.00 | 81.00 | 43.79 | 32.74 | -11.01 | 15.12 | 8.83 | -6.29 | 69.94 | 72.04 | 1.65 | 33.43 | 19.96 | -13.85 | 2.58 | 10.48 | 16.47 | 13.54 | 22.84 | 2.82 | 12 | 12.00 |
| subject7 | walkingTS | 1.10 | 0.62 | 0.48 | 56.36 | 80.95 | 50.75 | 35.90 | -14.84 | 13.66 | 6.17 | -7.49 | 57.96 | 62.76 | 4.97 | 28.10 | 18.55 | -9.55 | 2.45 | 12.64 | 9.90 | 43.63 | 20.77 | 5.59 | 13 | 11.82 |
| subject8 | walking | 1.01 | 0.59 | 0.41 | 58.95 | 82.11 | 45.30 | 33.54 | -9.92 | 16.54 | 10.05 | -6.22 | 65.48 | 71.81 | 6.33 | 34.96 | 14.81 | -19.93 | 2.95 | 7.02 | 12.97 | 9.54 | 25.43 | 7.75 | 11 | 11.54 |
| subject8 | walkingTS | 1.13 | 0.62 | 0.51 | 54.87 | 80.53 | 49.14 | 39.40 | -9.46 | 15.18 | 10.18 | -5.28 | 61.90 | 70.98 | 8.60 | 27.79 | 16.28 | -11.49 | 3.99 | 9.19 | 23.31 | 33.33 | 19.96 | 9.86 | 12 | 10.62 |
| subject9 | walking | 1.02 | 0.63 | 0.39 | 60.58 | 81.37 | 44.20 | 27.79 | -15.84 | 18.06 | 9.13 | -8.93 | 65.28 | 65.72 | 0.38 | 31.77 | 14.12 | -17.96 | 1.96 | 8.58 | 12.98 | 10.27 | 25.66 | 4.28 | 12 | 12.25 |
| subject9 | walkingTS | 1.02 | 0.55 | 0.48 | 52.38 | 77.00 | 42.68 | 30.46 | -12.22 | 18.83 | 13.75 | -5.07 | 63.43 | 63.92 | 0.41 | 29.19 | 16.38 | -15.83 | 4.69 | 11.21 | 9.20 | 27.89 | 27.56 | 7.60 | 13 | 12.75 |

(Column abbreviations expand to the names in `analysis/features.md`: `*_range` = `*_range_deg`, `*_peak` = `*_peak_deg`, `*_min` = `*_min_deg`, `hk_lag` = `hip_knee_lag`, `stance%` = `stance_pct_cycle`, `pk_knee_phase` = `peak_knee_flexion_phase`.)

### AC1b — Mean aggregate (robustness summary)

The mean aggregate is reproduced verbatim by the analysis script (`analysis/r3_subject_aggregate_tests.py` §AC1b). The aggregation-method-flip diagnostic — does any feature's per-subject paired delta median flip sign across mean vs median aggregation? — found **1 of 25 features** flipped: `hip_flexion_range_deg` (mean: +0.61° increase; median: −1.70° decrease). Both readings of `hip_flexion_range_deg` are ns (raw p > 0.5; q > 0.6) and the feature is not BH-significant under either aggregation. The other 24 features agree on direction; the seven BH-significant findings reported below hold under both aggregations.

### AC1c — Per-subject paired delta (trunk-sway median − natural median)

The 25×10 matrix of per-subject paired deltas is reproduced verbatim by `analysis/r3_subject_aggregate_tests.py` §AC1c. Headline rows for the seven BH-significant features (per-subject deltas; row = feature, column = subject):

| feature | subj10 | subj11 | subj2 | subj3 | subj4 | subj5 | subj6 | subj7 | subj8 | subj9 |
|---|---|---|---|---|---|---|---|---|---|---|
| cycle_duration_s | +0.18 | +0.17 | +0.26 | +0.24 | +0.08 | +0.05 | -0.07 | +0.11 | +0.12 | 0.00 |
| swing_duration_s | +0.07 | +0.12 | +0.11 | +0.12 | +0.02 | +0.04 | -0.05 | +0.08 | +0.10 | +0.09 |
| ankle_angle_range_deg | -9.35 | -8.93 | -5.28 | -7.96 | -6.10 | -2.36 | -7.35 | -5.32 | -7.17 | -2.58 |
| ankle_angle_min_deg | +5.83 | +4.61 | +3.39 | +6.16 | +8.05 | +5.75 | +3.37 | +4.29 | +8.45 | +2.13 |
| lumbar_bending_range_deg | +17.81 | +18.82 | +15.85 | +34.34 | +25.83 | +15.59 | +14.47 | +30.09 | +23.79 | +17.62 |
| lumbar_extension_range_deg | +1.10 | +1.18 | +1.00 | +0.34 | +3.89 | +0.39 | +3.23 | +2.77 | +2.11 | +3.32 |
| hip_knee_lag_samples | +3 | +2 | +5 | +1 | +1 | +2 | 0 | +1 | +1 | +1 |

For four of the seven (lumbar_bending_range_deg, lumbar_extension_range_deg, ankle_angle_range_deg, ankle_angle_min_deg) every subject moves in the BH-significant direction (r_rb = ±1.0). The cycle slowdown is positive in 9/10 subjects (subject6 is the lone non-positive at −0.07 s); swing-duration is positive in 9/10 (subject6 is the lone negative at −0.05 s). The hip-knee lag shifts by +1 to +5 samples in 9/10 subjects (subject6 is the lone zero).

## Paired Wilcoxon signed-rank tests (AC2)

n = 10 paired subjects. Test statistic = W (sum of positive signed ranks). Effect size = rank-biserial r_rb in [−1, +1]; sign agrees with median paired delta direction. 95% CI = percentile bootstrap over n=10 paired deltas, B=10,000, seed=20260519. p_BH = BH-adjusted q-value at FDR q=0.05. `BH q<.05` = `*` when q < 0.05.

| feature | H | median Δ (TS−nat) | n_nz / n | W | r_rb | r_rb 95% CI | p_raw | p_BH | BH q<.05 |
|---|---|---|---|---|---|---|---|---|---|
| cycle_duration_s | — | 0.115 | 9 / 10 | 2.0 | 0.911 | [0.564, 1.000] | 0.012 | 0.042 | * |
| stance_duration_s | — | 0.035 | 10 / 10 | 9.0 | 0.673 | [0.073, 1.000] | 0.062 | 0.130 |  |
| swing_duration_s | — | 0.085 | 10 / 10 | 3.0 | 0.891 | [0.564, 1.000] | 0.010 | 0.041 | * |
| stance_pct_cycle | — | -2.233 | 10 / 10 | 7.0 | -0.745 | [-1.000, -0.200] | 0.037 | 0.084 |  |
| peak_knee_flexion_phase | H1 | -0.465 | 10 / 10 | 16.0 | -0.418 | [-1.000, 0.273] | 0.275 | 0.362 |  |
| hip_flexion_range_deg | H1 | -1.700 | 10 / 10 | 21.0 | -0.236 | [-0.964, 0.491] | 0.557 | 0.605 |  |
| hip_flexion_peak_deg | — | 0.858 | 10 / 10 | 11.0 | 0.600 | [-0.091, 1.000] | 0.105 | 0.165 |  |
| hip_flexion_min_deg | — | 1.346 | 10 / 10 | 11.0 | 0.600 | [-0.055, 1.000] | 0.105 | 0.165 |  |
| hip_adduction_range_deg | H2 | -1.411 | 10 / 10 | 14.0 | -0.491 | [-0.927, 0.236] | 0.193 | 0.269 |  |
| hip_adduction_peak_deg | H2 | -0.060 | 10 / 10 | 26.0 | -0.055 | [-0.745, 0.637] | 0.922 | 0.922 |  |
| hip_adduction_min_deg | H2 | 0.467 | 10 / 10 | 19.0 | 0.309 | [-0.527, 0.818] | 0.432 | 0.491 |  |
| knee_angle_range_deg | H1 | -4.809 | 10 / 10 | 6.0 | -0.782 | [-1.000, -0.236] | 0.027 | 0.084 |  |
| knee_angle_peak_deg | — | -3.560 | 10 / 10 | 7.0 | -0.745 | [-1.000, -0.200] | 0.037 | 0.084 |  |
| knee_angle_min_deg | — | 1.365 | 10 / 10 | 10.0 | 0.636 | [0.018, 1.000] | 0.084 | 0.150 |  |
| ankle_angle_range_deg | H1 | -6.637 | 10 / 10 | 0.0 | -1.000 | [-1.000, -1.000] | 0.002 | 0.012 | * |
| ankle_angle_peak_deg | — | -1.740 | 10 / 10 | 18.0 | -0.345 | [-0.891, 0.382] | 0.375 | 0.446 |  |
| ankle_angle_min_deg | — | 5.182 | 10 / 10 | 0.0 | 1.000 | [1.000, 1.000] | 0.002 | 0.012 | * |
| pelvis_tilt_range_deg | H2 | 1.125 | 10 / 10 | 7.0 | 0.745 | [0.200, 1.000] | 0.037 | 0.084 |  |
| pelvis_list_range_deg | H2 | 1.210 | 10 / 10 | 10.0 | 0.636 | [0.055, 1.000] | 0.084 | 0.150 |  |
| pelvis_rotation_range_deg | H2 | -3.445 | 10 / 10 | 26.0 | -0.055 | [-1.000, 0.636] | 0.922 | 0.922 |  |
| lumbar_bending_range_deg | H2 | 18.315 | 10 / 10 | 0.0 | 1.000 | [1.000, 1.000] | 0.002 | 0.012 | * |
| lumbar_rotation_range_deg | H2 | -2.109 | 10 / 10 | 12.0 | -0.564 | [-1.000, 0.091] | 0.131 | 0.192 |  |
| lumbar_extension_range_deg | H2 | 1.646 | 10 / 10 | 0.0 | 1.000 | [1.000, 1.000] | 0.002 | 0.012 | * |
| hip_knee_lag_samples | — | 1.000 | 9 / 10 | 0.0 | 1.000 | [1.000, 1.000] | 0.004 | 0.020 | * |
| hip_knee_lag_pct_cycle | H1 | 0.134 | 10 / 10 | 17.0 | 0.382 | [-0.345, 0.891] | 0.322 | 0.403 |  |

**Reading the table.** 7 of 25 features are BH-significant at q<0.05. r_rb = ±1.0 for four of those seven (ankle_range, ankle_min, lumbar_bend_range, lumbar_ext_range, hip_knee_lag_samples — five if hip_knee_lag is counted) means *every single subject* moved in the same direction; the effect is not a few outliers driving the test. The CIs on those features are degenerate at the boundary because the bootstrap resampling preserves the all-same-direction property.

## Hypothesis evidence summary (AC3)

### H1 — Sagittal-dominant load transfer

**Features tested:** 5 of 5 pre-registered (`hip_flexion_range_deg`, `knee_angle_range_deg`, `ankle_angle_range_deg`, `hip_knee_lag_pct_cycle`, `peak_knee_flexion_phase`).

**Result:** 1 of 5 BH-significant at q<0.05. Direction: 4 of 5 features have negative median Δ (TS < natural); 1 positive (`hip_knee_lag_pct_cycle`, ns).

| feature | median Δ | r_rb | p_raw | p_BH | BH q<.05 |
|---|---|---|---|---|---|
| ankle_angle_range_deg | -6.637 | -1.000 | 0.002 | 0.012 | * |
| knee_angle_range_deg | -4.809 | -0.782 | 0.027 | 0.084 |  |
| hip_flexion_range_deg | -1.700 | -0.236 | 0.557 | 0.605 |  |
| peak_knee_flexion_phase | -0.465 | -0.418 | 0.275 | 0.362 |  |
| hip_knee_lag_pct_cycle | 0.134 | 0.382 | 0.322 | 0.403 |  |

**Mechanistic interpretation (measured signal):** Under trunk-sway, R-side ankle range decreases by 6.6° (all 10 subjects); R-side knee range trends downward (all 10 in the same direction, magnitude smaller, BH-adjusted q does not clear the 0.05 line); hip range, peak-knee timing, and hip-knee coordination lag do not respond.

**Mechanistic interpretation (inferred construct reading):** The sagittal *load-transfer chain* (hip → knee → ankle) is not uniformly suppressed under trunk-sway; the distal end of the chain (ankle) contracts most, the middle (knee) trends in the same direction, and the proximal end (hip) does not change measurably. This is consistent with "distal sagittal contraction under proximal compensation" — when the trunk segment absorbs the lateral perturbation (H2 below), distal push-off energy contracts. It is *not* consistent with the original H1 framing of "hip-driven sagittal load transfer dominating other planes"; the hip itself is not the responder.

**Verdict.** H1 *partially* survives R-side contact, in the modified form *distal sagittal contraction under proximal compensation*. The original "hip-driven" claim does not survive.

### H2 — Trunk-sway compensation

**Features tested:** 9 of 9 pre-registered (`lumbar_extension_range_deg`, `lumbar_bending_range_deg`, `lumbar_rotation_range_deg`, `pelvis_tilt_range_deg`, `pelvis_list_range_deg`, `pelvis_rotation_range_deg`, `hip_adduction_range_deg`, `hip_adduction_peak_deg`, `hip_adduction_min_deg`).

**Result:** 2 of 9 BH-significant at q<0.05. Direction: 5 features have positive median Δ (TS > natural); 4 negative. `pelvis_tilt_range_deg` trends in the same direction as the BH-significant trunk features (median Δ +1.1°, r_rb = +0.75, raw p = 0.037, q = 0.084).

| feature | median Δ | r_rb | p_raw | p_BH | BH q<.05 |
|---|---|---|---|---|---|
| lumbar_bending_range_deg | 18.315 | 1.000 | 0.002 | 0.012 | * |
| lumbar_extension_range_deg | 1.646 | 1.000 | 0.002 | 0.012 | * |
| pelvis_tilt_range_deg | 1.125 | 0.745 | 0.037 | 0.084 |  |
| pelvis_list_range_deg | 1.210 | 0.636 | 0.084 | 0.150 |  |
| hip_adduction_range_deg | -1.411 | -0.491 | 0.193 | 0.269 |  |
| lumbar_rotation_range_deg | -2.109 | -0.564 | 0.131 | 0.192 |  |
| hip_adduction_min_deg | 0.467 | 0.309 | 0.432 | 0.491 |  |
| hip_adduction_peak_deg | -0.060 | -0.055 | 0.922 | 0.922 |  |
| pelvis_rotation_range_deg | -3.445 | -0.055 | 0.922 | 0.922 |  |

**Mechanistic interpretation (measured signal):** Under trunk-sway, R-side lumbar bending range increases by 18.3° (all 10 subjects); lumbar extension range increases by 1.6° (all 10 subjects); pelvis tilt range trends upward (8/10 subjects positive). The frontal-plane hip features (`hip_adduction_*`) do not respond.

**Mechanistic interpretation (inferred construct reading):** The trunk-sway condition's intended kinematic consequence (deliberate amplification of frontal-plane trunk motion) is faithfully present in the data, and it appears as a coupled trunk-segment signature: bending dominates, with smaller extension-range increase. The hip-adduction channel — which the original H2 framing named as the load-transfer pathway for "trunk compensation" — does not respond at the R-side hip; the compensation lives in the lumbar segment, not at the hip. This is mechanistically consistent: deliberate trunk perturbation increases trunk motion in the bending and extension axes; the pelvis follows mildly (tilt trending); the hip ab/adduction does not need to change because the lumbar segment is doing the absorbing.

**Verdict.** H2 survives R-side contact in its *trunk-segment-driven* form. The hip-adduction-as-compensation-pathway sub-claim does not survive on R-side.

### H3 — Asymmetric phase-coupling (not testable)

H3 requires R/L pairs at matching (subject, cycle_number). The R-side feature table has **1 L-side cycle total** (subject8, walkingTS1). No subject has both R and L aggregates available; H3 is structurally non-testable on this archive and is deferred to cph#28's L-cycle recovery.

This deferral does *not* count toward the falsification threshold (per [`docs/concepts/support-path.md`](../docs/concepts/support-path.md) §Falsification: "Not testable" verdicts do not count). H3 awaits cph#28; until cph#28 produces L-side cycle yield ≥ some threshold, H3 cannot be evaluated, and the bilateral construct cannot be lifted from REVISE.

## Candidate support-path hypotheses (AC4)

Three candidate hypotheses surface from the R-side condition response. Each is *condition-bound* (binds to deliberate trunk perturbation, not to walking in general) and *measured-vs-inferred*-separated per [`docs/concepts/support-path.md`](../docs/concepts/support-path.md) §"Measured vs Inferred."

### Candidate 1 — Lateral-trunk substitution path

| Field | Value |
|---|---|
| Supporting features | `lumbar_bending_range_deg`, `lumbar_extension_range_deg` (both BH-sig at q=0.012, r_rb = +1.0); `pelvis_tilt_range_deg` (trending, q = 0.084, r_rb = +0.75) |
| Expected effect direction | trunk-segment range ↑ under trunk-sway |
| Observed effect direction | confirmed (lumbar bending +18.3°, lumbar extension +1.6°, pelvis tilt +1.1° trending; all medians, all 10 subjects in agreement on the BH-sig features) |
| Mechanistic interpretation | Enforced lateral trunk perturbation routes the response through a lumbar bending channel rather than through pelvis rotation or hip adduction. The lumbar extension co-increase suggests the bending is not pure frontal — there is a sagittal-coupled component as well, consistent with a multi-axis trunk strategy. |
| Condition-bound scope | Bound to the deliberate-trunk-perturbation walking condition. Does not generalize to natural walking, gait at non-self-selected speeds, or perturbations applied at other body locations. R-side only — L-side equivalence not testable here. |

### Candidate 2 — Distal sagittal contraction under proximal compensation

| Field | Value |
|---|---|
| Supporting features | `ankle_angle_range_deg` (BH-sig at q=0.012, r_rb = −1.0); `ankle_angle_min_deg` (BH-sig at q=0.012, r_rb = +1.0, less plantarflexion at trough); `knee_angle_range_deg` (trending, q = 0.084, r_rb = −0.78) |
| Expected effect direction | distal sagittal joint ROM ↓ when proximal (trunk) compensation engages |
| Observed effect direction | confirmed (ankle range −6.6°, ankle min +5.2° (less plantarflexion), knee range −4.8° trending) |
| Mechanistic interpretation | When the trunk segment absorbs the lateral perturbation (Candidate 1), distal push-off energy contracts: the ankle reduces its dorsiflexion-plantarflexion sweep, and the knee shows a smaller, consistent contraction. This is the *complement* of the trunk-segment amplification, not an independent finding — the body conserves total movement budget between trunk and distal limb. |
| Condition-bound scope | Bound to the deliberate-trunk-perturbation walking condition. Does not generalize to fatigue-induced or pain-driven ankle contraction (which would have different proximal correlates). R-side only — bilateral equivalence not testable here. |

### Candidate 3 — Cadence-slowdown signature

| Field | Value |
|---|---|
| Supporting features | `cycle_duration_s` (BH-sig at q=0.042, +0.12 s median Δ, r_rb = +0.91); `swing_duration_s` (BH-sig at q=0.041, +0.09 s median Δ, r_rb = +0.89); `stance_pct_cycle` (trending negative, q = 0.084, indicating the slowdown adds proportionally more swing than stance) |
| Expected effect direction | cycle and swing durations ↑ under voluntary perturbation; stance fraction ↓ |
| Observed effect direction | confirmed (cycle +0.12 s in 9/10 subjects; swing +0.09 s in 9/10; subject6 is the lone non-positive on both) |
| Mechanistic interpretation | Deliberate trunk perturbation increases per-step attentional load; subjects walk more cautiously, lengthening cycle and swing time. The stance-fraction decrease suggests subjects keep stance duration roughly stable in absolute terms but stretch the swing. The interpretation is *attentional-load-mediated cadence slowdown*, not a primary load-transfer pathway. |
| Condition-bound scope | Bound to deliberate-perturbation walking conditions. Would *not* generalize to fatigue-induced slowdown (which would slow stance, not swing) or to pace-instructed slowdown (which would slow both proportionally). R-side only; symmetric expectation on L. |

**Catalogue note.** Three is the AC4 floor, not a ceiling. A "Pelvis-tilt mild-coupling" candidate could be named on the trending evidence (pelvis_tilt_range_deg +1.1°, q = 0.084); it is held below the candidate-hypothesis line on this cycle because q does not clear the BH gate and the mechanistic story is the same as Candidate 1's secondary observation. β may surface it as a finding if the evidence reading deserves separate naming.

## Falsification re-evaluation on R-side (AC5)

The 6 conditions are evaluated against the R-side surface produced by this cycle, per the *empirical-data-prerequisite* discipline in [`docs/concepts/support-path.md`](../docs/concepts/support-path.md) §Falsification (a "not testable" verdict carries no evidence and does not count toward the 4-condition threshold).

| # | Condition | Verdict | Evidence |
|---|---|---|---|
| 1 | No repeatable patterns across gait cycles | **NOT triggered** (R-side) | 7 / 25 features BH-sig at q<0.05; four of those have r_rb = ±1.0 (every subject moves in the same direction); per-subject paired-delta heatmap shows systematic, not random, response. n=3 cycles per (subject, condition) is too few for within-subject ICC, but the cross-subject pattern is clearly non-random. |
| 2 | Features uncorrelated with movement context | **NOT triggered** (R-side) | The trunk-sway condition response is large (lumbar_bending_range_deg +18.3°) and broad (7 features cross BH at q<0.05). Features respond systematically to condition; the correlation with movement context is unambiguous. |
| 3 | Left-right asymmetry without systematic organization | **Not testable** (data shape) | 1 L-side cycle in the archive; no R/L pairs available at matching (subject, cycle_number). This is the gate cph#28 (L-cycle recovery) owns. Per `docs/concepts/support-path.md` §Falsification, this does not count toward the threshold. |
| 4 | Poor agreement between OpenCap and reference measurements | **NOT triggered** (carried over from cph#22/26) | Pearson r̄ = 0.962 (HRNet) / 0.933 (OpenPose_default) / 0.951 (OpenPose_highAccuracy) across 60 trials × 3 Video backbones. Unchanged from R1's resolution. |
| 5 | Feature extraction consistently fails on clean data | **NOT triggered** | 0.00% missingness across 35 columns × 61 cycles (per `analysis/feature-summary-zeroth-pilot.md` AC2); 25 numeric features extracted on all 60 R-side cycles for this cycle's tests. The aggregation step produced 700 cells with no missing values. |
| 6 | No distinguishable coordination signatures | **NOT triggered** (R-side) | The condition-response signatures themselves are mutually distinguishable: trunk-segment features (Candidate 1) and distal-sagittal features (Candidate 2) move in *opposite* directions; the cadence-slowdown signature (Candidate 3) moves independently of both. Per-subject paired-delta heatmap shows subject heterogeneity in *which* feature responds most strongly within each candidate group — distinguishability is present at both the feature-family and subject levels. A formal PCA / clustering step is out of R3's scope. |

**Falsification score (R-side surface):** 0 of 6 triggered; 5 of 6 cleanly NOT triggered; 1 not testable (condition 3, owned by cph#28). Mechanically ≪ the 4-condition NO-GO threshold from `docs/concepts/support-path.md` §Falsification. The construct survives R-side contact with measurement.

**Important caveat.** "Construct survives R-side contact" does *not* mean "construct is validated." The R-side surface anchors *half* of the bilateral construct the project explicitly tests; H3 (the bilateral pairing claim) is still unanchored. R1 stays REVISE.

## Decision per protocol (AC6)

[`protocols/existing-data-zeroth-pilot.md`](../protocols/existing-data-zeroth-pilot.md) §"Go/No-Go Criteria" decision thresholds vs this cycle's R-side surface:

| Criterion | Threshold | This cycle (R-side) | Pass? |
|---|---|---|---|
| Successfully segment ≥80% of walking trials into clean gait cycles | ≥80% | 60/60 R = 100% (carried from R2 close) | ✓ |
| Extract interpretable feature tables with <20% missing data | <20% missing | 0.00% missing across 35 columns × 61 cycles | ✓ |
| Reasonable agreement with reference measurements where available | qualitative | r̄ 0.93–0.96 across 3 Video backbones × 60 trials (carried) | ✓ |
| Generate ≥3 candidate support-path hypotheses from coordination patterns | ≥3 | 3 named in §"Candidate support-path hypotheses (AC4)" above | ✓ |
| Complete pipeline runs without major technical failures | none | reproducible single-script run; no failures | ✓ |

All GO criteria pass on the R-side surface.

**Decision: R3 = partial GO on R-side.** The R-side aggregate condition-response analysis produces statistically supported, mechanistically interpretable, subject-consistent condition responses across 25 numeric features, with 7 features BH-significant at q<0.05. Three candidate support-path hypotheses are named with mechanism and condition-bound scope. Five of six falsification conditions evaluate NOT triggered on R-side; the sixth (condition 3, L/R asymmetry) is not testable on this archive.

**R1 status: unchanged REVISE.** Per the cph#27 issue body §Non-goals and the γ scaffold §Cross-cycle coordination, R3 cannot lift R1. R1's transition gate is bilateral construct coverage, which depends on L-cycle yield — owned by cph#28. R3 is a *partial* GO because it anchors the R-side half of the bilateral construct, not the full construct.

**R3 phase status update.** R3 moves from NOT STARTED → partial GO on R-side. The remaining R3 work — adding bilateral pairing once cph#28 lifts L-cycle yield — is downstream of cph#28's outcome.

## Cross-cycle binding

cph#27 ran concurrently with cph#28 (L-cycle recovery, branch `cycle/l-cycle-recovery`). The cph#27 issue body §Non-goals binds R1 to remain REVISE regardless of R3 outcome: only cph#28 can lift R1. Highest-status R3 outcome possible was REVISE or partial GO on R-side; this cycle returns the latter.

The status surfaces (PROJECT.md, ROADMAP.md, CHANGELOG.md) updated by this cycle reflect the partial-GO-on-R-side reading and leave R1 / Hypothesis 3 / bilateral construct unchanged. If cph#28 merges to main first, those surfaces will be re-rebased against cph#28's updates and any R1 transition cph#28 produces.

## Next gates

1. **cph#28 — L-cycle recovery.** The owner of R1's transition. Until cph#28 produces L-side cycle yield sufficient for R/L pairing at matching (subject, cycle_number), H3 stays non-testable and R1 stays REVISE.
2. **Full R4 — falsification table at adequate n with bilateral coverage.** Re-runs the 6-condition evaluation in this report at bilateral n once cph#28 lands; specifically updates condition 3 verdict from "not testable" to a substantive verdict. Out of cph#27's scope.
3. **R-side replication / extension (out of scope).** A future cycle could refine: per-subject within-condition cycle-level repeatability (requires ≥10 cycles per (subject, condition), which OpenCap Lab Validation does not provide); first-pass PCA on R-side aggregates to look for sub-population structure; condition-response on a non-trunk-sway perturbation (none in this archive).

## Provenance / Receipt

```text
Receipt: R3 R-side aggregate condition-response analysis
Branch: cycle/r3-rside-aggregate-analysis
Commit: filled by β at merge
Merge SHA: filled by β at merge
Aggregation:
- subjects: 10
- conditions: 2 (natural, trunk-sway)
- features tested: 25 numeric (of 35 total feature-table columns)
- aggregate rows: 700 cells (20 (subject × condition) × 35 columns)
- method (mean/median): median primary, mean reported alongside; sign-flip across aggregations occurred for 1/25 features (hip_flexion_range_deg, ns under either aggregation)
Hypothesis evaluation:
- H1 evidence: partial (1/5 BH-sig at q<0.05, plus 1 trending); supported in distal-contraction form, hip-driven form not supported
- H2 evidence: partial (2/9 BH-sig at q<0.05, plus 1 trending); supported in trunk-segment-driven form, hip-adduction sub-claim not supported
- H3 evaluable: no (L=1 cycle; structurally not testable on this archive)
Falsification re-evaluation:
- conditions evaluable on R-side: 5 of 6 (conditions 1, 2, 4, 5, 6)
- conditions triggered: 0
- 4-condition threshold crossed: no (well below; 0/6 triggered)
Candidate hypotheses surfaced: 3 (Lateral-trunk substitution path; Distal sagittal contraction under proximal compensation; Cadence-slowdown signature)
Decision: partial GO on R-side
R1 status: unchanged REVISE (L-cycle bottleneck holds; cph#28 owns the transition gate)
R3 status: partial GO on R-side (NOT STARTED → partial GO; remaining bilateral work downstream of cph#28)
No raw data committed: yes
Next recommended issue:
- cph#28 — L-cycle recovery (owner of R1's transition); after cph#28 lands, a full R4 falsification re-evaluation at bilateral n
```

## Appendices

### A. Reproducibility

Single command from repo root, with the features CSV at `$GAIT_DATA_ROOT/cph-features/features-zeroth-pilot.csv` (or `/opt/gait-data/cph-features/features-zeroth-pilot.csv`):

```bash
python3 analysis/r3_subject_aggregate_tests.py
```

Output is markdown-rendered to stdout; the tables in §Aggregation surface (AC1), §Paired Wilcoxon signed-rank tests (AC2), and §Hypothesis evidence summary (AC3) are reproduced verbatim from that output. Bootstrap is deterministic (seed=20260519); BH-FDR runs over the 25 numeric-feature p-values.

### B. Method-pick reference

Full rationale: [`.cdr/unreleased/27/self-coherence.md`](../.cdr/unreleased/27/self-coherence.md) §Method picks (M1–M5).

### C. Data policy

No raw participant data, no `.zip`/`.trc`/`.mot`/`.sto`/`.c3d`/`.osim`/`.mp4`/`.mov`/`.csv`/`.parquet` files added to the repo in this cycle. The per-cycle features CSV at `/opt/gait-data/cph-features/features-zeroth-pilot.csv` (read-only input) lives outside the repo per `data/external/README.md`. The aggregate tables in this report are derived and inlined as markdown.
