#!/usr/bin/env bash
# Create milestones for the academy repo.
# Usage: ./create-milestones.sh --dry-run
set -euo pipefail

DRY_RUN=${1:-"--dry-run"}

if ! command -v gh >/dev/null; then
  echo "gh CLI is required." >&2
  exit 1
fi

while IFS= read -r line; do
  [[ -z "$line" ]] && continue
  name=$(echo "$line" | sed 's/^- //')
  if [[ "$DRY_RUN" == "--dry-run" ]]; then
    echo "Would create milestone: $name"
  else
    gh api repos/:owner/:repo/milestones -f title="$name" || true
  fi
done < ../../project/milestones.md
