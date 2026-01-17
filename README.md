# 🌸 Iris Flower Classification App

This project is a simple **Machine Learning web application** that predicts the species of an **Iris flower** based on its measurements.

The application uses a **FastAPI backend** for model inference and a **Streamlit frontend** for user interaction.

---

## 📌 Project Overview

The Iris Flower Classification App allows users to input flower measurements and instantly get a prediction of the Iris species using a trained machine learning model.

### Components:

* **FastAPI** – Backend API for predictions
* **Streamlit** – Interactive web UI
* **Scikit-learn model** – Trained on the Iris dataset
* **Joblib** – Used to load the model and scaler

---

## 📁 Project Structure

```
.
├── app.py                         # FastAPI backend
├── streamlit_app.py               # Streamlit frontend
├── iris_classification_model.pkl  # Trained ML model
├── iris_classification_scaler.pkl # Feature scaler
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
```

---

## 🧠 Model Details

* **Dataset:** Iris Dataset

* **Input Features:**

  * Sepal Length (cm)
  * Sepal Width (cm)
  * Petal Length (cm)
  * Petal Width (cm)

* **Target Classes:**

  * `0` → Iris-setosa
  * `1` → Iris-versicolor
  * `2` → Iris-virginica

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/realashok/iris_flower_classification.git
cd iris_flower_classification
```

---

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
```

**Activate the environment:**

* **Linux / macOS**

```bash
source venv/bin/activate
```

* **Windows**

```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### Start the FastAPI Backend

```bash
uvicorn app:app --reload
```

Backend will be available at:
**[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

### Start the Streamlit Frontend

```bash
streamlit run streamlit_app.py
```

The Streamlit app will open automatically in your browser.

---

## 📊 How It Works

1. User enters Iris flower measurements
2. Data is scaled using the trained scaler
3. Model predicts the flower species
4. Result is displayed on the Streamlit UI

---

## 🛠️ Technologies Used

* Python
* FastAPI
* Streamlit
* Scikit-learn
* Joblib
* Uvicorn

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 🙌 Acknowledgments

* UCI Machine Learning Repository
* Scikit-learn Iris Dataset

