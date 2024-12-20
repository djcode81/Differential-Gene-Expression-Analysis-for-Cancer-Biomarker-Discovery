import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Filepath for the processed data
file_path = "processed_expression_data.csv"

# === Step 1: Load Processed Dataset ===
print("\n=== Loading Processed Dataset ===")
try:
    expression_data = pd.read_csv(file_path, index_col=0)
    print(f"Processed dataset loaded successfully with shape: {expression_data.shape}")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# === Step 2: Summary Statistics ===
print("\n=== Summary Statistics ===")
summary_stats = expression_data.describe()
print(summary_stats)

# Save summary stats for reference
summary_stats.to_csv("summary_statistics.csv")
print("Summary statistics saved to summary_statistics.csv")

# === Step 3: Check for Missing Data ===
print("\n=== Checking for Missing Values ===")
missing_values = expression_data.isnull().sum().sum()
print(f"Total missing values: {missing_values}")

if missing_values > 0:
    print("Warning: Missing values detected! Please handle them appropriately.")

# === Step 4: Visualize Expression Value Distribution ===
print("\n=== Visualizing Expression Value Distribution ===")
plt.figure(figsize=(12, 6))
sns.boxplot(data=expression_data)
plt.title("Boxplot of Expression Values Across Samples")
plt.xlabel("Samples")
plt.ylabel("Expression Value")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("expression_boxplot.png")
plt.show()
print("Boxplot saved as expression_boxplot.png")

# === Step 5: Identify Most Variable Genes ===
print("\n=== Identifying Most Variable Genes ===")
expression_data['variance'] = expression_data.var(axis=1)
most_variable_genes = expression_data.nlargest(50, 'variance')  # Top 50 most variable genes
most_variable_genes.drop('variance', axis=1, inplace=True)
most_variable_genes.to_csv("most_variable_genes.csv")
print("Most variable genes saved to most_variable_genes.csv")

# === Step 6: Heatmap for Most Variable Genes ===
print("\n=== Heatmap: Most Variable Genes ===")
plt.figure(figsize=(10, 8))
sns.heatmap(most_variable_genes, cmap="coolwarm", cbar_kws={'label': 'Expression Value'})
plt.title("Heatmap of Top 50 Most Variable Genes")
plt.xlabel("Samples")
plt.ylabel("Genes")
plt.tight_layout()
plt.savefig("most_variable_genes_heatmap.png")
plt.show()
print("Heatmap saved as most_variable_genes_heatmap.png")

print("\n=== EDA + Basic Visualization Complete ===")
