import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from tensorflow.keras.models import load_model
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Loading the Saved Model
model = load_model("cancer_classifier.h5")

# Loading the Test Dataset
data = pd.read_csv("/Users/dheerajpv/Documents/compbio_final/processed_expression_data.csv", index_col=0)
metadata = pd.read_csv("/Users/dheerajpv/Documents/compbio_final/updated_metadata_with_group.csv")

# Metadata with Expression Data
metadata = metadata[metadata["Sample_geo_accession"].isin(data.columns)]
data = data[metadata["Sample_geo_accession"]]

# Labels
y = metadata["Group"].map({"Normal": 0, "Cancer": 1}).values

# Transpose data for model input
X = data.T.values

# Dimensionality Reduction with PCA
pca = PCA(n_components=50)
X = pca.fit_transform(X)

# Normalizing Data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Evaluation
predictions = model.predict(X)
# probabilities to binary predictions
predicted_classes = (predictions > 0.5).astype(int).flatten()

# Performance Metrics
print("Confusion Matrix:")
print(confusion_matrix(y, predicted_classes))
print("\nClassification Report:")
print(classification_report(y, predicted_classes))
print(f"\nAccuracy: {accuracy_score(y, predicted_classes) * 100:.2f}%")

# Results to File
results = pd.DataFrame({
    "Sample": metadata["Sample_geo_accession"],
    "True_Label": y,
    "Predicted_Label": predicted_classes
})
results.to_csv("model_test_results.csv", index=False)
print("\nTest results saved to 'model_test_results.csv'")
