# Friend Pre Pilot

This protocol describes how to run the friend pre-pilot.

The purpose is to test the pipeline, not to validate support paths.

## Governing question

Can the project capture, process, segment, and compare walking data well enough to decide whether a larger pilot is worth designing?

## Participants

Target 5-10 adults who can walk safely without assistance for the planned conditions.

Do not recruit people because their gait looks interesting. Use available participants and record context carefully.

Participation is voluntary. A friend can decline, skip a condition, stop, or withdraw data without needing to explain.

## Before recording

1. Give the participant the consent language in [Consent Template](/tmp/gait-support-paths/docs/ethics/consent-template.md).
2. Explain that this is not a clinical study, diagnosis, treatment, or type assignment.
3. Assign a participant code.
4. Record minimal metadata needed for interpretation.
5. Confirm that the participant can walk the selected conditions comfortably.
6. Prepare the capture setup described in [Capture Setup](/tmp/gait-support-paths/protocols/capture-setup.md).

## Metadata to record

Record:

- participant code
- session date
- footwear
- fatigue level using simple language
- recent exercise
- comfort with being recorded
- dominant side, if volunteered
- pain or injury note, if volunteered and relevant
- conditions completed
- capture notes

Do not record unnecessary personal detail.

## Conditions

Use the condition definitions in [Walking Conditions](/tmp/gait-support-paths/protocols/walking-conditions.md).

Minimum useful set:

- normal walking, shod
- slow walking, shod
- fast walking, shod
- normal walking, barefoot, if safe and comfortable

Optional:

- repeat normal shod trial
- repeat session on another day

## Recording sequence

For each condition:

1. Name the condition out loud or in the session note.
2. Let the participant practice once if needed.
3. Record the trial.
4. Stop and note any issue immediately.
5. Repeat only if the participant is comfortable and the recording failed.

Avoid coaching movement quality. Give task instructions, not body instructions.

Use:

> Walk at your normal comfortable pace.

Do not use:

> Walk naturally so we can see your real type.

## Blind observation memo

Before processing the videos through OpenCap, complete [Blind Observation Memo](/tmp/gait-support-paths/protocols/blind-observation-memo.md).

The memo should describe visible movement hypotheses without access to OpenCap curves.

Do not revise the memo after processing.

## Processing and extraction

After recording:

1. Process usable trials through OpenCap.
2. Export the outputs listed in [Outputs To Extract](/tmp/gait-support-paths/instruments/opencap/outputs-to-extract.md).
3. Segment gait cycles using the cycle unit defined in [Gait Cycle As Unit](/tmp/gait-support-paths/docs/concepts/gait-cycle-as-unit.md).
4. Extract features listed in [Features](/tmp/gait-support-paths/analysis/features.md).
5. Compare left and right sides using [Left Right Comparison](/tmp/gait-support-paths/analysis/left-right-comparison.md).

## Stop conditions

Stop the session if:

- the participant wants to stop
- the participant reports pain, dizziness, or discomfort
- the walking space becomes unsafe
- repeated recording failures make the session frustrating
- consent or data use becomes unclear

Stopping is a valid result.

## Output

The main output is a field report, not a classifier.

Use [Field Report 01 Friend Pre Pilot](/tmp/gait-support-paths/reports/field-report-01-friend-pre-pilot.md) after data collection.
