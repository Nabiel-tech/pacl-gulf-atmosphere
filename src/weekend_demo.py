from __future__ import annotations

import os
import numpy as np
import matplotlib.pyplot as plt

from m_profile import profile_from_arrays


def classify_environment(m_profile: np.ndarray) -> dict:
    gradient = np.gradient(m_profile)
    min_grad = float(np.min(gradient))

    if min_grad < -15.0:
        duct_risk = "High"
        radar = "Low"
        swir = "Medium"
    elif min_grad < -5.0:
        duct_risk = "Moderate"
        radar = "Medium"
        swir = "Medium"
    else:
        duct_risk = "Low"
        radar = "High"
        swir = "High"

    return {
        "duct_risk": duct_risk,
        "radar_stability": radar,
        "swir_quality": swir,
    }

def build_case(case_name: str):
    h = np.linspace(0, 100, 101)

    if case_name == "clear":
        temp = 34.0 - 0.03 * h
        pressure = 1008.0 - 0.11 * h
        rh = 60.0 - 0.10 * h
    elif case_name == "hazy":
        temp = 39.0 - 0.06 * h
        pressure = 1007.0 - 0.12 * h
        rh = 88.0 - 0.22 * h
    elif case_name == "duct_risk":
        temp = 40.0 - 0.10 * h
        pressure = 1009.0 - 0.10 * h
        rh = 95.0 - 0.45 * h
    else:
        raise ValueError(f"Unknown case: {case_name}")

    m = profile_from_arrays(temp, pressure, rh, h)
    return h, m


def main() -> None:
    os.makedirs("docs", exist_ok=True)

    cases = ["clear", "hazy", "duct_risk"]
    results = []

    plt.figure(figsize=(7, 8))

    for case in cases:
        h, m = build_case(case)
        cls = classify_environment(m)
        results.append((case, cls))
        plt.plot(m, h, label=f"{case} | duct={cls['duct_risk']}")

    plt.xlabel("Modified Refractivity (M-units)")
    plt.ylabel("Height (m)")
    plt.title("Weekend PACL Demo: Atmospheric Profiles and Sensing State")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("docs/weekend_pacl_demo.png", dpi=150)

    print("\nWeekend PACL Demo Results")
    print("-" * 60)
    print(f"{'Case':<12}{'Duct Risk':<12}{'SWIR':<12}{'Radar':<12}")
    print("-" * 60)
    for case, cls in results:
        print(
            f"{case:<12}"
            f"{cls['duct_risk']:<12}"
            f"{cls['swir_quality']:<12}"
            f"{cls['radar_stability']:<12}"
        )
    print("-" * 60)
    print("Saved figure to docs/weekend_pacl_demo.png")


if __name__ == "__main__":
    main()
