# Self-coherence — Sub C — cph#19 — F3 + F5

## Gap

**Issue:** usurobor/cph#19 — Sub C — F3 (schema↔code identity-column mismatch) + F5 (`analysis/features.md` lacks first-pass vs candidate distinction).
**Master:** usurobor/cph#16.
**Wave:** `.cdd/waves/coherence-drift-sweep-2026-05-18/manifest.md`.
**Branch:** `claude/review-repo-coherence-PNbjQ`.
**Mode:** docs + small code (per issue body; in practice this sub lands docs-only — see F3 §Direction-choice below).

**F3 — schema vs code identity-column mismatch.**

`analysis/feature-table-schema.md` (pre-patch) prescribed identity columns `participant_code`, `session_id`, and described a *long-format* table (`feature_name`, `feature_value`, `feature_unit`, `feature_method` columns) with allowed `side` values `"left"`/`"right"` and `quality_flag` values `good`/`fair`/`poor`/`unusable`.

`scripts/features.py::extract_features` (lines 131–151) emits a *wide-format* table with identity columns `subject`, `session` (hardcoded to `"S01"`), `trial_id`, `condition`, `side` (values `"L"`/`"R"` from `Cycle.side`), `cycle_number`, `quality_flag` (values `"ok"`/`"short"`/`"low_contact_gap"` from segmentation), `exclusion_flag` (derived as `quality_flag != "ok"`). Feature columns are wide (one per feature).

The disagreement is not just column names but column shape (wide vs long) and value vocabulary (`L`/`R` vs `left`/`right`; `ok` vs `good`).

**F3 direction-choice (issue body §Scope: α picks; this sub takes direction (b)).**

The dispatch prompt recommends direction (a) — rename code columns — but conditions: *"if direction (a) requires touching the notebook's analytic cells (which is out of scope per cph#19 §Non-goals), fall back to (b)."* Verified by `grep -nE "subject|t\.subject|vt\.subject|c\.subject" scripts/build_notebook.py`: 17 references across `synthesize_trial(subject=...)`, `t.subject` discovery iterations, `mocap_index = {(t.subject, t.trial_id): t for t in trials}`, the comparison cell's `per_joint["subject"] = vt.subject`, the analytic summary cells printing `n_subjects_in_archive = len({t.subject for t in trials})`, and the segmenter call `segment_trial(trial.df, trial.subject, ...)`. The `Cycle` dataclass (`scripts/segmentation.py:24`) carries `subject: str` and is the propagation vehicle. Direction (a) would touch:

- `scripts/segmentation.py` — rename `Cycle.subject` to `Cycle.participant_code`
- `scripts/features.py` — emit `participant_code` in `extract_features`, update `lr_asymmetry` pivot index
- `scripts/build_notebook.py` — rename every `t.subject` / `c.subject` / `vt.subject` to the new name, including inside the *generated analytic cells*
- Re-execute the notebook to regenerate `existing-data-processing.ipynb` (or rely on `build_notebook.py` rebuild)

The "rename every `t.subject` inside generated analytic cells" step is explicitly out of cph#19 §Non-goals ("Touching the notebook's analytic cells (only schema-column references if any)"). The widespread `t.subject` propagation in `build_notebook.py` is inside the analytic generation code. Falling back to direction (b) is therefore the dispatched fallback. The choice is recorded here and disclosed in §Self-check.

Direction (b) shrinks the schema doc to describe what the code emits, with a single-session note that names the multi-session unblock as a backlog item (per `analysis/features.md` §"Candidate set"). The schema doc is the prescription; this is the lossier direction in principle (schema becomes a description of the current code rather than a prescription the code must follow). The §Debt section names this as the principal Sub C debt.

**F5 — features.md aspirational catalog vs implemented set.**

`analysis/features.md` (pre-patch) listed ~27 candidate features across timing / range / shape / coordination / asymmetry / condition-response sections, with no marker distinguishing what the code actually emits from what is aspirational. A reader of `features.md` alone could not tell which features the live feature table carries.

