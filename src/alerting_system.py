import pandas as pd
import joblib

def check_faults():
    model = joblib.load("../models/fault_predictor.pkl")
    data = pd.read_csv("../data/device_data.csv")
    predictions = model.predict(data[["temperature", "energy_consumption"]])
    faults = data[predictions == 1]
    if not faults.empty:
        print("Fault Alert:", faults)

def check_anomalies():
    model = joblib.load("../models/anomaly_detector.pkl")
    data = pd.read_csv("../data/device_data.csv")
    predictions = model.predict(data[["temperature", "energy_consumption"]])
    anomalies = data[predictions == -1]
    if not anomalies.empty:
        print("Anomaly Alert:", anomalies)

if __name__ == "__main__":
    check_faults()
    check_anomalies()
