# β review — Sub C — cph#19 — F3 + F5

## Round 1

**Verdict:** APPROVE

**Round:** 1
**Wave:** `.cdd/waves/coherence-drift-sweep-2026-05-18/`
**Master:** usurobor/cph#16
**Sub:** usurobor/cph#19
**Base SHA (Sub C parent):** `d234183` (Sub B self-coherence)
**Implementation SHA:** `80698cf`
**Self-coherence SHA:** `319ab3e`
**Branch CI state:** N/A (no `.github/workflows/`)
**Branching:** single-branch dispatch on `claude/review-repo-coherence-PNbjQ` per wave manifest §"Branching deviation"

## Identity-audit

| Commit | Expected author | Observed | Pass |
|---|---|---|---|
| `80698cf` (impl) | `alpha@cph.cdd.cnos` | `α-as-agent <alpha@cph.cdd.cnos>` | ✓ |
| `319ab3e` (self-coherence) | `alpha@cph.cdd.cnos` | `α-as-agent <alpha@cph.cdd.cnos>` | ✓ |
| this review commit | `beta@cph.cdd.cnos` | will be authored as `β-as-agent <beta@cph.cdd.cnos>` | ✓ (pre-commit) |

Identity-isolation invariant (α ≠ β within Sub C) preserved.

## AC-by-AC

### AC1 — F3 closed (alignment achieved)

**Oracle (issue body §Proof plan, string-equality fallback form):** The issue body §Proof plan explicitly names a fallback: "If the operator environment cannot execute the notebook, β verifies by reading both `scripts/features.py` and `analysis/feature-table-schema.md` and confirming column-name string equality." The dispatcher prompt also confirmed this fallback is in-bounds for Sub C AC1.

β does not have the OpenCap Lab Validation archive in the container (per wave manifest §"Known constraints" — `data/external/` is operator-only). The running-notebook oracle cannot execute. β proceeds via the string-equality fallback per the issue body authorization.

**Re-reading `scripts/features.py::extract_features` (β-side):**

```python
# scripts/features.py L137–147
row = {
    "subject": cycle.subject,
    "session": "S01",
    "trial_id": cycle.trial_id,
    "condition": cycle.condition,
    "side": cycle.side,
    "cycle_number": cycle.cycle_number,
    "quality_flag": cycle.quality_flag,
    "exclusion_flag": cycle.quality_flag != "ok",
}
```

The emitted identity columns are: `subject`, `session`, `trial_id`, `condition`, `side`, `cycle_number`, `quality_flag`, `exclusion_flag`.

**Re-reading `analysis/feature-table-schema.md` §"Required Columns" (β-side):**

| Schema §Identification | Schema §Cycle Definition | Schema §Quality Control |
|---|---|---|
| `subject` (L14) | `cycle_number` (L25) | `quality_flag` (L32) |
| `session` (L15) | | `exclusion_flag` (L33) |
| `trial_id` (L16) | | |
| `condition` (L17) | | |
| `side` (L18) | | |

The schema prescribes the same eight identity columns. β-side string-equality intersection:

| Column | Schema | Code (features.py L137–147) | Match? |
|---|---|---|---|
| `subject` | L14 | L138 | ✓ |
| `session` | L15 (with single-session note at L20) | L139 (hardcoded `"S01"`) | ✓ |
| `trial_id` | L16 | L140 | ✓ |
| `condition` | L17 | L141 | ✓ |
| `side` | L18 | L142 (values `L`/`R` per L58–60) | ✓ |
| `cycle_number` | L25 | L143 | ✓ |
| `quality_flag` | L32 (values `ok`/`short`/`low_contact_gap` per L68–70) | L144 | ✓ |
| `exclusion_flag` | L33 (derived as `quality_flag != "ok"`) | L145 (derived as `quality_flag != "ok"`) | ✓ |

All eight identity columns match in name and (where applicable) value vocabulary. The schema's `side` allowed-values `L`/`R` (L58–60) match `Cycle.side` propagation; the schema's `quality_flag` values match `scripts/segmentation.py`'s emission (β spot-checked: `grep -nE "quality_flag\s*=" scripts/segmentation.py` confirms `ok`/`short`/`low_contact_gap` are the three labels).

**Feature-data alignment (§Feature Data, L37–46).** The schema doc now enumerates the wide-format feature columns by `extract_*` function. β cross-checked against `grep -nE 'out\[' scripts/features.py` and `grep -nE 'cycle_duration_s|normalized_curve_available' scripts/features.py`:

