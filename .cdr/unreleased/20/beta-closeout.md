# β close-out — Sub D (cph#20) — F4

## Verdict

**APPROVE** (round 1, no findings).

**Wave:** `.cdd/waves/coherence-drift-sweep-2026-05-18/`
**Master:** usurobor/cph#16
**Sub:** usurobor/cph#20
**Implementation SHA:** `8859b62`
**Self-coherence SHA:** `00f38b3`
**β review SHA:** (this commit)
**Branching:** single-branch dispatch on `claude/review-repo-coherence-PNbjQ` per wave manifest §"Branching deviation".

## What changed

| File | Lines changed | Surface | AC tested |
|---|---|---|---|
| `scripts/io_opencap.py` | +1 / −1 (L31, comment) | Module comment naming the output dir: `gait-support-paths-features/` → `cph-features/` | AC1 |
| `scripts/build_notebook.py` | +2 / −2 (L307, L382) | Two embedded source-cell strings: L307 (`PRIVATE_OUT = DATA_ROOT / "cph-features"`) + L382 (provenance markdown summary). Both inside `new_*_cell(...)` arguments — generator input, not generator logic. | AC1 |
| `notebooks/README.md` | +1 / −1 (L35) | Override-docs path citation: `<GAIT_DATA_ROOT>/cph-features/` | AC1 |
| `analysis/feature-summary-zeroth-pilot.md` | +1 / −1 (L27) | Provenance bullet: `$GAIT_DATA_ROOT/cph-features/features-zeroth-pilot.csv` | AC1 |
| `notebooks/existing-data-processing.ipynb` | 1418 lines changed (regeneration via `python3 scripts/build_notebook.py`) | Regenerated artifact: 2 substantive rename references (cells 19 + provenance markdown) + ~1300-line cached-execution-output strip (incidental — `build_notebook.py` emits cells without outputs; pre-patch notebook had cached outputs from a prior `jupyter nbconvert --execute` run). | AC2 |
| `.cdd/unreleased/20/self-coherence.md` | +268 | α-side cycle artifact (`cdd/alpha/SKILL.md` §2.5) | n/a (process) |

Five live surfaces touched matching wave manifest §"Issues" file list for Sub D verbatim. One regenerated artifact (the notebook). No charter docs, no field reports, no `.cdd/**` historical surfaces touched.

## What β verified (oracles re-run)

