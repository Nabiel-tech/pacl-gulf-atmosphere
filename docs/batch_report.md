# PACL Layer 1 – Batch Report

This report summarizes the current multi-profile PACL Layer 1 prototype.

## Summary Table

| File | Classification | Duct Risk | SWIR Quality | Radar Stability | Min Gradient | Mean Gradient |
|---|---|---|---|---|---:|---:|
| clear_profile.csv | CLEAR | Low | High | High | -2.396 | -2.034 |
| duct_risk_profile.csv | DUCT_RISK | High | Medium | Low | -22.319 | -16.018 |
| hazy_profile.csv | TRANSITIONAL | Moderate | Medium | Medium | -10.640 | -8.640 |

## Interpretation

This batch prototype demonstrates that PACL Layer 1 can process multiple atmospheric profiles,
compute modified refractivity, derive simple sensing-state classifications, and summarize results
in a reproducible form.

## Generated Files

- Summary CSV: `docs/batch_outputs/batch_summary.csv`
- Combined comparison figure: `docs/batch_outputs/batch_comparison.png`

## Current Research Value

The pipeline is now able to act as a small test harness for:

- comparing atmospheric profile classes
- calibrating environment classification thresholds
- preparing Layer 1 results for downstream sensing and fusion work
