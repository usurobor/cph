# β review — Sub D — cph#25 — F10 rename `extract_shape` placeholder

## Round 1

**Verdict:** APPROVE

**Round:** 1
**Wave:** `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/`
**Master:** usurobor/cph#21
**Sub:** usurobor/cph#25
**Base SHA (Sub D parent):** `d47a252` (Sub C self-coherence commit)
**Implementation SHA:** `129530b`
**Self-coherence SHA:** `e752ef8`
**Branch CI state:** N/A (no `.github/workflows/`)
**Branching:** single-branch dispatch on `claude/review-repo-coherence-PNbjQ` per wave manifest §"Branching deviation"

## Identity-audit

| Commit | Expected author | Observed | Pass |
|---|---|---|---|
| `129530b` (impl) | `α-as-agent <alpha@cph.cdd.cnos>` | `α-as-agent <alpha@cph.cdd.cnos>` | ✓ |
| `e752ef8` (self-coherence) | `α-as-agent <alpha@cph.cdd.cnos>` | `α-as-agent <alpha@cph.cdd.cnos>` | ✓ |
| this review commit | `β-as-agent <beta@cph.cdd.cnos>` | will be authored as `β-as-agent <beta@cph.cdd.cnos>` | ✓ (pre-commit) |

Identity-isolation invariant (α ≠ β within Sub D) preserved.

## AC-by-AC

### AC1 — function renamed; old name absent from live surfaces

**Code-side oracle (re-run β-independently, FIRST, per wave manifest §"β anchoring discipline" + AC7):**

β re-greps `scripts/features.py` directly for `extract_shape` BEFORE opening any doc:

```text
$ grep -n 'extract_shape' scripts/features.py
97:def extract_shape_sentinel(cycle: Cycle) -> dict:
149:    row.update(extract_shape_sentinel(cycle))
```

Two hits in `scripts/features.py`. Both carry the new name `extract_shape_sentinel`. No bare `extract_shape` remains in the code.

**β-side direct read of the post-patch function (L94–108):**

```text
$ sed -n '94,108p' scripts/features.py
    return out


def extract_shape_sentinel(cycle: Cycle) -> dict:
    """Shape features: PC scores deferred to aggregate phase; per-cycle
    record holds the 101-point normalized curves so PCA can run later.

    Returns a single column 'normalized_curve_path' that is filled by
    the notebook's aggregate cell after persisting per-cycle curves to
    a private parquet outside the repo.
    """
    return {"normalized_curve_available": True}


def extract_coordination(cycle: Cycle) -> dict:
```

Function body unchanged (docstring + `return {"normalized_curve_available": True}`). The signature `(cycle: Cycle) -> dict` is intact. Only the name on L97 has changed (`extract_shape` → `extract_shape_sentinel`).

**β-side direct read of the post-patch call site (L145–151):**

```text
$ sed -n '145,151p' scripts/features.py
        "exclusion_flag": cycle.quality_flag != "ok",
    }
    row.update(extract_timing(cycle))
    row.update(extract_range(cycle))
    row.update(extract_shape_sentinel(cycle))
    row.update(extract_coordination(cycle))
    return row
```

Call site at L149 calls `extract_shape_sentinel(cycle)`. The siblings `extract_timing`, `extract_range`, `extract_coordination` remain untouched.

**β-side word-boundary grep for old name (the load-bearing AC1 oracle):**

```text
$ grep -rn '\bextract_shape\b' --include="*.py" --include="*.md" --include="*.ipynb" --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude
(no matches; RC=1)
```

Empty. The word-boundary regex `\bextract_shape\b` matches `extract_shape` but not `extract_shape_sentinel` (the trailing `_` is a word-continuation character so `extract_shape` is not at a word boundary when followed by `_sentinel`). The old name is absent from every `*.py` / `*.md` / `*.ipynb` file in the live tree (excluding `.cdd/**` historical artifacts, `.git/**`, and `.claude/**` harness scaffolding).

