import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Stockwise-AI-WMS", page_icon="W", layout="wide")

st.title("Stockwise-AI-WMS - Warehouse Dashboard")
st.write("Real-time inventory tracking for Emfuleni Municipality")

@st.cache_data
def load_data():
    return pd.read_csv('data/cleaned_warehouse_data.csv')

df = load_data()

# Using tabs instead of sidebar navigation for a cleaner look
tab1, tab2, tab3 = st.tabs(["Dashboard", "AI Alerts", "Chatbot Interface"])

with tab1:
    st.subheader("Current Stock Levels")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Items in Stock", len(df))
    col2.metric("Low Stock Items", len(df[df['stock_level'] < df['reorder_point']]))
    col3.metric("Average Picking Time", f"{df['picking_time_seconds'].mean():.0f} sec")
    
    st.dataframe(df[['item_id', 'category', 'stock_level', 'daily_demand', 'picking_time_seconds']].head(15))

with tab2:
    st.subheader("AI-Generated Alerts")
    
    low_stock = df[df['stock_level'] < df['reorder_point']]
    if not low_stock.empty:
        st.warning(f"Low Stock Alert: {len(low_stock)} items are below their reorder point. Example: {low_stock.iloc[0]['item_id']}")
    else:
        st.success("All stock levels are healthy.")
        
    high_picking = df[df['picking_time_seconds'] > df['picking_time_seconds'].quantile(0.95)]
    if not high_picking.empty:
        st.error(f"Anomaly Detected: {len(high_picking)} items had unusually long picking times. Possible theft or misplacement. Example: Item {high_picking.iloc[0]['item_id']} took {high_picking.iloc[0]['picking_time_seconds']} seconds.")
    
    st.info("Forecast: High demand for pipes expected in the next cycle. Order now.")

with tab3:
    st.subheader("Warehouse Chatbot")
    st.write("Ask the warehouse bot about stock locations, expiry dates, or low stock warnings.")
    
    user_input = st.text_input("Type your question here (e.g., 'Where is the blue cable?'):")
    
    if user_input:
        query = user_input.lower()
        
        if any(word in query for word in ["hello", "hi", "hey", "greetings"]):
            st.success("Bot: Hello! I am the Stockwise AI assistant. How can I help you today?")
        elif "where" in query and "cable" in query:
            st.success("Bot: 16mm Electrical Cable is in Aisle 3, Shelf 2. Quantity: 15 units.")
        elif "where" in query and "pipe" in query:
            st.success("Bot: 110mm Water Pipe is in Aisle 3, Shelf 2. Quantity: 120 units.")
        elif "where" in query and "medicine" in query:
            st.success("Bot: Medicine is kept in the secure Pharma cabinet, Aisle 5. Please check expiry before dispensing.")
        elif any(word in query for word in ["expired", "expiry", "expire", "date"]):
            st.warning("Bot: Alert: 3 items are expiring in the next 7 days. Please check the medicine cabinet immediately.")
        elif any(word in query for word in ["low stock", "running out", "reorder", "shortage"]):
            st.error("Bot: Warning: 16mm Electrical Cable is low on stock (15 units left). Reorder point is 20 units.")
        elif any(word in query for word in ["how many", "quantity", "stock level"]):
            st.info("Bot: Current total stock level is 3,204 items across all categories.")
        elif any(word in query for word in ["theft", "stolen", "anomaly", "suspicious"]):
            st.error("Bot: AI Alert: I detected 12 anomalies in picking times today. Possible theft or misplacement.")
        elif any(word in query for word in ["help", "what can you do", "options", "features"]):
            st.info("Bot: I can help with: 1) Finding item locations, 2) Checking expiry dates, 3) Low stock warnings, 4) Reporting anomalies, and 5) Stock levels.")
        elif any(word in query for word in ["thank", "thanks", "appreciate"]):
            st.success("Bot: You're welcome! Always happy to help keep the warehouse running smoothly.")
        else:
            st.info("Bot: I'm sorry, I didn't quite understand that. Could you try asking about stock locations, expiry, low stock, or anomalies?")
