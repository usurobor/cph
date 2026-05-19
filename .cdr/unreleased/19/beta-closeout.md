# β close-out — Sub C (cph#19) — F3 + F5

## Verdict

**APPROVE** (round 1, no findings).

**Wave:** `.cdd/waves/coherence-drift-sweep-2026-05-18/`
**Master:** usurobor/cph#16
**Sub:** usurobor/cph#19
**Implementation SHA:** `80698cf`
**Self-coherence SHA:** `319ab3e`
**β review SHA:** (this commit)
**Branching:** single-branch dispatch on `claude/review-repo-coherence-PNbjQ` per wave manifest §"Branching deviation".

## What changed

| File | Lines changed | Surface | AC tested |
|---|---|---|---|
| `analysis/feature-table-schema.md` | 86 lines reshaped (148+/113− net across both files) | Rewrote §Purpose (names wide-vs-long resolution); §Identification (uses `subject`/`session`/`trial_id`/`condition`/`side`/`cycle_number` matching code); §Cycle Definition (cycle_number only); §Quality Control (`quality_flag` with code-vocabulary `ok`/`short`/`low_contact_gap`; `exclusion_flag` derived); §Feature Data (enumerates wide-format columns by `extract_*` function); §Allowed Values §side (`L`/`R` matching `Cycle.side`); §Allowed Values §quality_flag (matches segmentation.py); §Data Rules and §Example Rows updated. | AC1 (F3 dir-b) |
| `analysis/features.md` | 175 lines reshaped | §Required indexing rewritten to cite code column names; new §"First-pass set (currently implemented)" with subsections by `extract_*` function listing every realized column; new §"Candidate set (not yet implemented)" with per-item gating constraints organized by feature family (timing / range-amplitude / shape / coordination / asymmetry / condition-response / indexing-widening / quality-flag-widening / long-format-alternative / multi-session-widening); preserved §Feature principle / §Output / §Features to avoid verbatim from pre-patch; 5 cross-references to notebook §7 "Known debt" with one citing `scripts/build_notebook.py:400`. | AC2 (F5) |
| `.cdd/unreleased/19/self-coherence.md` | +294 | α-side cycle artifact (`cdd/alpha/SKILL.md` §2.5) | n/a (process) |

Two docs files substantively touched. Zero code change. Zero new files. Zero charter/roadmap/ledger touch.

## What β verified (oracles re-run)

