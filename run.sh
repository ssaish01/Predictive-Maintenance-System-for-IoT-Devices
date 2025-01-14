#!/bin/bash
# Shell script to run the project components
echo "Starting IoT Device Management System..."
python3 src/data_simulator.py &
python3 src/model_training.py &
python3 src/dashboard.py &
