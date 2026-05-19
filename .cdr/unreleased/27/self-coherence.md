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
  completed: [Gap]
---

# α self-coherence — cph#27

## §Gap

**Issue:** cph#27 — "R3 — R-side aggregate condition-response analysis (n=60 R cycles)" (`P1`, `surface:data`, `surface:analysis`).

**Incoherence the cycle closes.** After cph#26 (segmentation port → 60/60 R-side trials at 100%; 30 natural + 30 trunk-sway), the project has the *per-cycle* feature table the construct survival hypotheses need, but no inferential statement about whether the features actually respond to condition under the protocol's stated comparison (natural vs trunk-sway), at the inferential unit the protocol requires (*subject*, not cycle, to avoid pseudoreplication). PROJECT.md §"Next action" names R3 explicitly; ROADMAP.md §"Phase R3" status is NOT STARTED with the gate "Subject-level (not cycle-level) condition-response analysis demonstrates stable feature distributions per subject per condition." R3 is the first cycle in the project to produce *construct-level* evidence as distinct from *pipeline-level* evidence (R1 cleared technology stack; R2 cleared detector).

**Scope.** Build per-(subject, condition) aggregates from the existing 60 R-side feature rows; run paired condition-response tests at n=10 subjects; report effect size + 95% CI + p-value with explicit multiple-comparisons handling; write `reports/field-report-03-construct-evaluation.md` evaluating the 6 falsification conditions from `docs/concepts/support-path.md` §Falsification on R-side data; issue a GO/REVISE/NO-GO decision per `protocols/existing-data-zeroth-pilot.md` thresholds, where R1 stays REVISE by cross-cycle binding (only cph#28 can lift it).

**Mode.** explore / analysis — method picks (aggregation, paired-test choice, multiple-comparisons handling) are α's call within AC scope and are documented in §Method picks below; β verifies the choice is recorded and the resulting numbers are reproducible, not which method is "correct" (γ-scaffold §Mode rationale; `issue/SKILL.md` MCA preconditions, all three failed).

**Cross-cycle binding.** cph#27 runs concurrently with cph#28 (L-cycle recovery, branch `cycle/l-cycle-recovery`). The cph#27 issue body §Non-goals binds R1 to remain REVISE regardless of R3 outcome — only cph#28 can lift R1. Highest-status R3 outcome possible: REVISE or partial GO on R-side.
