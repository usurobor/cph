# OpenCap Is the Translation Layer

OpenCap converts video into biomechanical time series. It is not the classifier.

## The distinction

Raw video contains walking, but it also contains face, clothing, camera angle, lighting, shoes, body size, age, sex, background, and observer expectation.

If a model is trained directly on raw video, it may learn the wrong thing with confidence.

OpenCap changes the substrate. The project moves from person-in-video to movement data.

## What OpenCap provides here

OpenCap is useful because it estimates three-dimensional movement from synchronized smartphone videos and represents that movement in biomechanical formats. The project treats those outputs as a translation layer between qualitative observation and analysis.

For this repo, OpenCap should be used to obtain candidate traces such as:

- joint-angle curves
- marker or landmark trajectories
- pelvis and trunk orientation
- hip, knee, and ankle timing
- stance and swing timing, if events can be identified reliably
- left-right differences
- trial-to-trial repeatability

The owning file for specific outputs is [Outputs To Extract](/tmp/gait-support-paths/instruments/opencap/outputs-to-extract.md).

## What OpenCap does not provide

OpenCap does not see support paths directly.
It does not classify gait families for this project.
It does not decide whether a support-path hypothesis is true.
It does not remove the need for careful capture, metadata, cycle segmentation, and interpretation.

It produces measurements from which support-path hypotheses can be tested.

## Why this matters

The eye is allowed to propose.
The translation layer is allowed to measure.
The model is allowed to sort.

None of those steps should be allowed to silently replace the others.

If the qualitative memo says one thing and the curves say another, the discrepancy is the result. It should be studied, not hidden.

## Working rule

OpenCap output should be treated as processed measurement, not raw truth.

Every claim still needs:

- the condition
- the side
- the cycle set
- the extracted feature or waveform
- a note about capture or processing uncertainty

The safe sentence remains:

> Under this condition, this recording shows this movement pattern.
