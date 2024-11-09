# Ebola Prediction Project

## Project Overview

This project aims to predict the genetic shifts of future Ebola outbreaks using machine learning models trained on genomic data. By analyzing historical sequences and identifying patterns in protein and peptide shifts, we aim to forecast the potential genomic makeup of emergent Ebola strains. The goal is to create a predictive tool that can help inform public health responses and improve outbreak preparedness.

## Research Focus

- **Genomic Data**: We work with genomic sequences from NCBI, focusing on raw nucleotide (FASTA) and protein data, transcribed amino acids, and protein shifts over time.
- **Data Analysis**: The project focuses on feature extraction from these sequences, using machine learning techniques to identify patterns in peptide and protein shifts that may indicate potential changes in the Ebola virus's genetic code.
- **AI/ML Models**: We employ machine learning and deep learning models to make predictions about future Ebola strains. This includes analyzing trends in both protein and nucleotide sequences.

## Objectives

- Predict the genetic composition of future Ebola strains.
- Identify potential mutations that could affect transmission, virulence, or resistance.
- Provide actionable insights into potential outbreak scenarios.

## Installation

### Dependencies

We recommend setting up a virtual environment for the project. You can either use `pip` or `conda` to install the necessary dependencies.

1. Clone this repository:
    ```bash
    git clone https://github.com/your-org/ebola-prediction.git
    cd ebola-prediction
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

    Or, if using `conda`:
    ```bash
    conda env create -f environment.yml
    conda activate ebola-prediction
    ```

### Data Setup

- The `data/raw/` folder contains the raw genomic sequences (FASTA format).
- To download the necessary genomic data from NCBI, follow the instructions in the `data/` folder.
- Processed data should be stored in the `data/processed/` folder after running the preprocessing scripts.

## Project Structure

### `data/`
Contains raw, processed, and external data sources for analysis.

- `raw/`: Raw sequence data (FASTA, GenBank, etc.).
- `processed/`: Cleaned and feature-engineered data.
- `external/`: Data from external databases or sources.

### `notebooks/`
Contains Jupyter notebooks for data analysis and model development.

- `data_preprocessing.ipynb`: Explore and clean the raw genomic data.
- `model_training.ipynb`: Train machine learning models to predict Ebola strain shifts.
- `exploratory_analysis.ipynb`: Initial exploratory data analysis (EDA) and visualizations.

### `scripts/`
Contains Python scripts for running the project.

- `preprocess_data.py`: Script to clean, filter, and preprocess genomic data.
- `train_model.py`: Script to train AI/ML models on processed data.
- `evaluate_model.py`: Evaluate the trained models and analyze performance.
- `utils.py`: Helper functions for sequence manipulation, feature extraction, and more.

### `models/`
Store your trained machine learning models and model configuration files here.

- Example model files: `model_1.h5`, `model_2.pkl`.
- `config.yaml`: Model configuration and parameters.

### `results/`
Contains the output of model evaluations, predictions, and results.

- `figures/`: Visualizations of results and performance metrics.
- `predictions/`: Predictions made by trained models on new genomic sequences.
- `evaluation_metrics/`: Performance metrics such as accuracy, precision, recall, F1-score.

## Usage

1. **Preprocess Data**: Clean and prepare the raw genomic data:
    ```bash
    python scripts/preprocess_data.py
    ```

2. **Train Model**: Train the machine learning models using the processed data:
    ```bash
    python scripts/train_model.py
    ```

3. **Evaluate Model**: Assess model performance:
    ```bash
    python scripts/evaluate_model.py
    ```

4. **Make Predictions**: Use the trained models to predict future Ebola strains:
    ```bash
    python scripts/predict.py
    ```

## Contributing

We welcome contributions from the scientific and data science communities. If you would like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them.
4. Push to your fork (`git push origin feature-name`).
5. Open a pull request for review.

## Acknowledgments

This project uses data and tools from various resources, including NCBI and other scientific databases. We would like to acknowledge the open-source community for providing invaluable software tools, and thank the global scientific community for ongoing research into Ebola and infectious diseases.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

