import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load results
results = pd.read_csv("differential_expression_results.csv")

# Set thresholds for significance
pval_threshold = 0.05
tstat_threshold = 2  # Adjust based on your data

# Add columns for volcano plot
results["-log10(p-value)"] = -np.log10(results["p-value"])
results["Significant"] = (results["adjusted_p-value"] < pval_threshold) & (np.abs(results["t-statistic"]) > tstat_threshold)

# Create plot
plt.figure(figsize=(10, 6))
plt.scatter(results["t-statistic"], results["-log10(p-value)"], c='gray', alpha=0.7, label="Non-significant")
plt.scatter(
    results.loc[results["Significant"], "t-statistic"],
    results.loc[results["Significant"], "-log10(p-value)"],
    c='red', alpha=0.7, label="Significant"
)

# Add labels and legend
plt.axhline(y=-np.log10(pval_threshold), color='blue', linestyle='--', label=f"p-value < {pval_threshold}")
plt.axvline(x=-tstat_threshold, color='green', linestyle='--', label=f"t-statistic > {tstat_threshold}")
plt.axvline(x=tstat_threshold, color='green', linestyle='--')
plt.xlabel("t-statistic")
plt.ylabel("-log10(p-value)")
plt.title("Volcano Plot of Differential Gene Expression")
plt.legend()
plt.tight_layout()
plt.show()
