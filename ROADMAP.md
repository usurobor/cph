# Roadmap

This file tracks the gates by which the Coherence Path Hypothesis is validated, revised, or abandoned.

The hypothesis itself lives in [docs/concepts/coherence-path-hypothesis.md](docs/concepts/coherence-path-hypothesis.md). Live operational status lives in [PROJECT.md](PROJECT.md). The coherence ledger across waves lives in [CHANGELOG.md](CHANGELOG.md). This roadmap names what each phase must achieve and where each phase stands.

## Goal

Validate, revise, or abandon the Coherence Path Hypothesis through gates that name what each phase must produce, what currently exists, and what blocks the next transition.

## Current state

**R1 is REVISE** per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md). The OpenCap-vs-reference comparison cleanly passes; the gait-cycle segmentation primitive fails on real Mocap heel-marker data (18.3% of 60 trials, R-side only, 0 L-side). The next bounded cycle targets `scripts/segmentation.py::detect_heel_strikes`. R3–R4 are not testable at the current cycle count. R5 is blocked behind earlier gates. R6 is not started.

## How to read this file

Each phase carries seven fields:

- **Goal** — what the phase must achieve.
- **Current evidence** — what merged artifacts show today; cited from owning files.
- **Gate** — the condition that closes the phase. "Closes" means status transitions out of ACTIVE / REVISE into GO.
- **Status** — one of NOT STARTED, ACTIVE, GO, REVISE, STOP. R5 and R6 carry their own status phrasings per the master issue.
- **Coherence risk** — how running this phase could damage project coherence (terminology drift, evidence/claim drift, identity drift). Not an empirical risk; the empirical risks live in the protocol and field-report files.
- **Next action** — the next concrete step the phase requires.
- **Owning files** — the surfaces that this phase reads from and writes to.

A high coherence score (C_Σ in [CDR.md](CDR.md)) does not transition any phase. Only the gate transitions a phase.

## Phase R0 — Charter and operationalization

- **Goal:** Make the Coherence Path Hypothesis explicit, bound its operational terms, and pin source-of-truth ownership across the repo.
- **Current evidence:** [`README.md`](README.md), [`CDR.md`](CDR.md), [`docs/concepts/coherence-path-hypothesis.md`](docs/concepts/coherence-path-hypothesis.md), [`docs/concepts/support-path.md`](docs/concepts/support-path.md), [`docs/concepts/failure-conditions.md`](docs/concepts/failure-conditions.md), and [`docs/articles/seven-ways-people-walk.md`](docs/articles/seven-ways-people-walk.md) are merged (Sub A of master cph#11). This roadmap is the Sub B deliverable. `CHANGELOG.md`, `targets/*.tsc`, and `scripts/measure-coherence.sh` are the Sub C deliverables; the AC8/AC9/AC10 sweep is the Sub D deliverable.
- **Gate:** README, hypothesis doc, support-path doc, failure-conditions doc, CDR doctrine, ROADMAP, and CHANGELOG agree on terms, empirical state, and source-of-truth ownership. AC8/AC9/AC10 conformance sweep passes.
- **Status:** ACTIVE.
- **Coherence risk:** Charter files re-state the hypothesis or its operational terms with subtly different wording, producing the α-axis drift CDR.md is designed to catch. The risk is that `coherence path`, `support path`, `gait family`, and `feature` lose their boundaries across files. The Sub D sweep (AC8) is the structural backstop.
- **Next action:** Sub B (this), Sub C, Sub D merge; wave [`cdr-refactor-2026-05-18`](.cdd/waves/cdr-refactor-2026-05-18/manifest.md) closes; phase transitions to GO at wave close.
- **Owning files:** [`README.md`](README.md), [`CDR.md`](CDR.md), [`docs/concepts/coherence-path-hypothesis.md`](docs/concepts/coherence-path-hypothesis.md), [`docs/concepts/support-path.md`](docs/concepts/support-path.md), [`docs/concepts/failure-conditions.md`](docs/concepts/failure-conditions.md), [`docs/articles/seven-ways-people-walk.md`](docs/articles/seven-ways-people-walk.md), `ROADMAP.md` (this), [`PROJECT.md`](PROJECT.md), `CHANGELOG.md` (pending Sub C), `targets/*.tsc` (pending Sub C), `scripts/measure-coherence.sh` (pending Sub C).

## Phase R1 — Existing-data zeroth pilot

- **Goal:** Process the OpenCap Lab Validation archive end-to-end before any new data collection, and test whether the pipeline can produce usable gait-cycle segmentation, feature tables, plots, and reference comparisons on real walking data.
- **Current evidence:** Per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) (2026-05-17 real-data run), the archive (60 walking trials × 10 subjects) was acquired (SHA-256 `3290d485124fd12c85dd3bc9ee851f3a0530ad0ff58bc396973e665dd6d28187`), extracted, and run end-to-end. Discovery, IK parsing, marker pairing, feature extraction, OpenCap-vs-reference comparison, plotting, and persistence are real-data-ready. The OpenCap-vs-reference comparison passes (Pearson r̄ 0.962 HRNet, 0.933 OpenPose_default, 0.951 OpenPose_highAccuracy across 60 trials × 3 Video backbones). The segmentation primitive fails (see R2).
- **Gate:** Pipeline produces usable gait-cycle segmentation, feature tables, plots, and reference comparisons on the existing archive. All four artifact classes must clear their AC thresholds.
- **Status:** REVISE.
- **Coherence risk:** Mainline files cite branch-only segmentation numbers as fact, or treat the OpenCap-vs-reference pass as evidence for the Coherence Path Hypothesis itself. The comparison cleared the OpenCap *technology stack*, not the construct.
- **Next action:** Hold REVISE until R2 closes; then re-run [`notebooks/existing-data-processing.ipynb`](notebooks/existing-data-processing.ipynb) on the unchanged archive and re-evaluate the falsification table in field-report-01.
- **Owning files:** [`protocols/existing-data-zeroth-pilot.md`](protocols/existing-data-zeroth-pilot.md), [`notebooks/existing-data-processing.ipynb`](notebooks/existing-data-processing.ipynb), `scripts/io_opencap.py`, `scripts/build_notebook.py`, [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md), [`data/external/opencap-lab-validation.md`](data/external/opencap-lab-validation.md).

