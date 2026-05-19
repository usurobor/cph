# Wave Close-out: Existing-data zeroth pilot

**Wave date:** 2026-05-15
**Dispatcher:** δ-as-agent (single-actor collapse mode)
**Repo:** usurobor/gait-support-paths
**Parent issue:** #4 (closed manually after subs closed — see β #7 F1)
**Sub issues:** #5, #6, #7 (all CLOSED)
**Final SHA on main:** c739b98

## Final wave decision

**REVISE for friend pre-pilot.**

The wave's methodological foundation (selection rules, processing protocol, falsification framework, GO/NO-GO criteria) is sound; the pipeline (segmentation, feature extraction, comparison, plotting) is implemented, smoke-tested, and reproducible. The blocking constraint is a single procedural gap: the chosen dataset (OpenCap Lab Validation, Apache 2.0 licensed) requires an authenticated SimTK account to download, and the wave's standing permissions did not include operator-supplied credentials.

REVISE rather than NO-GO because none of the protocol's NO-GO conditions is empirically triggered — they are *not yet testable* on the synthetic smoke data used in #6. REVISE rather than GO because GO requires real-data validation that has not been performed.

**Recommended revision:** update `protocols/existing-data-zeroth-pilot.md` to add an "Access mechanism" subsection covering authentication/credential gates on candidate datasets, plus an operator-acquisition runbook (the current draft lives in `data/external/opencap-lab-validation.md §Acquisition procedure`). After acquisition, re-execute `notebooks/existing-data-processing.ipynb` and re-evaluate the GO/NO-GO criteria.

## Per-issue summary

### #5 — Sub A: Acquire dataset + manifest
- **Rounds:** 1
- **Verdict:** APPROVE
- **Final SHA on main:** d7c7444 (merge); fbcfbaf (γ close-out)
- **Key artifacts:** `data/external/opencap-lab-validation.md` (fully populated manifest, dataset selected: OpenCap Lab Validation, Apache 2.0); `.gitignore` (extended with `data/external/**` exclusions); `.cdd/unreleased/5/{self-coherence,beta-review,alpha-closeout,beta-closeout,gamma-closeout}.md`.
- **Debt:** Acquisition itself blocked at SimTK login gate (operator credentials required); speed-graduation partial (dataset has two coordination conditions at self-selected speed, not graded speeds); row-level walking-trial inventory blocked on download.

### #6 — Sub B: Pipeline
- **Rounds:** 2 (β R1 RC on `__pycache__/` commit; R2 APPROVE after fix)
- **Verdict:** APPROVE
- **Final SHA on main:** ced1425 (merge); 8997f6f (γ close-out)
- **Key artifacts:** `notebooks/existing-data-processing.ipynb` (full pipeline, executes end-to-end via nbconvert); `scripts/{io_opencap,segmentation,features,comparison,build_notebook}.py`; `requirements.txt` (pinned: numpy 2.4.4, pandas 3.0.3, scipy 1.17.1, matplotlib 3.10.9, nbformat 5.10.4, nbconvert 7.17.1, ipykernel 7.2.0); `notebooks/README.md` (rewritten); `analysis/feature-summary-zeroth-pilot.md` (auto-generated, smoke-mode marked); `.cdd/unreleased/6/{self-coherence,beta-review,alpha-closeout,beta-closeout,gamma-closeout}.md`.
- **Debt:** Real-data OpenCap-vs-reference pairing logic deferred (requires unzipped archive to verify file-naming convention); hard-coded `/opt/gait-data/` data path is a portability gap; hip ab/ad-duction features not in first-pass feature set; smoke-vs-real disclaimer must propagate to any downstream cycle.

### #7 — Sub C: Inference memo + field report + REVISE decision
- **Rounds:** 1
- **Verdict:** APPROVE
- **Final SHA on main:** a76b6d6 (merge); c739b98 (γ close-out)
- **Key artifacts:** `reports/field-report-01-existing-data-zeroth-pilot.md` (rewritten from template — 9 protocol outputs covered, 6-condition falsification table, REVISE decision); `PROJECT.md` (Current Stage + Realization 04 updated); `.cdd/unreleased/7/{self-coherence,beta-review,alpha-closeout,beta-closeout,gamma-closeout}.md`.
- **Debt:** Real-data hypothesis evaluation deferred to post-acquisition cycle; protocol revision (add "Access mechanism" subsection) intentionally out of this cycle's scope per issue non-goals; falsification table empirical-data prerequisite could be clarified in `docs/concepts/support-path.md`.

## Wave-level findings (cdd-*-gap patterns across cycles)

### Pattern 1 — Open license vs gated access mechanism

**Class:** `cdd-protocol-gap` for the project's protocol; not a CDD-method gap.

**Surface:** `data/external/opencap-lab-validation.md` (manifest documents the gap); `protocols/existing-data-zeroth-pilot.md §Dataset Selection Rules` (could be extended). Surfaced across #5 (α F1, β F1), #6 (inherited blocker), and #7 (β F2 in own close-out, α F2 in own close-out).

