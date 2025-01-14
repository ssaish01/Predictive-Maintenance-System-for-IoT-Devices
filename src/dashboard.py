import streamlit as st
import pandas as pd

st.title("IoT Device Management Dashboard")

data = pd.read_csv("../data/device_data.csv")
st.write("Real-time Device Data", data)

if st.button("Check Faults"):
    st.write("Fault detection coming soon!")
