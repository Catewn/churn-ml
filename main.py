import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Customer Churn Prediction')
st.header('Data Visualization')

# from backend import initial_cleaning
from PIL import Image

# This is to supress the warning messages (if any) generated in our code:
import warnings

warnings.filterwarnings('ignore')

st.subheader('Creditscore predictor')
image = Image.open('hist_creditscore.png')
st.image(image, caption='Graphical Representation of data by Credit Score')

col1, col_mid, col2 = st.beta_columns((1, 0.1, 1))
with col1:
        st.subheader('Age predictor')
        image = Image.open('hist_age.png')
        st.image(image, caption='Graphical Representation of data by customer age')

with col2:
        st.subheader('Geography predictor')
        image = Image.open('hist_geography.png')
        st.image(image, caption='Graphical Representation of data by customer Geographical location')

st.header('Feature Importance')
st.subheader("Features that predict customer's probability to  churn")
image = Image.open('hist_featureimportance.png')
st.image(image, caption='Graphical Representation of Feature Importance')



st.markdown('The results indicate an accuracy of 82.3%, which means that our algorithm successfully predicts customer churn 82.3% of the time.')



