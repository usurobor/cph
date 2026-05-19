# α Close-out: Concept patch — falsification empirical-data preamble

**Cycle:** #9
**Merged:** bfe531c

## Cycle summary

Goal: lift α #7's in-cycle distinction between "not testable" (deferred verdict) and "not triggered" (positive empirical claim) from the field-report instance into the concept doc itself, so the falsification table reads correctly when applied to any future synthetic / by-construction dataset. Result: 4 ACs met, 1 round, APPROVE. One commit on cycle/9 (implementation + self-coherence bundled), two files changed: an 11-line preamble + 1-line threshold refinement in `docs/concepts/support-path.md`, plus a new self-coherence document.

AC3 was a justified no-op: the filed field report (`reports/field-report-01-existing-data-zeroth-pilot.md` §Falsification Assessment) already uses the "Not testable" framing correctly at lines 155–166, so the AC's gating clause ("if it would mechanically miscount") does not fire. β independently re-verified this judgement.

## Findings

### F1 — Conditional ACs work when the gating clause is named explicitly

AC3 was structured as "if the field-report template would mechanically miscount, add a reminder; otherwise no-op." The explicit "if" gate let the cycle close with a justified no-op rather than a fabricated edit. Pattern: conditional ACs with a clearly-stated gating clause prevent the "I have to touch this file to satisfy the AC" pressure that would otherwise dilute scope discipline. Worth carrying as a wave-level finding — issue authors should write conditional ACs with the trigger condition foregrounded.

### F2 — Condition-5 carve-out was an unrequested but load-bearing addition

The preamble names *five* of the six conditions as testing for absence of empirical variation (1, 2, 3, 4, 6). Condition 5 — "Patterns are observer-effects rather than participant-effects" — is testable on synthetic data because by-construction kinematics ARE observer-effects (the simulator IS the observer). Without the carve-out, a reader would either: (a) include condition 5 as "not testable" wrongly, or (b) deduce the asymmetry on their own without textual support. The carve-out at line 105 closes that gap with one sentence. Not strictly required by the issue's AC1 wording but required for the preamble to be self-consistent under careful reading. β identified the same call as "load-bearing" independently.

## Friction log

- Numbering the five "absence-of-variation" conditions (1, 2, 3, 4, 6) required cross-referencing each condition's text — a slow read but well below the 600s budget.
- The Condition-5 carve-out wording took two passes — first draft was preachy; second draft scopes it tightly to "by construction is observer-effects."

## Engineering level reading

L6: cross-surface coherence held (concept doc ↔ field-report verdict framing ↔ protocol's GO/NO-GO logic all aligned on the empirical-vs-deferred distinction). Pure additive within `docs/concepts/support-path.md` — AC4 grep oracle held verbatim, body paragraphs byte-identical. L7 not pursued; the construct itself is unchanged, only the application-rule framing for falsification.

## Patterns for the wave

Three patterns worth carrying to wave close-out:

1. **Conditional ACs with foregrounded gating clauses preserve scope discipline.** AC3's "if it would mechanically miscount" let the cycle close honestly without fabricating an edit. Issue authors should adopt this pattern when an AC's relevance depends on a checkable upstream condition.
2. **Load-bearing carve-outs.** F2 (condition-5 exception) is an unrequested but necessary clarification — a tight one-sentence addition that prevents reader confusion. Worth flagging as a class of edit that doesn't appear in ACs but matters for self-consistency.
3. **Concept-doc patches as upstream lifts of field-report reasoning.** This cycle is the second wave-N → wave-(N+1) instance: an in-cycle reasoning move (α #7's "not testable" framing) became a permanent concept-doc subsection one wave later. Cross-confirms cycle #8's wave-loop pattern.

No `cdd-*-gap` (doctrine-level) findings. The only doctrine-level candidate — upstream lift of this preamble into cnos.cdd's skill bundle — is explicitly a Non-goal per the issue and remains an operator decision.
