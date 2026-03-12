from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    summary_path = Path("docs/batch_outputs/batch_summary.csv")
    output_path = Path("docs/batch_outputs/site_case_comparison.png")

    if not summary_path.exists():
        raise FileNotFoundError(f"Missing summary file: {summary_path}")

    df = pd.read_csv(summary_path)

    sites = ["doha", "mesaieed", "dukhan"]
    cases = ["clear", "hazy", "duct"]

    fig, ax = plt.subplots(figsize=(9, 5))

    x_positions = []
    labels = []
    y_values = []

    x = 0
    for site in sites:
        for case in cases:
            row = df[(df["site"] == site) & (df["case"] == case)]
            if not row.empty:
                y = float(row["mean_gradient"].iloc[0])
                x_positions.append(x)
                y_values.append(y)
                labels.append(f"{site}\n{case}")
                x += 1

    ax.bar(x_positions, y_values)
    ax.set_xticks(x_positions)
    ax.set_xticklabels(labels, rotation=0)
    ax.set_ylabel("Mean Gradient")
    ax.set_title("PACL Layer 1 Site/Case Comparison")
    ax.grid(True, axis="y")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

    print(f"Saved site comparison figure to {output_path}")


if __name__ == "__main__":
    main()
