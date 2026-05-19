# Wave Close-out: Coherence drift sweep (master cph#16)

**Wave:** `.cdd/waves/coherence-drift-sweep-2026-05-18/`
**Date opened:** 2026-05-18
**Date closed:** 2026-05-18 (same-day wave)
**Dispatcher:** δ-as-agent (γ=δ permitted at this scale per `cdd/operator/SKILL.md` §5.2)
**Master:** usurobor/cph#16 — *open* at wave close (master closure deferred to ε per the precedent set by `cdr-refactor-2026-05-18` §"Master closure"; see §Master closure below)
**Configuration:** single-branch dispatch on `claude/review-repo-coherence-PNbjQ` via two parallel `Agent` invocations (one α-session implementing all four subs serially; one β-session reviewing all four subs serially). Identity-isolation invariant preserved by Agent-session boundaries: α and β are independent context windows.

## Summary

Patched six coherence-drift findings (F1–F6) surfaced by the post-`cdr-refactor-2026-05-18` review on `claude/review-repo-coherence-PNbjQ`. Wave was a four-sub split per the five-factor heuristic on master cph#16: F1+F6 (Sub A), F2 (Sub B), F3+F5 (Sub C), F4 (Sub D). Every sub APPROVED round 1, zero β findings across the wave, zero fix-rounds.

