import streamlit as st

def main():
    st.title("1. Quick Project Summary")

    st.write("""
    ## Project Summary
    Lydia Doe, a Belgian citizen, has inherited four houses in Ames, Iowa, USA, from her great-grandfather. While she is knowledgeable about property prices in Belgium, she is unfamiliar with the Iowan real estate market and wants to avoid inaccurate appraisals that could lead to financial loss. Lydia seeks the help of a Data Practitioner to:
    - Accurately estimate the value of her inherited properties.
    - Understand what makes a house valuable in Ames, Iowa.
    - Predict the sale price of any house in Ames, Iowa for potential future investments.
    
    The project leverages a public dataset of Ames house prices to build a predictive dashboard and provide actionable insights.
    """)

    st.write("""
    ## Business Requirements
    1. **Correlation Insights:**
       - Visualize and analyze how different house attributes correlate with sale price in Ames, Iowa.
       - Provide clear data visualizations to help Lydia understand what drives value in this market.
    2. **Inherited House Price Prediction:**
       - Predict the sale price for each of Lydia's four inherited houses based on their attributes.
    3. **General House Price Prediction:**
       - Allow Lydia (or any user) to input attributes for any house in Ames, Iowa, and receive a predicted sale price.
    4. **User-Friendly Dashboard:**
       - Deliver an interactive web app that is easy to use and meets the above requirements.
    """)

    st.write("""
    ## Data Source
    - [Ames, Iowa Housing Prices Dataset (Kaggle)](https://www.kaggle.com/codeinstitute/housing-prices-data)
    
    ## Approach
    - Data exploration and visualization to uncover key drivers of house prices.
    - Machine learning regression model to predict sale prices.
    - Interactive dashboard for both EDA and prediction tasks.
    
    ## How to Use This App
    - Use the sidebar to navigate:
      - **Project Summary:** Overview and requirements.
      - **House Price Study:** Explore correlations and visualizations.
      - **Predict 4 Inherited Prices:** See predictions for Lydia's inherited houses.
      - **Predict Any House:** Get a price estimate for any house in Ames, Iowa.
      - **ML Regressor Model:** Learn about the model and its performance.
    """) 