# PACL Layer 1 – Initial Results

## Summary

This repository demonstrates a first-pass Layer 1 PACL artifact:
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

The demo also maps each atmospheric profile to a simple sensing-state interpretation:

| Case | Duct Risk | SWIR Quality | Radar Stability |
|---|---|---|---|
| Clear | Low | High | High |
| Hazy | Moderate | Medium | Medium |
| Duct-risk | High | Medium | Low |

## Interpretation

The purpose of this initial prototype is not operational prediction.
It is to demonstrate the PACL principle:

**atmospheric state can be converted into sensing context.**

This supports the broader PACL research direction:
Atmosphere → Sensing → Fusion → Edge
