# Left Right Comparison

This file defines how left-right asymmetry is analyzed.

## Governing question

How does the project compare right and left stance without turning asymmetry into diagnosis or identity?

## Principle

Right and left sides are analyzed separately first, then compared.

Asymmetry is not automatically pathology. It may reflect task, history, comfort, speed, footwear, fatigue, capture error, or ordinary variation.

The project describes what appears in the recording.

## Input

For each participant and condition, collect:

- right-defined gait cycles
- left-defined gait cycles
- right stance phase curves
- left stance phase curves
- timing features for each side
- quality flags
- exclusion notes

Do not average sides before checking whether averaging is justified.

## Timing comparison

Compare:

- right versus left gait-cycle duration
- right versus left stance duration
- right versus left stance percentage
- timing of key waveform peaks
- timing variability across cycles

Report both absolute differences and direction.

Example:

> In normal shod trials, right stance duration was longer than left stance duration in 5 of 6 usable cycle pairs.

## Waveform comparison

For each major curve, compare right and left:

- mean waveform
- within-side variability
- right-left difference waveform
- peak value difference
- peak timing difference
- curve correlation or distance

Plot curves before reducing them to one number.

## Coordination comparison

Compare side-specific coordination features:

- hip-knee timing
- knee-ankle timing
- pelvis rotation timing relative to stance
- pelvis-trunk relationship, if available
- stance-phase smoothness or interruption, if stable

These comparisons are closer to the support-path question than simple range differences, but they require more caution.

## Condition comparison

Ask whether asymmetry changes across:

- normal shod
- slow shod
- fast shod
- normal barefoot
- repeat trial
- repeat session, if available

An asymmetry that appears only under one condition should be reported as condition-specific.

## Reporting language

Use:

> Under the fast shod condition, left stance cycles showed later ankle plantarflexion peak than right stance cycles.

Do not use:

> The participant has a left-side problem.

## Failure cases

Left-right comparison fails for a trial if:

- one side has too few usable cycles
- side event detection is unreliable
- OpenCap tracking differs strongly by side because of camera view
- the participant turned, hesitated, or changed task
- curves are too noisy to interpret

Flag failure instead of forcing symmetry metrics.

## Output

The left-right output should include:

- side-specific cycle counts
- side-specific feature summaries
- plots of right and left curves
- explicit asymmetry findings
- uncertainty notes
- condition-specific interpretation

The result is a movement description, not a participant label.
