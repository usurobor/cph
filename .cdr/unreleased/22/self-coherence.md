# Self-coherence — Sub A — cph#22 — F7 quality_flag schema↔code vocabulary alignment

## Gap

**Issue:** usurobor/cph#22 — Sub A — F7 quality_flag schema↔code vocabulary alignment.
**Master:** usurobor/cph#21.
**Wave:** `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/manifest.md`.
**Branch:** `claude/review-repo-coherence-PNbjQ`.
**Mode:** docs + code (small).

**F7 — schema vs code quality_flag vocabulary mismatch.**

Pre-patch state (verified by `git show ced1425:scripts/segmentation.py | grep -n quality_flag` — the `ced1425` baseline that landed the segmenter in cph#6):

```text
ced1425:scripts/segmentation.py:35:    quality_flag: str = "ok"
ced1425:scripts/segmentation.py:121:                quality_flag="ok" if 0.5 < duration < 1.8 else "out_of_range",
```

The code emitted exactly two literals: `"ok"` (when `0.5 < duration < 1.8`) and `"out_of_range"` (otherwise). The schema doc `analysis/feature-table-schema.md` (pre-patch) prescribed `"ok"` / `"short"` / `"low_contact_gap"`; the example CSV row L87 carried `quality_flag=short`; `analysis/features.md` L27 / L132 / L137 referenced the same `ok`/`short`/`low_contact_gap` vocabulary. The values `"short"` and `"low_contact_gap"` were never produced by the code; the code's `"out_of_range"` literal never appeared in any doc.

This is the β-axis miss that the precursor wave (`coherence-drift-sweep-2026-05-18`, master cph#16) Sub C (cph#19, F3) was supposed to fix. Both prior-wave α and β anchored AC1 verification on the schema doc rather than re-grepping `scripts/segmentation.py`, so the mismatch slipped through. cph#21 §F7 named the miss and §"Review mode" named the structural fix: code-first oracle anchoring on any AC of form "doc matches code".

**Post-patch state.** Code emits `"ok"` / `"short"` / `"long"`; schema lists `"ok"` / `"short"` / `"long"`; example row CSV uses `short`; features.md L27 lists `ok`/`short`/`long`; features.md §"Quality-flag widening" (L137) describes what the schema now lists vs. what's deferred. String-for-string equality.

## Skills

**Tier 1 (CDD core):**
- `cdd/CDD.md` — lifecycle and role contract.
- `cdd/alpha/SKILL.md` — α role surface; §2.2 CDD-Trace steps, §2.5 self-coherence, §2.6 pre-review gate.
- `cdd/issue/SKILL.md` — AC interpretation for AC1–AC5.

**Tier 3 (issue-specific):**
- `cnos.core/skills/write/SKILL.md` — short prose; name files+lines, distinguish prescription from description, state direction-choice once.

**Not loaded:** no `eng/python` or `eng/markdown` bundle. Sub A is a 4-line Python literal change plus three small markdown edits; no design/plan skill — direction-choice is bounded by issue body §Scope (a-1/a-2/a-3 enumerated) and the wave manifest names a-1 as the recommendation.

## ACs

Sub A carries five ACs. AC1 is the load-bearing code-first oracle; AC5 names the β-anchoring discipline patch that β honors on their side.

### Direction choice

**Direction (a-1).** Emit `"short"` for `duration <= 0.5`, `"long"` for `duration >= 1.8`, `"ok"` otherwise. The schema doc lists exactly those three labels; `"low_contact_gap"` is named in `analysis/features.md` §"Quality-flag widening" as future-segmenter debt (gated on adding contact-gap inspection to the segmenter).

**Rationale.** Direction (a-1) is the cleanest 3-value vocabulary the segmenter can produce today using only `duration`. It distinguishes which threshold fired (short cycle vs long cycle), which is information the segmenter has but `"out_of_range"` discarded. Direction (a-2) (keep `"out_of_range"` as a generic label) would land a 2-value or schema-narrowing patch and lose the short-vs-long distinction. Direction (a-3) (add a true contact-gap check) is out of scope per §Non-goals unless the check is ≤10 lines, and adding swing-time or force-plate hints to the segmenter is larger than that; deferred under §"Quality-flag widening". The wave manifest's recommendation is a-1; α picks a-1.

### AC1 — code and schema agree on `quality_flag` literals (string-equality)

**Oracle anchor:** code-first per cph#21 §"Review mode". Read `scripts/segmentation.py` first; record the emitted literals; verify each doc reference matches the code-emitted set.

**Code-side grep (oracle anchor):**

```text
$ grep -nE 'quality_flag\s*=\s*"' scripts/segmentation.py
35:    quality_flag: str = "ok"
122:                quality_flag=("short" if duration <= 0.5
```

(L35 is the dataclass default; L122 is the segment_trial constructor with the multi-line conditional. The full literal set emitted at L122–124 is `"short"`, `"long"`, `"ok"`.)

Expanded look at the constructor (L122–124):

```text
$ sed -n '122,124p' scripts/segmentation.py
                quality_flag=("short" if duration <= 0.5
                              else "long" if duration >= 1.8
                              else "ok"),
```

**Code-emitted set:** {`"ok"`, `"short"`, `"long"`}.

**Doc-side cross-check (second, per the anchoring rule):**

```text
$ grep -nE '"(ok|short|long|low_contact_gap|out_of_range)"' analysis/feature-table-schema.md analysis/features.md
analysis/features.md:28:- exclusion flag (column `exclusion_flag`; derived as `quality_flag != "ok"`)
analysis/feature-table-schema.md:32:| `quality_flag` | string | Data quality assessment | No | "ok", "short", "long" |
analysis/feature-table-schema.md:33:| `exclusion_flag` | boolean | Should cycle be excluded from analysis (derived: `quality_flag != "ok"`) | No | True, False |
analysis/feature-table-schema.md:35:(`exclusion_reason` is not currently emitted as a separate column; the reason is implicit in `quality_flag` ("short", "long"). Materializing it as a dedicated string column is named in `analysis/features.md` §"Candidate set" → indexing widening.)
analysis/feature-table-schema.md:78:3. **Quality gates**: `exclusion_flag` is derived as `quality_flag != "ok"` by `scripts/features.py::extract_features`. No row should carry `quality_flag="ok"` with `exclusion_flag=True` (the derivation makes this impossible by construction).
```

Plus the §"Allowed Values" §quality_flag block at L64–72 and the example row L87, which use backtick-quoted (not double-quoted) literals so they don't match the grep regex above. Inspected directly:

```text
$ sed -n '64,72p' analysis/feature-table-schema.md
### quality_flag

Realized values emitted by `scripts/segmentation.py::segment_trial` and propagated through `scripts/features.py::extract_features`:

- `ok`: cycle duration in `(0.5, 1.8)` seconds; cycle passes segmenter QC
- `short`: cycle duration `<= 0.5` seconds (below typical adult walking range); `exclusion_flag=True`
- `long`: cycle duration `>= 1.8` seconds (above typical adult walking range, includes detector dropouts that produced a heel-strike-to-next-heel-strike interval that is too long to be a single cycle); `exclusion_flag=True`

(An earlier draft of this schema listed `good` / `fair` / `poor` / `unusable`, and a later draft listed `low_contact_gap` as a third realized label. ...)
```

```text
$ sed -n '85,87p' analysis/feature-table-schema.md
subject2,S01,walking1,walking,R,3,ok,False,1.05,0.65,0.40,61.9,38.4,55.2,12.5
subject2,S01,walking1,walking,L,3,ok,False,1.04,0.63,0.41,60.6,37.9,54.8,13.1
subject4,S01,walking2,walking,R,1,short,True,0.42,0.25,0.17,59.5,18.2,28.3,
```

`analysis/features.md` references:

```text
$ grep -nE 'ok|short|long' analysis/features.md | grep -E 'quality_flag|`short`|`long`|`ok`'
27:- quality flag (column `quality_flag`; values `ok`/`short`/`long` per `analysis/feature-table-schema.md` §"quality_flag")
28:- exclusion flag (column `exclusion_flag`; derived as `quality_flag != "ok"`)
132:- `exclusion_reason` — currently implicit in `quality_flag` values (`short`, `long`); materializing as a dedicated string column is a small ergonomic improvement
137:The schema doc originally listed `good` / `fair` / `poor` / `unusable`; an interim draft listed `ok` / `short` / `low_contact_gap`. The code emits `ok` / `short` / `long`, where `short` and `long` are derived from cycle duration alone (`duration <= 0.5` and `duration >= 1.8` respectively, in `scripts/segmentation.py::segment_trial`). ...
```

**Cross-reference intersection table:**

| Surface | Realized values |
|---|---|
| `scripts/segmentation.py:122–124` (code-of-truth) | `ok`, `short`, `long` |
| `analysis/feature-table-schema.md:32` §Quality Control | `ok`, `short`, `long` |
| `analysis/feature-table-schema.md:68–70` §quality_flag allowed-values | `ok`, `short`, `long` |
| `analysis/feature-table-schema.md:87` example row | `short` (realized; produced by code) |
| `analysis/features.md:27` §Required indexing | `ok`, `short`, `long` |
| `analysis/features.md:132` §indexing-widening | `short`, `long` (referenced in exclusion_reason note) |
| `analysis/features.md:137` §Quality-flag widening | names code-emitted set `ok`/`short`/`long` and historical drafts |

All five surfaces agree string-for-string on the code-emitted set. The example row at L87 carries `short` — a value the code actually emits. `low_contact_gap` appears at L72 / L137 only as historical-draft/deferred-work context, named explicitly as not realized in code today.

**Verdict:** AC1 met (string-equality on code-emitted vocabulary).

### AC2 — direction recorded

Named in §"Direction choice" above: **a-1**. Rationale: cleanest 3-value vocabulary the segmenter can produce from `duration` alone; distinguishes which threshold fired without introducing a new segmenter check. `low_contact_gap` named as future-segmenter debt with the gating constraint (segmenter would need to inspect contact-gap structure, not just `duration`) in `analysis/features.md` §"Quality-flag widening" L135–137.

**Verdict:** AC2 met.

### AC3 — no other surfaces touched without naming them

```text
$ git show a697265 --stat
 analysis/feature-table-schema.md | 14 +++++++-------
 analysis/features.md             |  6 +++---
 scripts/segmentation.py          |  4 +++-
 3 files changed, 13 insertions(+), 11 deletions(-)
```

Exactly the expected three files. No notebook regeneration. No `scripts/features.py` touch (it propagates `cycle.quality_flag` through and derives `exclusion_flag = quality_flag != "ok"`, both of which work unchanged for the new vocabulary). No `.cdd/**` historical artifact touched.

**Verdict:** AC3 met.

### AC4 — no empirical drift

```text
$ git show a697265 -- README.md PROJECT.md CHANGELOG.md ROADMAP.md
(empty)
```

No README / PROJECT / CHANGELOG / ROADMAP file touched. PROJECT.md §"Current empirical decision" remains `REVISE`. No new field report. `reports/field-report-01-existing-data-zeroth-pilot.md` untouched. Schema doc and features.md edits are vocabulary/wording changes that do not introduce or modify any empirical claim — they describe what the segmenter emits (which is unchanged in semantic) using the new literal names.

**Verdict:** AC4 met.

### AC5 — β anchors on code first

This AC names β's process discipline; α discharges it by:

1. Authoring AC1's oracle in this self-coherence with the code-side grep as the **first** evidence block (the `grep -nE 'quality_flag\s*=\s*"' scripts/segmentation.py` block at the top of §AC1) and the doc-side grep as the **second** evidence block. This makes the code-first ordering visible to β.
2. Naming the anchoring rule explicitly in §Gap as the structural fix the wave inherits from cph#21 §"Review mode".

β's own `beta-review.md` AC1 verification then re-greps `scripts/segmentation.py` independently of α's reported output, recording the code-side grep as the first oracle output before reading any doc.

**Verdict:** AC5 met on α's side; the β-side completion is β's to deliver in their review.

## Self-check

Re-read `git show a697265` looking for mistakes.

**Mistake check 1 — code-side correctness of the conditional.** The new constructor reads:

```python
quality_flag=("short" if duration <= 0.5
              else "long" if duration >= 1.8
              else "ok"),
```

Python parses this as `("short" if duration <= 0.5 else ("long" if duration >= 1.8 else "ok"))`. For `duration = 0.5` → `"short"` (boundary inclusive). For `duration = 1.8` → `"long"` (boundary inclusive). For `duration = 1.0` → `"ok"`. For `duration = 0.4` → `"short"`. For `duration = 2.0` → `"long"`. No path emits any other literal. The dataclass default at L35 (`quality_flag: str = "ok"`) is the fallback if a `Cycle(...)` constructor call ever omits the keyword; the segment_trial constructor always supplies the keyword, so the default is never used on the segmenter path. (A future caller that constructs a `Cycle` directly without `quality_flag` would receive `"ok"`.)

**Mistake check 2 — boundary-condition consistency with schema.** Schema §quality_flag L68 reads: "ok: cycle duration in `(0.5, 1.8)` seconds". The interval `(0.5, 1.8)` is open in both math-interval notation and Python's strict inequality. The code uses `duration <= 0.5` → `"short"` and `duration >= 1.8` → `"long"`. Boundary `duration = 0.5` exactly: schema says "in `(0.5, 1.8)`" → not in → not `ok` → must be `short`/`long`; code says `<=0.5` → `short`. ✓. Boundary `duration = 1.8` exactly: schema says not `ok` → must be `short`/`long`; code says `>=1.8` → `long`. ✓. Consistent.

**Mistake check 3 — features.py downstream.** `scripts/features.py:144–145` reads:

```python
"quality_flag": cycle.quality_flag,
"exclusion_flag": cycle.quality_flag != "ok",
```

For the new vocabulary {`ok`, `short`, `long`}: `exclusion_flag = True` for `short` and `long`, `False` for `ok`. The Data Rule at schema L78 ("No row should carry `quality_flag='ok'` with `exclusion_flag=True`") holds by construction. The example row at L87 has `quality_flag=short, exclusion_flag=True` — consistent. ✓.

**Mistake check 4 — summary_table downstream.** `scripts/segmentation.py:141` reads `n_fail = sum(1 for c in cs if c.quality_flag != "ok")`. Still works correctly for {`ok`, `short`, `long`}. ✓.

**Mistake check 5 — adjacency creep.** The patch touches the three files named in the issue body §Scope. Doc edits are all within the lines named in §Source-of-truth (schema L32 / L64–72 / L87, features.md L27 / L132 / L137). The schema §Allowed Values §quality_flag block (L64–72) is rewritten to describe the realized vocabulary; the parenthetical at L72 absorbs the historical-draft context that was previously at L72 with different wording. The features.md §"Quality-flag widening" block at L135–137 expanded from one-sentence to three-sentence to describe the deferral path; this is bounded inside the in-scope L132/L137 lines. No section outside §quality_flag was rewritten. No new feature added. No new column. ✓.

**Mistake check 6 — features.md L137 expanded text.** Pre-patch L137 was a single sentence. Post-patch it is a multi-sentence paragraph describing what the schema now lists (`ok`/`short`/`long`), what was deferred (`low_contact_gap`) with the gating constraint (segmenter inspecting contact-gap structure). The expansion is within the in-scope L132/L137 range. ✓.

**Ambiguity passed to β:**
- The boundary conventions (`<=` and `>=` in the code, `(0.5, 1.8)` open interval in the schema) are consistent but the open-interval notation might read as ambiguous to a fast reader. β may want to add the explicit boundary inclusion to the schema prose (e.g., "cycle duration in the open interval (0.5, 1.8) seconds, exclusive of both endpoints"). Out of scope for this sub if β does not push back; named here for visibility.
- `analysis/features.md` L137's "duration <= 0.5 and duration >= 1.8" is correct but uses `<=` / `>=` (Python literals) inside markdown prose, not the schema's `(0.5, 1.8)` open-interval notation. Internal consistency holds; cosmetic inconsistency between the two doc files. β may flag.

## Debt

1. **`low_contact_gap` is not produced by the segmenter today.** The label is named in `analysis/features.md` §"Quality-flag widening" L135–137 as future-segmenter debt. Adding it requires inspecting contact-gap structure (swing-time within cycle, contralateral HS hints, or force-plate data) rather than only `duration`. Gated on a downstream consumer needing the finer-grained label. **Out of scope per §Non-goals** (and per the wave manifest's "no new segmenter check beyond what's required for vocabulary alignment"). Named for follow-up.

2. **Boundary-notation cosmetic inconsistency between `feature-table-schema.md` (open-interval `(0.5, 1.8)`) and `features.md` (Python `<=` / `>=`).** Both are correct and consistent in meaning; the two doc files use different notations. A future sub could unify the notation; β may push back on this sub if they prefer it unified. Cost is one sentence in features.md or one sentence in the schema. Named in §Self-check mistake 6.

3. **`extract_shape` always-`True` placeholder.** Surfaced in cph#19's self-coherence §Debt 3 as pre-existing code debt and named explicitly as Sub D's surface in this wave (cph#25). Re-noted here only so β's serial review sees the cross-sub trace; Sub D's α (this same session, next step) lands the rename.

4. **Field-report-02 stub H1 number mismatch.** Surfaced in cph#19's self-coherence §Debt 4 (carried over from cph#18). Named as Sub C's surface in this wave (cph#24). Re-noted here for serial-review trace; Sub C's α (this session) lands the H1 fix.

## CDD-Trace

Per `cdd/alpha/SKILL.md` §2.2.

1. **Design** — direction-(a-1) chosen by wave-manifest recommendation. Single decision point ("which 3-value vocabulary can the segmenter produce from `duration` alone?" → `ok`/`short`/`long`). No separate design artifact.
2. **Coherence contract** — §Gap. Code and docs agree string-for-string on the `quality_flag` vocabulary {`ok`, `short`, `long`}; `low_contact_gap` named as deferred work with a gating constraint; no new feature; no empirical drift.
3. **Plan** — implicit. Linear: read code → read docs → pick direction → patch code → patch schema doc → patch features.md → AC oracles → self-coherence.
4. **Tests** — AC oracles pasted in §ACs (code-first grep + doc cross-check + cross-reference intersection table for AC1; direction-choice subsection for AC2; `git show --stat` for AC3; empty `git show -- README/PROJECT/CHANGELOG/ROADMAP` for AC4; code-first ordering of evidence in §AC1 for AC5).
5. **Code** — `scripts/segmentation.py` L122–124: 1-line `quality_flag=` expression replaced with a 3-line conditional emitting `short`/`long`/`ok`. No new function. No signature change. No new dependency.
6. **Docs** —
   - `analysis/feature-table-schema.md`: L32 (§Quality Control example values), L35 (§exclusion_reason parenthetical), L66 (§quality_flag header attribution), L68–70 (§quality_flag bullets), L72 (§quality_flag historical-draft parenthetical).
   - `analysis/features.md`: L27 (§Required indexing quality_flag line), L132 (§Indexing widening exclusion_reason example), L137 (§Quality-flag widening expanded explanation).
7. **Self-coherence** — this file.

**Step-by-step ledger:**

| # | Step | Evidence |
|---|---|---|
| 1 | Read wave manifest | `Read .cdd/waves/coherence-drift-sweep-followup-2026-05-18/manifest.md` |
| 2 | Read precedent self-coherence | `Read .cdd/unreleased/19/self-coherence.md` |
| 3 | Read sub-issue body | `mcp__github__issue_read(22)` |
| 4 | Code-first grep (pre-patch baseline) | `git show ced1425:scripts/segmentation.py` showed `"ok"`/`"out_of_range"` |
| 5 | Read schema doc | `Read analysis/feature-table-schema.md` |
| 6 | Read features.md | `Read analysis/features.md` |
| 7 | Direction choice | a-1 per §"Direction choice" |
| 8 | Edit segmentation.py L122 | `quality_flag="ok" if 0.5 < duration < 1.8 else "out_of_range"` → 3-arm conditional emitting `short`/`long`/`ok` |
| 9 | Edit feature-table-schema.md | L32, L35, L66, L68–70, L72 |
| 10 | Edit features.md | L27, L132, L137 |
| 11 | Code-first AC1 oracle | grep on segmentation.py first, then cross-check schema + features.md |
| 12 | AC3 oracle | `git show a697265 --stat` → exactly 3 files, no notebook touch |
| 13 | AC4 oracle | `git show a697265 -- README.md PROJECT.md CHANGELOG.md ROADMAP.md` empty |
| 14 | Implementation commit | `a697265 α #22: lift quality_flag literals to schema (F7 direction a-1)` |
| 15 | Self-coherence write | this file |
| 16 | Self-coherence commit | (next: `α #22: self-coherence`) |
| 17 | Push | (next) |

## Review-readiness

**Round:** 1.
**Base SHA for this sub:** `8981e96` (δ wave-open commit).
**Implementation SHA:** `a697265`.
**Branch CI:** N/A.
**Author email:** `alpha@cph.cdd.cnos` on `a697265`.

**Pre-review gate row-by-row:**

| # | Row | Status | Evidence |
|---|---|---|---|
| 1 | Branch rebased | ✓ | Sub A sits directly on top of wave-open `8981e96` |
| 2 | CDD Trace through step 7 | ✓ | §CDD-Trace |
| 3 | Tests present or "none apply" | ✓ | AC oracles inline (grep + git-show + cross-reference table) |
| 4 | Every AC has evidence | ✓ | AC1 (code-first grep + doc cross-check + intersection table); AC2 (§"Direction choice"); AC3 (`git show --stat`); AC4 (empty `git show -- README/PROJECT/CHANGELOG/ROADMAP`); AC5 (code-first ordering of evidence in §AC1) |
| 5 | Known debt explicit | ✓ | §Debt 1–4 |
| 6 | Schema/shape audit | ✓ | The patch is itself a code↔schema vocabulary audit; cross-reference intersection table is the audit artifact |
| 7 | Peer enumeration when closure touches a family | ✓ | All five surfaces (segmentation.py, schema doc §Quality Control, schema doc §quality_flag, schema doc example row, features.md L27/L132/L137) enumerated and checked |
| 8 | Harness audit | N/A | no harness change |
| 9 | Post-patch re-audit | N/A | single-pass round 1 |
| 10 | Branch CI green | N/A | no CI |
| 11 | Artifact enumeration matches diff | ✓ | `git show a697265 --stat` returns the 3 files named in §CDD-Trace step 6 |
| 12 | Caller-path trace for new modules | N/A | no new modules |
| 13 | Test assertion count | N/A | grep oracles inline |
| 14 | α commit author canonical | ✓ | `a697265` author = `alpha@cph.cdd.cnos` |

**Verdict:** ready for β review (round 1). β's load-bearing task is AC5 — independently re-grep `scripts/segmentation.py` for `quality_flag` literals before reading the schema doc, and record that grep output as the first AC1 oracle in `beta-review.md`. This is the F7-class anchoring discipline the wave inherits from cph#21 §"Review mode".
