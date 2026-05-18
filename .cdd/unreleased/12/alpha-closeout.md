# α Close-out — cycle/12 — Sub A — CDR charter docs

**Issue:** usurobor/cph#12
**Master:** usurobor/cph#11
**Wave:** `.cdd/waves/cdr-refactor-2026-05-18/`
**Mode:** design-and-build (docs-only)
**Branch (deleted post-merge):** `cycle/12`
**Merge commit:** `c3c274a` on `main`
**Base SHA at α intake:** `06341a4`
**Implementation SHA at review-ready:** `f20949e`
**Review SHA at APPROVE:** `9b291d3`
**β verdict:** APPROVED round 1, 0 findings
**β close-out commit:** `c08dddc`

## Cycle summary

Goal: render the pre-specified charter shape (master #11 §"Required changes" items 1, 2, 5 + AC10 table) into prose across four files — README rewrite, `CDR.md`, `docs/concepts/coherence-path-hypothesis.md`, `docs/articles/seven-ways-people-walk.md` — plus the AC10-initial source-of-truth table embedded in README. Result: 4 ACs met (1, 2, 4, 10-initial), 1 round, APPROVE, 0 findings. Five files changed (1 modified, 4 added) plus the self-coherence artifact; 569 insertions / 60 deletions; Markdown only.

α implementation ran in four narrative commits (`753092d` → `036bcd0` → `5193877` → `32defc5`) before the self-coherence chain. Self-coherence wrote in 7 incremental commits (`f39715d` → `873692f`) per α §2.5 — no resumption needed, no stream timeouts.

## Friction log

- ~2 min on the choice between `docs/articles/seven-ways-people-walk.md` (wave manifest preferred) and `docs/references/seven-gait-families.md` (AC2-permitted alternative). Picked the preferred path; no manifest update or Sub C coordination note required.
- ~1 min on table placement for AC10 — embed in README between Q7/Q8 vs spin out to a separate file linked from README. The AC10 surface text ("`README.md` (and any doc it forwards the table to)") explicitly permitted either; embedded chosen to keep one-click reading.
- Zero friction on the §C_Σ ≠ truth distinction in CDR.md — naming the two failure modes (coherence laundering / coherence dismissal) followed directly from the AC4 negative oracle.
- No mid-cycle patches, no β fix-rounds. The α-side pre-review gate (`self-coherence.md` §Review-readiness) ran clean on first pass.

## Pre-review gate observations

α §2.6 row outcomes worth surfacing:

- **Row 10 (CI green) — vacuous.** cph carries no `.github/workflows/`. α §2.6 row 10's "local CI unavailable" path applies. α recorded the explicit absence in `self-coherence.md` §Review-readiness; β re-verified independently in `beta-review.md` §3.10. This is the third consecutive cph cycle (8, 9, 10, 12) where the CI-green row resolves as structural absence rather than a green CI run.
- **Row 1 (rebased on current main) — held trivially under wave-mode parallel work.** Base SHA at intake (`06341a4`) equals base SHA at review-ready observation time (`06341a4`); `origin/main` did not advance during α's authoring because Subs B and C ran on `cycle/13` and `cycle/14` in parallel, not on `main`. The transient-row drift class α §2.6 names (rows 1, 10) was structurally suppressed by the wave-mode parallel-cycle pattern.
- **Row 14 (commit author email) — clean.** All 10 α commits on `cycle/12` carry `alpha@cph.cdd.cnos`; the path-(a) retroactive-reauthor surface α §2.6 row 14 documents was not exercised this cycle.

## Skill / spec gaps that survived the gate

One observable gap survived α's pre-review gate and reached β:

- **α §2.6 has no row for γ-artifact presence.** Rule 3.11b (β-side, `review/SKILL.md`) gates on `.cdd/unreleased/{N}/gamma-scaffold.md` literal presence. α's §2.6 checklist does not enumerate γ-side artifacts at all — `self-coherence.md` §Review-readiness does not record whether the γ scaffold exists at the rule-3.11b literal path. β surfaced the absence-vs-substance question as a non-binding observation (`beta-review.md` §3.11b) rather than a finding. Class: α gate does not look at the surface a β rule will examine, so the gate cannot pre-empt the read β will perform.

## Peer-enumeration / harness-audit observations

Peer enumeration applied (α §2.3):

- **Empirical-state surfaces (4 touchpoints).** README §Current empirical state, `coherence-path-hypothesis.md` §Current empirical status, `seven-ways-people-walk.md` §What the list is not — all carry REVISE + the four facts from `reports/field-report-01-existing-data-zeroth-pilot.md`. CDR.md *correctly* abstains (doctrine, not status). The "doctrine file abstains from carrying a verdict" outcome is a peer-set negative example — the enumeration class is "files that touch empirical state" and CDR.md is in the named-then-exempted category, not the missed-update category.
- **Seven-family naming (3 expected files).** Names appear in `docs/articles/seven-ways-people-walk.md` (authoritative), `coherence-path-hypothesis.md` (name-only), README (single-sentence inline). CDR.md again correctly absent. `grep -F "Pendular Carrier"` across the four authored files returns the three expected sites.
- **Intra-doc repetition (α §2.3 sub-rule).** REVISE / r̄ 0.93–0.96 / 18.3% / R-only language appears in 2 files (README, hypothesis doc) plus a deferred-form mention in the seven-families article. The grep `REVISE\|r̄\|18.3%\|2026-05-17` was run during α's polyglot re-audit (§Review-readiness); zero stale occurrences detected.

Harness audit (α §2.4) — N/A. No parsers, schema-bearing types, manifest shapes, or runtime contracts changed. The closest surface is the source-of-truth table in README, which is a documentary shape rather than a parsed contract.

## Cross-cycle pattern observations (cph cycles 5–10 vs cycle 12)

Patterns relative to prior cph cycles:

- **First wave-mode dispatch in cph.** Cycles 5–10 were per-cycle single-issue dispatches under master coordination but without a wave layer. Cycle 12 is the first cycle filed under a `.cdd/waves/{slug}/manifest.md` artifact and the first multi-sub wave. The γ-scaffold-path divergence β surfaced in §3.11b is a direct consequence — the rule and the dispatch shape were calibrated for the prior per-cycle pattern.
- **APPROVE-round-1 streak holds.** Cycles 5, 6, 7, 8, 9, 10, 12 all closed as 1-round APPROVE per the available close-outs. No `cycle/N` carries a fix-round commit chain across this range. Pattern: α-side pre-review-gate discipline is keeping fix-rounds out of the cph cadence.
- **Wave-N → wave-(N+1) protocol-patch loop continues.** Cycles 7, 8, 9 close-outs each named a doctrine-level pattern that became a later cycle's scoped patch (zeroth-pilot Pattern 1 → cycle #8 protocol subsection; α #7 "not testable" framing → α #9 preamble lift). Cycle 12 surfaces a new candidate for this loop: rule 3.11b vs wave-mode γ artifact path. β's `beta-review.md` §3.11b names the patch space; the patch itself is downstream γ-skill work, not Sub A scope.
- **CI-absence streak (cycles 8, 9, 10, 12).** Four consecutive cycles where `.github/workflows/` does not exist and rule 3.10 resolves as vacuous. Class: cph is structurally a docs-and-research repo where the CI rule's design assumption (a code repo with CI) does not apply.
- **Docs-only-cycle dominance.** Cycles 7 (docs), 8 (docs), 9 (docs), 12 (docs) vs cycle 10 (code + docs). Of the five most recent close-outs, four are docs-only. The α-side artifact set (no tests, no harness audit, narrative-only authoring constraints) is the same across all four.

## Wave position

Sub A is the first of four subs to close in `cdr-refactor-2026-05-18`. Subs B (#13) and C (#14) in flight; Sub D (#15) blocked on A+B+C terminal state. `.cdd/unreleased/12/` remains in place until δ's wave-level disconnect per β's close-out and `release/SKILL.md` §2.5b — α does not move directories on individual sub merges within a wave, and this close-out lands on `main` directly per the dispatch's standing permissions.

α's work on Sub A ends here.
