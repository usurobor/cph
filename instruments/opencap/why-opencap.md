# Why OpenCap

OpenCap is used because this project needs a translation layer between ordinary video and biomechanical time series.

## Governing question

Why use OpenCap instead of training directly on raw video or relying only on visual observation?

## Reason

The project is not trying to classify appearances. It is trying to test whether qualitative observations of load-transfer strategy correspond to recurring gait-cycle patterns.

Raw video is too mixed for that first analysis target. It contains movement, but it also contains face, clothing, body size, lighting, camera angle, room, shoes, and observer expectation.

OpenCap reduces that problem by estimating movement quantities that can be compared across gait cycles.

## What OpenCap is

OpenCap is an open-source platform for estimating human movement from smartphone videos. The OpenCap paper describes a system that computes kinematics and dynamics from videos captured from two or more smartphones. The OpenCap core repository states that the pipeline takes two or more videos and estimates 3D marker positions and human movement kinematics, including joint angles, in OpenSim format.

For this repo, that makes OpenCap a translation layer:

video -> biomechanical time series -> gait-cycle features -> hypothesis tests

## Why not direct visual labels

Direct visual labeling would make the observer's impression the target.

That is risky because the model could learn:

- clothing
- sex or body size
- camera angle
- shoe type
- participant identity
- the observer's naming habit

Those variables may correlate with labels without measuring the support-path hypothesis.

## Why not raw-video AI first

Raw-video models can be powerful, but they are hard to audit in a small pre-pilot. If a model separates participants, the project may not know whether it used movement coordination or a visible confound.

OpenCap-derived curves are not perfect, but they are inspectable. A hip-angle waveform, pelvis rotation curve, or stance-time difference can be plotted, questioned, and compared with the blind memo.

## Why not a full motion-capture lab

A marker-based motion-capture lab would provide stronger control and may be needed later.

It is not the right first instrument for this repo because the immediate question is whether the pipeline and concepts are coherent enough to justify more expensive collection.

OpenCap is accessible enough for a friend pre-pilot and structured enough to keep the analysis biomechanical rather than purely visual.

## Working position

OpenCap is not treated as ground truth.
OpenCap is not treated as a support-path detector.
OpenCap is not treated as a diagnosis system.

It is treated as a practical translation layer whose outputs may or may not be stable enough for this project's question.

Primary references are listed in [Bibliography](../../references/bibliography.md).
