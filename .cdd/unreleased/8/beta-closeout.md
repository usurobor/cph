# β Close-out: Protocol revision — «Access mechanism» subsection

**Cycle:** #8
**Review rounds:** 1
**Verdict:** APPROVE
**Merge:** d400153

## Review context

Single-round APPROVE. α's docs-only patch landed all four ACs cleanly and the self-coherence's AC4 grep oracle reproduced verbatim on β's side. No fix-rounds; no scope leaks; no doctrine-level gaps surfaced.

## Merge evidence

Merge commit: `d400153137e2f79a175e94ca909119f014fb23d5`
Merge message: `Closes #8: Protocol revision — add «Access mechanism» subsection to existing-data zeroth pilot`
Branch state: cycle/8 merged into main with `--no-ff` and pushed. Auto-close on `Closes #8` should fire at push receipt; γ to confirm at wave close.

## Summary of what merged

- `protocols/existing-data-zeroth-pilot.md` — new `### Access mechanism` subsection (34-line insertion, lines 27–59) nested under `## Dataset Selection Rules`. Covers three required topics: "publicly accessible" three-clause definition with the named `licensed-permissive-but-gated` term; credential-gate examples list plus the unauthenticated-`curl` probe; operator-credential preconditions plus the escalation loop. Closing sentence makes the proof-plan oracle directly answerable.
- `data/external/README.md` — new `## Wave-manifest escalation rule (external data)` section (10-line addition). Both triggers ("non-permissive license" / "access-mechanism gate") named as independently sufficient. Cross-links protocol-side definition rather than duplicating it.
- `data/external/opencap-lab-validation.md` — single cross-link paragraph in §Acquisition status. Anchors both the protocol subsection and the README rule. Grounds the cross-reference with the empirical case ("OpenCap Lab Validation falls into the second category and is the empirical case that motivated the broadening").
- `.cdd/unreleased/8/self-coherence.md` and `.cdd/unreleased/8/beta-review.md` — process artifacts.

## β-side observations / patterns worth carrying

- **Pattern: wave-N close-out patterns land as wave-(N+1) protocol patches.** This cycle is a textbook instance — zeroth-pilot's `cdd-protocol-gap` Pattern 1 became a 34-line protocol subsection one wave later. The wave-N → wave-(N+1) loop is doing real work. If the next wave-close yields more patterns of this shape (small, docs-only, anchored on a single named gap), the wave-manifest template could pre-allocate "patch cycles" by default. Not urgent.
- **Pattern: tri-anchor cross-link with empirical grounding.** α's cross-link in `opencap-lab-validation.md` line 26 names both the protocol anchor and the README anchor, and grounds the reference with the empirical instance ("falls into the second category"). This is a stronger shape than "see X" because the link site itself instantiates the rule. Worth lifting as a docs convention.
- **Pattern: README-vs-protocol surface choice was load-bearing.** AC2 explicitly gave α "author's choice" between two surfaces. α justified the README choice in self-coherence (wave-author audience vs cycle-author audience). The justification was tight; β did not need to second-guess. Issues that offer author-choice surfaces should require the author to record the choice rationale — this cycle modeled that well.
- **No `cdd-*-gap` findings.** The cycle is a clean closure of a prior wave's pattern with no new doctrine-level gaps surfaced. Empty findings list is the correct result here, not a sign of under-investigation.

## Process notes

- Three-cycle wave (cycle/8) executed under δ-as-agent dispatch. β identity (`beta@gait-support-paths.cdd.cnos`) used for review commit, merge commit, and this close-out. No `--no-verify`, `--amend`, or `git config` operations. All commits signed with `-c user.name`/`-c user.email`.
- Time budget: well under the 600s β cap.
- α-side scope discipline was strong — every issue non-goal was named in self-coherence §Self-check with the matching "not touched" assertion.
