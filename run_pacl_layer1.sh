#!/usr/bin/env bash
set -euo pipefail

echo "=== PACL Layer 1 pipeline start ==="

if [ ! -d ".venv" ]; then
  echo "ERROR: .venv not found. Create and activate the virtual environment first."
  exit 1
fi

source .venv/bin/activate

echo
echo "[1/4] Running single-profile CSV demo..."
PYTHONPATH=src python src/profile_from_csv.py

echo
echo "[2/4] Running batch profile pipeline..."
PYTHONPATH=src python src/batch_profiles.py

echo
echo "[3/4] Generating batch report..."
PYTHONPATH=src python src/generate_batch_report.py

echo
echo "[4/4] Pipeline complete."
echo "Key outputs:"
echo "  - docs/sample_profile_result.png"
echo "  - docs/batch_outputs/batch_summary.csv"
echo "  - docs/batch_outputs/batch_comparison.png"
echo "  - docs/batch_report.md"
