import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model(data_path):
    """Train a machine learning model to predict Ebola strain shifts."""
    # Load the preprocessed data
    data = pd.read_csv(data_path)  # Assuming data is in CSV format after preprocessing
    X = data.drop(columns=["target"])  # Features
    y = data["target"]  # Labels (e.g., strain type or mutation)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train a RandomForest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.4f}")

    # Save the trained model
    model_path = "models/ebola_predictor_rf.pkl"
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    data_file = "data/processed/ebola_features.csv"  # Preprocessed data file
    train_model(data_file)
