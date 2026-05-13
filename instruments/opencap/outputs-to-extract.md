# Outputs To Extract

This file owns the list of OpenCap-derived outputs to extract for the support-path project.

## Governing question

What does OpenCap provide that can be turned into gait-cycle features?

## First-pass outputs

Extract these first:

- processed joint-angle time series
- 3D marker or landmark trajectories, if available from the session export
- scaled OpenSim model or model metadata, if available
- trial metadata and frame timing
- video or processing quality notes
- any OpenCap event, kinematic, or results files needed to reconstruct the time base

The exact file names may depend on the OpenCap workflow used. Preserve the raw exported files privately and create analysis copies with participant codes.

## Kinematic curves of interest

For each usable trial, extract or derive time-normalized curves for:

- pelvis tilt, list, and rotation
- lumbar or trunk orientation, if available
- hip flexion-extension, adduction-abduction, and rotation
- knee flexion-extension
- ankle plantarflexion-dorsiflexion
- foot progression or foot orientation, if available
- center-of-mass proxy, if available and reliable

The first analysis should prefer kinematics that are visibly interpretable and consistently exported.

## Timing outputs

Extract or derive:

- trial duration
- frame rate or sampling interval
- candidate foot contact events
- candidate toe-off events, if reliable
- stance duration
- swing duration
- gait-cycle duration
- cadence or step timing

If event detection is uncertain, mark it as uncertain. Do not hide event ambiguity inside a feature table.

## Side-specific outputs

For each participant and condition, keep right and left cycles separate before averaging.

Needed exports:

- right-defined gait cycles
- left-defined gait cycles
- right stance phase curves
- left stance phase curves
- side-specific timing
- side-specific exclusion flags

Left-right comparison is owned by [Left Right Comparison](/tmp/gait-support-paths/analysis/left-right-comparison.md).

## Optional second-pass outputs

OpenCap and associated processing tools can support dynamics estimates such as joint moments, loads, muscle activations, or related simulation outputs. These are not first-pass requirements for the friend pre-pilot.

Use second-pass dynamics only if:

- capture quality is high
- kinematic cycle segmentation is stable
- the output can be interpreted responsibly
- limitations are reported clearly

Do not use dynamics estimates to make clinical claims.

## Export table

For each trial, maintain a table with:

- participant code
- session
- trial id
- condition
- exported file names
- processing status
- quality flag
- number of usable right cycles
- number of usable left cycles
- notes

The table is an analysis tool and an audit trail.

## Minimum viable extraction

The pre-pilot has enough data to proceed only if it can produce:

- at least a few usable gait cycles per side for the core conditions
- interpretable hip, knee, ankle, and pelvis curves
- condition labels attached to every cycle
- documented exclusions

If those outputs cannot be produced, the correct result is a pipeline failure note.
