from sklearn.metrics import classification_report
import joblib
import pandas as pd

def save_evaluation_report(model_path, test_data_path, output_file):
    """Save the classification report to a file."""
    model = joblib.load(model_path)
    data = pd.read_csv(test_data_path)
    X = data.drop(columns=["target"])
    y = data["target"]
    
    y_pred = model.predict(X)
    report = classification_report(y, y_pred)
    
    with open(output_file, 'w') as f:
        f.write(report)

if __name__ == "__main__":
    model_file = "models/ebola_predictor_rf.pkl"
    test_data_file = "data/processed/ebola_features_test.csv"
    output_report_file = "results/evaluation_metrics/classification_report.txt"
    save_evaluation_report(model_file, test_data_file, output_report_file)
