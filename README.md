# Support Paths

This repository investigates whether recurring whole-body load-transfer patterns in walking can be detected in gait-cycle data.

Walking is not treated as a style, personality signal, or fixed type. It is treated as a repeated support event: the foot contacts the ground, load enters the body, some regions stiffen, others yield, and movement either travels through the body or becomes trapped locally.

The research object is not the person.
The research object is the step under a condition.

## Governing Question

Can qualitative observations of walking strategy be translated into measurable gait-cycle patterns without pretending that the data already proves the theory?

## Core Claim

A walking step is a temporary load-transfer organization.

After ground contact, the body organizes support through timing, stiffness, orientation, and segment coordination. Some of these organizations may recur across steps, sides, speeds, footwear conditions, fatigue states, and contexts.

This project calls the inferred coordination pattern a **support path**.

A support path is not an anatomical structure. It is not a fixed fascia line. It is not a diagnosis.

A support path is a temporary pattern by which the body receives, routes, stabilizes, and returns load during a gait cycle.

## Working Sequence

Observation proposes.
OpenCap translates.
AI sorts.
Measurement decides.

## Method

The project moves through five realizations.

### Realization 01 — Walking Is Not a Style

Walking is a recurring whole-body load-transfer strategy, not a visual aesthetic.

### Realization 02 — The Type List Is Not the Object

Visible walking categories are provisional language. The object is the step, the support path, and the gait-cycle data.

### Realization 03 — OpenCap Is the Translation Layer

OpenCap converts video into biomechanical time series. It is not the classifier.

### Realization 04 — Friends Are a Pre-Pilot

The first friend cohort exists to break the pipeline, not to validate the theory.

### Realization 05 — What Broke

The first field report documents what survived, what failed, what was visible, and what was not.

## Instrument

OpenCap is treated as a translation layer.

Raw video contains gait, but it also contains face, clothing, camera angle, lighting, shoes, body size, age, sex, background, and observer expectation. Training directly on raw video risks learning the wrong thing with confidence.

OpenCap changes the substrate.

The object stops being the person in the video and becomes movement curves: joint angles, segment motion, marker trajectories, gait-cycle timing, asymmetry, and related biomechanical traces.

OpenCap does not see support paths directly.
It provides data from which support-path hypotheses can be tested.

## Unit of Analysis

The unit is the gait cycle under a condition.

Examples:

- normal speed, shod, right stance
- normal speed, shod, left stance
- slow speed, barefoot, right stance
- fast speed, barefoot, left stance
- repeat session, same condition, different day

The person is not classified first.
Steps are analyzed first.

Only after enough cycles are collected do we ask whether a person tends to return to a recognizable movement attractor.

## Candidate Traces

A support path may leave traces in:

- pelvis rotation
- trunk rotation
- hip-knee-ankle timing
- stance duration
- left-right asymmetry
- segment coupling
- smoothness
- delayed stabilization
- reduced counter-rotation
- push-off timing
- changes across speed, fatigue, footwear, or attention

These traces are not the support path itself.
They are measurable signs that may or may not support the hypothesis.

## Analysis Direction

The first AI task should not be supervised label imitation.

Do not label friends as fixed walking types and train a model to reproduce those labels. That would only automate observer bias.

The first useful model should be unsupervised or self-supervised.

Input:

- OpenCap-derived gait-cycle curves

Task:

- find recurring structures

Then compare those structures with the proposed families.

If the clusters resemble proposed patterns, the typology earns a first pass.
If the clusters produce fewer families, more families, or no useful families, the theory updates.
If clusters collapse into sex, height, shoe type, camera setup, or walking speed, the project has failed usefully.

## Friend Pre-Pilot

The first cohort is a pre-pilot.

It is not a study.
It is not validation.
It is not evidence for a public claim.

Its purpose is to test whether the pipeline is coherent.

Questions:

