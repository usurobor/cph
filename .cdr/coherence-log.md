# Coherence log

Per-version coherence assessment for cph. Each entry tracks the project's
internal coherence — does the repo still describe one research system as it
changes? Empirical validation of the Coherence Path Hypothesis lives elsewhere
(`reports/` + the falsification table in `docs/concepts/support-path.md`);
this log is about the repo's internal consistency, not the hypothesis.

Coherence axes:

- **α — pattern coherence.** Do the project's terms (`coherence path`,
  `support path`, `gait family`, `feature`, `evidence`) stay distinguishable
  across files?
- **β — evidence-relation coherence.** Do methods, data, scripts, reports,
  and claims refer to the same object?
- **γ — process coherence.** Can the project evolve through REVISE / GO /
  STOP transitions without losing identity?

`C_Σ` is the aggregate score. When `coh` is on PATH, the entrypoint is
[`scripts/measure-coherence.sh`](../scripts/measure-coherence.sh) reading
targets in [`targets/`](../targets/). Until then, each axis is judged
qualitatively from human review.

## Ledger

| Version | Date | Empirical state | α | β | γ | C_Σ | Bottleneck | Notes |
|---|---|---|---|---|---|---|---|---|
| 0.2.0 | 2026-05-18 | REVISE | stable | stable | clean | pending — coh unavailable | none | Two coherence-drift sweeps closed (F1–F11). β code-first oracle anchoring discipline now durable practice. CDR archived as advertised doctrine; operational machinery preserved. |
| 0.1.0 | 2026-05-18 | REVISE | stable (first explicit α surface) | pending | clean | pending — coh unavailable | not measured | Initial charter/roadmap/changelog refactor. Originally tagged `0.1.0-cdr`. |

## How to read this log

A coherence score is **not empirical validation.** A high C_Σ means the repo
currently describes one coherent research project. It does not mean the
Coherence Path Hypothesis is correct. A low C_Σ means the repo cannot be
trusted to know whether the hypothesis is correct — terms have drifted,
claims have outrun their evidence, or process transitions have left surfaces
stale.

Two failure modes follow from this distinction:

- **coherence laundering** — treating a high C_Σ (or a clean feature table,
  or a clean clustering output) as substantive evidence for the hypothesis.
  The score reports on the repo, not on the hypothesis.
- **coherence dismissal** — ignoring a low C_Σ on the grounds that "the data
  still looks fine." When the repo is incoherent, what counts as data is
  itself in question.

## When to update this log

Add an entry after:

- a CHANGELOG.md version bump
- README, ROADMAP, or hypothesis-doc changes
- field-report changes
- empirical gate transitions (REVISE / GO / STOP)
- coherence-drift-sweep waves
- any GO or STOP recommendation

The log is operational. It is not advertised in the README's source-of-truth
table; readers find it by reading the repo's contents (it lives at
`.cdr/coherence-log.md`, one of two top-level files inside `.cdr/`).
