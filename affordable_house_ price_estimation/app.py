import streamlit as st
import pickle
import pandas as pd
import numpy as np


model = pickle.load(open("house_model.pkl", "rb"))

data = pd.read_csv("Bengaluru_House_Data_Cleaned.csv")
locations = sorted(data['location'].unique())


st.set_page_config(
    page_title="Affordable Housing Price Estimator",
    layout="centered"
)


st.markdown(
    "<h1 style='text-align:center; color:#1f4e79;'>Affordable Housing Price Estimator</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center;'>Bangalore Housing Price Estimator</h4>",
    unsafe_allow_html=True
)

st.write("---")

st.subheader("Enter Property Details")


total_sqft = st.number_input("Total Square Feet", min_value=300)
bath = st.number_input("Number of Bathrooms", min_value=1)
bhk = st.number_input("Number of Bedrooms (BHK)", min_value=1)
location = st.selectbox("Select Location", locations)

st.write("")


if st.button("Predict Price"):
    
    input_data = np.array([[total_sqft, bath]]) 

    prediction = model.predict(input_data)

    st.success(f"Estimated House Price: ₹ {int(prediction[0])} Lakhs")