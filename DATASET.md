# PACL Gulf Atmosphere Dataset

## Overview

This dataset contains synthetic atmospheric vertical profiles representing
typical coastal atmospheric conditions in the Arabian Gulf.

The dataset is used to demonstrate the PACL Layer 1 prototype for
environment classification based on modified refractivity gradients.

The goal is to evaluate how atmospheric conditions influence sensing
quality for remote sensing and radar propagation.

---

## Geographic Context

Profiles represent Gulf coastal environments:

• Doha  
• Mesaieed  
• Dukhan  

These locations were selected to illustrate typical coastal atmospheric
conditions in Qatar.

---

## Atmospheric Cases

Each site contains multiple atmospheric scenarios:

CLEAR  
Stable atmosphere with weak refractivity gradients.

HAZY  
Moderate humidity gradients producing transitional sensing conditions.

DUCT_RISK  
Strong negative refractivity gradients potentially producing
atmospheric ducting conditions.

---

## File Structure

Profiles are stored as CSV files.

Example file name:

site_date_case.csv

Example:

doha_2026-03-12_clear.csv

---

## Variables

Each profile contains:

height_m  
Altitude above ground level.

temp_c  
Air temperature in degrees Celsius.

pressure_hpa  
Atmospheric pressure.

rh_percent  
Relative humidity.

---

## Derived Quantities

The PACL pipeline computes:

Modified Refractivity (M)

M-profile vertical gradients

Environment classification:

CLEAR  
TRANSITIONAL  
DUCT_RISK

---

## Limitations

This dataset is intended for demonstration purposes.

Profiles are synthetic approximations of Gulf atmospheric behavior and
should not be interpreted as real meteorological measurements.

Future versions may incorporate:

• radiosonde data  
• coastal sensor measurements  
• temporal atmospheric variation

---

## Usage

The dataset can be processed using the PACL Layer 1 pipeline:

./run_pacl_layer1.sh

Outputs include:

• M-profile plots  
• environment classification  
• batch comparison figures  
• site comparison visualizations

---

## License

Dataset released under the MIT License with the repository.