**Doc-side cross-check (SECOND, per anchoring rule):**

```text
$ grep -rn '\bextract_shape\b' analysis/
(no matches)
```

`analysis/features.md` and `analysis/feature-table-schema.md` no longer reference the old name.

**Notebook-side cross-check:**

```text
$ grep -l 'extract_shape' notebooks/*.ipynb
(no matches; RC=1)
$ ls notebooks/
README.md
existing-data-processing.ipynb
```

Empty. The notebook does not reference `extract_shape` (or `extract_shape_sentinel`) — consistent with the issue body §Scope claim that the notebook calls `extract_features` (the umbrella), which transitively dispatches to `extract_shape_sentinel` via the renamed call site at `scripts/features.py:149`. No notebook regeneration needed; the notebook's source cells never name the inner function.

**Verdict:** AC1 met (word-boundary string-equality on the absence of the old name across all live surfaces; code-first anchoring discipline held).

### AC2 — new name appears at all required sites

**β-side oracle (re-run):**

```text
$ grep -rn '\bextract_shape_sentinel\b' --include="*.py" --include="*.md" --include="*.ipynb" --exclude-dir=.cdd --exclude-dir=.git --exclude-dir=.claude
scripts/features.py:97:def extract_shape_sentinel(cycle: Cycle) -> dict:
scripts/features.py:149:    row.update(extract_shape_sentinel(cycle))
analysis/features.md:59:### Shape — `extract_shape_sentinel`
analysis/feature-table-schema.md:43:- `extract_shape_sentinel` → `normalized_curve_available`
```

Four sites — identical site list to α's pre-patch grep with the name swapped:

| Site | Purpose |
|---|---|
| `scripts/features.py:97` | function definition |
| `scripts/features.py:149` | call site inside `extract_features` |
| `analysis/features.md:59` | §Shape section header |
| `analysis/feature-table-schema.md:43` | §"Feature Data" schema cross-reference |

No new surface introduced; no expected surface missed. The 4-site grep is bijective with the pre-patch enumeration.

**Verdict:** AC2 met.

### AC3 — return value unchanged

**β-side oracle (re-run, full diff):**

