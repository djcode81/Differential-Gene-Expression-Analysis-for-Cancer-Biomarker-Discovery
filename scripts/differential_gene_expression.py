import pandas as pd
from scipy.stats import ttest_ind

# Load the processed and aligned datasets
expression_data = pd.read_csv("processed_expression_data.csv", index_col=0)
metadata = pd.read_csv("updated_metadata_with_group.csv")  # Replace with correct metadata file

# Ensure Sample IDs are aligned
metadata_samples = metadata["Sample_geo_accession"]
expression_samples = expression_data.columns

if not all(sample in expression_samples for sample in metadata_samples):
    raise ValueError("Some metadata samples are missing in the expression data!")

# Define groupings
normal_samples = metadata.loc[metadata["Group"] == "Normal", "Sample_geo_accession"]
cancer_samples = metadata.loc[metadata["Group"] == "Cancer", "Sample_geo_accession"]

# Ensure groups are not empty
if normal_samples.empty or cancer_samples.empty:
    raise ValueError("One or both groups are empty. Check your metadata.")

# Extract group data
normal_data = expression_data[normal_samples]
cancer_data = expression_data[cancer_samples]

# Perform t-test
results = []
for gene in expression_data.index:
    normal_values = normal_data.loc[gene]
    cancer_values = cancer_data.loc[gene]
    stat, pval = ttest_ind(normal_values, cancer_values, equal_var=False)
    results.append({"Gene": gene, "t-statistic": stat, "p-value": pval})

# Convert results to DataFrame
results_df = pd.DataFrame(results)

# Adjust p-values for multiple testing (optional)
from statsmodels.stats.multitest import multipletests
results_df["adjusted_p-value"] = multipletests(results_df["p-value"], method="fdr_bh")[1]

# Save results
results_df.to_csv("differential_expression_results.csv", index=False)
print("Analysis completed. Results saved to 'differential_expression_results.csv'.")




