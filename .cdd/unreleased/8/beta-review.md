# β Review: Protocol revision — «Access mechanism» subsection

**Cycle:** #8
**Branch:** cycle/8 (head: a025af3)
**Base:** origin/main (c7a7fd8)
**Reviewer:** β

## Round 1 — Verdict: APPROVE

### Contract integrity

α HEAD commit author: `alpha@gait-support-paths.cdd.cnos` on both cycle/8 commits (`0079fb4`, `a025af3`). β identity will be used for the review commit, merge, and close-out. Working tree clean before review.

### AC-by-AC verification

- **AC1 — «Access mechanism» subsection added to protocol.** ✓ Met. `protocols/existing-data-zeroth-pilot.md` lines 27–59 add `### Access mechanism` nested under `## Dataset Selection Rules`. All three required topics are present and non-thin: (a) "publicly accessible" definition as a three-clause conjunction at lines 31–37 with the named term `licensed-permissive-but-gated` at line 38; (b) authentication / credential-gate examples at lines 40–46 plus the concrete unauthenticated-`curl` probe at line 48; (c) operator-supplied credential expectations as a three-clause precondition list at lines 52–55 with the escalation loop at line 57. The closing sentence at line 59 makes the AC's proof-plan oracle ("reader can answer 'is this acquireable?' before selection") directly answerable.

- **AC2 — Wave-manifest escalation rule broadened.** ✓ Met. `data/external/README.md` lines 46–55 add `## Wave-manifest escalation rule (external data)`. Both triggers are named (lines 50–51), are stated as "independently sufficient" (line 53), and the historical narrower form is called out explicitly (line 53). The README surface is the right call per the issue's "author's choice" — it scopes the rule to wave-manifest authors without forcing the protocol section to leak cross-cycle convention. Cross-link to protocol-side definition at line 55 prevents duplication-drift.

- **AC3 — Cross-link from manifest.** ✓ Met. `data/external/opencap-lab-validation.md` line 26 adds a single paragraph inside §Acquisition status with two anchor-style links: `protocols/existing-data-zeroth-pilot.md#access-mechanism` and `data/external/README.md#wave-manifest-escalation-rule-external-data`. Both anchor slugs match the new heading text (GitHub markdown slug rules: lowercase, hyphens for spaces, parens stripped). The link is grounded empirically — "OpenCap Lab Validation falls into the second category and is the empirical case that motivated the broadening" — rather than asserted abstractly.

- **AC4 — No regression (additive invariant).** ✓ Met. AC4 grep oracle reproduced:
  ```
  $ grep -n "Dataset Selection Rules\|Backup datasets\|Exclusion criteria\|Primary target" protocols/existing-data-zeroth-pilot.md
  11:## Dataset Selection Rules
  13:**Primary target:** OpenCap Lab Validation dataset from SimTK
  19:**Backup datasets:** Other validated OpenCap datasets with walking data if primary target is insufficient
  21:**Exclusion criteria:**
  57:If any of the three is missing, ... (see §Backup datasets above) ...
  ```
  All four pre-existing headings/fields resolve unchanged. The diff against `origin/main` for `protocols/existing-data-zeroth-pilot.md` is a pure 34-line insertion between line 26 and the prior `## Required Outputs`. No prior line is rewritten, deleted, or renamed. The `data/external/opencap-lab-validation.md §Selection-Rules Check` table (lines 80–87) still validates against the original four rules.

### Scope discipline

Files touched (per `git diff --name-only origin/main..cycle/8`):
- `protocols/existing-data-zeroth-pilot.md` — in AC1 surface.
- `data/external/README.md` — in AC2 surface.
- `data/external/opencap-lab-validation.md` — in AC3 surface.
- `.cdd/unreleased/8/self-coherence.md` — α process artifact.

Files NOT touched (issue non-goals + wave-manifest constraints):
- `requirements.txt` — wave manifest forbids modification. PASS.
- `docs/concepts/support-path.md` — issue non-goal (#9 territory). PASS.
- `analysis/features.md` — issue non-goal. PASS.
- `notebooks/*` and `scripts/*` — issue non-goal (#10 territory). PASS.
- `.cdd/waves/protocol-patches-2026-05-15/manifest.md` — δ surface. PASS.
- Prior cycles' `.cdd/unreleased/{5,6,7}/`. PASS.

No backup-dataset selection authored; no SimTK credentials acquired; no pipeline re-run attempted. Non-goals respected.

### cdd-*-gap findings

None. The cycle is a textbook docs-only patch that closes the loop on a previously-surfaced wave-level pattern (`cdd-protocol-gap` from the zeroth-pilot close-out Pattern 1). No new doctrine-level gaps emerge from the review.

### Notes / observations

- **Documentation hygiene observation (non-blocking):** The cross-link in `opencap-lab-validation.md` line 26 references both the protocol anchor and the README anchor; this is the right shape but creates three nodes (protocol, README, manifest) that must stay in slug-sync if any heading is renamed. α's self-coherence §Debt item 2 flags this. No action needed in this cycle; worth tracking if a markdown link checker is introduced later.
- **Light redundancy between README and protocol:** The README escalation rule and the protocol's §Access mechanism overlap on the "credentialled-but-permissive" framing. α flagged this in self-coherence §Debt item 4 and chose readability over single-source-of-truth. Defensible call for a docs-only cycle; flagging for awareness only.

### Cycle-level note for γ

Clean single-round APPROVE. No fix-rounds. The cycle is doctrinally tidy: it lifts a wave-level pattern (`cdd-protocol-gap`) into durable protocol/README text and grounds the cross-link with the empirical case. Pattern is reusable — future close-outs should expect similar wave-N patterns to land as small protocol patches in wave-(N+1).

### Merge instruction

```
git switch main && git pull origin main --ff-only
git -c user.name='β-as-agent' -c user.email='beta@gait-support-paths.cdd.cnos' \
    merge --no-ff cycle/8 -m 'Closes #8: Protocol revision — add «Access mechanism» subsection to existing-data zeroth pilot'
git push origin main
```

**Verdict: APPROVE.**
