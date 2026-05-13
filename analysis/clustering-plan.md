# Clustering Plan

This file describes how clusters are tested.

## Governing question

Do OpenCap-derived gait-cycle features contain recurring structures that are not reducible to obvious confounds?

## Starting position

The first clustering task is exploratory.

It should not train a model to reproduce visual type labels. That would automate the observer's bias.

The first useful models should be unsupervised or self-supervised, using gait-cycle curves and features as input.

## Input units

Each input should represent one gait cycle or one side-specific stance phase under one condition.

Required labels are kept for auditing, not for supervised training:

- participant code
- condition
- side
- speed instruction
- footwear
- session
- trial id
- quality flag

## Preprocessing

Before clustering:

1. Exclude or flag failed cycles.
2. Normalize each cycle to a common 0-100% scale for waveform comparison.
3. Preserve original duration features.
4. Scale numeric features using a documented method.
5. Keep right and left cycles separate unless the analysis explicitly combines them.
6. Plot representative curves before modeling.

Do not cluster uninspected feature tables.

## First clustering passes

Run simple, inspectable approaches first:

- PCA or UMAP for visualization, with caution about overreading plots
- hierarchical clustering on waveform distances
- k-means or Gaussian mixture models on reduced features, if sample size allows
- dynamic time warping distances for curve-shape comparison, if justified

The friend pre-pilot may be too small for stable clustering. If so, report that directly.

## Confound checks

After any cluster appears, check whether it is mostly explained by:

- participant identity
- walking speed
- footwear
- side
- session
- camera setup
- trial order
- body size or sex, if such metadata were collected
- processing quality

A cluster that separates `fast_shod` from `slow_shod` may be useful for speed response, but it is not evidence for a support-path family.

## Stability checks

Ask:

- Do cycles from the same condition and participant cluster together?
- Do repeated trials land near each other?
- Do left and right sides separate consistently?
- Does removing one participant destroy the structure?
- Do clusters persist across feature sets?
- Are clusters visible in plotted curves, not only in coordinates?

If the answer is no, do not name the clusters.

## Relation to qualitative categories

Only after clustering should the blind observation memos be compared with cluster structure.

Possible outcomes:

- clusters resemble proposed categories
- clusters split a proposed category
- clusters merge proposed categories
- clusters contradict the observation
- clusters reflect confounds
- no stable clusters appear

All are valid results.

## Naming clusters

Do not give clusters person-type names.

Use descriptive analysis names:

- `late_right_pushoff_group`
- `high_pelvis_rotation_range_group`
- `speed_sensitive_cluster`
- `unclear_cluster_a`

Names should describe measured structure, not identity.

## Minimum report

Every clustering attempt should report:

- feature set used
- cycle count
- exclusion rules
- preprocessing
- algorithm
- number of clusters or distance threshold
- plots
- confound checks
- stability checks
- whether the result is interpretable

If the pre-pilot cannot support clustering, the correct output is a failure note and a revised plan.
