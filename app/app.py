
import streamlit as st
import pandas as pd
import numpy as np
import os
from catboost import CatBoostClassifier

# -------------------------------------------------
# Paths (important for Docker and portability)
# -------------------------------------------------

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "catboost_model.cbm")
LOG_FILE = os.path.join(BASE_DIR, "prediction_logs.csv")

# -------------------------------------------------
# Load CatBoost Model
# -------------------------------------------------

model = CatBoostClassifier()
model.load_model(MODEL_PATH)

# -------------------------------------------------
# Feature Columns (same order used in training)
# -------------------------------------------------

feature_columns = [
    "Temperature", "pH", "Dissolved O2", "COD", "Nitrate N", "Amonia N",
    "Phosphate", "Fecal Coliform", "Total Coliform", "Turbidity",
    "Total Dissolved Solids", "Hardness CaCo3", "Chlorides", "Sulphate"
]

# -------------------------------------------------
# Class Mapping
# -------------------------------------------------

class_mapping = {
    0: "A (Drinking Water source without conventional treatment but after disinfection)",
    1: "B (Outdoor bathing)",
    2: "C (Drinking water source)",
    3: "E (Irrigation / Industrial cooling / Controlled waste)"
}

# -------------------------------------------------
# Streamlit UI
# -------------------------------------------------

st.title("💧 Water Quality Classification App")
st.write("Enter water quality parameters to predict the water use-based classification.")

# Sidebar Inputs
input_data = {}

with st.sidebar:
    st.header("Water Quality Parameters")

    default_values = {
        "Temperature": 25.0,
        "pH": 7.5,
        "Dissolved O2": 6.0,
        "COD": 15.0,
        "Nitrate N": 1.0,
        "Amonia N": 0.5,
        "Phosphate": 0.3,
        "Fecal Coliform": 50.0,
        "Total Coliform": 200.0,
        "Turbidity": 2.0,
        "Total Dissolved Solids": 300.0,
        "Hardness CaCo3": 100.0,
        "Chlorides": 20.0,
        "Sulphate": 30.0
    }

    for col in feature_columns:
        input_data[col] = st.number_input(
            f"{col}",
            value=default_values[col],
            min_value=0.0
        )

# -------------------------------------------------
# Convert Inputs to DataFrame
# -------------------------------------------------

input_df = pd.DataFrame([input_data])

st.subheader("Input Data for Prediction")
st.dataframe(input_df)

# -------------------------------------------------
# Prediction
# -------------------------------------------------

if st.button("Predict Water Class"):

    prediction_proba = model.predict_proba(input_df)

    predicted_class_index = np.argmax(prediction_proba, axis=1)[0]
    predicted_class_label = class_mapping[predicted_class_index]

    # Display Prediction
    st.subheader("Prediction Result")
    st.success(predicted_class_label)

    # Probability Distribution
    st.subheader("Prediction Probability Distribution")

    proba_df = pd.DataFrame({
        "Class": list(class_mapping.values()),
        "Probability": prediction_proba[0]
    })

    st.bar_chart(proba_df.set_index("Class"))

    # -------------------------------------------------
    # Prediction Logging
    # -------------------------------------------------

    log_data = input_df.copy()
    log_data["Prediction"] = predicted_class_label

    log_data.to_csv(
        LOG_FILE,
        mode="a",
        header=not os.path.exists(LOG_FILE),
        index=False
    )

    st.success("Prediction logged successfully.")

# -------------------------------------------------
# Sidebar Info
# -------------------------------------------------

st.sidebar.subheader("About the App")

st.sidebar.info(
    "This application predicts water quality classification using a "
    "CatBoost machine learning model based on multiple chemical parameters."
)

