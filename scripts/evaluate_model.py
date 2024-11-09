import joblib
from sklearn.metrics import classification_report
import pandas as pd

def evaluate_model(model_path, data_path):
    """Evaluate the trained machine learning model."""
    # Load the trained model
    model = joblib.load(model_path)
    
    # Load the test data
    data = pd.read_csv(data_path)
    X = data.drop(columns=["target"])
    y = data["target"]
    
    # Make predictions
    y_pred = model.predict(X)

    # Print classification report (precision, recall, F1-score)
    print("Model Evaluation Results:")
    print(classification_report(y, y_pred))

if __name__ == "__main__":
    model_file = "models/ebola_predictor_rf.pkl"
    test_data_file = "data/processed/ebola_features_test.csv"  # Test dataset
    evaluate_model(model_file, test_data_file)
