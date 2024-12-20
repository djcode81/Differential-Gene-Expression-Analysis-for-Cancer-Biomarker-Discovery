import pandas as pd

# Loading the differential expression results
results_df = pd.read_csv("differential_expression_results.csv")

# Sorting by t-statistic to identify upregulated and downregulated genes
upregulated_genes = results_df.sort_values(by="t-statistic", ascending=False).head(10)
downregulated_genes = results_df.sort_values(by="t-statistic", ascending=True).head(10)

# Saving the results
upregulated_genes.to_csv("top_10_upregulated_genes.csv", index=False)
downregulated_genes.to_csv("top_10_downregulated_genes.csv", index=False)

print("saved to 'top_10_upregulated_genes.csv' and 'top_10_downregulated_genes.csv'.")
