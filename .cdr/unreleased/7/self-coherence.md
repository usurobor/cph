<!-- sections: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness] -->
<!-- completed: [Gap, Skills, ACs, Self-check, Debt, CDD-Trace, Review-readiness] -->

# Self-Coherence: Sub C — Inference memo + field report + GO/NO-GO decision

**Issue:** #7
**Mode:** docs-only (with reasoning, per issue)
**Branch:** cycle/7
**Author:** α

## Gap

The field-report template at `reports/field-report-01-existing-data-zeroth-pilot.md` was a stub with every section "(TBD)". No inference memo existed, no GO/NO-GO/REVISE decision was recorded, and `PROJECT.md` was unaware of the cycle outcome. The issue requires a support-path inference memo with ≥3 candidate hypotheses each cited against extracted features and checked against the six falsification conditions; a field report covering all 9 protocol outputs; an explicit GO/NO-GO/REVISE decision; `PROJECT.md` updated.

## Skills

- **Tier 1:** `cdd/CDD.md`, `cdd/SKILL.md`, `cdd/alpha/SKILL.md`
- **Tier 2:** `eng/writing` (durable docs — field report is a durable artifact).
- **Tier 3:** none explicit. Operative constraints: `docs/concepts/support-path.md §"Safe claim"` (strongest allowed sentence form) and `protocols/existing-data-zeroth-pilot.md §"Go/No-Go Criteria"`.

## ACs

### AC1 — ≥3 candidate support-path hypotheses

**Evidence:** Field report §Support-Path Inference contains three named hypotheses:
1. Sagittal-plane dominant load transfer.
2. Trunk-sway induced lateral compensation.
3. Asymmetric phase-coupling between sides.

Each hypothesis: names a coordination pattern; cites supporting features from `analysis/features.md` (e.g. `hip_flexion_range_deg`, `hip_knee_lag_pct_cycle`, `pelvis_list_range_deg`, side-specific deltas); names a falsification path mapped to one or more of the six conditions in `docs/concepts/support-path.md`.

**Oracle:** protocol §"Required Outputs" item 8. AC met.

### AC2 — Falsification check

**Evidence:** Field report §Falsification Assessment evaluates each hypothesis against the six conditions in `docs/concepts/support-path.md`. The honest result on smoke data: 5 of 6 conditions are **not testable** because synthetic data was used (the empirical variation those conditions test is absent by construction). Only condition 5 (extraction-failure on clean data) is empirically meaningful on smoke; it does NOT trigger (0% missingness, 100% segmentation).

**Threshold honesty:** The mechanical falsification score is 0/6 on smoke, well below the 4-condition NO-GO threshold. However, the field report explicitly states that this score is *not* evidence the construct survives — it is evidence the empirical test has not yet run. AC met.

**Negative:** No hypothesis is treated as "established"; the strongest sentence form ("Under this condition, this recording shows this movement pattern") is preserved throughout.

### AC3 — Field report covers all 9 protocol outputs

**Evidence:** Protocol §"Required Outputs" enumerates 9 items. Field report sections (with mapping):

1. Dataset Manifest → §Trial Inventory + §Failure Analysis (cites `data/external/opencap-lab-validation.md`)
2. Walking-Trial Inventory → §Trial Inventory
3. OpenCap/OpenSim Output Inventory → §Export Inventory
4. Gait-Cycle Segmentation Notes → §Segmentation Status
5. Feature Table → §Feature Extraction Status
6. First-Pass Plots → §Appendices §B
7. OpenCap-vs-Reference Comparison → §OpenCap vs Reference Comparison
8. Support-Path Inference Memo → §Support-Path Inference
9. Failure Report → §Failure Analysis

Every numbered output is referenced in the field report. AC met.

### AC4 — Failure report written

**Evidence:** Field report §Failure Analysis names:
- Technical failure: dataset acquisition blocked at SimTK login.
- Technical failure: real-data OpenCap-vs-reference pairing unimplemented (cycle #6 documented debt).
- Data quality issue: speed graduation absent in OpenCap Lab Validation.
- Data quality issue: hip ab/ad-duction features not in first-pass set.
- Pipeline bottleneck: synthetic-data validation circularity.
- Pipeline bottleneck: hard-coded data path.

Each issue is named honestly, with severity and resolution path. AC met.

### AC5 — GO / NO-GO / REVISE decision

**Evidence:** Field report §Go/No-Go Assessment §Recommendation: **REVISE.**

Rationale cites which thresholds apply: GO requires real-data segmentation / extraction / agreement results; smoke results don't satisfy GO. NO-GO requires ≥4 of 6 falsification conditions to trigger; only 1 is testable on smoke (and it doesn't trigger). REVISE names the specific gap (acquisition access mechanism) and recommends a protocol revision adding an "Access mechanism" subsection plus an operator-acquisition runbook.

