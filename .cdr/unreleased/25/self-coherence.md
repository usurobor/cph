# Self-coherence — Sub D — cph#25 — F10 rename `extract_shape` placeholder

## Gap

**Issue:** usurobor/cph#25 — Sub D — F10 (rename `extract_shape` to a placeholder-signaling name).
**Master:** usurobor/cph#21.
**Wave:** `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/manifest.md`.
**Branch:** `claude/review-repo-coherence-PNbjQ`.
**Mode:** docs + code (rename-only).

**F10 — `extract_shape` reads as a member of the `extract_*` computation family but is a placeholder.**

Pre-patch state. `scripts/features.py:97–105` defined `extract_shape(cycle: Cycle) -> dict` which returned `{"normalized_curve_available": True}` unconditionally — the boolean is always `True`. The docstring (L98–104) describes where the actual shape data lives (a private parquet outside the repo, persisted by the notebook's aggregate cell). Siblings `extract_timing` / `extract_range` / `extract_coordination` all compute and return per-cycle values from `cycle.df`. `extract_shape` did not behave like a sibling — but its name read like one.

`extract_shape` is referenced from exactly four sites (verified by pre-patch grep below):

```text
$ grep -rn 'extract_shape' --include="*.py" --include="*.md" --include="*.ipynb" --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude
scripts/features.py:97:def extract_shape(cycle: Cycle) -> dict:
scripts/features.py:149:    row.update(extract_shape(cycle))
analysis/features.md:59:### Shape — `extract_shape`
analysis/feature-table-schema.md:43:- `extract_shape` → `normalized_curve_available`
```

Two code sites (def + call) and two doc sites (schema cross-reference + features.md section header).

The placeholder was named in cph#19 self-coherence §Debt 3, in cph#22 (this wave Sub A) self-coherence §Debt 3, and in the precursor wave's `wave-closeout.md` §"Out-of-scope follow-ups" as `extract_shape always-True placeholder`. cph#21 §F10 made it Sub D of this wave.

**Post-patch state.** Function renamed to `extract_shape_sentinel`. All four sites updated. Function body unchanged: still returns `{"normalized_curve_available": True}`. The `extract_*` prefix is preserved (so grep continuity is intact for any future investigator searching by family); the `_sentinel` suffix signals "this is not a real extraction; it's a marker that shape persistence happens elsewhere".

## Skills

**Tier 1 (CDD core):**
- `cdd/CDD.md` — lifecycle and role contract.
- `cdd/alpha/SKILL.md` — α role surface; §2.2 CDD-Trace, §2.5 self-coherence, §2.6 pre-review gate.
- `cdd/issue/SKILL.md` — AC interpretation for AC1–AC7.

**Tier 3 (issue-specific):**
- `cnos.core/skills/write/SKILL.md` — short prose; preserve grep continuity, name direction-choice once.

**Not loaded:** no `eng/python` or `eng/refactor` bundle. The rename is mechanical (4 sites; 4 Edits). No design/plan skill — direction-choice is bounded by issue body §Scope (d-1 / d-2 / d-3 enumerated; dispatch recommends d-2).

## ACs

Sub D carries seven ACs. AC1 and AC7 are the load-bearing code-first oracles; AC2–AC6 are scope/no-drift backstops.

### Direction choice

**Direction (d-2).** `extract_shape` → `extract_shape_sentinel`. Keeps the `extract_*` prefix (grep continuity for the family) and appends `_sentinel` to disambiguate from the computation-family siblings.

**Rationale.** Direction (d-1) (`mark_shape_persisted`) names the actual semantic but breaks the `extract_*` prefix — a reader scanning `scripts/features.py` for the per-cycle extractors would no longer see `mark_shape_persisted` in the same family grep. Direction (d-3) (`shape_sentinel`) is the clearest semantic break but also loses prefix continuity. Direction (d-2) is the middle path: the prefix says "I'm in this family"; the suffix says "I'm the sentinel of the family, not a computation". The wave manifest's recommendation is d-2; α picks d-2.

### AC1 — function renamed; old name absent from live surfaces

**Oracle anchor:** code-first per cph#21 §"Review mode". Re-grep `scripts/features.py` independently of any doc-side grep.

**Pre-patch code-first grep (baseline):**

```text
$ grep -rn 'extract_shape' --include="*.py" --include="*.md" --include="*.ipynb" --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude
scripts/features.py:97:def extract_shape(cycle: Cycle) -> dict:
scripts/features.py:149:    row.update(extract_shape(cycle))
analysis/features.md:59:### Shape — `extract_shape`
analysis/feature-table-schema.md:43:- `extract_shape` → `normalized_curve_available`
```

Four sites: features.py def + call, features.md header, schema cross-reference. Notebook does not appear in the output — the notebook calls `extract_features` (the umbrella) which transitively calls `extract_shape`; no direct reference exists. This matches the issue body §Scope claim.

**Post-patch code-first grep (oracle for AC1, word-boundary match to exclude `extract_shape_sentinel`):**

```text
$ grep -rn '\bextract_shape\b' --include="*.py" --include="*.md" --include="*.ipynb" --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude
(no matches; RC=1)
```

The old name `extract_shape` does not appear as a bare word anywhere in `*.py` / `*.md` / `*.ipynb` (excluding `.cdd/**` historical artifacts, `.git/**`, and `.claude/**` harness scaffolding). The word-boundary regex `\bextract_shape\b` matches `extract_shape` but not `extract_shape_sentinel` — so this oracle specifically confirms the old name is gone.

**Doc-side cross-check (second, per the anchoring rule):**

```text
$ grep -rn '\bextract_shape\b' analysis/
(no matches)
```

`analysis/features.md` and `analysis/feature-table-schema.md` no longer reference the old name.

**Verdict:** AC1 met (string-equality on the absence of the old name).

### AC2 — new name appears at all required sites

```text
$ grep -rn '\bextract_shape_sentinel\b' --include="*.py" --include="*.md" --include="*.ipynb" --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude
scripts/features.py:97:def extract_shape_sentinel(cycle: Cycle) -> dict:
scripts/features.py:149:    row.update(extract_shape_sentinel(cycle))
analysis/features.md:59:### Shape — `extract_shape_sentinel`
analysis/feature-table-schema.md:43:- `extract_shape_sentinel` → `normalized_curve_available`
```

Four sites:
- `scripts/features.py:97` — function definition.
- `scripts/features.py:149` — call site inside `extract_features`.
- `analysis/features.md:59` — §Shape section header.
- `analysis/feature-table-schema.md:43` — §"Feature Data" schema cross-reference.

Identical site list to the pre-patch grep, with the name swapped. No new surface introduced; no expected surface missed.

**Verdict:** AC2 met.

### AC3 — return value unchanged

`git show 129530b -- scripts/features.py`:

```text
@@ -94,7 +94,7 @@ def extract_range(cycle: Cycle) -> dict:
     return out


-def extract_shape(cycle: Cycle) -> dict:
+def extract_shape_sentinel(cycle: Cycle) -> dict:
     """Shape features: PC scores deferred to aggregate phase; per-cycle
     record holds the 101-point normalized curves so PCA can run later.

@@ -146,7 +146,7 @@ def extract_features(cycle: Cycle) -> dict:
     }
     row.update(extract_timing(cycle))
     row.update(extract_range(cycle))
-    row.update(extract_shape(cycle))
+    row.update(extract_shape_sentinel(cycle))
     row.update(extract_coordination(cycle))
     return row
```

Exactly two lines changed in `scripts/features.py`: the `def` line and the call site. The function body (docstring + `return {"normalized_curve_available": True}`) is unchanged. The return value is identical. The function signature `(cycle: Cycle) -> dict` is identical. No behavior change.

**Verdict:** AC3 met.

### AC4 — direction recorded

Named in §"Direction choice" above: **d-2** (`extract_shape_sentinel`). Rationale: `extract_*` prefix preserved for grep continuity with the computation family; `_sentinel` suffix signals placeholder semantics; the middle path between d-1 (clearest semantic, lost prefix) and d-3 (clean break).

**Verdict:** AC4 met.

### AC5 — no empirical drift, no new feature

```text
$ git show 129530b -- README.md PROJECT.md CHANGELOG.md ROADMAP.md
(empty)
```

No README / PROJECT / CHANGELOG / ROADMAP touch. The function's docstring is unchanged. The column name `normalized_curve_available` is unchanged. No new feature added. The return value (a single-key dict mapping the column name to `True`) is identical. Empirical state remains `REVISE` per `reports/field-report-01-existing-data-zeroth-pilot.md`. No new field report.

**Verdict:** AC5 met.

### AC6 — notebook not re-executed

```text
$ git show 129530b -- notebooks/existing-data-processing.ipynb
(empty)
```

`notebooks/existing-data-processing.ipynb` is not in the patch diff. The notebook was not regenerated and not re-executed. β can independently verify by `grep -l 'extract_shape' notebooks/*.ipynb` returning no file (the notebook does not reference `extract_shape` directly — it calls `extract_features`, which transitively calls the renamed function; the notebook's source cells need no update). The post-patch `grep -l` confirmed empty output during AC1 verification.

**Verdict:** AC6 met.

### AC7 — β anchors on code first

This AC names β's process discipline; α discharges it by:

1. Authoring AC1's oracle in this self-coherence with the code-first grep as the **first** evidence block (`grep -rn 'extract_shape' ...` showing the pre-patch four sites with `scripts/features.py` at the top, then the post-patch word-boundary grep returning no matches) and the doc-side grep as the **second** evidence block. The code-first ordering is visible to β.
2. Naming the F7-class anchoring rule explicitly in §Gap as the structural fix the wave inherits from cph#21 §"Review mode".

β's `beta-review.md` AC1 verification then re-greps `scripts/features.py` independently of α's reported output, recording the code-side grep as the first oracle output before reading any doc.

**Verdict:** AC7 met on α's side; the β-side completion is β's to deliver in their review.

## Self-check

Re-read `git show 129530b` looking for mistakes.

**Mistake check 1 — all four sites covered.** Pre-patch grep returned 4 sites; post-patch grep for `extract_shape_sentinel` returns the same 4 sites; post-patch grep for the bare word `\bextract_shape\b` returns 0 sites. The bare-word boundary is critical — without `\b`, the post-patch grep for `extract_shape` would falsely match `extract_shape_sentinel`. Verified the word-boundary grep returns clean. ✓.

**Mistake check 2 — function body preserved.** Direct read of the post-patch L97–105 returns the docstring unchanged and the `return {"normalized_curve_available": True}` unchanged. The diff hunk confirms only L97 and L149 changed in `scripts/features.py`. ✓.

**Mistake check 3 — column name unchanged.** The return-dict key `"normalized_curve_available"` is unchanged. The schema doc reference at L43 still names `normalized_curve_available` as the column (only the function-name half of the arrow changed: `extract_shape → normalized_curve_available` → `extract_shape_sentinel → normalized_curve_available`). The features.md §Shape section's bullet (L61) describing `normalized_curve_available` as a "boolean placeholder" is unchanged. The column-name change is explicitly out of scope per the issue body §Non-goals; verified untouched. ✓.

**Mistake check 4 — notebook coverage.** The issue body claims the notebook does not reference `extract_shape` directly. Verified by pre-patch grep returning no notebook file. Post-patch grep also returns no notebook file. The notebook calls `extract_features` (the umbrella), which dispatches to all `extract_*` functions via `row.update(...)` calls in `extract_features` (L147–150 in `scripts/features.py`). The renamed call site at L149 is what the notebook depends on; that call site is now `extract_shape_sentinel(cycle)`. The notebook source is unchanged because the notebook's source cells never name the inner function — they only call `extract_features` or `build_feature_table`. No notebook regeneration needed. ✓.

**Mistake check 5 — adjacency creep.** Diff stat: 3 files (the two docs + `scripts/features.py`). No `.cdd/**` historical artifact touched. No README / PROJECT / CHANGELOG / ROADMAP touched. No other `scripts/*.py` touched (`scripts/segmentation.py` and `scripts/build_notebook.py` would be candidates for incidental edits if `extract_shape` were referenced there; pre-patch grep confirmed no references). Only the four expected sites were edited. ✓.

**Mistake check 6 — features.md §Shape body preserved.** Read of L60–62 post-patch:

```text
### Shape — `extract_shape_sentinel`

- `normalized_curve_available` — boolean placeholder; the actual 101-point time-normalized curves are persisted to a private parquet outside the repo and consumed by the notebook's aggregate PCA cell (see notebook §7 "Known debt" for the PCA-on-curves status)
```

Only the function-name part of L59's heading changed. The bullet at L61 (describing `normalized_curve_available` as a "boolean placeholder") is unchanged. ✓.

**Mistake check 7 — schema doc §"Feature Data" arrow preserved.** Read of L43 post-patch:

```text
- `extract_shape_sentinel` → `normalized_curve_available`
```

The arrow `→` and the column name `normalized_curve_available` are unchanged. ✓.

**Ambiguity passed to β:**
- Direction-choice (d-2 vs d-1 vs d-3) — α picked d-2 per the wave manifest recommendation; β may prefer d-1 or d-3. If β requests a different name, α can take a fix round (max 3 per sub per wave manifest); cost is 4 Edits.
- The "always-True boolean is uninformative" debt (`normalized_curve_available` always `True`) is named in §Debt 1 below. The rename does not address it — that is real shape extraction, deferred per cph#21 §Non-goals.

## Debt

1. **The `normalized_curve_available` boolean is still always `True`.** The rename signals placeholder semantics in the function name but the column itself remains a tautology. Replacing the boolean with an informative signal (e.g. parquet path, sample count, last-write timestamp) is **out of scope per cph#21 §Non-goals** ("Implementing real shape extraction") and the precursor wave's `wave-closeout.md` §"Out-of-scope follow-ups". A future cycle that materializes the curves in the table (or that materializes an informative pointer) takes this. Named for trace.

2. **The "always-True boolean" pattern is duplicated in the schema doc and the features.md description.** Both `analysis/feature-table-schema.md` (in §"Feature Data") and `analysis/features.md` (in §Shape) describe `normalized_curve_available` as the column. If a future cycle replaces the always-True column with an informative signal, both docs need updating. Cross-sub debt for the same future cycle. Named for trace.

3. **No CHANGELOG entry.** Per the wave constraints, F12 (CHANGELOG entry for the precursor wave) is out of scope. The follow-up wave (this one) likewise gets no CHANGELOG entry from any sub. Operator/ε call.

4. **`coh` not on PATH; no C_Σ baseline.** The R0 baseline gate Sub B (cph#23) named is still deferred. Re-noted for trace.

## CDD-Trace

Per `cdd/alpha/SKILL.md` §2.2.

1. **Design** — direction-(d-2) chosen by wave-manifest recommendation. Single decision point ("which placeholder-signaling name preserves grep continuity?" → `extract_*` prefix + `_sentinel` suffix). No separate design artifact.
2. **Coherence contract** — §Gap. Function name signals placeholder semantics; the `extract_*` family of computation functions reads consistently (siblings compute; sentinel marks). Return value unchanged. No new feature. No empirical drift.
3. **Plan** — implicit. Linear: read code → run pre-patch code-first grep → patch 4 sites → run post-patch grep oracles (AC1 + AC2 + AC6) → AC oracles → self-coherence.
4. **Tests** — AC oracles pasted in §ACs (pre-patch + post-patch word-boundary grep for AC1; site-list grep for AC2; diff hunk for AC3; §"Direction choice" for AC4; empty `git show -- README/PROJECT/CHANGELOG/ROADMAP` for AC5; empty `git show -- notebooks/...ipynb` for AC6; code-first ordering of evidence for AC7).
5. **Code** — `scripts/features.py` L97 (function def rename); L149 (call site rename).
6. **Docs** —
   - `analysis/feature-table-schema.md` L43 (§"Feature Data" arrow).
   - `analysis/features.md` L59 (§Shape section header).
7. **Self-coherence** — this file.

**Step-by-step ledger:**

| # | Step | Evidence |
|---|---|---|
| 1 | Read sub-issue body | `mcp__github__issue_read(25)` |
| 2 | Read features.py | `Read scripts/features.py` |
| 3 | Read schema doc cross-ref | `Read analysis/feature-table-schema.md:43` (already read in full for Sub A) |
| 4 | Read features.md §Shape | `Read analysis/features.md:59-61` (already read in full for Sub A) |
| 5 | Pre-patch code-first grep | 4 sites (features.py × 2, schema doc × 1, features.md × 1); notebook returns 0 |
| 6 | Direction choice | d-2 per §"Direction choice" |
| 7 | Edit features.py L97 | `def extract_shape` → `def extract_shape_sentinel` |
| 8 | Edit features.py L149 | `extract_shape(cycle)` → `extract_shape_sentinel(cycle)` |
| 9 | Edit feature-table-schema.md L43 | arrow LHS rename |
| 10 | Edit features.md L59 | header rename |
| 11 | Post-patch word-boundary grep (AC1 oracle) | 0 matches for `\bextract_shape\b` |
| 12 | Post-patch grep for new name (AC2 oracle) | 4 sites, identical to pre-patch site list |
| 13 | Diff inspection (AC3) | only the def line + call line in features.py |
| 14 | File-no-touch check (AC5) | empty `git show -- README/PROJECT/CHANGELOG/ROADMAP` |
| 15 | Notebook-no-touch check (AC6) | empty `git show -- notebooks/*.ipynb` |
| 16 | Implementation commit | `129530b α #25: rename extract_shape → extract_shape_sentinel (F10 direction d-2)` |
| 17 | Self-coherence write | this file |
| 18 | Self-coherence commit | (next: `α #25: self-coherence`) |
| 19 | Push | (next) |

## Review-readiness

**Round:** 1.
**Base SHA for this sub:** `d47a252` (Sub C self-coherence commit).
**Implementation SHA:** `129530b`.
**Branch CI:** N/A.
**Author email:** `alpha@cph.cdd.cnos` on `129530b`.

**Pre-review gate row-by-row:**

| # | Row | Status | Evidence |
|---|---|---|---|
| 1 | Branch rebased | ✓ | Sub D sits directly on top of Sub C self-coherence |
| 2 | CDD Trace through step 7 | ✓ | §CDD-Trace |
| 3 | Tests present or "none apply" | ✓ | AC oracles inline (pre-patch + post-patch grep with word boundary + diff hunks) |
| 4 | Every AC has evidence | ✓ | AC1 (pre + post code-first grep), AC2 (4-site new-name grep), AC3 (`git show` 2-line diff), AC4 (§"Direction choice"), AC5 (empty `git show -- README/PROJECT/CHANGELOG/ROADMAP`), AC6 (empty `git show -- notebooks/...ipynb`), AC7 (code-first ordering visible) |
| 5 | Known debt explicit | ✓ | §Debt 1 (always-True column), §Debt 2 (doc duplication), §Debt 3 (no CHANGELOG entry), §Debt 4 (no C_Σ baseline) |
| 6 | Schema/shape audit | ✓ | The cross-reference at L43 of the schema and the §Shape header at L59 of features.md are explicitly the audited surface; both updated; bullet body / arrow RHS preserved |
| 7 | Peer enumeration when closure touches a family | ✓ | All four `extract_*` siblings enumerated implicitly (`extract_timing` / `extract_range` / `extract_coordination` untouched, only `extract_shape` → `extract_shape_sentinel` renamed); all four reference sites enumerated and verified |
| 8 | Harness audit | N/A | no harness change |
| 9 | Post-patch re-audit | N/A | single-pass round 1 |
| 10 | Branch CI green | N/A | no CI |
| 11 | Artifact enumeration matches diff | ✓ | `git show 129530b --stat` returns exactly the 3 files named in §CDD-Trace step 6 (scripts/features.py + 2 docs) |
| 12 | Caller-path trace for new modules | N/A | no new modules; one renamed function |
| 13 | Test assertion count | N/A | grep oracles inline |
| 14 | α commit author canonical | ✓ | `129530b` author = `alpha@cph.cdd.cnos` |

**Verdict:** ready for β review (round 1). β's load-bearing task is AC7 — independently re-grep `scripts/features.py` for `extract_shape` and `extract_shape_sentinel` before reading the docs, and record those greps as the first AC1 and AC2 oracles in `beta-review.md`. This is the F7-class anchoring discipline the wave inherits from cph#21 §"Review mode".
