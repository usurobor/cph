# cph

Coherence Path Hypothesis — testing whether walking contains recurring, measurable support-path primitives.

This repo tests the **Coherence Path Hypothesis**: during walking, an active viscoelastic body may rhythmically form temporary whole-body coordination paths around ground contact, and those paths may be inferred from recurring patterns in gait-cycle data.

This repo is the gait-domain empirical case for a broader coherence-object theory; the broader theory lives in [`usurobor/cog`](https://github.com/usurobor/cog).

It is also a model of **CDR — Coherence-Driven Research**: research run through explicit hypotheses, gates, field reports, a changelog, and continuous coherence measurement.

The hypothesis is not validated. Current merged status is **REVISE**. The README is the public charter; live operational state lives in [PROJECT.md](PROJECT.md), and the [source-of-truth table](#source-of-truth) at the foot of this file names the owning file for every other question.

---

*The body of this README is a dialogue between two voices working through the project. The project's method is "observation proposes, measurement decides"; the charter is written as inquiry so the form matches the work.*

---

A: You said "may" twice in the opening.

B: Twice on purpose. The hypothesis is not "the body does this." It is "if we look carefully at gait-cycle data, we should find recurring coordination structure that behaves the way temporary paths would behave." The body model is an interpretive frame. The evidence has to come from cycles.

A: So the repo is the hypothesis, a method for testing it, and a way of keeping the project coherent while it tests.

B: Three things in one repo. The README should hold them without confusing them.

---

A: Say the governing question once, plainly.

B: Can real walking data reveal stable, recurring low-level coordination primitives that explain visible walking patterns more precisely than coarse gait "types"?

A: "More precisely than" — you are not asking whether the types are wrong.

B: Correct. The types may be useful surface phrases. The question is whether they are built from something measurable underneath. If yes, "more precisely" follows. If no, the question dies cleanly.

---

A: The hypothesis has a name.

B: The Coherence Path Hypothesis. Stated tightly: during walking, each step may create a temporary whole-body coordination path around ground contact. The path is not an anatomical cord, not a fascia line, not a visible object. It is inferred — from how timing, stiffness, segment coupling, orientation, asymmetry, and condition response organize in gait-cycle data.

A: Then what is a "support path"? You use both terms.

B: Operational term. The hypothesis is the research claim. A support path is the gait-cycle pattern we try to infer from data. If we conflate them, the project loses the gap between claim and evidence.

A: That gap is the whole project.

B: That gap is the whole project.

---

A: The body model.

B: A human body is an active viscoelastic structured volume. Not a rigid machine, not a passive fluid. Bones give shape, muscles regulate force and stiffness, connective tissues transmit tension and state, the nervous system coordinates the whole volume in time.

A: And walking?

B: Foot touches the ground. Force enters. Some regions firm. Some yield. Some rotate. Some delay. Some release. For a moment the body becomes less blob-like — a path, a rail, a triangle, a spiral, some support geometry may organize the step. Then the next step. Then again.

A: So the hypothesis is a rhythm claim, not only an event claim.

B: Yes. If it is real, repeated walking video should not look like isolated poses. It should show a phase-locked coordination pattern across cycles. If it does not, either the pattern is finer than our instruments, or it is not there. Both are answers.

---

A: Why does any of this matter outside the lab?

B: The goal is not to put people into gait boxes. It is to find the low-level primitives that make walking signatures recognizable. If they are real, gait analysis could move from "this person is a Braced Axial Walker" to something like "under this condition, this gait shows early same-side path locking, high axial stiffness, low pelvis-rib differentiation, and reduced release before the next step."

A: A grammar instead of a label.

B: Yes. Movement teachers, clinicians, athletes, researchers, AI systems — all of them could discuss a composition rather than an identity. Not who the person is. Not a diagnosis. Not a personality. A measurable composition under known conditions.

---

A: What are the candidate primitives today?

B: Provisional, today nine. Contact anchor — where and when the step organizes around ground contact. Path direction — same-side, diagonal, posterior, axial, spiral, fragmented, multi-path. Stiffness profile — rise time, concentration, hold. Yield profile — ankle, knee, hip, pelvis, spine, trunk, distributed. Segment coupling — whole system or local parts. Phase timing — early, on time, late. Release or transfer — clean dissolution into the next step, or held. Side relation — shared grammar, or one side protecting, avoiding, shortening, overworking. Variability — stable, adaptive, rigid, noisy, context-sensitive.

A: Nine gives us a first testing surface.

B: Not final. If measurement collapses some or splits others, the list changes.

---

A: The seven gait families.

B: Observational vocabulary. The article names seven — Pendular Carrier, Elastic Rebounder, Braced Axial Walker, Collapse-and-Catch Walker, Spiral Driver, Segmented Block Mover, Asymmetric Protector. Rough names for things humans can notice before measurement. They are not the core theory.

A: Could they be composed from the primitives?

B: That is the working guess. Pendular Carrier may be stance-leg support with quiet transfer. Braced Axial may be early path locking with high axial stiffness and reduced rotational release. Spiral Driver may be diagonal recurrence with pelvis-rib-arm coupling. Asymmetric Protector may be a side-specific modifier rather than a family.

A: Seven is not sacred.

B: If measurement finds three, twelve, or none, the list changes. The hypothesis survives only if recurring primitives survive measurement.

---

## Relation to COG

CPH is the gait-specific empirical case for a broader project: **COG — Coherence Object Grammar**.

COG asks whether coherence itself can become an object domain: a world of support, jam, release, timing, transfer, rupture, fit, and whole-body continuity that can be named, perceived, measured, trained, or acted on.

CPH does not try to prove that whole theory. It tests the first measurable candidate inside one concrete domain: walking. In this repo, the candidate coherence object is the **support path**: one step, one side, one condition, one inferred recurring coordination pattern.

So CPH asks a narrower question:

> Can gait-cycle data reveal a coherent grammar of walking — low-level support-path primitives that explain visible gait signatures more precisely than coarse gait types?

The broader theory lives in [`usurobor/cog`](https://github.com/usurobor/cog). This repo remains focused on testing whether those primitives appear in walking data.

---

A: How is the hypothesis tested?

B: Existing data, not new recordings. OpenCap validation data, then gait-cycle segmentation, feature extraction, comparison across condition and side, attempted support-path inference, falsification table. Only then do we let AI or clustering near it.

A: Why that order?

B: OpenCap is the translation layer — video-derived movement into biomechanical time series. AI is not asked to classify people first. The first task is to find whether gait-cycle data contains stable recurring structures at all. Observation proposes. OpenCap translates. Analysis sorts. Measurement decides. TSC measures whether the project itself stays coherent while it does all that.

A: When AI is finally allowed in?

B: It should not preserve our labels by force. It should test whether the data contains primitives or clusters that make the labels unnecessary, sharper, or wrong.

---

A: What would count as evidence?

B: Measured gait-cycle structure. Repeatable timing patterns across cycles. Stable segment-coupling signatures. Consistent stance and swing phase relationships. Left-right differences that are systematic rather than random. Condition response — natural walking versus, say, trunk-sway walking. Agreement between OpenCap-derived features and reference motion-capture data where available. Future agreement with force, pressure, or EMG measures.

A: And what does not count?

B: A visible impression can propose a coherence path. It cannot establish one. A named gait family can propose a pattern. It cannot validate one. A high project coherence score can show that the repo is internally consistent. It cannot prove the body model true.

---

A: What would weaken or falsify it?

B: If real gait-cycle data does not show recurring coordination structure. Or if apparent structure is better explained by trial crop, marker artifact, camera setup, walking speed, subject morphology, condition labels alone, OpenCap error, observer bias, or overfitted feature choices.

A: And the response?

B: Not to rescue the hypothesis by inventing more poetic labels. If measurement destroys the vocabulary, the vocabulary goes.

---

A: Boundaries.

B: The repo is not a diagnostic system. It does not infer personality from walking. It does not claim that video can see fascia. It does not classify people as types.

A: The safe sentence.

B: "Under this condition, this recording shows this movement pattern." Not "this is who you are."

A: The data itself.

B: Gait video is identifiable biometric data. Raw participant video and private traces do not belong in the public repo. Ethics rules live in [`docs/ethics/`](docs/ethics/).

---

A: CDR. Why coherence at all?

B: Because a research project has to stay coherent while it changes. Hypothesis, methods, evidence, roadmap, reports, changelog — they should keep describing one system. TSC tracks three axes. Alpha: are the project's terms stable. Beta: do methods, evidence, and claims refer to the same object. Gamma: can the project move through GO, REVISE, STOP without losing identity. C_Σ measures project coherence. Not truth.

A: So a high C_Σ does not mean the hypothesis is right.

B: It means the repo currently describes one coherent research project. It says nothing about whether walking actually forms support paths. A low C_Σ means the repo cannot safely claim to know what it knows.

A: That is the move the field needs more of.

B: That is the move this repo is trying to model.

---

## Source of truth

Stable facts live once. Other files point to the owner.

| Question | Owning file |
|---|---|
| What is this project? | `README.md` |
| What is CDR? | `CDR.md` |
| What is the hypothesis? | `docs/concepts/coherence-path-hypothesis.md` |
| What is a support path? | `docs/concepts/support-path.md` |
| What is the unit of analysis? | `docs/concepts/gait-cycle-as-unit.md` |
| What are the failure conditions? | `docs/concepts/failure-conditions.md` |
| How do the seven families relate? | `docs/articles/seven-ways-people-walk.md` |
| What is the broader coherence-object theory? | [`usurobor/cog`](https://github.com/usurobor/cog) |
| Where are research gates tracked? | `ROADMAP.md` |
| What is the current operational status? | `PROJECT.md` |
| What changed over time? | `CHANGELOG.md` |
| What empirical evidence exists? | `reports/` |
| What TSC targets are measured? | `targets/` |
| How is data handled? | `docs/ethics/data-handling.md` |

## Where to go next

- Hypothesis: [`docs/concepts/coherence-path-hypothesis.md`](docs/concepts/coherence-path-hypothesis.md)
- Operational term: [`docs/concepts/support-path.md`](docs/concepts/support-path.md)
- Roadmap: [`ROADMAP.md`](ROADMAP.md)
- Current status: [`PROJECT.md`](PROJECT.md)
- Latest field report: [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md)
- Seven-family article: [`docs/articles/seven-ways-people-walk.md`](docs/articles/seven-ways-people-walk.md)
- CDR doctrine: [`CDR.md`](CDR.md)
- Ethics: [`docs/ethics/data-handling.md`](docs/ethics/data-handling.md)

## References

- OpenCap paper: https://doi.org/10.1371/journal.pcbi.1011462
- OpenCap Core: https://github.com/opencap-org/opencap-core
- OpenSim: https://opensim.stanford.edu/
