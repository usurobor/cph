<!-- sections: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness] -->
<!-- completed: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness] -->

# Self-Coherence: Protocol revision — «Access mechanism» subsection

**Issue:** #8
**Mode:** docs-only
**Branch:** cycle/8
**Author:** α

## Gap

The zeroth-pilot wave (`.cdd/waves/zeroth-pilot-2026-05-15/wave-closeout.md` §"Pattern 1 — Open license vs gated access mechanism") surfaced a divergence between the protocol's selection rules and the project's empirical experience:

- `protocols/existing-data-zeroth-pilot.md §Dataset Selection Rules` lists four rules, all of which are license-shaped — "clear licensing terms" appears, but access channel does not.
- `data/external/opencap-lab-validation.md §Acquisition status` documents the load-bearing case: a dataset (OpenCap Lab Validation) that passes all four selection rules (Apache 2.0, multi-condition walking, reference measurements, multi-subject) yet cannot be downloaded in a credentialless sandbox because SimTK requires an authenticated session.
- The wave's manifest escalation rule was framed as "non-permissive license → escalate," which does not match the failure mode (permissive license + gated access mechanism).

A reader of the protocol alone could not have predicted the acquisition failure; the failure mode was only visible from the manifest. The patch closes the loop on the protocol side, broadens the wave-manifest convention, and cross-links the empirical case.

## Skills

- **Tier 1:** `cdd/CDD.md`, `cdd/SKILL.md`, `cdd/alpha/SKILL.md`.
- **Tier 2:** `eng/writing` (durable docs — protocol section is a durable artifact that future cycles cite).
- **Tier 3:** none explicit. Operative constraint: the wave manifest's "additive only" rule (AC4) — existing selection rules must not be deleted or rewritten, only extended.

## ACs

### AC1 — «Access mechanism» subsection added to protocol

**Evidence:** `protocols/existing-data-zeroth-pilot.md` gains a new `### Access mechanism` subsection at lines 27–59, nested under `## Dataset Selection Rules` (line 11) and immediately after the existing Exclusion criteria block (lines 21–25). The subsection covers all three required topics named in AC1:

- **Authentication / credential gates** — explicit list at lines 40–46 (SimTK, Figshare-private, OSF-private, Synapse, PhysioNet credentialed tier, OpenCap API tokens, click-through DUAs, IRB-style restricted tiers, captcha walls) plus a concrete unauthenticated-`curl` probe at line 48.
- **What counts as "publicly accessible" in this project's sense** — three-clause definition at lines 31–37, with the named term "licensed-permissive-but-gated" at line 38 for the partial-coverage case.
- **Operator-supplied credential expectations** — three-clause precondition list at lines 52–55, plus the escalation loop (one-line manifest note + wave escalation log entry) at line 57.

**Oracle:** the issue's "Proof plan" — a reader following the protocol can answer "is this dataset acquireable in our environment?" before selection without reading the manifest. The closing sentence at line 59 makes this answerable directly. AC met.

### AC2 — Wave-manifest escalation rule broadened

**Evidence:** Per the issue's "author's choice" between `data/external/README.md` and the protocol's §Methodological Constraints, I chose `data/external/README.md` — the README is the canonical surface for "rules that apply to wave manifests consuming external data," and putting the rule there keeps the protocol section's focus on per-dataset selection rather than on cross-cycle wave conventions.

`data/external/README.md` lines 46–55 add a new `## Wave-manifest escalation rule (external data)` section that:

- Names both triggers (non-permissive license OR access-mechanism gate requiring unsupplied credentials) at lines 50–51.
- States explicitly that "Both conditions are independently sufficient triggers" and that the historical convention was the narrower form (line 53).
- Cross-links the protocol-side definition (line 55) so the README does not duplicate the protocol's "publicly accessible" criteria, only the wave-side escalation rule.

**Oracle:** the wave manifest at `.cdd/waves/protocol-patches-2026-05-15/manifest.md` §"Known constraints" already cites this broadened rule prospectively (line 35); the README now backs the citation. AC met.

### AC3 — Cross-link from manifest

**Evidence:** `data/external/opencap-lab-validation.md` line 26 adds a single paragraph inside §Acquisition status that links to both:

- `protocols/existing-data-zeroth-pilot.md §Dataset Selection Rules → Access mechanism` (the protocol-side definition), and
- `data/external/README.md §Wave-manifest escalation rule` (the wave-side rule).

The link is anchored on the empirical case: "OpenCap Lab Validation falls into the second category and is the empirical case that motivated the broadening." This grounds the cross-reference in evidence rather than asserting it abstractly.

**Oracle:** the issue's AC3 surface — "`data/external/opencap-lab-validation.md §Acquisition status` references the new protocol subsection by anchor." The anchor `#access-mechanism` resolves against the new `### Access mechanism` heading. AC met.

### AC4 — No regression

**Evidence:** All existing selection-rule structure is preserved:

```
$ grep -n "Dataset Selection Rules\|Backup datasets\|Exclusion criteria\|Primary target" \
    protocols/existing-data-zeroth-pilot.md
11:## Dataset Selection Rules
13:**Primary target:** OpenCap Lab Validation dataset from SimTK
19:**Backup datasets:** Other validated OpenCap datasets with walking data if primary target is insufficient
21:**Exclusion criteria:**
57:If any of the three is missing, the candidate must be **escalated to the wave operator** ... (see §Backup datasets above) ...
```

The four headings + `Primary target` field + `Backup datasets` field + `Exclusion criteria` field all resolve unchanged. The new §Access mechanism is purely additive — inserted between the existing §Dataset Selection Rules block and §Required Outputs, with no rewrite of any prior line.

