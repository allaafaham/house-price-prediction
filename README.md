# Heritage Housing Issues: Ames, Iowa House Price Prediction

[![View the Live Dashboard](https://img.shields.io/badge/Live%20App-Streamlit-green?logo=heroku)](https://house-price-prediction-allaa-22f158218629.herokuapp.com/)

## Project Summary

Lydia Doe, a fictional individual from Belgium, has recently inherited four houses in Ames, Iowa, USA, from her deceased great-grandfather. While Lydia is well-versed in property valuation in her home country, she is acutely aware that the factors influencing house desirability and value in Belgium may not translate directly to the Iowan real estate market. She recognizes that relying solely on her European experience could lead to inaccurate appraisals and potentially significant financial loss or missed opportunity when selling the inherited properties.

<p><strong><a href="https://house-price-prediction-allaa-22f158218629.herokuapp.com/" target="_blank" rel="noopener noreferrer">Price Prediction Dashboard!</a></strong></p>

Faced with this challenge, Lydia seeks the expertise of a Data Practitioner. Her primary motivations are:
- She does not know the true worth of the four inherited properties and wants to avoid the risk of inaccurate pricing, given the substantial sums at stake.
- She is also interested in being able to predict the sale price of any house in Ames, Iowa, should she consider future property investments in the area.

Through her research, Lydia discovers a public dataset containing detailed records of house prices and attributes for Ames, Iowa. She provides this dataset to the Data Practitioner and requests the development of a data-driven web application to assist with her goals.

This project delivers a comprehensive solution: a user-friendly web dashboard that combines exploratory data analysis, interactive visualizations, and robust machine learning models. The app empowers Lydia—and any user—to make informed, data-driven decisions about property valuation in Ames, Iowa, regardless of their prior experience with the local market.

---

## ML Business Case and Business Requirements

**Business Case:**  
Accurately predicting house prices in Ames, Iowa, enables Lydia and other stakeholders to make informed decisions about selling, investing, or renovating properties. The solution must be accessible, interpretable, and reliable for non-technical users.

**Business Requirements:**
1. **BR1:** Lydia Doe must be able to estimate the value of her four inherited houses.
2. **BR2:** Any user should be able to estimate the sale price of any house in Ames, Iowa, by entering a small set of key features.
3. **BR3:** The solution should provide transparency about the model, its performance, and the factors influencing predictions.

---

## Business Requirements Mapping to ML Tasks

| Business Requirement | ML Task/Feature |
|----------------------|----------------|
| BR1 | Predict prices for the four inherited houses using a trained ML model. |
| BR2 | Provide a general prediction tool for any house, requiring only the most important features. |
| BR3 | Include model explainability, feature importance, and clear evaluation metrics in the dashboard. |

## User Stories & Task Breakdown

> All occurrences of “property owner” have been replaced with **user** for consistency.

### Data Visualization

| ID       | User Story                                                                                                 | Tasks                                                                                                                                                 |
|----------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **DV-1** | As a **user**, I want to understand which house features most influence the sale price, so that I can make informed decisions about my inherited properties. | • Create a correlation-matrix heatmap of all numerical features against `SalePrice`.<br>• Generate scatter plots of top-correlated features vs. `SalePrice`.<br>• Produce box plots for categorical features vs. `SalePrice`.<br>• Implement interactive feature selection for all visualizations.<br>• Add tooltips displaying exact values and summary statistics. |
| **DV-2** | As a **user**, I want to see the distribution of house prices in Ames, so that I can understand the market range. | • Create a histogram of `SalePrice` with adjustable bin width.                                                                                         |

### Machine Learning

| ID       | User Story                                                                                                   | Tasks                                                                                                                                                                     |
|----------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ML-1** | As a **user**, I want accurate price predictions for my four inherited houses, so that I can set appropriate selling prices. | • Implement a data-preprocessing pipeline (missing-value imputation, encoding, scaling).<br>• Create feature-engineering steps for numerical and categorical variables.<br>• Build and train multiple regression models (Linear Regression, Random Forest, XGBoost).<br>• Evaluate models using cross-validation and hold-out metrics.<br>• Generate predictions for the four inherited houses. |
| **ML-2** | As a **user**, I want to predict prices for any house in Ames, so that I can assess future investments.       | • Design an input form for new house features (dashboard).<br>• Implement an end-to-end prediction pipeline.<br>• Display feature-importance visualizations for each prediction. |

### Dashboard

| ID       | User Story                                                                                           | Tasks                                                                                                    |
|----------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **DB-1** | As a **user**, I want to interact with the data and predictions through a user-friendly interface, so that I can easily analyze and make decisions. | • Design and implement the dashboard layout in Streamlit.<br>• Build a clear sidebar navigation system with page routing. |

### Model Evaluation

| ID       | User Story                                                                                             | Tasks                                                                                                                  |
|----------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| **ME-1** | As a **user**, I want to understand how accurate the predictions are, so that I can trust the model’s outputs. | • Implement cross-validation for all candidate models.<br>• Visualize model performance metrics (`R²`, `RMSE`, `MAE`).<br>• Create model-comparison tables highlighting trade-offs and ranking. |

### Documentation

| ID        | User Story                                                                                                     | Tasks                                                                                                                                  |
|-----------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **DOC-1** | As a **user**, I want to understand how the model works and what factors it considers, so that I can trust its predictions. | • Write detailed model documentation (data-processing steps, algorithms, hyperparameters).<br>• Generate feature-importance documentation (global and local explanations).<br>• Provide clear usage instructions for the dashboard and codebase. |


---

## Dataset 

- **Source:** [Kaggle - codeinstitute/housing-prices-data](https://www.kaggle.com/codeinstitute/housing-prices-data)

| Feature         | Description                                                                                   | Imputation/Default |
|-----------------|----------------------------------------------------------------------------------------------|--------------------|
| 1stFlrSF        | First Floor Square Feet: The area (in square feet) of the first floor of the house.           |                    |
| 2ndFlrSF        | Second Floor Square Feet: The area (in square feet) of the second floor (if any).             | 0                  |
| BedroomAbvGr    | Bedrooms Above Grade: Number of bedrooms above ground level (not including basement rooms).   | median             |
| BsmtExposure    | Basement Exposure: Walkout or garden level walls in basement (e.g., None, Mn, Av, Gd).        | None               |
| BsmtFinSF1      | Basement Finished Area 1: Type 1 finished square feet in basement.                            |                    |
| BsmtFinType1    | Basement Finish Type 1: Describes the quality of the finished area (e.g., GLQ, ALQ, Unf).     | None               |
| BsmtUnfSF       | Unfinished Basement Square Feet: Unfinished square feet of basement area.                     |                    |
| EnclosedPorch   | Enclosed Porch Square Feet: Area of enclosed porch.                                           | 0                  |
| GarageArea      | Garage Area: Size of the garage in square feet.                                               |                    |
| GarageFinish    | Garage Finish: Interior finish of the garage (e.g., Finished, Unfinished, RFn).               | None               |
| GarageYrBlt     | Garage Year Built: Year the garage was built.                                                 | mean               |
| GrLivArea       | Ground Living Area: Above ground living area in square feet (does not include basement).      |                    |
| KitchenQual     | Kitchen Quality: Quality of the kitchen (e.g., Ex, Gd, TA, Fa).                              |                    |
| LotArea         | Lot Area: Size of the lot in square feet.                                                     |                    |
| LotFrontage     | Lot Frontage: Linear feet of street connected to property.                                    | median             |
| MasVnrArea      | Masonry Veneer Area: Area of masonry veneer (brick, stone) in square feet.                    |                    |
| OpenPorchSF     | Open Porch Square Feet: Area of open porch.                                                   |                    |
| OverallCond     | Overall Condition: Rates the overall condition of the house (1=Very Poor, 10=Excellent).      |                    |
| OverallQual     | Overall Quality: Rates the overall material and finish of the house (1=Very Poor, 10=Excellent).|                  |
| TotalBsmtSF     | Total Basement Square Feet: Total area of the basement.                                       |                    |
| WoodDeckSF      | Wood Deck Square Feet: Area of wood deck.                                                     | 0                  |
| YearBuilt       | Year Built: Original construction year of the house.                                          |                    |
| YearRemodAdd    | Year Remodeled: Year of last remodel (if any).                                                |                    |
| SalePrice       | Sale Price: The property's sale price (this is your target variable for prediction).           |                    |

---

## Model Objective, Metrics & Evaluation Strategy

**Objective:**  
Build a regression model to predict house sale prices in Ames, Iowa, with high accuracy and interpretability, using a minimal set of input features for user convenience.

**Modeling Approach:**
- Multiple regression models evaluated (Linear Regression, Random Forest, XGBoost, etc.)
- Final model: XGBRegressor, with a streamlined version using only the top 6 most important features (for dashboard simplicity).

**Metrics:**
- R² (Coefficient of Determination)
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)

**Evaluation Strategy:**
- Train/test split and cross-validation.
- Hyperparameter tuning via grid search.
- Comparison of full-feature and reduced-feature models.

**Performance:**
- **Full model (all features):** R² ≈ 0.85 on test set.
- **Reduced model (6 features):** R² ≈ 0.81 (cross-validated mean).

---

## Hypotheses

## Project Hypotheses and Validation

This section summarizes the key hypotheses formulated during the project and the evidence used to validate or refute them.

---

### Hypothesis 1

**Statement:**  
*OverallQual (the general material and finish quality of the house) is the single most influential individual variable for explaining variation in SalePrice in the Ames, IA data.*

**Validation:**
- **Correlation analysis:** Pearson correlation between OverallQual and SalePrice is approximately 0.79, the largest among all numeric features.
- **Model-based importance:** In the tuned XGBRegressor, gain-based feature importance for OverallQual is 0.676 (67.6%), far exceeding the second-ranked feature GrLivArea at 0.070.
- **Visual confirmation:** Scatter/box plots show a clear monotonic increase in median and upper-quartile prices with each step up the quality scale.

> **Conclusion:**  
> All three validation routes converge, supporting the hypothesis that OverallQual dominates the price signal in this market.

---

### Hypothesis 2

**Statement:**  
*Houses with more above-ground living area (GrLivArea) tend to sell for higher prices.*

**Validation:**
- **Pearson Correlation with SalePrice:** ≈ 0.71
- **Spearman Correlation:** Also indicates a strong positive monotonic relationship.
- **Scatter plot:** Shows a clear upward trend between GrLivArea and SalePrice.
- **Model importance:** GrLivArea is one of the top predictors in the XGBoost model used in this project.

> **Conclusion:**  
> The hypothesis is confirmed: more above-ground living area is strongly associated with higher sale prices in Ames, Iowa. GrLivArea is an important feature for both analysis and prediction.

---

## Notebooks: Summary and Results

| Notebook | Purpose | Key Results |
|----------|---------|-------------|
| **1-data-collection.ipynb** | Download and organize the Ames dataset from Kaggle. | Data successfully acquired and stored for analysis. |
| **2-data-exploration.ipynb** | EDA: Correlation analysis, feature-target relationships, and visualization. | Identified key predictors; OverallQual, GrLivArea, and TotalBsmtSF are most important. |
| **3-data-cleaning.ipynb** | Handle missing values, drop noisy features, and prepare clean datasets. | Cleaned train/test sets; missing data imputed or dropped as appropriate. |
| **4-feature-engineering.ipynb** | Encode categoricals, and transform numerical variables. | Chose tranformations for numerical bvariables and categorical variables were encoded. |
| **5-modelling-and-evaluation.ipynb** | Build, tune, and evaluate ML models; select best pipeline. | XGBRegressor selected; full and reduced-feature models compared; metrics reported. |
| **6-four-inherited-houses.ipynb** | Apply production pipeline to Lydia's inherited houses. | Predicted prices for all four houses; results confirm mid-market positioning. |

---

## Dashboard Design

- **Framework:** Streamlit

The dashboard is organized into the following pages, each designed to address a specific business or user need:

### 1. Quick Project Summary
**Purpose:**  
Provides a concise overview of the project, including the business problem, objectives, and key results.  
**Contents:**  
- Project background and Lydia's story  
- Business requirements and goals  
- High-level summary of the solution and its value

### 2. House Price Study (EDA)
**Purpose:**  
Enables users to explore the Ames housing dataset and understand how different features relate to sale price.  
**Contents:**  
- Interactive correlation heatmap of numerical features  
- Scatter plots of top correlated features vs. sale price  
- Box plots for categorical features  
- Distribution plots (histograms) for sale price  
- Feature selection tools for custom visualizations

### 3. Project Hypothesis and Validation
**Purpose:**  
Presents the main hypotheses about the Ames housing market and the evidence used to validate or refute them.  
**Contents:**  
- List of key hypotheses  
- Statistical, model-based, and visual validation for each  
- Clear conclusions for each hypothesis

### 4. Predicted Prices for 4 Inherited Houses
**Purpose:**  
Shows Lydia the predicted sale prices for her four inherited properties using the trained ML model.  
**Contents:**  
- Table of the four houses with their features  
- Predicted sale prices and confidence intervals  
- Comparison to Ames market statistics  
- Visualizations of where these houses fall within the market

### 5. Predict Any House Price
**Purpose:**  
Allows any user to input features for a house in Ames and receive a predicted sale price.  
**Contents:**  
- User-friendly input form for key features  
- Instant price prediction  
- Feature importance and model explanation for the prediction  
- Option to download the prediction result

### 6. ML Model Technical Details
**Purpose:**  
Provides transparency and technical insight into the machine learning models used.  
**Contents:**  
- Description of the modeling approach and feature engineering  
- Model performance metrics (R², RMSE, MAE)  
- Feature importance plots  
- Model comparison tables  

---

**Design Principles:**
- Clean, intuitive sidebar navigation
- Each page addresses a specific business/user need
- EDA plots and model explanations are interactive and concise
- Prediction forms require only the most important features for ease of use
- Responsive design for different devices

---

## Deployment


## Deployment on Heroku

You can deploy this Streamlit dashboard to Heroku by following these steps:

### 1. Prerequisites

- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
- A free [Heroku account](https://signup.heroku.com/)
- Your project files in a Git repository (including `requirements.txt` and a `Procfile`)

### 2. Add a `Procfile`

Create a file named `Procfile` in your project root with the following content:
web: streamlit run app_pages/multipage.py --server.port=$PORT

### 3. Commit your changes

```bash
git add Procfile
git commit -m "Add Procfile for Heroku deployment"
```

### 4. Create a Heroku app

```bash
heroku create your-app-name
```