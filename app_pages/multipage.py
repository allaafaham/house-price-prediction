import streamlit as st
from app_pages import page_1_Quick_Project_Summary, page_2_House_Price_Study, page_3_Project_Hypothesis_and_Validation, page_4_Predict_4_Inherited_Prices, page_5_Predict_Any_House, page_6_ML_Model_Technichal_Details


# Class to generate multiple Streamlit pages using an object oriented approach
class MultiPage:

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="📈")
            # Icon from https://smiley.cool/twitter-emoji.php

    def add_page(self, title, func) -> None:
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio(
            'Menu', self.pages, format_func=lambda page: page['title']
            )
        page['function']()

