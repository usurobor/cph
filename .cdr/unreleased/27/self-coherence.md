---
name: cph-27-self-coherence
description: α self-coherence for cph#27 (R3 — R-side aggregate condition-response analysis on n=60 R cycles, 10 subjects × 2 conditions × 35 columns)
metadata:
  type: cycle-artifact
  cycle: 27
  role: alpha
  mode: explore/analysis
sections:
  planned: [Gap, Skills, MethodPicks, ACs, SelfCheck, Debt, CDDTrace, PreReviewGate, ReviewReadiness]
  completed: [Gap, Skills, MethodPicks, ACs, SelfCheck, Debt, CDDTrace, PreReviewGate, ReviewReadiness]
---

# α self-coherence — cph#27

## §Gap

**Issue:** cph#27 — "R3 — R-side aggregate condition-response analysis (n=60 R cycles)" (`P1`, `surface:data`, `surface:analysis`).

**Incoherence the cycle closes.** After cph#26 (segmentation port → 60/60 R-side trials at 100%; 30 natural + 30 trunk-sway), the project has the *per-cycle* feature table the construct survival hypotheses need, but no inferential statement about whether the features actually respond to condition under the protocol's stated comparison (natural vs trunk-sway), at the inferential unit the protocol requires (*subject*, not cycle, to avoid pseudoreplication). PROJECT.md §"Next action" names R3 explicitly; ROADMAP.md §"Phase R3" status is NOT STARTED with the gate "Subject-level (not cycle-level) condition-response analysis demonstrates stable feature distributions per subject per condition." R3 is the first cycle in the project to produce *construct-level* evidence as distinct from *pipeline-level* evidence (R1 cleared technology stack; R2 cleared detector).

