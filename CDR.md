# CDR — Coherence-Driven Research

This document defines how cph runs coherence-driven research.

CDR is the discipline of continuously measuring whether the hypothesis, the methods, the evidence, and the project process still describe one system. It applies to research the way versioning, changelogs, and release gates apply to software.

The hypothesis under study is the Coherence Path Hypothesis — see [docs/concepts/coherence-path-hypothesis.md](docs/concepts/coherence-path-hypothesis.md). CDR governs how this repo argues about it.

## What CDR is

A way to run research by continuously measuring whether the hypothesis, methods, evidence, and process still describe one system.

Concretely, in this repo:

- **observation proposes** — qualitative description generates hypotheses
- **OpenCap translates** — video becomes biomechanical time series
- **AI / analysis sorts** — pattern extraction proposes structure
- **measurement decides** — features tested against gait-cycle data render the verdict
- **TSC measures the project itself** — the repo asks whether its own description is still coherent as the research changes

The four levels above run in order; later levels cannot license earlier ones. Measurement decides; observation does not.

## What CDR is not

- Not proof. Coherence is not truth.
- Not publication polish. CDR runs while the work is in progress, not at write-up time.
- Not a way to protect a theory. A coherent project may still need to abandon its hypothesis.
- Not a replacement for empirical validation. C_Σ does not stand in for an effect size.

## Research TSC axes

Triadic coherence is measured against three axes. Each axis names one way the project can fail to describe one system.

### α — Hypothesis pattern coherence

Does the project use stable terms and bounded definitions?

Specifically, do the terms `coherence path`, `support path`, `gait family`, `feature`, and `evidence` remain distinguishable across files? Drift between them is the failure mode this axis is designed to catch — for example, a file that calls a measured trace a "coherence path" without inference, or a file that calls the Coherence Path Hypothesis itself a "support path."

### β — Evidence relation coherence

Do methods, data, scripts, reports, and claims refer to the same object?

Specifically, does the README's empirical-state language match the latest merged field report? Do the analysis features named in [analysis/features.md](analysis/features.md) match the features the notebooks compute? Are conclusions supported by the actual measured surfaces, or by descriptions of them?

### γ — Process coherence

Can the project evolve through REVISE / GO / STOP transitions without losing identity?

Specifically, are gates explicit? Are status, changelog entries, and next actions named in their canonical files rather than improvised in commit messages? When a verdict changes, do the affected surfaces change together?

## C_Σ in this repo

C_Σ measures project coherence, not the truth of the Coherence Path Hypothesis.

A high C_Σ means the repo currently describes one coherent research project. It does **not** mean the hypothesis is correct.

A low C_Σ means the repo cannot be trusted to know whether the hypothesis is correct — terms drift, claims outrun their evidence, or process transitions have left surfaces stale. A low C_Σ blocks empirical claims until the project re-coheres.

Two failure modes follow from this distinction:

- **coherence laundering** — using a high C_Σ to support a substantive claim. The C_Σ score reports on the repo, not on the hypothesis.
- **coherence dismissal** — ignoring a low C_Σ on the grounds that "the data still looks fine." When the repo is incoherent, what counts as data is itself in question.

## Required cadence

Run TSC measurement after:

- README, [ROADMAP.md](ROADMAP.md), or hypothesis-doc changes
- field report changes
- empirical gate transitions (REVISE / GO / STOP)
- issue waves that alter project status
- any GO or STOP recommendation

TSC is run mechanically in this repo via [scripts/measure-coherence.sh](scripts/measure-coherence.sh) against the target manifests in [targets/](targets/). Hybrid mode (with LLM-aided assessment) is documented but not required.

## Changelog rule

Each meaningful research wave gets a [CHANGELOG.md](CHANGELOG.md) entry with:

- empirical state (REVISE / GO / STOP, or no-change with reason)
- α / β / γ / C_Σ if measured, or "pending — coh unavailable" if not
- bottleneck axis (which of α / β / γ is weakest)
- coherence delta (what moved since the prior entry)
- what changed (file-level summary, not commit summary)
- what remains unproven
- next gate (the next condition that must be met)

The changelog is a coherence ledger, not a release-note style log. It records whether the research project still describes one system, not which features shipped.
