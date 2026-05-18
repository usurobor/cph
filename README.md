# gait-support-paths

This repo tests the **Coherence Path Hypothesis**: during walking, an active viscoelastic body may rhythmically form temporary whole-body coordination paths around ground contact, and those paths may be inferred from recurring patterns in gait-cycle data.

The project is also a model of **CDR — Coherence-Driven Research**: research run through explicit hypotheses, gates, field reports, changelogs, and continuous coherence measurement.

## Governing question

Can real walking data reveal stable, recurring low-level coordination primitives that explain visible walking patterns more precisely than coarse gait "types"?

## The hypothesis

The **Coherence Path Hypothesis** says:

> During walking, each step may create a temporary whole-body coordination path around ground contact. This path is not a literal anatomical cord, fascia line, or visible object. It is inferred from how timing, stiffness, segment coupling, orientation, asymmetry, and condition response organize in gait-cycle data.

The repo uses **support path** as the operational term for the measurable surface of this idea.

```text
Coherence Path Hypothesis = the research claim
support path              = the operationalized gait-cycle pattern
```

The distinction matters. The hypothesis is the thing being tested. A support path is the pattern we try to infer from data.

Full definition: [docs/concepts/coherence-path-hypothesis.md](docs/concepts/coherence-path-hypothesis.md)
Operational term: [docs/concepts/support-path.md](docs/concepts/support-path.md)

## The body model

The working model is simple and strict.

A human body is an active viscoelastic structured volume. It is not a rigid machine, and it is not a passive fluid. Bones give shape. Muscles regulate force and stiffness. Connective tissues transmit tension and state. The nervous system coordinates the whole volume in time.

When the foot touches the ground, force enters the system. Some regions firm. Some yield. Some rotate. Some delay. Some release. For a moment, the body becomes less blob-like: a temporary path, rail, triangle, spiral, or support geometry may organize the step.

Walking repeats this event.

So the hypothesis is not only an event claim. It is a rhythm claim:

```
foot contact
→ coherence path forms
→ body moves around it
→ path releases or transfers
→ next contact
→ path forms again
```

If the hypothesis is true, repeated walking video should not show only isolated poses or single steps. It should show a stable, phase-locked coordination pattern across gait cycles.

## Why this matters

The goal is not to assign people to gait types.

The goal is to discover the low-level primitives that make walking signatures recognizable.

The seven visible gait families from the article are coarse surface phrases. The Coherence Path Hypothesis asks whether those phrases are built from lower-level primitives: contact timing, path direction, stiffness profile, yield profile, segment coupling, phase timing, release, side relation, and variability.

If supported, gait analysis could move from this:

> This person is a Braced Axial Walker.

to this:

> Under this condition, this gait shows early same-side path locking,
> high axial stiffness, low pelvis-rib differentiation,
> and reduced release before the next step.

That would matter because it could give movement teachers, clinicians, athletes, researchers, and AI systems a better object to discuss:

- not identity
- not diagnosis
- not personality
- not visual vibe
- but a measurable movement composition

The practical hope is a grammar of walking: a way to express any walking signature as a composition of primitives rather than forcing it into a type box.

## The primitive layer

The current candidate primitive set is provisional.

A walking signature may be composed from primitives such as:

| Primitive | Question it asks |
|---|---|
| Contact anchor | Where and when does the step organize around ground contact? |
| Path direction | Does organization run same-side, diagonal, posterior, axial, spiral, fragmented, or multi-path? |
| Stiffness profile | How quickly does stiffness rise, where does it concentrate, and how long does it hold? |
| Yield profile | Where does the body absorb load: ankle, knee, hip, pelvis, spine, trunk, or distributed? |
| Segment coupling | Do foot, leg, pelvis, ribs, arms, spine, and head coordinate as one system or local parts? |
| Phase timing | Do stabilization, rotation, push-off, and transfer happen early, on time, or late? |
| Release / transfer | Does the path dissolve cleanly into the next step or remain held? |
| Side relation | Do left and right share a grammar, or does one side protect, avoid, shorten, or overwork? |
| Variability | Is the pattern stable, adaptive, rigid, noisy, or context-sensitive? |

