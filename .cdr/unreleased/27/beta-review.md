---
name: cph-27-beta-review
description: β review verdict for cph#27 (R3 R-side aggregate condition-response analysis)
metadata:
  type: cycle-artifact
  cycle: 27
  role: beta
sections:
  planned: [Round1Header, GammaArtifactPresence, ACVerification, BetaAdditionalVerification, Findings, Verdict]
  completed: [Round1Header, GammaArtifactPresence, ACVerification, BetaAdditionalVerification, Findings, Verdict]
---

# β review — cph#27

## Round 1

| Field | Value |
|---|---|
| Round | 1 |
| SHA reviewed (cycle/r3-rside-aggregate-analysis head) | `8a1a7fa832ec005936f5a3cb984a85ad67bd874c` |
| Base SHA (`origin/main` at review time) | `1d87d4a3db170bbb6c77e8633bc37a550187fc43` |
| α's review-readiness signal | `.cdr/unreleased/27/self-coherence.md` §Review-readiness, round 1, verdict "ready for β" |
| Identity | `beta@cph.cdd.cnos` |
| Reviewer | β |
| Verdict | **APPROVE** |

## §3.11b — γ-artifact presence (non-binding observation)

γ scaffold present at `.cdr/unreleased/27/gamma-scaffold.md` (commit `03ff147`, author `gamma@cph.cdd.cnos`, 195 lines). γ ≠ δ for this cycle — the scaffold carries γ's mode declaration, cycle-scope-sizing reading, cross-cycle coordination binding, α/β dispatch surfaces, and per-AC oracle hints. No γ=δ collapse observed for cph#27. Non-binding observation per §3.11b.

## AC verification

### AC1 — Per-subject-condition aggregates produced

**β independent oracle.**

Ran `python3 analysis/r3_subject_aggregate_tests.py` against the input CSV at `/opt/gait-data/cph-features/features-zeroth-pilot.csv` (61 rows × 35 columns; 60 R + 1 L; not committed per AC9). Script exited 0. Output reports:

- `Total per-cycle columns: 35` (matches issue body and `analysis/feature-summary-zeroth-pilot.md` AC2)
- `Aggregate frames shape: (20, 25)` = 20 (subject × condition) rows × 25 numeric features
- `AC1 long-format cell count: 700 cells (20 rows × (25 numeric + 10 carry-through indexing/sentinel) = 20 × 35 = 700)`

Cell-count oracle: **700 ✓**.

Aggregation method named in self-coherence.md §Method picks §M1 ("median primary + mean robustness") and in field-report-03 §"Method picks" table row. Rationale appears once with named-alternative-rejected ("Mean-only. Rejected because the project's quality_flag is binary..."). **Aggregation method documented ✓**.

Spot-check 3 (subject, condition, feature) cells against the script output:
- `subject10 / walking / cycle_duration_s` = 0.9 (script) vs 0.90 (report line 46) ✓
- `subject3 / walkingTS / lumbar_bending_range_deg` = 52.928 (script) vs 52.93 (report line 53) ✓
- `subject9 / walkingTS / ankle_angle_range_deg` = 29.191 (script) vs 29.19 (report line 65) ✓

α's §M5 clarification (35 columns = 8 indexing + 2 metadata sentinels + 25 numeric tested) is honest about the AC1 cell-count interpretation. The 700-cell oracle holds either way (25 + 10 = 35 columns at 20 rows = 700 cells). **AC1 PASS.**

### AC2 — Subject-paired tests run on every feature

**β independent oracle.**

The AC2 test table in field-report-03 (lines 93–119) has 25 feature rows with columns `H | median Δ | n_nz/n | W | r_rb | r_rb 95% CI | p_raw | p_BH | BH q<.05`. Method picks named in self-coherence.md §Method picks §M2 (Wilcoxon signed-rank, two-sided), §M3 (rank-biserial r_rb + percentile bootstrap 95% CI, B=10,000, seed=20260519), §M4 (BH-FDR at q=0.05) with one-line rationale each. **Test-statistic + effect size + CI + p-value + MC handling each named once with rationale ✓**.

