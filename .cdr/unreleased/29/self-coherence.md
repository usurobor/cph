<!-- sections: [Gap, ACs, Self-check, Debt] -->
<!-- completed: [Gap, ACs, Self-check, Debt] -->

# α self-coherence — cph#29 — feature-table schema doc-drift on `detection_method`

## Gap

**Issue:** [usurobor/cph#29](https://github.com/usurobor/cph/issues/29) — "feature-table schema doc-drift on detection_method column (post-cph#28); recurring sibling-surface pattern" (small docs-only cycle per `CDD.md` §1.2; named as known debt D1 in `.cdr/unreleased/28/self-coherence.md §Debt` and `.cdr/unreleased/28/alpha-closeout.md`).

**Gap.** cph#28 added a `detection_method` string column to the per-cycle feature table emitted by `scripts/features.py::extract_features` with values `"measured" | "inferred_contralateral" | "inferred_contralateral_partial"`. The schema-doc surfaces — `analysis/feature-table-schema.md` and `analysis/features.md` — were not co-updated; a downstream R3-bilateral / R4-falsification consumer reading the schema doc would not see the column documented. This cycle is the docs-coherence tidy that resolves D1 from cph#28.

**Scope (binding, from issue body):**

1. Add a `detection_method` row to `analysis/feature-table-schema.md` under §"Cycle Definition" or §"Detection provenance" (new subsection — α chose the new subsection so that the §"Cycle Definition" row stays exclusively about `cycle_number`, and the path-(a) honesty caveat earns its own header); document the three realized values verbatim from `scripts/features.py` / `scripts/segmentation_contralateral.py` / `scripts/segmentation.py::Cycle.detection_method`.
2. Update `analysis/features.md` to name `detection_method` in the feature catalog with the same value enumeration.
3. Cross-reference both surfaces back to the producer modules.

**Non-goals (preserved):** no edits to `scripts/features.py`, `scripts/segmentation.py`, `scripts/segmentation_contralateral.py`, `notebooks/existing-data-processing.ipynb`, `PROJECT.md`, `ROADMAP.md`, `CHANGELOG.md`, `README.md`, `docs/concepts/*`, `docs/articles/*`. No data files committed (preserves cph#28 AC8).

## ACs

cph#29 carries 5 ACs.

### AC1 — `analysis/feature-table-schema.md` documents the `detection_method` column with the three realized values

**Surface:** new §"Detection provenance" subsection under §"Required Columns" (between §"Cycle Definition" and §"Quality Control"); new §"detection_method" subsection under §"Allowed Values" (between §"side" and §"quality_flag"). The detection-provenance row gives the column type (`string`), null=`No`, and the example value set; the Allowed-Values block enumerates the three realized values with each value's semantic + producer-module crossreference.

**Evidence (grep oracle on the schema doc):**

```
$ grep -nE 'detection_method|Detection provenance' analysis/feature-table-schema.md
```

names: §"Detection provenance" header, the table row (`| detection_method | string | ... |`), the cross-reference paragraph naming `scripts/segmentation.py::Cycle.detection_method` + `scripts/segmentation_contralateral.py::segment_trial_with_contralateral_l` + `analysis/r3_subject_aggregate_tests.py::NON_FEATURE_COLS`, the §"detection_method" §Allowed Values block with three bullet entries, and the updated §"Example Rows" CSV (which now shows a `detection_method` column with one `measured` row and one `inferred_contralateral_partial` row). **PASS.**

### AC2 — `analysis/features.md` names `detection_method` in the feature catalog

**Surface:** new bullet under §"Required indexing" naming `detection_method` with values `measured`/`inferred_contralateral`/`inferred_contralateral_partial`, the path-(a) honesty caveat one-liner, the producer-module cross-reference, and the `NON_FEATURE_COLS` exclusion note. Placed in §"Required indexing" (not §"First-pass set") because the column is an indexing/provenance column, not a feature — matching how `quality_flag` / `exclusion_flag` are categorized.

**Evidence:**

```
$ grep -n 'detection_method\|detection method' analysis/features.md
```

names: the new bullet in §"Required indexing", the cross-reference to the schema doc §"detection_method", and the closing prose's pointer to §"Detection provenance" alongside §"Identification". **PASS.**

### AC3 — Schema doc + features.md catalog enumerate the same value set as `scripts/features.py` and `scripts/segmentation_contralateral.py` (grep oracle)

**Grep oracle on the three string literals:**

```
$ grep -hoE '"(measured|inferred_contralateral_partial|inferred_contralateral)"' \
    scripts/features.py scripts/segmentation.py scripts/segmentation_contralateral.py | sort -u
"inferred_contralateral"
"inferred_contralateral_partial"
"measured"

$ grep -hoE '`(measured|inferred_contralateral_partial|inferred_contralateral)`|"(measured|inferred_contralateral_partial|inferred_contralateral)"' \
    analysis/feature-table-schema.md | sort -u
"inferred_contralateral"
"inferred_contralateral_partial"
"measured"
`inferred_contralateral_partial`
`inferred_contralateral`
`measured`

$ grep -hoE '`(measured|inferred_contralateral_partial|inferred_contralateral)`|"(measured|inferred_contralateral_partial|inferred_contralateral)"' \
    analysis/features.md | sort -u
`inferred_contralateral_partial`
`inferred_contralateral`
`measured`
```

All three surfaces enumerate the same three-literal set; no extras, no omissions. **PASS.**

### AC4 — No regression on any other feature column documented in the schema doc; no charter drift

**Schema-doc regression check.** The edits add (a) a §"Detection provenance" subsection, (b) a §"detection_method" Allowed Values block, and (c) a `detection_method` column inserted into the §"Example Rows" CSV header + each of the three example rows. No removals; no changes to the pre-existing rows for `subject` / `session` / `trial_id` / `condition` / `side` / `cycle_number` / `quality_flag` / `exclusion_flag` / Feature Data bullets / quality_flag values / Data Rules. Verified via `git diff origin/main..HEAD -- analysis/feature-table-schema.md` — the diff is purely additive plus the CSV header/row insertion.

**Charter drift check.**

```
$ git diff origin/main..HEAD --name-only | grep -E 'README\.md|^docs/(concepts|articles)/|PROJECT\.md|ROADMAP\.md|CHANGELOG\.md|^notebooks/|^scripts/'
```

(expected empty) — only `analysis/feature-table-schema.md`, `analysis/features.md`, and `.cdr/unreleased/29/self-coherence.md` are touched. **PASS.**

### AC5 — No data files committed (preserves cph#28 AC8)

**Oracle:**

```
$ git diff origin/main..HEAD --name-only | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$' || echo NONE
NONE
```

**PASS.**

## Self-check

**Did α push ambiguity onto β?** Two places where this could plausibly happen, with mitigations:

1. **Placement choice — §"Cycle Definition" row vs. new §"Detection provenance" subsection.** The issue body explicitly delegates this judgement to α ("under §"Cycle Definition" OR a new §"Detection provenance" subsection — your judgment"). α chose the new subsection so the path-(a) honesty caveat earns its own header (the column carries semantic content distinct from `cycle_number` — it tags the provenance of how endpoints were obtained, which is closer in spirit to `quality_flag` than to `cycle_number`). β can challenge the placement; the row content (type / null / example values / cross-references) would be identical under either placement.

2. **Catalog vs. indexing in `analysis/features.md`.** The issue body says "Name `detection_method` in the feature catalog" but the column is not a feature — it's an indexing/provenance column. α placed it in §"Required indexing" (where `quality_flag` and `exclusion_flag` already live), not §"First-pass set", because the new bullet sits naturally alongside the other non-feature indexing columns. β can challenge this if the literal reading of "feature catalog" is binding; the relocation is a single bullet move.

**Every claim backed by evidence in the diff?** Yes — each AC row names a specific surface (file path + section); each grep oracle is reproducible from `git diff origin/main..HEAD`.

**Peer enumeration.** The change touches a small family of surfaces, all docs:

- **Schema-bearing docs:** `analysis/feature-table-schema.md` (updated), `analysis/features.md` (updated). These are the only two surfaces in the repo that enumerate feature-table column values.
- **Schema-consuming code:** `analysis/r3_subject_aggregate_tests.py` (touched in cph#28; `NON_FEATURE_COLS` already excludes `detection_method`; this cycle adds cross-references *to* it but does not modify it).
- **Producer code:** `scripts/features.py`, `scripts/segmentation.py`, `scripts/segmentation_contralateral.py` — explicitly out of scope per cph#29 issue body; α confirms (via the AC3 grep oracle) the literal set matches.

**Schema audit (alpha/SKILL.md §2.6 row 6).** The cph#28 audit named D1 as the schema-doc-drift gap; this cycle is the gap's resolution. Post-cycle, the schema doc and features.md catalog enumerate the same value set as the producer modules (AC3 PASS). Audit re-runs clean.

## Debt

None named by this cycle. D1 from `.cdr/unreleased/28/self-coherence.md §Debt` is resolved by AC1–AC3.

ε's filing in the cph#29 issue body names a project-side discipline-level pattern ("when a feature column is added to `scripts/features.py`, the schema doc + features.md catalog do not have a co-update gate"). This cycle resolves the instance but does not install a co-update gate; whether to add such a gate (e.g., a CI check that grep-extracts string literals from `scripts/features.py` and asserts they appear in the schema doc) is out of scope for this docs-only cycle and is left for ε to decide whether to file as a follow-on cycle.
