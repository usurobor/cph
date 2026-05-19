# β Close-out — cycle/14 — Sub C — TSC targets + measure-coherence.sh + CHANGELOG baseline + PROJECT.md repartition

<!--
section-manifest:
  planned: [Review Summary, Implementation Assessment, Technical Review, Process Observations, Wave Position]
  completed: [Review Summary, Implementation Assessment, Technical Review, Process Observations, Wave Position]
-->

**Issue:** usurobor/cph#14 — Sub C of master cph#11
**Master:** usurobor/cph#11 (CDR refactor)
**Wave:** `.cdd/waves/cdr-refactor-2026-05-18/`
**Mode:** MCA-eligible (TSC target-manifest format + `measure-coherence.sh` shape pinned in master cph#11 §"Required changes" items 6–7; PROJECT.md repartition mechanical given AC-PROJECT invariant)
**Branch (still live; δ owns disconnect):** `cycle/14`
**Merge commit:** `f6ad183` on `main`
**Base SHA (origin/main at review):** `f13164d`
**Review SHA at APPROVE:** `b4a5569` (cycle/14 head before β verdict commit)
**Verdict SHA:** `29bc71e` (β round-1 verdict commit on cycle/14)
**Disconnect type:** part-of-wave; no tag, no version bump, no `.cdd/unreleased/14/` move yet — wave terminal state under δ at Sub D close.

## Review Summary

One round, one verdict, zero findings.

α's self-coherence carried §CDD-Trace through step 7 with grep-level evidence reproduced for every claimed AC. The four ACs (AC5 / AC6 / AC7 / AC-PROJECT) mapped to clean positive + negative oracles. β re-verified every claim independently:

- AC5 — five `targets/*.tsc` files parse via `tomllib.load`; `registry.tsc` carries `format = "tsc-target-registry/0.1"`, `default_target = "repo"`, four `[target.*]` manifest paths all resolve; the per-target `sources` arrays resolve to ≥1 match per glob (33 entries across the four per-target manifests, 100% resolution); `.tsc/**` does not appear in any `sources` array — only in comment-block exclusions in `registry.tsc` and `repo.tsc`.
- AC6 — `scripts/measure-coherence.sh` is executable, `bash -n` clean, mechanical-mode-only (no LLM credential references), and the missing-`coh` branch in the dispatch env exits 127 with an install-instruction block to stderr (verified by direct run on both the cycle branch and the merge tree).
- AC7 — `CHANGELOG.md` carries the full ledger header (Entry / Date / Empirical state / α / β / γ / C_Σ / Bottleneck / Decision), the `0.1.0-cdr` baseline row with `pending — coh unavailable`, the §Coherence delta with α/β/γ/C_Σ bullets, §Known limits opening with the verbatim `Coherence score is not empirical validation`, and §Next gate naming R0 closure conditions.
- AC-PROJECT — `PROJECT.md` repartitioned to exactly seven `## ` headings matching the AC invariant; no R0–R6 phase blocks (no roadmap content duplication); no ledger table (no CHANGELOG content duplication); points to `ROADMAP.md` and `CHANGELOG.md` for delegated concerns.

β reviewed under `cdd/review/SKILL.md` Phases 1–3 with sub-skills for contract integrity (§2.0.0), issue contract (§2.0), diff/context (§2.1), architecture (§2.2), and honest-claim verification (§2.2a). Rule 3.13 honest-claim checks ran clean across reproducibility (a), source-of-truth alignment (b), wiring (c), and gap claims (d). Rule 3.10 (CI green) is vacuous in cph today — no `.github/workflows/` directory; the wave-manifest standing permissions contemplate this. Rule 3.11b (γ artifact completeness) was handled substantively in `beta-review.md §2.5`: the wave manifest at `.cdd/waves/cdr-refactor-2026-05-18/manifest.md` carries the substantive γ coordination that rule 3.11b protects against losing, the sub-issue body explicitly invokes the `operator/SKILL.md` §5.2 "γ = δ permitted" relaxation, and sibling cycles cph#12 / cph#13 in the same wave merged cleanly under the same pattern.

Pre-merge gate (β/SKILL.md §Pre-merge gate):

| Row | Item | Result |
|---|---|---|
| 1 | Identity truth — `beta@cph.cdd.cnos` | passed (verified pre-merge; also re-verified post-merge — merge commit `f6ad183` is authored by `Beta <beta@cph.cdd.cnos>`) |
| 2 | Canonical-skill freshness — `origin/main` matches session-start `f13164d` | passed (re-fetched synchronously at pre-merge; no advance since β intake) |
| 3 | Non-destructive merge-test in throwaway worktree | passed (auto-merge clean, zero unmerged paths, all five `.tsc` files re-parse on merge tree, `bash -n` re-passes on merge tree, worktree torn down; β identity unaffected on the shared repo config — confirmed post-cleanup `git config --get user.email` returns `beta@cph.cdd.cnos`) |
| 4 | γ artifact completeness | passed — wave-manifest serves as γ artifact of record per cph-canonical model; details in `beta-review.md §2.5` |

## Implementation Assessment

α's eight-file diff lands a complete TSC measurement surface (registry + four per-target manifests + entrypoint) and the supporting documentation surfaces (CHANGELOG ledger + PROJECT.md repartition) without back-edits to Sub A or Sub B. The forward-reference contract pinned in the wave manifest was honored verbatim: `targets/hypothesis.tsc` references the eight paths in the order the manifest pins; the seven-gait-families path resolves to `docs/articles/seven-ways-people-walk.md` (the manifest's preferred form) without an α-side override.

