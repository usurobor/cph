# Wave: CDR refactor (master #11)

**Date:** 2026-05-18
**Dispatcher:** δ-as-agent (γ=δ permitted at this scale per `cdd/operator/SKILL.md` §5.2)
**Repo:** usurobor/cph (renamed 2026-05-18 from `usurobor/gait-support-paths`; GitHub auto-redirects cover the old name)
**Master:** #11 (10 ACs; kind=enhancement; labels: enhancement, P2, cdd) — stays open until subs close
**Origin:** master #11 + rename context comment (cph#11 comment 4475887390) + `.cdd/iterations/cross-repo/cnos/bootstrap-cdr/LINEAGE.md` § "Repository rename event"
**Five-factor heuristic outcome:** split — strong signals on (a) ≥6 new files, (b) ≥4 modules touched, (e) charter / roadmap / infra / sweep all ship independently; partial signals on (c) lifecycle span and (d) MCA preconditions (mixed: design-and-build for charter, MCA-eligible for TSC infra).

## Issues (ordered; D depends on A+B+C)

| Order | # | Title | ACs from #11 | Mode | Type | Depends on |
|-------|---|-------|--------------|------|------|------------|
| 1 | 12 | Sub A — CDR charter docs (README + hypothesis + seven-families + CDR.md + source-of-truth init) | 1, 2, 4, 10 (initial) | design-and-build | docs | — |
| 2 | 13 | Sub B — CDR roadmap (ROADMAP.md, phases R0–R6) | 3 | design-and-build | docs | — |
| 3 | 14 | Sub C — TSC targets + measure-coherence.sh + CHANGELOG baseline + PROJECT.md repartition | 5, 6, 7 (+ PROJECT.md repartition supporting AC10) | MCA-eligible | infra + docs | — |
| 4 | 15 | Sub D — CDR refactor conformance sweep | 8, 9, 10 (final) | docs-only | sweep | #12, #13, #14 |

