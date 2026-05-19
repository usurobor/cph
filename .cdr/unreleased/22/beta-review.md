# β review — Sub A — cph#22 — F7 quality_flag schema↔code vocabulary alignment

## Round 1

**Verdict:** APPROVE

**Round:** 1
**Wave:** `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/`
**Master:** usurobor/cph#21
**Sub:** usurobor/cph#22
**Base SHA (wave-open):** `8981e96` (δ wave-open commit)
**Implementation SHA:** `a697265`
**Self-coherence SHA:** `3bc4242`
**Branch CI state:** N/A (no `.github/workflows/`)
**Branching:** single-branch dispatch on `claude/review-repo-coherence-PNbjQ` per wave manifest §"Branching deviation"

## Identity-audit

| Commit | Expected author | Observed | Pass |
|---|---|---|---|
| `a697265` (impl) | `α-as-agent <alpha@cph.cdd.cnos>` | `α-as-agent <alpha@cph.cdd.cnos>` | ✓ |
| `3bc4242` (self-coherence) | `α-as-agent <alpha@cph.cdd.cnos>` | `α-as-agent <alpha@cph.cdd.cnos>` | ✓ |
| this review commit | `β-as-agent <beta@cph.cdd.cnos>` | will be authored as `β-as-agent <beta@cph.cdd.cnos>` | ✓ (pre-commit) |

Identity-isolation invariant (α ≠ β within Sub A) preserved by Agent-session boundary (separate Agent invocations for α and β).

## AC-by-AC

### AC1 — code and schema agree on `quality_flag` literals (string-equality)

**Code-side oracle (re-run β-independently, FIRST, per wave manifest §"β anchoring discipline"):**

β re-greps `scripts/segmentation.py` for all `quality_flag` references — the dispatcher-prompt regex `quality_flag\s*=\s*"` does NOT match L122 (the `=` is followed by `(` and a newline before the first literal `"short"`), so β widened to the bare token to be sure no emission is missed:

```text
$ grep -nE 'quality_flag' scripts/segmentation.py
35:    quality_flag: str = "ok"
122:                quality_flag=("short" if duration <= 0.5
141:        n_fail = sum(1 for c in cs if c.quality_flag != "ok")
```

Direct read of the multi-line conditional at L122–124 (β-side, code-of-truth):

```text
$ sed -n '122,125p' scripts/segmentation.py
                quality_flag=("short" if duration <= 0.5
                              else "long" if duration >= 1.8
                              else "ok"),
            ))
```

L35 dataclass default = `"ok"`. L122–124 segment_trial constructor emits exactly three literals via the chained ternary: `"short"` (when `duration <= 0.5`), `"long"` (when `duration >= 1.8`), `"ok"` (otherwise). L141 is a non-emitting comparison (`!= "ok"`) which does not introduce a new literal into the vocabulary.

