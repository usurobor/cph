# γ scaffold — cph#27

R3 — R-side aggregate condition-response analysis (n=60 R cycles).

## §Issue

**cph#27** — "R3 — R-side aggregate condition-response analysis (n=60 R cycles)" — labels: `P1`, `surface:data`, `surface:analysis`.

The cycle's purpose: test whether the per-cycle features named in `analysis/features.md` show stable, interpretable coordination signatures at the subject level under condition response (natural vs trunk-sway) on the R-side n=60 surface that cph#26 anchored. This is the first construct-level evidence cycle in the R-line. It runs in parallel with cph#28 (L-cycle recovery). Aggregation unit is *subject* (not cycle) to avoid pseudoreplication. The hypothesis evaluation surface covers H1 (sagittal-dominant load transfer) and H2 (trunk-sway compensation); H3 is explicitly non-testable on this archive (L=1 cycle). Decision space is `REVISE / partial GO on R-side / NO-GO`; the issue body's §Non-goals binds R1 to remain REVISE regardless of R3 outcome (only cph#28 can lift R1).

Fetch full body: `gh issue view 27 --repo usurobor/cph --json title,body,labels`.

## §Mode

**explore** (analysis cycle; not MCA).

**Mode-precondition rationale.**
- (1) Design not committed: aggregation method (mean / median / both) is α's call per AC1; paired-test choice (Wilcoxon vs paired-t) is α's call per AC2; multiple-comparisons handling is α's call per AC2. No converged design artifact exists at a stable path.
- (2) Plan not committed: the issue body §Steps is a 7-bullet working sketch, not a sequenced plan committed at a stable path.
- (3) Stability not given: method picks may shift during analysis as α reads the empirical surface.

Per `issue/SKILL.md` MCA preconditions, failing any one of the three triggers `explore`. Failing all three with the gap nonetheless real triggers `explore`, not `design-and-build` — there is no design surface to *converge* on within this cycle; the method picks are documented in α's `self-coherence.md` and verified by β as part of AC1/AC2 evidence.

## §Design

Not required for this cycle. Method picks are α's call per AC, documented in α's `self-coherence.md`:
- AC1: aggregation method (mean / median / both)
- AC2: paired-test choice (Wilcoxon signed-rank vs paired t) + justification
- AC2: multiple-comparisons handling (BH-FDR / Bonferroni / no-correction-with-rationale)

These are method picks, not pre-cycle design. β verifies the choice is recorded and the resulting numbers are reproducible from the choice — β does not adjudicate which method is "correct."

## §Plan

Not required for this cycle. The 7 bullets in the issue body §Steps form α's working plan:
1. Build per-(subject, condition) aggregates from the existing feature table.
2. Generate plots: feature distributions per (subject, condition); subject-paired deltas; per-feature condition-response strip plots.
3. Run paired condition-response tests (one method per feature; document the choice).
4. Compute effect sizes (Cohen's d for paired-t; rank-biserial for Wilcoxon).
5. Write `reports/field-report-03-construct-evaluation.md`.
6. Update status surfaces (PROJECT.md, ROADMAP.md, CHANGELOG.md) to reflect R3 status.
7. Commit + push to `cycle/r3-rside-aggregate-analysis`.

## §ACs (verbatim from cph#27 body)

### AC1 — Per-subject-condition aggregates produced

One aggregate row per (subject, condition, feature) — 10 subjects × 2 conditions × 35 features = 700 aggregate rows. Aggregation method documented (mean / median / both).

### AC2 — Subject-paired tests run on every feature

For each feature: paired test between natural and trunk-sway aggregates, n=10 subjects. Effect size + 95% CI + p-value reported. Multiple-comparisons handling explicit (BH-FDR, Bonferroni, or "no correction with rationale").

### AC3 — H1 and H2 evidence summary

- H1: ≥3 features tested with mechanistic interpretation
- H2: ≥3 features tested with mechanistic interpretation
- H3: explicit non-testable note with reason (L=1 cycle)

### AC4 — At least 3 candidate support-path hypotheses

Each hypothesis names:
- which features support it
- expected effect direction
- observed effect direction
- mechanistic interpretation
- condition-bound scope

### AC5 — `field-report-03-construct-evaluation.md` written

- Distinguishes measured signal from inferred interpretation
- Uses condition-bound language ("under trunk-sway, subjects showed X")
- States GO/NO-GO/REVISE decision against protocol thresholds
- Explicitly evaluates the 6 falsification conditions from `docs/concepts/support-path.md` §Falsification on R-side data; non-evaluable conditions named with reason
- Names L-cycle recovery and full R4 as the next gates

### AC6 — Decision per protocol (likely REVISE/partial)

R3 cannot transition R1 to GO while the L-cycle bottleneck holds. A "REVISE" or "partial GO on R-side" decision is the highest-status outcome possible. NO-GO is allowed if R-side data fails the construct-survival tests in `docs/concepts/support-path.md` §Falsification.

### AC7 — Status surfaces realigned

- `PROJECT.md` §"Current empirical decision" / §"Current blocker" / §"Next action" / §"Last field report" updated
- `ROADMAP.md` R3 status updated; R4 status reflects which falsification conditions are R-side-evaluable
- `CHANGELOG.md` entry for this cycle (suggested version: `0.3.1` or `0.4.0`)

### AC8 — No empirical drift on charter

- `README.md` / `docs/concepts/coherence-path-hypothesis.md` / `docs/concepts/support-path.md` / `docs/articles/seven-ways-people-walk.md` untouched
- Empirical-state language consistent across PROJECT.md / ROADMAP.md / CHANGELOG.md / field-report-03

### AC9 — No data policy regression

No raw participant data, no `.zip`/`.trc`/`.mot`/`.sto`/`.c3d`/`.osim`/`.mp4`/`.mov`/`.csv`/`.parquet` files committed. Aggregate tables in the field report are derived.

## §Cycle scope sizing

9 ACs lands in the at-edge (8–10) band per `issue/SKILL.md`. Five-factor reading:

| Factor | Reading | Splitting signal? |
|---|---|---|
| (a) New code surface | 0 new modules; 0 new runtime contracts. Analysis produces a field-report and a derived aggregate table embedded in the report; no library/package additions. | No |
| (b) Cross-module breadth | Reads `scripts/features.py`, `analysis/feature-summary-zeroth-pilot.md`, `notebooks/existing-data-processing.ipynb`; writes one new report (`reports/field-report-03-construct-evaluation.md`) + small status-surface patches (PROJECT/ROADMAP/CHANGELOG). One write surface, three small status patches. | No |
| (c) Lifecycle span | Single phase: analysis → docs. No design / code / infra serialization required. | No |
| (d) MCA preconditions | Not MCA — method picks (aggregation, paired-test, MC-handling) are intentionally α's call within AC scope. Mode is explore (§Mode above). | Not applicable (no signal) |
| (e) Independent shippability of AC groups | ACs form one artifact chain: AC1 produces aggregates → AC2 runs tests on those aggregates → AC3/AC4 interpret those tests → AC5 lands the report → AC6 is the report's decision → AC7/AC8/AC9 are guardrails on the same write surface. No AC subset ships independently of `field-report-03`. | No |

**Decision: keep whole.** Justification: zero "yes" signals across five factors. All 9 ACs build one report from one aggregate table over one read surface; splitting would create artifact-chain dependencies (sub-B blocks on sub-A's merge of the aggregate table) which `issue/SKILL.md` names as an anti-pattern. ACs 6–9 are guardrails (decision-per-protocol, status realignment, no charter drift, no data regression) that belong on the same write surface they constrain.

## §Cross-cycle coordination

**Partner cycle — verbatim from γ dispatch.**

| Field | Value |
|---|---|
| Partner issue | cph#28 — "L-cycle recovery — contralateral-anchored detection or wider IK windows" |
| Partner branch | `cycle/l-cycle-recovery` |
| Partner mode | implementation (α picks path (a) contralateral-anchored detection OR (b) wider IK windows) |

**Shared file surfaces (both cycles touch these — NOT file-disjoint):**
- `PROJECT.md` §"Current empirical decision" / §"Current blocker" / §"Next action"
- `ROADMAP.md` (cph#28 *may* flip R1 REVISE → GO if bilateral coverage achieves AC1 ≥80% on both sides AND L≥10; **cph#27 explicitly cannot flip R1**)
- `CHANGELOG.md` (both add an entry)
- `analysis/feature-summary-zeroth-pilot.md` + `notebooks/existing-data-processing.ipynb` (cph#28 reruns the notebook after L-recovery; cph#27 builds aggregates from the existing feature table)

**Recommended merge order (named here; not enforced — that is a future δ gate).**

cph#28 merges first if it achieves AC1; this either (a) lifts R1 → GO (then cph#27 runs on the updated empirical state) or (b) holds R1 at REVISE with documented recovery method (then cph#27 runs on the existing REVISE state). cph#27's α will need to rebase onto post-cph#28 main if cph#28 merges first.

**R1 binding (verbatim from γ dispatch).** cph#27 cannot lift R1; only cph#28 can. The cph#27 issue body §Non-goals names this explicitly ("Changing R1 status to GO (L-cycle bottleneck still active; R3 cannot lift R1)"). A REVISE or "partial GO on R-side" verdict is the highest-status outcome possible for cph#27.

**Where this surfaces.** The α dispatch surface (§α dispatch surface) carries this binding so α sees it before deciding decision-language in the field report. The β dispatch surface (§β dispatch surface) carries it so β rejects any commit that attempts to move R1 → GO.

## §α dispatch surface

| Field | Value |
|---|---|
| Mode | explore / analysis |
| Branch | `cycle/r3-rside-aggregate-analysis` |
| Identity | `alpha@cph.cdd.cnos` |
| ACs to satisfy | AC1 — AC9 (verbatim in §ACs above) |
| Issue link | `gh issue view 27 --repo usurobor/cph --json title,body,state,labels,comments` |
| Self-coherence path | `.cdr/unreleased/27/self-coherence.md` |
| Review-readiness signal | bottom-of-`self-coherence.md` §"Review-readiness" section |

**Standing reading list (α reads each before writing):**
- cph#27 issue body (full)
- `protocols/existing-data-zeroth-pilot.md` (decision thresholds for AC6)
- `docs/concepts/support-path.md` §Falsification (6 conditions for AC5)
- `reports/field-report-01-existing-data-zeroth-pilot.md` (cph#22 anchor; reference for evidence-table format and tone)
- `analysis/feature-summary-zeroth-pilot.md` (the 35-column R-side feature table)
- `analysis/features.md` (feature catalog + H1/H2/H3 mapping)
- `scripts/features.py` (feature computation; do not modify)
- `notebooks/existing-data-processing.ipynb` (feature-table provenance; do not re-execute unless aggregation requires it)
- `PROJECT.md`, `ROADMAP.md`, `CHANGELOG.md` (status surfaces that α patches per AC7)

**Non-goals (carried verbatim from issue body):**
- L-side data (separate cycle; runs in parallel)
- Friend pre-pilot recruitment
- Clustering, UMAP, or any ML modeling
- CPH validation claims
- Validating the seven gait families
- Charter surface edits (README, `docs/concepts/coherence-path-hypothesis.md`, `docs/concepts/support-path.md`, `docs/articles/seven-ways-people-walk.md`)
- Raw participant data commits
- **H3 (asymmetric phase-coupling)** — explicitly not testable on this archive; do not attempt
- Changing R1 status to GO (L-cycle bottleneck still active; R3 cannot lift R1)

## §β dispatch surface

| Field | Value |
|---|---|
| Branch | `cycle/r3-rside-aggregate-analysis` |
| Identity | `beta@cph.cdd.cnos` (β ≠ α as commit author) |
| ACs to verify | AC1 — AC9 (each verified independently against source surfaces) |
| Inputs | `.cdr/unreleased/27/self-coherence.md` (α's gap, mode, ACs, method picks, review-readiness); `reports/field-report-03-construct-evaluation.md`; the diff on `cycle/r3-rside-aggregate-analysis` vs `origin/main` |
| Output | `.cdr/unreleased/27/beta-review.md` (round 1 verdict APPROVE \| REQUEST CHANGES) |
| Merge authority | β (`git merge --no-ff cycle/r3-rside-aggregate-analysis` on main after APPROVE; β pushes main; β deletes the cycle branch from origin) |
| Tag / release authority | NO (δ-only gate) |
| Fix-round protocol | Per `CDD.md` §1.6a — RC verdict returns to α; α appends a `## Fix-round N` section to `self-coherence.md`; β re-reviews when the branch transition fires |

**Per-AC independent oracle hints (β does not anchor on α's claims — re-checks the source surface):**

| AC | β oracle hint |
|---|---|
| AC1 | Count aggregate rows in `field-report-03`'s aggregate table: must be 10 × 2 × 35 = 700 (or compatible long/wide layout that totals 700 cells). α's method note (mean/median/both) must appear in `self-coherence.md` §Method picks. |
| AC2 | For each of the 35 features the report names a test statistic + effect size + 95% CI + p-value. The MC-handling choice appears once with rationale. Spot-check 3 features by reading the underlying aggregates against the reported test direction. |
| AC3 | grep `field-report-03` for ≥3 features supporting H1 and ≥3 features supporting H2; an explicit H3-non-testable note with the L=1 reason. |
| AC4 | ≥3 candidate support-path hypotheses; each names features / expected direction / observed direction / mechanistic interpretation / condition-bound scope. |
| AC5 | `reports/field-report-03-construct-evaluation.md` exists. Language audit: spot-check 5 declarative sentences for condition-bound framing ("under trunk-sway, ..."). All 6 falsification conditions from `docs/concepts/support-path.md` §Falsification appear by name with R-side evaluability + outcome. |
| AC6 | Decision GO / REVISE / NO-GO appears explicitly. Verify R1 remains REVISE on the empirical surface; verify decision is on R3 only, not on R1. |
| AC7 | `git diff origin/main..HEAD -- PROJECT.md ROADMAP.md CHANGELOG.md` shows R3-status patches; ROADMAP §R4 reflects R-side evaluability; CHANGELOG has one new entry. |
| AC8 | `git diff origin/main..HEAD -- README.md docs/concepts/coherence-path-hypothesis.md docs/concepts/support-path.md docs/articles/seven-ways-people-walk.md` is empty. |
| AC9 | `git diff origin/main..HEAD --name-only \| grep -E '\.(zip\|trc\|mot\|sto\|c3d\|osim\|mp4\|mov\|csv\|parquet)$' \|\| echo NONE` returns NONE. |

**Cross-cycle binding (β enforces).** Any patch that moves R1 REVISE → GO is a blocking finding. R1 status is bound to cph#28's L-cycle recovery; cph#27 cannot lift it. See §Cross-cycle coordination above.
