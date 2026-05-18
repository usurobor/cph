# Coherence Path Hypothesis

This document defines the Coherence Path Hypothesis, the research claim cph tests.

The hypothesis is one sentence:

> During walking, each step may create a temporary whole-body coordination path around ground contact — a path that is not anatomical, but inferred from how timing, stiffness, segment coupling, orientation, asymmetry, and condition response organize in gait-cycle data.

Everything below explains what that sentence means, what would count as evidence for or against it, and what the hypothesis does *not* claim.

## Governing question

Can recurring whole-body support/coherence paths be inferred from gait-cycle data?

## Definition

A coherence path is an inferred coordination pattern that recurs across walking steps under similar conditions.

The path is not a fascia line, not a fixed anatomical structure, and not a property of the person. It is a temporary organization of how the body receives, routes, and returns load through one gait cycle. The same body can express different coherence paths under different speeds, footwear, fatigue, or attention conditions.

The hypothesis claims that such paths exist, recur measurably, and can be told apart from each other in gait-cycle data. It does not claim that any specific named path is correct.

## What counts as evidence

Evidence for the hypothesis is built from measured quantities and reaches the hypothesis only through interpretation. The measured side:

- joint kinematics — hip, knee, ankle, pelvis, trunk angle traces
- timing — heel-strike and toe-off events, stance and swing durations, cycle duration
- segment coupling — cross-correlation, phase lag, coordination between segments within a cycle
- left–right asymmetry — systematic, not random, differences between sides
- condition response — how the above shift across walking speeds, footwear, trunk-sway perturbation, fatigue, repeat session
- reference comparisons — agreement between OpenCap-derived kinematics and gold-standard mocap on the same population

Evidence *for* the hypothesis is a pattern in those quantities that (a) recurs across cycles within a participant under one condition, (b) shifts predictably across conditions, and (c) can be told apart from neighbouring patterns in the same participant or in others.

## What does not count as evidence

The following may propose a coherence path but cannot establish one:

- a memorable visual impression of a person's walk
- a still-frame posture
- one unusually clear step
- a participant's personality, history, or self-description
- a named walking type, including any of the seven families below
- the observer's confidence

These belong on the proposal side of the working sequence (observation proposes → measurement decides). They generate hypotheses; they do not confirm them.

A high project coherence score (C_Σ, see [CDR.md](../../CDR.md)) is also not evidence. C_Σ measures whether the repo describes one coherent research project. It is mute on whether the hypothesis is correct.

## Relationship to support path

`support path` is the repo's operational term for the measurable surface of this hypothesis. [docs/concepts/support-path.md](support-path.md) owns the operational definition; this document does not redefine it.

The mapping is:

```
Coherence Path Hypothesis = the research claim (this document)
support path              = the operationalized gait-cycle pattern (support-path.md)
```

The hypothesis and its operationalization must remain terminologically distinct. Drift between them — calling a measured trace a "coherence path" without inference, or calling the hypothesis a "support path" — is one of the recurring failure modes the CDR α-axis (pattern coherence) is meant to catch.

## Relationship to the seven gait families

Seven informal walking families have been named as observational vocabulary:

- Pendular Carrier
- Elastic Rebounder
- Braced Axial Walker
- Collapse-and-Catch Walker
- Spiral Driver
- Segmented Block Mover
- Asymmetric Protector

[docs/articles/seven-ways-people-walk.md](../articles/seven-ways-people-walk.md) carries the longer description.

The families are *candidate surface expressions* of coherence-path organization. They are not the core theory. Three of the load-bearing consequences follow:

1. The hypothesis does not depend on the seven families. If measurement supports three families, twelve, or none, the hypothesis can still survive — it is the recurrence of coordination paths that is at stake, not the count.
2. Asymmetry may be a modifier across families rather than a family of its own. The seventh entry ("Asymmetric Protector") is the most provisional.
3. AI clustering is not required to preserve the list. Measurement is allowed to destroy, split, merge, or replace the families.

