import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load expression data and results
expression_data = pd.read_csv("processed_expression_data.csv", index_col=0)
results = pd.read_csv("differential_expression_results.csv")

# Filter for significant genes
significant_genes = results[results["adjusted_p-value"] < 0.05].sort_values(by="t-statistic", ascending=False)

# Select top 50 significant genes (or adjust this number as needed)
top_genes = significant_genes.head(50)["Gene"]

# Subset expression data for the top genes
heatmap_data = expression_data.loc[top_genes]

# Standardize the data for visualization
heatmap_data = (heatmap_data - heatmap_data.mean(axis=1).values.reshape(-1, 1)) / heatmap_data.std(axis=1).values.reshape(-1, 1)

# Create heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(heatmap_data, cmap="vlag", xticklabels=False, yticklabels=top_genes, cbar=True)
plt.title("Heatmap of Top 50 Significant Genes")
plt.xlabel("Samples")
plt.ylabel("Genes")
plt.tight_layout()
plt.show()
