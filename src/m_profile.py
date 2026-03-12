from __future__ import annotations

import numpy as np


def water_vapor_pressure_hpa(temp_c: float, rh_percent: float) -> float:
    """
    Approximate water vapor pressure in hPa using Tetens formula.
    """
    es = 6.112 * np.exp((17.67 * temp_c) / (temp_c + 243.5))
    return (rh_percent / 100.0) * es


def modified_refractivity_m_units(
    temp_c: float,
    pressure_hpa: float,
    rh_percent: float,
    height_m: float,
) -> float:
    """
    Compute modified refractivity (M-units).

    M(h) = 77.6/T * (P + 4810e/T) + 0.157h

    where:
      T = temperature in Kelvin
      P = pressure in hPa
      e = water vapor pressure in hPa
      h = height in meters
    """
    temp_k = temp_c + 273.15
    e = water_vapor_pressure_hpa(temp_c, rh_percent)
    m = (77.6 / temp_k) * (pressure_hpa + (4810.0 * e / temp_k)) + (0.157 * height_m)
    return float(m)


def profile_from_arrays(
    temp_c: np.ndarray,
    pressure_hpa: np.ndarray,
    rh_percent: np.ndarray,
    height_m: np.ndarray,
) -> np.ndarray:
    """
    Vectorized M-profile computation.
    """
    temp_k = temp_c + 273.15
    es = 6.112 * np.exp((17.67 * temp_c) / (temp_c + 243.5))
    e = (rh_percent / 100.0) * es
    m = (77.6 / temp_k) * (pressure_hpa + (4810.0 * e / temp_k)) + (0.157 * height_m)
    return m


if __name__ == "__main__":
    temp_c = 38.0
    pressure_hpa = 1005.0
    rh_percent = 85.0
    height_m = 10.0

    m = modified_refractivity_m_units(temp_c, pressure_hpa, rh_percent, height_m)
    print(f"M-profile value at {height_m} m: {m:.2f} M-units")
