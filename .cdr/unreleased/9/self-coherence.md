<!-- sections: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness] -->
<!-- completed: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness] -->

# Self-Coherence: Concept patch — falsification table empirical-data preamble

**Issue:** #9
**Mode:** docs-only
**Branch:** cycle/9
**Author:** α

## Gap

The zeroth-pilot wave (`.cdd/waves/zeroth-pilot-2026-05-15/wave-closeout.md` §"Pattern 2 — Falsification framework requires empirical variation") and α #7's in-cycle reasoning (`.cdd/unreleased/7/alpha-closeout.md` §F1) both surface the same load-bearing distinction:

- `docs/concepts/support-path.md §"Falsification Conditions for Existing-Data Zeroth Pilot"` lists six conditions; five (1, 2, 3, 4, 6) test for the *absence of empirical variation*. On synthetic / by-construction-coherent data, those five cannot be evaluated — running them anyway returns a misleading "0 of 6 triggered" reading that mechanically resembles a GO signal.
- α #7 had to introduce the "Not testable" vs "Not triggered" distinction by hand in the field report (`reports/field-report-01-existing-data-zeroth-pilot.md` §Falsification Assessment) to avoid that false GO. The distinction was load-bearing in the REVISE call, but it lived only in the field report — not in the concept doc that the field report cites.
- The threshold rule ("If 4 or more of these conditions occur…") did not mention the verdict distinction at all, so a future reader applying the table without α #7's framing would re-trip the same mechanical misfire.

This patch closes the loop on the concept-doc side: it adds the preamble (AC1), refines the threshold rule to count only triggered conditions (AC2), confirms AC3 is a no-op on the already-filed instance (the field report already discharges its intent), and preserves the six conditions' wording (AC4).

## Skills

- **Tier 1:** `cdd/CDD.md`, `cdd/SKILL.md`, `cdd/alpha/SKILL.md`.
- **Tier 2:** `eng/writing` — the falsification section is a durable artifact that downstream cycles (and any future zeroth-pilot re-runs) cite; the preamble has to read cleanly without α #7's in-cycle scaffolding present.
- **Tier 3:** none explicit. Operative constraint from the issue's Non-goals + this wave's manifest: do NOT rewrite the six conditions, do NOT add new conditions, do NOT touch the protocol's GO/NO-GO thresholds.

## ACs

### AC1 — Empirical-data preamble added

**Evidence:** `docs/concepts/support-path.md` lines 96–105 add a new `### Empirical-data prerequisite` subsection nested immediately under `## Falsification Conditions for Existing-Data Zeroth Pilot` (line 92) and before condition 1 (line 107). The subsection states all three required claims named in the issue's AC1:

- **"Five of six conditions test for absence of empirical variation; they require empirical data to evaluate."** — covered at line 98, naming conditions 1, 2, 3, 4, 6 explicitly, with a per-condition gloss of the absence each tests for.
- **"On synthetic / by-construction data, return verdict 'not testable' rather than 'not triggered.'"** — covered at lines 100–103 with explicit definitions of both verdicts in bulleted form.
- **"'Not triggered' is a positive empirical claim. 'Not testable' is a deferred verdict."** — verbatim phrasing at lines 102–103 ("*positive empirical claim*" and "*deferred verdict*" both italicized for emphasis).

Line 105 additionally calls out condition 5 as the exception (testable on synthetic clean data), which protects against an over-reading of the preamble that would mark all six "not testable" on smoke and drop the only honest signal the smoke run produces.

**Oracle:** the issue's "Proof plan" — a reader applying the table to a synthetic-only dataset returns "not testable" for the absence-of-variation conditions, not "not triggered." Lines 100–103 give the reader the exact decision rule. AC met.

### AC2 — Threshold rule refined

**Evidence:** `docs/concepts/support-path.md` line 125. The threshold rule reads:

> **Falsification threshold:** If 4 or more of these conditions are **triggered** during existing-data processing, the construct requires fundamental revision before proceeding with friend data collection. "Not testable" verdicts do **not** count toward the threshold — rationale: a deferred verdict carries no empirical evidence either for or against the construct, so it cannot be used to license a revision decision.

Three changes from the original (line 114 pre-patch):
1. "**triggered**" added (bolded) to make the count rule precise.
2. New clause explicitly excluding "Not testable" verdicts from the count.
3. One-line rationale ("a deferred verdict carries no empirical evidence either for or against the construct") explaining why exclusion is the only honest call.

**Oracle:** the issue's AC2 — "the '4 or more' rule is updated to explicitly exclude 'not testable' verdicts from the count, with a one-line rationale." The rationale is the dependent clause beginning "— rationale:". AC met.

### AC3 — Field-report template aligned (NO-OP on already-filed instance)

**Verdict:** No-op. The field report at `reports/field-report-01-existing-data-zeroth-pilot.md` is the wave's already-filed instance (not a separately-versioned template), and the issue's AC3 surface explicitly says "Surface: report file (template form, not the wave's already-filed instance)." The repo has no separate template form; the filed instance is the only artifact.

