import streamlit as st
import joblib
import os
import numpy as np
import pandas as pd

st.title("Predict Any House Price")

MODEL_PATH = os.path.join("outputs", "ml_pipeline", "predict_house_price", "best_pipeline_with_top_features.joblib")
DATA_PATH = os.path.join("inputs", "datasets", "raw", "inherited_houses.csv")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

@st.cache_data
def get_feature_defaults():
    df = pd.read_csv(DATA_PATH)
    defaults = {}
    for col in df.columns:
        if df[col].dtype == 'O':
            defaults[col] = df[col].mode()[0]
        else:
            defaults[col] = float(df[col].median())
    return defaults, list(df.columns)

model = load_model()
defaults, all_features = get_feature_defaults()

# Only the features used by the model
user_features = [
    'GarageArea', 'BsmtFinSF1', 'GrLivArea', 'KitchenQual', 'OverallQual', 'TotalBsmtSF'
]

with st.form("predict_form"):
    st.write("### Enter House Features:")
    user_input = {}
    user_input['GarageArea'] = st.number_input('GarageArea', min_value=0.0, value=float(defaults['GarageArea']))
    user_input['BsmtFinSF1'] = st.number_input('BsmtFinSF1', min_value=0.0, value=float(defaults['BsmtFinSF1']))
    user_input['GrLivArea'] = st.number_input('GrLivArea', min_value=0.0, value=float(defaults['GrLivArea']))
    user_input['KitchenQual'] = st.selectbox('KitchenQual', ['Po', 'Fa', 'TA', 'Gd', 'Ex'], index=['Po', 'Fa', 'TA', 'Gd', 'Ex'].index(defaults['KitchenQual']) if defaults['KitchenQual'] in ['Po', 'Fa', 'TA', 'Gd', 'Ex'] else 2)
    user_input['OverallQual'] = st.selectbox('OverallQual', list(range(1, 11)), index=int(defaults['OverallQual'])-1 if 1 <= int(defaults['OverallQual']) <= 10 else 5)
    user_input['TotalBsmtSF'] = st.number_input('TotalBsmtSF', min_value=0.0, value=float(defaults['TotalBsmtSF']))
    submitted = st.form_submit_button("Predict Price")

if submitted:
    # Fill all features with defaults, then update with user input
    input_data = defaults.copy()
    input_data.update(user_input)
    input_df = pd.DataFrame([{col: input_data[col] for col in all_features}])
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🏷️ Predicted Sale Price: ${prediction:,.0f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}") 