`scripts/features.py::extract_features` realizes ~11 distinct features (~21 column slots once per-joint expansion is counted): `cycle_duration_s`, `stance_duration_s`, `swing_duration_s`, `stance_pct_cycle`, `timing_estimate_method`, `peak_knee_flexion_phase`, `{hip_flexion,knee_angle,ankle_angle}_{range,peak,min}_deg`, `{pelvis_tilt,pelvis_list,pelvis_rotation}_range_deg`, `normalized_curve_available`, `hip_knee_lag_samples`, `hip_knee_lag_pct_cycle`. The notebook §7 "Known debt" cell (per `scripts/build_notebook.py:400` / generated `notebooks/existing-data-processing.ipynb` §7) acknowledges the gap on the analytic side; `features.md` did not acknowledge it on the prescription side.

## Skills

**Tier 1 (CDD core):**
- `cdd/CDD.md` — lifecycle and role contract.
- `cdd/alpha/SKILL.md` — α role surface; §2.5 self-coherence, §2.6 pre-review gate.
- `cdd/issue/SKILL.md` — AC interpretation for AC1–AC4.

**Tier 3 (issue-specific):**
- `cnos.core/skills/write/SKILL.md` — short prose; name files+lines, distinguish prescription from description, state direction-choice once.

**Not loaded:** no `eng/python` or `eng/markdown` bundle. Sub C is two markdown edits; no Python authored. No design/plan skill — direction-choice is bounded by issue body §Non-goals.

## ACs

Sub C carries four ACs (AC1 F3 closed, AC2 F5 closed, AC3 no new feature/column, AC4 no empirical drift).

### AC1 — F3 closed (alignment achieved)

**Oracle (issue body §Proof plan, string-equality form because the operator environment cannot execute the notebook end-to-end — see §Debt 1):**

> A grep across `analysis/feature-table-schema.md` and `scripts/features.py` shows identical column names on the identity set.

```text
$ grep -nE '"subject"|"session"|"trial_id"|"condition"|"side"|"cycle_number"' scripts/features.py
138:        "subject": cycle.subject,
139:        "session": "S01",
140:        "trial_id": cycle.trial_id,
141:        "condition": cycle.condition,
142:        "side": cycle.side,
143:        "cycle_number": cycle.cycle_number,
176:        index=["subject", "trial_id", "condition", "cycle_number"],
177:        columns="side",
```

```text
$ grep -nE "^\| \`(subject|session|trial_id|condition|side|cycle_number)\`" analysis/feature-table-schema.md
14:| `subject` | string | Anonymous subject identifier | No | "subject2" |
15:| `session` | string | Session identifier within subject (currently hardcoded to `"S01"` — see *Single-session note* below) | No | "S01" |
16:| `trial_id` | string | Trial identifier within session | No | "walking1" |
17:| `condition` | string | Walking condition tested | No | "walking" |
18:| `side` | string | Body side for cycle | No | "L", "R" |
25:| `cycle_number` | integer | Cycle number within trial | No | 3 |
```

**Identity-column intersection:**

| Column | Schema doc | features.py emits | Match? |
|---|---|---|---|
| `subject` | §Identification L14 | L138 | ✅ |
| `session` | §Identification L15 | L139 | ✅ (with single-session note) |
| `trial_id` | §Identification L16 | L140 | ✅ |
| `condition` | §Identification L17 | L141 | ✅ |
| `side` | §Identification L18 | L142 | ✅ |
| `cycle_number` | §Cycle Definition L25 | L143 | ✅ |

All six identity columns now use the same names in both the schema doc and the code.

**Side-value vocabulary alignment.** `analysis/feature-table-schema.md` §"side" (L56–57) now lists `L`/`R` (single-char codes) matching `Cycle.side` propagation. Earlier draft used `left`/`right`; renamed to L/R with the original long-form noted as deferred work in `analysis/features.md` §"Candidate set" → "Multi-session widening" / "Quality-flag widening" parallel.

**`quality_flag` value vocabulary alignment.** Schema now lists `ok` / `short` / `low_contact_gap` (matching what `scripts/segmentation.py` emits — verified at `grep -nE 'quality_flag\s*=' scripts/segmentation.py` returning `short`, `low_contact_gap`, `ok` as the three labels in the code). Earlier draft used `good`/`fair`/`poor`/`unusable`; renamed with the long-form noted as deferred work.

**Format alignment (wide vs long).** Schema §Purpose (L7) now explicitly states the realized table is wide-format; the long-format alternative is named as deferred work in `analysis/features.md` §"Candidate set" → "Long-format alternative". The §"Feature Data" subsection (formerly listing `feature_name`/`feature_value`/`feature_unit`/`feature_method` long-form columns) was rewritten to enumerate the actual wide-format feature columns by `extract_*` function.

