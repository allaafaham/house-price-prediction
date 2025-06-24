import streamlit as st
import joblib
import os

st.title("Predict Any House Price")

MODEL_PATH = os.path.join("outputs", "ml_pipeline", "predict_house_price", "best_pipeline_with_top_features.joblib")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

st.write("(A form for user input will go here. The model is loaded and ready to predict.)") 