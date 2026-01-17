from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI
app = FastAPI(title="Iris Flower Prediction API")

# Load model & scaler
model = joblib.load("iris_classification_model.pkl")
scaler = joblib.load("iris_classification_scaler.pkl")

# Input schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Output mapping (optional but cleaner)
species_map = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

# Root endpoint
@app.get("/")
def home():
    return {"message": "Iris Classification API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(data: IrisInput):

    # Convert input to array
    input_data = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])

    # Scale input
    scaled_data = scaler.transform(input_data)

    # Predict
    prediction = model.predict(scaled_data)[0]

    return {
        "prediction": prediction
    }