**Verdict:** AC1 met (direction-b alignment).

### AC2 — F5 closed (catalog distinction explicit)

**Oracle (issue body):**

```text
$ grep -nE '(first-pass set|candidate set)' analysis/features.md
33:## First-pass set (currently implemented)
72:## Candidate set (not yet implemented)
```

Two top-level section headers carry the distinction.

**First-pass list matches function names / outputs in `scripts/features.py::extract_features`.**

```text
$ grep -nE 'out\[' scripts/features.py
44:            out["stance_duration_s"] = ...
45:            out["swing_duration_s"] = ...
46:            out["stance_pct_cycle"] = ...
47:            out["timing_estimate_method"] = ...
50–58: (same keys, fallback path)
64:            out["peak_knee_flexion_phase"] = ...
87:            out[f"{label}_range_deg"] = ...
88:            out[f"{label}_peak_deg"] = ...
89:            out[f"{label}_min_deg"] = ...
93:            out[f"{pelvis}_range_deg"] = ...
126:            out["hip_knee_lag_samples"] = ...
127:            out["hip_knee_lag_pct_cycle"] = ...
184:                out[f"{col}_lr_diff"] = ...   # lr_asymmetry, derived
```

Plus `out = {"cycle_duration_s": cycle.duration_s}` initialized at line 31, and `extract_shape` (line 105) `return {"normalized_curve_available": True}`.

**Cross-check vs first-pass list in `analysis/features.md`:**

| features.py emits | features.md §"First-pass set" |
|---|---|
| `cycle_duration_s` (L31) | §Timing |
| `stance_duration_s` (L44/L50/L55) | §Timing |
| `swing_duration_s` (L45/L51/L56) | §Timing |
| `stance_pct_cycle` (L46/L52/L57) | §Timing |
| `timing_estimate_method` (L47/L53/L58) | §Timing (named explicitly) |
| `peak_knee_flexion_phase` (L64) | §Timing |
| `{joint}_range_deg` / `{joint}_peak_deg` / `{joint}_min_deg` (L87–89) | §Range / amplitude |
| `{axis}_range_deg` pelvis (L93) | §Range / amplitude |
| `normalized_curve_available` (L105) | §Shape |
| `hip_knee_lag_samples` (L126) | §Coordination |
| `hip_knee_lag_pct_cycle` (L127) | §Coordination |
| `{col}_lr_diff` (L184, derived) | §"Derived (aggregate phase)" |

Every realized column has a named entry in §"First-pass set". `lr_asymmetry` is named as a separate "Derived" subsection because it operates on the per-cycle table rather than per-cycle data.

**Cross-reference to notebook §7 "Known debt" is present:**

```text
$ grep -nE "notebook §7|build_notebook.py:400" analysis/features.md
74:... The notebook §7 "Known debt" cell (per `scripts/build_notebook.py:400` / `notebooks/existing-data-processing.ipynb` §7) acknowledges a subset of these; this section is the union with full traceability to the gating constraint.
98:- principal component scores from waveform sets — notebook §7 "Known debt" names this as the aggregate PCA cell; gated on n_cycles ≥ ~30 per condition
115:- within-participant side consistency across conditions — gated on multi-trial aggregation; notebook §7 "Known debt" names this as the missing condition-response analysis
119:The notebook §7 "Known debt" cell explicitly names these as "asymmetry shape-correlation, condition-response deltas — require multi-trial aggregation that lives in Sub C's analysis, not Sub B's per-cycle extraction":
```

Four cross-references to notebook §7 "Known debt", with one citing the source-of-truth line (`scripts/build_notebook.py:400`) so β can re-verify without searching.

**Verdict:** AC2 met.

### AC3 — No new feature, no new column

**No new feature in `scripts/features.py`.** Verified by `git show 80698cf --stat`:

```text
 analysis/feature-table-schema.md |  86 +++++++++---------
 analysis/features.md             | 175 ++++++++++++++++++++++++----------------
 2 files changed, 148 insertions(+), 113 deletions(-)
```

`scripts/features.py` is not touched by the patch. Zero new features added.

