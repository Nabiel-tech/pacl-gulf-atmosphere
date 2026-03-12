from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    batch_dir = Path("docs/batch_outputs")
    summary_path = batch_dir / "batch_summary.csv"
    report_path = Path("docs/batch_report.md")
    combined_plot_path = batch_dir / "batch_comparison.png"

    if not summary_path.exists():
        raise FileNotFoundError(f"Missing summary file: {summary_path}")

    df = pd.read_csv(summary_path)

    # Combined comparison chart: min vs mean gradient
    plt.figure(figsize=(7, 5))
    for _, row in df.iterrows():
        plt.scatter(row["mean_gradient"], row["min_gradient"], s=90)
        plt.text(
            row["mean_gradient"],
            row["min_gradient"],
            row["file"],
            fontsize=8,
            ha="left",
            va="bottom",
        )

    plt.xlabel("Mean Gradient")
    plt.ylabel("Minimum Gradient")
    plt.title("PACL Batch Profile Comparison")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(combined_plot_path, dpi=150)
    plt.close()

    lines = [
        "# PACL Layer 1 – Batch Report",
        "",
        "This report summarizes the current multi-profile PACL Layer 1 prototype.",
        "",
        "## Summary Table",
        "",
        "| File | Classification | Duct Risk | SWIR Quality | Radar Stability | Min Gradient | Mean Gradient |",
        "|---|---|---|---|---|---:|---:|",
    ]

    for _, row in df.iterrows():
        lines.append(
            f"| {row['file']} | {row['classification']} | {row['duct_risk']} | "
            f"{row['swir_quality']} | {row['radar_stability']} | "
            f"{row['min_gradient']:.3f} | {row['mean_gradient']:.3f} |"
        )

    lines += [
        "",
        "## Interpretation",
        "",
        "This batch prototype demonstrates that PACL Layer 1 can process multiple atmospheric profiles,",
        "compute modified refractivity, derive simple sensing-state classifications, and summarize results",
        "in a reproducible form.",
        "",
        "## Generated Files",
        "",
        f"- Summary CSV: `{summary_path}`",
        f"- Combined comparison figure: `{combined_plot_path}`",
        "",
        "## Current Research Value",
        "",
        "The pipeline is now able to act as a small test harness for:",
        "",
        "- comparing atmospheric profile classes",
        "- calibrating environment classification thresholds",
        "- preparing Layer 1 results for downstream sensing and fusion work",
    ]

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Saved report to {report_path}")
    print(f"Saved combined comparison figure to {combined_plot_path}")


if __name__ == "__main__":
    main()
