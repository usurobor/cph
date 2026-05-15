# α Close-out: Sub C — Inference memo + field report

**Cycle:** #7
**Merged:** a76b6d6

## Cycle summary

Goal: complete field report, generate ≥3 hypotheses, evaluate against 6 falsification conditions, record GO/NO-GO/REVISE decision, update PROJECT.md. Result: 6 ACs met, 1 round, APPROVE. REVISE decision recorded. Two files changed (field report, PROJECT.md).

## Findings

### F1 — "Not testable on smoke" framing

The honest framing of the 6-condition falsification table required marking 5 of 6 conditions as "Not testable" with smoke-status justification per hypothesis. This is *not* a falsification result — it is a result-not-yet-computable. The framing distinction matters because the protocol's NO-GO threshold (≥4 conditions trigger) would have mechanically passed (0 of 6 trigger on smoke), which would mis-license a GO decision. Pattern: when a falsification framework depends on empirical variation, executing it on by-construction-coherent data yields a misleading score. Surface: `docs/concepts/support-path.md §"Falsification Conditions for Existing-Data Zeroth Pilot"` — could carry a note that the falsification table requires real empirical data.

### F2 — REVISE vs NO-GO calibration

α first considered NO-GO. Re-read of protocol §"Go/No-Go Criteria":
- NO-GO requires segmentation <60%, extraction failure >30%, systematic reference disagreement, no discernible patterns, or multiple pipeline failures.
- None of those is met (smoke achieves 100% / 0% / N/A / N/A / no failures).
- REVISE is "Partial success requiring protocol or analysis adjustments" — which matches: methodology and pipeline are sound, the access-mechanism gap requires a protocol revision.

Pattern: decision-frameworks calibrated for the "data exists, run it" case can mis-fire on the "data acquisition itself is the gap" case. Surface: protocol §"Go/No-Go Criteria" could add a fourth axis for "preconditions met" (data acquired, pipeline runnable).

## Friction log

- The "0 of 6 conditions trigger" → would-be-GO mechanical misfire required 2 minutes of careful reading before the honest framing settled.
- The NO-GO vs REVISE call required 3 minutes of reading the protocol's threshold definitions.

## Engineering level reading

L6: cross-surface coherence held (field report ↔ PROJECT.md ↔ data manifest ↔ protocol all aligned on REVISE). L5 cleanly. L7 not pursued — though F1/F2 patterns above are L7 candidates for the next cycle.

## Patterns for the wave

Two of α's findings (F1 framing, F2 calibration) point at protocol-level gaps that surface only when data acquisition is itself the blocker. γ should triage these into wave-level next moves: a protocol revision cycle that adds an "Access mechanism" subsection AND clarifies the falsification table's empirical-data prerequisite.
