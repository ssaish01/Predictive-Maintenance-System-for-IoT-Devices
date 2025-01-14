import pandas as pd
import numpy as np
import time

def generate_data(num_devices=10, duration=60):
    devices = [f"Device_{i}" for i in range(1, num_devices + 1)]
    columns = ["timestamp", "device_id", "temperature", "energy_consumption"]
    data = []

    start_time = time.time()
    while time.time() - start_time < duration:
        for device in devices:
            data.append([
                pd.Timestamp.now(),
                device,
                np.random.normal(25, 5),
                np.random.normal(100, 20)
            ])
        time.sleep(1)
    
    df = pd.DataFrame(data, columns=columns)
    df.to_csv("../data/device_data.csv", index=False)
    print("IoT device data simulation complete!")

if __name__ == "__main__":
    generate_data()