**Description:** A dataset can be permissively licensed (Apache 2.0, MIT, CC-BY) yet behind an account-gated download endpoint. The wave manifest's escalation rule was framed around "non-permissive license," which does not match this failure mode. The protocol's selection rules list "clear license" but not "open access mechanism." The result: a dataset that passes all four selection rules cannot actually be downloaded in a credentialless sandbox.

**Recommended patch:** Add an "Access mechanism" subsection to `protocols/existing-data-zeroth-pilot.md §Dataset Selection Rules` covering authentication/credential gates and what counts as "publicly accessible." Update the wave-manifest template (this file's `.cdd/waves/...` directory pattern) to broaden the escalation rule.

### Pattern 2 — Falsification framework requires empirical variation

**Class:** `cdd-skill-gap` candidate (project-specific) — `docs/concepts/support-path.md §"Falsification Conditions"`.

**Surface:** field report §Falsification Assessment; α #7 close-out F1.

**Description:** Five of six falsification conditions test for *absence of empirical variation* (no repeatable patterns; features uncorrelated with context; random L/R asymmetry; etc.). When applied to by-construction-coherent synthetic data, the score reads as "0/6 conditions triggered" which mechanically suggests GO. The framing distinction "not testable on smoke" vs "tested and not triggered" was load-bearing in α's correct call.

**Recommended patch:** Add a preamble to `docs/concepts/support-path.md §"Falsification Conditions"` noting that the table assumes empirical data; on synthetic / by-construction data, conditions return "not testable" rather than "not triggered."

### Pattern 3 — Multi-sub parent issue auto-close

**Class:** `cdd-tooling-gap` — wave-manifest convention.

**Surface:** wave manifest stated "Parent issue: #4 (auto-closes when all subs close)" — false assumption. GitHub's auto-close fires on `Closes #N` per merge commit, not on transitive sub-closure.

**Recommended patch:** Update wave-manifest template to either:
- (a) include the parent in each sub's merge-commit `Closes` list, or
- (b) explicitly state that γ closes the parent manually at wave close.

This wave used path (b).

### Pattern 4 — Python repo hygiene

**Class:** `cdd-tooling-gap` — generic Python project.

**Surface:** `.gitignore` missing `__pycache__/`; β #6 caught at R1.

**Recommended patch:** Project template — `.gitignore` for any Python-using repo should include `__pycache__/` and `*.pyc` from creation. This wave fixed it; future cycles inherit the fix.

## Sub-issue dependency chain — held cleanly

The cycle order #5 → #6 → #7 with declared dependencies was honored:
- #5 selected the dataset and documented the acquisition gap.
- #6 inherited the gap and built the pipeline for both real-data and synthetic-smoke paths; smoke-tested.
- #7 inherited the smoke-only status and called REVISE honestly, with three hypotheses and falsification paths ready to be evaluated post-acquisition.

No cycle pretended to have data it didn't have. No hypothesis was promoted past "candidate." The chain is intact.

## Authority bounds — observed

All actions taken matched the wave's standing permissions:
- ✅ Push to cycle/{N} branches — yes; cycles 5, 6, 7 all pushed.
- ✅ Push merges to main — yes; three merge commits with `Closes #N`.
- ✅ Auto-dispatch α fix rounds on β REQUEST CHANGES — used once (#6 round 2).
- ✅ Branch delete after merge — cycle/5, cycle/6, cycle/7 all deleted.
- ✅ Install Python packages and commit requirements.txt — yes; cycle #6.
- ❌ Tag/release — NONE created (operator gate, as per manifest).
- ❌ Commit raw participant data — NONE (no data was acquired; rule held vacuously).

## Escalations to operator

1. **SimTK access mechanism for OpenCap Lab Validation.** The dataset is Apache 2.0 permissive; SimTK requires a logged-in account for file downloads. Operator credentials needed to complete acquisition. Surfaced in `data/external/opencap-lab-validation.md` §Acquisition status + §Acquisition procedure.

2. **Wave-manifest escalation rule mismatch.** The manifest's escalation rule was framed as "If the candidate dataset has a non-permissive license, escalate." The actual failure mode (permissive license + gated access) does not match. Wave-manifest convention should be broadened — see Pattern 1 recommendation above.

## Known wave-level gaps

- Real-data acquisition + run is the load-bearing follow-up.
- Protocol revision (`Access mechanism` subsection) is recommended in the field report; the revision itself is a separate cycle.
- Falsification-table empirical-data prerequisite (Pattern 2 above) is a small documentation patch.
- Hip ab/ad-duction features (referenced by Hypothesis 2 in #7) need a feature-extraction extension once real OpenCap output columns are confirmed.

## Wave decision

**REVISE.** Methodology and pipeline are sound; the gating step is the dataset acquisition. With operator-supplied SimTK credentials (or substitution of a backup dataset without an access gate), the wave can re-run starting at #5's acquisition procedure, propagate through the existing #6 pipeline unchanged, and re-evaluate #7's falsification table with real numbers.

Friend pre-pilot remains contingent on a future GO outcome from the re-executed wave.