**Code-emitted set (β-side, independent of α's reported set):** {`"ok"`, `"short"`, `"long"`}.

**Doc-side cross-check (SECOND, per anchoring rule; verify each surface matches the code-emitted set):**

```text
$ grep -nE '"(ok|short|long|low_contact_gap|out_of_range)"' analysis/feature-table-schema.md analysis/features.md
analysis/features.md:28:- exclusion flag (column `exclusion_flag`; derived as `quality_flag != "ok"`)
analysis/feature-table-schema.md:32:| `quality_flag` | string | Data quality assessment | No | "ok", "short", "long" |
analysis/feature-table-schema.md:33:| `exclusion_flag` | boolean | Should cycle be excluded from analysis (derived: `quality_flag != "ok"`) | No | True, False |
analysis/feature-table-schema.md:35:(`exclusion_reason` is not currently emitted as a separate column; the reason is implicit in `quality_flag` ("short", "long"). Materializing it as a dedicated string column is named in `analysis/features.md` §"Candidate set" → indexing widening.)
analysis/feature-table-schema.md:78:3. **Quality gates**: `exclusion_flag` is derived as `quality_flag != "ok"` by `scripts/features.py::extract_features`. No row should carry `quality_flag="ok"` with `exclusion_flag=True` (the derivation makes this impossible by construction).
```

The §"Allowed Values" §quality_flag block (L64–72) and the §Example Rows block (L83–87) use backtick-quoted literals (not double-quoted), so they do not match the regex. β read them directly:

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

```text
$ sed -n '27p;132p;137p' analysis/features.md
27:- quality flag (column `quality_flag`; values `ok`/`short`/`long` per `analysis/feature-table-schema.md` §"quality_flag")
132:- `exclusion_reason` — currently implicit in `quality_flag` values (`short`, `long`); materializing as a dedicated string column is a small ergonomic improvement
137:The schema doc originally listed `good` / `fair` / `poor` / `unusable`; an interim draft listed `ok` / `short` / `low_contact_gap`. The code emits `ok` / `short` / `long`, where `short` and `long` are derived from cycle duration alone (`duration <= 0.5` and `duration >= 1.8` respectively, in `scripts/segmentation.py::segment_trial`). ...
```

**β-side cross-reference intersection table (independent enumeration):**

| Surface | Realized values | Matches code-emitted set {`ok`,`short`,`long`}? |
|---|---|---|
| `scripts/segmentation.py:122–124` (code-of-truth, β-anchored) | `short`, `long`, `ok` | (reference) |
| `scripts/segmentation.py:35` (dataclass default) | `ok` | ✓ subset of code-emitted set |
| `analysis/feature-table-schema.md:32` §Quality Control "Example" cell | `"ok"`, `"short"`, `"long"` | ✓ exact match |
| `analysis/feature-table-schema.md:35` parenthetical | `"short"`, `"long"` | ✓ subset (cites the two exclusion-implying values) |
| `analysis/feature-table-schema.md:68–70` §quality_flag bullets | `ok`, `short`, `long` | ✓ exact match |
| `analysis/feature-table-schema.md:72` historical-draft parenthetical | names `good`/`fair`/`poor`/`unusable` + `low_contact_gap` as NOT realized | ✓ (negative claim, no false realization) |
| `analysis/feature-table-schema.md:87` example CSV row | `short` | ✓ value the code actually emits (`duration <= 0.5` → `short`) |
| `analysis/features.md:27` §Required indexing | `ok`/`short`/`long` | ✓ exact match |
| `analysis/features.md:132` §Indexing widening | `short`, `long` | ✓ subset (cites the two exclusion-implying values) |
| `analysis/features.md:137` §Quality-flag widening | code-emitted `ok`/`short`/`long` named; historical `low_contact_gap` named as deferred | ✓ exact match + named deferral |

All five canonical doc surfaces (schema L32, schema L64–72, schema L87, features.md L27, features.md L132/L137) agree string-for-string with the code-emitted set {`ok`, `short`, `long`}. The `low_contact_gap` literal appears only in historical-draft parentheticals (schema L72) and the deferred-work explanation (features.md L137), both correctly named as not-realized.

**Downstream propagation sanity (β-side spot check, not strictly an AC1 oracle but adjacent):**

```text
$ grep -n 'quality_flag' scripts/features.py
144:        "quality_flag": cycle.quality_flag,
145:        "exclusion_flag": cycle.quality_flag != "ok",
```

`scripts/features.py` is untouched by this patch (confirmed under AC3 below). The derivation `quality_flag != "ok"` correctly yields `True` for both `"short"` and `"long"` and `False` only for `"ok"` — the schema's Data Rule 3 ("No row should carry `quality_flag='ok'` with `exclusion_flag=True`") holds by construction.

**Verdict:** AC1 met. Code-emitted set {`ok`, `short`, `long`} agrees string-for-string with every canonical doc surface. β anchored on `scripts/segmentation.py` FIRST, then verified docs match.

### AC2 — direction recorded

α's `self-coherence.md` §"Direction choice" (L43–46) names direction **a-1**: "Emit `\"short\"` for `duration <= 0.5`, `\"long\"` for `duration >= 1.8`, `\"ok\"` otherwise. The schema doc lists exactly those three labels; `\"low_contact_gap\"` is named in `analysis/features.md` §\"Quality-flag widening\" as future-segmenter debt (gated on adding contact-gap inspection to the segmenter)."

Rationale named (L46): "Direction (a-1) is the cleanest 3-value vocabulary the segmenter can produce today using only `duration`. It distinguishes which threshold fired (short cycle vs long cycle), which is information the segmenter has but `\"out_of_range\"` discarded."

The dropped/deferred `low_contact_gap` is named as cross-sub debt with its gating constraint at `analysis/features.md:137` and in α's §Debt 1. The added literal `"long"` (relative to pre-patch schema's `low_contact_gap`) is named: it's the 3rd label the segmenter can produce from `duration` alone.

**Verdict:** AC2 met.

### AC3 — no other surfaces touched without naming them

**Oracle (β-re-run):**

