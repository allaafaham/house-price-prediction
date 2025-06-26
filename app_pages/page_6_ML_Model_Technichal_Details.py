import streamlit as st


def main():
    st.title("6. ML Model Technical Details")

    st.write("""
    ## Model Overview
    The final production model is an **XGBRegressor** inside a scikit-learn pipeline, trained on a reduced set of the most important features for both accuracy and user simplicity.

    The pipeline includes:
    - Feature dropping (removes high-missingness and low-importance features)
    - Ordinal encoding for `KitchenQual`
    - Yeo-Johnson transformation for `BsmtFinSF1` and `TotalBsmtSF`
    - Log10 transformation for `GrLivArea`
    - Standard scaling
    - Final XGBRegressor model

    **Best model hyperparameters:**
    - learning_rate: 0.05
    - max_depth: 5
    - n_estimators: 100
    - subsample: 0.8

    ---
    """)

    st.write("## Model Evaluation Metrics")
    st.write("""
    **Train Set:**
    - MAE: 12,940.25
    - MSE: 306,820,800.00
    - RMSE: 17,516.30
    - R²: 0.9502
    
    **Test Set:**
    - MAE: 19,640.81
    - MSE: 916,381,056.00
    - RMSE: 30,271.79
    - R²: 0.8673
    
    ---
    """)

    st.write("""
    ## Feature Selection Rationale
    The best features for the final model were selected based on their importance as determined by the XGBoost model. Feature importance was evaluated using the model's gain-based metric, and only the top predictors were retained to maximize predictive power while keeping the model simple and user-friendly.
    
    The selected features are:
    - **OverallQual**
    - **GrLivArea**
    - **TotalBsmtSF**
    - **BsmtFinSF1**
    - **GarageArea**
    - **KitchenQual**
    
    These features were found to have the highest impact on sale price prediction and form the basis of the streamlined production pipeline.
    """)


    st.image("outputs/eda_images/feature_importance.png", caption="Feature Importance (XGBRegressor)", use_container_width=True)

    st.write("""
    ---
    ### Summary
    - The streamlined model achieves strong performance (R² ≈ 0.81) using only the six most important features, making predictions fast and user-friendly.
    - The pipeline includes robust preprocessing and feature selection, ensuring reliability and interpretability.
    - **OverallQual** is by far the most important feature, followed by GrLivArea and TotalBsmtSF.
    - See the sidebar for prediction and EDA pages.
    """) 