1. **AC1 string-equality (issue body §Proof plan fallback, dispatcher-authorized):** re-read `scripts/features.py::extract_features` (L137–147) and `analysis/feature-table-schema.md` §"Required Columns" (L11–35). Built 8×8 identity-column intersection table independently; all eight columns (`subject`, `session`, `trial_id`, `condition`, `side`, `cycle_number`, `quality_flag`, `exclusion_flag`) match in name. Value vocabularies (`L`/`R` for side; `ok`/`short`/`low_contact_gap` for quality_flag) also align. The running-notebook oracle (`jupyter nbconvert --execute`) is not runnable in the container per wave manifest §"Known constraints"; the issue body §Proof plan explicitly names the string-equality fallback for that case.
2. **AC1 wide-format enumeration:** schema §"Feature Data" (L41–44) lists the same set of wide-format columns that `grep -nE 'out\[' scripts/features.py` returns + `cycle_duration_s` (L31 init) + `normalized_curve_available` (L105 extract_shape return). Match is complete.
3. **AC1 direction-(b) verification (α flag 3):** re-ran `grep -nE "subject" scripts/build_notebook.py` → 18 hits. Identified which hits are inside generated analytic cells (L114, L117, L119, L130, L132, L140, L250–252, L257, L262, L327, L331, L365) — dataclass-attribute accesses inside the analytic computation, not schema-column references. Direction (a) (rename `Cycle.subject` to `Cycle.participant_code`) would require touching these analytic-cell references, which issue body §Non-goals forbids ("Touching the notebook's analytic cells"). Direction (b) is the only in-scope path. α's choice is forced by the scope wall, not discretionary. β endorses.
4. **AC2 catalog distinction:** `grep -niE '(first-pass set|candidate set)' analysis/features.md` → headers at L32 (`## First-pass set (currently implemented)`) and L72 (`## Candidate set (not yet implemented)`) plus prose at L166. The case-sensitive dispatcher-prompt regex hits only L166; the case-insensitive form (which the issue body's substantive AC reasonably reads as) finds the headers. AC2 first bullet met under both readings.
5. **AC2 first-pass list independent enumeration:** built the column set from `scripts/features.py` independently (`grep -nE 'out\['` + L31 + L105) and cross-matched against `analysis/features.md` §"First-pass set" subsections. Every code-emitted column has a named entry in the doc; no doc-listed first-pass column is missing from the code. Match is bijective.
6. **AC2 cross-reference to notebook §7 "Known debt":** `grep -nE 'notebook §7|Known debt' analysis/features.md` → 5 hits. One (L74) cites `scripts/build_notebook.py:400` for source-of-truth lookup.
7. **AC3 file surface:** `git diff --name-only 80698cf^..80698cf` → exactly `analysis/feature-table-schema.md` and `analysis/features.md`. `scripts/features.py` is not in the diff (`git show 80698cf -- scripts/features.py` is empty). Zero code change.
8. **AC3 no new column:** β read the post-patch schema doc. It *removes* columns (`cycle_start_frame`, `cycle_end_frame`, `exclusion_reason`, long-format `feature_name`/`feature_value`/`feature_unit`/`feature_method`/`source_file`) and shrinks value vocabularies. It does not add any column not already emitted by `scripts/features.py`.
9. **AC4 no charter touch:** `git show 80698cf -- README.md ROADMAP.md PROJECT.md CHANGELOG.md` → empty. No new files (`git diff --diff-filter=A` empty). REVISE posture intact at PROJECT.md L20.
10. **`scripts/build_notebook.py:400` spot-check:** confirmed the "Known debt" markdown cell exists in `build_notebook.py` around the cited line region (it generates the notebook §7 cell α's doc cross-references).

## Cross-sub debt

For δ wave-closeout consideration:

1. **Direction-(a) follow-up is the more correct fix.** Sub C took direction (b) because direction (a) requires touching analytic cells in `scripts/build_notebook.py` (18 `subject` references including inside generated cells), forbidden by §Non-goals. A future cycle with a wider scope wall can escalate: rename `Cycle.subject` to `Cycle.participant_code` across `scripts/segmentation.py` + `scripts/features.py` + `scripts/build_notebook.py` (analytic cells included), regenerate the notebook, revert the schema doc's `subject` → `participant_code`, switch doc voice from mixed-description back to pure-prescription. α §Debt 2; β concurs.

2. **`scripts/features.py::extract_shape` returns `{"normalized_curve_available": True}` unconditionally.** Pre-existing code debt the F5 doc pass surfaced. The boolean carries no information; the actual normalized curves live outside the table. Out of Sub C scope per §Non-goals. The post-patch `analysis/features.md` §Shape (L61) describes it accurately as a "boolean placeholder" with cross-ref to notebook §7. Wave-scoped follow-up: replace the always-true boolean with a more informative signal (per-cycle parquet path? sample count? presence-of-normalized-curve in the persisted bundle?). α §Debt 3; β concurs.

3. **Schema doc voice tension.** Direction (b) leaves `feature-table-schema.md` with mixed prescription/description voice. Named and bounded in the post-patch §Purpose, §Single-session note, and §Implementation Notes. Acceptable as bounded-description, not preferable to pure-prescription. Resolves under a direction-(a) follow-up. α §Self-check mistake-check 2; β concurs.

4. **`reports/field-report-02-friend-pre-pilot.md` stub H1 mismatch** (Sub B carry-over). β surfaces in Sub C debt list so the wave-closeout aggregates all cross-sub debt in one place. α §Debt 4.

## Identity discipline

| Commit | Author email | Role | Pass |
|---|---|---|---|
| `80698cf` (α impl) | `alpha@cph.cdd.cnos` | α | ✓ |
| `319ab3e` (α self-coherence) | `alpha@cph.cdd.cnos` | α | ✓ |
| this close-out commit | `beta@cph.cdd.cnos` | β | ✓ (pre-commit) |

Identity-isolation invariant (α ≠ β within Sub C) preserved.

## Next

- This close-out lands on `claude/review-repo-coherence-PNbjQ` as a commit marker.
- β proceeds to Sub D (cph#20) review.
- δ owns wave-closeout after all four subs reach terminal state.

β's role on cph#19 concludes here.
