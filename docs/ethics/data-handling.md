# Data Handling

Gait video is identifiable biometric data. It can show face, body shape, clothing, injury compensation, location, voice, and social context.

This file owns the data-handling policy for the repo.

## Governing question

How is participant data handled so the project can test movement hypotheses without exposing or labeling people?

## Public repository rule

Do not commit raw videos.
Do not commit faces.
Do not commit names.
Do not commit consent forms.
Do not commit injury histories.
Do not commit identifiable participant notes.

The public repository may contain:

- theory
- protocols
- consent language
- analysis code
- anonymized traces
- synthetic examples
- field reports
- failure notes

Any public example must be checked against [Public Sharing Rules](/tmp/gait-support-paths/docs/ethics/public-sharing-rules.md).

## Participant codes

Use participant codes such as `P001`, `P002`, and `P003`.

Keep the mapping from code to name outside the repo in private storage. The mapping should be readable only by the project lead or explicitly named collaborators.

Do not use initials, birthdays, nicknames, workplace names, or other guessable identifiers.

## Storage

Store raw capture data in private storage with access control.

Minimum requirements:

- one private folder per participant code
- no names in file names
- consent record stored separately from movement data
- access limited to named people
- backup only to private storage, not public sync folders by accident
- deletion process documented

If a cloud service is used, participants should be told which service or platform is involved. If OpenCap cloud processing is used, that must be included in consent language.

## File naming

Use descriptive but non-identifying names:

```txt
P001_S01_T01_normal_shod_rightleft_raw
P001_S01_T02_slow_shod_raw
P001_S01_T03_fast_shod_raw
P001_S01_T04_normal_barefoot_raw
```

Processed outputs should keep the same participant, session, trial, and condition codes.

## Metadata

Record only metadata needed to interpret movement data:

- participant code
- session date
- walking condition
- footwear
- fatigue state
- recent exercise
- pain or injury note, if voluntarily disclosed and relevant
- dominant side, if voluntarily disclosed
- capture setup notes
- processing status

Do not record broad personal history because it is interesting. If a note does not help interpret the recording, leave it out.

## Consent and withdrawal

Use the consent language in [Consent Template](/tmp/gait-support-paths/docs/ethics/consent-template.md) before recording.

Participants may decline any condition, stop recording, ask questions, or withdraw their data. If a participant withdraws, remove raw data and any derived traces that can reasonably be linked back to that participant. Record that deletion occurred without retaining unnecessary personal detail.

## Analysis exports

Before analysis data are placed in the repo, remove direct identifiers and inspect whether the export can reasonably identify the participant.

Allowed public analysis artifacts may include:

- normalized gait-cycle curves labeled only by participant code or anonymized group code
- aggregate feature tables without names
- plots that omit faces and raw video frames
- synthetic examples
- field-report summaries with non-identifying context

Small samples are easier to re-identify. For the friend pre-pilot, prefer private analysis outputs unless there is a clear reason to publish a trace.

## Participant feedback

Do not give participants type labels.
Do not imply diagnosis.
Do not describe movement as defect, pathology, or identity.

Use condition-bound language:

> Under this condition, this recording shows this movement pattern.