AC met.

### AC6 — PROJECT.md updated

**Evidence:** `PROJECT.md` §"Current Stage" is updated to "Existing-data zeroth pilot — REVISE" with next-action pointing to the acquisition procedure and the protocol-revision recommendation. `PROJECT.md` §"Realization 04" status is updated from "In progress" to "REVISE" with a pointer to the field report.

AC met.

## Self-check

α-side audit: did α push ambiguity onto β?

- **AC1**: three hypotheses are explicit and individually testable. β can verify each cites real columns from `analysis/features.md` and maps to a falsification condition.
- **AC2**: the falsification table is honest — 5 of 6 conditions named as not-testable-on-smoke, with the explicit caveat that the 0/6 score is not evidence the construct survives.
- **AC3**: the 9-output mapping table is explicit; β can grep the field report for each section header.
- **AC4**: failure modes are honestly named, not hidden in caveats.
- **AC5**: the REVISE decision rationale is structurally complete (why not GO, why not NO-GO, what to revise).
- **AC6**: PROJECT.md changes are surgical (two sections), no scope creep.

Did α outsource authoring work to β? The only deferred work is the actual protocol revision (adding §"Access mechanism" subsection to `protocols/existing-data-zeroth-pilot.md`) — that revision is recommended in the field report but not authored in this cycle, because the issue explicitly puts "Modifying the protocol or features list" in non-goals. The recommendation is correctly scoped; β should verify the non-goal compliance.

Is every claim backed by evidence in the diff?
- Field report sections map 1:1 to AC requirements (verifiable by section headings).
- Falsification table honesty is verifiable by reading the §"Smoke status" line of each hypothesis.
- REVISE decision cites specific protocol thresholds.

## Debt

1. **Real-data hypothesis evaluation.** The three hypotheses are stated and have explicit falsification paths, but cannot be evaluated on the synthetic smoke data. This is named explicitly in the smoke-status line of each hypothesis. Carry to post-acquisition cycle.

2. **Protocol revision authoring.** Field report recommends adding §"Access mechanism" to `protocols/existing-data-zeroth-pilot.md`; the authoring of that subsection is NOT done in this cycle because it is in the issue's non-goals ("Modifying the protocol or features list"). γ should triage this at wave close-out: file a follow-up issue for the protocol revision.

3. **Hip ab/ad-duction features.** Hypothesis 2 references hip ab/ad-duction features that are not in the first-pass feature set. The feature definitions in `analysis/features.md` already include these as candidates; the pipeline implementation (`scripts/features.py`) does not extract them yet. Trivial extension once real OpenCap output column names are confirmed.

4. **Smoke disclaimer salience.** The notebook prints `mode: synthetic-smoke` when real data is absent; the field report carries this caveat throughout; but a future cycle re-running the notebook against real data should refresh the §Trial Inventory, §Segmentation Status, §Feature Extraction Status, and §OpenCap vs Reference Comparison rows with real numbers. The (blocked) rows in those tables are the explicit placeholders that the re-run replaces.

## CDD-Trace

| Step | Artifact | Skills loaded | Decision |
|------|----------|---------------|----------|
| 0 Observe | — | — | Read issue #7, field report template, protocol §Required Outputs, support-path concept, cycle #5/#6 outputs |
| 1 Select | — | — | Gap: empty field report + no decision recorded |
| 2 Branch | cycle/7 | cdd | γ created from origin/main |
| 3 Bootstrap | n/a | cdd | Not required — docs-only cycle |
| 4 Gap | self-coherence §Gap | — | Stub field report → complete report + decision + PROJECT.md update |
| 5 Mode | self-coherence §Skills | cdd, eng/writing | docs-only |
| 6 Artifacts | reports/field-report-01-existing-data-zeroth-pilot.md (rewritten); PROJECT.md (updated) | eng/writing | Field report + PROJECT.md |
| 7 Self-coherence | self-coherence.md | cdd | This file |
| 7a Pre-review | self-coherence.md §Review-readiness | cdd | 6 ACs evidenced; honest REVISE decision; protocol-revision recommendation respects non-goal |

## Review-readiness

Round 1. Cycle branch base SHA: `8997f6f` (origin/main at branch creation). Two files changed:
- `reports/field-report-01-existing-data-zeroth-pilot.md` (rewritten from template).
- `PROJECT.md` (Current Stage + Realization 04 updated).

All six ACs have evidence in the diff. Honest REVISE decision recorded. Ready for β.

**Specific β decision points:**
1. Is the REVISE decision the right call given the smoke-vs-real distinction?
2. Are the three hypotheses adequately framed (each names a coordination pattern, supporting features, and falsification path)?
3. Is the "9 protocol outputs covered" mapping complete?