```text
$ git show a697265 --stat
commit a697265253b8b7c0086e46dc30ddf7319621db57
Author: α-as-agent <alpha@cph.cdd.cnos>
Date:   Tue May 19 02:45:35 2026 +0000

    α #22: lift quality_flag literals to schema (F7 direction a-1)

 analysis/feature-table-schema.md | 14 +++++++-------
 analysis/features.md             |  6 +++---
 scripts/segmentation.py          |  4 +++-
 3 files changed, 13 insertions(+), 11 deletions(-)
```

Exactly the three expected surfaces: `scripts/segmentation.py` (code), `analysis/feature-table-schema.md` (schema), `analysis/features.md` (catalog). No notebook regeneration. No `scripts/features.py` touch. No `.cdd/**` touch in impl commit. No other file in the diff.

**Verdict:** AC3 met.

### AC4 — no empirical drift

**Oracle (β-re-run):**

```text
$ git show a697265 -- README.md PROJECT.md CHANGELOG.md ROADMAP.md
(empty)
```

No charter / roadmap / changelog / project-doc surface touched.

**REVISE posture check (PROJECT.md L20 at HEAD, per field-report-01 invariant):**

```text
$ grep -n 'REVISE' PROJECT.md
20:**REVISE** (2026-05-17 real-data run, per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md)). The Coherence Path Hypothesis is not validated; it is also not refuted. ...
42:[`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) — 2026-05-17 real-data run ...
```

REVISE posture intact. No new field report added (no new file under `reports/` from `git diff --diff-filter=A`).

**Verdict:** AC4 met.

### AC5 — β anchors on code first

This AC names β's process discipline. β honors it as follows:

1. The §AC1 verification above begins with the **code-side** oracle (`grep` + direct read of `scripts/segmentation.py:35,122–125,141`), explicitly anchored on the code-of-truth before any doc was opened.
2. Only after the code-emitted set {`ok`, `short`, `long`} was independently enumerated did β open the doc surfaces (schema L32/L64–72/L87 + features.md L27/L132/L137) and verify each doc matches what the code emits.
3. β re-ran the greps independently rather than trusting α's reported output. β found the dispatcher-prompt regex `quality_flag\s*=\s*"` does NOT match L122 (the multi-line conditional puts the `=` adjacent to `(`, not adjacent to the literal); β widened to `quality_flag` to confirm no emission is missed. α's self-coherence reports the same hit set, so the regex-mismatch is a documentation artifact, not a missed emission — but β flagging it independently is exactly the F7-class behavior the wave's anchoring discipline is meant to produce.

**Verdict:** AC5 met on β's side. The structural fix the wave inherits from cph#21 §"Review mode" held.

## Notes

**N1 (regex-vs-multi-line-conditional, oracle robustness).** The dispatcher-prompt and issue-body AC1 oracle `grep -nE 'quality_flag\s*=\s*"' scripts/segmentation.py` does not match the L122–124 multi-line conditional in α's post-patch code (the `=` is followed by `(` and a newline before `"short"`). α reported only the L35 dataclass-default match plus the L122 partial line; β confirms. The substantive AC1 claim (code-emitted set matches docs) is met regardless — β widened to the bare token `quality_flag` to enumerate emissions — but a future-wave oracle phrasing would benefit from a regex that survives multi-line conditionals (e.g., `quality_flag\s*=` or a `rg` multi-line search). Not a finding; named for re-runner clarity and for ε's `cdd-iteration.md` if useful.

**N2 (boundary-notation cosmetic inconsistency).** α's self-coherence §Self-check mistake 6 + §Debt 2 names that `feature-table-schema.md:68` uses open-interval `(0.5, 1.8)` notation while `analysis/features.md:137` uses Python `<=` / `>=` notation. Both correct, both internally consistent (open interval is exclusive of endpoints; the code uses `<=` and `>=` so the endpoints map to short/long, not to ok — matching the open-interval reading). β concurs: cosmetic-only, not a finding. Named for ε.

**N3 (boundary inclusion at `duration == 0.5` and `duration == 1.8`).** α's chained ternary at L122–124 evaluates `"short" if duration <= 0.5 else ("long" if duration >= 1.8 else "ok")`. At `duration == 0.5` → `"short"` (the first arm). At `duration == 1.8` → `"long"` (the second arm, because the first arm's `<=` is false for `1.8`). At `duration == 1.0` → `"ok"`. This is consistent with the schema's L68 "in `(0.5, 1.8)` seconds" (open interval, exclusive of both endpoints) — the endpoints themselves are NOT in the ok set, matching code. ✓.

