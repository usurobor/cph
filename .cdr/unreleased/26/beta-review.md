# β review — cph#26 — Port segmentation-real-data-fix onto current main

## Round 1

- **Round:** 1
- **SHA reviewed:** `bb85aae` (HEAD of `cycle/port-segmentation-fix`); α's named implementation SHA is `c5cf241` (last code-touching commit before §Review-readiness; readiness/gate commits `b374652`/`bb85aae` are self-coherence appends only).
- **Base SHA (origin/main):** `ebd909c` (re-fetched synchronously at review-base computation time per β/SKILL.md Role Rule 1).
- **Identity:** `beta@cph.cdd.cnos`.
- **Verdict:** **APPROVE.**

## §3.11b — γ-artifact presence

`.cdr/unreleased/26/` carries only `self-coherence.md`; no `gamma-scaffold.md`. The cph project operates in γ=δ collapse mode (per dispatch prompt context — "no separate γ-scaffold expected"), and the issue body itself (`gh issue view 26`) is the dispatched coordination artifact for this cycle. Recorded as a **non-binding configuration-floor observation**; no protocol-compliance finding.

## AC verification

### AC1 — Detector fix is ported — **PASS**

`scripts/segmentation.py::detect_heel_strikes` (HEAD = `bb85aae`) contains the robust-percentile + stance-region-gating detector:

```text
$ git show HEAD:scripts/segmentation.py | grep -nE 'def detect_heel_strikes|q05|q95'
41:def detect_heel_strikes(heel_y: np.ndarray, fs: float,
51:    of `yn < stance_thr` (where `yn = (smoothed_heel - q05) / (q95 - q05)`)
88:    q05 = float(np.percentile(smooth, 5))
89:    q95 = float(np.percentile(smooth, 95))
93:    yn = (smooth - q05) / amp
```

