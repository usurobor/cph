# Limitations

OpenCap is useful for this project, but it is not a complete answer to the research question.

## Governing question

What are OpenCap's limits for support-path analysis?

## Measurement limits

OpenCap estimates movement from video. It does not directly measure bones, muscles, fascia, force paths, pain, intention, or identity.

The output is processed measurement. It depends on:

- camera placement
- synchronization
- calibration
- lighting
- body visibility
- pose-estimation quality
- clothing and occlusion
- model assumptions
- processing settings

Bad capture can produce confident-looking curves.

## Conceptual limits

OpenCap does not output support paths.

It can provide joint angles, trajectories, timing, and related biomechanical quantities. The project must still define features, segment gait cycles, compare conditions, and test whether the traces support a support-path hypothesis.

Do not write:

> OpenCap found the participant's support path.

Write:

> OpenCap-derived curves showed this pattern under this condition.

## Small-sample limits

The friend pre-pilot is too small to validate categories.

With 5-10 participants, apparent structure may reflect:

- one participant's idiosyncrasy
- footwear
- speed
- fatigue
- the room
- camera setup
- trial order
- processing artifact

This is why the first goal is methodological clarity.

## Kinematic limits

Kinematic curves can show movement pattern, but they do not by themselves prove load, force, tissue behavior, or cause.

For example:

- delayed pelvis rotation may be visible, but its cause may be unclear
- asymmetry may be present, but its meaning may depend on pain, habit, speed, or capture error
- smoother curves may reflect processing filters as well as movement
- a cluster may separate conditions without representing a load-transfer strategy

The project should describe kinematics as kinematics unless additional analysis justifies more.

## Dynamics limits

OpenCap-associated workflows can estimate dynamics, but estimated forces and muscle quantities require stronger assumptions than joint-angle curves.

For this repo, dynamics are optional second-pass outputs. They should not be used in the friend pre-pilot to make health, injury, or performance claims.

## Ethics limits

OpenCap does not anonymize the original video.

Even if the analysis uses curves, raw capture data remain identifiable. Follow [Data Handling](/tmp/gait-support-paths/docs/ethics/data-handling.md) and [Public Sharing Rules](/tmp/gait-support-paths/docs/ethics/public-sharing-rules.md).

## Failure rule

If OpenCap output is noisy, inconsistent, or not interpretable for the intended feature, the feature fails for that round.

Do not compensate by making a stronger qualitative claim.
