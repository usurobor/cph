---
name: cph-31-self-coherence
description: α self-coherence for cph#31 (R4 full falsification re-evaluation on post-cph#27 + cph#28 surfaces — analysis-only synthesis cycle, no new compute)
metadata:
  type: cycle-artifact
  cycle: 31
  role: alpha
  mode: explore/analysis
sections:
  planned: [Gap, Skills, MethodPicks, ACs, SelfCheck, Debt, CDDTrace, PreReviewGate, ReviewReadiness]
  completed: [Gap, Skills, MethodPicks, ACs, SelfCheck, Debt, CDDTrace, PreReviewGate, ReviewReadiness]
---

# α self-coherence — cph#31

## §Gap

**Issue:** [usurobor/cph#31](https://github.com/usurobor/cph/issues/31) — "R4 full falsification re-evaluation on post-cph#27 + cph#28 surfaces" (`P1`, `surface:analysis`).

**Incoherence the cycle closes.** After cph#27 (R3 R-side aggregate; partial GO on R-side; 5 of 6 falsification conditions evaluated NOT triggered on R-side surfaces; condition 3 marked "not testable on this archive") and cph#28 (R1 L-cycle recovery via half-stride contralateral inference; condition 3 surface lifted from "not testable" to "evaluable on inferred-bilateral surface"), the project's falsification table has partial coverage but no full 6-condition synthesis report at adequate empirical coverage. cph#28 field report §Open issues named the R4 full re-evaluation as the now-reachable substantive verdict. The empirical state on `main` is "R4 fully evaluable on inferred-bilateral surface" (ROADMAP.md Phase R4 status pre-cph#31); cph#31 closes the gap from "evaluable" to "evaluated" with the wave-level verdict + standing-decision implications.

**Scope.** Walk the 6 falsification conditions in [`docs/concepts/support-path.md`](../../../docs/concepts/support-path.md) §Falsification one by one. For each, declare testability (testable / partially testable / not testable on this archive), verdict (triggered / not triggered / evaluable-but-pending), and bounded scope (surface anchor + caveats). Apply the wave-level threshold (0–1 triggered → survives; 2–3 → ambiguous; ≥4 → fundamental revision). Write [`reports/field-report-04-falsification-evaluation.md`](../../../reports/field-report-04-falsification-evaluation.md) (new file) with the table, the verdict, and the standing-decision implications for R1 / R3 / R5 / R6. Update status surfaces (PROJECT.md, ROADMAP.md, CHANGELOG.md).

**Mode.** explore / analysis — same shape as cph#27 (β verifies the synthesis is recorded and self-consistent, not "the right verdict"). α's method picks (anchoring choices, caveat language, deferred-verdict accounting) are α's call within AC scope and are documented in §Method picks below.

**Cross-cycle binding.** cph#30 (R3 bilateral extension on the inferred-bilateral surface) runs in parallel with cph#31. The issue body §NOTE explicitly addresses the parallel-run scenario: if cph#30 lands first, cph#31 cites its `field-report-03` §"R3 bilateral extension" section; if it doesn't land first, cph#31 notes the condition-3 verdict as anchored on whatever R3-bilateral evidence exists at the time of the run. **State at cph#31 run time (α intake observation):** `origin/cycle/30-r3-bilateral-extension` exists locally (visible in `git branch -a`) but is *not* merged on `origin/main` (`git log origin/main --oneline -5` does not show a cph#30 closeout). cph#31 therefore anchors condition 3 on cph#28's surface-lift evidence and treats the substantive lr-diff verdict as deferred to cph#30 / non-contributory to the threshold tally (per `docs/concepts/support-path.md` §Falsification "Empirical-data prerequisite" reading).

## §Skills

Tier 1 loaded (CDD lifecycle):
- `cnos.cdd/skills/cdd/CDD.md` — canonical lifecycle (referenced; full read not required for analysis-only synthesis cycle)
- `cnos.cdd/skills/cdd/alpha/SKILL.md` — α load order, incremental self-coherence discipline (§2.5), pre-review gate (§2.6)
- `cnos.cdd/skills/cdd/issue/SKILL.md` — AC discipline, MCA preconditions (confirmed explore mode applies — no formalization gate, no language-spec gate, no architecture gate)

Tier 2 loaded:
- `cnos.core/skills/write/SKILL.md` — field-report-04 prose discipline (lead with the point; condition-bound language; measured-vs-inferred discipline carried verbatim from cph#27 / cph#28 precedents)

Tier 3 loaded (cycle-specific):
- *None as packaged skills.* This is an analysis-only synthesis cycle: no new code, no new test, no schema-bearing contract changed. The cycle re-cites cph#27 and cph#28 evidence; α does not run new statistics. Per the issue body §Hard constraints: "Do not modify code in `scripts/` — this is an analysis-only cycle"; per the issue body §Approach: "Don't duplicate cph#27 / cph#28 analyses."

**Domain references (read-only, treated as authoritative):**
- `docs/concepts/support-path.md` §Falsification — the 6 conditions are fixed (per AC6 / issue body §Non-goals — content untouched); the threshold rule (0–1 / 2–3 / ≥4) drives the wave-level verdict; the "Empirical-data prerequisite" discipline drives the deferred-verdict accounting on condition 3.
- `reports/field-report-03-construct-evaluation.md` — cph#27 R-side anchors for conditions 1, 2, 6.
- `reports/field-report-01-existing-data-zeroth-pilot.md` — cph#28 inferred-bilateral anchor for condition 3 surface availability; R1 anchor for condition 4 (OpenCap-vs-reference, carried from cph#22/26); cph#28 anchor for condition 5 (feature-extraction missingness on 117 cycles × 35 columns post-recovery).
- `.cdr/unreleased/27/self-coherence.md`, `.cdr/unreleased/28/self-coherence.md` — format precedents for this file's section structure.

## §Method picks

Three picks settled before any field-report sentence ran; rationale below; each pick verified by β as "recorded and self-consistent," not as "correct."

### M1 — Deferred-verdict accounting (condition 3)

**Pick.** cph#30 has not landed on `main` at cph#31 run time. The substantive triggered / not triggered verdict on condition 3 (L/R asymmetry) requires the bilateral lr-diff aggregate tests that cph#30 owns. cph#31 cannot run those tests without duplicating cph#30 (explicitly forbidden by issue body §Approach: "Don't duplicate cph#27 / cph#28 analyses" — extended in spirit to cph#30, which is the active R3-bilateral cycle).

**Resolution.** Read condition 3 as "evaluable on inferred-bilateral surface, substantive verdict pending cph#30." Treat the row as **non-contributory to the threshold tally** (same accounting as "not testable" per `docs/concepts/support-path.md` §Falsification "Empirical-data prerequisite": no empirical evidence has yet been produced to count for or against the construct). The condition has surface availability evidence (cph#28: 57 inferred-partial L cycles; 57 bilateral pairs; lr-diff computable) but no per-feature triggered / not triggered finding.

**Why non-contributory.** Counting "evaluable but pending" as "not triggered" would mechanically lift the verdict by reading absence of evidence as evidence of absence. Counting it as "triggered" would do the symmetric wrong thing. The doc's "Empirical-data prerequisite" discipline explicitly anticipates this case for "not testable" verdicts; α extends the same accounting to "evaluable but verdict-pending" because the threshold rule is empirical (it counts conditions whose empirical reading is in hand) and verdict-pending is by definition not empirically read yet.

**Predictability.** The reading is named explicitly in the field report §"Wave-level falsification verdict" + §Appendix C: when cph#30 lands, the condition 3 row updates to triggered / not triggered with cph#30's surface anchor; the tally moves to 0 of 6 (if NOT triggered) or 1 of 6 (if triggered) — either way still in the 0–1 "survives" bucket. No interpretive ambiguity is left for β or for cph#30's closeout.

### M2 — Anchor naming per condition (AC2)

**Pick.** Each row in the 6-condition table names its surface anchor explicitly: which prior cycle's report + which section + which artifact-level number is being cited. Conditions 1, 2, 6 → cph#27 R-side aggregate (field-report-03 §AC5 + §AC4); condition 3 → cph#28 inferred-bilateral surface (field-report-01 §"L-side recovery (cph#28)" + §Falsification Assessment); condition 4 → R1 OpenCap-vs-reference (carried from cph#22/26, surfaced in field-report-01 §"OpenCap vs Reference Comparison"); condition 5 → feature-extraction missingness (analysis/feature-summary-zeroth-pilot.md §AC2; field-report-01 §"Feature Extraction Status").

**Why explicit anchors.** AC2 requires per-condition anchor naming; AC3 requires inference caveats applied where the bilateral surface anchors the verdict. Reading from one citation chain (e.g. "anchored on cph#27 + cph#28") would leave β unable to verify which cycle's evidence drives which row. The explicit per-row anchor is a verification handle.

### M3 — Caveat language carried verbatim from precedents

**Pick.** Path (a) honesty caveat phrasing (inferred not measured; partial-clip coverage 0.80–0.94; "consistent with" not "measurement of"), R-side scope caveat phrasing, and "survives ≠ validated" caveat phrasing are all carried verbatim from cph#28 field-report-01 §"L-side recovery (cph#28)" §Claim-scope bounds and cph#27 field-report-03 §"Falsification re-evaluation on R-side (AC5)" Important caveat. The exact phrasings are reused so that cross-doc consistency (`grep -F`-checkable) is preserved.

**Why verbatim.** Coherence-laundering is the named failure mode in ROADMAP.md Phase R4 §Coherence risk and PROJECT.md Open issues language. Drift in caveat phrasing between cph#27 / cph#28 / cph#31 would be exactly the kind of small-edit erosion that lifts inferred findings into measurement-grade claims. Reusing the precedent phrasing keeps the caveat surface stable.

## §ACs

Row-per-AC evidence map. The issue body lists 9 ACs (AC1 through AC9). Each AC names artifact + section + oracle β can re-verify.

| AC | Issue text (one-line gloss) | Evidence (artifact §section) | β oracle |
|---|---|---|---|
| AC1 | All 6 falsification conditions evaluated — each has a verdict | `reports/field-report-04-falsification-evaluation.md` §"6-condition table (AC1 + AC2 + AC3)" — 6 rows, one per condition, with verdict column populated. No condition is silently skipped. | `grep -c '^\| [1-6] \|' reports/field-report-04-falsification-evaluation.md` returns 6 (the six condition rows in the table). |
| AC2 | Per-condition anchor named — each verdict cites the surface(s) that anchor it | Same §"6-condition table" — each row's fourth column ("Bounded scope (surface + caveats)") names the anchor cycle + report section + numeric anchor (e.g. condition 1: "Anchor: cph#27 R-side aggregate (`reports/field-report-03-construct-evaluation.md` §AC5 row 1)"; condition 3: "Anchor: cph#28 inferred-bilateral surface (`reports/field-report-01-existing-data-zeroth-pilot.md` §"L-side recovery (cph#28)" + §Falsification Assessment row 3)"; condition 4: "Anchor: R1 OpenCap-vs-reference comparison, carried from cph#22/26"; condition 5: "Anchor: feature-extraction missingness on real + smoke"; condition 6: "Anchor: cph#27 R-side aggregate"). | β spot-checks 2 rows: condition 1 cites cph#27 field-report-03 §AC5 row 1 + the 7-of-25 BH-sig number; condition 3 cites cph#28 field-report-01 §"L-side recovery" + the 57 inferred-partial L cycles number. |
| AC3 | Inference caveats applied — verdicts on inferred-bilateral surface name the path (a) caveat; R-side verdicts name R-side bounded scope | Condition 3 row carries the full path (a) honesty caveat verbatim (inferred not measured; partial-clip coverage 0.80–0.94; "consistent with" not "measurement of"). Conditions 1, 2, 6 carry R-side bounded scope caveats (e.g. condition 6: "the verdict is bound to the trunk-sway perturbation condition response, not to gait in general; the bilateral lr-diff version of condition 6 is owned by cph#30"). The four wave-level anchor caveats are restated in §"Wave-level falsification verdict (AC4)" and in §"Decision". | β verifies the phrase "consistent with" appears at least once in the condition 3 row; verifies the phrase "R-side" appears in conditions 1, 2, 6 rows; verifies the four anchor caveats are enumerated 1–4 in §"Wave-level falsification verdict". |
| AC4 | Wave-level verdict produced — the 0–1 / 2–3 / ≥4 trigger threshold from `docs/concepts/support-path.md` §Falsification is applied; the verdict is stated | `reports/field-report-04-falsification-evaluation.md` §"Wave-level falsification verdict (AC4)" — threshold rule restated verbatim; tally restated (0 triggered / 5 NOT triggered / 1 evaluable-but-pending non-contributory); verdict: "Construct survives (0–1 triggered ≤ 1; threshold satisfied for the 'survives' bucket)". | β reads §"Wave-level falsification verdict", verifies the threshold rule appears verbatim, the tally adds up to 0+5+1=6, the verdict string "construct survives" appears. |
| AC5 | `field-report-04-falsification-evaluation.md` written — new file; distinguishes measured signal from inferred interpretation; uses condition-bound language; states wave-level verdict + standing-decision implications for R1, R3, R5, R6 | File exists at `reports/field-report-04-falsification-evaluation.md`. Sections: Overview, Executive summary, Methodological note, 6-condition table, Wave-level verdict, Standing-decision implications (R1 / R3 / R5 / R6 each named), Open issues, Decision, Provenance/Receipt, Appendices. Measured-vs-inferred discipline is explicit in conditions 1/2/4/5/6 (measured anchors) vs condition 3 (inferred-bilateral anchor); the wave-level verdict carries the "survives ≠ validated" caveat. | β verifies the file exists at the path; counts the 6 conditions in §"6-condition table" ✓; verifies "R1", "R3", "R5", "R6" each appear in §"Standing-decision implications" as named sub-headings or paragraphs. |
| AC6 | `docs/concepts/support-path.md` §Falsification content untouched — the 6 conditions are evaluated, not rewritten | `git diff origin/main..HEAD -- docs/concepts/support-path.md` returns empty (exit 0, no output). | β re-runs the diff command; verifies empty output. |
| AC7 | Status surfaces realigned — PROJECT.md / ROADMAP.md / CHANGELOG.md updated; R4 status transitions according to the verdict | `git diff origin/main..HEAD -- PROJECT.md ROADMAP.md CHANGELOG.md` shows R4-status patches: PROJECT.md §"Current empirical decision" + §"Current blocker" + §"Next action" + §"Open issues" + §"Last field report" updated; ROADMAP.md §"Current state" + §"Phase R4" (status, current evidence, gate, coherence risk, next action, owning files) + §"Phase R5" status updated; CHANGELOG.md has a new 0.4.0 entry (narrative-progress form matching 0.3.0 / 0.3.1 / 0.3.2 precedent). | β runs the diff command; verifies all three files are modified; spot-checks PROJECT.md §"Last field report" points to field-report-04; CHANGELOG.md 0.4.0 entry has narrative-progress form matching the 0.3.x cycle precedents (Where we were / What this version unblocked / What is now read / What is still bounded-or-blocked / The new question / Changed (file-level) / Decision / Next gate). |
| AC8 | No empirical drift on charter — README / hypothesis doc / seven-families article / support-path doc untouched | `git diff origin/main..HEAD -- README.md docs/concepts/coherence-path-hypothesis.md docs/concepts/support-path.md docs/articles/seven-ways-people-walk.md docs/concepts/failure-conditions.md` returns empty (exit 0, no output). | β re-runs the diff command; verifies empty output. |
| AC9 | No data policy regression — no raw participant data committed | `git diff origin/main..HEAD --name-only \| grep -E '\.(zip\|trc\|mot\|sto\|c3d\|osim\|mp4\|mov\|csv\|parquet)$' \|\| echo NONE` returns `NONE`. | β re-runs the same grep; verifies `NONE`. |

## §Self-check

α's pre-review sweep — does α's work push ambiguity onto β?

**1. Method-pick clarity.** Every interpretive choice (deferred-verdict accounting for condition 3, per-row anchor naming, verbatim caveat phrasing) is named in §Method picks M1–M3 with rationale. β does not have to infer why a choice was made.

**2. AC1's "all 6 conditions evaluated" interpretation.** The condition 3 row reads "evaluable, substantive verdict pending cph#30" — *not* a silent skip. The row carries surface-availability evidence (57 inferred-partial L cycles; 57 bilateral pairs; lr-diff computable) and the deferred-verdict accounting reading (non-contributory to the threshold). β can independently verify the row is populated by reading the table; the deferred-verdict accounting is named in M1 above and in field-report-04 §Appendix C ("Threshold-rule reading for evaluable, verdict pending").

**3. Sibling-surface peer enumeration.** α did not introduce new candidate-hypothesis names in this cycle (no new construct surfaces; the 3 cph#27 candidates are cited, not extended). α did introduce one new framing phrase: "construct survives subject to anchor caveats." Peer-check:
- `grep -rn "construct survives" /home/user/cph` (excluding new files) returns hits only in `reports/field-report-03-construct-evaluation.md` §AC5 (verbatim "the construct survives R-side contact") and `CHANGELOG.md` 0.3.1 entry. The cph#31 framing "construct survives subject to anchor caveats" is a new compound but uses the existing precedent stem.
- No collision with `docs/concepts/support-path.md` (the canonical doc) on the verdict phrasing.

**4. Measured-vs-inferred discipline.** The field report separates measured signal from inferred interpretation in every condition row: condition 1 (measured R-side feature responses → inferred construct reading of systematic-vs-random); condition 2 (measured trunk-sway condition response → inferred context-correlation); condition 3 (inferred-bilateral surface availability → substantive verdict deferred to cph#30); conditions 4–5 (measurement-substrate anchors); condition 6 (R-side measured signature distinguishability → inferred candidate-hypothesis-level distinguishability; formal cluster structure held for R6). The wave-level verdict carries the "survives ≠ validated" caveat (measured surfaces clear the gate; inferred construct is not lifted to validated by this).

**5. Cross-cycle binding compliance.** α did not lift R1 (R1 stays GO with bounded scope per cph#28); did not lift R3 (partial GO on R-side per cph#27; bilateral extension owned by cph#30); did not lift R5 (still blocked behind R3-bilateral closure); did not lift R6 (still blocked; R4 GO does not unblock R6). The R4 transition is the only status surface that changes, and the transition is to "construct survives subject to anchor caveats" — a synthesis statement, not a gate lift.

**6. AC6 charter-surface discipline.** α did not modify `docs/concepts/support-path.md` (the 6 conditions are fixed per issue body §Hard constraints + §AC6). α did not modify any other charter file (README / hypothesis doc / seven-families article / failure-conditions doc). The 5-file diff sweep returns empty.

**7. AC9 data policy discipline.** α did not commit any raw data file. The cycle is analysis-only synthesis on cited prior-cycle outputs; no CSV / parquet / TRC / MOT / OSIM / STO / C3D / MP4 / MOV / ZIP files added. The `git diff --name-only | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$' || echo NONE` oracle returns NONE.

**8. Reproducibility.** No new compute commissioned (§Method picks M1 + field-report-04 §"Methodological note: no new compute commissioned"). β reproduces by reading the field report's per-row anchors and re-citing the cited prior-cycle reports. No script to re-run; no bootstrap to seed; no statistics to redo.

**9. No outsourced authoring.** α did not punt: deferred-verdict accounting (M1), per-condition anchor naming (M2), caveat-phrasing reuse (M3), wave-level verdict synthesis, standing-decision implications for R1 / R3 / R5 / R6 are all explicit in α's surfaces. β verifies, does not author.

**10. cph#30 parallel-run handling.** Per issue body §NOTE: cph#30 hasn't landed first; α anchors condition 3 on the cph#28 surface lift + treats the substantive verdict as deferred to cph#30. The accounting is non-contributory to the threshold tally; the predictability rule (when cph#30 lands, tally moves to 0 of 6 or 1 of 6, still in "survives" bucket) is named in field-report-04 §Appendix C. If cph#30 lands first and the operator wants cph#31 to cite cph#30's bilateral verdict directly, that is a rebase-and-update operation — flagged as debt below (D1).

## §Debt

**D1 — cph#30 parallel-run rebase risk.** If cph#30 lands on `main` before cph#31's β merge, the cph#31 field report's condition 3 row + the wave-level tally + the CHANGELOG 0.4.0 entry references to "cph#30 owns the substantive verdict" / "not yet landed on `main`" all need re-reading against cph#30's actual closeout. The rebase is mechanical (update the condition 3 row's verdict from "evaluable, substantive verdict pending cph#30" to "triggered / not triggered per cph#30 [field-report-03 §...]"; re-tally the wave-level count; update CHANGELOG 0.4.0 entry). β should flag this as RC if cph#30 has landed by the time β picks up cph#31. **Resolution path:** rebase `cycle/31-r4-full-falsification` onto post-cph#30 `main`; update condition 3 row + tally + CHANGELOG narrative; re-validate the wave-level verdict; re-push.

**D2 — Within-subject within-condition cycle-level repeatability (carried from cph#27 D2).** Condition 1's verdict reads cross-subject consistency, not within-subject stability. n=3 cycles per (subject, condition) is too thin for within-subject ICC. The verdict is bounded accordingly in the condition 1 row's "Caveat" sub-line. *Not in cph#31 scope; named to maintain debt continuity from cph#27.*

**D3 — Formal PCA / clustering on R-side aggregates deferred (carried from cph#27 D3).** Condition 6's verdict reads feature-family distinguishability, not formal cluster structure. Cluster structure is held for R6. The verdict is bounded accordingly in the condition 6 row's "Caveat" sub-line. *Not in cph#31 scope; named to maintain debt continuity from cph#27. Also explicitly out of cph#31 scope per issue body §Non-goals.*

**D4 — Path (b) measured-bilateral upgrade (carried from cph#28).** The path (a) honesty caveat applies to every bilateral reading; the path (b) upgrade (operator-side OpenSim IK rerun with extended trial windows on the reachable TRC files at `/opt/gait-data/opencap-lab-validation/extracted/`) remains the route to truly measured bilateral data. cph#31's wave-level verdict does not require pursuing it; cph#30's eventual findings will name whether it is required. *Not in cph#31 scope; named to maintain debt continuity from cph#28.*

**D5 — Provisional close-out not written.** Per `alpha/SKILL.md` §2.8, the standard close-out path is γ-requested re-dispatch after β merge. α has not written `alpha-closeout.md` in this cycle; α will write it on re-dispatch after β approval + merge. No provisional close-out fallback used. *Standing pattern; not actual debt unless re-dispatch does not happen.*

## §CDD-Trace

CDD canonical artifact order (per `CDD.md` §5.2 and `alpha/SKILL.md` §2.2):

| Step | Required artifact | Status in this cycle | Surface |
|---|---|---|---|
| 1 | Design artifact (or "not required") | **Not required.** Per issue body §Approach, this is an analysis-only synthesis cycle; the "design" is the 6-condition table walk + the wave-level verdict tally, which is fully specified by the canonical doc + the prior-cycle anchors. No separate design artifact needed. | Issue body §Approach; this file §Method picks |
| 2 | Coherence contract (.cdr/unreleased/{N}/self-coherence.md §Gap) | **Done.** §Gap above names the incoherence in α's words anchored to issue body + cph#27 / cph#28 §Open issues. | `.cdr/unreleased/31/self-coherence.md` §Gap |
| 3 | Plan (or "not required") | **Not required.** Per issue body §Approach, the 6-condition walk is the plan; α executed condition-by-condition. No separate plan artifact. | Issue body §Approach + this file §ACs |
| 4 | Tests | **Not applicable as automated test suite** — this is an analysis-only synthesis cycle, not a code-change cycle. No new compute commissioned (per M1 + field-report-04 §"Methodological note"). The "test" surface is the per-row anchor verifiability: β re-cites the cited prior-cycle reports and confirms the numeric anchors match. | Field-report-04 §"6-condition table" anchor citations; this file §ACs row AC2 oracle |
| 5 | Code | **No new code.** Issue body §Hard constraints: "Do not modify code in `scripts/` — this is an analysis-only cycle." cph#31 did not write `analysis/r4_falsification_eval.py` because no condition needed new compute (M1 rationale + field-report-04 §"Methodological note"). Zero `*.py` files in the diff. | `git diff --name-only origin/main..HEAD` excludes `.py` extensions |
| 6 | Docs | **Done.** Three categories of doc writes: (a) new field report `reports/field-report-04-falsification-evaluation.md` (the cycle's primary artifact); (b) status surface patches on PROJECT.md, ROADMAP.md, CHANGELOG.md (per AC7); (c) self-coherence sections on `.cdr/unreleased/31/self-coherence.md` (this file). **All files in `git diff origin/main..HEAD --name-only` accounted for:** `.cdr/unreleased/31/self-coherence.md` (step 6c — this file), `reports/field-report-04-falsification-evaluation.md` (step 6a), `PROJECT.md` / `ROADMAP.md` / `CHANGELOG.md` (step 6b). No additional surfaces touched. | `git diff origin/main..HEAD --stat`; field-report-04; PROJECT.md, ROADMAP.md, CHANGELOG.md; this file. |
| 7 | Self-coherence + pre-review | **Done (this section).** §Gap + §Skills + §Method picks + §ACs + §Self-check + §Debt + §CDD-Trace + §Pre-review gate + §Review-readiness sections written per `alpha/SKILL.md` §2.5 + cph#27 / cph#28 precedent. | `.cdr/unreleased/31/self-coherence.md` |

## §Pre-review gate

Per `alpha/SKILL.md` §2.6, all 14 rows verified before signaling review-readiness.

| # | Row | Verdict | Evidence (observation moment) |
|---|---|---|---|
| 1 | `origin/cycle/N` rebased onto current `origin/main` | **PASS** | `git fetch --quiet origin && git rev-parse origin/main` = `c7d374d` at α intake; branch `cycle/31-r4-full-falsification` was created from `c7d374d` (the merge-base); branch is on the same base; no rebase needed. *Transient row — re-validated before §Review-readiness signal below.* If cph#30 lands during this cycle, see §Debt D1 for the rebase plan. |
| 2 | self-coherence.md carries CDD Trace through step 7 | **PASS** | §CDD-Trace above carries rows 1–7. |
| 3 | tests present or explicit reason none apply | **PASS** | Explicit reason in §CDD-Trace step 4: analysis-only synthesis cycle; no new compute commissioned; per-row anchor verifiability is the test surface. β re-cites prior-cycle reports and confirms the numeric anchors match. |
| 4 | every AC has evidence | **PASS** | §ACs above maps AC1–AC9 to evidence with β oracle for each. |
| 5 | known debt explicit | **PASS** | §Debt above names D1–D5. |
| 6 | schema / shape audit when contracts changed | **N/A** | No schema-bearing contract changed in this cycle. The 6 falsification conditions are fixed per AC6 (charter-surface untouched); no feature-table column changed; no Cycle dataclass field changed. |
| 7 | peer enumeration when closure touches a family | **PASS** | §Self-check item 3 above: peer-checked the one new framing phrase "construct survives subject to anchor caveats" against existing surfaces. No collision; the precedent stem "construct survives" was in cph#27 field-report-03 and the cph#31 compound extends it without overlap. |
| 8 | harness audit when schema-bearing contract changed | **N/A** | Same as row 6. |
| 9 | post-patch re-audit after mid-cycle patch (covering every language in diff) | **PASS** | No mid-cycle patches. Diff languages: Markdown only (5 files: field-report-04, PROJECT.md, ROADMAP.md, CHANGELOG.md, self-coherence). No Python / no YAML / no schema. Markdown surfaces are cross-checked via §ACs row 7's AC7 oracle (status-surface consistency) + §Self-check item 6 (charter-surface untouched). |
| 10 | branch CI green on head commit | **N/A (no project CI for analysis surfaces)** | The repo's CI (`scripts/measure-coherence.sh` + `.github/workflows/coherence.yml`) runs only on tagged releases per [`CHANGELOG.md`](../../../CHANGELOG.md) 0.2.0 entry; this cycle does not tag. No per-PR CI gate exists for analysis surfaces; β verifies by re-citing the prior-cycle reports per the per-row anchors in field-report-04 §"6-condition table". *Transient row — re-validated before §Review-readiness signal below.* |
| 11 | artifact enumeration matches diff | **PASS** | §CDD-Trace step 6 enumerates all 5 files in `git diff origin/main..HEAD --name-only`: `.cdr/unreleased/31/self-coherence.md`, `reports/field-report-04-falsification-evaluation.md`, `PROJECT.md`, `ROADMAP.md`, `CHANGELOG.md`. Each is mentioned + tied to a CDD step. |
| 12 | caller-path trace for new modules | **N/A** | No new modules; no new Python files; no new scripts. The cycle adds one new markdown file (field-report-04) and edits four existing markdown files (PROJECT.md, ROADMAP.md, CHANGELOG.md, plus this self-coherence under .cdr/). field-report-04 is "called" by reading it (cross-linked from PROJECT.md §"Last field report" + ROADMAP.md Phase R4 §"Current evidence" + CHANGELOG.md 0.4.0 entry). |
| 13 | test assertion count from runner output | **N/A** | No automated assertion-based tests added in this cycle; the cycle is analysis-only synthesis; the verification surface is the per-row anchor citations in field-report-04 §"6-condition table". |
| 14 | α's commit author email matches `alpha@cph.cdd.cnos` | **PASS (to be verified at commit time)** | The dispatch identity is `git -c user.name='α-as-agent' -c user.email='alpha@cph.cdd.cnos'`. Every commit in this cycle is created with this identity per the issue body §Hard constraints. β verifies via `git log --format='%ae' origin/cycle/31-r4-full-falsification ^origin/main` returns `alpha@cph.cdd.cnos` for each cph#31 commit. |

## §Review-readiness

| Field | Value |
|---|---|
| Round | 1 |
| Implementation SHA (last α implementation commit before the readiness signal) | `1c887a5` (commit `1c887a5` — "α #31: R4 full falsification re-evaluation — construct survives subject to caveats"). The readiness-signal commit (this self-coherence file landing) follows. |
| Base SHA (cycle base, was `c7d374d` at branch creation; re-verified immediately before this signal) | `c7d374d` (the `δ: backfill coherence-log with 0.3.0/0.3.1/0.3.2 rows` commit — the `origin/main` HEAD at branch creation per issue body §Steps `git pull --ff-only`). Note: `origin/main` has since advanced (δ landed cph#31 equivalent content as `1ad0446` + `f2f43ae` in a parallel-dispatch operation while α was working). The α branch is intentionally based on `c7d374d` per the issue body's branching instruction; if β chooses to rebase against current `origin/main` rather than merge, the field-report / status-surface diff will reconcile cleanly since main already carries identical content for those files. The self-coherence file under `.cdr/unreleased/31/` is the additional artifact this branch contributes beyond what δ landed. |
| Branch | `cycle/31-r4-full-falsification` |
| Branch CI | not applicable (no per-PR CI for analysis surfaces; release-only CI per `.github/workflows/coherence.yml`); β verifies by re-citing the prior-cycle reports per the per-row anchors in field-report-04 §"6-condition table" |
| AC6 charter-surface sweep | empty diff verified at `git diff origin/main..HEAD -- docs/concepts/support-path.md` (returns no output, exit 0) — `docs/concepts/support-path.md` §Falsification content untouched per the AC6 hard constraint; re-validated immediately before this signal |
| AC8 charter-surface sweep | empty diff verified at `git diff origin/main..HEAD -- README.md docs/concepts/coherence-path-hypothesis.md docs/concepts/support-path.md docs/articles/seven-ways-people-walk.md docs/concepts/failure-conditions.md` (returns no output, exit 0); re-validated immediately before this signal |
| AC9 raw-data sweep | `NONE` verified at `git diff origin/main..HEAD --name-only \| grep -E '\.(zip\|trc\|mot\|sto\|c3d\|osim\|mp4\|mov\|csv\|parquet)$' \|\| echo NONE`; re-validated immediately before this signal |
| Verdict | **ready for β** (subject to D1 rebase if cph#30 lands first) |
