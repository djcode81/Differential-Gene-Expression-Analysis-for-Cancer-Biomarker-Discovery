import pandas as pd

# Load the results
results = pd.read_csv("differential_expression_results.csv")

# Define significance threshold
significant_genes = results[results["adjusted_p-value"] < 0.05]

# Save the filtered results
significant_genes.to_csv("significant_genes.csv", index=False)
print(f"Number of significant genes: {len(significant_genes)}")
print("Significant genes saved to 'significant_genes.csv'.")
