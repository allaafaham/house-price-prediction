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

1. **OverallQual is the most influential variable for SalePrice.**
   - *Validation:* Highest Pearson correlation (ρ ≈ 0.79), top model-based importance (gain = 0.676), and clear monotonic trend in visualizations.
   - *Result:* Strongly supported by all analyses.

2. **A tuned XGBRegressor outperforms linear and bagged tree models, achieving R² > 0.85 and RMSE < $30,000.**
   - *Validation:* Cross-validation and test set results confirm XGBRegressor as best performer (R² = 0.8966, RMSE = $26,725).
   - *Result:* Confirmed.

3. **The four inherited houses are mid-priced within the Ames distribution.**
   - *Validation:* Predicted prices cluster around the sample mean ($163,904 vs. dataset mean ≈ $175,000).
   - *Result:* Confirmed; all four are within one interquartile range of the median.

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

- **Local Deployment:**  
  1. Clone the repository.
  2. Create and activate a Python 3.11+ virtual environment.
  3. Install dependencies:
     ```
     pip install -r requirements.txt
     ```
  4. Run the dashboard:
     ```
     streamlit run app_pages/multipage.py
     ```