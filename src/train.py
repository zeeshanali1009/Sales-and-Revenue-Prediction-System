# src/train.py
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_PATH = os.path.join(BASE_DIR, "../data/processed/processed_data.csv")
MODEL_DIR = os.path.join(BASE_DIR, "../models")
os.makedirs(MODEL_DIR, exist_ok=True)

# Load processed data
df = pd.read_csv(PROCESSED_PATH)

# Features and target
X = df.drop('Sales', axis=1)
y = df['Sales']

# Save feature names
feature_names = X.columns.tolist()
joblib.dump(feature_names, os.path.join(MODEL_DIR, "feature_names.pkl"))

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, os.path.join(MODEL_DIR, "scaler.pkl"))

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_scaled, y)
joblib.dump(model, os.path.join(MODEL_DIR, "sales_model.pkl"))

print("Training complete. Model saved.")