**Existing text that discharges AC3's intent:**

- `reports/field-report-01-existing-data-zeroth-pilot.md` lines 155–162 (the Falsification Assessment table) already uses the "Not testable" verdict for 5 of 6 conditions, with smoke-status justification per row. Line 161 is the lone "NOT triggered" — for condition 5, which is exactly the exception called out in the preamble (AC1, line 105).
- Lines 164–166 already carry the empirical-data caveat in prose: "5 of 6 conditions are not yet testable because they require empirical (non-synthetic) variation. The 0/6 score is **not** evidence that the construct survives; it is evidence that the empirical test has not yet run." That paragraph is exactly the framing the new preamble formalizes upstream.
- "Threshold Status" line 166: "Below 4-condition NO-GO threshold *mechanically*, but the threshold's interpretation is degraded when 5 of 6 are not testable. Real-data execution is required before any threshold-based decision is methodologically valid." This already encodes the AC2 refinement on the field-report side.

The filed instance already uses the verdict distinction correctly, so a reminder pointing back to AC1 would be net-noise on a report that already does the right thing. The issue's AC3 phrasing — "**if it would mechanically miscount**" — is the gating clause; the field report would not mechanically miscount, so the conditional does not fire.

If a future cycle introduces a separately-versioned template for downstream field reports (none exists today — see `reports/` directory listing), that template should carry a one-line pointer to `docs/concepts/support-path.md §"Empirical-data prerequisite"`. Carrying as Debt item #1 below.

**Oracle:** the issue's AC3 — "If `reports/field-report-01-existing-data-zeroth-pilot.md` (or its template form) has a falsification table that could be filled out without using the 'not testable' verdict, add a one-line reminder pointing to AC1." The field report's existing table at lines 155–166 uses "Not testable" five times and explicitly justifies the verdict against the empirical-data caveat. AC met by existing text; no edit required.

### AC4 — No regression

**Evidence:** All six existing falsification conditions are present and unchanged. Reproducible grep:

```
$ grep -n "^### [1-6]\." docs/concepts/support-path.md
107:### 1. No Repeatable Patterns Across Gait Cycles
110:### 2. Features Uncorrelated with Movement Context
113:### 3. Left-Right Asymmetry Without Systematic Organization
116:### 4. Poor Agreement Between OpenCap and Reference Measurements
119:### 5. Feature Extraction Consistently Fails on Clean Data
122:### 6. No Distinguishable Coordination Signatures
```

The condition body paragraphs at lines 108, 111, 114, 117, 120, 123 are byte-identical to the pre-patch text. The only changes in the section are the added §Empirical-data prerequisite (lines 96–105) and the threshold-rule refinement (line 125). The construct definition above the falsification section (lines 1–91) is untouched.

**Oracle:** the issue's AC4 — "All six existing falsification conditions remain present and unchanged in wording." Grep oracle holds; condition bodies unchanged. AC met.

## Self-check

α-side audit: did α push ambiguity onto β?

- **AC1:** the preamble has three explicit claims with line-range citations and a non-trivial Condition-5 carve-out. β can verify by reading lines 96–105 against the three required claims in the issue.
- **AC2:** the rationale clause is single-sentence and on one line; β can grep `grep -n "Falsification threshold" docs/concepts/support-path.md` to find it.
- **AC3:** the no-op justification is grounded in three concrete line-range citations from the existing field report. β can verify by reading lines 155–166 of the field report and confirming the "Not testable" framing is already in use; the conditional in AC3 ("if it would mechanically miscount") gates the edit, and the conditional does not fire.
- **AC4:** the grep oracle is explicit and reproducible.

Did α outsource authoring work to β? No — the patch is self-contained. The AC3 no-op call is α's, justified inline, not deferred to β with "your call."

Is every claim backed by evidence in the diff?
- AC1, AC2, AC4: line-range citations in the modified file.
- AC3: line-range citations in the unchanged field report, plus a directory-shape observation (no template file separate from the filed instance).

Scope discipline. Files explicitly NOT touched:

