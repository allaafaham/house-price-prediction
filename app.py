import streamlit as st
from app_pages.multipage import MultiPage

# Import your page functions
from app_pages.page_1_Quick_Project_Summary import main as summary_page
from app_pages.page_2_House_Price_Study import main as study_page
from app_pages.page_3_Project_Hypothesis_and_Validation import main as hypothesis_and_validation_page
from app_pages.page_4_Predict_4_Inherited_Prices import main as predict_inherited_page
from app_pages.page_5_Predict_Any_House import main as predict_any_page
from app_pages.page_6_ML_Model_Technichal_Details import main as ml_model_technical_details_page

# Create an instance of the app
app = MultiPage(app_name="House Prices Project")

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", summary_page)
app.add_page("House Price Study", study_page)
app.add_page("Project Hypothesis and Validation", hypothesis_and_validation_page)
app.add_page("Predict 4 Inherited Prices", predict_inherited_page)
app.add_page("Predict Any House", predict_any_page)
app.add_page("ML Model Technical Details", ml_model_technical_details_page)

# Run the app
app.run() 