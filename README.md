# Heritage Housing Issues: Ames, Iowa House Price Prediction

## Project Summary

Lydia Doe, a fictional individual from Belgium, has recently inherited four houses in Ames, Iowa, USA, from her deceased great-grandfather. While Lydia is well-versed in property valuation in her home country, she is acutely aware that the factors influencing house desirability and value in Belgium may not translate directly to the Iowan real estate market. She recognizes that relying solely on her European experience could lead to inaccurate appraisals and potentially significant financial loss or missed opportunity when selling the inherited properties.

Faced with this challenge, Lydia seeks the expertise of a Data Practitioner. Her primary motivations are:
- She does not know the true worth of the four inherited properties and wants to avoid the risk of inaccurate pricing, given the substantial sums at stake.
- She is also interested in being able to predict the sale price of any house in Ames, Iowa, should she consider future property investments in the area.

Through her research, Lydia discovers a public dataset containing detailed records of house prices and attributes for Ames, Iowa. She provides this dataset to the Data Practitioner and requests the development of a data-driven web application to assist with her goals.

**Business Requirements:**
- Lydia wants to understand how various house attributes (such as size, quality, and amenities) correlate with sale price in Ames. She expects clear, interactive data visualizations that reveal these relationships and help her build intuition about the local market.
- She needs accurate predictions of the sale prices for her four inherited houses, based on their specific attributes.
- She also wants the flexibility to predict the sale price of any other house in Ames, Iowa, by entering its key features into the app.

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
| **4-feature-engineering.ipynb** | Create new features, encode categoricals, and transform variables. | Engineered features improved model performance; categorical variables encoded. |
| **5-modelling-and-evaluation.ipynb** | Build, tune, and evaluate ML models; select best pipeline. | XGBRegressor selected; full and reduced-feature models compared; metrics reported. |
| **6-four-inherited-houses.ipynb** | Apply production pipeline to Lydia's inherited houses. | Predicted prices for all four houses; results confirm mid-market positioning. |

---

## Dashboard and Its Design

- **Framework:** Streamlit
- **Pages:**
  1. Quick Project Summary
  2. House Price Study (EDA)
  3. Project Hypothesis and Validation
  4. Predicted Prices for 4 Inherited Houses
  5. Predict Any House Price
  6. ML Model Technical Details

**Design Principles:**
- Clean, intuitive sidebar navigation.
- Each page addresses a specific business/user need.
- EDA plots and model explanations are interactive and concise.
- Prediction forms require only the most important features for ease of use.

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

### 5. Push your code to Heroku

```bash
git push heroku main
```
*(If your default branch is `master`, use `git push heroku master` instead.)*

### 6. Scale the web process

```bash
heroku ps:scale web=1
```

### 7. Open your deployed app

```bash
heroku open
```

---

**Note:**  
- Make sure your `requirements.txt` includes all necessary dependencies.
- If you use files or folders for data, ensure they are included in your repository or handled via environment variables/cloud storage.