Re-ran the script; every AC2 row reproduces exactly. Spot-check 3 features:
- `ankle_angle_range_deg` (H1): script `W=0.0, r_rb=-1.000, CI=[-1.000, -1.000], p_raw=0.002, p_BH=0.012, *`; report identical ✓. Direction sanity: all 10 per-subject deltas negative in AC1c (-9.35 to -2.36) → r_rb=-1.0 consistent ✓.
- `lumbar_bending_range_deg` (H2): script `W=0.0, r_rb=1.000, p_raw=0.002, p_BH=0.012, *`; report identical ✓. All 10 deltas positive (+14.47 to +34.34) → r_rb=+1.0 consistent ✓.
- `hip_knee_lag_samples`: script `W=0.0, r_rb=1.000, p_raw=0.004, p_BH=0.020, *`; report identical ✓. 9/10 positive (+1 to +5), one zero (subject6) → r_rb=+1.0 on nonzero pairs consistent with the script's nz-only rank-biserial formula ✓.

MC-handling appears once with rationale (self-coherence §M4 + field-report-03 §"Method picks" table); raw p-values reported alongside per row. **AC2 PASS.**

### AC3 — H1 and H2 evidence summary

**β independent oracle.**

Field-report-03 §"Hypothesis evidence summary (AC3)" §H1 lists 5 features (`hip_flexion_range_deg`, `knee_angle_range_deg`, `ankle_angle_range_deg`, `hip_knee_lag_pct_cycle`, `peak_knee_flexion_phase` — all 5 expected per issue body §"Hypothesis evaluation surface"). **H1 ≥3 ✓**. Each carries measured-signal + inferred-construct interpretation split.

§H2 lists 9 features (`lumbar_extension_range_deg`, `lumbar_bending_range_deg`, `lumbar_rotation_range_deg`, `pelvis_tilt_range_deg`, `pelvis_list_range_deg`, `pelvis_rotation_range_deg`, `hip_adduction_range_deg`, `hip_adduction_peak_deg`, `hip_adduction_min_deg` — all 9 expected per issue body). **H2 ≥3 ✓**. Same measured-vs-inferred split.

§H3 explicit non-testable note: *"1 L-side cycle in the archive (subject8 walkingTS1); no R/L pairs at matching (subject, cycle_number) for any subject. R3's R-only design cannot evaluate H3; cph#28's L-cycle recovery owns this gate."* The L=1 reason is named with provenance (script output confirms `(df['side']=='L').sum() == 1`, subject8 walkingTS1). **H3 non-testable note with L=1 reason ✓**.

**AC3 PASS.**

### AC4 — At least 3 candidate support-path hypotheses

**β independent oracle.**

§"Candidate support-path hypotheses (AC4)" surfaces three candidates:
1. **Lateral-trunk substitution path** (5-field table: features / expected direction / observed direction / mechanistic interpretation / condition-bound scope all present)
2. **Distal sagittal contraction under proximal compensation** (5-field table present)
3. **Cadence-slowdown signature** (5-field table present)

Catalogue note explicitly defers `pelvis_tilt_range_deg` below the AC4 line (trending, q=0.084), preserving honest reporting without inflating the candidate count. **3 ≥ 3 ✓; 5 fields per candidate ✓**.

**AC4 PASS.**

### AC5 — `field-report-03-construct-evaluation.md` written

**β independent oracle.**

File exists at `/root/cph/reports/field-report-03-construct-evaluation.md` (308 lines).

Condition-bound language spot-check (5 declarative sentences):
- L13 (Executive summary): *"Under trunk-sway, R-side gait showed seven Benjamini–Hochberg–significant..."* ✓
- L139 (H1 measured-signal): *"Under trunk-sway, R-side ankle range decreases by 6.6°..."* ✓
- L163 (H2 measured-signal): *"Under trunk-sway, R-side lumbar bending range increases by 18.3°..."* ✓
- L187 (Candidate 1 condition-bound scope): *"Bound to the deliberate-trunk-perturbation walking condition. Does not generalize to natural walking..."* ✓
- L197 (Candidate 2 condition-bound scope): *"Bound to the deliberate-trunk-perturbation walking condition. Does not generalize to fatigue-induced or pain-driven ankle contraction..."* ✓

All 5 sentences are condition-bound. **Condition-bound framing ✓**.

