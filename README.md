# Machine Learning Coursework Experiments

A curated set of smaller machine learning experiments: compressed sensing, PCA, regression, SVM, gene networks, and graph embeddings.

## Overview

import matplotlib.pyplot as plt from sklearn.model_selection import train_test_split mat = scipy.io.loadmat('POS.mat') from sklearn.linear_model import LogisticRegression import matplotlib.pyplot as plt def error_calc(alpha,n,d,beta): import matplotlib.pyplot as plt https://tcga-xena-hub.s3.us-east-1.amazonaws.com/download/TCGA.BRCA.sampleMap%2FGistic2_CopyNumber_Gistic2_all_data_by_genes.gz The file is named: TCGA.BRCA.sampleMap_Gistic2_CopyNumber_Gistic2_all_data_by_genes

## Repository Structure

- `notebooks/`: cleaned Jupyter/Colab notebooks with descriptive filenames.
- `src/`: standalone Python scripts where available.
- `requirements.txt`: inferred Python dependencies.
- `SOURCE_MAP.md`: traceability back to original Google Drive files.

## Key Files

- `src/embedding.py` from `embedding.py`
- `src/svm-lr-risk.py` from `SVM_LR_Risk.py`
- `src/gene-2024.py` from `Gene_2024.py`
- `src/panda.py` from `Panda.py`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Open notebooks with JupyterLab, VS Code, or Google Colab. Some notebooks expect external public datasets and may need path updates before execution.

## Data Notes

Large datasets, raw CSV exports, screenshots, PDFs, private download URLs, and assignment prompt files were intentionally excluded from this public-ready package.

## Suggested GitHub Repository

`ml-coursework-experiments`

## Main Dependencies

- `matplotlib`
- `networkx`
- `numpy`
- `pandas`
- `scikit-learn`
- `scipy`