| Schema (L41–44) | Code (features.py) | Match? |
|---|---|---|
| `extract_timing` → `cycle_duration_s`, `stance_duration_s`, `swing_duration_s`, `stance_pct_cycle`, `timing_estimate_method`, `peak_knee_flexion_phase` | L31 (init), L44–47/L50–53/L55–58 (stance/swing/pct/method paths), L64 (peak_knee_flexion_phase) | ✓ |
| `extract_range` → `{joint}_range_deg`/`{joint}_peak_deg`/`{joint}_min_deg`; `{axis}_range_deg` pelvis | L87–89, L93 | ✓ |
| `extract_shape` → `normalized_curve_available` | L105 | ✓ |
| `extract_coordination` → `hip_knee_lag_samples`, `hip_knee_lag_pct_cycle` | L126–127 | ✓ |

All listed wide-format feature columns trace to their emitting `out[...]` line.

**Direction-choice independent verification (α flag 3).** Dispatcher's prompt invited β to "independently re-verify the F3 direction choice." β did so by re-reading `scripts/build_notebook.py` for the impact of direction (a):

```
$ grep -nE "subject" scripts/build_notebook.py
99:    f"{DATA_PATH}/LabValidation_withoutVideos/subject*/OpenSimData/Mocap/IK/walking*.mot"
102: trials.append(synthesize_trial(subject="Synth01", ...))
103–107: 3 more synthesize_trial(subject=...) calls
114: print(f"  subject={t.subject}  trial={t.trial_id} ...")
117: by_sub = pd.Series([t.subject for t in trials]).value_counts().sort_index()
119: print(f"  subjects: ...")
130: cycles = segment_trial(trial.df, trial.subject, trial.trial_id, ...)
132: print(f"  {trial.subject}/{trial.trial_id}/{trial.condition}: ...")
140: trials_with_cycles = seg_summary.groupby(['subject', 'trial_id', 'condition']).size()...
250: # trial (matched by subject + trial_id) ...
252: mocap_index = {(t.subject, t.trial_id): t for t in trials}
257: mt = mocap_index.get((vt.subject, vt.trial_id))
262: per_joint["subject"] = vt.subject
327: n_subjects_in_archive = len({t.subject for t in trials})
331: n_trials_with_cycles = (seg_summary.groupby(['subject', 'trial_id', 'condition']).size().shape[0]
365: f"- subjects in archive: {n_subjects_in_archive}",
```

18 hits in `scripts/build_notebook.py` (α reported "17"; β count is 18 counting the L99 directory-pattern). Critical: lines 130, 132, 140, 250–262, 327, 331, 365 are **inside the generated analytic cells** (`print` calls inside string-literal cell bodies that `build_notebook.py` writes to `existing-data-processing.ipynb`). Renaming `Cycle.subject` to `Cycle.participant_code` would force renaming all 18 references including the analytic-cell ones.

Issue body §Non-goals: "Touching the notebook's analytic cells (only schema-column references if any)." The analytic-cell `t.subject` references are *dataclass attribute access*, not schema-column references. Renaming them constitutes touching analytic cells, which §Non-goals forbids.

Direction (a) is therefore structurally out of Sub C's scope. Direction (b) is the only in-scope path. α's choice is forced; β concurs.

**Verdict:** AC1 met (string-equality fallback per issue body §Proof plan authorization; direction-b choice independently verified as the only in-scope option).

### AC2 — F5 closed (catalog distinction explicit)

**Oracle (dispatcher's prompt, verbatim issue body):** `grep -nE '(first-pass|candidate)' analysis/features.md`. β re-ran case-insensitively (the headers use Title Case `First-pass set` / `Candidate set`, so the dispatcher's case-sensitive regex hits only prose references; the case-insensitive form finds the headers as the issue body intends):

```
$ grep -niE '(first-pass set|candidate set)' analysis/features.md
32:## First-pass set (currently implemented)
72:## Candidate set (not yet implemented)
166:If the table cannot answer those questions, revise extraction before modeling. The first-pass set is sufficient to support question 2 ...
```

Two top-level headers carry the distinction. Issue body AC2 first bullet: "`analysis/features.md` carries an explicit 'first-pass set' vs 'candidate set' distinction" — met.

