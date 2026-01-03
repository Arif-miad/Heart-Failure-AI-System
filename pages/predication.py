import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.title("🤖 Heart Failure Prediction")

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")

X = df.drop("DEATH_EVENT", axis=1)
y = df["DEATH_EVENT"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

st.subheader("📋 Enter Patient Details")

age = st.number_input("Age", 1, 120)
serum_creatinine = st.number_input("Serum Creatinine", 0.1, 10.0)
ejection_fraction = st.number_input("Ejection Fraction", 1, 100)
serum_sodium = st.number_input("Serum Sodium", 100, 150)
platelets = st.number_input("Platelets", 10000, 1000000)
time = st.number_input("Follow-up period", 1, 300)

anaemia = st.selectbox("Anaemia", [0,1])
diabetes = st.selectbox("Diabetes", [0,1])
high_bp = st.selectbox("High Blood Pressure", [0,1])
smoking = st.selectbox("Smoking", [0,1])
sex = st.selectbox("Sex 1=Male,0=Female", [0,1])

if st.button("🔮 Predict"):
    input_data = [[age, anaemia, df["creatinine_phosphokinase"].mean(), diabetes,
                   ejection_fraction, high_bp, platelets, serum_creatinine,
                   serum_sodium, sex, smoking, time]]
    
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠ High risk of heart failure")
    else:
        st.success("✅ Low risk of heart failure")
