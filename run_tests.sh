#!/usr/bin/env bash
set -euo pipefail

# Activate virtual environment
if [ ! -f "venv/Scripts/activate" ]; then
  echo "Virtual environment not found at venv/Scripts/activate" >&2
  exit 1
fi

# shellcheck disable=SC1091
source "venv/Scripts/activate"

# Execute test suite
python -m pytest -q
