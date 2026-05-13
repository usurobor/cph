# Gait Cycle As Unit

The unit of analysis is one gait cycle under one recorded condition.

A gait cycle begins with an event on one side, usually foot contact, and continues until the same event recurs on that same side. In this repo, a right gait cycle and a left gait cycle are treated as separate units before they are compared.

The person is not classified first.
The step is described first.

## Governing question

What is the smallest repeatable unit that can carry the support-path hypothesis without turning the participant into the object?

The answer is:

> one gait cycle, from one side, during one condition, from one recording.

## Why this unit matters

Walking is repetitive, but it is not identical from step to step. Speed changes, attention changes, footwear changes, fatigue changes, and the first few steps of a trial may differ from later steps.

If the project uses "the person" as the unit, those differences disappear too early. A person can become a label before the movement has been measured.

If the project uses isolated frames, the sequence disappears. A support path is about timing and coordination, not a pose.

The gait cycle is small enough to preserve variation and large enough to contain load acceptance, mid-stance support, push-off, swing, and return to contact.

## Required labels for each cycle

Each extracted cycle should keep at least these labels:

- participant code
- session date
- trial id
- condition
- side used to define the cycle
- step number within the trial
- footwear state
- walking speed condition
- known capture notes
- exclusion flag, if used

These labels do not define the pattern. They prevent false structure from being mistaken for a pattern.

## What is compared

Cycles can be compared within a participant:

- right side against left side
- normal speed against slow or fast speed
- shod against barefoot
- early trial against later trial
- first session against repeat session

Cycles can also be compared across participants, but only after condition labels are preserved. A cluster that mostly separates by speed, footwear, camera setup, or body size is not evidence for a support path.

## Normalization

For analysis, each cycle should be time-normalized to a common scale such as 0-100% of the gait cycle. The original timing must also be retained.

Normalized curves allow shape comparison.
Original durations preserve timing differences.

Both matter.

## Exclusions

A cycle should be excluded or flagged if:

- the foot contact event cannot be identified consistently
- the participant starts, stops, turns, or visibly avoids the capture space
- OpenCap tracking is visibly unstable
- a camera obstruction interrupts the body view
- the participant reports pain, fatigue, or distraction that changes the intended condition

Exclusion is not failure. It is part of keeping the unit honest.
