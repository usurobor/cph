# Wave Close-out: CDR refactor (master cph#11)

**Wave:** `.cdd/waves/cdr-refactor-2026-05-18/`
**Date opened:** 2026-05-18 (post-rename of `usurobor/gait-support-paths` → `usurobor/cph`)
**Date closed:** 2026-05-18
**Dispatcher:** δ-as-agent (γ=δ permitted at this scale per `cdd/operator/SKILL.md` §5.2)
**Master:** usurobor/cph#11 — *open* at wave close (master closure is a separate δ action; see §Master closure below)
**Configuration:** sequential multi-cycle dispatch via `claude -p` (one role at a time per `operator/SKILL.md` §5.1 within a shared working tree at `/root/cph`)

## Summary

Refactored the cph repo from a methods scaffold into a model CDR (Coherence-Driven Research) project. Wave was a four-sub split per the five-factor heuristic on master #11 (10 ACs across charter / roadmap / TSC infra / sweep). Every sub APPROVED round 1, zero β findings across the wave, zero fix-rounds across the wave.

## Aggregate metrics

| Cycle | Mode | ACs from #11 | Rounds | α turns | β turns | α-closeout turns | Wall (cycle) | Cost (cycle) | Merge commit |
|---|---|---|---|---|---|---|---|---|---|
| #12 (Sub A — charter) | design-and-build | 1, 2, 4, 10-init | 1 (APPROVE) | 75 | 66 | 20 | ~30 min | $8.72 | `c3c274a` |
| #13 (Sub B — roadmap) | design-and-build | 3 | 1 (APPROVE) | 67 | 24 | 20 | ~17 min | $5.80 | `49cd888` |
| #14 (Sub C — TSC infra + CHANGELOG + PROJECT.md) | MCA-eligible | 5, 6, 7 + AC-PROJECT | 1 (APPROVE) | 111 | 65 | 17 | ~21 min | $8.92 | `f6ad183` |
| #15 (Sub D — conformance sweep) | docs-only | 8, 9, 10-final | 1 (APPROVE) | 76 | 45 | 16 | ~21 min | $7.17 | `9bf00f1` |
| **Wave totals** | — | — | **4 × APPROVE / 0 RC** | 329 | 200 | 73 | **~89 min cycles** | **$30.61** | — |

### Repository delta (origin/main: 06341a4 → 275ba10... → ba36725 + status)

- **31 files changed, +3,219 / −214** (net +3,005 lines)
- **New canonical surfaces:** `CDR.md`, `CHANGELOG.md`, `ROADMAP.md`, `docs/concepts/coherence-path-hypothesis.md`, `docs/articles/seven-ways-people-walk.md`, `targets/{registry,hypothesis,method,evidence,repo}.tsc`, `scripts/measure-coherence.sh`
- **Modified surfaces:** `README.md` (charter rewrite), `PROJECT.md` (repartition to status-only)
- **Cycle artifacts:** 16 files under `.cdd/unreleased/{12,13,14,15}/` (self-coherence, beta-review, alpha-closeout, beta-closeout per cycle)

## ACs from master #11 — final state

| AC | Owner sub | Status |
|---|---|---|
| 1 — README identity is clear | #12 | ✅ |
| 2 — Hypothesis authority exists (docs/concepts/coherence-path-hypothesis.md) | #12 | ✅ |
| 3 — Roadmap exists and is gate-based (ROADMAP.md) | #13 | ✅ |
| 4 — CDR doctrine exists (CDR.md) | #12 | ✅ |
| 5 — TSC targets exist (`targets/*.tsc`) | #14 | ✅ |
| 6 — Coherence measurement can run (`scripts/measure-coherence.sh`) | #14 | ✅ |
| 7 — Changelog records CDR baseline (`CHANGELOG.md`) | #14 | ✅ |
| 8 — No empirical overclaim | #15 | ✅ (sweep clean) |
| 9 — No data policy regression | #15 | ✅ (sweep clean) |
| 10 — Source-of-truth boundaries explicit | #12 (initial) + #15 (final) | ✅ |

All 10 master ACs met. Empirical REVISE posture preserved.

## Cross-sub findings & cycle iteration

The wave ran cleanly enough that no `cdd-skill-gap` / `cdd-protocol-gap` / `cdd-tooling-gap` / `cdd-metric-gap` finding rose to the level requiring a follow-on issue this wave. But the wave's α close-outs surfaced four observations worth carrying forward as candidate skill-patch material for a future cycle's γ to triage:

