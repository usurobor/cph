# β Review: Concept patch — falsification table empirical-data preamble

**Cycle:** #9
**Branch:** cycle/9 (head: 1220dfa)
**Base:** origin/main (d400153)
**Reviewer:** β

## Round 1 — Verdict: APPROVE

### Contract integrity

α HEAD commit author: `alpha@gait-support-paths.cdd.cnos` on the single cycle/9 commit (`1220dfa`). β identity will be used for the review commit, merge, and close-out. Working tree clean before review. Both implementation and self-coherence landed in one commit, as expected for a docs-only patch.

### AC-by-AC verification

- **AC1 — Empirical-data preamble added.** ✓ Met. `docs/concepts/support-path.md` lines 96–105 add a new `### Empirical-data prerequisite` subsection nested under `## Falsification Conditions for Existing-Data Zeroth Pilot` (line 92) and immediately preceding condition 1 (line 107). The subsection discharges all three required claims:
  - "Five of six conditions test for absence of empirical variation" — covered at line 98, naming conditions 1, 2, 3, 4, 6 explicitly and glossing the absence each tests for.
  - "On synthetic / by-construction data, return verdict 'not testable' rather than 'not triggered'" — covered at lines 100–103 as a bulleted contrast between the two verdicts.
  - "'Not triggered' is a positive empirical claim. 'Not testable' is a deferred verdict" — verbatim phrasing at lines 102–103 with both terms italicized.
  Line 105 carves out condition 5 (pipeline competence on clean data) as the lone exception that *can* be evaluated on synthetic clean inputs. This is not strictly required by AC1, but it is the right call: without it, a reader could mechanically mark all six "not testable" on smoke and drop the only honest signal the smoke run produces — exactly the kind of mechanical misreading the preamble exists to prevent. The carve-out preserves the field report's correct "NOT triggered" verdict for condition 5 (`reports/field-report-01-existing-data-zeroth-pilot.md` line 161).

- **AC2 — Threshold rule refined.** ✓ Met. `docs/concepts/support-path.md` line 125 reworks the threshold rule with three changes from the pre-patch text:
  1. "are **triggered**" replaces "occur" — makes the count rule precise.
  2. New clause: "'Not testable' verdicts do **not** count toward the threshold" — the exclusion AC2 requires.
  3. One-line rationale: "a deferred verdict carries no empirical evidence either for or against the construct, so it cannot be used to license a revision decision" — the rationale AC2 requires.
  The rationale is clean: it grounds the exclusion in the asymmetry between "tested and survived" and "not yet tested," which is the same asymmetry the preamble draws at lines 102–103. AC2's "one-line rationale" requirement is satisfied; the dependent clause beginning "— rationale:" is the rationale.

- **AC3 — Field-report template alignment (NO-OP).** ✓ Met by existing text. α's no-op call is independently correct. I verified by reading `reports/field-report-01-existing-data-zeroth-pilot.md §Support-Path Inference` (lines 71–121) and §Falsification Assessment (lines 151–166):
  - Lines 157–162 (the Falsification Assessment table) already uses "Not testable" verdict for five of six conditions (rows 1, 2, 3, 4, 6), each with a smoke-status justification. Row 5 is the lone "NOT triggered" — matching the carve-out the new preamble formalizes at line 105.
  - Lines 164–166 already carry the empirical-data caveat in prose: "5 of 6 conditions are not yet testable because they require empirical (non-synthetic) variation. The 0/6 score is **not** evidence that the construct survives." This is exactly the framing AC1 formalizes upstream.
  - Line 166 "Threshold Status" already encodes the AC2 refinement on the report side: "Below 4-condition NO-GO threshold *mechanically*, but the threshold's interpretation is degraded when 5 of 6 are not testable."

  AC3's surface clause — "(template form, not the wave's already-filed instance)" — refers to a template that does not exist in the repo (only `field-report-00-plan.md`, `field-report-01-existing-data-zeroth-pilot.md`, `field-report-02-friend-pre-pilot.md`; no `_template.md`). AC3's gating clause — "if it would mechanically miscount" — does not fire because the filed instance already uses the verdict distinction correctly. α flagged the missing template as Debt item 1 for visibility; that is the right disposition. AC met.

