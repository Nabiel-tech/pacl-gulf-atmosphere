from __future__ import annotations

import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from m_profile import profile_from_arrays


def classify_environment(m_profile: np.ndarray) -> dict:
    gradient = np.gradient(m_profile)
    min_grad = float(np.min(gradient))
    mean_grad = float(np.mean(gradient))

    if min_grad < -15.0:
        duct_risk = "High"
        radar = "Low"
        swir = "Medium"
        label = "DUCT_RISK"
    elif min_grad < -5.0:
        duct_risk = "Moderate"
        radar = "Medium"
        swir = "Medium"
        label = "TRANSITIONAL"
    else:
        duct_risk = "Low"
        radar = "High"
        swir = "High"
        label = "CLEAR"

    return {
        "classification": label,
        "duct_risk": duct_risk,
        "radar_stability": radar,
        "swir_quality": swir,
        "min_gradient": min_grad,
        "mean_gradient": mean_grad,
    }
    return {
        "classification": label,
        "duct_risk": duct_risk,
        "radar_stability": radar,
        "swir_quality": swir,
        "min_gradient": min_grad,
        "mean_gradient": mean_grad,
    }


def main() -> None:
    input_path = Path("data/raw/sample_profile.csv")
    output_plot = Path("docs/sample_profile_result.png")
    output_text = Path("docs/sample_profile_result.txt")

    if not input_path.exists():
        raise FileNotFoundError(f"Missing input file: {input_path}")

    os.makedirs("docs", exist_ok=True)

    df = pd.read_csv(input_path)

    required_columns = {"height_m", "temp_c", "pressure_hpa", "rh_percent"}
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    height_m = df["height_m"].to_numpy(dtype=float)
    temp_c = df["temp_c"].to_numpy(dtype=float)
    pressure_hpa = df["pressure_hpa"].to_numpy(dtype=float)
    rh_percent = df["rh_percent"].to_numpy(dtype=float)

    m_profile = profile_from_arrays(
        temp_c=temp_c,
        pressure_hpa=pressure_hpa,
        rh_percent=rh_percent,
        height_m=height_m,
    )

    result = classify_environment(m_profile)

    plt.figure(figsize=(6, 8))
    plt.plot(m_profile, height_m, marker="o")
    plt.xlabel("Modified Refractivity (M-units)")
    plt.ylabel("Height (m)")
    plt.title(f"Sample Profile M-Profile | {result['classification']}")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_plot, dpi=150)

    lines = [
        "PACL Layer 1 – Sample Profile Result",
        "=" * 40,
        f"Input file: {input_path}",
        f"Classification: {result['classification']}",
        f"Duct Risk: {result['duct_risk']}",
        f"SWIR Quality: {result['swir_quality']}",
        f"Radar Stability: {result['radar_stability']}",
        f"Minimum M-profile gradient: {result['min_gradient']:.4f}",
        f"Mean M-profile gradient: {result['mean_gradient']:.4f}",
        f"Output plot: {output_plot}",
    ]

    output_text.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines))


if __name__ == "__main__":
    main()
