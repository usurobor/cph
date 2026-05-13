# Features

This file owns the candidate features extracted from gait-cycle data.

## Governing question

Which measurable traces might support or reject a support-path hypothesis?

## Feature principle

Extract features that can be tied to a gait cycle, side, condition, and interpretable movement question.

Do not extract features only because they are available.
Do not train on participant identity.
Do not use labels from visual type lists as ground truth.

## Required indexing

Every feature row should include:

- participant code
- session
- trial id
- condition
- side
- cycle number
- quality flag
- exclusion flag

Without this indexing, feature values cannot be interpreted.

## Timing features

Candidate timing features:

- gait-cycle duration
- stance duration
- swing duration
- stance percentage of cycle
- step-to-step timing variability
- right-left duration difference
- timing of peak hip extension
- timing of peak knee flexion
- timing of peak ankle plantarflexion
- timing of pelvis rotation extrema

Keep original durations as well as normalized timing.

## Range and amplitude features

Candidate waveform summary features:

- pelvis rotation range
- pelvis list range
- trunk rotation range, if available
- hip flexion-extension range
- hip adduction-abduction range
- knee flexion-extension range
- ankle plantarflexion-dorsiflexion range
- peak values and their timing
- stance-phase range for each major joint

Use these features carefully. Range alone can miss sequencing.

## Shape features

Candidate curve-shape features:

- normalized waveform samples across 0-100% gait cycle
- stance-only normalized waveform samples
- first derivative summaries, if noise allows
- smoothness or jerk-like measures, if stable
- curve correlation between cycles
- dynamic time warping distance, if used transparently
- principal component scores from waveform sets

Shape features should remain inspectable through plots.

## Coordination features

Candidate coordination features:

- pelvis-trunk phase relationship
- hip-knee timing offset
- knee-ankle timing offset
- pelvis rotation relative to stance side
- contralateral arm or trunk relation, if available and reliable
- cross-correlation between segment curves
- side-specific coupling differences

These features are closest to the support-path hypothesis, but they are also easier to overinterpret.

## Asymmetry features

Candidate asymmetry features:

- right-left stance duration difference
- right-left waveform difference
- right-left peak timing difference
- right-left range difference
- right-left coordination difference
- within-participant side consistency across conditions

The method is defined in [Left Right Comparison](left-right-comparison.md).

## Condition-response features

Candidate condition-response features:

- normal-to-slow change
- normal-to-fast change
- shod-to-barefoot change
- first-to-repeat trial change
- first-session to repeat-session change, if available

These features ask whether a candidate pattern is stable, speed-dependent, footwear-dependent, or session-dependent.

## Features to avoid at first

Avoid first-pass features that are hard to interpret in the pre-pilot:

- black-box embeddings from raw video
- participant identity predictions
- facial or clothing features
- unreviewed automated labels
- diagnosis-like scores
- any feature that cannot be traced back to a cycle and condition

## Output

The feature table should support three questions:

- Do repeated cycles within a condition resemble each other?
- Do right and left sides differ in interpretable ways?
- Do unsupervised structures remain after accounting for speed, footwear, and capture notes?

If the table cannot answer those questions, revise extraction before modeling.