The project does not claim this primitive list is final. It exists to make the hypothesis testable.

## Connection to the seven gait families

The article [docs/articles/seven-ways-people-walk.md](docs/articles/seven-ways-people-walk.md) names seven visible walking families:

- Pendular Carrier
- Elastic Rebounder
- Braced Axial Walker
- Collapse-and-Catch Walker
- Spiral Driver
- Segmented Block Mover
- Asymmetric Protector

Those families are not the core theory.

They are observational vocabulary: rough names for patterns humans can notice before measurement. The Coherence Path Hypothesis is the deeper claim that those visible shapes may be composed from recurring support-path primitives.

| Visible family | Possible primitive story |
|---|---|
| Pendular Carrier | stance-leg support, quiet transfer, low-noise travel over the foot |
| Elastic Rebounder | compression and return, clean release, spring-like timing |
| Braced Axial Walker | early path locking, high axial stiffness, reduced rotational release |
| Collapse-and-Catch Walker | delayed path formation, early drop, late stabilization |
| Spiral Driver | diagonal recurrence, pelvis-rib-arm coupling, rotational transfer |
| Segmented Block Mover | poor inter-segment coupling, local control, broken wave |
| Asymmetric Protector | side-specific path availability; possibly a modifier, not a family |

The number seven is not sacred.

If measurement finds three families, twelve families, or no stable families, the list changes. The hypothesis survives only if recurring coordination primitives survive measurement.

## How the project tests the hypothesis

The project starts with existing data, not new human recordings.

Current empirical route:

```
existing OpenCap validation data
→ gait-cycle segmentation
→ feature extraction
→ condition and side comparison
→ support-path inference
→ falsification table
→ only then AI / clustering
```

OpenCap is the translation layer. It turns video-derived movement into biomechanical time series. AI is not asked to classify people first. The first task is to find whether gait-cycle data contains stable recurring structures.

The working sequence is:

- **Observation proposes.**
- **OpenCap translates.**
- **Analysis sorts.**
- **Measurement decides.**
- **TSC measures whether the project itself remains coherent.**

AI classification comes later. It should not preserve our labels by force. It should test whether the data contains primitives or clusters that make the labels unnecessary, sharper, or wrong.

## Current empirical state

The hypothesis is not validated.

Current merged status is **REVISE**. The OpenCap Lab Validation archive has been acquired and processed. The OpenCap-vs-reference comparison passed strongly on the current archive, but the project has not yet shown that coherence paths recur as stable, interpretable gait-cycle structures.

The live operational state lives in [PROJECT.md](PROJECT.md).
The latest empirical evidence lives in [reports/field-report-01-existing-data-zeroth-pilot.md](reports/field-report-01-existing-data-zeroth-pilot.md).
The durable feature summary lives in [analysis/feature-summary-zeroth-pilot.md](analysis/feature-summary-zeroth-pilot.md).

Do not infer current status from this README if those files disagree. The status files own status.

## What would count as evidence

Evidence for the hypothesis must come from measured gait-cycle structure.

Possible evidence:

- repeatable timing patterns across cycles
- stable segment-coupling signatures
- consistent stance / swing / phase relationships
- pelvis-trunk or hip-knee-ankle coordination patterns
- left-right differences that are systematic rather than random
- condition response, such as natural walking versus trunk-sway walking
- agreement between OpenCap-derived features and reference motion-capture data where available
- future agreement with force, pressure, or EMG measures where available

A visible impression can propose a coherence path. It cannot establish one.

A named gait family can propose a pattern. It cannot validate the pattern.

A high project coherence score can show that the repo is internally coherent. It cannot prove the body model true.

## What would weaken or falsify the hypothesis