- **AC4 — No regression.** ✓ Met. Reproduced α's grep oracle:
  ```
  $ grep -n "^### [1-6]\." docs/concepts/support-path.md
  107:### 1. No Repeatable Patterns Across Gait Cycles
  110:### 2. Features Uncorrelated with Movement Context
  113:### 3. Left-Right Asymmetry Without Systematic Organization
  116:### 4. Poor Agreement Between OpenCap and Reference Measurements
  119:### 5. Feature Extraction Consistently Fails on Clean Data
  122:### 6. No Distinguishable Coordination Signatures
  ```
  All six headings present. Cross-checked condition body text against `origin/main:docs/concepts/support-path.md` — every condition body line (108, 111, 114, 117, 120, 123) is byte-identical to the pre-patch text. The construct-definition block (lines 1–92) is byte-identical to `origin/main` (verified by `diff` against the first 92 lines). AC met.

### Scope discipline

Files touched (per `git diff --name-only origin/main..cycle/9`):
- `docs/concepts/support-path.md` — AC1/AC2 surface.
- `.cdd/unreleased/9/self-coherence.md` — α process artifact.

Files NOT touched (issue non-goals + wave-manifest constraints + AC4):
- `requirements.txt` — wave manifest forbids modification. PASS.
- `protocols/existing-data-zeroth-pilot.md` — cycle 8's surface (merged); GO/NO-GO thresholds at lines 122–129 are an explicit issue Non-goal. PASS (zero-line diff under `protocols/`).
- `reports/field-report-01-existing-data-zeroth-pilot.md` — assessed and determined no-op per AC3. PASS.
- Construct definition (lines 1–91 of `docs/concepts/support-path.md`). PASS (byte-identical).
- Six condition body paragraphs (lines 108, 111, 114, 117, 120, 123). PASS (byte-identical, AC4).
- `analysis/features.md`, `notebooks/*`, `scripts/*` — out of scope. PASS.
- `.cdd/waves/protocol-patches-2026-05-15/manifest.md` — δ surface. PASS.
- Prior cycles' `.cdd/unreleased/{5,6,7,8}/` — cross-cycle boundary. PASS.
- Upstream `cnos.cdd` skill bundle — explicit Non-goal ("Generalizing this preamble back into cnos.cdd"). PASS.

### cdd-*-gap findings

None. The cycle is a clean closure of a wave-N pattern (`cdd-skill-gap` candidate from zeroth-pilot wave close-out Pattern 2) into the concept doc one wave later — same shape as cycle #8. No new doctrine-level gaps emerge from the review.

### Notes / observations

- **Condition-5 carve-out is the load-bearing α-side judgement.** AC1 names three required claims; α added a fourth (the condition-5 exception) at line 105. The carve-out is not in the issue's AC1 text but is the only way the preamble doesn't accidentally invalidate the field report's existing "NOT triggered" verdict for condition 5. β endorses the carve-out: without it, the preamble would over-read.
- **AC3 no-op is correctly justified.** α did not push the AC3 call onto β with "your call." The self-coherence §AC3 cites three concrete line-ranges in the unchanged field report (lines 155–162, 164–166, 166) plus a directory-shape observation (no separate template). β verified all three citations independently. The conditional in AC3 ("if it would mechanically miscount") gates the edit; the conditional does not fire.
- **Documentation-shape pattern continues:** wave-N close-out Pattern 2 → wave-(N+1) concept patch. Same pattern as cycle #8 (Pattern 1 → protocol patch). The wave-N → wave-(N+1) loop is doing real work; close-out patterns are reliably becoming small, surface-anchored docs cycles.
- **Anchor-stability debt (α flagged):** the preamble references conditions by number (1, 2, 3, 4, 6) and calls out condition 5. If a future cycle ever renumbers or reorders conditions (a Non-goal here, but a real future risk if new conditions are added), the preamble's numeric references would silently drift. α flagged this as Debt item 4. Not blocking; worth tracking.

### Cycle-level note for γ

Clean single-round APPROVE. No fix-rounds. The cycle continues the wave-N-pattern-becomes-wave-(N+1)-patch shape established by cycle #8. α's scope discipline is again strong — every issue Non-goal is named in self-coherence §Self-check with a matching "not touched" assertion, and the AC3 no-op call is justified rather than punted.

### Merge instruction

```
git switch main && git pull origin main --ff-only
git -c user.name='β-as-agent' -c user.email='beta@gait-support-paths.cdd.cnos' \
    merge --no-ff cycle/9 -m 'Closes #9: Concept patch — falsification table needs empirical-data preamble'
git push origin main
```

**Verdict: APPROVE.**
