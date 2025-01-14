import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
import joblib

# Train Fault Prediction Model
def train_fault_predictor():
    data = pd.read_csv("../data/device_data.csv")
    data['fault'] = (data['temperature'] > 40) | (data['energy_consumption'] > 150)
    X = data[["temperature", "energy_consumption"]]
    y = data["fault"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    joblib.dump(model, "../models/fault_predictor.pkl")
    print("Fault predictor model trained and saved!")

# Train Anomaly Detection Model
def train_anomaly_detector():
    data = pd.read_csv("../data/device_data.csv")
    X = data[["temperature", "energy_consumption"]]
    
    model = IsolationForest(contamination=0.05)
    model.fit(X)
    joblib.dump(model, "../models/anomaly_detector.pkl")
    print("Anomaly detector model trained and saved!")

if __name__ == "__main__":
    train_fault_predictor()
    train_anomaly_detector()
