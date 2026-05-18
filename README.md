# cph — Coherence Path Hypothesis

cph is a research project that tests one claim: during walking, each step may create a temporary whole-body coordination path around ground contact, inferred from how timing, stiffness, segment coupling, orientation, asymmetry, and condition response organize in gait-cycle data.

The repo is also a model project for **CDR — Coherence-Driven Research**. It does for research what versioning, changelogs, and release gates do for software: continuously measure whether the hypothesis, methods, evidence, and process still describe one system.

## What is this project?

cph is a research project that tests the **Coherence Path Hypothesis** in human walking. It is not a product, not a clinical tool, not a typology of people. It is the disciplined attempt to find out whether the hypothesis survives measurement against real gait-cycle data.

The repo holds the theory, the methods, the analysis pipeline, the field reports, and the coherence ledger of the project itself.

## What is the hypothesis?

> During walking, each step may create a temporary whole-body coordination path around ground contact. The path is not a literal anatomical cord or fascia line. It is inferred from timing, stiffness, segment coupling, orientation, asymmetry, and condition response in gait-cycle data.

The full definition, the evidence rules, the operationalization, the falsification conditions, and the practical consequences if supported all live in [docs/concepts/coherence-path-hypothesis.md](docs/concepts/coherence-path-hypothesis.md).

The repo's operational term for the measurable surface of the hypothesis is **support path**, defined in [docs/concepts/support-path.md](docs/concepts/support-path.md). The hypothesis and its operationalization are kept terminologically distinct on purpose:

```
Coherence Path Hypothesis = the research claim
support path              = the operationalized gait-cycle pattern
```

## Why is this worth testing?

If recurring coherence paths can be inferred from gait-cycle data, several things become possible — *none of which the project claims today*:

- gait description can move from visual labels toward measurable movement organization
- available and missing movement strategies can be named without typing people
- movement education, rehab reasoning, athletic analysis, and AI gait interpretation gain a measurable substrate to argue from
- somatic observation and biomechanical measurement gain a shared object

These are reasons to test the hypothesis. They are not consequences the hypothesis has earned.

## What is not being claimed

- not diagnosis
- not personality inference
- not fascia-line proof
- not "you are this gait type"
- not validation of the seven gait families
- not a typology of people — the object is the step under a condition, not the person

### Safety boundary

Gait video is identifiable biometric data. The repo treats it accordingly: no public raw video, no participant labeling, no diagnostic claims. The strongest allowed sentence about a recording is:

> Under this condition, this recording shows this movement pattern.

Not: "This is who you are." Complete ethics protocols live in [docs/ethics/](docs/ethics/).

## How does this connect to the seven gait families?

Seven informal walking families — Pendular Carrier, Elastic Rebounder, Braced Axial Walker, Collapse-and-Catch Walker, Spiral Driver, Segmented Block Mover, Asymmetric Protector — exist as observational vocabulary, described in [docs/articles/seven-ways-people-walk.md](docs/articles/seven-ways-people-walk.md).

The families are *candidate surface expressions* of coherence-path organization. They are not the core theory.

Three consequences follow:

1. The Coherence Path Hypothesis does not depend on the seven families. If measurement supports three families, twelve, or none, the hypothesis can still survive — what is at stake is recurrence of coordination paths, not the count.
2. Asymmetry may be a modifier across families rather than a family of its own.
3. AI clustering is not required to preserve the list. Measurement is allowed to destroy, split, merge, or replace the families.

## Current empirical state

**REVISE** (per [reports/field-report-01-existing-data-zeroth-pilot.md](reports/field-report-01-existing-data-zeroth-pilot.md), 2026-05-17 real-data run).

- The OpenCap Lab Validation archive (60 walking trials × 10 subjects) has been acquired and run through the pipeline.
- The OpenCap-vs-reference comparison **passes** by a wide margin (Pearson r̄ 0.93–0.96 across HRNet, OpenPose_default, OpenPose_highAccuracy). OpenCap-derived kinematics are reliable enough for the rest of the chain to use them.
- Gait-cycle segmentation **fails** on real Mocap heel-marker data: 18.3% of trials (11 / 60), all right-side; zero left-side cycles. The failure is bounded to `scripts.segmentation.detect_heel_strikes` and is the next gate.
- The hypothesis itself **is not yet testable** — with 11 right-side cycles and no left-side cycles, recurrence and asymmetry tests cannot be evaluated yet.

The hypothesis is not validated. It is also not refuted. [PROJECT.md](PROJECT.md) carries the live operational status.

## How CDR works in this repo

This repo runs research the way software is run: with versioning, changelogs, tests, and gates — but the unit being versioned is the project's coherence, not its features.

The working sequence:

- **observation proposes** — qualitative description generates hypotheses
- **OpenCap translates** — video becomes biomechanical time series
- **AI / analysis sorts** — pattern extraction proposes structure
- **measurement decides** — features tested against gait-cycle data render the verdict
- **TSC measures the project itself** — does the repo still describe one coherent research project as the research changes?

[CDR.md](CDR.md) owns the full doctrine: what CDR is, what it is not, the three triadic-coherence axes (α pattern, β evidence relation, γ process), what C_Σ means and does not mean, the measurement cadence, and the changelog rule.

A high project coherence score does **not** mean the Coherence Path Hypothesis is correct. A low score blocks empirical claims until the project re-coheres.

## Source of truth

Each question below has one owning file. Sibling files point here; they do not restate it.

| Question | Owning file |
|----------|-------------|
| What is this project? | `README.md` |
| What is CDR? | `CDR.md` |
| What is the hypothesis? | `docs/concepts/coherence-path-hypothesis.md` |
| What is a support path? | `docs/concepts/support-path.md` |
| Where are research gates tracked? | `ROADMAP.md` |
| What is current operational status? | `PROJECT.md` |
| What changed over time? | `CHANGELOG.md` |
| What empirical evidence exists? | `reports/` |
| What TSC targets are measured? | `targets/` |

`ROADMAP.md`, `CHANGELOG.md`, and `targets/` are delivered by sibling sub-issues in the same wave (master usurobor/cph#11) and may not be present on this branch in isolation. The table is the wave's source-of-truth contract; rows resolve as the wave merges.

## Where to go next

- **What is the hypothesis exactly?** → [docs/concepts/coherence-path-hypothesis.md](docs/concepts/coherence-path-hypothesis.md)
- **What is a support path?** → [docs/concepts/support-path.md](docs/concepts/support-path.md)
- **What are the seven families?** → [docs/articles/seven-ways-people-walk.md](docs/articles/seven-ways-people-walk.md)
- **How does CDR work here?** → [CDR.md](CDR.md)
- **What is the current operational status?** → [PROJECT.md](PROJECT.md)
- **What is the latest field evidence?** → [reports/field-report-01-existing-data-zeroth-pilot.md](reports/field-report-01-existing-data-zeroth-pilot.md)
- **How is data handled ethically?** → [docs/ethics/data-handling.md](docs/ethics/data-handling.md)

## References

- OpenCap Core: https://github.com/opencap-org/opencap-core
- OpenCap paper: https://doi.org/10.1371/journal.pcbi.1011462
- OpenSim: https://opensim.stanford.edu/
