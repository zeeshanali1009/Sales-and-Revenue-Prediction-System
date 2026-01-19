# src/predict.py
import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "../models")

# Load trained objects
model = joblib.load(os.path.join(MODEL_DIR, "sales_model.pkl"))
scaler = joblib.load(os.path.join(MODEL_DIR, "scaler.pkl"))
feature_names = joblib.load(os.path.join(MODEL_DIR, "feature_names.pkl"))

def predict_sales(quantity, discount, category, segment):
    # Create input DataFrame
    input_df = pd.DataFrame([[quantity, discount, category, segment]],
                            columns=['Quantity', 'Discount', 'Category', 'Segment'])

    # One-hot encode like training
    input_df = pd.get_dummies(input_df, columns=['Category', 'Segment'], drop_first=True)

    # Add missing columns with 0
    for col in feature_names:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[feature_names]

    # Scale and predict
    input_scaled = scaler.transform(input_df)
    pred = model.predict(input_scaled)[0]
    return pred
