import streamlit as st
import os

def main():
    st.title("2. House Price Study")

    st.write("""
    This page presents key findings from the exploratory data analysis (EDA) of Ames house prices. Use the toggles below to explore correlation heatmaps and feature-target relationships, each accompanied by concise insights.
    """)

    EDA_IMG_DIR = os.path.join("outputs", "eda_images")

    # Heatmap images and their explanations
    heatmap_files = [
        ("Spearman Correlation Heatmap", "spearman_corr_heatmap.png",
         "**Spearman Correlation:** Measures monotonic relationships, capturing both linear and non-linear associations. Useful for identifying variables that move together, even if not perfectly linear."),
        ("Pearson Correlation Heatmap", "pearson_corr_heatmap.png",
         "**Pearson Correlation:** Focuses on linear relationships between continuous variables. High values indicate strong linear association with sale price or between features."),
        ("PPS Score Heatmap", "pps_heatmap.png",
         "**Power Predictive Score (PPS):** Detects both linear and non-linear predictive relationships. PPS ranges from 0 (no predictive power) to 1 (perfect prediction), highlighting features that best predict the target, including categorical variables.")
    ]

    # Feature plot explanations (summarized and reworded)
    var_explanations = {
        "GrLivArea": "**Above Ground Living Area:** Shows a strong positive linear relationship with sale price. Larger living areas generally command higher prices, though a few outliers exist.",
        "GarageArea": "**Garage Area:** Displays a moderate positive correlation. Larger garages tend to increase sale price, but the effect plateaus for very large garages.",
        "TotalBsmtSF": "**Total Basement Area:** Positively correlated with sale price. More basement space typically adds value, though not as strongly as living area.",
        "1stFlrSF": "**First Floor Area:** Similar to basement area, more first-floor space is associated with higher prices, but the relationship is less pronounced than for total living area.",
        "YearBuilt": "**Year Built:** Newer homes tend to sell for more, with a noticeable upward trend for houses built after the 1980s. The relationship is not strictly linear.",
        "GarageYrBlt": "**Garage Year Built:** Newer garages are linked to higher sale prices, but some implausible years (e.g., zero) suggest data quality issues.",
        "OverallQual": "**Overall Quality:** Strong monotonic relationship with sale price. Each step up in quality brings a substantial price increase, making this a key predictor.",
        "KitchenQual": "**Kitchen Quality:** Sale prices are clearly stratified by kitchen quality. Higher ratings (e.g., Excellent, Good) correspond to higher median prices, making this a strong categorical predictor."
    }

    show_heatmaps = st.toggle("Show Correlation Heatmaps", value=False)
    show_varplots = st.toggle("Show Important Variable Plots", value=False)

    if show_heatmaps:
        st.subheader("Correlation Heatmaps")
        for caption, fname, explanation in heatmap_files:
            img_path = os.path.join(EDA_IMG_DIR, fname)
            if os.path.exists(img_path):
                st.image(img_path, caption=caption, use_container_width=True)
                st.markdown(explanation)
            else:
                st.warning(f"{caption} not found.")

        st.markdown("""
        **Feature Selection Based on Correlation and PPS Analysis**
        
        To identify the most important features for predicting sale price, we combined insights from three methods:
        - **Spearman Correlation:** Selected features with strong monotonic relationships to SalePrice (e.g., GrLivArea, OverallQual, GarageArea, GarageYrBlt, YearBuilt).
        - **Pearson Correlation:** Highlighted features with strong linear relationships (e.g., GrLivArea, OverallQual, 1stFlrSF, GarageArea, TotalBsmtSF).
        - **PPS (Power Predictive Score):** Identified features with high predictive power, including non-linear and categorical effects (e.g., OverallQual, KitchenQual).
        
        The final set of important variables was created by combining the top features from all three methods and removing duplicates. This comprehensive approach ensures that both linear and non-linear, as well as categorical, predictors are considered for further analysis and modeling.
        """)

    if show_varplots:
        st.subheader("Important Variable Plots")
        all_files = os.listdir(EDA_IMG_DIR) if os.path.exists(EDA_IMG_DIR) else []
        important_var_files = [f for f in all_files if f.endswith('.png') and not any(h[1] == f for h in heatmap_files)]
        for fname in important_var_files:
            var_name = fname.replace('_vs_SalePrice.png', '')
            img_path = os.path.join(EDA_IMG_DIR, fname)
            st.image(img_path, caption=var_name.replace('_', ' ').title(), use_container_width=True)
            # Show explanation if available
            key = var_name.split('_')[0]  # Handles e.g. 'GrLivArea', 'GarageArea', etc.
            if key in var_explanations:
                st.markdown(var_explanations[key])

    # Add summary section at the end
    st.markdown("""
    ## Summary

    - Variables with the strongest association to `SalePrice` include `GrLivArea`, `OverallQual`, `KitchenQual`, and `YearBuilt`.
    - Moderate predictors include `GarageArea`, `1stFlrSF`, and `TotalBsmtSF`.
    - `GarageYrBlt` may contain data quality issues and requires preprocessing.
    """) 