# src/preprocess.py
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_PATH = os.path.join(BASE_DIR, "../data/raw/superstore.csv")
PROCESSED_PATH = os.path.join(BASE_DIR, "../data/processed/processed_data.csv")

def preprocess():
    df = pd.read_csv(RAW_PATH, encoding="latin1")

    # Convert dates
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month

    # Keep relevant columns
    df = df[['Quantity', 'Discount', 'Category', 'Segment', 'Sales']]

    # One-hot encoding
    df = pd.get_dummies(df, columns=['Category', 'Segment'], drop_first=True)

    # Save processed data
    os.makedirs(os.path.join(BASE_DIR, "../data/processed"), exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)
    print("Preprocessing done. Processed file saved.")

if __name__ == "__main__":
    preprocess()