## Operationalization

The hypothesis becomes testable when each of its terms is bound to something measurable. The current operational chain:

1. **gait cycle** — one cycle from one side from one trial under one condition, per [gait-cycle-as-unit.md](gait-cycle-as-unit.md).
2. **coordination pattern** — a vector of timing, joint-angle, pelvis, and coupling features extracted per cycle, per [analysis/features.md](../../analysis/features.md).
3. **recurrence** — within-participant within-condition stability of those features.
4. **distinguishability** — between-condition or between-participant separability of those features.
5. **inference to coherence path** — accepted only after recurrence and distinguishability are demonstrated on data capable of showing them.

The chain runs forward only. A break in any earlier link blocks inference at the later links.

## Current empirical status

**REVISE** (per [reports/field-report-01-existing-data-zeroth-pilot.md](../../reports/field-report-01-existing-data-zeroth-pilot.md), 2026-05-17 real-data run).

State of the chain as of the latest merged field report:

- **OpenCap technology** — PASS. The OpenCap-vs-reference comparison on the OpenCap Lab Validation archive (60 walking trials × 10 subjects) returns Pearson r̄ 0.962 (HRNet), 0.933 (OpenPose_default), 0.951 (OpenPose_highAccuracy), well above the r̄ ≥ 0.7 GO threshold. OpenCap-derived kinematics are reliable enough for the rest of the chain to use them.
- **Gait-cycle segmentation** — FAIL on real Mocap heel-marker data. The detector fires on 18.3% of trials (11 / 60), all right-side; zero left-side cycles were extracted. The failure is in `scripts.segmentation.detect_heel_strikes` and is bounded to a single-issue revision cycle.
- **Hypothesis testability** — blocked. With 11 right-side cycles and no left-side cycles, the within-participant recurrence and left–right asymmetry tests cannot be evaluated yet.

The hypothesis is not validated. It is also not refuted. The current REVISE posture means the next gate is the segmentation fix, after which the recurrence and distinguishability tests can be run.

## Falsification conditions

The hypothesis weakens under any of the following, evaluated against data capable of triggering them (see [support-path.md §Falsification](support-path.md#falsification-conditions-for-existing-data-zeroth-pilot) for the operational form and the empirical-prerequisite framing that distinguishes "not triggered" from "not testable"):

1. No repeatable patterns across gait cycles within participant within condition.
2. Features uncorrelated with condition or participant.
3. Left–right asymmetry without systematic organization.
4. Poor OpenCap–reference agreement (currently CLEARED).
5. Feature extraction consistently fails on clean data.
6. No distinguishable coordination signatures.

The hypothesis also weakens — without any of the six triggering — if the observed patterns are better explained by trial crop, marker artifact, camera setup, subject morphology, or condition labels alone. That alternative-explanation check is part of inference, not a separate row in the table.

Decision rule per `support-path.md`: 4 or more triggered (on data capable of triggering) requires fundamental revision before friend data collection.

## Practical consequences if supported

If the hypothesis survives measurement, several things become possible — and none are claims the project makes today:

- gait description can move from visual labels toward measurable movement organization
- available and missing movement strategies can be named without typing people
- movement education, rehab reasoning, athletic analysis, and AI gait interpretation gain a measurable substrate to argue from
- somatic observation and biomechanical measurement gain a shared object

These are reasons to test the hypothesis. They are not consequences the hypothesis has earned.

## What would still remain unproven

Even if the hypothesis survives every test in this repo, the following remain open:

- whether the inferred path corresponds to any specific anatomical mechanism
- whether the path is causal for any specific functional outcome (performance, injury, fatigue)
- whether the seven families are the right partition, the wrong partition, or one of many viable partitions
- whether observations made on existing-data populations generalize to other populations, ages, or pathologies
- whether the path concept transfers to running, climbing, or non-walking gait

Each of these is a separate research question. None are answered by surviving the current measurement chain.