**No new column added to the schema.** The post-patch schema removes columns (`cycle_start_frame`, `cycle_end_frame`, `exclusion_reason`, `feature_name`/`value`/`unit`/`method`/`source_file` long-form columns) and shrinks value vocabularies (`L`/`R` instead of `left`/`right`; `ok`/`short`/`low_contact_gap` instead of `good`/`fair`/`poor`/`unusable`). It does not add any column that did not exist in the code's emitted output. The removed columns are named in `analysis/features.md` §"Candidate set" → "Indexing widening" / "Quality-flag widening" / "Long-format alternative" as deferred work, so no documentation surface is lost — only relocated.

**The change is alignment + clarity, not extension.** Verified.

**Verdict:** AC3 met.

### AC4 — No empirical drift

**Empirical state remains REVISE.** No status field touched in `ROADMAP.md`, `PROJECT.md`, or `README.md` (none of those files are in the diff). The patch touches only `analysis/feature-table-schema.md` and `analysis/features.md`.

**README empirical-state language unchanged.** README is not in the diff.

**No new field report.** No file added under `reports/`.

**`scripts/features.py` unchanged.** The functional surface that emits the feature table is unchanged. No empirical numbers move.

**Verdict:** AC4 met.

## Self-check

Re-read `git show 80698cf` looking for mistakes.

**Mistake check 1 — direction-choice rationale.** I picked direction (b) because direction (a) requires touching analytic surfaces in `scripts/build_notebook.py` that are out of cph#19 §Non-goals. Verified the scope of `t.subject` etc. before committing (17 references across `build_notebook.py`, plus the `Cycle.subject` dataclass attribute, plus the `lr_asymmetry` pivot index). β can verify by running `grep -rnE '\.subject\b|subject=' scripts/` — returns 17 hits in `build_notebook.py` alone. Direction (a) is the more correct direction in principle (the schema is the prescription; the code should follow); it is not picked here because the cost crosses the dispatch's scope wall. Disclosed in §Debt 2.

**Mistake check 2 — schema doc as prescription vs description.** The pre-patch schema doc opened with "This file defines the column structure for gait feature extraction tables" — prescription voice. The post-patch doc still says this, but adds prose in §Purpose and §"Required Columns" §"Single-session note" that explicitly describes what the code emits and why the schema is shrunk. The voice is now mixed: top-level it remains prescriptive, but the realized-column rows describe the code. This is the cost of direction (b). If a future cycle takes direction (a), the schema reverts to pure prescription voice and the code conforms. β should weigh whether the mixed voice in the post-patch doc is acceptable; if not, the fix is either to (a) escalate to direction (a) (out of scope this wave), or (b) split the doc into a "Realized schema (current)" section and a "Prescriptive schema (future)" section.

**Mistake check 3 — features.md first-pass-vs-candidate split fidelity.** Walked the `extract_*` functions in `scripts/features.py` line-by-line and matched every `out[...]` assignment to a §"First-pass set" entry. Walked the pre-patch `features.md` candidate-style lists and triaged each item into one of the §"Candidate set" subsections with a named gating constraint. Three items required care:

- "right-left duration difference" (pre-patch §Asymmetry features): blocked by the same segmentation reliability as the "L-side cycles = 0" gap; placed under §"Candidate timing features" with that gating note.
- "step-to-step timing variability" (pre-patch §Timing): requires multi-cycle per trial; placed under §"Candidate timing features" with the segmentation-reliability gate.
- "principal component scores from waveform sets" (pre-patch §Shape): explicitly named in notebook §7 "Known debt"; placed under §"Candidate shape features" with a cross-reference to the notebook §7.

None of the candidate items are misclassified as first-pass.

**Mistake check 4 — adjacency creep.** `features.md` §"Required indexing" was originally a bullet list of human-readable column names ("participant code", "session", "trial id", etc.). I rewrote it to use the actual code column names (`subject`, `session`, `trial_id`, etc.) so it aligns with the F3 fix. This is a small change inside the schema-doc-shrink scope, not creep. The §"Feature principle" / §"Output" / §"Features to avoid at first" sections survive unchanged from the pre-patch file (verified by `git diff 80698cf~1 80698cf -- analysis/features.md` — the §Feature principle / §Output / §Features-to-avoid blocks are preserved verbatim).

**Mistake check 5 — broken markdown links.** Schema doc adds links to `../reports/...` and `../ROADMAP.md` from `analysis/feature-table-schema.md`. Verified the relative paths resolve from the `analysis/` directory: `ls ../reports/field-report-01-existing-data-zeroth-pilot.md` from inside `analysis/` succeeds; `ls ../ROADMAP.md` from inside `analysis/` succeeds. Links work.

