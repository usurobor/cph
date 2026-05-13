# External Data Policy

## Storage Guidelines

**Do not commit downloaded files to this repository.**

External datasets are stored locally for processing but are not tracked in git due to size, licensing, and storage constraints.

## What goes here

- Dataset manifest files (`.md` format) documenting what was downloaded
- Processing metadata and data quality notes  
- Links and access instructions for reproducibility
- Local storage path documentation

## What does NOT go here

- Raw downloaded data files (videos, motion capture, force plates)
- Processed dataset outputs (unless explicitly small and cleared for sharing)
- Participant data from friend pre-pilot or other collection efforts
- Temporary processing files

## Access Documentation

Each external dataset used by this project has a corresponding manifest file documenting:

- Source URL and access date
- Licensing terms and usage permissions
- Local storage location (private, not committed)
- Data contents and organization
- Processing status and quality notes

## Reproducibility

Others reproducing this work should:

1. Review dataset manifest files for source information
2. Download datasets independently from documented sources  
3. Follow the same local storage organization documented in manifests
4. Use the processing protocols in `../protocols/` to replicate analysis

## Privacy and Ethics

External datasets may contain identifiable biometric data. Follow the ethics guidelines in `docs/ethics/` when working with any downloaded data.