# PACL Layer 1 – Initial Results

## Summary

This repository demonstrates an initial Layer 1 PACL artifact:
modified refractivity (M-profile) computation for Gulf-like atmospheric conditions.

## Generated Outputs

### 1. Synthetic Gulf Coastal M-Profile
File: `docs/synthetic_m_profile.png`

This figure shows a synthetic vertical atmospheric profile converted into modified refractivity (M-units).

### 2. Weekend PACL Demo
File: `docs/weekend_pacl_demo.png`

This figure compares three atmospheric cases:

- clear
- hazy
- duct-risk

### 3. CSV-Driven Sample Profile Result
File: `docs/sample_profile_result.png`  
File: `docs/sample_profile_result.txt`

This output demonstrates a reproducible input-to-result pipeline:

- load profile CSV
- compute M-profile
- classify sensing state
- save figure and text summary

## Interpretation

The purpose of this prototype is not operational prediction.
It demonstrates the PACL principle:

**atmospheric state can be converted into sensing context.**

This supports the broader PACL research direction:

Atmosphere → Sensing → Fusion → Edge
