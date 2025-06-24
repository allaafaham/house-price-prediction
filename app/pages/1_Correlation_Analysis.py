import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Correlation Analysis")
st.markdown("""
This section explores how key house attributes relate to the sale price.
These insights are based on the Ames Housing dataset.
""")

@st.cache_data
def load_data():
    return pd.read_csv("../inputs/datasets/raw/house_prices_records.csv")

df = load_data()

# Top correlations
st.subheader("🔗 Top Correlated Features with SalePrice")
corr = df.corr(numeric_only=True)
top_corr = corr['SalePrice'].abs().sort_values(ascending=False)[1:8]
st.dataframe(top_corr)

# Scatter plots
st.subheader("📈 Numerical Features vs SalePrice")
numeric_features = ['GrLivArea', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', 'YearBuilt']
for feature in numeric_features:
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=feature, y='SalePrice', ax=ax)
    ax.set_title(f"{feature} vs SalePrice")
    st.pyplot(fig)

# Box plot for categorical
st.subheader("📦 Kitchen Quality vs SalePrice")
fig, ax = plt.subplots()
sns.boxplot(data=df, x='KitchenQual', y='SalePrice', order=['Po', 'Fa', 'TA', 'Gd', 'Ex'], ax=ax)
ax.set_title("KitchenQual vs SalePrice")
st.pyplot(fig)

# Heatmap (optional)
with st.expander("📡 Full Correlation Heatmap"):
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, cmap='coolwarm', annot=False)
    st.pyplot(fig)