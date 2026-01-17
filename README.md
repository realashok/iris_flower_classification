## Iris Flower Classification App

This project is a simple machine learning web application that predicts the species of an Iris flower based on its measurements.
It consists of:
        FastAPI backend for model inference
        Streamlit frontend for user interaction
        A trained ML model and scaler loaded with joblib

## Project Structure
    .
    ├── app.py                 # FastAPI backend
    ├── streamlit_app.py       # Streamlit frontend
    ├── iris_classification_model.pkl
    ├── iris_classification_scaler.pkl
    ├── requirements.txt
    └── README.md

Model Details
    Dataset: Iris Dataset
    Input Features:
        Sepal Length (cm)
        Sepal Width (cm)
        Petal Length (cm)
        Petal Width (cm)

    Output:
        0 → Iris-setosa
        1 → Iris-versicolor
        2 → Iris-virginica

Clone the repository

Create and activate virtual environment
    python -m venv venv
    source venv/bin/activate   # Linux / Mac
    venv\Scripts\activate      # Windows

Install dependencies
    pip install -r requirements.txt

Start the FastAPI backend
    uvicorn app:app --reload

Start the Streamlit frontend
    streamlit run streamlit_app.py