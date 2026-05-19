# β Review: Sub A — OpenCap Lab Validation manifest

**Cycle:** #5
**Branch:** cycle/5 (head: 3f96ff7)
**Base:** main (0a65f7c)
**Reviewer:** β (beta@gait-support-paths.cdd.cnos)

## Round 1 — Verdict: APPROVE

### Contract integrity

α complied with all role constraints. Single named cycle branch. Self-coherence written in section order. Manifest is the primary output artifact; self-coherence is the secondary. Identity audit: HEAD commit is authored `alpha@gait-support-paths.cdd.cnos`. β identity confirmed.

### Issue contract (#5)

AC-by-AC re-verification:

- **AC1 (no placeholders):** PASS. Re-ran `grep -nE "to be specified|to be determined|to be documented|to be counted|to be calculated|Pending" data/external/opencap-lab-validation.md`. Exit code 1 (no matches). Mechanical oracle satisfied.

- **AC2 (selection rules):** PASS. The §"Selection-Rules Check" table enumerates four rules with met / met / met / partial-with-evidence. The "multiple speeds" rule is honestly marked partial — the OpenCap Lab Validation dataset has two coordination conditions (natural + trunk-sway) at self-selected speed, not a graded speed range. α's call to accept the partial and not invoke the backup-dataset fallback is defensible: protocol §"Dataset Selection Rules" lists multi-speed as one of four selection criteria, and the other three are fully met; the L/R-comparison purpose that the rule serves is delivered by trial repetitions. The partial does mean speed-graded findings are unavailable to Sub C; this is recorded honestly in §Debt.

- **AC3 (walking-trial inventory):** PASS-WITH-DOCUMENTED-PARTIAL. The manifest §"Walking Trials Identified" populates: 10 participants, 2 walking conditions, speed variations (self-selected, not graded), trial repetitions (estimated), gait-cycle count estimate (60–500 range). α's call: "AC met for the documentation-derived inventory; the row-level inventory is named as known debt to be appended when operator credentials are supplied." β-side judgment: the AC text reads "Required: number of participants, walking conditions, speed variations, trial repetitions, gait-cycle count estimate" — all five rows are populated, with the bottom three explicitly labelled as paper-derived estimates pending download. The AC does not literally require file-content-derived numbers; it requires the listed fields populated. A future cycle (or this manifest's appendix update once acquisition lands) will replace estimates with measurements. **Decision: AC met, with the row-level partial recorded as load-bearing debt for the wave.**

- **AC4 (raw data not committed):** PASS. `git log --diff-filter=A --name-only origin/main..origin/cycle/5 -- data/external/` returns no binary additions; the only `data/external/` change is the manifest itself (modified, not added). `.gitignore` was extended with `data/external/**/*.zip`, `*.trc`, `*.mot`, `*.c3d`, `*.sto`, `*.osim`, `*.csv`, `*.parquet`. Policy enforced going forward.

### Diff context

Three files touched. All three are inside `## Scope: In` of the issue (manifest + supporting policy). No file outside scope was modified.

### Architecture

The acquisition-procedure section at the bottom of the manifest is a useful addition not strictly required by the issue but coherent with the manifest's purpose: it gives the wave-operator a concrete unblock path. No structural concerns.

### Findings

None binding. One observation:

- **Observation O1 (informational, not blocking):** The wave manifest authorized "Download public OpenCap Lab Validation data to a local path outside the repo: yes" but the SimTK gate prevents anonymous download even though the license is Apache 2.0 permissive. This is a wave-level expectation mismatch, not a cycle-level finding. α surfaced it correctly in §Debt. Downstream subs (#6 pipeline, #7 inference) will inherit this block — γ should track this in the wave status and consider whether the wave's outcome is NO-GO at #7.

### Merge instruction

On approval (this is APPROVE), β will execute:
```
git switch main && git pull --ff-only
git merge --no-ff origin/cycle/5 -m "Closes #5: Sub A — Acquire OpenCap Lab Validation dataset and complete manifest"
git push origin main
```

No CI gate exists for this repo; the manifest + self-coherence are the integration surfaces.

### Cycle-level note for γ PRA

The cycle ran in 1 round, no fix-rounds, with one load-bearing debt entry that has implications for the rest of the wave. Engineering level reading: L6 — cross-surface coherence maintained (manifest + .gitignore + self-coherence + escalation path) even under an environmental block; system-shaping leverage (L7) was not in scope.

**Verdict: APPROVE for merge into main with `Closes #5` in the merge commit message.**