**Scope.** Build per-(subject, condition) aggregates from the existing 60 R-side feature rows; run paired condition-response tests at n=10 subjects; report effect size + 95% CI + p-value with explicit multiple-comparisons handling; write `reports/field-report-03-construct-evaluation.md` evaluating the 6 falsification conditions from `docs/concepts/support-path.md` §Falsification on R-side data; issue a GO/REVISE/NO-GO decision per `protocols/existing-data-zeroth-pilot.md` thresholds, where R1 stays REVISE by cross-cycle binding (only cph#28 can lift it).

**Mode.** explore / analysis — method picks (aggregation, paired-test choice, multiple-comparisons handling) are α's call within AC scope and are documented in §Method picks below; β verifies the choice is recorded and the resulting numbers are reproducible, not which method is "correct" (γ-scaffold §Mode rationale; `issue/SKILL.md` MCA preconditions, all three failed).

**Cross-cycle binding.** cph#27 runs concurrently with cph#28 (L-cycle recovery, branch `cycle/l-cycle-recovery`). The cph#27 issue body §Non-goals binds R1 to remain REVISE regardless of R3 outcome — only cph#28 can lift R1. Highest-status R3 outcome possible: REVISE or partial GO on R-side.

## §Skills

Tier 1 loaded:
- `cnos.cdd/skills/cdd/CDD.md` — canonical lifecycle (referenced; full read not required for analysis cycle)
- `cnos.cdd/skills/cdd/alpha/SKILL.md` — α load order, incremental self-coherence discipline (§2.5), pre-review gate (§2.6)
- `cnos.cdd/skills/cdd/issue/SKILL.md` — AC discipline, MCA preconditions (used to confirm explore mode)

Tier 2 loaded:
- `cnos.core/skills/write/SKILL.md` — field-report-03 prose discipline (one governing question per file; lead with the point; condition-bound language)

Tier 3 loaded (cycle-specific):
- *None as packaged skills.* The cycle is data-analysis-only; no language-specific (`eng/python`, `eng/cli`) authorship discipline applies because no production code is added. The analysis script (`analysis/r3_subject_aggregate_tests.py`) is a single-purpose reproducibility harness, not a library or CLI tool. *Per the dispatch surface, scripts/features.py is upstream and α does not modify it.*

**Domain references (read-only, treated as authoritative):**
- `protocols/existing-data-zeroth-pilot.md` §"Go/No-Go Criteria" — the GO/REVISE/NO-GO thresholds for AC6
- `docs/concepts/support-path.md` §Falsification — the 6 falsification conditions for AC5
- `reports/field-report-01-existing-data-zeroth-pilot.md` — evidence-table format, condition-bound prose, decision-language conventions
- `analysis/features.md` — feature catalog + H1 / H2 / H3 mapping (issue body Approach §"Hypothesis evaluation surface" cites specific features by name)
- `analysis/feature-summary-zeroth-pilot.md` — feature-table provenance (61 cycles × 35 columns, 0.00% missingness)

## §Method picks

Three picks settled before any test ran; rationale below; each pick verified by β as "recorded and reproducible," not as "correct."

### M1 — Aggregation method (AC1): **median AND mean, both reported; median is primary**

**Pick.** For each (subject, condition, feature) triple, aggregate the 3 R-side cycles by *median*. Also report mean. Primary analysis (paired tests, effect sizes, falsification) uses the median aggregate. The mean aggregate is reported alongside as a robustness check.

**Why.** n=3 cycles per (subject, condition) cell. With n=3, a single per-cycle outlier (e.g. a marker-pop or a borderline-quality segmentation) moves the mean by ~33% but moves the median by 0%. The protocol's stated comparison is "natural vs trunk-sway under subject as the inferential unit"; the aggregation step exists to suppress within-subject within-condition cycle-level noise so the cross-subject test is not driven by per-cycle artifacts. Median does this strictly; mean does not. Reporting both lets β confirm the test direction does not flip across aggregations (a directional flip across mean/median would itself be a finding worth reporting).

**Alternative considered.** Mean-only. Rejected because the project's quality_flag is binary (`ok`/`short`/`long`) and excludes only the implausible-cycle-duration tail; it does not catch single-marker-pop artifacts that would distort a 3-sample mean.

### M2 — Paired test (AC2): **Wilcoxon signed-rank**

**Pick.** Wilcoxon signed-rank on the per-subject paired delta (trunk-sway median − natural median) for each numeric feature. Two-sided. Method = `scipy.stats.wilcoxon(..., zero_method="wilcox", alternative="two-sided")`. Reported per feature: test statistic W, two-sided p-value, n_pairs (=10), n_nonzero_pairs.

**Why.** n=10 subjects. With n=10, normality of the paired delta cannot be checked reliably (Shapiro–Wilk is underpowered at n=10 to distinguish "normal" from "heavy-tailed-but-symmetric"). Wilcoxon signed-rank assumes only that the paired-delta distribution is symmetric around its location, which is weaker than the paired t-test's normality assumption and adequate for the inference being made ("under trunk-sway, does this feature shift relative to natural?"). The cost is ~5% loss in power if the distribution actually is normal, which is acceptable for an exploratory cycle.

**Alternative considered.** Paired t-test (Student's). Rejected because it requires either n≥30 (CLT) or normality (which n=10 can't certify). For the cycle's "primary aggregate analysis on R-side n=60" framing, the *inference* unit is the per-subject delta (n=10), not the per-cycle observation (n=60); n=60 governs aggregate precision, not paired-test degrees of freedom.

### M3 — Effect size + 95% CI (AC2): **rank-biserial correlation r_rb with percentile bootstrap 95% CI (B=10,000)**

**Pick.** Per feature, report r_rb = (W_pos − W_neg) / (W_pos + W_neg) where W_pos/W_neg are the sums of positive/negative signed ranks. CI from a non-parametric percentile bootstrap over the n=10 paired deltas, resampling with replacement, B=10,000 iterations, percentile 2.5%–97.5%. Also report the *median paired delta* in the feature's original units for direct mechanistic readability.

**Why rank-biserial.** Wilcoxon's natural effect-size companion is the rank-biserial correlation; range is [−1, 1] with magnitude interpretable as "fraction of cross-condition rank differences that favor trunk-sway minus the fraction that favor natural." (Cohen's d is a t-test–native effect size and presupposes the paired-delta scale Wilcoxon does not use; reporting d alongside Wilcoxon would invite a metric mismatch.)

**Why percentile bootstrap.** Rank-biserial does not have a closed-form analytic CI for paired data; the percentile bootstrap is the standard fallback. n=10 is small enough that BCa would not add meaningful coverage accuracy and is omitted to keep the resampling reading transparent for β's spot-check.

