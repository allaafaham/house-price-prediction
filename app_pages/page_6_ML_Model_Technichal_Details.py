import streamlit as st
import os
import json
import pandas as pd

def main():
    st.title("6. ML Model Technical Details")

    st.write("""
    ## Model Overview
    This project uses an **XGBRegressor** inside a scikit-learn pipeline for house price prediction. The pipeline includes:
    - Median and categorical imputation
    - Zero imputation for some features
    - Feature dropping
    - Ordinal encoding
    - Yeo-Johnson and log transforms
    - Standard scaling
    - Final XGBRegressor model

    **Best model hyperparameters:**
    - learning_rate: 0.05
    - max_depth: 5
    - n_estimators: 100
    - subsample: 0.8

    ---
    """)

    # Show pipeline steps
    with st.expander("Show Pipeline Steps"):
        st.markdown("""
        1. MeanMedianImputer (BedroomAbvGr, LotFrontage)
        2. CategoricalImputer (BsmtExposure, BsmtFinType1, GarageFinish)
        3. ArbitraryNumberImputer (2ndFlrSF, GarageYrBlt, MasVnrArea)
        4. DropFeatures (EnclosedPorch, WoodDeckSF, ...)
        5. OrdinalEncoder (BsmtExposure, BsmtFinType1, GarageFinish, KitchenQual)
        6. YeoJohnsonTransformer (1stFlrSF, BedroomAbvGr, ...)
        7. LogTransformer (GrLivArea)
        8. StandardScaler
        9. XGBRegressor
        """)

    # Load evaluation metrics
    metrics_path = os.path.join("outputs", "ml_pipeline", "predict_house_price", "evaluation_metrics.json")
    metrics = None
    if os.path.exists(metrics_path):
        with open(metrics_path) as f:
            metrics = json.load(f)

    st.write("## Model Evaluation Metrics")
    if metrics:
        st.write(f"**Train Set:**")
        st.write(f"- MAE: {metrics['train']['MAE']:.2f}")
        st.write(f"- RMSE: {metrics['train']['RMSE']:.2f}")
        st.write(f"- R²: {metrics['train']['R2']:.4f}")
        st.write(f"**Test Set:**")
        st.write(f"- MAE: {metrics['test']['MAE']:.2f}")
        st.write(f"- RMSE: {metrics['test']['RMSE']:.2f}")
        st.write(f"- R²: {metrics['test']['R2']:.4f}")
    else:
        st.info("Evaluation metrics not found.")

    # Feature importances (from notebook)
    feature_importances = [
        ("OverallQual", 0.676),
        ("GrLivArea", 0.070),
        ("TotalBsmtSF", 0.036),
        ("GarageArea", 0.033),
        ("KitchenQual", 0.023),
        ("BsmtFinSF1", 0.023),
        ("YearBuilt", 0.018),
        ("YearRemodAdd", 0.017),
        ("LotArea", 0.013),
        ("GarageFinish", 0.012),
        ("1stFlrSF", 0.011),
        ("GarageYrBlt", 0.010),
        ("2ndFlrSF", 0.009),
        ("OverallCond", 0.009),
        ("OpenPorchSF", 0.009),
        ("MasVnrArea", 0.008),
        ("LotFrontage", 0.008),
        ("BedroomAbvGr", 0.005),
        ("BsmtUnfSF", 0.005),
        ("BsmtExposure", 0.004),
        ("BsmtFinType1", 0.003),
    ]

    st.write("## Feature Importances")
    imp_df = pd.DataFrame(feature_importances, columns=["Feature", "Importance"])
    st.dataframe(imp_df, use_container_width=True, hide_index=True)

    # Show feature importance plot if available
    eda_img_dir = os.path.join("outputs", "eda_images")
    fi_plot = os.path.join(eda_img_dir, "feature_importance.png")
    if os.path.exists(fi_plot):
        st.image(fi_plot, caption="Feature Importance (XGBRegressor)", use_container_width=True)
    else:
        st.info("Feature importance plot not found. (You can add it as 'feature_importance.png' in outputs/eda_images/)")

    st.write("""
    ---
    ### Summary
    - The model achieves strong performance (R² ≈ 0.81) using only the six most important features. This design allows users to make predictions by entering just a few key variables, making the tool simple and accessible.
    - If we used the full model with all available variables, the R² would be approximately 0.85, but it would require users to provide many more inputs.
    - **OverallQual** is by far the most important feature, followed by GrLivArea and TotalBsmtSF.
    - The pipeline includes robust preprocessing and feature selection.
    - See the sidebar for prediction and EDA pages.
    """) 