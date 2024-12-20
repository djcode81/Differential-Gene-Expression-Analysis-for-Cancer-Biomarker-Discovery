import pandas as pd
import numpy as np

# Input and output file paths
input_file = "GSE15852_series_matrix.txt"  
output_file = "processed_expression_data.csv"

# Loading dataset
print("=== Loading Original Dataset ===")
try:
    with open(input_file) as f:
        # Skip metadata until the actual data table starts
        lines = f.readlines()
        start_idx = [i for i, line in enumerate(lines) if line.startswith("!series_matrix_table_begin")][0] + 1
        end_idx = [i for i, line in enumerate(lines) if line.startswith("!series_matrix_table_end")][0]
        expression_data = pd.read_csv(input_file, sep="\t", skiprows=start_idx, nrows=end_idx - start_idx - 1, index_col=0)
    print(f"Original dataset loaded successfully with shape: {expression_data.shape}")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

#  Removeing metadata and focus on expression values
print("\n=== Cleaning Data ===")
try:
    # Ensure column names are consistent
    expression_data.columns = expression_data.columns.str.strip()
    expression_data = expression_data.astype(float)
    print("Metadata removed, dataset cleaned.")
except Exception as e:
    print(f"Error during data cleaning: {e}")
    exit()

# Step 3: Log2 transformation
print("\n=== Log2 Transformation ===")
try:
    expression_data = expression_data.applymap(lambda x: np.log2(x + 1) if isinstance(x, (int, float)) else x)
    print("Log2 transformation applied successfully.")
except Exception as e:
    print(f"Error during Log2 transformation: {e}")
    exit()

# Step 4: Filter low-expression genes
print("\n=== Filtering Low-Expression Genes ===")
try:
    threshold = 1  # Adjust based on the dataset
    filtered_data = expression_data.loc[expression_data.mean(axis=1) > threshold]
    print(f"Filtered dataset shape (after removing low-expression genes): {filtered_data.shape}")
except Exception as e:
    print(f"Error during gene filtering: {e}")
    exit()

# Step 5: Save the processed data
print("\n=== Saving Processed Data ===")
try:
    filtered_data.to_csv(output_file)
    print(f"Processed data saved to {output_file}")
except Exception as e:
    print(f"Error saving processed data: {e}")
    exit()