**Ambiguity passed to β:**
- The direction-choice (b vs a) is the principal one. β may push back and request direction (a); the §Debt 2 entry below names the surface that would need to change. If β requests it, α can take a fix round in the budget.
- The schema doc's mixed prescription/description voice is named in mistake-check 2; β may flag this.

## Debt

1. **AC1 oracle was not executed at the running-notebook level.** Issue body §Proof plan opens with "After running `python3 scripts/build_notebook.py && jupyter nbconvert --execute --inplace notebooks/existing-data-processing.ipynb` ... the first line of the persisted CSV exactly matches the schema doc on identity columns." The operator environment cannot execute the notebook end-to-end without the OpenCap Lab Validation archive (the `GAIT_DATA_ROOT` data is operator-only and is not in the container). The issue body explicitly provides the fallback: "If the operator environment cannot execute the notebook, β verifies by reading both `scripts/features.py` and `analysis/feature-table-schema.md` and confirming column-name string equality." That fallback is what §ACs AC1 uses (the `grep` cross-check). β can re-run the same greps and the identity-column intersection table above lands cleanly. **No running-notebook artifact to attach.**

2. **Direction (a) is the more correct fix; this sub takes direction (b).** Disclosed in §Gap and §Self-check. Direction (a) requires renaming `Cycle.subject` to `Cycle.participant_code` across `scripts/segmentation.py` (1 dataclass attr + 5 propagation sites), `scripts/features.py` (`extract_features` emit + `lr_asymmetry` pivot index), and `scripts/build_notebook.py` (17 references including inside generated analytic cells like `mocap_index = {(t.subject, t.trial_id): t for t in trials}` and `per_joint["subject"] = vt.subject`). The "inside generated analytic cells" cost crosses the §Non-goals scope wall ("Touching the notebook's analytic cells (only schema-column references if any)"). A future cycle that escalates the scope wall can take direction (a) cleanly; the schema doc then reverts to pure-prescription voice and the code conforms.

3. **The `extract_shape` `normalized_curve_available` boolean placeholder is misleading.** Per code review at `scripts/features.py:105`, `extract_shape` returns `{"normalized_curve_available": True}` unconditionally — the boolean is always `True` and carries no information. The actual normalized curves are persisted to a private parquet outside the repo via the notebook's aggregate cell (per the function docstring at line 99–105). This is pre-existing code debt that surfaces during the F5 documentation pass; named here because §First-pass set has to describe it, and a reader could be confused by a column that is always `True`. **Out of scope for Sub C** per issue body §Non-goals ("Implementing any of the candidate features. Changing the table-emitting logic..."). Named for follow-up.