The threshold/length constants are parameter defaults (not literal `<` comparisons against numbers, so my initial regex against `< 0\.30` / `< 0\.10` / `>= 150` returned empty — α's surface description still holds; the comparisons happen via the named parameters):

```text
44:                        stance_thr: float = 0.30,
45:                        deep_thr: float = 0.10,
46:                        min_stance_s: float = 0.15) -> np.ndarray:
95:    min_stance_n = max(3, int(min_stance_s * fs))   # ⇒ 0.15 s × fs samples
96:    below = yn < stance_thr                          # ⇒ yn < 0.30
106:        if (e - s + 1) < min_stance_n:              # ⇒ length ≥ 150 ms
109:        if float(np.min(seg)) > deep_thr:           # ⇒ ≥ 0.10 depth gate
111:        deep_idx = np.where(seg < deep_thr)[0]
```

Quality_flag tri-value (cph#22 preservation): the initial regex `'quality_flag\s*=\s*"'` missed because the dataclass annotation at L38 reads `quality_flag: str = "ok"` (colon-syntax) and the emission at L165 uses a keyword-arg form. Direct inspection:

```text
38:    quality_flag: str = "ok"
165:                quality_flag=("short" if duration <= 0.5
166:                              else "long" if duration >= 1.8
167:                              else "ok"),
```

All three literals (`"ok"`, `"short"`, `"long"`) preserved through the 3-way port. **AC1 PASS confirmed.**

### AC2 — Notebook reruns on real data — **PASS**

Per the prompt, no re-execution needed; I inspected cell outputs in `notebooks/existing-data-processing.ipynb` directly via Python:

```text
cell 3: Found 60 walking trials from Mocap IK under /opt/gait-data/opencap-lab-validation/extracted
        Total trials: 60   by condition: {'walking': 30, 'walkingTS': 30}
        subjects: 10  (trials per subject: min=6 max=6 mean=6.0)
cell 6: Walking trials: 60   Trials with ≥1 cycle: 60
        Segmentation rate: 100.0%   (GO ≥80%, NO-GO <60%)
cell 16: Paired comparisons: 1080 rows (3 sources × ~60 trials × 6 joints)
cell 17: Mean Pearson r across joints, per source:
           HRNet_5cam                       : r̄ = 0.962  (GO ≥ 0.7)
           OpenPose_default_5cam            : r̄ = 0.933  (GO ≥ 0.7)
           OpenPose_highAccuracy_5cam       : r̄ = 0.951  (GO ≥ 0.7)
cell 19: pyarrow unavailable; wrote CSV instead: /opt/gait-data/cph-features/features-zeroth-pilot.csv
         Aggregate summary written to /root/cph/analysis/feature-summary-zeroth-pilot.md
```

Real-data path (`/opt/gait-data/opencap-lab-validation/extracted`) confirmed by the discovery cell; no synthetic-fallback marker present. **AC2 PASS.**

### AC3 — Evidence matches branch-level result — **PASS**

Independently re-grepped `reports/field-report-01-existing-data-zeroth-pilot.md` for each of the 12 quantities in α's §AC3 table:

| Quantity | Field-report-01 line | Match |
|---|---|---|
| 60 trials | L47 ("**60**") | ✓ |
| 60/60 R-seg | L47, L56, L57 | ✓ |
| 1 L-cycle | L8, L47, L57 (`1 / 60 (1.7%)`) | ✓ |
| 61 total cycles | L8 ("All 61 cycles"), L16, L47 ("61 cycles"), L79, L88 | ✓ |
| 60 R + 1 L | L8, L47 | ✓ |
| 30/30 natural | L45 | ✓ |
| 30/30 trunk-sway | L46 | ✓ |
| 0.00% missingness | L88, L179, L195 | ✓ |
| r̄ 0.962 HRNet | L96 | ✓ |
| r̄ 0.933 OpenPose_default | L97 | ✓ |
| r̄ 0.951 OpenPose_highAccuracy | L98 | ✓ |
| 35 columns | L88, L179 | ✓ |

All 12 quantities line up with notebook output. **AC3 PASS — no drift to explain.**

### AC4 — Decision remains REVISE — **PASS**

Empirical-state surfaces:

- `PROJECT.md` L20 — "**REVISE** (2026-05-17 segmentation-fix run, …)"
- `ROADMAP.md` L13 — "**R1 is REVISE**"
- `ROADMAP.md` L44 — R1 **Status: REVISE**
- `ROADMAP.md` L54 — R2 **Status: GO** (detector-level; permitted per α's instruction and ROADMAP §R2 next-action which keeps R1 REVISE)
- `CHANGELOG.md` L7 — §0.3.0 §Empirical state **REVISE**
- `reports/field-report-01-existing-data-zeroth-pilot.md` L22 — "REVISE, not GO" with the L=1 cycle constraint named
- `docs/concepts/coherence-path-hypothesis.md` L118 — **REVISE**

The R2→GO transition is bounded to the detector level and explicitly does not flip the construct-level R1 verdict (ROADMAP L46 "R2 has closed GO at the detector level. R1 remains REVISE…"; ROADMAP L55 names "Reading R2 GO as removing the R1 REVISE constraint" as a coherence risk). **AC4 PASS.**

### AC5 — Current repo surfaces preserved — **PASS**

```text
$ git diff origin/main..HEAD -- README.md
(empty)

$ git diff origin/main..HEAD --name-only | grep -E '^(targets/|scripts/measure-coherence|\.github/workflows/coherence)'
(empty)
```

`docs/concepts/coherence-path-hypothesis.md` patch is **bounded to §"Current empirical status" (L116–125 only)**: 4 insertions / 4 deletions, all within the empirical-state paragraph. The conceptual framing sections — §Governing question, §Definition, §What counts as evidence, §What does not count as evidence, §Relationship to support path, §Relationship to the seven gait families, §Basis and lineage, §Operationalization, §Falsification conditions, §Practical consequences if supported, §What would still remain unproven — are untouched.

α's "Round-1 RC risk surface" flagged this as the closest-to-boundary patch. My read: the §"Current empirical status" subsection is peer to PROJECT/ROADMAP/CHANGELOG (an empirical-state surface, not the conceptual framing of CPH) and the patch only refreshes the post-fix segmentation numbers + Hypothesis-testability paragraph. The "What it would falsify" / "Falsification conditions" sections — which AC5 nominally protects — are untouched. **AC5 PASS; no RC.**

### AC6 — No data policy regression — **PASS**

```text
$ git ls-files | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$' || echo NONE
NONE

$ git diff origin/main..HEAD --name-only | grep -E '\.(zip|trc|mot|sto|c3d|osim|mp4|mov|csv|parquet)$' || echo NONE
NONE
```

The features CSV is written to `/opt/gait-data/cph-features/features-zeroth-pilot.csv` (outside the repo). PNG plot bytes inside the .ipynb are derived visualizations, not raw participant data. **AC6 PASS.**

## β additional verification

### 1. Schema↔code peer enumeration (fix-round 1)

`grep -nE 'out\[' scripts/features.py` enumerates the emissions, including:

- L88 `out[f"{label}_range_deg"]` / L89 `_peak_deg` / L90 `_min_deg` — driven by the joint_map (`hip_flexion`, `hip_adduction`, `knee_angle`, `ankle_angle`)
- L94 `out[f"{pelvis}_range_deg"]` for `pelvis_tilt/list/rotation`
- L98 `out[f"{trunk}_range_deg"]` for `lumbar_bending/rotation/extension`

`analysis/feature-table-schema.md` L42 now lists all four joints (`hip_flexion`, `hip_adduction`, `knee_angle`, `ankle_angle`), the three pelvis axes, **and** the three trunk axes — matching what features.py actually emits. `analysis/features.md` §"Range / amplitude" L49–60 mirrors the same realized set; §"Candidate range/amplitude features" L92 carries the parenthetical that hip ab/adduction + lumbar are now realized (cph#26) and is no longer listed as unimplemented. **Peer enumeration consistent.**

### 2. Intra-doc repetition rule (§2.3) cross-doc check

`60/60 R; 1 L; 61 cycles` tuple verified across PROJECT.md L20+L42 / ROADMAP.md L13+L42+L52 / CHANGELOG.md L7+L16+L17 / field-report-01 L8+L16+L45–47 / coherence-path-hypothesis.md L123. Consistent.

Stale-reference sweep for `18.3%` / `11/60` / `11 of 60` against live surfaces:

```text
CHANGELOG.md:18:        "supersedes the 18.3%-segmentation REVISE"        (historical-context; CHANGELOG 0.3.0 §changed pointer)
reports/field-report-01:5:   "supersedes the same-day 18.3%-segmentation REVISE"  (history line)
reports/field-report-01:192: "18.3% | **100.0%** | ✓"   (delta table; prior vs current)
reports/field-report-01:247: "Second REVISE posted on the back of 18.3% segmentation"  (history)
```

All four occurrences are explicitly historical-context references (the prompt names CHANGELOG 0.3.0 §changed + field-report-01 §History as acceptable). No stale live claims. **Clean.**

### 3. α identity discipline (§2.6 row 14)

```text
$ git log origin/main..HEAD --format='%h %ae' | grep -v 'alpha@cph.cdd.cnos' || echo CLEAN
CLEAN
```

All 12 cycle commits (`2392ef3`, `822ba6e`, `bb0ee76`, `c13eec3`, `1c7fed0`, `beebcca`, `c5cf241`, `1078dea`, `b374652`, `bb85aae`, plus the two implementation commits `9bcef90` and `f27904a`) author as `alpha@cph.cdd.cnos`. No `δ-as-agent` or `epsilon` survivors. Path (a) retroactive correction held; no re-rewrite needed (per β constraint: history is sealed).

### 4. Self-coherence completeness

`.cdr/unreleased/26/self-coherence.md` carries:

- §Gap (L3–18)
- §Skills (L20–34)
- §ACs (L36–170, with AC1–AC6 each evidenced)
- §Self-check (L172–186)
- §Debt (L188–212)
- §CDD-Trace (L214–266, through step 7 + step-by-step ledger of 21 rows)
- §Fix-round 1 — peer-enumeration (L268–310, with F1–F9)
- §Pre-review gate (L312–333, 14 rows; PASS)
- §Review-readiness (L335–363, round 1)

All sections present. Transient rows 1 + 10 of the pre-review gate are re-validated under §Review-readiness. **Complete.**

## Findings

**None.** All six ACs pass on independent oracle re-runs; peer enumeration is coherent; identity discipline is clean; the empirical posture is REVISE on R1 with the R2→GO transition cleanly bounded to the detector level.

## Verdict

**APPROVE.** Proceeding to merge `cycle/port-segmentation-fix` → `main` with `--no-ff` (preserving α's commit history including the §2.6 row 14 identity-rewrite trail), then push, then delete the cycle branch from origin per the wave manifest convention.