A/B/C are **parallelizable** — they touch disjoint file sets. D runs only after A+B+C close (or after the wave closes any of them as deferred — D's scope adjusts to the merged set).

### File-disjointness check (A/B/C)

- Sub A touches: `README.md` (rewrite); `docs/concepts/coherence-path-hypothesis.md` (new); `docs/articles/seven-ways-people-walk.md` OR `docs/references/seven-gait-families.md` (new — α picks one); `CDR.md` (new).
- Sub B touches: `ROADMAP.md` (new).
- Sub C touches: `targets/registry.tsc`, `targets/{hypothesis,method,evidence,repo}.tsc` (new); `scripts/measure-coherence.sh` (new); `CHANGELOG.md` (new); `PROJECT.md` (repartition / shrink).

Three of the four wave files A/B/C touch — `README.md` (Sub A), `ROADMAP.md` (Sub B), `PROJECT.md` (Sub C) — co-exist in repo root, but each sub modifies a disjoint file, so concurrent merges do not conflict. Sub C's `targets/hypothesis.tsc` *names* `README.md` / `CDR.md` / `ROADMAP.md` / hypothesis doc / etc. as canonical sources — the manifest is a forward reference; Sub C does not depend on A/B *merge*, only on the agreed file *path* (which the wave manifest pins below).

## Pinned file paths (forward-reference contract)

To allow Sub C to ship in parallel with Sub A/B without rebasing, the wave pins the following authoritative paths up-front. Sub A and Sub B MUST use exactly these paths; Sub C MUST reference exactly these paths in `targets/*.tsc`.

| Path | Owner | Notes |
|------|-------|-------|
| `README.md` | Sub A | Rewrite — file already exists |
| `CDR.md` | Sub A | New |
| `docs/concepts/coherence-path-hypothesis.md` | Sub A | New |
| `docs/concepts/support-path.md` | (existing) | Preserved; Sub A cross-references |
| `docs/concepts/gait-cycle-as-unit.md` | (existing if present) | Sub C `targets/hypothesis.tsc` includes only if present |
| `docs/concepts/failure-conditions.md` | (existing if present) | Same |
| Seven-gait-families doc | Sub A | Path is `docs/articles/seven-ways-people-walk.md` (preferred) — α may use `docs/references/seven-gait-families.md` only if it explicitly notes the change in self-coherence so Sub C can match in `targets/hypothesis.tsc` |
| `ROADMAP.md` | Sub B | New |
| `CHANGELOG.md` | Sub C | New |
| `PROJECT.md` | Sub C | Repartition (existing file) |
| `targets/registry.tsc`, `targets/hypothesis.tsc`, `targets/method.tsc`, `targets/evidence.tsc`, `targets/repo.tsc` | Sub C | All new |
| `scripts/measure-coherence.sh` | Sub C | New; executable; mechanical-mode only |

If the seven-gait-families file path changes during Sub A's authoring, α must update this manifest's row *and* notify Sub C's γ via a `gamma-coordination.md` entry on Sub C's cycle branch before Sub C signals review-readiness on `targets/hypothesis.tsc`.

## Standing permissions

- Push to `cycle/{N}` branches: yes
- Push merges to main: yes
- Auto-dispatch α fix rounds on β REQUEST CHANGES: yes (max 3 per sub)
- Tag/release: NO — operator gate
- Branch delete after merge: yes
- Install Python packages: NO (this wave does not touch `requirements.txt`)
- Modify `requirements.txt`: NO
- Run `coh` (TSC CLI) in CI: best-effort — Sub C's `scripts/measure-coherence.sh` AC6 says the script must fail clearly when `coh` is missing; producing `.tsc/` reports is preferred not required
- Cross-repo touches (`usurobor/cnos`): NO — out of scope; cnos bundle-path updates handled in a separate cnos-side task

## Timeout budgets

| Role | Sub A (charter) | Sub B (roadmap) | Sub C (TSC infra) | Sub D (sweep) | Rationale |
|------|-----------------|-----------------|-------------------|---------------|-----------|
| γ | 1200s | 1200s | 1200s | 1200s | §5.2 full-cycle γ minimum per `.cdd/iterations/wave-2026-05-12.md` finding #4 |
| α | 1500s | 900s | 1500s | 900s | Charter (Sub A) is the heaviest authoring load; TSC infra (Sub C) bundles 8 file touches; B and D are tightly scoped |
| β | 900s | 600s | 900s | 600s | Review surface scales with α output |

Sub C is MCA-eligible (master #11 specifies the TSC target manifest format and `measure-coherence.sh` shape); MCA cycles run 1–2 review rounds historically per `issue/SKILL.md`. Sub A is design-and-build with substantial narrative authoring; budget the larger α window for the charter narrative.

## Known constraints

- **Empirical REVISE posture (master #11 §10).** No sub may overclaim the Coherence Path Hypothesis. The latest merged field report governs README / ROADMAP / PROJECT / CHANGELOG empirical-state language. Sub D's AC8 sweep is the structural backstop.
- **Repository rename (2026-05-18).** Every new file created by this wave uses `cph` from first commit. GitHub auto-redirects cover any pre-rename URL still in active artifacts. Historical bundle files under `.cdd/iterations/cross-repo/cnos/bootstrap-cdr/` (and the comparable bundle in cnos) are **preserved verbatim** — this wave does not touch them.
- **Segmentation-fix branch.** `origin/cycle/segmentation-real-data-fix` (tip `a95415c`) is unmerged and orthogonal to #11. Wave cycle branches base on current `origin/main`, **not** on the segmentation tip. Merging the segmentation branch is a separate operator decision.
- **Cross-repo bundle paths in cnos.** `cnos:.cdd/iterations/cross-repo/gait-support-paths/bootstrap-cdr/` references the pre-rename name. Updating cnos-side paths is downstream cross-repo work and **explicitly out of this wave's scope**.
- **`cnos#376` Source Proposal block in cph#11.** Old repo name appears verbatim in the as-filed snapshot; references resolve via GitHub redirect. Left intact.
- **Identity-isolation invariant.** α ≠ β within a single sub (hard rule per `cdd/CDD.md` §1.4). γ = δ permitted at this scale per `cdd/operator/SKILL.md` §5.2.
- **Fix-round chain branches under §5.2 push restrictions.** If a harness blocks force-pushes to an existing remote branch, α may chain `cycle/{N}-impl-rN` per `operator/SKILL.md` §5.2(3). Each link is a valid cycle branch for that fix-round.

## Resumption / failure handling

- An α or β session that SIGTERMs before committing follows `cdd/operator/SKILL.md` §8 timeout-recovery.
- A sub closed as **failed** triggers γ to write a `gamma-coordination.md` entry on the master's tracking surface (a cph#11 comment naming the failed sub and why), and Sub D's scope adjusts at sweep time.
- A sub closed as **deferred** is named in master #11's closure comment as tracked debt; the master does not auto-close until all subs are terminal (closed or deferred).

## Out-of-scope follow-ups (named, not in this wave)

- Update of `usurobor/cnos:.cdd/iterations/cross-repo/gait-support-paths/bootstrap-cdr/` to the new name.
- Merge decision for `origin/cycle/segmentation-real-data-fix` (orthogonal review thread).
- Hybrid-mode TSC coherence runs (mechanical only this wave per Sub C AC6).
- Body edit of cph#11 (left as as-filed snapshot; rename context lives in comment + LINEAGE.md).