The wave validates that the CDR refactor (cph#11 wave) succeeded structurally — the patches landed cleanly and the canonical surfaces re-cohered without process friction — and closes the α-axis cross-file drift items that the cph#11 wave itself shipped with.

## Aggregate metrics

| Cycle | Mode | Findings | Rounds | α SHA (impl) | α SHA (self-coh) | β SHA (review+closeout) | Notes |
|---|---|---|---|---|---|---|---|
| #17 (Sub A) | docs-only | F1, F6 | 1 (APPROVE) | `72c3845` | `7893ee9` | `b32bde2` | Two single-line patches; minimum cph-credibility fix |
| #18 (Sub B) | docs-only (design call) | F2 | 1 (APPROVE) | `a7684f1` | `d234183` | `a69a863` | Scheme forced by existing stub `field-report-02-friend-pre-pilot.md`: R5 = -02, R3 = -03 |
| #19 (Sub C) | docs + code | F3, F5 | 1 (APPROVE) | `80698cf` | `319ab3e` | `399bfd8` | Direction (b) — shrunk schema to match code; F5 first-pass list verified bijective |
| #20 (Sub D) | docs + code | F4 | 1 (APPROVE) | `8859b62` | `00f38b3` | `040ed3c` | Renamed to `cph-features/`; notebook regenerated; cached outputs stripped (~1400-line diff) |
| **Wave totals** | — | F1–F6 (six findings) | **4 × APPROVE round 1 / 0 RC** | — | — | — | — |

### Repository delta (origin/main: 42fd348 → wave-closeout commit)

- **24 files changed, +2,479 / −1,479** (net +1,000 lines)
- Of which **+1,000 net** is dominated by:
  - `.cdd/unreleased/{17,18,19,20}/` cycle artifacts: 12 new files (self-coherence + beta-review + beta-closeout per sub)
  - `.cdd/waves/coherence-drift-sweep-2026-05-18/` wave artifacts: 3 new files (manifest, status, this close-out)
- **Non-`.cdd` delta:** 10 files changed, +226 / −1,479 — the negative count is Sub D's notebook regeneration stripping cached execution outputs (−1,418 lines on `notebooks/existing-data-processing.ipynb` alone).
- **Charter / roadmap / ledger touch (substantive):** `PROJECT.md` (one line), `ROADMAP.md` (four lines across L66, L83, L85, L87), `analysis/feature-table-schema.md` (86 lines reshaped), `analysis/features.md` (175 lines reshaped).
- **No new top-level files. No new directories.** Two new files inside `analysis/` are not created; all touches are to existing files.

### Identity audit (commit-author roll-call)

- **α commits (8):** all `α-as-agent <alpha@cph.cdd.cnos>` — `72c3845`, `7893ee9`, `a7684f1`, `d234183`, `80698cf`, `319ab3e`, `8859b62`, `00f38b3`.
- **β commits (4):** all `β-as-agent <beta@cph.cdd.cnos>` — `b32bde2`, `a69a863`, `399bfd8`, `040ed3c`.
- **δ commits (2):** both `δ-as-agent <delta@cph.cdd.cnos>` — `dcd0d50` (wave open) and `91fd2e5` (`.gitignore` patch for `.claude/` harness scaffolding, named for audit-trail completeness in Sub A self-coherence §Debt 2 and β closeout §Cross-sub debt 5).
- **Identity-isolation invariant:** α ≠ β within every sub, held across the wave. No `git config` operations. No `--amend`. No `--no-verify`.

## Master cph#16 ACs — final state

| AC | Owner sub | Status |
|---|---|---|
| AC1 — F1 closed (broken realization ref) | #17 | ✅ |
| AC2 — F2 closed (field-report-02 collision) | #18 | ✅ |
| AC3 — F3 closed (schema/code column alignment) | #19 | ✅ — direction (b); see §"Cross-sub findings" item 3 |
| AC4 — F4 closed (rename live `gait-support-paths-features/`) | #20 | ✅ |
| AC5 — F5 closed (first-pass vs candidate distinction in `features.md`) | #19 | ✅ — bijective with code |
| AC6 — F6 closed (PROJECT.md R0 wording) | #17 | ✅ |
| AC7 — No empirical drift | cross-cutting | ✅ — REVISE posture intact; no new field report; README empirical-state language unchanged |
| AC8 — No new schema, no new features | cross-cutting | ✅ — no feature added to `scripts/features.py`; no column added to the schema; Sub C is alignment-only |

All 8 master ACs met. Empirical REVISE posture preserved per `reports/field-report-01-existing-data-zeroth-pilot.md`.

## Cross-sub findings & cycle iteration

The wave ran cleanly (4× APPROVE round 1; 0 β findings). The α and β close-outs surfaced five cross-sub debt items worth carrying forward — none rose to the level of requiring a follow-on issue *from this wave*, but they are named here for ε's wave-level review:

1. **ROADMAP R0 §Next action is itself stale.** Sub A patched `ROADMAP.md:85` (F1) and `PROJECT.md:16` (F6) but left `ROADMAP.md:36` ("Next action: Sub B (this), Sub C, Sub D merge; wave `cdr-refactor-2026-05-18` closes; phase transitions to GO at wave close") unchanged because the cdr-refactor wave already closed and editing R0 §Next action is outside cph#17 §Non-goals. α named this in §Debt 1; β endorsed in beta-closeout §Cross-sub debt 1. **Class:** out-of-scope follow-up. **Action:** follow-on cycle to refresh ROADMAP R0 §Next action (and probably R0 §Status — "ACTIVE" pending what specifically) once `coh` is on PATH or independently of that.

2. **Stub-H1-vs-filename mismatch in `reports/field-report-02-friend-pre-pilot.md`.** Sub B's scheme decision was forced by the existence of `field-report-02-friend-pre-pilot.md` as a stub on disk; α verified the file exists with `head -5` and is genuinely a stub. The stub's H1 may not match the filename (β re-noted in cph#19 §Debt 4 cross-reference). **Class:** stub-cleanup debt; orthogonal to this wave. **Action:** when R5's field report actually ships, the stub gets filled or renamed.

3. **Sub C direction (b) vs (a).** α chose direction (b) — shrunk the schema doc to match the code — because direction (a) would require touching ~18 `subject`/`session` references inside `build_notebook.py`'s generated analytic cells, which cph#19 §Non-goals forbids. β independently verified this in beta-closeout §AC1 verification item 3 ("Direction (a) … would require touching these analytic-cell references, which issue body §Non-goals forbids. Direction (b) is the only in-scope path. α's choice is forced by the scope wall, not discretionary. β endorses."). **Class:** scoped-out from cph#19; the better direction is still (a). **Action:** future cycle scoped to allow `build_notebook.py` analytic-cell touch can rename `Cycle.subject` → `Cycle.participant_code` and propagate.

4. **Sub D `pip install` policy interpretation.** α ran `pip3 install nbformat==5.10.4` to regenerate the notebook. `nbformat==5.10.4` is already pinned in `requirements.txt:16`; α disclosed this in Sub D §Debt 1 as an exception to the wave-manifest standing-permission "Install Python packages: NO (this wave does not touch `requirements.txt`)". β read this in beta-closeout §Cross-sub debt 4 as "install-to-match-spec, not a policy breach (no `requirements.txt` modification, no dependency drift)" and recommended a wave-manifest standing-permissions clarification for future waves. **Class:** cdd-protocol clarification candidate. **Action:** ε to comment; future wave manifests can read "Install Python packages: only to satisfy existing pinned versions in `requirements.txt`" (or whatever phrasing ε prefers).

5. **Intermediate δ commit `91fd2e5` (`.gitignore` `.claude/`).** Between Sub A's α impl (`72c3845`) and α's self-coherence (`7893ee9`), δ committed a `.gitignore` patch to suppress the `.claude/worktrees/` harness scaffolding that the parallel agent infrastructure created. β named this in beta-closeout §Cross-sub debt 5 "for audit trail completeness". **Class:** dispatch-infrastructure artifact, not a CDD-protocol issue. **Action:** future waves under Claude Code's worktree-spawning infrastructure inherit the `.gitignore` line; no patch needed.

## Wave-internal disconnect posture

This wave **does not produce a release tag.** No version bump, no `RELEASE.md`, no `scripts/release.sh` invocation. The disconnect signal is the four α-implementation commits + four β-approval commits + this wave-closeout landing on `claude/review-repo-coherence-PNbjQ`. Per the wave manifest's standing permissions, tag/release is operator-gated and was explicitly NO at wave open; the wave honored that.

The `.cdd/unreleased/{17,18,19,20}/` directories remain in `.cdd/unreleased/` — they do **not** move to `.cdd/releases/{X.Y.Z}/{N}/` at this wave's close because the cph repo has no release-cut for this wave. Future release work (if any) inherits these unreleased directories as part of its scope.

## Master closure

Master cph#16 remains **OPEN** at wave close. The wave manifest declared no automatic master-close action (consistent with the precedent set by `cdr-refactor-2026-05-18` §"Master closure"). All 8 ACs from cph#16 are met; all 4 subs are at β-APPROVE; the wave-closeout is on the dispatch branch. ε (or the operator) holds the master-close decision after wave-level review.

Recommended closure comment for cph#16: a one-comment summary linking to this wave-closeout, the per-sub commit pairs, and the four sub-issues; close with `Closes #16`. The same comment should reference the five cross-sub debt items in §"Cross-sub findings" above so they survive master closure as named-debt, not silent-debt.

## Out-of-scope follow-ups (named, not executed by this wave)

Carried forward verbatim from the wave manifest plus items surfaced by α/β during execution:

- **First mechanical `coh --mode mechanical` run** + recording the numeric α/β/γ/C_Σ baseline into `CHANGELOG.md` (still gated on `coh` being on PATH; same deferred item the cph#11 wave named).
- **Operator-side on-disk data migration** from `gait-support-paths-features/` to `cph-features/`. Operators currently using the old path keep working under `GAIT_DATA_ROOT` until they switch.
- **Restoration of `cycle/{N}` push permissions** on the cph harness (out of scope; this wave used the single-branch deviation per the manifest).
- **ROADMAP R0 §Next action refresh** — cross-sub debt 1 above.
- **Sub C direction (a)** — cross-sub debt 3 above; rename `Cycle.subject` → `Cycle.participant_code` in a cycle scoped to allow `build_notebook.py` analytic-cell touch.
- **`extract_shape` always-`True` placeholder** in `scripts/features.py:97–105` (β surfaced in cph#19 §Cross-sub debt) — the function returns `{"normalized_curve_available": True}` with no actual normalized waveforms. Out of scope for cph#19 (Sub C is alignment-only). Worth instrumenting in a future cycle.
- **Notebook re-execution** to re-bake the analytic outputs after Sub D's regeneration stripped them (operator-side; gated on data availability).
- **`pip install` policy clarification** in future wave manifests (cross-sub debt 4 above).
- **Stub-H1-vs-filename cleanup** in `reports/field-report-02-friend-pre-pilot.md` (cross-sub debt 2 above).
- **Body edit of master cph#16** (left as as-filed; sub-issue links live in cph#16 comments + this wave's manifest).

## Dispatch infrastructure observations

Three infrastructure observations from this wave's δ-as-agent execution that may inform future waves:

1. **Single-branch dispatch via paired Agent sessions held cleanly.** Identity-isolation was realized not by `cycle/{N}` branches + identity-config-per-worktree (the cph#11 wave's model) but by Agent-session boundaries: α-as-agent ran in one Agent context for all four subs serially; β-as-agent ran in a separate Agent context for all four subs serially. Each Agent invocation is an independent context window; α and β cannot share state. The hard rule `α ≠ β within a single sub` (per `cdd/CDD.md` §1.4) held across all four subs by construction.
2. **`.claude/worktrees/` scaffolding requires `.gitignore`.** The Claude Code harness's Agent tool creates `.claude/worktrees/{id}/` directories as side-effect scratch space. These are ephemeral container state, not project source. The `.gitignore` patch (δ commit `91fd2e5`) ignores `.claude/` and is durable for future waves under the same harness configuration. Future cph wave manifests should expect this scaffolding and not need to re-patch.
3. **Serial-within-Agent + parallel-across-Agents is the right granularity for small-sub waves.** This wave's four subs were each 1–4 file touches with no cross-sub merge conflicts. Running α through all four serially (within one Agent session) and β through all four serially (within a separate Agent session) was simpler than spawning eight separate Agent calls (one α + one β per sub), and the identity-isolation invariant held just as cleanly. For larger sub-loads (multi-file authoring; cph#11 wave's Sub A style), per-sub Agent dispatch is still preferred for context-window hygiene.

---
_End of wave close-out._