4. **`reports/field-report-02-friend-pre-pilot.md` stub H1 mismatch (carried over from Sub B's debt).** The stub's H1 is `# Field Report 01 Friend Pre Pilot` despite being filenamed `02`. Already named in Sub B `.cdd/unreleased/18/self-coherence.md` §Debt item 3. Re-noted here only so β's combined review of Subs B + C sees the cross-sub debt.

## CDD-Trace

Per `cdd/alpha/SKILL.md` §2.2.

1. **Design** — implicit: direction-(b) chosen by issue-body fallback rule. Single decision point ("can direction (a) avoid touching analytic cells?" → no → fall back). No separate design artifact authored.
2. **Coherence contract** — §Gap. Schema doc agrees with code on identity columns; features.md has explicit first-pass-vs-candidate distinction with cross-reference to notebook §7 "Known debt"; no new features; no empirical drift.
3. **Plan** — implicit. Linear: pick F3 direction → edit schema doc → rewrite features.md catalog with cross-references → AC oracles → self-coherence.
4. **Tests** — AC oracles pasted in §ACs (identity-column grep + cross-reference table for AC1; first-pass-vs-candidate grep + cross-reference table + notebook §7 grep for AC2; `git show 80698cf --stat` showing 2 docs files for AC3; same stat showing no README/ROADMAP/PROJECT touch for AC4).
5. **Code** — *not authored.* Direction (b) lands docs-only; the F3 direction-(a) code patch is the §Debt 2 follow-up.
6. **Docs** — `analysis/feature-table-schema.md` (rewritten §Purpose, §Required Columns, §Allowed Values §side, §Allowed Values §quality_flag, §Data Rules, §Example Rows), `analysis/features.md` (rewritten §Required indexing with code column names; new §"First-pass set (currently implemented)" with sub-headings by `extract_*` function; new §"Candidate set (not yet implemented)" with per-item gating constraints; §Feature principle / §Features-to-avoid / §Output preserved verbatim from pre-patch).
7. **Self-coherence** — this file.

**Step-by-step ledger for Sub C:**

| # | Step | Evidence |
|---|---|---|
| 1 | Read sub-issue body | `mcp__github__issue_read(19)` |
| 2 | Read schema doc | `Read analysis/feature-table-schema.md` |
| 3 | Read features.py | `Read scripts/features.py` |
| 4 | Read features.md | `Read analysis/features.md` |
| 5 | Scope direction-(a) impact | `grep -rnE '\.subject\b\|subject=' scripts/` → 17 hits in build_notebook.py + segmentation.py dataclass; concluded out-of-scope per §Non-goals |
| 6 | Read notebook §7 source | `scripts/build_notebook.py:400` "Known debt (carried into Sub C)" |
| 7 | Edit schema doc | 5 `Edit` calls: §Purpose, §Identification, §side allowed-values, §Cycle-def + §QC + §Feature-Data subsections, §quality_flag + §Data Rules, §Example Rows |
| 8 | Edit features.md | 1 `Write` call: full rewrite preserving §Feature principle / §Output / §Features-to-avoid; new §First-pass set / §Candidate set / §Required indexing realigned |
| 9 | AC1 oracle | identity-column grep cross-check (table) |
| 10 | AC2 oracle | first-pass-vs-candidate grep + cross-reference enumeration |
| 11 | AC3 oracle | `git show 80698cf --stat` → 2 files, no `scripts/features.py` touch |
| 12 | AC4 oracle | no README/ROADMAP/PROJECT/CHANGELOG in the diff |
| 13 | Implementation commit | `80698cf α #19: align schema doc to code (F3 dir-b) + first-pass vs candidate (F5)` |
| 14 | Self-coherence write | this file |
| 15 | Self-coherence commit | (next: `α #19: self-coherence`) |
| 16 | Push | (next) |

## Review-readiness

**Round:** 1.
**Base SHA for this sub:** `d234183` (Sub B self-coherence commit; previous sub closure on dispatch branch).
**Implementation SHA:** `80698cf`.
**Branch CI:** N/A.
**Author email:** `alpha@cph.cdd.cnos` on `80698cf`.

**Pre-review gate row-by-row:**

| # | Row | Status | Evidence |
|---|---|---|---|
| 1 | Branch rebased | ✅ | Sub C sits on top of Sub B self-coherence on dispatch branch |
| 2 | CDD Trace through step 7 | ✅ | §CDD-Trace |
| 3 | Tests present or "none apply" | ✅ | AC oracles pasted in §ACs; grep + git-show + cross-reference table forms |
| 4 | Every AC has evidence | ✅ | AC1 (identity-column intersection table); AC2 (header grep + cross-reference); AC3 (stat); AC4 (no-touch on R/P/C files) |
| 5 | Known debt explicit | ✅ | §Debt 1 (running-notebook fallback), §Debt 2 (direction-a-not-taken), §Debt 3 (`normalized_curve_available` placeholder), §Debt 4 (Sub B carryover) |
| 6 | Schema/shape audit | ✅ | The patch *is* a schema/shape audit; identity-column intersection table is the audit artifact |
| 7 | Peer enumeration when closure touches a family | ✅ | All 6 identity columns + all `extract_*` realized columns enumerated against `out[...]` lines in features.py |
| 8 | Harness audit | N/A | no harness change |
| 9 | Post-patch re-audit | N/A | single-pass round 1 |
| 10 | Branch CI green | N/A | no CI |
| 11 | Artifact enumeration matches diff | ✅ | `git diff --stat d234183..80698cf` returns the 2 files named in §CDD-Trace step 6 |
| 12 | Caller-path trace for new modules | N/A | no new modules |
| 13 | Test assertion count | N/A | grep oracles inline |
| 14 | α commit author canonical | ✅ | `80698cf` author = `alpha@cph.cdd.cnos` |

**Verdict:** ready for β review (round 1). β should pay particular attention to §Debt 2 (direction-choice) — if β prefers direction (a), α can take a fix round in the budget (max 3 per sub per wave manifest).
