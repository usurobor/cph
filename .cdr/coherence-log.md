# Coherence log

Per-version coherence assessment for cph. Update on each release.

> **⚠ Stream-A scaffolding caveat (applies to 0.3.0 onward).** Empirical-state columns below for 0.3.0/0.3.1/0.3.2/0.4.0/0.4.1 reflect Stream-A (engineering) dev-work cycles run without the OpenCap data archive mounted in the dispatch container. The α/β/γ coherence-axis assessments (`stable` / `clean`) apply to the *project's internal coherence as a research repo* — the question this log was designed to answer — not to the empirical claims attached to each version. Those empirical claims are scaffolding pending Stream-B validation; see [CHANGELOG.md](../CHANGELOG.md) caveat for the full statement.

| Version | Date | Empirical state | α | β | γ | C_Σ | Bottleneck | Notes |
|---|---|---|---|---|---|---|---|---|
| 0.3.2 | 2026-05-19 | GO with bounded scope (R1) | stable | stable | clean | pending | partial-clip L cycles (inference layer) | cph#28 contralateral-anchored L-cycle inference; 57/60 L cycles recovered (95%); R1 transitions REVISE → GO with bounded scope. `detection_method` column distinguishes measured from inferred surfaces. |
| 0.3.1 | 2026-05-19 | partial GO on R3 (R-side) | stable | stable | clean | pending | R-side-only test surface | cph#27 R-side aggregate analysis (10 subjects × 2 conditions × 25 features). 7 BH-significant condition responses including textbook-magnitude lumbar bending increase (r_rb = +1.0, all 10 subjects). Three candidate support-path hypotheses surfaced. |
| 0.3.0 | 2026-05-19 | REVISE (bilateral half-anchored) | stable | stable | clean | pending | L-side cycle yield (source-archive cropping) | cph#26 R2 segmentation fix ported; real-data detector at 60/60 R-side; bilateral construct half-anchored at L=1. |
| 0.2.0 | 2026-05-18 | REVISE | stable | stable | clean | pending | none | Two coherence-drift sweeps closed (cph#16, cph#21). β code-first oracle anchoring is durable practice. |
| 0.1.0 | 2026-05-18 | REVISE | stable | pending | clean | pending | not measured | Initial charter: README, hypothesis doc, support-path doc, failure-conditions doc, ROADMAP. |

## When to update

After a CHANGELOG version bump, README / ROADMAP / hypothesis-doc changes, field-report changes, empirical gate transitions, or coherence-drift-sweep waves.

Scores are operational. They are not advertised in the README source-of-truth table.

## On `C_Σ = pending`

CI workflow at `.github/workflows/coherence.yml` triggers on tag push (`X.Y.Z` or `vX.Y.Z`); the `coh` binary installs from the latest release of the source repo and runs mechanical mode against the targets registered in `targets/registry.tsc`. The first numeric `C_Σ` baseline lands when the workflow runs on a tagged release; until then, the qualitative α/β/γ assessment above is the operational record.