**N4 (downstream sanity, `summary_table`).** `scripts/segmentation.py:141` reads `n_fail = sum(1 for c in cs if c.quality_flag != "ok")`. For new vocabulary {`ok`, `short`, `long`}: this still counts both `"short"` and `"long"` cycles as failures. Behavior unchanged in spirit (failure := not ok). ✓.

**N5 (features.py untouched).** `scripts/features.py:144–145` reads `"quality_flag": cycle.quality_flag, "exclusion_flag": cycle.quality_flag != "ok"`. The propagation is structural (passes through whatever literal `Cycle.quality_flag` carries) and the derivation uses `!= "ok"` which is correct for any non-`"ok"` literal. No `scripts/features.py` patch needed.

## Scope-drift check

| Surface | Expected per wave manifest §"Issues" + cph#22 §Scope | Touched in diff? |
|---|---|---|
| `scripts/segmentation.py:116–123` (Cycle constructor quality_flag) | yes | yes (L122–124, 4 lines net) |
| `scripts/segmentation.py:35` (dataclass default) | possibly | no (default `"ok"` still in code-emitted set; no change needed) |
| `analysis/feature-table-schema.md` L32 / L64–72 / L87 (§Quality Control + §quality_flag + example row) | yes | yes (L32, L35, L66–72, L87) |
| `analysis/features.md` L27 / L132 / L137 | yes | yes (L27, L132, L137) |
| `scripts/features.py` | no (downstream propagation works unchanged) | no |
| `notebooks/existing-data-processing.ipynb` | no (§Non-goals: "Re-executing the notebook") | no |
| `Cycle.subject` → `participant_code` (cph#19 deferred dir-a) | no | no |
| `extract_shape` rename (Sub D's surface) | no | no |
| README / PROJECT / CHANGELOG / ROADMAP / `reports/*` | no | no |
| `.cdd/**` historical artifacts | no | no |

No scope-drift. α stayed inside Sub A's surface exactly. The three-file impl-diff matches the wave manifest §"File-disjointness check" §Sub A line-range prediction.

## Cross-sub debt (for δ wave-closeout)

1. **`low_contact_gap` is not produced by the segmenter today.** Named in `analysis/features.md` §"Quality-flag widening" L137 as future-segmenter debt with gating constraint (segmenter must inspect contact-gap structure — swing-time within cycle, contralateral HS hints, or force-plate data — rather than only `duration`). Gated on a downstream consumer needing finer-grained quality labels. α §Debt 1; β concurs.

2. **Boundary-notation cosmetic inconsistency between schema and features.md.** `feature-table-schema.md:68` uses open-interval `(0.5, 1.8)`; `analysis/features.md:137` uses Python `<=` / `>=`. Both correct, both internally consistent. A future micro-cycle could unify the notation (one sentence in either file). Cost: trivial. α §Self-check mistake 6 + §Debt 2; β concurs.

3. **Regex-oracle phrasing brittleness.** The AC1 oracle `quality_flag\s*=\s*"` from the issue body does not match the post-patch multi-line conditional at `scripts/segmentation.py:122–124`. The substantive AC1 claim is met regardless under a widened grep; this is a phrasing fragility worth fixing in future issue templates (use `quality_flag\s*=` or a multi-line `rg` search). Named for ε's `cdd-iteration.md` consideration as part of the β-anchoring SKILL patch the wave manifest §"β anchoring discipline" already proposes.

4. **Carry-over: `extract_shape` always-`True` placeholder** (this wave's Sub D / cph#25; α §Debt 3 re-notes the cross-sub trace). β will verify in Sub D.

5. **Carry-over: field-report-02 stub H1 number mismatch** (this wave's Sub C / cph#24; α §Debt 4 re-notes). β will verify in Sub C.

## Round 1 close

AC1 (code-first oracle anchored on `scripts/segmentation.py`, code-emitted set {`ok`,`short`,`long`} verified to agree string-for-string with all five doc surfaces), AC2 (direction a-1 named in α §"Direction choice"; `low_contact_gap` deferral named with gating constraint), AC3 (exactly three expected files in `git show --stat`), AC4 (zero touches to README/PROJECT/CHANGELOG/ROADMAP; REVISE posture intact), AC5 (β re-greps `scripts/segmentation.py` FIRST, doc cross-check SECOND; F7-class anchoring discipline held) all met under independent β re-run. No scope-drift. No identity-isolation breach. Sub A APPROVE.
