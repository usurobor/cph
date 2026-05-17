# β Close-out: Concept patch — falsification table empirical-data preamble

**Cycle:** #9
**Review rounds:** 1
**Verdict:** APPROVE
**Merge:** bfe531c

## Review context

Single-round APPROVE. α's docs-only patch landed all four ACs (AC3 as a justified no-op) and the self-coherence's AC4 grep oracle reproduced verbatim on β's side. No fix-rounds; no scope leaks; no doctrine-level gaps surfaced. β independently read the field report's §Support-Path Inference and §Falsification Assessment to vet α's AC3 no-op judgement; the call was correct.

## Merge evidence

Merge commit: `bfe531cab4d067c0048d450fb5a0113956353c92`
Merge message: `Closes #9: Concept patch — falsification table needs empirical-data preamble`
Branch state: cycle/9 merged into main with `--no-ff` and pushed (`main` head `bfe531c`, `origin/cycle/9` at `3b9c2f8`). Auto-close on `Closes #9` fired at push receipt — issue state is `closed/completed` per GitHub at 2026-05-17T13:27:49Z. γ to confirm at wave close.

## Summary of what merged

- `docs/concepts/support-path.md` — new `### Empirical-data prerequisite` subsection (lines 96–105, 11-line insertion) nested immediately under `## Falsification Conditions for Existing-Data Zeroth Pilot` (line 92) and before condition 1 (line 107). Covers three required claims: (1) line 98 names conditions 1, 2, 3, 4, 6 as testing for absence of empirical variation with a per-condition gloss; (2) lines 100–103 define "Not triggered" vs "Not testable" as a bulleted contrast; (3) lines 102–103 carry the verbatim "*positive empirical claim*" / "*deferred verdict*" phrasing. Line 105 adds a Condition-5 carve-out (pipeline competence on clean data) — not strictly required by AC1, but the only way the preamble doesn't accidentally invalidate the field report's existing "NOT triggered" verdict for condition 5.
- `docs/concepts/support-path.md` line 125 — threshold rule reworked with three changes: "are **triggered**" replaces "occur"; explicit exclusion of "Not testable" verdicts from the count; one-line rationale ("a deferred verdict carries no empirical evidence either for or against the construct, so it cannot be used to license a revision decision").
- Six condition body paragraphs (lines 108, 111, 114, 117, 120, 123) byte-identical to pre-patch text (AC4 grep oracle confirms all six headings present and numbered). Construct definition (lines 1–91) untouched. `protocols/existing-data-zeroth-pilot.md` (cycle 8's surface) untouched. `requirements.txt` untouched. `reports/field-report-01-existing-data-zeroth-pilot.md` deliberately untouched per AC3 no-op.
- `.cdd/unreleased/9/self-coherence.md` and `.cdd/unreleased/9/beta-review.md` — process artifacts.

## β-side observations / patterns worth carrying

- **Pattern: wave-N close-out patterns continue to land as wave-(N+1) docs patches.** Cycle #8 closed the zeroth-pilot wave's `cdd-protocol-gap` (Pattern 1); this cycle closed the same wave's `cdd-skill-gap` candidate (Pattern 2). Two-for-two same-shape cycles. The wave-N → wave-(N+1) loop is doing real work; the pattern is stable enough that wave manifests can begin to pre-allocate "patch cycles" from close-out pattern lists by default.
- **Pattern: AC-as-conditional with justified no-op is the right shape for "alignment IF needed" ACs.** AC3 was phrased "if it would mechanically miscount" — a conditional gating clause. α did not punt the conditional ("β, your call"); instead α discharged it inline with three concrete line-range citations from the unchanged field report (`reports/field-report-01-existing-data-zeroth-pilot.md` lines 157–162, 164–166, 166) plus a directory-shape observation (no separate template). β verified all three citations independently. This is the correct way to handle conditional ACs: the conditional is the author's to evaluate, with evidence, not the reviewer's to guess at. Worth lifting as a doctrine convention.
- **Pattern: load-bearing un-requested addition justified inline.** AC1 named three required claims for the preamble; α added a fourth (Condition-5 carve-out, line 105) that was not in the AC text. The addition is load-bearing — without it, a reader could mechanically mark all six "not testable" on smoke and drop the only honest signal the smoke run produces, which would silently contradict the field report's correct "NOT triggered" verdict for condition 5. α called this out in self-coherence §Review-readiness as a β decision point rather than slipping it in. β endorsed the carve-out. The pattern — name un-requested additions explicitly and justify their load-bearing role — is the right shape for additions that extend beyond strict AC text without violating scope.
- **No `cdd-*-gap` findings.** Empty list is the correct result here. The only `cdd-*-gap` referenced in cycle-9 artifacts is the *retrospective* lift candidate noted in self-coherence §Debt item 3 (upstream cnos.cdd skill-gap lift), which is explicitly out-of-scope per #9's Non-goals and is an operator decision, not a finding from this review.
- **Anchor-stability debt is a real future risk worth tracking.** The new preamble references conditions by number (1, 2, 3, 4, 6) and calls out condition 5 by number. If a future cycle ever renumbers or reorders conditions (a #9 Non-goal, but a real risk if new conditions are added), the preamble's references would silently drift without CI catching it. α flagged this as Debt item 4. Not blocking; worth γ-tracking for wave close so the next wave's manifest can decide whether to add a markdown structural check.

## Process notes

- β identity (`beta@gait-support-paths.cdd.cnos`) used for the review commit (`3b9c2f8`), the merge commit (`bfe531c`), and this close-out. No `--no-verify`, `--amend`, or `git config` operations. All commits signed with `-c user.name`/`-c user.email`.
- α-side scope discipline was strong — every issue Non-goal is named in self-coherence §Self-check with a matching "not touched" assertion (`requirements.txt`, `protocols/existing-data-zeroth-pilot.md`, six condition bodies, construct definition, GO/NO-GO thresholds, upstream cnos.cdd lift). Zero scope leaks observed in the diff.
- Time budget: well under the 600s β cap.
