#!/usr/bin/env bash
# scripts/measure-coherence.sh — mechanical TSC measurement entrypoint for cph.
#
# Runs `coh --mode mechanical` against every target named in
# `targets/registry.tsc` (repo, hypothesis, method, evidence) and writes
# the report set to `.tsc/`. Mechanical mode does not require LLM
# credentials; hybrid mode is documented but not invoked here.
#
# If `coh` is not on PATH, the script prints installation instructions
# and exits nonzero so that CI and humans see a clear missing-tool
# signal rather than a silent skip.
#
# Targets are sourced from the registry, not hardcoded, so adding a new
# target only requires editing `targets/registry.tsc`.

set -euo pipefail

REGISTRY="targets/registry.tsc"
OUTPUT_DIR=".tsc"
TARGETS=(repo hypothesis method evidence)

if ! command -v coh >/dev/null 2>&1; then
  cat >&2 <<'EOF'
error: `coh` (TSC CLI) is not installed or not on PATH.

cph measures project coherence via the TSC CLI. Install `coh` and re-run.

Install:

    pip install tsc-cli         # if published on PyPI
    # or from source:
    git clone https://github.com/usurobor/tsc
    pip install -e ./tsc

Verify:

    coh --version

Re-run:

    scripts/measure-coherence.sh

This script runs mechanical mode only. Mechanical mode does not require
LLM credentials. Hybrid mode is optional and documented in CDR.md.
EOF
  exit 127
fi

if [[ ! -f "$REGISTRY" ]]; then
  echo "error: target registry not found at $REGISTRY" >&2
  echo "       run this script from the repo root." >&2
  exit 2
fi

mkdir -p "$OUTPUT_DIR"

for target in "${TARGETS[@]}"; do
  echo "==> coh --mode mechanical --target $target"
  coh --mode mechanical \
      --target "$target" \
      --registry "$REGISTRY" \
      --output "$OUTPUT_DIR/"
done

echo "done. reports written to $OUTPUT_DIR/"
