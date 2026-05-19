#!/usr/bin/env bash
# scripts/measure-coherence.sh — coherence measurement entrypoint for cph.
#
# Runs `coh --mode mechanical` against every target in
# `targets/registry.tsc` and writes reports to `.tsc/`.

set -euo pipefail

REGISTRY="targets/registry.tsc"
OUTPUT_DIR=".tsc"
TARGETS=(repo hypothesis method evidence)

if ! command -v coh >/dev/null 2>&1; then
  cat >&2 <<'EOF'
error: `coh` is not installed or not on PATH.

Install:

    curl -fsSL https://raw.githubusercontent.com/usurobor/tsc/main/install.sh | sh

Verify:

    coh --version

Re-run:

    scripts/measure-coherence.sh
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
