# Differential Gene Expression Analysis For Cancer Biomarker Discovery



under construction:


This project focuses on identifying biomarkers for breast cancer by performing differential gene expression (DGE) analysis and functional enrichment using DAVID (Database for Annotation, Visualization, and Integrated Discovery). Additionally, a machine learning (ML) component was incorporated as an added feature to classify cancerous vs. normal samples using gene expression profiles.

## Project Overview
- **Dataset:** Breast cancer gene expression data from GEO (GSE15852).
- **Objective:** Identify key biomarkers and pathways associated with cancer, and use ML to classify samples.
- **Tech Stack:** Python, TensorFlow, NumPy, SciPy, Matplotlib, Seaborn, Scikit-learn.

## Workflow
1. **Preprocessing:**
   - Removed irrelevant metadata and focused on expression data.
   - Applied log2 transformation to stabilize variance.
   - Filtered low-expression genes based on a mean expression threshold.
   - Merged metadata to label samples as "Cancer" or "Normal."

2. **Differential Expression Analysis:**
   - Performed t-tests to identify significantly upregulated and downregulated genes.
   - Adjusted p-values using the Benjamini-Hochberg method.
   - Identified 1741 significant genes for further analysis.

3. **Visualization and Functional Enrichment:**
   - Created heatmaps and volcano plots for top significant genes.
   - Conducted functional enrichment analysis with DAVID, identifying pathways like Glucagon Signaling pathway and Estrogen Signaling pathway involved in cancer progression.

4. **Machine Learning Classification:**
   - Applied PCA for dimensionality reduction (50 components).
   - Trained a TensorFlow-based binary classification model to distinguish between cancerous and normal samples.
   - Achieved test accuracies ranging from 87.21% to 89.53%.

## File Structure
```
.
├── data/
│   ├── updated_metadata_with_group.csv     # Metadata with sample labels
│   ├── differential_expression_results.csv # Results of DEG analysis
│   ├── top_10_upregulated_genes.csv        # Top 10 upregulated genes
│   ├── top_10_downregulated_genes.csv      # Top 10 downregulated genes
├── models/
│   └── cancer_classifier.h5                # Trained TensorFlow model
├── scripts/
│   ├── data_preprocessing.py               # Data preprocessing script
│   ├── differential_expression_results.py  # DGE analysis script
│   ├── ml_training2.py                     # Model training script
│   ├── test_ml.py                          # Model evaluation script
│   ├── heatmap.py and volancoplots.py      # Visualization scripts
├── outputs/
│   ├── most_variable_genes_heatmap.png     # Heatmap of top genes
│   ├── volcanoplot_DGEanalysis.png         # Volcano plot of DEG results
│   ├── model_test_results.csv              # Predictions on test set
└── README.md                               # Project README
```


## Results
- Identified 1741 significant genes, including ANGPTL4 and CDH1, as potential biomarkers.
- Highlighted key pathways like Glucagon Signaling and Estrogen Signaling involved in cancer progression.
- Achieved classification accuracies ranging from 87.21% to 89.53% using the ML model.

## Future Work
- Validate identified biomarkers experimentally to confirm clinical relevance.
- Explore more advanced ML models for improved classification.
- Expand functional enrichment analysis using additional tools.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Acknowledgments
- Gene Expression Omnibus (GEO) for providing the dataset.
- DAVID for functional annotation and enrichment analysis tools.
