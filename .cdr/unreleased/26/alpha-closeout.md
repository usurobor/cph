# α closeout — cph#26

Per `cdd/alpha/SKILL.md §2.8`. Voice: factual observations and patterns only; no dispositions (triage is γ/δ).

## Cycle summary

- **Issue:** [usurobor/cph#26](https://github.com/usurobor/cph/issues/26) — Port segmentation-real-data-fix onto current main.
- **Branch:** `cycle/port-segmentation-fix` (deleted from origin after merge per β closeout).
- **Mode:** empirical implementation port (not design-and-build); two-step structure (A = surgical 3-way merge; B = notebook rerun + status-surface realignment) emerged from the issue body's §Steps 6 "Hard stop if notebook falls back to synthetic mode" gate.
- **Rounds:** 1. APPROVE on first read. Zero RC.
- **Implementation SHA:** `c5cf241`. **Merge SHA:** `a63aecc`. **Base (origin/main pre-cycle):** `ebd909c`.
- **β verdict commit:** `77426a5`. **β closeout:** `8331f8b`.
- **Files merged:** 14 — 4 scripts (incl. one new module `scripts/segmentation_diagnostics.py`), 1 notebook, 1 feature-summary, 1 field report, 3 status surfaces (PROJECT/ROADMAP/CHANGELOG), 3 sibling-docs from fix-round 1 (feature-table-schema, features, coherence-path-hypothesis §"Current empirical status"), 1 self-coherence + 1 beta-review (cycle dir).
- **All commits authored as `alpha@cph.cdd.cnos`** after §2.6 row 14 path (a) retroactive identity correction at the start of self-coherence authoring.

## Observations (factual; no recommendation)

### Pattern: pre-review gate row 6 surfaced sibling-surface drift that the implementation port had not enumerated

**Context.** Step A's per-file 3-way merge into `scripts/features.py` cleanly added 6 new feature-column emissions (`hip_adduction_{range,peak,min}_deg` via the joint_map; `lumbar_{bending,rotation,extension}_range_deg` via a new trunk loop) inherited from the precursor branch. The 3-way merge's "clean" status reported no conflict — and there was no Python-side conflict. The drift surfaced at row 6 of the pre-review gate (schema/shape audit when contracts changed): `analysis/feature-table-schema.md` L42 and `analysis/features.md` §"Range / amplitude" still listed only the pre-cycle joints (hip_flexion / knee_angle / ankle_angle) and pelvis axes; `analysis/features.md` §"Candidate range/amplitude features" L86 carried "hip adduction-abduction range" as Candidate-not-implemented.

**Friction.** Nine peer-surface drift findings (F1–F9 in self-coherence §Fix-round 1) — one row each in two schema docs, one stale-list entry, three stale segmentation-status references in §"Candidate set", and one §"Current empirical status" patch on `docs/concepts/coherence-path-hypothesis.md` (peer to PROJECT/ROADMAP/CHANGELOG). Resolved on first audit pass via a single fix-round commit (`c5cf241`).

**Pattern surface.** A clean 3-way merge of code that *adds* dict-key emissions to a side-channel schema-bearing function passes Python-level conflict detection but does not surface the cross-document peer surface that documents those keys. The schema-bearing surface here is `extract_range`'s output dict shape, which is a Python-level contract but not a typed one — `pd.DataFrame(rows)` accepts any dict shape silently. Surfaces affected: `cnos.eng/python` if a peer-enumeration row exists; `cdd/alpha/SKILL.md §2.3` (peer enumeration before closure claims, "multiple writers / readers of the same schema") — the row is already present but did not fire pre-author; it fired at row 6 (schema audit) which is the post-author gate.

### Pattern: identity drift via session continuation across roles

**Context.** Session-start identity was `epsilon@cph.cdd.cnos` (carried from the prior wave's ε run that closed the `cdr-refactor-2026-05-18` wave). The pre-existing two implementation commits on this branch (`41b3693` Step A, `9eb34ee` Step B) carried `delta@cph.cdd.cnos` authorship (drift via session continuation through an intermediate δ-as-agent attribution).

**Friction.** §2.6 row 14 path (a) retroactive correction rewrote both commits before review-readiness signal (`41b3693 → 9bcef90`, `9eb34ee → f27904a`). Force-with-lease push, no upstream rejection. Self-coherence §Debt names the corrected identity-state.

**Pattern surface.** Long-running sessions that span multiple cycles and role transitions accumulate `git config user.email` state from each role. The §2.6 row 14 check is positioned at gate-time; the missing check is at session-start / role-transition. Surfaces affected: `cdd/operator/SKILL.md` (the role-as-agent identity-config rule), `cdd/CDD.md §1.4` step-1 (configure git identity *as the first action* on dispatch). Same pattern class as cnos #287 R1 F3 named in α/SKILL.md §2.6 row 14's derivation note, but originating from session-continuation rather than session-start muscle memory.

### Pattern: large notebook re-execution surfaces a Read-token limit on review

**Context.** β round-1 review hit `TOOL_ERR File content (39618 tokens) exceeds maximum allowed tokens (25000)` while reading either the executed notebook (548928 bytes) or the full self-coherence file (~660 lines). β adapted with offset/limit reads and completed the review.

**Friction.** Non-fatal. Same class as the prior wave's β-15 / ε Read token limit (named in `.cdr/waves/cdr-refactor-2026-05-18/receipt.md` §5). The notebook is the load-bearing instance — executed notebooks with cached cell outputs (PNG plot bytes inline in the .ipynb JSON) exceed Read-tool limits even for moderate analyses.

**Pattern surface.** This recurs each time a cycle merges an executed notebook with embedded outputs. The α-side mitigation is named in self-coherence §"Round-1 RC risk surface" ("the notebook file itself is a build artifact"; canonical review surface is the Python source under `scripts/` + runner-output excerpts in §AC2 + the field-report-01 cross-reference table in §AC3). Surfaces affected: `cdd/beta/SKILL.md` (β tooling: when does β need to read the full notebook?), and downstream `cdd/alpha/SKILL.md §2.6` row 11 (artifact enumeration matches diff) when the diff includes executed notebooks.

## Out-of-scope follow-ups carried forward (named, not filed)

These are documented in self-coherence §Debt + are reachable on top of this merge:

1. **R-side aggregate condition-response analysis** (P4 in cph#26 §"Post-port decision"; operator-recommended next issue). R-side n=60 across 10 subjects × 2 conditions; `hip_adduction_range_deg` + `pelvis_list_range_deg` + `lumbar_bending_range_deg` populated.

2. **L-side cycle recovery** (P5). Structural data-shape constraint; two paths named in field-report-01 §"Decision" (contralateral-anchored detection OR longer-trial capture).

3. **First mechanical `coh --mode mechanical` run for CHANGELOG.md 0.3.0.** Gated on `coh` being on PATH in an operator environment + a tagged release (`.github/workflows/coherence.yml` trigger).

4. **`origin/cycle/segmentation-real-data-fix` (tip `a95415c`).** Precursor branch superseded by this port. Cleanup is δ/operator authority.

5. **cph#26 issue close.** The issue is still OPEN as of this closeout; β did not exercise issue-close authority (not granted in the dispatch prompt). δ/operator decision per the standard single-issue-cycle convention.

## CDD-iteration candidacy

α voice rule §2.8 forbids dispositions — the following is named only, not recommended for ε to act on:

- **Pattern 1** (sibling-surface drift after clean Python 3-way merge): same finding class as F7-class anchoring discipline from cph#21 / cph#22 — code-first oracle anchoring. Whether `cdd/alpha/SKILL.md §2.3` needs an explicit "dict-key emission peer" row vs. the existing schema-writer/reader row already covering it is ε's call.

- **Pattern 2** (session-continuation identity drift): same class as cnos #287 R1 F3, but originating site differs (session-start muscle-memory vs. cross-role session continuation). Whether this warrants a session-start `git config` check parallel to the gate-time §2.6 row 14 check is ε's call.

- **Pattern 3** (executed-notebook Read-tool limit): recurring β-side friction; prior wave receipt §5 already named it. Whether this is a `cdd/beta/SKILL.md` patch or a build-artifact discipline (don't merge cached cell outputs?) or operator-environment-only is ε's call.