The hypothesis weakens if real gait-cycle data does not show recurring coordination structure.

It also weakens if apparent structure is better explained by:

- trial crop
- marker artifact
- camera setup
- walking speed
- subject morphology
- condition labels alone
- OpenCap error
- observer bias
- overfitted feature choices

The project should not rescue the hypothesis by inventing more poetic labels.

If measurement destroys the current vocabulary, the vocabulary goes.

## Boundaries

This repo is not a diagnostic system.

It does not infer personality from walking.

It does not claim that video can see fascia.

It does not claim that the seven gait families are proven.

It does not classify people as types.

The safe sentence is:

> Under this condition, this recording shows this movement pattern.

Not:

> This is who you are.

Gait video is identifiable biometric data. Raw participant video and private traces do not belong in the public repo. Ethics rules live in [docs/ethics/](docs/ethics/).

## CDR: coherence-driven research

This repo is intended to become a model cnos.cdr project.

CDR treats a research project as something that must remain coherent while it changes. The hypothesis, methods, evidence, roadmap, reports, and changelog should keep describing one system.

TSC coherence measurement tracks three axes:

| Axis | Research meaning |
|---|---|
| α — pattern coherence | Are the project's terms stable? |
| β — relation coherence | Do methods, evidence, and claims refer to the same object? |
| γ — process coherence | Can the project move through GO / REVISE / STOP without losing identity? |

C_Σ measures project coherence, not truth.

A high C_Σ means the repo currently describes one coherent research project. It does not mean the Coherence Path Hypothesis is correct. A low C_Σ means the repo cannot safely claim to know whether the hypothesis is correct.

- CDR doctrine: [CDR.md](CDR.md)
- Research gates: [ROADMAP.md](ROADMAP.md)
- Coherence ledger: [CHANGELOG.md](CHANGELOG.md)
- TSC targets: [targets/](targets/)
- Measurement entrypoint: [scripts/measure-coherence.sh](scripts/measure-coherence.sh)

## Source of truth

| Question | Owning file |
|---|---|
| What is this project? | `README.md` |
| What is CDR? | `CDR.md` |
| What is the hypothesis? | `docs/concepts/coherence-path-hypothesis.md` |
| What is a support path? | `docs/concepts/support-path.md` |
| What is the unit of analysis? | `docs/concepts/gait-cycle-as-unit.md` |
| What are the failure conditions? | `docs/concepts/failure-conditions.md` |
| How do the seven families relate? | `docs/articles/seven-ways-people-walk.md` |
| Where are research gates tracked? | `ROADMAP.md` |
| What is the current operational status? | `PROJECT.md` |
| What changed over time? | `CHANGELOG.md` |
| What empirical evidence exists? | `reports/` |
| What TSC targets are measured? | `targets/` |
| How is data handled? | `docs/ethics/data-handling.md` |

Stable facts should live once. Other files should point to the owner.

## Where to go next

Start here:

- Hypothesis: [docs/concepts/coherence-path-hypothesis.md](docs/concepts/coherence-path-hypothesis.md)
- Operational term: [docs/concepts/support-path.md](docs/concepts/support-path.md)
- Roadmap: [ROADMAP.md](ROADMAP.md)
- Current status: [PROJECT.md](PROJECT.md)
- Latest field report: [reports/field-report-01-existing-data-zeroth-pilot.md](reports/field-report-01-existing-data-zeroth-pilot.md)
- Seven-family article: [docs/articles/seven-ways-people-walk.md](docs/articles/seven-ways-people-walk.md)
- CDR doctrine: [CDR.md](CDR.md)
- Ethics: [docs/ethics/data-handling.md](docs/ethics/data-handling.md)

## References

- OpenCap paper: https://doi.org/10.1371/journal.pcbi.1011462
- OpenCap Core: https://github.com/opencap-org/opencap-core
- OpenSim: https://opensim.stanford.edu/
