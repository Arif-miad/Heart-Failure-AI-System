import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Heart Failure Dashboard")

df = pd.read_csv("heart_failure_clinical_records_dataset.csv")

col1, col2, col3 = st.columns(3)

col1.metric("Total Patients", len(df))
col2.metric("Deaths", df["DEATH_EVENT"].sum())
col3.metric("Survived", len(df) - df["DEATH_EVENT"].sum())

fig1 = px.histogram(df, x="age", nbins=20, title="Age Distribution")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.box(df, y="serum_creatinine", title="Serum Creatinine Levels")
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.pie(df, names="sex", title="Gender Distribution")
st.plotly_chart(fig3, use_container_width=True)
