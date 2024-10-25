# Iris Flower Classification Project

This project uses the Iris flower dataset to explore data relationships, visualize features, and classify flower species using a Support Vector Machine (SVM) model. The trained model is saved with `pickle` for future predictions.

## Project Overview
This project performs the following:
1. Data analysis and visualization of the Iris dataset.
2. Training an SVM classifier to predict the Iris species.
3. Saving the trained model for future use.

## Dataset
The Iris dataset, found in `data/IRIS.csv`, includes 150 samples with these features:
- `sepal_length`, `sepal_width`, `petal_length`, `petal_width`, and `species` (target).

## Installation
1. **Clone Repository**:
    -------------------------


2. **Install Requirements**:
   pip install -r requirements.txt
   *(Includes `numpy`, `pandas`, `matplotlib`, `seaborn`, and `scikit-learn`)*

## Usage
1. **Run Script**:
   python iris_classification.py

   This script loads data, visualizes relationships, trains the model, and saves it as `SVM.pickle`.

2. **Predict New Data**:
   After training, the model will output predictions for sample data and store the model for reuse.

## Project Structure

Iris_Flower_Classification_Model/
├── data/IRIS.csv              # Dataset
├── iris_classification.py      # Main script
└── SVM.pickle                  # Trained model file

## Results
- **Visualization**: Pair plots show feature relationships across species.
- **Model Evaluation**: The SVM classifier achieves good accuracy, shown in the classification report.


**Contributions are welcome!** Open an issue to discuss ideas or changes.