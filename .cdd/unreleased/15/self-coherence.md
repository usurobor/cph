# Self-coherence — cycle/15 — Sub D CDR refactor conformance sweep

## Gap

**Issue:** usurobor/cph#15 — Sub D CDR refactor conformance sweep (AC8 / AC9 / AC10 across A+B+C).
**Master:** usurobor/cph#11.
**Wave:** `.cdd/waves/cdr-refactor-2026-05-18/` — Sub D is the final terminal sub, gated behind Subs A/B/C (all merged).
**Mode:** docs-only (conformance sweep — verifies; does not author charter / roadmap / infra content).
**Surface swept:** every non-`.cdd/` path touched by the three merged subs:

- Sub A (`c3c274a`): `README.md`, `CDR.md`, `docs/concepts/coherence-path-hypothesis.md`, `docs/articles/seven-ways-people-walk.md`.
- Sub B (`49cd888`): `ROADMAP.md`.
- Sub C (`f6ad183`): `CHANGELOG.md`, `PROJECT.md`, `targets/{registry,hypothesis,method,evidence,repo}.tsc`, `scripts/measure-coherence.sh`, `.gitignore`.

Pre-wave baseline = `317779c^1` = `d30aa4a` (last `main` commit before δ opened the wave). The A+B+C diff against that baseline is the swept surface; `.cdd/**` and `.tsc/**` are excluded per wave manifest and `.gitignore`.

**ACs in scope:**

- AC8 — no empirical overclaim (hypothesis validated; seven families proven; AI can classify; support paths directly visible; gait implies identity/personality/diagnosis/pathology).
- AC9 — no data policy regression (no raw `*.trc *.mot *.sto *.c3d *.osim *.mp4 *.mov`, no new payload under `data/external/**`).
- AC10 (final) — every source-of-truth row in `README.md` resolves; the question→owner mapping is injective; Sub A/B/C-authored files match their declared owners.

**Out of scope:** authoring new charter / roadmap / infra content (Subs A/B/C did that); running `scripts/measure-coherence.sh` (operator gate); modifying empirical state.
