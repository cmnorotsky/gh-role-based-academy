#!/usr/bin/env bash
# Create labels for the academy repo.
# Usage: ./create-labels.sh --dry-run
set -euo pipefail

DRY_RUN=${1:-"--dry-run"}

if ! command -v gh >/dev/null; then
  echo "gh CLI is required." >&2
  exit 1
fi

while IFS= read -r label; do
  [[ -z "$label" ]] && continue
  if [[ "$DRY_RUN" == "--dry-run" ]]; then
    echo "Would create label: $label"
  else
    gh label create "$label" --color "ededed" --description "academy label" || true
  fi
done < ../../project/labels.md
