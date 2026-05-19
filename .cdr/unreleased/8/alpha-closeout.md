# α Close-out: Protocol revision — Access mechanism subsection

**Cycle:** #8
**Merged:** d400153

## Cycle summary

Goal: codify the protocol gap surfaced by zeroth-pilot Pattern 1 — "permissive license is not the same as credentialless access" — into `protocols/existing-data-zeroth-pilot.md §Dataset Selection Rules`, broaden the wave-manifest escalation rule in `data/external/README.md`, and cross-link the broadened rule from `data/external/opencap-lab-validation.md §Acquisition status`. Result: 4 ACs met, 1 round, APPROVE. Two commits on cycle/8 (implementation + self-coherence); three doc files changed (+47 lines) plus one new self-coherence document. Patch is purely additive — the existing four selection rules and manifest fields all resolve unchanged under the grep oracle.

## Findings

### F1 — Author-choice surface required a rationale

AC2 gave the author choice between `data/external/README.md` and the protocol's `§Methodological Constraints` for the broadened escalation rule. Choice landed on the README. The self-coherence documented the rationale: the README is the wave-author surface (where escalation triggers are evaluated when staging a new external-data acquisition), while the protocol is the cycle-author surface. β surfaced the same observation independently — cross-confirmed. Pattern: when an issue treats two surfaces as equivalent, the author should still record the choice rationale, because the choice ages and the next maintainer needs to know which audience the section is targeted at.

### F2 — Tri-anchor cross-link grounded in empirical instance

The cross-link from `opencap-lab-validation.md §Acquisition status` to both the new protocol subsection and the README rule was grounded with the empirical instance ("OpenCap Lab Validation falls into the second category and is the empirical case that motivated the broadening"). This is a stronger shape than a bare "see X" because the link site itself instantiates the rule it cites. β surfaced the same pattern independently — cross-confirmed.

## Friction log

- AC2 surface choice (README vs protocol) took ~3 minutes of weighing audiences before settling. The decision held under β review.
- No friction on the protocol subsection itself — the three required topics from the issue body mapped cleanly onto three sub-headings (publicly-accessible definition, credential-gate examples + curl probe, operator-credential preconditions).

## Engineering level reading

L6: cross-surface coherence held (protocol ↔ README ↔ dataset manifest aligned on the broadened escalation rule). Pure additive — AC4 grep oracle held verbatim on β's side. L7 not pursued — no rewrite warranted.

## Patterns for the wave

Two patterns to carry into the wave close-out, both cross-confirmed by β:

1. **Wave-N close-out patterns landing as wave-(N+1) protocol patches.** This cycle is a textbook instance — zeroth-pilot's `cdd-protocol-gap` Pattern 1 became a 34-line protocol subsection one wave later. The wave → wave loop is doing real work.
2. **Tri-anchor cross-link grounded in the empirical instance** is a stronger shape than bare "see X". Worth lifting as a docs convention; not urgent.

Neither is a `cdd-*-gap` finding — both are process patterns observable from the closure itself.
