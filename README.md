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

The project moves through five realizations:

1. **Walking Is Not a Style** — Walking is a recurring whole-body load-transfer strategy, not a visual aesthetic.
2. **The Type List Is Not the Object** — Visible walking categories are provisional language. The object is the step, the support path, and the gait-cycle data.
3. **OpenCap Is the Translation Layer** — OpenCap converts video into biomechanical time series. It is not the classifier.
4. **Existing Data Comes First** — Process existing validation datasets before collecting new participant data.
5. **Friends Are Not Validation** — The friend cohort tests pipeline robustness, not theoretical claims.
6. **What Broke** — The first field report documents what survived, what failed, what was visible, and what was not.

## Current Status

See [PROJECT.md](PROJECT.md) for current stage, implementation status, and next steps.

This repository is at the existing-data zeroth pilot stage. All 24 content files have been written. The next step is processing existing OpenCap Lab Validation walking data to test whether the pipeline can segment gait cycles, extract features, and generate interpretable support-path hypotheses before collecting new participant data.

## Safety Boundary

Gait video is identifiable biometric data.

- Do not publish raw friend videos casually
- Do not diagnose participants
- Do not tell a participant, "you are this type"
- Do not imply pathology
- Do not turn private body observations into public labels

The output sentence is: "Under this condition, this recording shows this movement pattern."

Not: "This is who you are."

Complete ethics protocols are in [docs/ethics/](docs/ethics/).

## Repository Structure

```txt
gait-support-paths/
  README.md                    # What the repo is, core claim, status overview
  PROJECT.md                   # Current stage, implementation status, next steps
  docs/
    realizations/              # The five project realizations
    concepts/                  # Core theory: support paths, units, failure conditions
    ethics/                    # Consent, data handling, public sharing rules
  protocols/                   # How to run the friend pre-pilot
  instruments/                 # OpenCap usage, outputs, limitations
  analysis/                    # Feature extraction, clustering plans
  reports/                     # Field reports from testing
  data/                        # Private storage guidelines
  notebooks/                   # Analysis code
  references/                  # Bibliography
```

## Where to Go Next

- **What is a support path?** → [docs/concepts/support-path.md](docs/concepts/support-path.md)
- **How to run the pre-pilot?** → [protocols/friend-pre-pilot.md](protocols/friend-pre-pilot.md)
- **What features are extracted?** → [analysis/features.md](analysis/features.md)
- **What can go wrong?** → [docs/concepts/failure-conditions.md](docs/concepts/failure-conditions.md)
- **How is data handled ethically?** → [docs/ethics/data-handling.md](docs/ethics/data-handling.md)

## References

- OpenCap Core: https://github.com/opencap-org/opencap-core
- OpenCap paper: https://doi.org/10.1371/journal.pcbi.1011462
- OpenSim: https://opensim.stanford.edu/
