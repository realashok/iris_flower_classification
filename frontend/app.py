
import streamlit as st
import requests

# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/predict"

# Page config
st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸",
    layout="centered"
)

# Title
st.title("Iris Flower Classification")
st.write("Enter flower measurements to predict the species")

# Input fields
sepal_length = st.number_input(
    "Sepal Length (cm)",
    min_value=0.0,
    step=0.1
)

sepal_width = st.number_input(
    "Sepal Width (cm)",
    min_value=0.0,
    step=0.1
)

petal_length = st.number_input(
    "Petal Length (cm)",
    min_value=0.0,
    step=0.1
)

petal_width = st.number_input(
    "Petal Width (cm)",
    min_value=0.0,
    step=0.1
)

# Predict button
if st.button("Predict"):
    
    # Prepare data
    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    try:
        # Send request to FastAPI
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"Predicted Species: **{prediction}**")
        else:
            st.error("Error from API")

    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to FastAPI. Is the backend running?")
