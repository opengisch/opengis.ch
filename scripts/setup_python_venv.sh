#!/usr/bin/env bash
set -euo pipefail

VENV_DIR="${1:-.venv}"

python3 -m venv "$VENV_DIR"
"$VENV_DIR/bin/python" -m pip install --disable-pip-version-check -r requirements-dev.txt

echo "Python virtual environment ready at: $VENV_DIR"
echo "Activate it with: source $VENV_DIR/bin/activate"