- `requirements.txt` — manifest forbids modification.
- `protocols/existing-data-zeroth-pilot.md` — out-of-scope (cycle 8's surface; merged; the GO/NO-GO thresholds the protocol carries are an explicit Non-goal of #9).
- `reports/field-report-01-existing-data-zeroth-pilot.md` — assessed and determined no-op per AC3.
- `analysis/features.md` — unrelated to falsification framing.
- `notebooks/*` and `scripts/*` — #10's territory.
- `.cdd/waves/protocol-patches-2026-05-15/manifest.md` — δ's surface, not α's.
- Any prior cycle's `.cdd/unreleased/{5,6,7,8}/` files — cross-cycle boundary.
- The six condition body paragraphs and the construct definition — explicit Non-goal of #9 (AC4 plus issue's Non-goals).
- Upstream `cnos.cdd` skill bundle — out-of-scope per Non-goals ("Generalizing this preamble back into cnos.cdd").

## Debt

1. **No separately-versioned field-report template exists.** The current `reports/field-report-01-existing-data-zeroth-pilot.md` is both the filed instance and the only artifact of its shape. If a future cycle introduces a separate template (e.g. `reports/_template-field-report.md`) for downstream zeroth-pilot re-runs against real data, that template should carry a one-line pointer to `docs/concepts/support-path.md §"Empirical-data prerequisite"`. Out of scope for #9 because no template file exists to edit; AC3's conditional ("**if** it would mechanically miscount") explicitly handles this case.

2. **Cross-link from field report to concept doc is not anchor-stable.** The field report at line 153 already links to `../docs/concepts/support-path.md` (whole-file), and lines 155–166 use the verdict framing without anchor-linking to the new §Empirical-data prerequisite heading. A future cycle could anchor that reference for navigability; the link as it stands does not break.

3. **Upstream cnos.cdd lift.** Pattern 2 in the zeroth-pilot wave close-out was flagged as a `cdd-skill-gap` candidate — i.e. the empirical-data preamble idea may belong in the cnos skill bundle for any project doing construct-falsification work, not just gait-support-paths. The issue's Non-goals explicitly defer this to a separate upstream PR (operator decision). Naming as debt for visibility; not an in-scope action.

4. **No CI / link-check enforcement.** The new preamble references conditions 1, 2, 3, 4, 6 by number and calls out condition 5 as the exception. If a future cycle renumbers or reorders the conditions (a real risk if new conditions are ever added — also a Non-goal here), the preamble's references would silently drift. A markdown structural check would catch this; not in scope.

## CDD-Trace

| Step | Artifact | Skills loaded | Decision |
|------|----------|---------------|----------|
| 0 Observe | — | cdd | Read issue #9, wave manifest, zeroth-pilot wave close-out §Pattern 2, α #7 close-out §F1, current `docs/concepts/support-path.md`, full `reports/field-report-01-existing-data-zeroth-pilot.md` |
| 1 Select | — | cdd | Gap: concept doc's falsification table has no empirical-data preamble and no verdict distinction in the threshold rule; field report already uses the distinction so AC3 is a candidate no-op |
| 2 Branch | cycle/9 | cdd | δ created from origin/main; α landed via `git switch cycle/9` |
| 3 Bootstrap | n/a | cdd | Not required — docs-only cycle, no package installs (manifest forbids anyway) |
| 4 Gap | self-coherence §Gap | — | Add §Empirical-data prerequisite to concept doc; refine threshold rule; confirm field report no-op |
| 5 Mode | self-coherence §Skills | cdd, eng/writing | docs-only |
| 6 Artifacts | `docs/concepts/support-path.md` (added §Empirical-data prerequisite at lines 96–105; refined threshold rule at line 125) | eng/writing | One file changed; six conditions unchanged (AC4 grep oracle); field report deliberately not touched (AC3 no-op justified) |
| 7 Self-coherence | self-coherence.md | cdd | This file |
| 7a Pre-review | self-coherence.md §Review-readiness | cdd | 4 ACs evidenced (AC3 as justified no-op); additive-only invariant held for the six conditions; scope discipline documented |

## Review-readiness

Round 1. Cycle branch base: `cycle/9` off `origin/main` (post-#8 merge at `d400153`). Files changed:

- `docs/concepts/support-path.md` — `### Empirical-data prerequisite` subsection added (lines 96–105); threshold rule refined (line 125). Six conditions and construct definition unchanged.
- `.cdd/unreleased/9/self-coherence.md` — this file.

All four ACs have evidence:
- AC1: lines 96–105 of `docs/concepts/support-path.md`.
- AC2: line 125 of `docs/concepts/support-path.md`.
- AC3: no-op, justified against lines 155–166 of `reports/field-report-01-existing-data-zeroth-pilot.md` (unchanged).
- AC4: `grep -n "^### [1-6]\." docs/concepts/support-path.md` oracle holds.

**Specific β decision points:**
1. Is the preamble's three-claim coverage (lines 96–105) faithful to AC1's three bullet points, or is one of the three thin?
2. Is the Condition-5 carve-out at line 105 a useful refinement or a non-required addition? (It's not strictly named in AC1; it prevents an over-reading of the preamble that would mark *all* conditions "not testable" on smoke and drop the only honest signal the smoke run produces. α's call was: include, because without it the preamble could read as "no smoke conclusion is ever valid," which contradicts the field report's correct use of "NOT triggered" for condition 5.)
3. Is the AC3 no-op call justified, or should a one-line cross-reference still be added to the field report? α's read: the field report already discharges AC3's intent (lines 155–166); a reminder would be net-noise. If β disagrees, the minimal alternative is one line near `reports/field-report-01-existing-data-zeroth-pilot.md` line 153 pointing to the new §Empirical-data prerequisite anchor.
4. Is AC4's grep oracle reproducible (β can run it locally)?