The manifest's "Selection-Rules Check" table at `data/external/opencap-lab-validation.md` lines 80–87 continues to validate against the four original rules without change; the new access-mechanism material is separately documented in §Acquisition status (where it already lived) plus the new cross-link.

**Oracle:** the issue's AC4 — "existing selection rules and manifest fields remain valid; this is additive." AC met.

## Self-check

α-side audit: did α push ambiguity onto β?

- **AC1**: the subsection covers all three named topics with explicit lists and a concrete probe; β can verify by reading each of the three bolded sub-headings and confirming the issue's requirements are addressed.
- **AC2**: the README surface was chosen and the choice is justified above; β can spot-check that the rule is named in the README, not orphaned in a different file.
- **AC3**: the cross-link is a single paragraph in the manifest with two named anchors; β can verify by clicking each anchor (or by running a markdown link-checker).
- **AC4**: the grep oracle is explicit in this file and reproducible.

Did α outsource authoring work to β? No — the patch is self-contained and the wave manifest's prospective citation of the broadened rule is now backed by an actual README section.

Is every claim backed by evidence in the diff?
- Each AC has a line-range citation in the modified file.
- The grep oracle output is reproducible.
- The cross-links are concrete (anchor names match heading text).

Scope discipline. Files explicitly NOT touched:

- `requirements.txt` — manifest forbids modification.
- `analysis/features.md` — issue non-goal.
- `docs/concepts/support-path.md` — issue non-goal (and #9's territory).
- `notebooks/*` and `scripts/*` — issue non-goal (and #10's territory).
- Any prior cycle's `.cdd/unreleased/{5,6,7}/` files — cross-wave boundary.
- The wave manifest at `.cdd/waves/protocol-patches-2026-05-15/manifest.md` — δ's surface, not α's.
- Backup-dataset selection / SimTK credential acquisition / pipeline re-run — explicitly named non-goals.

## Debt

1. **Wave-manifest template not updated.** The broadened escalation rule is now documented in `data/external/README.md`, but the canonical wave-manifest template (if one exists at the `cnos` level — `.cdd/waves/...` is per-wave, not templated) is unchanged. Future waves will need to cite the README anchor; this is a workflow expectation, not a protocol gap. Carry to a future tooling cycle if a manifest template is introduced upstream.

2. **No automated link check.** The cross-links between the three files use GitHub-style markdown anchors. They were authored by hand and validated by inspection (heading text → expected anchor slug). A repo-level markdown link checker would catch drift if any heading is renamed. Not in scope for this cycle.

3. **"Open access mechanism" probe is descriptive, not enforced.** The `curl -L -o /dev/null` probe at line 48 is documentation, not a CI gate. A future cycle could codify it as a pre-acquisition script that runs against any candidate dataset URL before selection is finalized; that script would live alongside `scripts/io_opencap.py`. Out of scope for #8.

4. **The README's escalation rule and the protocol's «Access mechanism» subsection partially overlap.** The README mentions "non-permissive license OR access-mechanism gate" as triggers; the protocol's subsection covers the access-mechanism side in detail. The README points to the protocol for definitions, so the duplication is bounded. If a future revision wants single-source-of-truth, the README rule could be shortened to a pure link; for now the inline rule is slightly redundant but readable on its own.

## CDD-Trace

| Step | Artifact | Skills loaded | Decision |
|------|----------|---------------|----------|
| 0 Observe | — | — | Read issue #8, manifest, wave close-out §Pattern 1, all three target files |
| 1 Select | — | — | Gap: protocol lists license rules but not access mechanism; manifest documents the empirical failure |
| 2 Branch | cycle/8 | cdd | δ created from origin/main; α landed via `git switch cycle/8` |
| 3 Bootstrap | n/a | cdd | Not required — docs-only cycle |
| 4 Gap | self-coherence §Gap | — | Add §Access mechanism to protocol; broaden README escalation rule; cross-link from manifest |
| 5 Mode | self-coherence §Skills | cdd, eng/writing | docs-only |
| 6 Artifacts | `protocols/existing-data-zeroth-pilot.md` (added §Access mechanism); `data/external/README.md` (added §Wave-manifest escalation rule); `data/external/opencap-lab-validation.md` (added cross-link paragraph in §Acquisition status) | eng/writing | Three files changed; all additive |
| 7 Self-coherence | self-coherence.md | cdd | This file |
| 7a Pre-review | self-coherence.md §Review-readiness | cdd | 4 ACs evidenced; additive-only invariant held; scope discipline documented |

## Review-readiness

Round 1. Cycle branch base SHA: `c7a7fd8` (origin/main + δ scaffold at branch creation). Three files changed plus this self-coherence:

- `protocols/existing-data-zeroth-pilot.md` — `### Access mechanism` subsection added (lines 27–59).
- `data/external/README.md` — `## Wave-manifest escalation rule (external data)` section added (lines 46–55).
- `data/external/opencap-lab-validation.md` — cross-link paragraph added inside §Acquisition status (line 26).
- `.cdd/unreleased/8/self-coherence.md` — this file.

All four ACs have evidence in the diff. Existing selection-rule structure is preserved (AC4 grep oracle holds). Ready for β.

**Specific β decision points:**
1. Is the «Access mechanism» subsection's three-part structure (publicly-accessible definition / credential-gate list / operator expectations) faithful to the AC1 requirement, or is one of the three thin?
2. Is the README the right surface for AC2 (vs the protocol's §Methodological Constraints)?
3. Are the cross-link anchors stable (heading text vs anchor slug match)?
4. Is the additive-only invariant held (AC4 grep oracle reproducible)?