1. **AC1 negative oracle:** `grep -rln "gait-support-paths-features" . --exclude-dir=.git` → 8 hits, all inside the AC1-allowed surfaces (1 frozen field report at `reports/field-report-01-existing-data-zeroth-pilot.md`; 7 `.cdd/**` historical artifacts including α's own `.cdd/unreleased/20/self-coherence.md` §Gap text).
2. **AC1 positive oracle:** `grep -rln "cph-features" .` → 7 hits: the 4 source live surfaces (`scripts/io_opencap.py`, `scripts/build_notebook.py`, `notebooks/README.md`, `analysis/feature-summary-zeroth-pilot.md`), the regenerated notebook (`notebooks/existing-data-processing.ipynb`), α's self-coherence text, and the wave-manifest's pre-existing naming-recommendation mention at line 39.
3. **AC1 per-file count check:** `scripts/io_opencap.py`:1, `scripts/build_notebook.py`:2, `notebooks/README.md`:1, `analysis/feature-summary-zeroth-pilot.md`:1, `notebooks/existing-data-processing.ipynb`:2. Counts match expected per-file occurrence counts.
4. **AC1 rename consistency:** spot-checked each rename site for slash discipline and typo'd variants. All five sites preserve their pre-patch surrounding-character convention. No `cph_features` underscore-variant. No `cph-feature` singular.
5. **AC2 regenerated-notebook old-name absence:** `grep -c "gait-support-paths-features" notebooks/existing-data-processing.ipynb` → 0.
6. **AC2 regenerated-notebook new-name presence:** `grep -c "cph-features" notebooks/existing-data-processing.ipynb` → 2.
7. **AC2 structural integrity:** parsed .ipynb JSON via `python3 json`; enumerated all 21 cells; confirmed 7 sections (§1–§7 plus title + Configuration cell) are intact; cell 19 (`PRIVATE_OUT = DATA_ROOT / "cph-features"`) carries the rename directly; cell 20 (§7 "Known debt") is preserved (important for Sub C's cross-reference to still resolve).
8. **AC2 cross-sub consistency:** verified `scripts/build_notebook.py:400` still resolves to the §7 "Known debt" cell generator (Sub C's `analysis/features.md` cross-references this line; Sub D's edits at L307/L382 did not affect L400). `grep -nE 'Known debt' scripts/build_notebook.py` → L400.
9. **AC2 `pip install nbformat==5.10.4` audit:** verified `requirements.txt:16` carries the `nbformat==5.10.4` pin pre-existing; verified `git diff 319ab3e..8859b62 -- requirements.txt` is empty (no pin change). β-side disposition: install-to-match-spec, not a dependency change. Not a policy breach. Surfaced to ε in §Cross-sub debt for explicit confirmation.
10. **AC3 charter docs untouched:** `git show 8859b62 -- README.md PROJECT.md ROADMAP.md CHANGELOG.md` → empty. PROJECT.md L20 REVISE posture intact.
11. **AC3 substantive logic check:** read the diff to `scripts/build_notebook.py` — both edits are inside `new_*_cell(...)` arguments (cell-source string literals); zero generator logic change. `scripts/io_opencap.py` edit is comment-only (L31 starts with `#`).
12. **AC3 no new files:** `git diff --diff-filter=A --name-only 8859b62^..8859b62` → empty.
13. **AC4 reports/ untouched:** `git diff 8859b62^..8859b62 -- reports/` → empty. `reports/field-report-01-existing-data-zeroth-pilot.md:270` preserves the historical `gait-support-paths-features/` cite.
14. **AC4 .cdd/ untouched:** `git diff 8859b62^..8859b62 -- '.cdd/'` → empty. Prior-cycle artifacts in `.cdd/unreleased/{6,10}/` and wave scaffolding in `.cdd/waves/coherence-drift-sweep-2026-05-18/` unchanged.

## Cross-sub debt

For δ wave-closeout consideration:

1. **`pip install nbformat==5.10.4` policy interpretation (α flag 4).** Wave manifest §"Standing permissions" reads `Install Python packages: NO (this wave does not touch \`requirements.txt\`)`. α installed an already-pinned package (`nbformat==5.10.4` at `requirements.txt:16`) without modifying `requirements.txt`. β reads as install-to-match-spec; not a dependency change; not a policy breach. The strict-literal reading would make AC2 (notebook regeneration) infeasible. β surfaces to ε for explicit confirmation: should the wave-manifest standing-permissions wording be clarified to (a) explicitly allow install-to-match-spec, or (b) explicitly prohibit it and pre-install required runtime in the wave-open phase? Recommended: (a). β does not block on this.

2. **Operator-side on-disk migration `gait-support-paths-features/` → `cph-features/`.** Wave manifest §"Out-of-scope follow-ups" second bullet. Operator-owned; out of Sub D scope. Operators with existing data at `<GAIT_DATA_ROOT>/gait-support-paths-features/` will see the notebook create a parallel `cph-features/` directory on next re-run. α §Debt 4; β concurs.

3. **Notebook re-execution to re-bake outputs.** Sub D's regeneration produces a clean notebook (`build_notebook.py` emits cells without `outputs[]`). The pre-patch notebook had cached outputs from a prior `jupyter nbconvert --execute` run; those are stripped. Re-baking requires the operator's OpenCap Lab Validation archive and a local execution pass. Out of Sub D scope. α §Debt 2; β concurs.

4. **Wave manifest line 39 naming-recommendation mention.** Now slightly redundant (recommendation resolved to `cph-features/`). Editing wave scaffolding is out of Sub D scope. δ/ε may wish to update as part of wave-closeout. α §Debt 3.

5. **Aggregate debt from prior subs** (re-noted here so the wave-closeout has all cross-sub debt in one place):
   - **Sub A:** ROADMAP R0 §Next action is itself stale (names `cdr-refactor-2026-05-18` wave close, which already happened). Follow-on cycle should refresh to point at first numeric C_Σ baseline; PROJECT.md and ROADMAP will then realign literally.
   - **Sub B:** Stub H1/filename mismatch in `reports/field-report-02-friend-pre-pilot.md` (H1 says "Field Report 01 Friend Pre Pilot"; filename says "02"). Plus undocumented field-report numbering convention.
   - **Sub C:** Direction-(a) follow-up (rename `Cycle.subject` → `Cycle.participant_code` end-to-end, including in build_notebook.py analytic cells) is the more correct fix; Sub C took direction (b) because direction (a) requires touching analytic cells which §Non-goals forbids. Plus `extract_shape` `normalized_curve_available` always-`True` placeholder. Plus schema doc mixed prescription/description voice.

## Identity discipline

| Commit | Author email | Role | Pass |
|---|---|---|---|
| `8859b62` (α impl) | `alpha@cph.cdd.cnos` | α | ✓ |
| `00f38b3` (α self-coherence) | `alpha@cph.cdd.cnos` | α | ✓ |
| this close-out commit | `beta@cph.cdd.cnos` | β | ✓ (pre-commit) |

Identity-isolation invariant (α ≠ β within Sub D) preserved. Project-suffixed identity form (`{role}@cph.cdd.cnos`) observed across all sub commits in this wave.

## Next

- This close-out lands on `claude/review-repo-coherence-PNbjQ` as a commit marker.
- All four subs (cph#17, cph#18, cph#19, cph#20) have terminal β verdicts: APPROVE × 4.
- Master cph#16 stays open until δ writes the wave-closeout and operator gates the PR review on `claude/review-repo-coherence-PNbjQ` per wave manifest §"Branching deviation".
- ε may wish to comment on cross-sub debt items 1 (pip-install policy) and 5 (aggregate prior-sub debt).
- δ owns the wave-closeout (`.cdd/waves/coherence-drift-sweep-2026-05-18/wave-closeout.md`) and master cph#16 closure.

β's role on cph#20 concludes here. β's role on the wave concludes here.