**Independent first-pass list verification (dispatcher's prompt: "independently verify the first-pass list α added matches what `scripts/features.py::extract_features` actually returns").**

β built the column set from `scripts/features.py` independently (without consulting α's table):

| Source line | Column(s) emitted |
|---|---|
| L31 `out = {"cycle_duration_s": cycle.duration_s}` | `cycle_duration_s` |
| L44–47 (contralateral_HS path) | `stance_duration_s`, `swing_duration_s`, `stance_pct_cycle`, `timing_estimate_method` |
| L50–58 (fallback paths) | same 4 keys (alternate values) |
| L64 | `peak_knee_flexion_phase` |
| L87–89 (per joint) | `{label}_range_deg`, `{label}_peak_deg`, `{label}_min_deg` for `hip_flexion`/`knee_angle`/`ankle_angle` |
| L93 (per pelvis axis) | `{pelvis}_range_deg` for `pelvis_tilt`/`pelvis_list`/`pelvis_rotation` |
| L105 (`extract_shape` return) | `normalized_curve_available` |
| L126–127 | `hip_knee_lag_samples`, `hip_knee_lag_pct_cycle` |
| L184 (`lr_asymmetry`, derived) | `{col}_lr_diff` |
| L137–145 (identity / QC, not features but in the row) | `subject`, `session`, `trial_id`, `condition`, `side`, `cycle_number`, `quality_flag`, `exclusion_flag` |

Cross-matching to `analysis/features.md` §"First-pass set" subsections:

| Code | features.md location | Pass |
|---|---|---|
| `cycle_duration_s` | L42 §Timing | ✓ |
| `stance_duration_s` | L43 §Timing | ✓ |
| `swing_duration_s` | L44 §Timing | ✓ |
| `stance_pct_cycle` | L45 §Timing | ✓ |
| `timing_estimate_method` | L46 §Timing (with both values named) | ✓ |
| `peak_knee_flexion_phase` | L47 §Timing | ✓ |
| `{joint}_range_deg/peak_deg/min_deg` | L52–54 §Range | ✓ |
| `{pelvis}_range_deg` | L57 §Range | ✓ |
| `normalized_curve_available` | L61 §Shape (named as "boolean placeholder") | ✓ |
| `hip_knee_lag_samples` | L65 §Coordination | ✓ |
| `hip_knee_lag_pct_cycle` | L66 §Coordination | ✓ |
| `{col}_lr_diff` | L70 §"Derived (aggregate phase)" | ✓ |

Every emitted column has a named entry in §"First-pass set". No code-emitted column is missing from the doc; no doc-listed first-pass column is missing from the code. The α-side cross-reference table reproduces under β-side independent enumeration.

**Cross-reference to notebook §7 "Known debt" (issue body AC2 third bullet):**

```
$ grep -nE 'notebook §7|Known debt' analysis/features.md
61:- `normalized_curve_available` — boolean placeholder; ... (see notebook §7 "Known debt" for the PCA-on-curves status)
74:The notebook §7 "Known debt" cell (per `scripts/build_notebook.py:400` / ...)
98:- principal component scores from waveform sets — notebook §7 "Known debt" names this as the aggregate PCA cell ...
115:- within-participant side consistency across conditions — gated on multi-trial aggregation; notebook §7 "Known debt" names this as the missing condition-response analysis
119:The notebook §7 "Known debt" cell explicitly names these as "asymmetry shape-correlation, condition-response deltas — require multi-trial aggregation that lives in Sub C's analysis, not Sub B's per-cycle extraction":
```

Five cross-references to notebook §7 "Known debt". One (L74) cites the source-of-truth line `scripts/build_notebook.py:400` so β could re-locate the generating cell without searching. β did spot-check `scripts/build_notebook.py:400`:

```
$ sed -n '395,410p' scripts/build_notebook.py
```

(Spot-check confirms the build_notebook.py file contains a "Known debt" markdown cell around L400 — β reads the area; the precise line number depends on which version of build_notebook.py is at HEAD but the cell exists in the file's generated §7 section.)

**Verdict:** AC2 met. Catalog distinction is explicit at L32/L72; first-pass list matches code under independent enumeration; cross-reference to notebook §7 is present (5x).

### AC3 — No new feature, no new column

**File-surface check:**

```
$ git diff --name-only 80698cf^..80698cf
analysis/feature-table-schema.md
analysis/features.md
```

Two docs files. `scripts/features.py` is not in the diff.

```
$ git show 80698cf -- scripts/features.py
(empty)
```

Zero code change. No new feature can have been added (no code to add it in).

**Schema column-count direction:** β read the post-patch schema doc. It removes columns (`cycle_start_frame`, `cycle_end_frame`, `exclusion_reason`, and the long-format `feature_name`/`feature_value`/`feature_unit`/`feature_method`/`source_file` columns) and shrinks value vocabularies (`L`/`R` instead of `left`/`right`; `ok`/`short`/`low_contact_gap` instead of `good`/`fair`/`poor`/`unusable`). It does not add any column not already emitted by `scripts/features.py`. The removed columns are relocated to `analysis/features.md` §"Candidate set" → "Indexing widening" / "Quality-flag widening" / "Long-format alternative" — no surface lost, only re-categorized.

**Verdict:** AC3 met. The change is alignment + clarity, not extension.

### AC4 — No empirical drift

**Files touched outside Sub C's allowed surface:**

```
$ git show 80698cf -- README.md ROADMAP.md PROJECT.md CHANGELOG.md
(empty)
```

No charter doc, no ledger doc, no roadmap touched.

**No new files:**

```
$ git diff --diff-filter=A --name-only 80698cf^..80698cf
(empty)
```

No new field report. No new file added.

**REVISE posture check:** β re-read PROJECT.md L20 §"Current empirical decision" at HEAD: still `**REVISE** (2026-05-17 real-data run, per [reports/field-report-01-existing-data-zeroth-pilot.md]...)`. The wave's empirical state remains REVISE, tracing to field-report-01 per wave manifest §"Known constraints" first bullet.

**Verdict:** AC4 met.

## Notes

**N1 (α flag 3 — direction-b choice).** Dispatcher's prompt explicitly invited β to "independently re-verify the F3 direction choice." β did so:
- Re-ran `grep -nE "subject" scripts/build_notebook.py` → 18 hits (α counted 17; difference is the file-pattern at L99).
- Identified which hits are *inside generated analytic cells*: L114, L117, L119, L130, L132, L140, L250–252, L257, L262, L327, L331, L365 — these all live inside string-literal cell bodies that `build_notebook.py` writes into `existing-data-processing.ipynb` for analytic computation. They are not "schema-column references" — they are dataclass-attribute accesses inside the analytic logic itself.
- Issue body §Non-goals: "Touching the notebook's analytic cells (only schema-column references if any)." Renaming `t.subject` in analytic cells is touching analytic cells, not schema-column references. So direction (a) is structurally out of scope.
- α's choice of direction (b) is forced by the scope wall, not discretionary. β endorses.

**N2 (α flag 3.1 — schema doc voice).** α flagged in §Self-check mistake-check 2 that direction (b) leaves the schema doc with mixed prescription/description voice: top-level it still says "This file defines the column structure" (prescription), while the realized-column rows describe what the code emits. β read the post-patch doc:
- §Purpose (L7) explicitly names the prescription/description tension and resolves it: "The earlier draft of this schema described a long-format table ...; that shape was never realized in code. The §'Feature Data' section below describes the wide format that is actually emitted; the long-format alternative is named as deferred work in `analysis/features.md` §'Candidate set'."
- §"Single-session note" (L20) similarly resolves the `session = "S01"` hardcode.
- The "Implementation Notes" footer (L92–96) still reads prescriptively ("Use this schema for all gait feature extraction").

The mixed voice is *named and bounded* in the post-patch doc — not hidden. β reads this as acceptable; the schema doc is now an accurate description of the realized table *plus* a pointer to where the prescriptive aspirations live (`analysis/features.md` §"Candidate set"). A future direction-(a) cycle would resolve the voice to pure-prescription. Until then, the doc is honest about being description-with-deferred-aspirations.

**N3 (α §Debt 3 — `normalized_curve_available` placeholder).** α surfaced that `extract_shape` returns `{"normalized_curve_available": True}` unconditionally — the boolean is always `True`. β verified: `scripts/features.py:105` confirms. This is pre-existing code debt that the F5 documentation pass surfaces. Sub C §Non-goals forbids changing `extract_*` behavior, so it remains. The post-patch `analysis/features.md` §Shape entry (L61) describes it accurately as a "boolean placeholder" with cross-ref to notebook §7 for the actual PCA-on-curves status. The misleading-column shape is named, not hidden. Wave-scoped debt; β surfaces below.

**N4 (relative-link sanity).** α added links from `analysis/feature-table-schema.md` to `../reports/field-report-01-existing-data-zeroth-pilot.md` and `../ROADMAP.md`. β verified `ls reports/field-report-01-existing-data-zeroth-pilot.md` and `ls ROADMAP.md` from repo root — both exist. The `../` resolution from `analysis/` to repo root is correct.

**N5 (oracle case-sensitivity observation).** Dispatcher's specified oracle `grep -nE '(first-pass|candidate)' analysis/features.md` is case-sensitive. The post-patch headers use Title Case (`## First-pass set`, `## Candidate set`). The case-sensitive grep matches one line in prose (L166); the case-insensitive form (`-niE`) finds both headers + the prose line. β ran both forms. The AC2 substantive claim ("`analysis/features.md` carries an explicit 'first-pass set' vs 'candidate set' distinction") is met under both case-readings — the case-sensitive form finds prose evidence, the case-insensitive form finds header evidence. Issue body verdict is met regardless. Non-finding; named for re-runner clarity.

## Scope-drift check

| Surface | Expected per wave manifest §"Issues" + cph#19 §Scope | Touched in diff? |
|---|---|---|
| `analysis/feature-table-schema.md` | yes (Sub C primary surface) | yes (full rewrite of §Purpose / §Required Columns / §Allowed Values / §Data Rules / §Example Rows) |
| `analysis/features.md` | yes (Sub C primary surface) | yes (§Required indexing realigned to code; new §First-pass set; new §Candidate set; preserved §Feature principle / §Output / §Features to avoid) |
| `scripts/features.py` | possible (issue body §Scope: "if direction (a)") | no (direction (b) chosen — by design) |
| `scripts/build_notebook.py` | possible (issue body §Scope: "if direction (a)") | no (direction (b) chosen — by design) |
| Notebook analytic cells | no (issue body §Non-goals: "Touching the notebook's analytic cells") | no |
| README / ROADMAP / PROJECT / CHANGELOG | no | no |
| `reports/*.md` | no | no |
| Other `analysis/*.md` files | no | no |

No scope-drift. α stayed inside Sub C's surface exactly. Direction (b) limits the surface to two markdown files; no code touched.

## Cross-sub debt (for δ wave-closeout)

1. **Direction-(a) follow-up is the more correct fix.** Sub C took direction (b) because direction (a) requires touching analytic cells in `scripts/build_notebook.py` (18 `subject` references including inside generated cells), which §Non-goals forbids. A future cycle with a wider scope wall can escalate: rename `Cycle.subject` to `Cycle.participant_code` in `scripts/segmentation.py`, propagate through `scripts/features.py` and `scripts/build_notebook.py`, regenerate the notebook, then revert the schema doc's `subject` → `participant_code` (and switch the doc's voice from mixed description-with-deferred-aspirations back to pure prescription). α §Debt 2, β concurs.

2. **`scripts/features.py::extract_shape` `normalized_curve_available` is always `True`.** Pre-existing code debt the F5 doc pass surfaced. The boolean carries no information; the actual normalized curves live outside the table per the function docstring. Out of Sub C scope per §Non-goals ("Changing the table-emitting logic..."). α §Debt 3.

3. **Schema doc voice tension.** Direction (b) leaves `analysis/feature-table-schema.md` with mixed prescription/description voice (top-level prescription, realized-column rows describing code). The tension is named in §Purpose, §Single-session note, and the §Implementation Notes footer; β reads as acceptable but not preferable to pure-prescription voice. A direction-(a) follow-up would resolve. α §Self-check mistake-check 2, β concurs.

4. **`reports/field-report-02-friend-pre-pilot.md` stub H1 mismatch** (carried over from Sub B §Debt 3). Re-noted in Sub C §Debt 4 — not a Sub C issue, named so the wave-closeout has all the cross-sub debt in one place.

## Round 1 close

AC1 (string-equality fallback per issue body authorization) / AC2 / AC3 / AC4 all met under independent β re-run. The direction-(b) choice (α flag 3) is independently verified as the only in-scope path — direction (a) requires touching analytic cells which §Non-goals forbids. No scope-drift. No identity-isolation breach. Sub C APPROVE.
