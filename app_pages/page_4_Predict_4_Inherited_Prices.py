import streamlit as st
import pandas as pd
import os

def main():
    st.title("4. Predicted Prices for 4 Inherited Houses")

    st.write("""
    Lydia Doe has inherited four unique houses in Ames, Iowa. The predicted sale prices below are calculated using a machine learning model trained only on the six most important features, as determined by feature importance (importance > 0.02):

    - **OverallQual** (Overall material and finish quality)
    - **GrLivArea** (Above ground living area square feet)
    - **TotalBsmtSF** (Total basement area in square feet)
    - **GarageArea** (Size of garage in square feet)
    - **KitchenQual** (Kitchen quality)
    - **BsmtFinSF1** (Type 1 finished basement square feet)

    This focused approach helps ensure the predictions are both robust and interpretable.
    """)

    # Load predictions
    PRED_PATH = os.path.join("outputs", "four_houses_with_predictions.csv")
    df_pred = pd.read_csv(PRED_PATH)

    # Only show the top 6 features
    top6_cols = ["OverallQual", "GrLivArea", "TotalBsmtSF", "GarageArea", "KitchenQual", "BsmtFinSF1"]
    st.write("#### Inherited Houses: Top 6 Features Used for Prediction")
    st.dataframe(df_pred[top6_cols], use_container_width=True)

    # Show predicted sale prices in a separate table
    st.write("#### Predicted Sale Price for Each House")
    sale_price_df = df_pred[["Predicted_SalePrice"]].copy()
    sale_price_df = sale_price_df.rename(columns={"Predicted_SalePrice": "Predicted Sale Price ($)"})
    st.dataframe(sale_price_df, use_container_width=True)

    st.markdown("""
    **Summary:**
    - The predicted sale prices for Lydia's inherited homes range from approximately 130,000$ to 188,000$.
    - These estimates are based on a streamlined model using only the most influential property features.
    - Lydia can use these insights to make informed decisions about selling, renting, or renovating her properties.
    """) 