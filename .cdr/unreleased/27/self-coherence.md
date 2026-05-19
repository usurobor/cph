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
  completed: [Gap, Skills, MethodPicks]
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