The script is small and disciplined: `set -euo pipefail` at the top, missing-tool guard before any side effect, missing-registry guard before `mkdir -p`, explicit exit codes (127 / 2) that surface the right signal to CI and humans. The mechanical-mode-only invariant is structural (no `--mode hybrid` branch, no credential references) rather than narrative.

The CHANGELOG-vs-PROJECT separation is sharp: CHANGELOG owns the historical ledger row + the 0.1.0-cdr entry detail; PROJECT.md owns the live operational snapshot and points to CHANGELOG for history. Cross-references are bidirectional and resolve. The pre-diff PROJECT.md content (Implementation Status, Realization Sequence, Implementation Timeline, Friend Pre-Pilot Overview, Risk Management, Source-of-truth table, Success Criteria, Decision Points) was cleanly removed rather than gradually deprecated — the new file reads as a 44-line live snapshot, not a residual edit.

The empirical posture is preserved verbatim: REVISE per `reports/field-report-01-existing-data-zeroth-pilot.md`, with the literal phrase `not validated; it is also not refuted` reused consistently across CHANGELOG.md and PROJECT.md. No new empirical claim is introduced; no clustering, no participant recruitment, no rewrite of the field report. β's honest-claim sweep returned no overclaim matches (matches for `validated` are negations or are about structural validation of the manifests in α's self-coherence artifact, which is process metadata not a public claim).

## Technical Review

Findings: zero (D / C / B / A all empty).

Strengths β surfaced during review:

1. **Schema consistency across the five `.tsc` files.** All four per-target manifests carry the same `{format, name, description, sources}` shape with the same `tsc-target/0.1` format string. The registry distinct-format string (`tsc-target-registry/0.1`) per the master-issue example is honored. A future reviewer can read one manifest and the others are predictable.
2. **`registry.tsc` ↔ script ↔ wave-manifest triple-alignment.** The four `[target.*]` blocks in `registry.tsc` exactly match the four entries in the script's `TARGETS=()` array, which exactly match the four targets named in master cph#11 §"Required changes" item 6. β cross-verified the chain end-to-end.
3. **`.tsc/**` exclusion handled at three layers — `.gitignore` (out of the index), per-target `sources` exclusion (out of canonical measurement), and explicit comment-block declarations in `registry.tsc` and `repo.tsc` (out of human ambiguity).** The triple-redundancy makes future drift on the generated-vs-canonical distinction unlikely.
4. **α's incremental self-coherence commit discipline.** §Gap / §Skills / §ACs / §Self-check / §Debt / §CDD-Trace / §Review-readiness each landed as separate commits with sub-section labels. Easy to audit; matches `cdd/alpha/SKILL.md` §2.5. The one mid-process self-correction (`1dde070`, count `6 → 4`) was filed transparently before review-readiness was signaled.

Known debt α declared in §Debt, β concurs:

