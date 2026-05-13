#!/usr/bin/env bash
# Wrapper for git-sizer with safe defaults.
# Usage: ./git-sizer-wrapper.sh <repo-path>
set -euo pipefail

REPO_PATH=${1:-""}
if [[ -z "$REPO_PATH" ]]; then
  echo "Usage: ./git-sizer-wrapper.sh <repo-path>" >&2
  exit 1
fi

if ! command -v git-sizer >/dev/null; then
  echo "git-sizer is required." >&2
  exit 1
fi

git -C "$REPO_PATH" sizer