```text
$ git show 129530b -- scripts/features.py
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

Two hunks. Hunk 1 changes L97 only (`def extract_shape` → `def extract_shape_sentinel`). Hunk 2 changes L149 only (`row.update(extract_shape(cycle))` → `row.update(extract_shape_sentinel(cycle))`). The return statement (`return {"normalized_curve_available": True}` at L105) is in unchanged territory between the hunks — confirmed by β's direct read of L105 above.

Function signature `(cycle: Cycle) -> dict` is identical. Return-value-dict key `"normalized_curve_available"` is identical. Return-value-dict value `True` is identical. No behavior change.

**Verdict:** AC3 met.

### AC4 — direction recorded

α's `self-coherence.md` §"Direction choice" (L47–51) names direction **d-2**: "`extract_shape` → `extract_shape_sentinel`. Keeps the `extract_*` prefix (grep continuity for the family) and appends `_sentinel` to disambiguate from the computation-family siblings."

Rationale named (L51): "Direction (d-1) (`mark_shape_persisted`) names the actual semantic but breaks the `extract_*` prefix... Direction (d-3) (`shape_sentinel`) is the clearest semantic break but also loses prefix continuity. Direction (d-2) is the middle path."

**Verdict:** AC4 met.

### AC5 — no empirical drift, no new feature

**β-side oracle (re-run):**

```text
$ git show 129530b -- README.md PROJECT.md CHANGELOG.md ROADMAP.md
(empty)
```

No README / PROJECT / CHANGELOG / ROADMAP touch.

**REVISE posture check (PROJECT.md L20 at HEAD):**

PROJECT.md §"Current empirical decision" still `REVISE` (verified in Sub B/Sub C review). No new field report (no new file under `reports/` from the impl diff).

**New-feature check:** The function still returns `{"normalized_curve_available": True}` (a single-key dict mapping the column name to `True`). No new column. No new function (the existing function is renamed, not duplicated). The function's docstring is unchanged. The column `normalized_curve_available` is unchanged.

**Verdict:** AC5 met.

### AC6 — notebook not re-executed

**β-side oracle (re-run):**

```text
$ git show 129530b -- notebooks/existing-data-processing.ipynb
(empty)
```

The notebook is not in the patch diff.

**β-side spot check that the notebook genuinely does not reference `extract_shape`:**

```text
$ grep -l 'extract_shape' notebooks/*.ipynb
(no matches; RC=1)
```

The notebook does not reference `extract_shape` (or `extract_shape_sentinel`) at all — it calls `extract_features` (the umbrella). The transitive call chain `notebook → extract_features → extract_shape_sentinel` works correctly because the rename touches the function name + the in-`features.py` call site, both of which are inside the live code path. No notebook regeneration needed; the notebook's source cells need no edit.

**Verdict:** AC6 met.

### AC7 — β anchors on code first

This AC names β's process discipline. β honors it as follows:

1. The §AC1 verification above begins with the **code-side** oracle (`grep -n 'extract_shape' scripts/features.py` + direct read of L94–108 + L145–151) BEFORE opening any doc. The code-of-truth was anchored first; the docs were verified to match second.
2. The word-boundary regex `\bextract_shape\b` was chosen β-side to discriminate against `extract_shape_sentinel` (the trailing `_` is a word-continuation character so `extract_shape` does not match at a word boundary when followed by `_sentinel`). This is the correct oracle phrasing for an old-name-absent claim under a rename to a prefix-extended new name; β verified the regex behavior by also running the new-name grep (AC2 oracle returned the 4 expected sites, including the def at L97 — which is `extract_shape_sentinel`, NOT matching `\bextract_shape\b`).
3. β independently re-ran each grep rather than trusting α's reported output. β found the same site list (4 sites; bijective with α's pre-patch enumeration).

**Verdict:** AC7 met on β's side. The F7-class anchoring discipline the wave inherits from cph#21 §"Review mode" held.

## Notes

**N1 (`_sentinel` suffix is the natural inverse of the F7 fix pattern).** Sub A's F7 fix lifted code-emitted literals to match the schema (code-first authority over docs). Sub D's F10 fix renames code to better describe its placeholder behavior. Both are within the same "code is source of truth" stance: in F7, the schema deferred to the code; in F10, the code's own name was updated to be more honest about its semantics. The two subs together close the same class of drift (function/literal names that read like they mean more than they do). Named for ε's wave-level retrospective.

**N2 (`normalized_curve_available` always-True column is unchanged debt).** The rename signals placeholder semantics in the function name but the column itself remains a tautology (`True` always). Replacing the boolean with an informative signal (e.g. parquet path, sample count, last-write timestamp) is explicitly out of scope per cph#21 §Non-goals + the precursor wave-closeout §"Out-of-scope follow-ups". α §Debt 1; β concurs. Named for the next wave.

**N3 (notebook transitive call chain).** The notebook calls `extract_features` (umbrella), not `extract_shape` directly — so the rename does not require notebook regeneration. β verified via `grep -l 'extract_shape' notebooks/*.ipynb` returning empty (and the issue body §Scope makes the same claim). This is the structural reason Sub D could close without a `pip install nbformat ; python3 scripts/build_notebook.py` round (the F12-class wave-manifest-permission item the precursor wave navigated).

**N4 (`extract_*` family enumeration).** β re-greps `scripts/features.py` for `def extract_`:
```text
$ grep -n '^def extract_' scripts/features.py
24:def extract_timing(cycle: Cycle) -> dict:
72:def extract_range(cycle: Cycle) -> dict:
97:def extract_shape_sentinel(cycle: Cycle) -> dict:
108:def extract_coordination(cycle: Cycle) -> dict:
130:def extract_features(cycle: Cycle) -> dict:
```
Five functions in the family. The three computation siblings (`extract_timing`, `extract_range`, `extract_coordination`) are untouched. The umbrella `extract_features` (L130) is untouched. Only `extract_shape_sentinel` (the renamed function, L97) has the new name. Consistent.

## Scope-drift check

| Surface | Expected per wave manifest §"Issues" + cph#25 §Scope | Touched in diff? |
|---|---|---|
| `scripts/features.py:97` (function def) | yes | yes (1 line) |
| `scripts/features.py:149` (call site inside `extract_features`) | yes | yes (1 line) |
| `scripts/features.py` function body (L98–105 docstring + return) | no (preserved by issue body §Out) | no |
| `analysis/feature-table-schema.md:43` (§"Feature Data" arrow) | yes | yes (1 line) |
| `analysis/features.md:59` (§Shape section header) | yes | yes (1 line) |
| `analysis/features.md` L61 (bullet describing `normalized_curve_available`) | no (preserved) | no |
| `notebooks/existing-data-processing.ipynb` | no (notebook calls `extract_features` transitively) | no |
| `scripts/build_notebook.py` | no (no `extract_shape` reference per pre-patch grep) | no |
| `extract_timing` / `extract_range` / `extract_coordination` | no (only `extract_shape` is the sentinel) | no |
| `normalized_curve_available` column name | no (orthogonal; column name, not function name) | no |
| README / PROJECT / CHANGELOG / ROADMAP | no | no |
| `reports/*.md` | no | no |
| `.cdd/**` historical artifacts | no | no |

No scope-drift. α stayed inside Sub D's surface exactly. The three-file impl-diff (`scripts/features.py` + `analysis/feature-table-schema.md` + `analysis/features.md`) matches the wave manifest §"File-disjointness check" §Sub D prediction.

## Cross-sub debt (for δ wave-closeout)

1. **`normalized_curve_available` boolean is still always `True`.** The rename signals placeholder semantics in the function name but the column itself remains a tautology. Replacing with an informative signal (parquet path, sample count, last-write timestamp) is explicitly out of scope per cph#21 §Non-goals + precursor wave-closeout §"Out-of-scope follow-ups". α §Debt 1; β concurs. Future wave when shape extraction is materialized.

2. **The "always-True boolean" pattern is duplicated in the schema doc and features.md description.** Both surfaces describe `normalized_curve_available` as the column. A future cycle replacing the column needs to update both docs in lock-step. α §Debt 2; β concurs. Cross-sub debt with item 1.

3. **F12 (CHANGELOG entry for the precursor wave + this wave) is policy decision for ε/operator.** Re-noted from earlier subs; no Sub D CHANGELOG entry. α §Debt 3.

4. **`coh` not on PATH; no C_Σ baseline.** R0 §"Next action" gate (named in Sub B) still deferred. α §Debt 4.

## Round 1 close

AC1 (code-first oracle anchored on `scripts/features.py`; word-boundary `\bextract_shape\b` grep across `*.py`/`*.md`/`*.ipynb` returns empty; old name absent from all live surfaces), AC2 (new name `extract_shape_sentinel` at exactly 4 expected sites; bijective with α's pre-patch enumeration), AC3 (diff shows only the def line + call-site swap; function body unchanged; return value `{"normalized_curve_available": True}` identical), AC4 (direction d-2 named in α §"Direction choice" with rationale), AC5 (zero touches to README/PROJECT/CHANGELOG/ROADMAP; REVISE posture intact; no new column or function; docstring + column-name preserved), AC6 (notebook not in diff; β-verified the notebook does not reference `extract_shape` at all — transitive call via `extract_features` works correctly), AC7 (β re-greps `scripts/features.py` FIRST with word-boundary discrimination, doc + notebook cross-checks SECOND; F7-class anchoring discipline held) all met under independent β re-run. No scope-drift. No identity-isolation breach. Sub D APPROVE.
