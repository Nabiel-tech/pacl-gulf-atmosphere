from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from m_profile import profile_from_arrays


def main() -> None:
    height_m = np.linspace(0, 100, 101)
    temp_c = 38.0 - 0.05 * height_m
    pressure_hpa = 1008.0 - 0.12 * height_m
    rh_percent = 90.0 - 0.25 * height_m

    m_profile = profile_from_arrays(
        temp_c=temp_c,
        pressure_hpa=pressure_hpa,
        rh_percent=rh_percent,
        height_m=height_m,
    )

    plt.figure(figsize=(6, 8))
    plt.plot(m_profile, height_m)
    plt.xlabel("Modified Refractivity (M-units)")
    plt.ylabel("Height (m)")
    plt.title("Synthetic Gulf Coastal M-Profile")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("docs/synthetic_m_profile.png", dpi=150)
    print("Saved plot to docs/synthetic_m_profile.png")


if __name__ == "__main__":
    main()
