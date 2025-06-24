import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="House Prices App", layout="wide")

st.title("🏠 House Prices Project")
st.write("""
Welcome to the House Prices Project app!

Navigate using the sidebar to:
- See a quick project summary
- Explore the house price study
- Predict prices for 4 inherited houses
- Predict the price of any house you want
- Learn about the ML regressor model
""")

st.sidebar.title("Navigation")
st.sidebar.info("Select a page from the sidebar menu.")
