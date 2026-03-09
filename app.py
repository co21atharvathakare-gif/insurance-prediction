import streamlit as st
import joblib
import numpy as np

# 1. Load the saved model
model = joblib.load('insurance_model.pkl')

# 2. Build the UI (The "Look")
st.title("💰 Insurance Premium Predictor")
st.write("Enter customer details below to estimate insurance charges.")

# Input fields
age = st.slider("Age", 18, 100, 30)
bmi = st.number_input("BMI (Body Mass Index)", 10.0, 50.0, 25.0)
smoker_input = st.selectbox("Do they smoke?", ["No", "Yes"])

# Convert "Yes/No" back to 1/0 so the model understands
smoker = 1 if smoker_input == "Yes" else 0

# 3. Predict button
if st.button("Predict Cost"):
    # Arrange inputs into the exact format used during training
    features = np.array([[age, bmi, smoker]])
    prediction = model.predict(features)
    
    # Show the result
    st.success(f"The estimated insurance premium is: ${prediction[0]:,.2f}")