# β close-out — Sub D (cph#25) — F10 rename `extract_shape` placeholder

## Verdict

**APPROVE** (round 1, no findings).

**Wave:** `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/`
**Master:** usurobor/cph#21
**Sub:** usurobor/cph#25
**Implementation SHA:** `129530b`
**Self-coherence SHA:** `e752ef8`
**β review SHA:** (this commit)
**Branching:** single-branch dispatch on `claude/review-repo-coherence-PNbjQ` per wave manifest §"Branching deviation".

## What changed

| File | Lines changed | Surface | AC tested |
|---|---|---|---|
| `scripts/features.py` | 4 lines net (2 hunks, +2/-2): L97 `def extract_shape` → `def extract_shape_sentinel`; L149 call site `row.update(extract_shape(cycle))` → `row.update(extract_shape_sentinel(cycle))` | function def + transitive call site inside `extract_features` umbrella; function body (docstring + `return {"normalized_curve_available": True}`) unchanged | AC1, AC2, AC3, AC7 |
| `analysis/feature-table-schema.md` | 2 lines (1 hunk, +1/-1): L43 `extract_shape → normalized_curve_available` → `extract_shape_sentinel → normalized_curve_available` | §"Feature Data" cross-reference arrow LHS rename; column name on RHS preserved | AC1, AC2 |
| `analysis/features.md` | 2 lines (1 hunk, +1/-1): L59 `### Shape — \`extract_shape\`` → `### Shape — \`extract_shape_sentinel\`` | §Shape section header rename; L61 bullet body describing `normalized_curve_available` as "boolean placeholder" preserved | AC1, AC2 |
| `.cdd/unreleased/25/self-coherence.md` | +287 | α-side cycle artifact (`cdd/alpha/SKILL.md` §2.5) | n/a (process) |

Three live surfaces touched (code + 2 docs). Zero new files. Zero charter/roadmap/changelog touch. Zero notebook touch. Zero `scripts/build_notebook.py` touch. Zero `.cdd/**` historical artifact touch. Zero `extract_*` sibling touch (timing/range/coordination untouched).

## What β verified (oracles re-run)

1. **AC1 code-side anchor (β re-greps `scripts/features.py` FIRST, per wave manifest §"β anchoring discipline" + AC7):** `grep -n 'extract_shape' scripts/features.py` → 2 hits, both carrying new name `extract_shape_sentinel` (L97 def, L149 call). Direct read of L94–108 confirmed function body unchanged (docstring + `return {"normalized_curve_available": True}`). Direct read of L145–151 confirmed call site is `extract_shape_sentinel(cycle)` and sibling calls (timing/range/coordination) untouched.
2. **AC1 word-boundary grep (load-bearing oracle):** `grep -rn '\bextract_shape\b' --include="*.py" --include="*.md" --include="*.ipynb" --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude` → empty. The `\b` word boundary discriminates against `extract_shape_sentinel` (trailing `_` is a word-continuation character). Old name absent from all live `*.py`/`*.md`/`*.ipynb` surfaces.
3. **AC1 doc-side cross-check (SECOND):** `grep -rn '\bextract_shape\b' analysis/` → empty. Schema doc + features.md no longer reference the old name.
4. **AC1 notebook cross-check:** `grep -l 'extract_shape' notebooks/*.ipynb` → empty. The notebook does not reference `extract_shape` (or `extract_shape_sentinel`) directly — it calls the umbrella `extract_features`, which transitively dispatches to `extract_shape_sentinel` via the renamed call site at `scripts/features.py:149`. No notebook regeneration needed.
5. **AC2 new-name grep:** `grep -rn '\bextract_shape_sentinel\b' --include="*.py" --include="*.md" --include="*.ipynb" --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude` → exactly 4 hits: `scripts/features.py:97` (def), `scripts/features.py:149` (call), `analysis/features.md:59` (§Shape header), `analysis/feature-table-schema.md:43` (§"Feature Data" arrow). Bijective with α's pre-patch enumeration.
6. **AC3 return-value unchanged:** `git show 129530b -- scripts/features.py` shows 2 hunks. Hunk 1 changes only L97 (def); hunk 2 changes only L149 (call). L105 (return statement) is in unchanged territory between hunks. Function signature `(cycle: Cycle) -> dict` identical. Return-value dict `{"normalized_curve_available": True}` identical.
7. **AC4 direction recorded:** α §"Direction choice" (L47–51) names direction **d-2** (`extract_shape_sentinel`) with rationale: preserve `extract_*` prefix for grep continuity; `_sentinel` suffix signals placeholder; middle path between d-1 (broken prefix) and d-3 (clean break).
8. **AC5 no empirical drift:** `git show 129530b -- README.md PROJECT.md CHANGELOG.md ROADMAP.md` → empty. REVISE posture intact at PROJECT.md L20. No new column (return dict still maps single key `normalized_curve_available` to `True`). No new function.
9. **AC6 notebook not re-executed:** `git show 129530b -- notebooks/existing-data-processing.ipynb` → empty. `grep -l 'extract_shape' notebooks/*.ipynb` → empty (notebook never named the inner function directly).
10. **AC7 β code-first anchoring:** β authored §AC1 with `grep -n 'extract_shape' scripts/features.py` + direct-read of L94–108 + L145–151 BEFORE any doc-side grep was opened. Word-boundary regex chosen β-side to discriminate old name from new name. F7-class anchoring discipline held.
11. **`extract_*` family enumeration:** `grep -n '^def extract_' scripts/features.py` → 5 functions: `extract_timing` (L24), `extract_range` (L72), `extract_shape_sentinel` (L97, renamed), `extract_coordination` (L108), `extract_features` (L130, umbrella). Only the sentinel was renamed; three computation siblings + umbrella untouched.
12. **Identity audit:** `git log --format='%an <%ae>' 129530b e752ef8` → both `α-as-agent <alpha@cph.cdd.cnos>`. β-side commits will be `β-as-agent <beta@cph.cdd.cnos>` per identity-isolation invariant.

