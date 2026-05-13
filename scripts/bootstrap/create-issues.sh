#!/usr/bin/env bash
# Create issues from project/issue-backlog.md.
# Usage: ./create-issues.sh --dry-run
set -euo pipefail

DRY_RUN=${1:-"--dry-run"}

if ! command -v gh >/dev/null; then
  echo "gh CLI is required." >&2
  exit 1
fi

echo "TODO: Implement markdown parsing for issue-backlog.md"
if [[ "$DRY_RUN" == "--dry-run" ]]; then
  echo "Dry run: no issues created."
fi
