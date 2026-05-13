# Capture Setup

This protocol describes how recordings are captured for the friend pre-pilot.

## Governing question

How can walking recordings be captured consistently enough for OpenCap processing and gait-cycle comparison?

## Capture principle

The recording should make the walking task visible, repeatable, and interpretable.

Do not optimize for cinematic video. Optimize for stable movement data.

## Equipment

Use the OpenCap capture workflow when possible.

Minimum:

- two compatible smartphones or cameras for OpenCap-style multi-view capture
- stable mounts or tripods
- adequate battery and storage
- clear walking path
- consistent lighting
- session notes

OpenCap's core pipeline is designed around two or more videos and outputs movement data in OpenSim-compatible formats. The capture should respect that assumption.

## Space

Use a flat, uncluttered walking path.

Record:

- approximate path length
- surface type
- footwear condition
- lighting condition
- obstructions
- whether the participant starts and stops inside or outside the capture area

Avoid tight spaces where the participant has to turn immediately, dodge objects, or shorten steps to fit the room.

## Camera placement

Follow OpenCap's current capture guidance when using the OpenCap app.

For project notes, record:

- number of cameras
- approximate camera positions
- camera height
- whether full body stayed visible
- whether either side was occluded
- whether the participant walked out of frame
- whether synchronization or calibration issues occurred

Do not compare trials as if camera setup were identical unless the notes support that.

## Lighting and clothing

Use even lighting where the full body remains visible.

Avoid:

- strong backlighting
- dark rooms
- reflective glare
- loose clothing that hides joint motion, if the participant is comfortable wearing different clothing
- bags, coats, or objects carried during walking unless that is the tested condition

Do not pressure participants about clothing. If clothing limits interpretation, note the limitation.

## Trial recording

For each trial:

1. Confirm participant code and condition in the session note.
2. Start recording.
3. Let the participant enter the walking path.
4. Record enough steps for multiple gait cycles.
5. Stop recording after the participant clears the path.
6. Note any visible issue before the next trial.

The first and last steps may be acceleration or deceleration steps. Prefer middle cycles when enough are available.

## Quality check before processing

Review the recording privately before OpenCap processing.

Flag the trial if:

- the full body is not visible
- the participant turns within the analyzed segment
- a camera moves
- another person enters the frame
- lighting changes sharply
- the participant appears to change task
- the wrong condition was recorded

Do not delete failed trials silently. Record why they failed.

## Data handling

Use participant codes in file names.
Keep raw videos out of the public repo.

Follow [Data Handling](../docs/ethics/data-handling.md).