## Cross-sub debt

For δ wave-closeout consideration:

1. **`normalized_curve_available` boolean is still always `True`.** Rename signals placeholder semantics in the function name; the column itself remains a tautology. Out of scope per cph#21 §Non-goals + precursor wave-closeout §"Out-of-scope follow-ups". α §Debt 1; β concurs. Future wave when real shape extraction is materialized — both the schema doc and features.md need updating in lock-step.

2. **Doc duplication of the "always-True boolean" description.** Both `analysis/feature-table-schema.md` (§"Feature Data" L43) and `analysis/features.md` (§Shape L61) describe `normalized_curve_available`. A future cycle replacing the column needs both docs. α §Debt 2; β concurs. Cross-sub with item 1.

3. **F12 (CHANGELOG entry for the precursor wave + this wave) is policy decision for ε/operator.** Re-noted from prior subs. α §Debt 3.

4. **`coh` not on PATH; no C_Σ baseline.** R0 §"Next action" gate (named in Sub B) still deferred. α §Debt 4.

5. **(β-axis observation, cross-sub with Sub A.)** Sub A's F7 fix lifted code-emitted literals to match the schema (code-first authority over docs). Sub D's F10 fix renames code to better describe its placeholder behavior. Both close the same class of drift — function/literal names that read like they mean more than they do. ε's wave-level retrospective might surface this pattern as a candidate for a single `cdd/beta/SKILL.md` patch ("anchor on code-emitted reality when reviewing code/doc alignment claims") alongside the F7-class anchoring discipline that the wave manifest §"β anchoring discipline" already proposes.

## Identity discipline

| Commit | Author email | Role | Pass |
|---|---|---|---|
| `129530b` (α impl) | `alpha@cph.cdd.cnos` | α | ✓ |
| `e752ef8` (α self-coherence) | `alpha@cph.cdd.cnos` | α | ✓ |
| β review commit | `beta@cph.cdd.cnos` | β | ✓ (pre-commit) |
| β close-out commit | `beta@cph.cdd.cnos` | β | ✓ (pre-commit) |

Identity-isolation invariant (α ≠ β within Sub D) preserved by Agent-session boundary.

## Next

- This close-out lands on `claude/review-repo-coherence-PNbjQ` as a commit marker.
- All four subs (cph#22, cph#23, cph#24, cph#25) reach terminal state APPROVE round 1.
- δ owns wave-closeout: write `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/wave-closeout.md`, comment on master cph#21, surface cross-sub debt to ε.

β's role on cph#25 concludes here. β's role on the wave concludes here.
