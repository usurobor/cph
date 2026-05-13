# Support Path

A support path is an inferred coordination pattern during a gait cycle.

It is the temporary way a body receives load from the ground, routes that load through linked segments, stabilizes itself, and prepares the next step.

It is not an anatomical structure.
It is not a fixed fascial line.
It is not a diagnosis.
It is not a trait that belongs permanently to a person.

The object is the step under a condition.

## Operational Definition

A support path is an inferred coordination pattern in gait-cycle time series. It is not load itself. It is not a visible line in the body.

Support paths are organizational hypotheses about how timing, stiffness, and segment coordination work together during a gait cycle. These hypotheses can only be tested through quantitative analysis of measured movement data.

## Governing question

When a foot contacts the ground, does the resulting movement show a repeatable organization of timing, orientation, stiffness, rotation, and segment coordination?

If yes, that organization may be described as a candidate support path.

If no, the observation remains a visual impression and should not be promoted into a research object.

## What the term holds together

The word "support" means that walking is being treated as a load-bearing event. A step is not only a limb swinging forward. It is also a body accepting weight, preventing collapse, redirecting force, and returning energy.

The word "path" does not mean a visible line in the body. It means a temporal route through coordination. Load may appear to move through one region cleanly, pause locally, be redirected by rotation, or require compensation somewhere else. Those descriptions are hypotheses until measurement supports them.

## Measured vs Inferred

**Measured quantities** (observable from sensors and instruments):
- Kinematics (position, velocity, acceleration of body segments)
- Timing (heel-strike, toe-off, swing duration, stance duration)
- Joint angles (hip, knee, ankle flexion/extension, rotation)
- Segment motion (pelvis tilt, trunk rotation, limb trajectories)
- Force-plate data (ground reaction forces, center of pressure)
- EMG signals (muscle activation timing and amplitude)
- OpenCap estimates (video-derived joint angles and timing events)

**Inferred constructs** (interpretations requiring theoretical framework):
- Support path (coordination pattern hypothesis)
- Load-transfer organization (how forces route through the body)
- Bracing strategies (stiffness patterns during weight acceptance)
- Collapse-and-catch patterns (controlled yielding and recovery)
- Spiral coupling (rotational coordination between segments)

Support paths belong in the inferred category. They are organizational hypotheses derived from measured quantities, not direct observations. The validity of these inferences depends on consistent patterns appearing across multiple measured traces.

## What can count as evidence

A support path is never observed directly. It is inferred from traces such as:

- gait-cycle timing
- pelvis and trunk rotation
- hip, knee, and ankle angle curves
- stance and swing durations
- left-right asymmetry
- segment coupling
- smoothness or interruption of movement
- delayed stabilization after contact
- push-off timing
- changes across speed, footwear, fatigue, attention, or repeat session

These traces are signs. They are not the support path itself.

## What cannot count as evidence by itself

The following may generate hypotheses, but they do not establish a support path on their own:

- a memorable visual impression
- a named walking type
- posture in a still frame
- one unusually clear step
- a participant's personality, identity, or history
- the observer's confidence

The project can use qualitative observation, but only as a proposal to be tested against gait-cycle data.

## Relation to other project files

The unit used to test a support path is defined in [Gait Cycle As Unit](gait-cycle-as-unit.md).

The functional action being studied is defined in [Load Transfer Strategy](load-transfer-strategy.md).

The analysis features used as candidate traces are listed in [Features](../../analysis/features.md).

## Falsification Conditions for Existing-Data Zeroth Pilot

The support path construct weakens under the following empirical conditions during existing-data processing:

### 1. No Repeatable Patterns Across Gait Cycles
If extracted features show purely random variation between gait cycles within the same trial and participant, with no discernible coordination patterns, then support paths may be theoretical artifacts rather than measurable phenomena.

### 2. Features Uncorrelated with Movement Context  
If extracted timing, joint angle, and coordination features fail to show systematic differences between walking speeds, conditions, or participants, the construct lacks empirical grounding in the measured data.

### 3. Left-Right Asymmetry Without Systematic Organization
If left and right limb features show random asymmetry rather than systematic differences that could reflect coordination strategies, then support paths may not capture meaningful organizational patterns.

### 4. Poor Agreement Between OpenCap and Reference Measurements
If OpenCap-derived features show poor correlation with gold-standard measurements (force plates, optical motion capture), then the technical foundation for support path analysis is compromised.

### 5. Feature Extraction Consistently Fails on Clean Data
If the pipeline cannot reliably extract interpretable features from high-quality gait data, then the measurement approach is inadequate for testing support path hypotheses.

### 6. No Distinguishable Coordination Signatures
If feature analysis reveals only continuous variation without discrete organizational types or clusters, then support paths may represent observer bias rather than measurable coordination patterns.

**Falsification threshold:** If 4 or more of these conditions occur during existing-data processing, the construct requires fundamental revision before proceeding with friend data collection.

## Safe claim

The strongest allowed sentence at this stage is:

> Under this condition, this recording shows this movement pattern.

The forbidden shortcut is:

> This is who you are.
