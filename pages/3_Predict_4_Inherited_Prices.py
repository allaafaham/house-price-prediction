import streamlit as st
import pandas as pd
import joblib
import os

st.title("Predict 4 Inherited House Prices")

# Load model and data
MODEL_PATH = os.path.join("outputs", "ml_pipeline", "predict_house_price", "best_pipeline.joblib")
DATA_PATH = os.path.join("inputs", "datasets", "raw", "inherited_houses.csv")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

model = load_model()
data = load_data()

st.write("### Inherited Houses Data:")
st.dataframe(data)

st.write("(Predictions will be shown here.)") 