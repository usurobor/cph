# α closeout — cph#27

Per `cdd/alpha/SKILL.md §2.8`. Voice: factual observations and patterns only; no dispositions (triage is γ/ε).

## Cycle summary

- **Issue:** [usurobor/cph#27](https://github.com/usurobor/cph/issues/27) — R3 R-side aggregate condition-response analysis (n=60 R cycles).
- **Branch:** `cycle/r3-rside-aggregate-analysis` (deleted from origin after merge per β closeout).
- **Mode:** explore / analysis (per γ scaffold §Mode rationale; `issue/SKILL.md` MCA preconditions all failed). Method picks are α's call within AC scope; β verifies "recorded and reproducible," not "correct."
- **Rounds:** 1. APPROVE on first read. Zero RC. Two non-binding observations (N1 = `pelvis_tilt_range_deg` held below AC4 line; N2 = inline `df_to_markdown()` helper avoiding `tabulate` dep) — no action.
- **Implementation SHA:** `8a1a7fa` (α's last commit before β review). **Merge SHA:** `dcf688b`. **Base (`origin/main` pre-cycle):** `1d87d4a`.
- **β verdict commit:** `7a24418` (APPROVE round 1). **β closeout:** `3684f35`.
- **Files merged:** 8 — 1 analysis script (`analysis/r3_subject_aggregate_tests.py`, 394 lines, new module), 1 field report (`reports/field-report-03-construct-evaluation.md`, 308 lines), 3 status surfaces (PROJECT.md / ROADMAP.md / CHANGELOG.md), 3 cycle-dir artifacts (γ scaffold, α self-coherence, β review). Net 1422 insertions / 18 deletions.
- **Cross-cycle binding honored:** R1 status row in `ROADMAP.md §"Phase R1"` deliberately untouched; cph#27 verdict is "partial GO on R-side," R1 stays REVISE; only cph#28 (concurrent on `cycle/l-cycle-recovery`) can lift R1.
- **All commits authored as `alpha@cph.cdd.cnos`** (verified at §Pre-review gate row 14; no identity drift this cycle).

## Observations (factual; no recommendation)

### Pattern: issue-body "35 features" shorthand conflated column-count with testable-feature-count

**Context.** Issue cph#27 body asserts "10 subjects × 2 conditions × 35 features = 700 aggregate rows" as the AC1 cell-count oracle. The "35" comes from `analysis/feature-summary-zeroth-pilot.md` AC2 ("0.00% missingness across 35 columns"). Of those 35 columns: 8 are indexing (`subject`, `session`, `trial_id`, `condition`, `side`, `cycle_number`, `quality_flag`, `exclusion_flag`), 2 are non-numeric metadata sentinels (`timing_estimate_method`, `normalized_curve_available`), and 25 are numeric features that aggregate meaningfully and can be paired-tested.

**Friction.** None at review time — α surfaced the interpretation explicitly in self-coherence §Method picks §M5 and in field-report-03 §"Aggregation surface (AC1)" rather than silently testing fewer features. β re-verified via independent script run (`Aggregate frames shape: (20, 25)`; `AC1 long-format cell count: 700 cells (20 rows × (25 numeric + 10 carry-through indexing/sentinel) = 20 × 35 = 700)`) and confirmed the 700-cell oracle holds either way. Had α tested only 25 features without surfacing the 35→25 column reading, β would have hit a quantity-vs-test-population mismatch on first read.

**Pattern surface.** The pattern is "issue-body shorthand that conflates the schema-shape count with the testable-population count when the schema carries non-numeric columns and the inferential test only applies to a subset." Surfaces where this can recur: `cnos.cdd/skills/cdd/issue/SKILL.md` (issue-author AC discipline — naming the testable-population count separately from the schema-shape count); `cnos.cdd/skills/cdd/alpha/SKILL.md §2.5` (self-coherence §Method picks / §AC interpretation discipline — α surfaces the interpretation rather than silently subsetting); `cnos.cdd/skills/cdd/gamma/SKILL.md` (γ scaffold per-AC oracle hints — flagging when an AC's numeric oracle has an interpretive layer).

### Pattern: cross-cycle binding enforced by surface omission rather than overwrite

**Context.** cph#27 ran concurrently with cph#28 on `cycle/l-cycle-recovery` (L-cycle recovery). The cph#27 issue body §Non-goals binds R1 to remain REVISE regardless of R3 outcome; only cph#28 can lift R1. R3's "partial GO on R-side" verdict therefore had to be propagated to PROJECT.md / ROADMAP.md / CHANGELOG.md *without* editing the R1-status row in `ROADMAP.md §"Phase R1"`.

**Friction.** None. α executed the binding by *not editing* the R1-status row in ROADMAP.md (verified at β review §AC6 "ROADMAP.md §Phase R1: status line unchanged from main (no edit to that section per `git diff origin/main..HEAD -- ROADMAP.md` — only Current state, Phase R3, Phase R4 sections touched)"). PROJECT.md / ROADMAP.md §"Current state" / CHANGELOG.md / field-report-03 each carry "R1 stays REVISE" in prose where the R3 verdict appears, but the canonical R1 status row was preserved verbatim. β diff-sweep `git diff origin/main..HEAD -- PROJECT.md ROADMAP.md CHANGELOG.md | grep -E '^\+.*R1.*GO|^\-.*R1.*REVISE'` returned nothing.

**Pattern surface.** The pattern is "cross-cycle binding satisfied by leaving the canonical status row of the bound-cycle untouched while declaring the binding in prose around the unbound-cycle's verdict." Surfaces where this would recur: `cnos.cdd/skills/cdd/CDD.md §Tracking` (cross-cycle coordination — what is the load-bearing surface for binding-preservation? The omitted-edit or the prose declaration?); `cnos.cdd/skills/cdd/gamma/SKILL.md` (γ scaffold §Cross-cycle coordination — γ's scaffold for cph#27 carried this binding load-bearingly, and the convention propagated cleanly to α + β); `cnos.cdd/skills/cdd/beta/SKILL.md` (β's diff-sweep for "no `R1 → GO` patch anywhere in the diff" as the binding-verification oracle — already exercised this cycle, named here for surface continuity).

### Pattern: analysis-cycle test surface is the reproducibility property, not assertion count

**Context.** cph#27 is analysis-mode (no production code; no library or CLI tool added). The "test" surface is `analysis/r3_subject_aggregate_tests.py`'s deterministic-output property: same input CSV + same script + same seed (20260519) = same numbers. β re-runs the script and diffs stdout against the field report's verbatim markdown tables.

**Friction.** None. α marked §Pre-review gate row 13 ("test assertion count from runner output") as `N/A` with the explicit reason "the reproducibility property is the test surface." β accepted the substitution and verified by independent re-run (every AC1 / AC1c / AC2 / AC3 / Appendix-A cell reproduced verbatim, including bootstrap CIs at B=10,000).

**Pattern surface.** The pattern is "analysis cycles where the test surface is the reproducibility property, not a unit-test assertion count, and the pre-review gate row 13 admits `N/A` with a named substitution oracle." Surfaces where this is load-bearing: `cnos.cdd/skills/cdd/alpha/SKILL.md §2.6` row 13 (the row already admits N/A, but the substitution oracle — "stdout diff against the field report tables, with deterministic seed" — is the part β actually exercises; whether to name this oracle pattern explicitly in the row is a separate question); `cnos.cdd/skills/cdd/beta/SKILL.md` (β's review-time oracle for analysis cycles; the cycle exercised "re-run script → diff stdout against report markdown" cleanly, and the convention is portable to future analysis cycles); `cnos.eng/skills/eng/python` if any analysis-cycle reproducibility-property discipline lives there.

## Out-of-scope follow-ups carried forward (named, not filed)

These are documented in self-coherence §Debt + are reachable on top of this merge:

1. **D1 — `tabulate` Python package not added; inline `df_to_markdown()` helper used instead.** A 25-line stdout-rendering helper in `analysis/r3_subject_aggregate_tests.py` (no behavioral coupling to numerics). β verified at N2 in beta-review.md §Findings. Acceptable for a single-purpose reproducibility harness; deletable if `tabulate` is later added project-wide.

2. **D2 — Per-subject within-condition cycle-level repeatability (ICC / within-subject variance decomposition) not formally tested.** With n=3 cycles per (subject, condition), formal ICC is statistically thin. The aggregate analysis assumes median-of-3 is a stable subject-level estimate; the assumption is consistent with the observed r_rb=±1.0 on four BH-sig features but not directly tested. A future cycle with a longer-trial archive or a deliberately within-trial-repeated subset could close this gap.

3. **D3 — First-pass PCA / dimensionality reduction on R-side aggregates deferred.** With 25 aggregated features × 10 subjects × 2 conditions, an unsupervised structure scan would be the natural next step for falsification condition 6 ("distinguishable coordination signatures"). cph#27 explicitly held this below the line; held for a future R4-bilateral or R3-extended cycle.

4. **D5 — `pelvis_tilt_range_deg` held below the AC4 candidate-hypothesis line.** Trends in H2-supporting direction (+1.1° median Δ, r_rb=+0.75, raw p=0.037, BH q=0.084). Held because (a) mechanism overlaps Candidate 1's secondary observation and (b) AC4's ≥3 floor is met without it. Surfaces honestly in field-report-03 §AC4 "Catalogue note" and self-coherence §Debt §D5. β concurred at N1 in beta-review.md §Findings.

5. **cph#28 (L-cycle recovery) — R1's REVISE→? gate.** Ran concurrently with cph#27 on `cycle/l-cycle-recovery`. R3's "partial GO on R-side" verdict does not lift R1. cph#28 owns the R1 transition gate; field-report-03 §"Next gates" and PROJECT.md / ROADMAP.md / CHANGELOG.md all name cph#28 as R1's gate owner.

6. **Full R4 — bilateral falsification table at adequate n.** Named as the downstream gate in field-report-03 §"Next gates" and ROADMAP.md §"Phase R4" (which moved from `NOT STARTED` to `Partially evaluable on R-side` this cycle). Not in cph#27 scope.

7. **cph#27 issue close.** Auto-closed by `Closes #27` in β's merge commit (`dcf688b`) per β closeout §Merge evidence. No δ/operator follow-up needed for issue lifecycle.

## CDD-iteration candidacy

α voice rule §2.8 forbids dispositions — the following is named only, not recommended for ε to act on:

- **Pattern 1** (issue-body shorthand conflating schema-shape count with testable-population count): same finding class as intra-doc-repetition / measured-vs-inferred discipline already named in `cdd/alpha/SKILL.md §2.3` and `docs/concepts/support-path.md`, but on the *issue-author* surface rather than the artifact-author surface. Whether `cdd/issue/SKILL.md` needs an explicit "name the testable-population count separately from the schema-shape count" row vs. relying on α's §Method picks to surface the interpretation is ε's call.

- **Pattern 2** (cross-cycle binding enforced by surface omission): the binding worked cleanly this cycle because γ's scaffold carried the binding load-bearingly into the α/β dispatch. Whether `cdd/CDD.md §Tracking` should name "the canonical status row of a bound cycle is preserved by omission, with the binding declared in prose around the unbound cycle's verdict" as a recurring pattern — vs. leaving it as a per-cycle γ-scaffold convention — is ε's call. Whether `cdd/beta/SKILL.md` should name the diff-sweep oracle (`grep -E '^\+.*{bound-cycle}.*GO|^\-.*{bound-cycle}.*REVISE'`) for binding-verification is also ε's call.

- **Pattern 3** (analysis-cycle test surface = reproducibility property): `cdd/alpha/SKILL.md §2.6` row 13 already admits N/A; what worked this cycle is the *substitution oracle* — deterministic seed + single-script run + stdout=table-text + β-side re-run-and-diff. Whether to name this oracle pattern explicitly in row 13 (for analysis-mode cycles), or to leave the N/A row as generic and rely on per-cycle α discipline, is ε's call. Same pattern class as the broader question of how non-code cycles fit the test-evidence gate.