## Phase R2 — Contact-event and segmentation reliability

- **Goal:** Establish reliable heel-strike detection and gait-cycle segmentation on real Mocap calcaneus markers, on both sides or with a clearly justified one-side analysis path.
- **Current evidence:** Per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) §Segmentation Status, `scripts.segmentation.detect_heel_strikes` fires on 11 of 60 trials (18.3%, all R-side); zero L-side cycles were extracted. Root cause is parameters fit to the synthetic generator: real calcaneus markers carry a ~25 mm R/L mean offset that the detector's smoothed-threshold logic does not tolerate. Smoke synthetic data hits 100% segmentation; the regression is on real data only. A bounded revision is named: per-side baseline subtraction + percentile-of-range threshold, estimated one cycle. An orthogonal branch `origin/cycle/segmentation-real-data-fix` (tip `a95415c`) is unmerged; merge is a separate operator decision per the wave manifest.
- **Gate:** Detector fires on ≥60% of real Mocap walking trials per side, *or* the report explicitly justifies a one-side analysis path with documented reasoning for the asymmetry.
- **Status:** REVISE.
- **Coherence risk:** A segmenter fix produces better numbers, but the empirical-state language in README / PROJECT.md / CHANGELOG / this roadmap is not updated together — the project then reads as more advanced than the merged field report supports. A second risk is treating smoke-test passing as construct evidence; the smoke generator hardcodes the heel shape the detector targets, which is a tautology, not validation.
- **Next action:** Open a single-issue cycle scoped to `scripts/segmentation.py::detect_heel_strikes` plus a verification harness using the 60 Mocap heel-marker trials already in `/opt/gait-data/opencap-lab-validation/extracted/`. Merge the fix; re-run the notebook; re-evaluate the falsification table.
- **Owning files:** `scripts/segmentation.py`, the verification harness fixtures, [`notebooks/existing-data-processing.ipynb`](notebooks/existing-data-processing.ipynb), [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) (re-evaluation).

## Phase R3 — First construct-level evidence

