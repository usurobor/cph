---
name: cph-27-beta-closeout
description: β close-out for cph#27 (R3 R-side aggregate condition-response analysis); merge evidence + ACs verified + cycle-level observations
metadata:
  type: cycle-artifact
  cycle: 27
  role: beta
sections:
  planned: [MergeEvidence, ACsVerified, Findings, FilesMerged, CycleObservations]
  completed: [MergeEvidence, ACsVerified, Findings, FilesMerged, CycleObservations]
---

# β close-out — cph#27

## §Merge evidence

| Field | Value |
|---|---|
| Cycle branch | `cycle/r3-rside-aggregate-analysis` |
| Cycle head SHA (pre-merge) | `7a24418` (β review verdict commit) |
| Cycle implementation tip | `8a1a7fa` (α's last commit before β review) |
| Base SHA (`origin/main` at merge) | `1d87d4a3db170bbb6c77e8633bc37a550187fc43` |
| Merge commit SHA | `dcf688bd1d628782b5e7abd013d20d86ee0331bb` |
| Merge strategy | `--no-ff` (preserves α + γ + β commit history; no squash) |
| Merge commit message | `Merge cycle/r3-rside-aggregate-analysis — cph#27 R3 R-side analysis` (includes `Closes #27` for auto-close) |
| Issue auto-close | yes (`Closes #27` in merge commit message) |
| β review round count | 1 (APPROVE on first pass) |

## §ACs verified

| AC | Status | β oracle |
|---|---|---|
| AC1 — Per-subject-condition aggregates (700 cells) | PASS | Re-ran `python3 analysis/r3_subject_aggregate_tests.py`; script confirms `(20, 25)` aggregate shape and `700 cells (20 rows × 35 columns)`. Aggregation method (median primary + mean robustness) documented in self-coherence.md §Method picks §M1. |
| AC2 — Paired Wilcoxon + r_rb + 95% CI + BH-FDR | PASS | 25-row test table reproduces verbatim from script (W, r_rb, percentile-bootstrap CI, p_raw, p_BH). Method picks named with rationale in §M2 / §M3 / §M4. Spot-checked 3 features against AC1c per-subject deltas — direction and rank-biserial consistent. |
| AC3 — H1/H2/H3 evidence summary | PASS | H1: 5 features tested (≥3 ✓); H2: 9 features tested (≥3 ✓); H3: explicit non-testable note with L=1 reason (subject8 walkingTS1; no R/L pairs; cph#28 owns the gate). |
| AC4 — ≥3 candidate support-path hypotheses | PASS | 3 candidates (Lateral-trunk substitution path; Distal sagittal contraction under proximal compensation; Cadence-slowdown signature); each carries 5 named fields (features / expected dir / observed dir / mechanism / condition-bound scope). |
| AC5 — `reports/field-report-03-construct-evaluation.md` written | PASS | File present at `reports/field-report-03-construct-evaluation.md` (308 lines); 6 falsification conditions enumerated verbatim against `docs/concepts/support-path.md` §Falsification with R-side outcome; condition-bound language confirmed at 5 spot-checked sentences; L-cycle recovery + full R4 named in §Next gates. |
| AC6 — Decision per protocol (R3 partial GO; R1 stays REVISE) | PASS | All 5 GO criteria from `protocols/existing-data-zeroth-pilot.md` §"Go/No-Go Criteria" pass on R-side surface; decision `partial GO on R-side` appears in field-report-03 §Status / §Executive summary / §Decision / §Receipt and is mirrored in PROJECT.md / ROADMAP.md / CHANGELOG.md. Cross-cycle binding honored — no `R1 → GO` patch anywhere in the diff. |
| AC7 — Status surfaces realigned | PASS | PROJECT.md §"Current empirical decision" / §"Current blocker" / §"Next action" / §"Open issues" / §"Last field report" updated; ROADMAP.md §"Current state" / §"Phase R3" / §"Phase R4" updated (§"Phase R1" unchanged per binding); CHANGELOG.md 0.3.1 entry added with narrative-progress structure matching 0.3.0. |
| AC8 — No empirical drift on charter | PASS | `git diff origin/main..HEAD -- README.md docs/concepts/coherence-path-hypothesis.md docs/concepts/support-path.md docs/articles/seven-ways-people-walk.md` empty. Intra-doc consistency: n=60 R-cycle framing consistent across PROJECT.md / ROADMAP.md / CHANGELOG.md / field-report-03. Stale `18.3%` / `11/60` references appear only in historical-context locations (prior CHANGELOG entries, field-report-01, prior cycle artifacts). |
| AC9 — No data policy regression | PASS | `git diff origin/main..HEAD --name-only` returns no `.zip/.trc/.mot/.sto/.c3d/.osim/.mp4/.mov/.csv/.parquet` files; `git ls-files` likewise clean. Aggregate tables inlined as markdown; analysis script writes nothing to disk. |

## §Findings

**None blocking.**

Two non-binding observations carried forward (recorded in beta-review.md §Findings as N1, N2):

- **N1 (non-binding) — `pelvis_tilt_range_deg` held below AC4 line.** Self-coherence §Debt §D5 honestly names the BH-q=0.084 trending feature as deliberately held below the candidate-hypothesis line; field-report-03 §AC4 "Catalogue note" carries the same disclosure. β concurred that the mechanism overlaps Candidate 1 and the BH-gate is not crossed; AC4's ≥3 floor is met without it. No action.

- **N2 (non-binding) — inline `df_to_markdown()` helper avoids `tabulate` dependency.** Self-coherence §Debt §D1 documents the choice; β verified no behavioral coupling (stdout rendering only). Acceptable for a single-purpose reproducibility harness. No action.

## §Files merged from cycle

| File | Provenance | Bytes added (net) |
|---|---|---|
| `.cdr/unreleased/27/gamma-scaffold.md` | γ scaffold commit `03ff147` (`gamma@cph.cdd.cnos`) | +195 lines |
| `.cdr/unreleased/27/self-coherence.md` | α implementation commits `0bec5d6` / `81a00f7` / `84df451` / `8a1a7fa` (`alpha@cph.cdd.cnos`) | +194 lines |
| `.cdr/unreleased/27/beta-review.md` | β review commit `7a24418` (`beta@cph.cdd.cnos`) | +279 lines |
| `analysis/r3_subject_aggregate_tests.py` | α implementation commit `1d84603` | +394 lines |
| `reports/field-report-03-construct-evaluation.md` | α implementation commit `d1eaaed` | +308 lines |
| `PROJECT.md` | α status-surface commit `d043576` | net +14 lines |
| `ROADMAP.md` | α status-surface commit `d043576` | net +22 lines |
| `CHANGELOG.md` | α status-surface commit `d043576` | +34 lines |

Total: 8 files changed, 1422 insertions(+), 18 deletions(-) — verified against the merge commit `dcf688b` diff.

## §Cycle-level observations

Factual observations only; γ disposes via PRA.

1. **Reproducibility-property test surface worked cleanly.** α's analysis script is deterministic (seed=20260519) and emits all field-report tables to stdout in one command. β re-ran the script against the input CSV and matched every cell of the AC1 / AC1c / AC2 / AC3 tables to the field report verbatim. This is the right shape for an analysis cycle where no traditional test surface exists.

2. **Method-pick verification was independent of α's claims.** Self-coherence.md §Method picks named aggregation / paired-test / effect-size / MC-handling each with one-line rationale + alternative-rejected. β did not have to infer choices or guess at why a method was preferred. The pre-cycle binding "β verifies recorded + reproducible, not 'correct'" was applied without ambiguity.

3. **Cross-cycle binding (R1 ↔ cph#28) survived intact across four surfaces.** PROJECT.md / ROADMAP.md / CHANGELOG.md / field-report-03 all explicitly named R1 as REVISE and cph#28 as the gate owner. ROADMAP §"Phase R1" was left untouched — the binding was enforced by surface omission rather than by overwriting. This is the right shape: R3 cannot lift R1, so R3's diff should not edit R1's status row.

4. **Single review round.** No fix-round was needed. α's self-coherence §Pre-review gate (14 rows, 9 PASS + 4 N/A with named reason + 1 PASS marked transient with explicit re-validation step) reflects careful pre-flight; the AC oracles in the artifact matched β's independent oracle on first read.

5. **γ scaffold completeness.** γ's scaffold carried per-AC oracle hints that aligned with β's independent oracles; the cross-cycle coordination section made the R1 binding load-bearing on β's side as well as α's. This reduced β's review-time disambiguation work materially.

End of β close-out for cph#27.
