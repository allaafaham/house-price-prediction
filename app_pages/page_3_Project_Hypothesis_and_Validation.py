import streamlit as st

def main():
    st.title("3. Project Hypothesis and Validation")

    st.write("""
    This page presents key hypotheses formulated during the project and the evidence used to validate or refute them. Each hypothesis is supported by multiple lines of analysis, including statistical, model-based, and visual validation.
    """)

    # Hypothesis 1
    st.subheader("Hypothesis 1")
    st.markdown("""
    **Statement:**  
    *OverallQual (the general material and finish quality of the house) is the single most influential individual variable for explaining variation in SalePrice in the Ames, IA data.*
    """)
    st.markdown("**Validation:**")
    st.markdown("""
    - **Correlation analysis:** Pearson correlation between OverallQual and SalePrice is approximately 0.79, the largest among all numeric features (see EDA).
    - **Model-based importance:** In the tuned XGBRegressor, gain-based feature importance for OverallQual is 0.676 (67.6%), far exceeding the second-ranked feature GrLivArea at 0.070.
    - **Visual confirmation:** Scatter/box plots show a clear monotonic increase in median and upper-quartile prices with each step up the quality scale.
    """)
    st.success("All three validation routes converge, supporting the hypothesis that OverallQual dominates the price signal in this market.")

    # Hypothesis 2
    st.subheader("Hypothesis 2")
    st.markdown("""
    **Statement:**  
    *Houses with more above-ground living area (GrLivArea) tend to sell for higher prices.*
    """)
    st.markdown("**Validation:**")
    st.markdown("""
    - **Pearson Correlation with SalePrice:** ≈ 0.71
    - **Spearman Correlation:** Also indicates a strong positive monotonic relationship.
    - **Scatter plot:** Shows a clear upward trend between GrLivArea and SalePrice.
    - **Model importance:** GrLivArea is one of the top predictors in the XGBoost model used in this project.
    """)
    st.success("The hypothesis is confirmed: more above-ground living area is strongly associated with higher sale prices in Ames, Iowa. GrLivArea is an important feature for both analysis and prediction.") 