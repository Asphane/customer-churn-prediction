import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessors
model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoders = joblib.load('label_encoders.pkl')
columns = joblib.load('columns.pkl')

# App title
st.title("Customer Churn Prediction App")

# User input fields
input_data = {}
input_data['gender'] = st.selectbox("Gender", ["Female", "Male"])
input_data['SeniorCitizen'] = st.selectbox("Senior Citizen", [0, 1])
input_data['Partner'] = st.selectbox("Partner", ["Yes", "No"])
input_data['Dependents'] = st.selectbox("Dependents", ["Yes", "No"])
input_data['tenure'] = st.slider("Tenure (months)", 0, 72, 12)
input_data['PhoneService'] = st.selectbox("Phone Service", ["Yes", "No"])
input_data['MultipleLines'] = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
input_data['InternetService'] = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
input_data['OnlineSecurity'] = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
input_data['OnlineBackup'] = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
input_data['DeviceProtection'] = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
input_data['TechSupport'] = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
input_data['StreamingTV'] = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
input_data['StreamingMovies'] = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
input_data['Contract'] = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
input_data['PaperlessBilling'] = st.selectbox("Paperless Billing", ["Yes", "No"])
input_data['PaymentMethod'] = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
input_data['MonthlyCharges'] = st.number_input("Monthly Charges", min_value=0.0)
input_data['TotalCharges'] = st.number_input("Total Charges", min_value=0.0)

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# Encode categorical variables using loaded label encoders
for col, le in label_encoders.items():
    input_df[col] = le.transform(input_df[col])

# Reorder columns to match training data
input_df = input_df.reindex(columns=columns)

# Scale the input
input_scaled = scaler.transform(input_df)

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(input_scaled)[0]
    result = "Yes" if prediction == 1 else "No"
    st.subheader(f"Churn Prediction: {result}")