1. No numeric C_Σ baseline this wave (`coh` not installed in dispatch env). First numeric baseline lands the first time `coh` runs against this branch or a successor; the entrypoint and target manifests are in place.
2. `coh --target / --registry / --output` flag spelling is inferred from master cph#11 §"Required changes" item 7 example, not verified against a live CLI. The missing-`coh` branch is verified end-to-end; the present-`coh` branch is only structurally validated.
3. The `tsc-target/0.1` per-target manifest format string is α's choice (master cph#11 only pins the registry format `tsc-target-registry/0.1`). If the live `coh` CLI expects a different per-target schema, the per-target manifests need a one-pass schema update; the file paths inside the manifests are independent of the schema, so AC-content survives.
4. `shellcheck` not run (not installed in dispatch env). `bash -n` is clean; the script is small (≈40 executable lines) and uses standard constructs.

None of these are blocking; all are appropriately surfaced in CHANGELOG §Known limits and `self-coherence.md §Debt`.

## Process Observations

(γ-axis, for the PRA.)

- **β intake → APPROVED in one round, zero findings.** α's self-coherence quality (grep-level evidence per AC, full §CDD-Trace, declared §Debt) front-loaded the verification work. β's role reduced to independent re-verification of α's claims plus the architecture sweep and the merge gate. This matches the MCA profile the wave manifest declared for Sub C.
- **The wave-manifest forward-reference contract worked.** Sub C shipped concurrently with Sub A / Sub B (per the wave manifest's parallelizable claim) without rebasing on either, because the pinned paths in the manifest were treated as authoritative by all three subs. β verified the chain at review time: `targets/hypothesis.tsc` references `docs/articles/seven-ways-people-walk.md` (Sub A's chosen path) and the file exists on `origin/main` post-Sub-A-merge. Zero coordination cost.
- **γ-artifact-of-record is the wave manifest.** Worth recording for γ's wave-level PRA: cph's repo-canonical γ model is wave-manifest-based (one `manifest.md` per dispatch wave), not per-cycle `gamma-scaffold.md`. This was already the pattern in sibling cycles 12 and 13 (this wave) and older cycles 5–8 (pre-wave). Rule 3.11b's exemption discoverability is satisfied by the sub-issue body's `γ = δ permitted` line invoking `operator/SKILL.md` §5.2. β's `beta-review.md §2.5` documents this read so a future reviewer of cph cycles does not need to re-derive it.
- **`pending — coh unavailable` cadence is honest.** The CLI is not installed in the dispatch environment, the script's missing-tool branch is the one that gets exercised, and the CHANGELOG row carries `pending — coh unavailable` literally rather than a fabricated baseline. The first numeric baseline lands when `coh` is available — likely after the Sub D conformance sweep or via a subsequent operator-tooling decision.

No process patches recommended this cycle. No `cdd/CDD.md` / role-skill changes warranted.

## Wave Position

This sub is **Sub C** of the four-sub `cdr-refactor-2026-05-18` wave.

- Sub A (cph#12) — **merged** (per the wave-manifest tracking).
- Sub B (cph#13) — **merged**.
- Sub C (cph#14) — **merged** (this close-out).
- Sub D (cph#15) — **pending**. Per the wave manifest: "Sub D runs only after A+B+C close (or after the wave closes any of them as deferred — D's scope adjusts to the merged set)." All three of A/B/C are now in terminal merged state, so the wave is ready to dispatch Sub D as the conformance sweep (AC8 / AC9 / AC10 across A+B+C).

Master cph#11 stays open until Sub D closes (per the wave dispatcher comment on cph#11). δ owns the disconnect release: tag (if any), branch deletion of `cycle/14`, and the move of `.cdd/unreleased/14/` to its release-final location.

Empirical state remains REVISE per `reports/field-report-01-existing-data-zeroth-pilot.md`. The active R2 segmentation blocker (`scripts/segmentation.py::detect_heel_strikes`) is unchanged; the orthogonal `origin/cycle/segmentation-real-data-fix` branch is unmerged and unaffected by this wave.

---

**Closing:** β work on cph#14 is done. δ owns the release boundary (tag / disconnect / cycle branch cleanup); γ owns the PRA at wave-terminal-state. Hand-off is via the merged artifacts on `main` and this close-out file.
