import pandas as pd
import joblib

# Load the anomaly detection model
def load_model(model_path="../models/anomaly_detector.pkl"):
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        print("Anomaly detection model not found. Please train the model first.")
        return None

# Detect anomalies in the IoT data
def detect_anomalies(data_path="../data/device_data.csv", model_path="../models/anomaly_detector.pkl"):
    # Load the data
    try:
        data = pd.read_csv(data_path)
    except FileNotFoundError:
        print("Device data not found. Please generate data first.")
        return None
    
    # Check required columns
    required_columns = ["temperature", "energy_consumption"]
    if not all(column in data.columns for column in required_columns):
        print(f"Required columns {required_columns} not found in data.")
        return None
    
    # Load the model
    model = load_model(model_path)
    if model is None:
        return None
    
    # Extract features for anomaly detection
    features = data[required_columns]
    
    # Predict anomalies (-1 = anomaly, 1 = normal)
    predictions = model.predict(features)
    data["is_anomaly"] = predictions == -1  # True if anomaly
    
    # Save anomalies to a separate file for review
    anomalies = data[data["is_anomaly"]]
    anomalies.to_csv("../data/anomalies_detected.csv", index=False)
    print(f"Anomalies detected and saved to ../data/anomalies_detected.csv")
    return anomalies

if __name__ == "__main__":
    # Run the anomaly detection script
    anomalies = detect_anomalies()
    if anomalies is not None and not anomalies.empty:
        print(f"Anomalies detected:\n{anomalies}")
    else:
        print("No anomalies detected.")