- **Goal:** Test whether the per-cycle features named in [`analysis/features.md`](analysis/features.md) show stable, interpretable coordination signatures at the subject level under condition response (natural vs trunk-sway), without pseudoreplication.
- **Current evidence:** Per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) §Support-Path Inference, Hypothesis 1 (sagittal-dominant load transfer) is *partially evaluable* from the comparison data (sagittal joints reconstruct cleanly across 60 trials) and from the 11 R-side cycles (hip-knee cross-correlation lag 12.5–15.4% of cycle). Hypothesis 2 (trunk-sway compensation) and Hypothesis 3 (asymmetric phase-coupling) are blocked — only 2 trunk-sway cycles segmented and zero L-side cycles across the entire archive. Within-trial repeatability is not testable at one cycle per successful trial. The empirical claim is held in reserve.
- **Gate:** Subject-level (not cycle-level) condition-response analysis demonstrates stable feature distributions per subject per condition; aggregation method excludes pseudoreplication; at least two of the three framed hypotheses survive specification under adequate n.
- **Status:** NOT STARTED.
- **Coherence risk:** Pseudoreplication — reporting per-cycle distributions as if cycles were independent observations. Adjacent risks: `support path` and `coherence path` losing their distinction once recurrence/distinguishability tests run; alternative explanations (trial crop, marker artifact, camera setup, subject morphology, condition labels alone) being collapsed into the "construct survives" verdict instead of being named separately.
- **Next action:** After R2 closes, plan and execute the subject-level condition-response analysis per [`analysis/left-right-comparison.md`](analysis/left-right-comparison.md) and [`analysis/feature-table-schema.md`](analysis/feature-table-schema.md). Produce `field-report-03-construct-evaluation` with the construct evaluation, separating measured signal from inferred interpretation.
- **Owning files:** [`analysis/features.md`](analysis/features.md), [`analysis/feature-table-schema.md`](analysis/feature-table-schema.md), [`analysis/feature-summary-zeroth-pilot.md`](analysis/feature-summary-zeroth-pilot.md), [`analysis/left-right-comparison.md`](analysis/left-right-comparison.md), [`notebooks/existing-data-processing.ipynb`](notebooks/existing-data-processing.ipynb), future `reports/field-report-03-construct-evaluation.md`.

## Phase R4 — Support/coherence-path inference

- **Goal:** Determine whether the coordination signatures from R3 justify the inference to a support/coherence path, distinct from measured data alone.
- **Current evidence:** Per [`reports/field-report-01-existing-data-zeroth-pilot.md`](reports/field-report-01-existing-data-zeroth-pilot.md) §Falsification Assessment, 0 of 6 falsification conditions cleanly triggered; condition 5 (feature extraction failure) is partially triggered via the segmenter; condition 4 (OpenCap-reference agreement) is cleanly NOT triggered; 4 of 6 are not testable at n=11. The hypothesis is neither validated nor refuted. The mechanical "below the 4-condition NO-GO threshold" reading is not construct-survival evidence; it reflects cycle scarcity.
- **Gate:** The falsification table from [`docs/concepts/support-path.md`](docs/concepts/support-path.md) §Falsification is evaluated on data capable of triggering each condition; the evaluation distinguishes measured surfaces (kinematics, timing, segment coupling, asymmetry, condition response) from inferred interpretation (coherence-path organization, load-transfer reading); alternative explanations are named per [`docs/concepts/failure-conditions.md`](docs/concepts/failure-conditions.md).
- **Status:** NOT STARTED.
- **Coherence risk:** Treating coherence-path inference as a measurement. The α-axis terminology distinction (Coherence Path Hypothesis = the claim; support path = the operationalized pattern) collapses if a phase-4 write-up calls a measured feature a "coherence path" without inference, or treats the seven gait families as proven by a clustering output rather than as candidate surface expressions. CDR.md names this failure mode as `coherence laundering` — using a high project coherence score (or a clean feature table) to support the substantive claim.
- **Next action:** After R3 closes, re-evaluate the falsification table at adequate n; report per-condition pass/fail with explicit n; separate measurement from interpretation in the field report.
- **Owning files:** [`docs/concepts/support-path.md`](docs/concepts/support-path.md) (§Falsification), [`docs/concepts/failure-conditions.md`](docs/concepts/failure-conditions.md), [`docs/concepts/coherence-path-hypothesis.md`](docs/concepts/coherence-path-hypothesis.md) (§Falsification conditions, §Current empirical status), future field report.

