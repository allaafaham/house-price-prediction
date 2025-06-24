import streamlit as st
import os

st.title("House Price Study")

st.write("""
This page contains exploratory data analysis (EDA), visualizations, and insights from the house price study. Use the toggles below to view correlation heatmaps or important variable plots.
""")

EDA_IMG_DIR = os.path.join("outputs", "eda_images")

# Heatmap images
heatmap_files = [
    ("Spearman Correlation Heatmap", "spearman_corr_heatmap.png"),
    ("Pearson Correlation Heatmap", "pearson_corr_heatmap.png"),
    ("PPS Score Heatmap", "pps_heatmap.png")
]

# Important variable plots (all PNGs except the heatmaps)
all_files = os.listdir(EDA_IMG_DIR) if os.path.exists(EDA_IMG_DIR) else []
important_var_files = [f for f in all_files if f.endswith('.png') and not any(h[1] == f for h in heatmap_files)]

show_heatmaps = st.toggle("Show Correlation Heatmaps", value=False)
show_varplots = st.toggle("Show Important Variable Plots", value=False)

if show_heatmaps:
    st.subheader("Correlation Heatmaps")
    for caption, fname in heatmap_files:
        img_path = os.path.join(EDA_IMG_DIR, fname)
        if os.path.exists(img_path):
            st.image(img_path, caption=caption, use_container_width=True)
        else:
            st.warning(f"{caption} not found.")

if show_varplots:
    st.subheader("Important Variable Plots")
    for fname in important_var_files:
        img_path = os.path.join(EDA_IMG_DIR, fname)
        st.image(img_path, caption=fname.replace('_vs_SalePrice.png', '').replace('_', ' ').title(), use_container_width=True) 