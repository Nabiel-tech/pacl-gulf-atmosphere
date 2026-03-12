# PACL Layer 1 – Batch Profile Prototype

This prototype extends the single-profile PACL demo into a mini research pipeline.

## What it does

- reads multiple atmospheric profile CSV files
- computes modified refractivity (M-profile) for each
- classifies each profile into a sensing-state label
- saves one plot per profile
- writes a combined batch summary CSV

## Input folder

`data/raw/profiles/`

## Output folder

`docs/batch_outputs/`

## Purpose

This upgrade demonstrates that PACL Layer 1 can scale from a single demonstrator
to a small reproducible profile-processing workflow.

That is the first step toward a more realistic research pipeline for degraded-environment sensing.