### M4 — Multiple-comparisons handling (AC2): **Benjamini–Hochberg FDR at q=0.05**

**Pick.** Apply BH-FDR (`scipy.stats.false_discovery_control(..., method='bh')`) across the testable numeric features. Report per feature: raw p-value, BH-adjusted p-value (q-value), and "BH-significant at q=0.05" boolean.

**Why FDR over FWER.** The cycle tests on the order of 25 numeric features. Bonferroni at α=0.05 would require p < 0.002 — the test is exploratory and discovery-oriented, and Bonferroni's family-wise error rate guarantee is the wrong loss function for "which features warrant a mechanistic claim worth listing in a field report." BH controls the expected fraction of false positives among rejected nulls, which matches the field report's job (a mechanistic claim that turns out to be a false positive is acceptable if the FDR is bounded; missing a real signal because Bonferroni was over-conservative is the more costly error in an evidence-gathering cycle).

**Why q=0.05.** Convention. Same level used in the protocol's `<20% missingness` and `≥80% segmentation` AC thresholds — choosing q=0.05 here matches the precision regime the project's other ACs already operate in.

**Reported alongside.** Raw p-values are also reported per-feature so β can apply a stricter correction without re-running the analysis.

### M5 — Scope of "35 features" in AC1

**Clarification (not a method pick — an AC interpretation that β should verify).** The issue body claims "10 subjects × 2 conditions × 35 features = 700 aggregate rows." The "35" refers to the 35 *columns* of the per-cycle feature table (per `analysis/feature-summary-zeroth-pilot.md` AC2: "0.00% missingness across 35 columns"). Of those 35 columns:
- 8 are indexing columns (`subject`, `session`, `trial_id`, `condition`, `side`, `cycle_number`, `quality_flag`, `exclusion_flag`) — aggregation is a passthrough or identity.
- 2 are non-numeric metadata sentinels (`timing_estimate_method`, `normalized_curve_available`).
- **25 are numeric features** that aggregate meaningfully and can be tested.

α's aggregate table satisfies AC1's *cell count* (10 × 2 × 35 = 700 cells in the long-format aggregate table, with indexing columns carried through identity) AND honors the spirit of the AC (one aggregate value per (subject, condition, feature) triple) by providing the per-feature numeric aggregates for the 25 testable features. The paired tests in AC2 run on the 25 testable numeric features, not on the 10 non-test columns. β verifies that (a) the aggregate table has 700 cells in long format, (b) the AC2 test list covers the 25 numeric features.

## §ACs

Row-per-AC evidence map. Each AC names the artifact + section + oracle β can re-verify.

