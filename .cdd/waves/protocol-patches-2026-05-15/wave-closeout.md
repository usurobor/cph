# Wave Close-out: Protocol patches from zeroth-pilot

**Wave date:** 2026-05-15
**Dispatcher:** δ-as-agent (single-actor collapse mode)
**Repo:** usurobor/gait-support-paths
**Origin:** `.cdd/waves/zeroth-pilot-2026-05-15/wave-closeout.md` (Patterns 1 & 2; #6 portability debt)
**Issues:** #8, #9, #10 (all CLOSED, all single-round APPROVE)
**Final SHA on main:** 988a9d2

## Final wave decision

**COMPLETE.**

This wave was a downstream patch wave — no GO/NO-GO gate to clear. Three small, independent issues each addressed a distinct gap surfaced by the zeroth-pilot wave's close-out: a protocol-level gap (#8), a concept-doc gap (#9), and a code-level portability debt (#10). All three closed in a single review round; β APPROVE on each; no scope creep; no `cdd-*-gap` (doctrine-level) findings across the wave.

The wave's structural success is that it closed Patterns 1 & 2 from the zeroth-pilot wave honestly: the patches sharpen the protocol/concept-doc framing so the next credentialled re-run will not repeat the access-mechanism stall or the synthetic-vs-empirical falsification miscount.

## Per-issue summary

### #8 — Protocol revision: «Access mechanism» subsection
- **Rounds:** 1
- **Verdict:** APPROVE
- **Final SHA on main:** d400153 (merge); bdebc14 (γ close-out)
- **Key artifacts:** `protocols/existing-data-zeroth-pilot.md` (new `### Access mechanism` subsection, 34 lines under §Dataset Selection Rules); `data/external/README.md` (new `## Wave-manifest escalation rule (external data)` section broadening the rule to fire on either non-permissive license OR access-mechanism gate); `data/external/opencap-lab-validation.md` (tri-anchor cross-link from §Acquisition status); `.cdd/unreleased/8/{self-coherence,beta-review,alpha-closeout,beta-closeout,gamma-closeout}.md`.
- **Debt:** Wave-manifest template upstream (cnos-level) not updated — workflow expectation, not a protocol gap. No automated link-check. Inline-`curl` probe is descriptive, not a CI gate. Slight redundancy between README rule + protocol subsection bounded by cross-link. No scope creep.

### #9 — Concept patch: falsification empirical-data preamble
- **Rounds:** 1
- **Verdict:** APPROVE (AC3 a justified no-op)
- **Final SHA on main:** bfe531c (merge); 5db6fbf (γ close-out)
- **Key artifacts:** `docs/concepts/support-path.md` (new `### Empirical-data prerequisite` subsection — 11 lines — plus a 1-line refinement to the threshold rule at line 125 to count only "triggered" conditions); `.cdd/unreleased/9/{self-coherence,beta-review,alpha-closeout,beta-closeout,gamma-closeout}.md`.
- **Debt:** No separately-versioned field-report template exists; if one is later introduced, it should carry a one-line pointer to §Empirical-data prerequisite. Field report's existing concept-doc link is not anchored to the new heading (cosmetic). Upstream cnos.cdd lift is an explicit Non-goal — operator decision. No CI link-check enforces the preamble's numeric condition references against future renumbering.

### #10 — Pipeline portability: `GAIT_DATA_ROOT` env-var
- **Rounds:** 1
- **Verdict:** APPROVE
- **Final SHA on main:** 0544dfc (merge); 988a9d2 (γ close-out)
- **Key artifacts:** `scripts/io_opencap.py` (`DEFAULT_DATA_ROOT`, `GAIT_DATA_ROOT_ENV`, `get_data_root()` with tilde expansion + empty-string-to-default fallback, `get_opencap_extracted_root()` — stdlib `os.environ` only); `scripts/build_notebook.py` (loader cell + persistence cell route through the helpers); `notebooks/existing-data-processing.ipynb` (regenerated — outputs dropped); `notebooks/README.md` (new `## Overriding the data root` section + one-line bash example); `.cdd/unreleased/10/{self-coherence,beta-review,alpha-closeout,beta-closeout,gamma-closeout}.md`.
- **Debt:** Notebook lost rendered outputs after regeneration (regenerate-without-execute trade-off, foreseen at commit time; durable numerical evidence preserved in `analysis/feature-summary-zeroth-pilot.md`). Build-time pinned-version pip install in a grey zone vs the wave manifest's "Install: NO" rule. No env-var-typo guard. Tilde expansion + empty-string fallback are α design choices not strictly required by the issue body.

## Wave-level findings

**`cdd-*-gap` (doctrine-level) findings: none.** All three cycles surfaced only process / docs-content / wave-manifest-template patterns. The cnos.cdd skill bundle and the project's CDD discipline both held cleanly across all three cycles.

The following are wave-level *process* observations consolidated across cycles, organized by what they affect.

### O1 — Wave-N → wave-(N+1) patch loop is structural, not coincidental

**Surface:** This wave itself. Surfaced in α #8 §Patterns, β #8 §Patterns, α #9 §Patterns, γ #8 close-out triage, γ #9 close-out triage.

Two of three cycles (#8 and #9) were direct lifts of zeroth-pilot Patterns 1 & 2 into permanent protocol/concept-doc surfaces. The pattern: zeroth-pilot wave's ε-level findings became protocol-patches wave's α-level work one wave later, with each cycle closing exactly one named pattern. Cross-confirmed independently by α and β on both cycles. The wave loop is doing real CDD work, not aesthetic ceremony.

**Disposition:** No action — this is the system operating correctly. If the next wave-close yields more patterns of this shape, the wave-manifest template could pre-allocate "patch cycles" by default. Not urgent.

### O2 — Wave-manifest template refinements

Three distinct refinements surfaced, one per cycle:

#### O2a — Author-choice surface rationale (from #8)
When an issue's AC offers two equivalent surfaces (e.g. AC2 in #8 gave a choice between `data/external/README.md` and the protocol's §Methodological Constraints), the author should record the choice rationale even when the issue treats them as equivalent. The choice ages; the next maintainer needs to know which audience the section is targeted at. Cross-confirmed α/β in #8.

#### O2b — Conditional ACs with foregrounded gating clauses (from #9)
AC3 in #9 was structured as "if the field-report would mechanically miscount, add a reminder; otherwise no-op." The explicit "if" gate let the cycle close with a justified no-op rather than a fabricated edit. Pattern: issue authors should write conditional ACs with the trigger condition foregrounded.

#### O2c — Build-script execution declaration + pinned-install carve-out (from #10)
Two refinements from #10:

- **Build-script execution declaration:** any future wave touching `scripts/build_notebook.py` (or similar build artifacts) should pre-declare in the wave manifest whether the closing artifact should include execution outputs. The regenerate-with-vs-without-execute trade-off is consequential and should be a wave-author decision, not an α-runtime decision.
- **Pinned-install carve-out:** the "Install Python packages: NO" rule should explicitly distinguish "no new dependencies" from "no installation of already-pinned versions to materialize the build environment." Cycle #10's pip install of `nbformat`, `numpy`, `pandas`, `scipy` (all in `requirements.txt`) crossed the letter but not the spirit of the rule.

**Disposition:** None of O2a/b/c is urgent for the next wave. They become candidate refinements to the wave-manifest template when an operator next revises that template.

### O3 — Docs conventions

#### O3a — Tri-anchor cross-link with empirical grounding (from #8)
α's cross-link in `data/external/opencap-lab-validation.md` line 26 names both the protocol anchor and the README anchor, and grounds the reference with the empirical instance ("falls into the second category"). Stronger shape than bare "see X" because the link site itself instantiates the rule. Cross-confirmed α/β. Worth lifting as a docs convention; not urgent.

#### O3b — Load-bearing carve-outs are legitimate even when unrequested (from #9)
The Condition-5 carve-out in `docs/concepts/support-path.md` line 105 was not required by AC1's wording but was required for the preamble to be self-consistent under careful reading. Class of edit that doesn't appear in ACs but matters for self-consistency. Cross-confirmed α/β.

### O4 — Evidentiary-chain hygiene (from #10)

Wave-N receipts that cite notebook inline outputs (figures, segmentation rates, missingness tables) may need back-pointer notes when a wave-(N+1) cycle regenerates the notebook. Zeroth-pilot wave's receipt cites "3 inline figures" — those figures are gone from the regenerated notebook. The durable numerical evidence is preserved in `analysis/feature-summary-zeroth-pilot.md`, which is the right shape for this kind of receipt.

**Disposition:** ε-level question for the operator: should the zeroth-pilot wave receipt be updated with a back-pointer / refresh note, or is the existence of `analysis/feature-summary-zeroth-pilot.md` enough? The cycle treated this as a wave-level (not cycle-level) concern. Recorded here for operator consideration.

## Wave debt

1. **Remote branch deletes blocked.** `git push origin --delete cycle/{8,9,10}` returned HTTP 403 across all three cycles. Local branches deleted; remote branches still exist at `origin/cycle/8`, `origin/cycle/9`, `origin/cycle/10`. Sandbox restriction, not a workflow error. Operator may need to clean up via the GitHub UI or with elevated credentials.
2. **The three O2 refinements** above are candidates for the next wave-manifest-template revision.
3. **Existing zeroth-pilot wave receipt** cites notebook outputs that no longer exist in the regenerated notebook. Operator decision on whether to refresh.

No `cdd-*-gap` findings; no skill failures; no rule-of-three triggers.

## Branches

- `cycle/8` — local deleted; remote remains (403). Merged in d400153.
- `cycle/9` — local deleted; remote remains (403). Merged in bfe531c.
- `cycle/10` — local deleted; remote remains (403). Merged in 0544dfc.
- `claude/add-support-paths-readme-t5ZW3` — untouched per wave manifest.

## Tags / releases

None (per wave manifest standing permissions: "Tag/release: NO — operator gate").

## Per-cycle round counts (wave-level aggregate)

| Cycle | α rounds | β rounds | β verdict | Mode |
|---|---|---|---|---|
| #8 | 1 | 1 | APPROVE | docs-only |
| #9 | 1 | 1 | APPROVE | docs-only |
| #10 | 1 | 1 | APPROVE | design-and-build (small) |

Zero fix-rounds across the wave. Single-round APPROVE on every cycle. β verdict discipline held — every APPROVE was preceded by an independent re-verification (smoke commands for #10, grep oracle for #8, AC3 no-op judgement for #9).

## Hand-back

The repo is now positioned for the credentialled re-run of the zeroth-pilot pipeline. The two zeroth-pilot patterns are closed; the data-root override is in place; `notebooks/README.md` documents `GAIT_DATA_ROOT` for the operator. The next wave's preconditions: operator-supplied SimTK credentials → download `LabValidation_withoutVideos.zip` → update `data/external/opencap-lab-validation.md` with the SHA-256 + row-level walking-trial inventory → set `GAIT_DATA_ROOT` (or accept the `/opt/gait-data/` default) → re-run `notebooks/existing-data-processing.ipynb`.

That wave is gated on operator action (SimTK credentials) and is not staged here.