§"Falsification re-evaluation on R-side (AC5)" enumerates all 6 conditions from `docs/concepts/support-path.md` §Falsification by name with R-side evaluability + outcome:
1. No repeatable patterns across gait cycles → NOT triggered (R-side) ✓
2. Features uncorrelated with movement context → NOT triggered (R-side) ✓
3. Left-right asymmetry without systematic organization → **Not testable** (data shape; named reason: 1 L-side cycle in archive; named owner: cph#28) ✓
4. Poor agreement between OpenCap and reference measurements → NOT triggered (carried over from cph#22/26) ✓
5. Feature extraction consistently fails on clean data → NOT triggered ✓
6. No distinguishable coordination signatures → NOT triggered (R-side) ✓

The non-evaluable condition (3) has a named reason. Conditions match `docs/concepts/support-path.md` §Falsification verbatim. **All 6 falsification conditions enumerated by name with R-side evaluability + outcome ✓**.

§"Next gates" names `cph#28 — L-cycle recovery` (L-cycle recovery) and `Full R4 — falsification table at adequate n with bilateral coverage` (full R4) as the next gates. **L-cycle recovery + full R4 named ✓**.

Measured-signal vs inferred-interpretation discipline: explicit "Mechanistic interpretation (measured signal)" / "Mechanistic interpretation (inferred construct reading)" subsections in §H1 and §H2 (lines 139–143, 163–167). **AC5 PASS.**

### AC6 — Decision per protocol

**β independent oracle.**

§"Decision per protocol (AC6)" lays out 5 criteria from `protocols/existing-data-zeroth-pilot.md` §"Go/No-Go Criteria" — re-verified verbatim against the protocol file:
1. Successfully segment ≥80% of walking trials → R-side 100% ✓
2. Extract interpretable feature tables with <20% missing data → 0.00% missing ✓
3. Reasonable agreement with reference measurements → r̄ 0.93–0.96 carried from cph#22 ✓
4. Generate ≥3 candidate support-path hypotheses → 3 named ✓
5. Complete pipeline runs without major technical failures → reproducible single-script run ✓

All 5 GO criteria pass on R-side. Decision string: `R3 = partial GO on R-side` appears at line 9 (Status header), line 23 (Executive summary §Decision), line 242 (§Decision per protocol AC6), line 282 (Receipt §Decision), and is mirrored in PROJECT.md, ROADMAP.md, CHANGELOG.md. **Decision GO/REVISE/NO-GO appears explicitly ✓**.

**Cross-cycle binding (BLOCKING).** R1 status verified:
- field-report-03 L9 / L23 / L226 / L244 / L283 / L262 (Receipt): each names "R1 stays REVISE" / "R1 status: unchanged REVISE" / "R1 stays REVISE because the bilateral construct is still half-anchored".
- PROJECT.md §"Current empirical decision": `**REVISE on R1; partial GO on R-side construct (R3)**` ✓
- ROADMAP.md §"Current state": `**R1 is REVISE; R3 is partial GO on R-side**` ✓
- ROADMAP.md §"Phase R1": status line unchanged from main (no edit to that section per `git diff origin/main..HEAD -- ROADMAP.md` — only Current state, Phase R3, Phase R4 sections touched) ✓
- CHANGELOG.md 0.3.1 entry: `**R1 itself stays REVISE** — partial GO on R-side does *not* lift R1.` and `R3 = partial GO on R-side. R1 stays REVISE (cross-cycle binding; cph#28 owns the transition gate).` ✓

Cross-cycle-binding diff sweep:
```
git diff origin/main..HEAD -- PROJECT.md ROADMAP.md CHANGELOG.md | grep -E '^\+.*R1.*GO|^\-.*R1.*REVISE'
```
No `R1 → GO` or `R1 = GO` patches anywhere in the diff. Every reference to R1 in the cycle's status-surface edits names REVISE explicitly. **R1 binding honored ✓**.

**AC6 PASS.**

### AC7 — Status surfaces realigned

**β independent oracle.**

`git diff origin/main..HEAD -- PROJECT.md ROADMAP.md CHANGELOG.md`:
- **PROJECT.md** — §"Current empirical decision" updated to name partial-GO-on-R-side + REVISE-on-R1 + cph#27 R3 + field-report-03; §"Current blocker" carries forward L-cycle-yield + names cph#28 as owner; §"Next action" rewritten to point at cph#28 as R1's gate + full R4 as downstream; §"Open issues" updates cph#27 with verdict + names cph#28 as R1-transition gate owner; §"Last field report" updated from field-report-01 → field-report-03 with full 2026-05-19 reading. **§"Current empirical decision" + §"Current blocker" + §"Next action" + §"Last field report" all updated ✓**.
- **ROADMAP.md** — §"Current state" rewritten (R1 REVISE + R3 partial GO + R-side falsification reading); §"Phase R3" status moved from `NOT STARTED` to `**Partial GO on R-side.**` with rewritten current-evidence + coherence-risk additions; §"Phase R4" status moved from `NOT STARTED` to `**Partially evaluable on R-side** (5 of 6 conditions readable, 0 triggered)`; §"Phase R1" left unchanged (correct per R1 binding). **R3 status updated; R4 reflects which falsification conditions are R-side-evaluable ✓**.
- **CHANGELOG.md** — one new `## 0.3.1 — R3 R-side construct evaluation; partial GO on R-side (2026-05-19)` entry with "Where we were / What this version unblocked / What is still blocked / The new question / Changed (file-level) / Decision / Next gate" narrative-progress structure matching the 0.3.0 entry. **CHANGELOG.md has one new entry ✓**.

**AC7 PASS.**

### AC8 — No empirical drift on charter

**β independent oracle.**

```
git diff origin/main..HEAD -- README.md docs/concepts/coherence-path-hypothesis.md docs/concepts/support-path.md docs/articles/seven-ways-people-walk.md
```
Exit 0, no output. **All 4 charter surfaces untouched ✓**.

Intra-doc consistency audit (n=60 R-cycle framing):
- PROJECT.md: "60 R cycles × 10 subjects × 2 conditions" (consistent) ✓
- ROADMAP.md: "60 R cycles" (consistent) ✓
- CHANGELOG.md 0.3.1: "60 R cycles × 25 numeric features" (consistent) ✓
- field-report-03: "60 R + 1 L; 10 subjects × 2 conditions × 3 R-side cycles per (subject, condition) cell" (consistent) ✓

Stale-reference sweep for `18.3%` / `11/60` / `11 of 60` on live surfaces:
- CHANGELOG.md L41 (0.3.0 entry "Where we were"): historical context — pre-fix state described in narrative ✓ acceptable
- CHANGELOG.md L73 (0.3.0 entry, file-level changed list): "supersedes the 18.3%-segmentation REVISE" — historical context ✓ acceptable
- `reports/field-report-01-existing-data-zeroth-pilot.md`: historical context in the older field report ✓ acceptable
- `.cdr/unreleased/{12,13,26}/`: prior cycle artifacts (immutable history) ✓ acceptable
- **No live references** to 11/60 or 18.3% as current empirical state.

**AC8 PASS.**

### AC9 — No data policy regression

**β independent oracle.**

```
git diff origin/main..HEAD --name-only | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$' || echo NONE
```
Returns `NONE` ✓.

```
git ls-files | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$' || echo NONE
```
Returns `NONE` ✓ (no tracked binary regression in working tree).

Aggregate tables in field-report-03 are inlined as markdown (derived); `analysis/r3_subject_aggregate_tests.py` writes nothing to disk (verified by reading the script — `print()` to stdout only, no `to_csv` / `to_parquet` calls). The features CSV input at `/opt/gait-data/cph-features/features-zeroth-pilot.csv` is read-only and external to the repo.

**AC9 PASS.**

## β additional verification

### α identity discipline

```
git log origin/main..HEAD --format='%h %ae %s'
8a1a7fa alpha@cph.cdd.cnos α #27: self-coherence — fill implementation SHA + re-validate transient gate rows
84df451 alpha@cph.cdd.cnos α #27: self-coherence §ACs + §Self-check + §Debt + §CDD-Trace + §Pre-review gate + §Review-readiness
d043576 alpha@cph.cdd.cnos α #27: AC7 status surfaces — R3 partial GO on R-side; R1 stays REVISE
d1eaaed alpha@cph.cdd.cnos α #27: field-report-03 — R3 R-side construct evaluation
1d84603 alpha@cph.cdd.cnos α #27: add R3 subject-aggregate analysis script (read-only; no data committed)
81a00f7 alpha@cph.cdd.cnos α #27: self-coherence §Skills + §Method picks
0bec5d6 alpha@cph.cdd.cnos α #27: self-coherence §Gap
03ff147 gamma@cph.cdd.cnos  γ #27: scaffold — R3 R-side aggregate analysis cycle
```

7 α commits + 1 γ scaffold commit. **No β or other-identity commits on the cycle branch ✓**.

### Self-coherence completeness

`.cdr/unreleased/27/self-coherence.md` (194 lines) carries all required sections:
- §Gap ✓
- §Skills ✓ (Tier 1 + Tier 2 + Tier 3 named with rationale)
- §Method picks ✓ (M1 aggregation, M2 paired test, M3 effect size, M4 MC-handling, M5 AC1 interpretation — each named with rationale)
- §ACs ✓ (AC1–AC9 row-per-AC with β oracle)
- §Self-check ✓ (9 items including sibling-surface peer enumeration with grep evidence)
- §Debt ✓ (D1–D5)
- §CDD-Trace ✓ (steps 1–7)
- §Pre-review gate ✓ (rows 1–14)
- §Review-readiness ✓ (round 1, base SHA + head SHA + verdict "ready for β")

### Sibling-surface peer enumeration

Self-coherence §Self-check item 3 carries grep evidence for the three new candidate-hypothesis names ("Lateral-trunk substitution", "Distal sagittal contraction", "Cadence-slowdown signature") and for "partial GO" and "support path". β re-verified one assertion:

```
rg "Lateral-trunk substitution|Cadence-slowdown signature" /root/cph/docs /root/cph/analysis /root/cph/reports
```
(no hits outside the cycle's new files — confirmed against the prior field reports and analysis docs.) **Peer enumeration honest ✓**.

### Receipt block

field-report-03 §"Provenance / Receipt" (lines 262–288) matches the issue body's Receipt format template. β cross-checked the Receipt numbers against the report body:
- subjects: 10 ✓ (matches AC1a 20-row aggregate table)
- conditions: 2 (natural, trunk-sway) ✓
- features tested: 25 numeric (of 35 total) ✓ (matches script output + §Method picks §M5)
- aggregate rows: 700 cells ✓ (matches script output)
- method: median primary, mean reported ✓ (matches §M1)
- H1 evidence: partial (1/5 BH-sig) ✓ (matches §AC3 H1)
- H2 evidence: partial (2/9 BH-sig) ✓ (matches §AC3 H2)
- H3 evaluable: no (L=1) ✓
- Falsification: 5 of 6 evaluable on R-side; 0 triggered ✓ (matches §AC5)
- Candidate hypotheses: 3 named ✓ (matches §AC4)
- Decision: partial GO on R-side ✓
- R1 status: unchanged REVISE ✓
- R3 status: partial GO on R-side (NOT STARTED → partial GO) ✓
- No raw data committed: yes ✓
- Next recommended issue: cph#28 ✓

Receipt `Commit:` and `Merge SHA:` fields are correctly placeholdered as `filled by β at merge` — β fills them at merge time per convention. **Receipt block complete ✓**.

## Findings

**None.**

The cycle delivers a clean R3 R-side aggregate analysis with reproducible numbers, honest measured-vs-inferred discipline, explicit cross-cycle binding to cph#28 for R1, and no charter / data-policy drift. Method picks are documented with rationale and verifiable independent of α's claims. The "partial GO on R-side" framing is correctly scoped to R3 and does not lift R1.

Two non-binding observations (not findings):

1. **N1 (non-binding).** Self-coherence §Debt §D5 honestly names `pelvis_tilt_range_deg` (q=0.084, r_rb=+0.75) as held below the AC4 candidate-hypothesis line; field-report-03 §"Candidate support-path hypotheses" carries the same disclosure in the "Catalogue note". The choice not to promote it to a 4th candidate is α's call within AC4's "≥3" floor; β concurs the mechanistic story overlaps Candidate 1 and the BH-gate is not crossed. No action.

2. **N2 (non-binding).** Self-coherence §Debt §D1 inlines a 25-line `df_to_markdown()` helper in `analysis/r3_subject_aggregate_tests.py` to avoid adding `tabulate` to `requirements.txt`. β verified the helper has no behavioral coupling to the rest of the analysis (used only for stdout rendering; never feeds back into numerics). Acceptable for a single-purpose reproducibility harness. No action.

## Verdict

**APPROVE.**

Cycle is ready for merge. β will execute `git merge --no-ff cycle/r3-rside-aggregate-analysis` onto main, push main, delete the cycle branch from origin, and write `.cdr/unreleased/27/beta-closeout.md` carrying the merge SHA + ACs-verified table + files merged.
