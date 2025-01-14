# Smart IoT Monitoring and Predictive Maintenance System

## Overview

The **IoT Device Management System** is a Python-based application designed for monitoring and managing IoT devices in a smart city environment. The system includes functionalities for fault detection, anomaly detection, and real-time data monitoring via a web dashboard. By leveraging machine learning models, the system can predict potential device failures and detect unusual patterns in the data, minimizing downtime and enhancing operational efficiency.

### Key Features:
- **Real-time Data Monitoring**: View and interact with device data through an interactive web dashboard.
- **Predictive Fault Detection**: A machine learning model predicts when devices may fail based on key metrics like temperature and energy consumption.
- **Anomaly Detection**: The system detects abnormal patterns in device data using isolation forests, alerting users to potential issues.
- **Device Data Simulation**: Simulate IoT device data for testing purposes, allowing easy integration and evaluation.
- **Model Training**: Train fault prediction and anomaly detection models with historical device data.

## Prerequisites

Before using the system, make sure to have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- Virtual environment (optional, but recommended)
- Required Python libraries (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ssaish01/iot-device-management.git
   cd iot-device-management
   ```

2. **Set up a virtual environment (optional)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the project**: Ensure the following directory structure is in place for data and model storage:
   - `../data/`: For storing IoT device data.
   - `../models/`: For storing trained machine learning models.

## Running the System

To run the IoT Device Management System, execute the following steps:

### 1. **Generate IoT Device Data**:
Simulate IoT device data to use in the system:

```bash
python src/data_simulator.py
```

This will generate data for multiple IoT devices and save it as `device_data.csv` in the `../data/` directory.

### 2. **Train Machine Learning Models**:
Train both the fault prediction and anomaly detection models:

```bash
python src/model_training.py
```

This will generate the models (`fault_predictor.pkl` and `anomaly_detector.pkl`) and save them in the `../models/` directory.

### 3. **Run the Dashboard**:
Start the dashboard, which allows real-time monitoring of device data:

```bash
streamlit run src/dashboard.py
```

This will open the dashboard in your browser where you can view real-time device data and interact with the system.

### 4. **Check for Faults and Anomalies**:
You can manually check for faults and anomalies in the device data by running the respective scripts:

- **Fault detection**:
  ```bash
  python src/alerting_system.py --check_faults
  ```

- **Anomaly detection**:
  ```bash
  python src/anomaly_detection.py
  ```

### 5. **Run the Entire System**:
Alternatively, you can run the entire system using the provided `run.sh` script, which will simulate data generation, train the models, and start the dashboard:

```bash
bash run.sh
```

This script will execute the data simulator, model training, and dashboard in parallel.

## File Descriptions

- **`src/data_simulator.py`**: Simulates IoT device data, including temperature and energy consumption, and stores it in `device_data.csv`.
- **`src/model_training.py`**: Trains the fault prediction and anomaly detection models using the simulated device data.
- **`src/anomaly_detection.py`**: Loads the trained anomaly detection model and checks the device data for anomalies, saving any detected anomalies to a CSV file.
- **`src/alerting_system.py`**: Uses the trained models to check for faults and anomalies in the device data, printing alerts to the console.
- **`src/dashboard.py`**: A Streamlit-based dashboard for visualizing the real-time device data and interacting with the system.
- **`run.sh`**: A shell script that automates the execution of data simulation, model training, and the dashboard.

## Running the Models

### Fault Prediction Model:
The fault prediction model is trained using a random forest classifier. It predicts whether a device is likely to fail based on features such as temperature and energy consumption.

### Anomaly Detection Model:
The anomaly detection model uses Isolation Forest to detect unusual patterns in the device data. The model labels each data point as either normal (1) or anomalous (-1).

## Data Format

The data used by the system is stored in a CSV file (`device_data.csv`) with the following columns:

- **`timestamp`**: The timestamp of the data entry.
- **`device_id`**: A unique identifier for the IoT device.
- **`temperature`**: The temperature value recorded by the device.
- **`energy_consumption`**: The energy consumption value recorded by the device.

Example of a row in `device_data.csv`:

```csv
timestamp,device_id,temperature,energy_consumption
2025-01-01 12:00:00,Device_1,25.3,120.4
2025-01-01 12:00:01,Device_2,28.1,130.5
```

## Contributing

Contributions to the project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Test your changes thoroughly.
5. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
