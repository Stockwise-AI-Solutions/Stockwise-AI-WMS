import streamlit as st
import pandas as pd

st.title("Stockwise AI - Warehouse Dashboard")
st.write("Real-time inventory tracking for Emfuleni Municipality")

# loading the cleaned dataset
df = pd.read_csv('data/cleaned_warehouse_data.csv')

st.subheader("Current Stock Levels")
# showing the first 10 rows of relevant columns
if 'item_id' in df.columns and 'stock_level' in df.columns:
    st.dataframe(df[['item_id', 'category', 'stock_level', 'daily_demand']].head(10))
else:
    st.dataframe(df.head(10))

st.subheader("AI Alerts")
st.warning("Low Stock: 16mm Electrical Cable (15 units left)")
st.error("Anomaly Detected: Picking time over 600 seconds on Item 45. Possible theft.")
st.success("Forecast: High demand for pipes expected. Order now.")

st.subheader("Chatbot Interface")
user_input = st.text_input("Ask the warehouse bot (e.g., 'Where is the blue cable?'):")
if user_input:
    if "pipe" in user_input.lower():
        st.write("Bot: 110mm Water Pipe is in Aisle 3, Shelf 2. Quantity: 120.")
    elif "expired" in user_input.lower():
        st.write("Bot: Alert: 3 items are expiring in 7 days.")
    else:
        st.write("Bot: I'm sorry, I didn't understand.")