- Can we capture usable OpenCap data?
- Can we segment gait cycles?
- Can we extract interpretable curves?
- Can we compare left and right stance phases?
- Can we repeat trials without the data falling apart?
- Can blind qualitative observation be compared with kinematic data?
- Which proposed features are useless?
- Which proposed categories become clearer?
- Which proposed categories fail?

## Minimal Pre-Pilot Design

Use 5–10 people.

Do not recruit "interesting bodies." Use available participants and record context carefully.

Record:

- footwear
- fatigue
- pain or injury history
- dominant side
- recent exercise
- comfort with being recorded
- walking condition
- repeat session if possible

Walking conditions:

- normal walking
- slow walking
- fast walking
- barefoot walking
- shod walking
- repeat session on another day if possible

Before processing the videos, write a blind observation memo.
After processing, compare observation with data.

The valuable result is discrepancy.

Where did the eye invent a pattern?
Where did the data show a pattern the eye missed?
Where did OpenCap fail?
Where did the setup distort the result?
Where did the categories become too vague?

## Ethics

Gait video is identifiable biometric data.

Do not publish raw friend videos casually.
Do not diagnose participants.
Do not tell a participant, "you are this type."
Do not imply pathology.
Do not turn private body observations into public labels.

Use explicit consent.
State what is captured, where it is stored, who can see it, and what may be published.

Public materials should use anonymized movement traces when possible.

The output sentence is:

> Under this condition, this recording shows this movement pattern.

Not:

> This is who you are.

## Repository Structure

```txt
gait-support-paths/
  README.md
  PROJECT.md
  docs/
    realizations/
      01-walking-is-not-a-style.md
      02-the-type-list-is-not-the-object.md
      03-opencap-is-the-translation-layer.md
      04-friends-are-a-pre-pilot.md
      05-what-broke.md
    concepts/
      support-path.md
      gait-cycle-as-unit.md
      load-transfer-strategy.md
      failure-conditions.md
    ethics/
      consent-template.md
      data-handling.md
      public-sharing-rules.md
  protocols/
    friend-pre-pilot.md
    capture-setup.md
    walking-conditions.md
    blind-observation-memo.md
  instruments/
    opencap/
      why-opencap.md
      outputs-to-extract.md
      limitations.md
  analysis/
    features.md
    clustering-plan.md
    left-right-comparison.md
  reports/
    field-report-00-plan.md
    field-report-01-friend-pre-pilot.md
  data/
    README.md
  notebooks/
    README.md
  references/
    bibliography.md
```

## Data Policy

Do not commit raw videos.

Do not commit names, faces, injury histories, consent forms, or identifiable participant notes.

The public repository may contain:

- theory
- protocols
- consent language
- analysis code
- anonymized traces
- synthetic examples
- field reports
- failure notes

Raw data belongs in private storage with explicit consent and access rules.

## Success Condition

The first success condition is methodological clarity, not classification accuracy.

After the pre-pilot, the project should know whether OpenCap-derived gait-cycle data contains enough structure to pursue support-path classification.

## Failure Conditions

The project weakens or fails if:

- proposed gait families remain only visual impressions
- support path cannot be translated into measurable features
- OpenCap outputs are too noisy for the intended questions
- clusters reflect camera setup, footwear, sex, height, body size, or walking speed instead of load-transfer organization
- left-right asymmetry cannot be represented clearly
- blind observation and kinematic traces cannot be compared coherently
- the friend pre-pilot does not produce repeatable, interpretable gait-cycle data

All of these outcomes are useful.

The goal is not to protect the theory.
The goal is to find out what survives contact with measurement.

## Current Status

This repository is at the methods-design stage.

All 24 content files have been written. The next step is field testing: execute the friend pre-pilot protocol to test whether the pipeline can capture, process, and analyze gait data coherently.

## References

- OpenCap Core: https://github.com/opencap-org/opencap-core
- OpenCap paper: https://doi.org/10.1371/journal.pcbi.1011462
- OpenSim: https://opensim.stanford.edu/
