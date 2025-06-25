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
    *A gradient-boosted tree model (specifically XGBRegressor) trained on the engineered feature set attains R² > 0.85 and RMSE < 30,000 USD on previously unseen data, outperforming baseline linear and bagged tree models.*
    """)
    st.markdown("**Validation:**")
    st.markdown("- **Cross-validation:** Per-fold cross-validation during grid search selected XGBRegressor as the best estimator.")
    st.markdown("- **Held-out test set performance:**")
    st.table({
        "Model": ["XGBRegressor", "Linear Regression", "Random Forest"],
        "R²": ["0.8966", "0.78†", "0.84†"],
        "RMSE (USD)": ["26,725", "34–36k†", "30–32k†"],
        "MAE (USD)": ["16,772", "—", "—"]
    })
    st.caption("†Linear-regression and random-forest scores were logged during the model-comparison loop; exact values vary by CV fold but remain outside the target thresholds.")
    st.success("The hypothesis is confirmed: the tuned gradient-boosted model exceeds the stipulated accuracy targets and materially outperforms simpler baselines.")

    # Hypothesis 3
    st.subheader("Hypothesis 3")
    st.markdown("""
    **Statement:**  
    *The four inherited houses are mid-priced within the Ames distribution, with predicted sale prices clustering around the sample mean (~175,000 USD).*  
    """)
    st.markdown("**Validation:**")
    st.markdown("- **Predicted prices for the four inherited houses:**")
    st.table({
        "House": ["1", "2", "3", "4"],
        "Predicted price (USD)": ["130,459", "155,725", "181,397", "188,034"]
    })
    st.markdown("- **Descriptive statistics:**  ")
    st.markdown("  - Mean = 163,904  ")
    st.markdown("  - Min = 130,459  ")
    st.markdown("  - Max = 188,034  ")
    st.markdown("  - Range ≈ 58k  ")
    st.markdown("- **Ames dataset context:**  ")
    st.markdown("  - Overall mean ≈ 175,000 USD  ")
    st.markdown("  - Median ≈ 164,000 USD  ")
    st.success("All four predictions lie within one inter-quartile range of the population median; the inherited properties therefore sit squarely in the mid-market segment, corroborating the hypothesis.") 