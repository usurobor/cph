# β close-out — Sub A (cph#22) — F7 quality_flag schema↔code vocabulary alignment

## Verdict

**APPROVE** (round 1, no findings).

**Wave:** `.cdd/waves/coherence-drift-sweep-followup-2026-05-18/`
**Master:** usurobor/cph#21
**Sub:** usurobor/cph#22
**Implementation SHA:** `a697265`
**Self-coherence SHA:** `3bc4242`
**β review SHA:** (this commit's parent if split; otherwise this commit)
**Branching:** single-branch dispatch on `claude/review-repo-coherence-PNbjQ` per wave manifest §"Branching deviation".

## What changed

| File | Lines changed | Surface | AC tested |
|---|---|---|---|
| `scripts/segmentation.py` | 4 lines net (L122 1-line ternary replaced with L122–124 3-arm chained ternary) | `Cycle(...)` constructor `quality_flag` literal: `"ok"`/`"out_of_range"` → `"short"`/`"long"`/`"ok"` | AC1, AC2, AC5 |
| `analysis/feature-table-schema.md` | 14 lines changed (L32 example cell, L35 parenthetical, L66 attribution, L68–70 §quality_flag bullets, L72 historical-draft parenthetical) | §Quality Control + §Allowed Values §quality_flag + (no example-row change required since `short` was already in the example) | AC1 (doc-side cross-check), AC3 |
| `analysis/features.md` | 6 lines changed (L27 §Required indexing quality_flag line, L132 §Indexing widening exclusion_reason example, L137 §Quality-flag widening expanded explanation) | §Required indexing + §Candidate set ⊃ §Indexing widening + §Quality-flag widening | AC1 (doc-side cross-check), AC3 |
| `.cdd/unreleased/22/self-coherence.md` | +283 | α-side cycle artifact (`cdd/alpha/SKILL.md` §2.5) | n/a (process) |

Three live surfaces touched (code + 2 docs). Zero new files. Zero charter/roadmap/ledger/changelog touch. Zero notebook touch.

## What β verified (oracles re-run)

1. **AC1 code-side anchor (β re-greps `scripts/segmentation.py` FIRST, per wave manifest §"β anchoring discipline"):** `grep -nE 'quality_flag' scripts/segmentation.py` → 3 hits (L35 dataclass default `"ok"`, L122 constructor first-arm `"short"`, L141 non-emitting comparison `!= "ok"`). Direct read of L122–125 with `sed -n` confirmed the chained ternary emits exactly {`"short"`, `"long"`, `"ok"`}. The dispatcher-prompt regex `quality_flag\s*=\s*"` does NOT match L122 because the `=` is followed by `(` and a newline before the literal `"short"`; β widened to the bare token `quality_flag` to confirm no emission is missed (named in §Notes N1).
2. **AC1 doc-side cross-check (SECOND):** `grep -nE '"(ok|short|long|low_contact_gap|out_of_range)"' analysis/feature-table-schema.md analysis/features.md` returned 5 hits across both files. Backtick-quoted literals (schema §quality_flag bullets L68–70, schema example-row CSV L85–87, features.md L27/L132/L137) do not match the double-quoted regex; β read them directly with `sed -n`. All five canonical surfaces (schema L32, schema L64–72, schema L87, features.md L27, features.md L132/L137) agree string-for-string with code-emitted set {`ok`, `short`, `long`}. `low_contact_gap` appears only in historical-draft parentheticals correctly named as not-realized.
3. **AC1 cross-reference intersection table:** 10-row table (5 code surfaces + 5 doc surfaces) built β-side; bijective match on the code-emitted set; deferred labels named with gating constraint.
4. **AC1 downstream sanity:** `grep -n 'quality_flag' scripts/features.py` → L144 (propagation, structural pass-through) + L145 (`!= "ok"` derivation, correct for any non-`ok` literal). No `scripts/features.py` patch needed. The schema Data Rule 3 (no row with `quality_flag="ok"` and `exclusion_flag=True`) holds by construction.
5. **AC1 boundary inclusion:** chained ternary at L122–124 evaluates `"short" if duration <= 0.5 else ("long" if duration >= 1.8 else "ok")`. At `duration == 0.5` → `"short"` (matches schema's open-interval `(0.5, 1.8)` exclusivity). At `duration == 1.8` → `"long"` (same). At `duration == 1.0` → `"ok"`. Consistent.
6. **AC2 direction recorded:** α §"Direction choice" (L43–46) names direction **a-1** with rationale (3-value vocabulary the segmenter can produce from `duration` alone; distinguishes short vs long); `low_contact_gap` named as deferred work at `analysis/features.md:137` with gating constraint (segmenter must inspect contact-gap structure).
7. **AC3 file surface:** `git show a697265 --stat` → exactly `scripts/segmentation.py`, `analysis/feature-table-schema.md`, `analysis/features.md` (3 files, +13/-11 lines). No notebook touch. No `scripts/features.py` touch.
8. **AC4 no empirical drift:** `git show a697265 -- README.md PROJECT.md CHANGELOG.md ROADMAP.md` → empty. PROJECT.md L20 REVISE posture intact at HEAD (cited field-report-01 2026-05-17). No new file under `reports/`.
9. **AC5 β code-first anchoring:** β authored §AC1 with code-side grep + direct-read of `scripts/segmentation.py:35,122–125,141` BEFORE any doc was opened, then verified each doc surface matches. The structural fix the wave inherits from cph#21 §"Review mode" held.
10. **Identity audit:** `git log --format='%an <%ae>' a697265 3bc4242` → both `α-as-agent <alpha@cph.cdd.cnos>`. β-side commits will be `β-as-agent <beta@cph.cdd.cnos>` per identity-isolation invariant.

## Cross-sub debt

For δ wave-closeout consideration:

1. **`low_contact_gap` future-segmenter debt.** Named in `analysis/features.md` §"Quality-flag widening" L137. Gated on segmenter inspecting contact-gap structure (swing-time within cycle, contralateral HS hints, or force-plate data) rather than only `duration`. Further gated on a downstream consumer needing finer-grained quality labels. α §Debt 1; β concurs.

2. **Boundary-notation cosmetic inconsistency** between schema (`(0.5, 1.8)` open interval) and features.md (Python `<=`/`>=`). Both correct, both internally consistent. A future micro-cycle could unify in one sentence. α §Self-check mistake 6 + §Debt 2; β concurs (cosmetic, not a finding).

3. **Regex-oracle phrasing brittleness.** Issue body AC1 oracle `quality_flag\s*=\s*"` does not match multi-line conditional. Future issue templates should use `quality_flag\s*=` or a multi-line `rg` search. Candidate input for ε's `cdd-iteration.md` β-anchoring SKILL patch (already proposed in wave manifest §"β anchoring discipline").

4. **Carry-over: `extract_shape` always-`True` placeholder** (this wave's Sub D / cph#25; α §Debt 3 cross-sub trace).

5. **Carry-over: field-report-02 stub H1 number mismatch** (this wave's Sub C / cph#24; α §Debt 4 cross-sub trace).

## Identity discipline

| Commit | Author email | Role | Pass |
|---|---|---|---|
| `a697265` (α impl) | `alpha@cph.cdd.cnos` | α | ✓ |
| `3bc4242` (α self-coherence) | `alpha@cph.cdd.cnos` | α | ✓ |
| β review commit | `beta@cph.cdd.cnos` | β | ✓ (pre-commit) |
| β close-out commit (this one if combined) | `beta@cph.cdd.cnos` | β | ✓ (pre-commit) |

Identity-isolation invariant (α ≠ β within Sub A) preserved by Agent-session boundary.

## Next

- This close-out lands on `claude/review-repo-coherence-PNbjQ` as a commit marker.
- β proceeds to Sub B (cph#23) review.
- δ owns wave-closeout after all four subs reach terminal state.

β's role on cph#22 concludes here.
