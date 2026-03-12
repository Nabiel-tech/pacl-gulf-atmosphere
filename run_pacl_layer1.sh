#!/usr/bin/env bash
set -euo pipefail

echo "=== PACL Layer 1 pipeline start ==="

if [ ! -d ".venv" ]; then
  echo "ERROR: .venv not found. Create and activate the virtual environment first."
  exit 1
fi

source .venv/bin/activate

echo
echo "[1/5] Running single-profile CSV demo..."
PYTHONPATH=src python src/profile_from_csv.py

echo
echo "[2/5] Running batch profile pipeline..."
PYTHONPATH=src python src/batch_profiles.py

echo
echo "[3/5] Generating batch report..."
PYTHONPATH=src python src/generate_batch_report.py

echo
echo "[4/5] Generating site comparison figure..."
PYTHONPATH=src python src/site_comparison.py

echo
echo "[5/5] Pipeline complete."
echo "Key outputs:"
echo "  - docs/sample_profile_result.png"
echo "  - docs/batch_outputs/batch_summary.csv"
echo "  - docs/batch_outputs/batch_comparison.png"
echo "  - docs/batch_outputs/site_case_comparison.png"
echo "  - docs/batch_report.md"
