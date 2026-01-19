# app.py
import streamlit as st
from src.predict import predict_sales

st.set_page_config(page_title="Sales Prediction System")
st.title("📊 Sales Prediction System")
st.markdown("Predict future sales using historical trends and machine learning.")

# Input fields
quantity = st.number_input("Quantity Sold", min_value=1, value=5)
discount = st.slider("Discount", min_value=0.0, max_value=1.0, value=0.1)
category = st.selectbox("Product Category", ["Technology", "Furniture", "Office Supplies"])
segment = st.selectbox("Customer Segment", ["Consumer", "Corporate", "Home Office"])

if st.button("Predict Sales"):
    prediction = predict_sales(quantity, discount, category, segment)
    st.success(f"💰 Predicted Sales: ${prediction:.2f}")