| AC | Evidence (artifact §section) | β oracle |
|---|---|---|
| AC1 — 700 per-(subject, condition, feature) aggregate rows; aggregation method documented | `reports/field-report-03-construct-evaluation.md` §"Aggregation surface (AC1)" carries the cell-count derivation (20 (subject × condition) rows × 35 columns = 700 cells; 25 numeric + 8 indexing + 2 metadata sentinel); §"AC1a — Median aggregate (primary)" carries the 20×26 wide-format median table verbatim. `analysis/r3_subject_aggregate_tests.py` §AC1 prints the same derivation and table to stdout. §Method picks §M1 documents median+mean choice. §Method picks §M5 documents the 35-column interpretation. | `python3 analysis/r3_subject_aggregate_tests.py \| grep "20 rows × 35"` returns the 700-cell derivation; the median table in the field report §AC1a has 20 data rows × 26 displayed columns (2 index + 24 abbreviated feature names — full names in §Method picks §M5). |
| AC2 — Paired test per feature with effect size + 95% CI + p-value; explicit MC-handling | `reports/field-report-03-construct-evaluation.md` §"Paired Wilcoxon signed-rank tests (AC2)" carries the 25-row test table with `W`, `r_rb`, `r_rb 95% CI` (percentile bootstrap), `p_raw`, `p_BH`, and a `BH q<.05` significance marker. §Method picks §M2 / §M3 / §M4 document Wilcoxon, rank-biserial+bootstrap, BH-FDR choices and rationale. | β counts rows: 25 features tested. β spot-checks 3 features (e.g. `ankle_angle_range_deg`: W=0; r_rb=−1.0; p_raw=0.002; p_BH=0.012) against the median paired delta in §AC1c and the per-subject deltas — all 10 subjects show negative delta, consistent with r_rb=−1.0. β confirms MC-handling text appears once with rationale (§Method picks §M4). |
| AC3 — H1 ≥3 features, H2 ≥3 features each with mechanistic interpretation; H3 non-testable note | `reports/field-report-03-construct-evaluation.md` §"Hypothesis evidence summary (AC3)" — H1 lists 5 features (≥3 ✓), each with mechanistic interpretation (split into measured signal vs inferred construct reading); H2 lists 9 features (≥3 ✓) with same split; H3 has an explicit non-testable section naming L=1 cycle as the structural reason. | β counts: H1 features ≥3 ✓; H2 features ≥3 ✓; H3 non-testable note present with reason (L=1) ✓. |
| AC4 — ≥3 candidate support-path hypotheses each with 5 named fields | `reports/field-report-03-construct-evaluation.md` §"Candidate support-path hypotheses (AC4)" — 3 candidates (Lateral-trunk substitution path; Distal sagittal contraction under proximal compensation; Cadence-slowdown signature). Each carries a 5-field table: supporting features, expected effect direction, observed effect direction, mechanistic interpretation, condition-bound scope. | β counts: 3 candidates ≥3 ✓; each candidate's 5-field table is present ✓. |
| AC5 — `reports/field-report-03-construct-evaluation.md` written with 6 falsification conditions enumerated | The file exists at the named path. §"Falsification re-evaluation on R-side (AC5)" carries the 6-row condition table; each condition has a verdict (NOT triggered / Not testable) with evidence and an R-side-specific reading. Measured-signal-vs-inferred-construct framing is explicit in §AC3 (H1 / H2 sub-readings) and §AC4 (mechanistic interpretation). Condition-bound language appears throughout (e.g. "Under trunk-sway, R-side gait showed...", "Bound to the deliberate-trunk-perturbation walking condition"). §"Next gates" names L-cycle recovery (cph#28) and full R4 as the next gates. | β verifies the file exists; counts 6 conditions in §AC5 table ✓; spot-checks 5 declarative sentences for condition-bound framing (Executive Summary, §AC3, §AC4); confirms "L-cycle recovery" and "full R4" appear in §"Next gates". |
| AC6 — GO/REVISE/NO-GO decision per protocol; R1 stays REVISE (cross-cycle binding) | `reports/field-report-03-construct-evaluation.md` §"Decision per protocol (AC6)" carries the 5-criterion comparison against `protocols/existing-data-zeroth-pilot.md` §"Go/No-Go Criteria"; verdict is "R3 = partial GO on R-side"; "R1 status: unchanged REVISE" is stated explicitly with cross-cycle binding rationale. PROJECT.md / ROADMAP.md / CHANGELOG.md all reflect partial-GO-on-R-side and REVISE-on-R1 verdicts. | β verifies the decision string `partial GO on R-side` appears in field-report-03 §AC6, PROJECT.md §"Current empirical decision", ROADMAP.md §"Current state", CHANGELOG.md §0.3.1 §Decision. β verifies "R1 status: unchanged REVISE" appears in field-report-03 §AC6 and §Receipt. β verifies R1's status row in ROADMAP.md §"Phase R1" still reads "REVISE" (unchanged from prior). |
| AC7 — PROJECT.md / ROADMAP.md / CHANGELOG.md status patches | `git diff origin/main..HEAD -- PROJECT.md ROADMAP.md CHANGELOG.md` shows R3-status patches: PROJECT.md §"Current empirical decision" + §"Current blocker" + §"Next action" + §"Open issues" + §"Last field report" updated; ROADMAP.md §"Current state" + §"Phase R3" + §"Phase R4" updated; CHANGELOG.md has a new 0.3.1 entry. | β runs the diff command; verifies all three files are modified; spot-checks PROJECT.md §"Last field report" points to field-report-03; CHANGELOG.md 0.3.1 entry has narrative-progress form matching 0.3.0. |
| AC8 — README.md + docs/concepts/{coherence-path-hypothesis,support-path}.md + docs/articles/seven-ways-people-walk.md UNTOUCHED | `git diff origin/main..HEAD -- README.md docs/concepts/coherence-path-hypothesis.md docs/concepts/support-path.md docs/articles/seven-ways-people-walk.md` returns empty (exit 0, no output) — verified at §Pre-review gate row below. | β re-runs the same diff command; verifies empty output. |
| AC9 — No raw data files committed | `git diff origin/main..HEAD --name-only \| grep -E '\.(zip\|trc\|mot\|sto\|c3d\|osim\|mp4\|mov\|csv\|parquet)$' \|\| echo NONE` returns `NONE` — verified at §Pre-review gate row below. | β re-runs the same grep; verifies `NONE`. |

## §Self-check

α's pre-review sweep — does α's work push ambiguity onto β?

**1. Method-pick clarity.** Every numerical choice (median, Wilcoxon, rank-biserial, percentile bootstrap, BH-FDR q=0.05) is named in §Method picks with rationale. β does not have to infer why a method was chosen.

**2. AC1's "35 features" interpretation.** The issue body's "35 features" actually refers to 35 columns of the per-cycle feature table (per `analysis/feature-summary-zeroth-pilot.md`). α surfaced this explicitly in §Method picks §M5 and in field-report-03 §"Aggregation surface (AC1)" rather than silently testing fewer features. β can re-verify the interpretation by reading either surface; the 700-cell oracle is satisfied either way.

**3. Sibling-surface peer enumeration.** α introduced three new candidate-hypothesis names in field-report-03 (Lateral-trunk substitution path; Distal sagittal contraction under proximal compensation; Cadence-slowdown signature). Each was peer-checked against existing surfaces:
- `rg "Lateral-trunk substitution|Distal sagittal contraction|Cadence-slowdown|distal-contraction-under-proximal-compensation|trunk-segment-driven" /root/cph` returns hits *only* in the cycle's new files (field-report-03, PROJECT.md, ROADMAP.md, CHANGELOG.md). No collision with `analysis/`, `docs/`, or `reports/field-report-{00,01,02}`.
- `rg -i "partial GO" /root/cph` returns hits *only* in the cycle's new files + γ scaffold + self-coherence. No prior surface uses "partial GO" semantics for a different concept.
- The term "support path" itself is reserved for the authoritative concept in `docs/concepts/support-path.md`. α uses it only in the AC4-prescribed compound "candidate support-path hypothesis" form, consistent with prior usage in `ROADMAP.md`, `protocols/existing-data-zeroth-pilot.md`, and `docs/concepts/support-path.md`.

**4. Measured-vs-inferred discipline.** Per `docs/concepts/support-path.md` §"Measured vs Inferred", the field report separates measured signal from inferred interpretation in both §AC3 (per-hypothesis: "Mechanistic interpretation (measured signal)" / "Mechanistic interpretation (inferred construct reading)") and §AC4 (per candidate hypothesis: "expected effect direction" vs "observed effect direction" vs "mechanistic interpretation"). No measured feature is called a "support path"; support paths remain inferred candidate organizational patterns.

**5. Cross-cycle binding compliance.** α did not move R1 → GO on any surface. R1's REVISE status is preserved verbatim on ROADMAP.md §"Phase R1" (no edit to that section), and field-report-03 §AC6 + §Receipt + §Cross-cycle binding all carry "R1 status: unchanged REVISE." The partial-GO verdict is bound to R3 on R-side only, not to R1.

**6. Pseudoreplication discipline.** AC1 mandated per-subject aggregation, not per-cycle. α aggregated by (subject, condition) before any cross-subject test; n=10 paired deltas drive every Wilcoxon test, never n=60 cycles. The field report §AC1 surfaces the aggregation step explicitly so β can verify the inferential unit was honored.

**7. Robustness reporting.** α reported both median and mean aggregations and flagged the one feature (`hip_flexion_range_deg`) whose paired-delta sign disagrees between the two aggregations. Both readings of that feature are ns, but the flag is reported so β can spot-check whether any test direction depends on aggregation choice. (It does not: every BH-significant finding holds under both aggregations.)

**8. Reproducibility.** Single command (`python3 analysis/r3_subject_aggregate_tests.py`) reproduces every number in the field report from the read-only features CSV. Bootstrap is deterministic (seed=20260519). β can re-run and diff stdout against the report.

**9. No outsourced authoring.** α did not punt: AC interpretation (35 vs 25 features), method picks, hypothesis framing modifications (e.g. "H1 distal-contraction sub-claim" vs the original "hip-driven" sub-claim), and decision framing (partial GO on R-side) are all explicit in α's surfaces. β verifies, does not author.

## §Debt

**D1 — `tabulate` Python package avoided by inlining a markdown renderer.** When `analysis/r3_subject_aggregate_tests.py` first called `pd.DataFrame.to_markdown()`, the runtime errored on missing `tabulate`. α did not add `tabulate` to `requirements.txt`; instead α inlined a 25-line `df_to_markdown()` helper in the script. Rationale: a single-call dependency is overhead for a single-purpose reproducibility harness; the inline helper has no behavioral coupling to the rest of the analysis and can be deleted if `tabulate` is later added project-wide. *No requirements.txt change made this cycle.*

**D2 — Per-subject within-condition cycle-level repeatability not tested.** With n=3 cycles per (subject, condition), formal ICC / within-subject variance decomposition is statistically thin. The aggregate analysis assumes the median-of-3-cycles is a stable subject-level estimate; the assumption is *consistent with* the observed across-subject pattern (r_rb = ±1.0 on four BH-sig features means the per-subject medians are themselves rank-ordered consistently across conditions) but not directly tested. A future cycle with a longer-trial archive (or a deliberately within-trial-repeated subset) could close this gap. *Not in cph#27 scope.*

**D3 — First-pass PCA / dimensionality reduction on R-side aggregates deferred.** With 25 aggregated features × 10 subjects × 2 conditions, an unsupervised structure scan would be the natural next step in distinguishability testing (falsification condition 6). The notebook §7 "Known debt" cell names this gate; AC3-AC6 of this cycle do not require PCA, and AC8 (no charter drift) plus the cycle's "no clustering yet" non-goal explicitly defers it. *Out of cph#27 scope; held for a future R4-bilateral or R3-extended cycle.*

**D4 — Provisional close-out not written.** Per `alpha/SKILL.md` §2.8, the standard close-out path is γ-requested re-dispatch after β merge. α has not written `alpha-closeout.md` in this cycle; α will write it on re-dispatch after β approval + merge. No provisional close-out fallback used. *Standing pattern; not actual debt unless re-dispatch does not happen.*

**D5 — Pelvis-tilt-mild-coupling candidate hypothesis held below the AC4 line.** `pelvis_tilt_range_deg` trends in the H2-supporting direction (+1.1° median Δ, r_rb = +0.75, raw p = 0.037) but BH-adjusted q = 0.084 does not clear the 0.05 line. α did not promote it to a fourth candidate hypothesis on this cycle because (a) the mechanism overlaps with Candidate 1's secondary observation and (b) AC4's "≥3" floor is met without it. β may surface it as a finding if the evidence reading deserves separate naming. *Reported in field-report-03 §AC4 "Catalogue note".*

## §CDD-Trace

CDD canonical artifact order (per `CDD.md` §5.2 and `alpha/SKILL.md` §2.2):

| Step | Required artifact | Status in this cycle | Surface |
|---|---|---|---|
| 1 | Design artifact (or "not required") | **Not required.** Per γ scaffold §Design, method picks are α's call within AC scope; no design surface to converge on within the cycle. | γ scaffold §Design; §Method picks above |
| 2 | Coherence contract (.cdr/unreleased/{N}/self-coherence.md §Gap or design §Problem) | **Done.** §Gap above names the incoherence in α's words anchored to issue body + γ scaffold. | `.cdr/unreleased/27/self-coherence.md` §Gap |
| 3 | Plan (or "not required") | **Not required.** Per γ scaffold §Plan, the 7-step working sketch in issue body §Steps is α's plan; no separate plan artifact. α executed all 7 steps. | γ scaffold §Plan; issue body §Steps |
| 4 | Tests | **Not applicable as automated test suite** — this is an analysis cycle, not a code-change cycle. The analysis script's "test" surface is the reproducibility property: same input CSV + same script = same numbers (bootstrap seeded). β verifies by re-running `python3 analysis/r3_subject_aggregate_tests.py` and diffing stdout against the field report tables. | `analysis/r3_subject_aggregate_tests.py`; field-report-03 §AC1 / §AC2 / §AC3 / §Appendix A |
| 5 | Code | **Done.** Single new file: `analysis/r3_subject_aggregate_tests.py` (394 lines, single-purpose). No modification to upstream code (scripts/features.py, scripts/segmentation.py, etc.) per dispatch constraints. | `analysis/r3_subject_aggregate_tests.py` |
| 6 | Docs | **Done.** Three categories of doc writes: (a) new field report `reports/field-report-03-construct-evaluation.md` (the cycle's primary artifact); (b) status surface patches on PROJECT.md, ROADMAP.md, CHANGELOG.md (per AC7); (c) self-coherence sections on `.cdr/unreleased/27/self-coherence.md`. **Caller-path trace for new module:** `analysis/r3_subject_aggregate_tests.py` is invoked from the command line (Appendix A of field-report-03 documents the single command); also from the script's `if __name__ == "__main__":` block. It produces the markdown tables that the field-report-03 §AC1 / §AC2 / §AC3 sections cite verbatim. The script is not imported by other code. **All 7 files in `git diff origin/main..HEAD --name-only` accounted for:** `.cdr/unreleased/27/gamma-scaffold.md` (γ artifact carried forward from γ scaffold commit), `.cdr/unreleased/27/self-coherence.md` (α's contract + this trace), `analysis/r3_subject_aggregate_tests.py` (step 5), `reports/field-report-03-construct-evaluation.md` (step 6a), `PROJECT.md` / `ROADMAP.md` / `CHANGELOG.md` (step 6b). | `git diff origin/main..HEAD --stat`; field-report-03; PROJECT.md, ROADMAP.md, CHANGELOG.md; this file. |
| 7 | Self-coherence + pre-review | **Done (this section).** §Gap + §Skills + §Method picks + §ACs + §Self-check + §Debt + §CDD-Trace + §Pre-review gate + §Review-readiness sections written incrementally per `alpha/SKILL.md` §2.5. | `.cdr/unreleased/27/self-coherence.md` |

## §Pre-review gate

Per `alpha/SKILL.md` §2.6, all 14 rows verified before signaling review-readiness.

| # | Row | Verdict | Evidence (observation moment) |
|---|---|---|---|
| 1 | `origin/cycle/N` rebased onto current `origin/main` | **PASS** | `git fetch --quiet origin main && git rev-parse origin/main` = `1d87d4a3` at observation; γ scaffold commit `03ff147` was made from `1d87d4a3` (the merge-base); branch is on the same base; no rebase needed. *Transient row — re-validated before §Review-readiness signal below.* |
| 2 | self-coherence.md carries CDD Trace through step 7 | **PASS** | §CDD-Trace above carries rows 1–7. |
| 3 | tests present or explicit reason none apply | **PASS** | Explicit reason in §CDD-Trace step 4: analysis cycle; reproducibility-property test surface = same script + same input = same output (deterministic seed). β re-runs the script and diffs against the field report. |
| 4 | every AC has evidence | **PASS** | §ACs above maps AC1–AC9 to evidence with β oracle for each. |
| 5 | known debt explicit | **PASS** | §Debt above names D1–D5. |
| 6 | schema / shape audit when contracts changed | **N/A** | No schema-bearing contract changed in this cycle. The features CSV schema is the *input* (read-only, owned upstream by `scripts/features.py` which α does not modify per dispatch constraints). |
| 7 | peer enumeration when closure touches a family | **PASS** | §Self-check item 3 above: peer-checked the three new candidate-hypothesis names + "partial GO" + "support path" against analysis/ + docs/ + reports/. No collisions; all introductions intentional. |
| 8 | harness audit when schema-bearing contract changed | **N/A** | Same as row 6. |
| 9 | post-patch re-audit after mid-cycle patch (covering every language in diff) | **PASS** | No mid-cycle patches. Diff languages: Python (one file: `analysis/r3_subject_aggregate_tests.py`) + Markdown (six files). Python script ran cleanly end-to-end (deterministic output captured at `/tmp/r3_output.md`); Markdown surfaces are linked together via §ACs row 7 + §Self-check items 1–9. |
| 10 | branch CI green on head commit | **N/A (no project CI for analysis surfaces)** | The repo's CI (`scripts/measure-coherence.sh` + `.github/workflows/coherence.yml`) runs only on tagged releases per [`CHANGELOG.md`](../../CHANGELOG.md) 0.2.0 entry; this cycle does not tag. No per-PR CI gate exists for analysis surfaces; β verifies by re-running the reproducibility command in field-report-03 §Appendix A. *Transient row — re-validated before §Review-readiness signal below.* |
| 11 | artifact enumeration matches diff | **PASS** | §CDD-Trace step 6 enumerates all 7 files in `git diff origin/main..HEAD --name-only`: `.cdr/unreleased/27/gamma-scaffold.md`, `.cdr/unreleased/27/self-coherence.md`, `analysis/r3_subject_aggregate_tests.py`, `reports/field-report-03-construct-evaluation.md`, `PROJECT.md`, `ROADMAP.md`, `CHANGELOG.md`. Each is mentioned + tied to a CDD step. |
| 12 | caller-path trace for new modules | **PASS** | §CDD-Trace step 6 documents the caller path for `analysis/r3_subject_aggregate_tests.py`: invoked from command line (per field-report-03 §Appendix A) and from its own `if __name__ == "__main__":` block. Not imported by other code. The script's output is consumed by the field-report-03 §AC1 / §AC2 / §AC3 sections as verbatim markdown tables. |
| 13 | test assertion count from runner output | **N/A** | No automated assertion-based tests added in this cycle; the reproducibility property is the test surface. β can re-run the script and diff against the field report's tables. |
| 14 | α's commit author email matches `alpha@cph.cdd.cnos` | **PASS** | `git log -1 --format='%ae' HEAD` = `alpha@cph.cdd.cnos` at observation; verified across the 5 α commits in §CDD-Trace step 6's enumeration (`git log --format='%ae' origin/cycle/r3-rside-aggregate-analysis ^origin/main` returns `alpha@cph.cdd.cnos` for each α commit, `gamma@cph.cdd.cnos` for the γ scaffold commit). |

## §Review-readiness

| Field | Value |
|---|---|
| Round | 1 |
| Implementation SHA (last α implementation commit before the readiness signal) | `d0435760498ff2c90cbfa9dcdb078ac7301fae4a` (commit `d043576` — "α #27: AC7 status surfaces — R3 partial GO on R-side; R1 stays REVISE"). The readiness signal itself first landed in commit `84df451`; this row is appended in the subsequent commit. |
| Base SHA (cycle base, was `1d87d4a` at γ scaffold; re-verified immediately before this signal) | `1d87d4a3db170bbb6c77e8633bc37a550187fc43` (current `origin/main` at re-validation; `origin/main` has not advanced since γ scaffold; cph#28 has not merged yet — if it lands first, α will rebase and append a fix-round section here) |
| Branch | `cycle/r3-rside-aggregate-analysis` |
| Branch CI | not applicable (no per-PR CI for analysis surfaces; release-only CI per `.github/workflows/coherence.yml`); β verifies reproducibility by re-running `python3 analysis/r3_subject_aggregate_tests.py` per field-report-03 §Appendix A |
| AC8 charter-surface sweep | empty diff verified at `git diff origin/main..HEAD -- README.md docs/concepts/coherence-path-hypothesis.md docs/concepts/support-path.md docs/articles/seven-ways-people-walk.md` (returns no output, exit 0); re-validated immediately before this signal |
| AC9 raw-data sweep | `NONE` verified at `git diff origin/main..HEAD --name-only \| grep -E '\.(zip\|trc\|mot\|sto\|c3d\|osim\|mp4\|mov\|csv\|parquet)$' \|\| echo NONE`; re-validated immediately before this signal |
| Verdict | **ready for β** |