## Phase R5 — New capture / friend pre-pilot

- **Goal:** Only after existing data justifies new capture, test the acquisition pipeline against a small friend cohort to evaluate consent, capture rehearsal, OpenCap output reliability, and the rest of the protocol stack.
- **Current evidence:** Protocols are drafted ([`protocols/friend-pre-pilot.md`](protocols/friend-pre-pilot.md), [`protocols/capture-rehearsal.md`](protocols/capture-rehearsal.md), [`protocols/capture-setup.md`](protocols/capture-setup.md), [`protocols/session-notes-template.md`](protocols/session-notes-template.md), [`protocols/blind-observation-memo.md`](protocols/blind-observation-memo.md), [`protocols/walking-conditions.md`](protocols/walking-conditions.md)). Ethics protocols are in place in [`docs/ethics/`](docs/ethics/). No friend data has been collected. No capture rehearsal has been executed.
- **Gate:** R3 and R4 have closed with GO; consent and capture rehearsal protocols pass dry-run; OpenCap output reliability on a friend cohort matches Lab Validation reference; `field-report-02-friend-pre-pilot` documents what survived, what failed, what was visible, and what was not.
- **Status:** Blocked until earlier gates pass.
- **Coherence risk:** Friend data is read as validation of the hypothesis rather than as a pipeline-robustness test (the realization the project owns as [`docs/realizations/04-friends-are-a-pre-pilot.md`](docs/realizations/04-friends-are-a-pre-pilot.md)). Adjacent risks: body-typing or labeling participants, eroding the "object is the step under a condition, not the person" boundary; the safety-boundary sentence in [`README.md`](README.md) ("Under this condition, this recording shows this movement pattern") drifting toward typology language in protocol or report drafts.
- **Next action:** Wait for R3 and R4 to close GO. While waiting, run no friend captures; do not soft-start the cohort.
- **Owning files:** [`protocols/friend-pre-pilot.md`](protocols/friend-pre-pilot.md), [`protocols/capture-rehearsal.md`](protocols/capture-rehearsal.md), [`protocols/capture-setup.md`](protocols/capture-setup.md), [`protocols/walking-conditions.md`](protocols/walking-conditions.md), [`protocols/session-notes-template.md`](protocols/session-notes-template.md), [`protocols/blind-observation-memo.md`](protocols/blind-observation-memo.md), [`docs/ethics/`](docs/ethics/), [`reports/field-report-02-friend-pre-pilot.md`](reports/field-report-02-friend-pre-pilot.md) (stub; awaiting data).

## Phase R6 — AI classification

- **Goal:** Apply unsupervised or self-supervised structure-finding to per-cycle feature tables only after stable feature surfaces exist and survive confound checks.
- **Current evidence:** No clustering has been run. [`analysis/clustering-plan.md`](analysis/clustering-plan.md) exists as a plan-only document.
- **Gate:** A stable per-cycle feature table from R3 / R4 is available; unsupervised structure (clusters, embeddings, manifold organization) survives confound checks against trial crop, marker artifact, camera setup, subject morphology, and condition labels alone; clustering output is reported as candidate structure, not as confirmation of the seven gait families or the Coherence Path Hypothesis.
- **Status:** Not started.
- **Coherence risk:** The largest coherence risk in the project. Clustering output is the most likely surface to be read as hypothesis confirmation, since AI labels are easy to mistake for measurement. CDR.md names this failure mode as `coherence laundering` — using a high project coherence score (or a clean clustering output) to support a substantive claim. Adjacent risks: the seven gait families being reintroduced as proven categories by automated labels; the project's identity drifting from "test the hypothesis" toward "build a typology"; the safety boundary in [`README.md`](README.md) eroded by labels that read as diagnoses.
- **Next action:** Hold. Do not run clustering against existing or future data until R4 closes GO.
- **Owning files:** [`analysis/clustering-plan.md`](analysis/clustering-plan.md), future analysis documents.
