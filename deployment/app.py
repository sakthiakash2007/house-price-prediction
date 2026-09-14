import streamlit as st
import requests

st.title("House Price Prediction App")
st.write("Enter the house details below.")

with st.form("house_details", border=True):

    area = st.number_input(
        "Area",
        min_value=0.0,
        value=1500.0
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        value=2
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0,
        value=2
    )

    age = st.number_input(
        "House age",
        min_value=0,
        value=5
    )

    distance_city = st.number_input(
        "Distance from city",
        min_value=0.0,
        value=5.0
    )

    submitted = st.form_submit_button(
        "Predict house price",
        type="primary"
    )


if submitted:

    data = {
        "Area": area,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Age": age,
        "Distance_City": distance_city
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    predicted_price = result["predicted_price"]

    st.metric(
        "Estimated House Price",
        f"{predicted_price:,.2f} lakhs"
    )