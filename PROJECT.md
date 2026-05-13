# Project

## Current realization sequence

The project moves through realizations. Each realization should answer one question and produce one artifact.

### Realization 01 — Walking Is Not a Style

Walking is a recurring whole-body load-transfer strategy, not a visual aesthetic.

Expected artifact:
- `docs/realizations/01-walking-is-not-a-style.md`

### Realization 02 — The Type List Is Not the Object

Visible walking categories are provisional language. The object is the step, the support path, and the gait-cycle data.

Expected artifact:
- `docs/realizations/02-the-type-list-is-not-the-object.md`

### Realization 03 — OpenCap Is the Translation Layer

OpenCap converts video into biomechanical time series. It is not the classifier.

Expected artifact:
- `docs/realizations/03-opencap-is-the-translation-layer.md`

### Realization 04 — Friends Are a Pre-Pilot

The first friend cohort exists to break the pipeline, not to validate the theory.

Expected artifact:
- `docs/realizations/04-friends-are-a-pre-pilot.md`

### Realization 05 — What Broke

The first field report documents what survived, what failed, what was visible, and what was not.

Expected artifact:
- `docs/realizations/05-what-broke.md`

## Friend pre-pilot

The first cohort is a pre-pilot. It is not a study, validation, or evidence for a public claim. Its purpose is to test whether the pipeline is coherent.

The pre-pilot asks:

- Can we capture usable OpenCap data?
- Can we segment gait cycles?
- Can we extract interpretable curves?
- Can we compare left and right stance phases?
- Can we repeat trials without the data falling apart?
- Can blind qualitative observation be compared with kinematic data?
- Which proposed features are useless?
- Which proposed categories become clearer?
- Which proposed categories fail?

The valuable result is discrepancy. Where did the eye invent a pattern? Where did the data show a pattern the eye missed? Where did OpenCap fail? Where did the setup distort the result? Where did the categories become too vague?

## Data policy

Do not commit raw videos. Do not commit names, faces, injury histories, consent forms, or identifiable participant notes.

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

## Source of truth

| Question | Owning file |
|----------|-------------|
| What is this repo? | `README.md` |
| What is a support path? | `docs/concepts/support-path.md` |
| What is the unit of analysis? | `docs/concepts/gait-cycle-as-unit.md` |
| How is the friend pre-pilot run? | `protocols/friend-pre-pilot.md` |
| How are recordings captured? | `protocols/capture-setup.md` |
| What does OpenCap provide? | `instruments/opencap/outputs-to-extract.md` |
| What are OpenCap's limits? | `instruments/opencap/limitations.md` |
| Which features are extracted? | `analysis/features.md` |
| How are clusters tested? | `analysis/clustering-plan.md` |
| How is data handled? | `docs/ethics/data-handling.md` |

Do not duplicate stable facts across files. State the fact once in its owning file and point to it elsewhere.

## Success condition

The first success condition is methodological clarity, not classification accuracy.

After the pre-pilot, the project should know whether OpenCap-derived gait-cycle data contains enough structure to pursue support-path classification.

## Failure conditions

The project weakens or fails if:

- proposed gait families remain only visual impressions
- support path cannot be translated into measurable features
- OpenCap outputs are too noisy for the intended questions
- clusters reflect camera setup, footwear, sex, height, body size, or walking speed instead of load-transfer organization
- left-right asymmetry cannot be represented clearly
- blind observation and kinematic traces cannot be compared coherently
- the friend pre-pilot does not produce repeatable, interpretable gait-cycle data

All of these outcomes are useful. The goal is not to protect the theory. The goal is to find out what survives contact with measurement.