1. **α §2.6 has no row for γ-artifact presence.** β rule 3.11b gates on `.cdd/unreleased/{N}/gamma-scaffold.md` literal presence; α pre-review gate does not enumerate γ-side artifacts at all. β surfaced the absence-vs-substance question as a non-binding observation in each cycle's `beta-review.md` §3.11b. Class: α gate does not pre-empt a surface β rule will examine. Candidate skill patch: add a row to alpha/§2.6 for "γ-side artifact enumeration (scaffold + coordination + any γ-write surfaces named in the wave manifest)." (Observed across #12, #13, #14, #15.)
2. **Wave manifest forward-reference contract worked cleanly.** Sub C's `targets/hypothesis.tsc` referenced files Sub A would author (README, CDR.md, hypothesis doc, seven-ways article) without rebase coordination. The manifest's pinned-paths table was sufficient — no `gamma-coordination.md` write was needed across the wave. Class: positive — first wave that exercised forward-reference contracts under parallelizable-but-serially-executed subs. Worth naming as a successful pattern in any future wave manifest skill.
3. **Intra-doc repetition rule (α §2.3) fired twice as a self-correction during self-coherence authoring** — once in #14 (grep count 4 not 6 in §Self-check polyglot re-audit) and once in #15 (intra-doc owner-reference count). In both cases α caught its own drift before signaling review-readiness, proving the rule transfers from prior cycles' empirical anchors (notably tsc #266 F3/F3-bis) without re-derivation. Class: positive — generalization of a rule first hardened in tsc was load-bearing in cph.
4. **β-side worktree-validation glitch surfaced twice (#12, #14) with identical recovery.** β tried to set up an isolated worktree to validate cycle merges, hit the "current working directory: No such file or directory" race after cleanup, recovered in the same session. Non-fatal in both cases; no β rule violation; β APPROVED cleanly afterward. Class: probable β skill local-to-cph or a worktree-strategy edge case. Worth a future cycle to instrument or eliminate — not material at the wave level.

No empirical overclaim. No data policy regression. No silent rewrites of charter content by Sub D's α (sweep diff = self-coherence only).

## Wave-internal disconnect posture

This wave **does not produce a release tag.** No version bump, no `RELEASE.md`, no `scripts/release.sh` invocation. The disconnect signal is the four merge commits + the wave's own `wave-closeout.md` landing on main. Per the wave manifest's standing permissions, tag/release is operator-gated and was explicitly NO at wave open; the wave honored that.

The `.cdd/unreleased/{12,13,14,15}/` directories remain in `.cdd/unreleased/` — they do **not** move to `.cdd/releases/{X.Y.Z}/{N}/` at this wave's close because the cph repo has no release-cut for this wave. Future release work (if any) inherits these unreleased directories as part of its scope.

## Master closure

Master cph#11 remains **OPEN** at wave close. The wave manifest declared master closure as a separate δ action ("not by this wave's automatic action"). All 10 ACs from #11 are met; all 4 subs are closed; the wave-closeout is on main. Operator (δ in the originating conversation) holds the master-close decision.

Recommended closure comment for cph#11: a one-comment summary linking to this wave-closeout, the four merge commits, and the four sub-issues; close with `Closes #11`.

## Out-of-scope follow-ups (named, not executed by this wave)

Carried forward verbatim from the wave manifest:

- Update of `usurobor/cnos:.cdd/iterations/cross-repo/gait-support-paths/bootstrap-cdr/` to the new repo name (`cph`). Cross-repo work owned by cnos-side δ.
- Merge decision for `origin/cycle/segmentation-real-data-fix` (orthogonal review thread; tip `a95415c`).
- Hybrid-mode TSC coherence runs. This wave's `scripts/measure-coherence.sh` (AC6) is mechanical-only by design.
- Body edit of cph#11 (left intact as as-filed snapshot; rename context lives in cph#11 comment + `.cdd/iterations/cross-repo/cnos/bootstrap-cdr/LINEAGE.md`).
- First mechanical TSC measurement run + recording into `CHANGELOG.md` (the `0.1.0-cdr` baseline entry carries `C_Σ: pending — coh unavailable` placeholders to be filled when `coh` is on PATH in the operator's environment).
- Triage of the four cross-sub observations above into either skill patches or follow-on issues.

## Dispatch infrastructure observations

Two infrastructure observations from this wave's δ-as-agent execution that may inform future waves:

- **Monitor filter iteration.** The v1 `grep -aoE` filter was OOM-killed on JSONL events containing large file contents. v2 was python-based but too broad (matched "REVISE" / "verdict" / "APPROVED" inside file content read by α/β, not just in commit-push lines). v3 anchored on `[branch hash]` push-line shape and merge-strategy phrase — clean across cycles #14 and #15. The v3 pattern is durable for future cph waves under this configuration. Lives at `/tmp/cph-wave/scripts/wave-filter.py`.
- **Single working-tree dispatch is correct under `claude -p`.** Cycles A/B/C are declared parallelizable by file-disjointness in the manifest, but a shared `/root/cph` working tree forces serial execution per `operator/SKILL.md` §5.1. The wave honored serial dispatch; no working-tree corruption. A future wave wanting true cross-cycle parallelism would need per-cycle clones or `Agent(isolation: "worktree")` semantics.

---
_End of wave close-out._
