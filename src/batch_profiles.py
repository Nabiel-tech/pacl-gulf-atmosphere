from __future__ import annotations

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


def process_profile(csv_path: Path, output_dir: Path) -> dict:
    df = pd.read_csv(csv_path)

    required_columns = {"height_m", "temp_c", "pressure_hpa", "rh_percent"}
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"{csv_path.name}: missing required columns {sorted(missing)}")

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

    plot_name = f"{csv_path.stem}_m_profile.png"
    plot_path = output_dir / plot_name

    plt.figure(figsize=(6, 8))
    plt.plot(m_profile, height_m, marker="o")
    plt.xlabel("Modified Refractivity (M-units)")
    plt.ylabel("Height (m)")
    plt.title(f"{csv_path.stem} | {result['classification']}")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(plot_path, dpi=150)
    plt.close()

    return {
        "file": csv_path.name,
        "classification": result["classification"],
        "duct_risk": result["duct_risk"],
        "swir_quality": result["swir_quality"],
        "radar_stability": result["radar_stability"],
        "min_gradient": result["min_gradient"],
        "mean_gradient": result["mean_gradient"],
        "plot_file": plot_name,
    }


def main() -> None:
    input_dir = Path("data/raw/profiles")
    output_dir = Path("docs/batch_outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_files = sorted(input_dir.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {input_dir}")

    results = []
    for csv_file in csv_files:
        result = process_profile(csv_file, output_dir)
        results.append(result)
        print(
            f"{result['file']}: "
            f"class={result['classification']} | "
            f"duct={result['duct_risk']} | "
            f"SWIR={result['swir_quality']} | "
            f"Radar={result['radar_stability']}"
        )

    summary_df = pd.DataFrame(results)
    summary_path = output_dir / "batch_summary.csv"
    summary_df.to_csv(summary_path, index=False)

    print(f"\nSaved batch summary to {summary_path}")
    print(f"Saved {len(results)} plot(s) to {output_dir}")


if __name__ == "__main__":
    main()
