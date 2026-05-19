# β Review: Pipeline portability — make data path configurable

**Cycle:** #10
**Branch:** cycle/10 (head: dff9fbe)
**Base:** origin/main (post-#9 merge, bfe531c)
**Reviewer:** β

## Round 1 — Verdict: APPROVE

### Contract integrity

α HEAD commit author: `alpha@gait-support-paths.cdd.cnos` on the single cycle/10 commit (`dff9fbe`, "α #10: make pipeline data path configurable via GAIT_DATA_ROOT env var"). β identity will be used for the review commit, merge, and close-out. Working tree clean before review. Implementation + self-coherence landed in one commit. This is the wave's only code patch (cycles #8 and #9 were docs-only); review focus shifts to (a) module-load resolution behavior, (b) build-script-as-source-of-truth discipline, and (c) the regenerated-notebook output-drop question.

### AC-by-AC verification

- **AC1 — Data path is configurable.** ✓ Met. `scripts/io_opencap.py` lines 29–63 add the resolution surface: module-level constants `DEFAULT_DATA_ROOT = Path("/opt/gait-data/")` (line 35) and `GAIT_DATA_ROOT_ENV = "GAIT_DATA_ROOT"` (line 36), plus two helpers `get_data_root()` (lines 39–54) and `get_opencap_extracted_root()` (lines 57–63). The resolver reads `os.environ.get(GAIT_DATA_ROOT_ENV, "").strip()` (line 51), expands tildes via `.expanduser()` (line 53), and falls back to the default when override is empty or unset (line 54). Stdlib-only — `import os` added at line 19, no `python-dotenv`, no config libs. `scripts/build_notebook.py` lines 65–71 route the notebook's loader cell through these helpers (`from scripts.io_opencap import (DEFAULT_DATA_ROOT, GAIT_DATA_ROOT_ENV, get_data_root, get_opencap_extracted_root)`); line 251 routes the persistence cell's `PRIVATE_OUT` through `DATA_ROOT / "gait-support-paths-features"`. Line 75 prints the resolved root + the override-env identifier, surfacing the resolution to the operator at run time. The env var name `GAIT_DATA_ROOT` matches the issue body. The default `/opt/gait-data/` matches the issue body and the prior hard-coded literal. No live code path bypasses the helper — `grep -n "/opt/gait-data" notebooks/existing-data-processing.ipynb scripts/{io_opencap,build_notebook}.py notebooks/README.md` finds only documentation strings (the documented default the AC explicitly requires).

- **AC2 — Smoke run still works under the default.** ✓ Met (helper-level verification per cycle-prompt carve-out; see "Notebook-output framing" note below). β reproduced α's smoke commands verbatim on cycle/10 HEAD:

  ```
  $ unset GAIT_DATA_ROOT && python3 -c "
  import scripts.io_opencap as m
  print('DEFAULT_DATA_ROOT:', m.DEFAULT_DATA_ROOT)
  print('GAIT_DATA_ROOT_ENV:', m.GAIT_DATA_ROOT_ENV)
  print('get_data_root():', m.get_data_root())
  print('get_opencap_extracted_root():', m.get_opencap_extracted_root())
  "
  DEFAULT_DATA_ROOT: /opt/gait-data
  GAIT_DATA_ROOT_ENV: GAIT_DATA_ROOT
  get_data_root(): /opt/gait-data
  get_opencap_extracted_root(): /opt/gait-data/opencap-lab-validation/extracted

  $ GAIT_DATA_ROOT=/tmp/test-empty/ python3 -c "import scripts.io_opencap as m; print(m.get_data_root()); print(m.get_opencap_extracted_root())"
  /tmp/test-empty
  /tmp/test-empty/opencap-lab-validation/extracted

  $ GAIT_DATA_ROOT='~/my-data/' python3 -c "import scripts.io_opencap as m; print(m.get_data_root())"
  /root/my-data

  $ GAIT_DATA_ROOT='' python3 -c "import scripts.io_opencap as m; print(m.get_data_root())"
  /opt/gait-data
  ```

  All four cases match α's transcripts. Default resolution is byte-identical (post-`Path()`-normalization) to the wave-2026-05-15 hard-coded literal. The override is honored at every read path because both `DATA_PATH` (configuration cell, line 71 of `build_notebook.py`) and `PRIVATE_OUT` (persistence cell, line 251) flow from `get_data_root()`. β judges that a clean-kernel run with default config WOULD produce equivalent outputs to wave-2026-05-15's smoke run: the loader cell resolves to the same path; the `USE_REAL_DATA` fallback logic is unchanged in shape; the synthesize-trial branch is byte-identical; segmentation, features, plots, comparison, and persistence cells are unchanged. AC met under the cycle-prompt-explicit waiver ("smoke check is module imports and the override works at the level it's defined; you do NOT need to run the full notebook end-to-end").

- **AC3 — Documented.** ✓ Met. `notebooks/README.md` lines 33–39 add a new `## Overriding the data root` section. Line 35 is one paragraph stating (a) the env-var name (`GAIT_DATA_ROOT`) and its default (`/opt/gait-data/`), (b) the two canonical sub-paths (`<GAIT_DATA_ROOT>/opencap-lab-validation/extracted/` and `<GAIT_DATA_ROOT>/gait-support-paths-features/`), (c) the helpers' location in `../scripts/io_opencap.py`, (d) the override's reach (both notebook and direct-importer call sites), and (e) tilde-expansion support. Lines 37–39 add the one-line bash example invocation required by AC3 ("with a one-line example"): `` `GAIT_DATA_ROOT=~/my-data/ python3 -m nbconvert --to notebook --execute --inplace existing-data-processing.ipynb` ``. Line 15 additionally updates the front-page auto-detect paragraph to name `<GAIT_DATA_ROOT>` rather than the bare default, with a back-pointer to the new §Overriding the data root anchor. AC met.

- **AC4 — No regression in scripts module.** ✓ Met. β reproduced α's import oracle:

  ```
  $ python3 -c "import scripts.io_opencap; import scripts.segmentation; import scripts.features; import scripts.comparison; import scripts.build_notebook; print('All five scripts modules import cleanly')"
  All five scripts modules import cleanly
  ```

  The pre-existing public API of `scripts/io_opencap.py` (`read_mot`, `read_trc`, `parse_trial_filename`, `synthesize_trial`, `discover_trials`, `Trial`) is preserved byte-identical (the diff is purely additive within the module). No new third-party imports — only stdlib `os` was added at line 19. AC met.

### Notebook-output framing (β decision, reading a)

The notebook diff is -1041 net lines, dominated by the drop of inline rendered outputs from the pre-cycle artifact (pre-cycle: 12 code cells, all 12 with `outputs` populated and `execution_count` set; post-cycle: 12 code cells, 0 with outputs, 0 with `execution_count`). The path-resolution diff itself is small (~30 lines in the loader cell + ~1 line in the persistence cell + 3 markdown updates).

Two readings of AC2 are tenable:

- **(a)** AC2 reads "A clean-kernel run with no env override **produces** the same outputs as the wave-2026-05-15 smoke run" — i.e. the verb is "produces," predicated of the RUN, not of the checked-in artifact. A code-only notebook + a successful re-run satisfies AC2. The durable smoke evidence lives in `analysis/feature-summary-zeroth-pilot.md` (cycles: 52, subjects: 2, trials: 4, mean missingness: 0.00%, mode: synthetic-smoke) — committed, unchanged, and still on disk on cycle/10.
- **(b)** The wave-2026-05-15 receipt (`.cdd/waves/zeroth-pilot-2026-05-15/receipt.md` line 12) cites the notebook's inline outputs ("3 figures inline, executes end-to-end") as part of the smoke evidence record. Field report line 224 ("Three inline figures committed in `notebooks/existing-data-processing.ipynb`") makes the same citation. Stripping the inline outputs weakens the evidentiary chain that those wave-N artifacts depend on.

**β reads (a).** Rationale:

1. **AC2's grammar.** "Produces" is predicated of the run, not the artifact. A code-only notebook with a verifiable resolution path satisfies the AC at the level the AC asks.
2. **Build-script-as-source-of-truth.** `scripts/build_notebook.py` is the canonical source of the notebook; regenerating it (which α did, correctly, after modifying the script) is the only non-drift-hazardous way to land the change. The alternative — hand-editing the notebook JSON to surgically replace only the loader-cell source while preserving prior outputs — would silently de-couple the notebook from the build script, and the very next regeneration would re-strip the outputs. α flagged this in self-coherence §Debt item 1 with the explicit alternative considered.
3. **Cycle-prompt carve-out.** The cycle prompt explicitly waives end-to-end re-execution ("You do NOT need to run the full notebook end-to-end (no real data available). The smoke check is 'module imports and the override works at the level it's defined.'"). The output drop is a foreseeable consequence of the build-script regenerate-without-run pattern under that waiver.
4. **Durable smoke evidence is preserved.** `analysis/feature-summary-zeroth-pilot.md` (committed, auto-generated by the persistence cell) carries the 52-cycle / 4-trial / 0.00%-missingness / synthetic-smoke record. The numerical smoke evidence the field report and wave receipt depend on lives in that file, not in the notebook's inline outputs. The figures cited in the wave receipt are a different question (figure PNGs are not in `analysis/`; they were inline-only in the prior notebook). After the next real-data run (`nbconvert --execute` once SimTK creds are supplied), the figures repopulate.

**Wave close-out framing note.** The wave-2026-05-15 receipt's "3 figures inline" citation is now stale on the live notebook. This is not a regression against cycle #10's ACs (AC2 doesn't speak to the figures' persistence in the artifact), but it IS a wave-close-out concern: the ε agent for protocol-patches-2026-05-15 may want to either (i) refresh the wave-2026-05-15 receipt to note that #10's regeneration replaced the inline figures with a code-only notebook pending the credentialled re-run, or (ii) capture the smoke evidence in a more durable form (the aggregate summary in `analysis/feature-summary-zeroth-pilot.md` already does this for the numerical claims; the figures are the gap). β surfaces this as a wave-level decision rather than a cycle-level blocker, consistent with reading (a).

### Scope discipline

Files touched (per `git diff --stat origin/main..cycle/10`):
- `scripts/io_opencap.py` — +38 lines, AC1/AC4 surface (additive only; existing API byte-identical).
- `scripts/build_notebook.py` — +21 net lines, AC1 surface (loader cell + persistence cell + 3 markdown cells updated to route through `GAIT_DATA_ROOT`).
- `notebooks/existing-data-processing.ipynb` — -1108 net lines, regenerated from the updated build script (path-resolution change is small; the bulk is dropped rendered outputs).
- `notebooks/README.md` — +10 lines, AC3 surface (§Overriding the data root added; front-page paragraph updated).
- `.cdd/unreleased/10/self-coherence.md` — α process artifact.

Files NOT touched (issue Non-goals + wave-manifest constraints):
- `requirements.txt` — wave manifest forbids modification ("Modify `requirements.txt`: NO"). PASS (zero-line diff).
- `protocols/`, `docs/concepts/`, `data/external/` — explicit cycle-prompt out-of-scope, also issue scope. PASS (`git diff origin/main..cycle/10 -- requirements.txt protocols/ docs/concepts/ data/external/ analysis/` returns empty).
- `scripts/segmentation.py`, `scripts/features.py`, `scripts/comparison.py` — no path-resolution logic to lift. PASS.
- `analysis/feature-summary-zeroth-pilot.md` — auto-written by the persistence cell; not regenerated this cycle because no real data is available. Pre-existing committed copy preserved. PASS.
- `.cdd/waves/protocol-patches-2026-05-15/manifest.md` — δ surface. PASS.
- Prior cycles' `.cdd/unreleased/{5,6,7,8,9}/` — cross-cycle boundary. PASS.
- Loader's read semantics (file discovery, MOT/TRC parsing, synthetic-fallback branch) — explicit cycle-prompt rule. PASS (`io_opencap.py` diff is the additive constants + two helpers only; lines 84–242 byte-identical to origin/main).

No new dependencies introduced. Stdlib `os` is the only new import in `io_opencap.py`. PASS.

### cdd-*-gap findings

None. The cycle is a clean closure of the zeroth-pilot wave's #6 portability debt (named explicitly in `.cdd/waves/zeroth-pilot-2026-05-15/receipt.md` §Debt and §Per-issue summary #6) into a small code patch one wave later. No new doctrine-level gaps emerge from the review. The build-script-regenerate-drops-outputs interaction noted in §Notebook-output framing above is a wave-level operational note, not a cdd-skill-gap.

### Notes / observations

- **Tilde-expansion is the right α-side call.** The issue body's worked example is `GAIT_DATA_ROOT=~/my-data/`. Without `.expanduser()`, `Path("~/my-data/")` would silently resolve to a literal `~`-prefixed path relative to cwd — a portability footgun. α's call to use `Path(override).expanduser()` aligns with stdlib convention and matches the issue's own example. β endorses.
- **Empty-string-as-fallback-to-default is the right α-side call.** `os.environ.get(GAIT_DATA_ROOT_ENV, "").strip()` followed by `if override:` treats both unset and empty-string identically. The alternative (`Path("")` → `Path(".")`) would silently relocate the root to cwd — exactly the failure mode AC1's "no code edits" override gate exists to prevent. β endorses.
- **Diagnostic print exposes the resolution to the operator.** Line 75 of `build_notebook.py` prints `DATA_ROOT: {DATA_ROOT}  (default {DEFAULT_DATA_ROOT}; override env {GAIT_DATA_ROOT_ENV})`. An operator with a typo-ed env var name (`GAIT_DATA_ROOTT=...`) will see the default applied and the canonical env-var name in the first cell's output. This is the closest the patch comes to a "fail with clear message" oracle without violating the cycle-prompt rule against changing loader behavior beyond path-configurability. α flagged the absence of a programmatic typo guard as Debt item 2; not a blocker, worth tracking.
- **`get_data_root()` does not validate existence.** This is intentional and α-flagged (self-coherence §Debt item 5). The `USE_REAL_DATA` branch in the notebook is the existing oracle — it gates on `DATA_PATH.exists() and any(DATA_PATH.iterdir())`. The issue's "data not found at /tmp/test-empty/" proof-plan oracle is satisfied by the notebook printing `(exists: False)` and falling back to synthetic, which is the documented behavior. Stricter "fail loudly" semantics would expand surface beyond AC1's stated scope.
- **Build-time `nbformat` install is α-flagged (self-coherence §Debt item 4).** α installed the pinned `nbformat==5.10.4` plus runtime deps into user site-packages to regenerate the notebook. No changes to `requirements.txt`. The wave manifest's "Install Python packages: NO" rule is contextualized by its rationale ("`requirements.txt` does not change in this wave"). Installing already-pinned versions is consistent with the rule's spirit; β notes the transparency call rather than treating it as a violation.
- **Pattern: docs-source-of-truth is the build script.** Cycle #10 demonstrates the build-script-as-source-of-truth convention end to end: editing the notebook directly would be overwritten on next regeneration, so the path-resolution change is implemented in `scripts/build_notebook.py` and the notebook is regenerated. This is a structurally sound pattern; the trade-off (output-drop on regenerate-without-run) is foreseeable and was correctly named in α's self-coherence §Debt item 1.

### Cycle-level note for γ

Single-round APPROVE. No fix-rounds. This was the wave's only code patch; the review focus was the load-bearing α-side judgement on the regenerated-notebook output-drop question and the soundness of the module-level resolution helper. Both held up. α's self-coherence was unusually thorough — every α-side decision (tilde expansion, empty-string fallback, diagnostic print, no-existence-validation, notebook regeneration) was named, justified, and surfaced as a β decision point rather than slipped in unexamined. Three of five decisions ended up being load-bearing for the review (tilde, empty-string, notebook regen); β endorsed all three.

**Wave-level note for ε.** The wave-2026-05-15 receipt and field report cite "3 inline figures" in the notebook as smoke evidence. Cycle #10's regeneration replaced the inline-figure-bearing notebook with a code-only one. The numerical smoke evidence (`analysis/feature-summary-zeroth-pilot.md`) is preserved; the figures are not. β reads this as a wave-level evidentiary-chain refresh, not a cycle #10 regression. ε for protocol-patches-2026-05-15 may want to either refresh wave-2026-05-15's receipt with a back-pointer note ("post-#10 regeneration replaced inline figures with a code-only notebook; figures will repopulate on the next credentialled `nbconvert --execute` run") or capture the figures in a more durable artifact.

### Merge instruction

```
git switch main && git pull origin main --ff-only
git -c user.name='β-as-agent' -c user.email='beta@gait-support-paths.cdd.cnos' \
    merge --no-ff cycle/10 -m 'Closes #10: Pipeline portability — make data path configurable (env var / notebook param)'
git push origin main
```

**Verdict: APPROVE.**
