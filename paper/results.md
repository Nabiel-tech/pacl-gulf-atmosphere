# PACL Layer 1 – Results Summary

## Objective

The PACL Layer 1 prototype evaluates whether atmospheric state can be converted into a simple sensing-environment classification using modified refractivity gradients.

The goal is not operational prediction but demonstration of a reproducible sensing-state pipeline.

---

## Dataset

Profiles represent three Gulf coastal environments:

- Doha
- Mesaieed
- Dukhan

Each site includes atmospheric scenarios:

- clear
- hazy
- duct-risk

Profiles are represented as vertical atmospheric samples containing:

- temperature
- pressure
- relative humidity
- height

The repository currently contains:

3 sites × 3 cases × multiple dates

---

## Processing Pipeline

The pipeline performs:

1. compute modified refractivity (M-profile)
2. derive gradient features
3. classify sensing environment

Outputs include:

- per-profile M-profile plots
- batch summary table
- multi-site comparison figures

---

## Observed Behavior

Across sites, the classification logic consistently identifies:

CLEAR  
→ weak gradients  
→ stable sensing conditions

TRANSITIONAL  
→ moderate negative gradients  
→ degraded sensing conditions

DUCT_RISK  
→ strong negative gradients  
→ potential refractive ducting

---

## Interpretation

These results demonstrate that simple refractivity gradient features can provide a first-order indicator of degraded sensing environments in Gulf coastal atmospheres.

The prototype therefore serves as a minimal Layer 1 atmospheric awareness module.

Further work would incorporate:

- temporal variation
- real radiosonde or sensor data
- probabilistic classification models
