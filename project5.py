import sys
import streamlit as st
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
# Load the trained Random Forest model and scaler

# Set up the Streamlit app
st.title("Energy Prediction App")

# Create input fields for the features
purchases = st.number_input('Purchases', value=0.0)
sb_total = st.number_input('SB Total', value=0.0)
sb_solar = st.number_input('SB Solar', value=0.0)
sb_non_solar = st.number_input('SB Non-Solar', value=0.0)
sb_hydro = st.number_input('SB Hydro', value=0.0)
mcv_total = st.number_input('MCV Total', value=0.0)
mcv_solar = st.number_input('MCV Solar', value=0.0)
mcv_non_solar = st.number_input('MCV Non-Solar', value=0.0)
mcv_hydro = st.number_input('MCV Hydro', value=0.0)
fsv_total = st.number_input('FSV Total', value=0.0)
fsv_solar = st.number_input('FSV Solar', value=0.0)
fsv_non_solar = st.number_input('FSV Non-Solar', value=0.0)
fsv_hydro = st.number_input('FSV Hydro', value=0.0)

# Button to make a prediction
if st.button('Predict'):
    # Collect input features into a list
    features = [
        purchases,
        sb_total,
        sb_solar,
        sb_non_solar,
        sb_hydro,
        mcv_total,
        mcv_solar,
        mcv_non_solar,
        mcv_hydro,
        fsv_total,
        fsv_solar,
        fsv_non_solar,
        fsv_hydro
    ]

    # Scale the input features
    features_scaled = scaler.transform([features])

    # Make prediction
    prediction = rf_model.predict(features_scaled)[0]

    # Display the prediction
    st.success(f'The predicted energy output is: {prediction}')
