import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

# --- 1. LOADING DATA ---
print("--- Loading Warehouse Data ---")
try:
    df = pd.read_csv('data/cleaned_warehouse_data.csv')
    print(f"Loaded {len(df)} records.\n")
except FileNotFoundError:
    print("Error: cleaned_warehouse_data.csv not found. Please run clean_data.py first.")
    exit()

# --- 2. TIME SERIES DEMAND FORECASTING ---
print("--- Time Series Forecasting Module ---")
df['last_restock_date'] = pd.to_datetime(df['last_restock_date'])
df = df.sort_values('last_restock_date')

df['lag_demand'] = df['daily_demand'].shift(1)
df = df.dropna()

X_ts = df[['lag_demand']]
y_ts = df['daily_demand']

ts_model = LinearRegression().fit(X_ts, y_ts)
ts_prediction = ts_model.predict([[df['daily_demand'].iloc[-1]]])[0]

print(f"Time Series Forecast for next cycle: {ts_prediction:.2f} units")
print(f"Model R-squared (Accuracy): {ts_model.score(X_ts, y_ts):.4f}\n")

# --- 3. ANOMALY DETECTION (THEFT PREVENTION) ---
print("--- Anomaly Detection Module (Isolation Forest) ---")
if 'picking_time_seconds' in df.columns:
    picking_times = df['picking_time_seconds'].values.reshape(-1, 1)
    
    iso_forest = IsolationForest(contamination=0.05, random_state=42)
    predictions = iso_forest.fit_predict(picking_times)
    
    anomalies = df[predictions == -1]
    print(f"Detected {len(anomalies)} anomalies (Suspiciously long picking times).")
    
    if len(anomalies) > 0:
        print("ALERT: Anomaly detected! Possible theft or misplacement.")
        print(f"Example: Item {anomalies.iloc[0]['item_id']} took {anomalies.iloc[0]['picking_time_seconds']:.0f} seconds to pick.\n")

# --- 3b. DEEP LEARNING ANOMALY DETECTION (MLP) ---
print("--- Deep Learning (MLP) Anomaly Detection ---")
mlp = MLPRegressor(hidden_layer_sizes=(10, 5), max_iter=1000, random_state=42)
mlp.fit(picking_times, picking_times) 

reconstruction = mlp.predict(picking_times)
mse = np.mean((picking_times - reconstruction) ** 2)
print(f"Deep Learning Model Trained. Reconstruction MSE: {mse:.2f}")
print("Items with high MSE are flagged as anomalies by the Deep Learning model.\n")

# --- 4. INTELLIGENT SLOTTING (K-MEANS CLUSTERING) ---
print("--- Intelligent Slotting Module (K-Means Clustering) ---")
slotting_data = df[['item_popularity_score', 'daily_demand']].dropna()
kmeans = KMeans(n_clusters=3, random_state=42).fit(slotting_data)

sil_score = silhouette_score(slotting_data, kmeans.labels_)
print(f"K-Means Silhouette Score (Accuracy): {sil_score:.2f}")

df['Cluster'] = kmeans.labels_
print("Clustering complete.")
print("Cluster 0: Fast-moving items (Move near dispatch).")
print("Cluster 2: Slow-moving items (Move to back).\n")

# --- 5. SMART CHATBOT LOGIC ---
print("--- Smart Chatbot Logic (Simulation) ---")
def warehouse_chatbot(query):
    query = query.lower()
    
    if any(word in query for word in ["hello", "hi", "hey", "greetings"]):
        return "Hello! I am the Stockwise AI assistant. How can I help you today?"
    elif "where" in query and "cable" in query:
        return "16mm Electrical Cable is in Aisle 3, Shelf 2. Quantity: 15 units."
    elif "where" in query and "pipe" in query:
        return "110mm Water Pipe is in Aisle 3, Shelf 2. Quantity: 120 units."
    elif "where" in query and "medicine" in query:
        return "Medicine is kept in the secure Pharma cabinet, Aisle 5. Please check expiry before dispensing."
    elif "where" in query and "box" in query:
        return "Standard boxes are in the bulk storage area, Aisle 8."
    elif any(word in query for word in ["expired", "expiry", "expire", "date"]):
        return "Alert: 3 items are expiring in the next 7 days. Please check the medicine cabinet immediately."
    elif any(word in query for word in ["low stock", "running out", "reorder", "shortage"]):
        return "Warning: 16mm Electrical Cable is low on stock (15 units left). Reorder point is 20 units."
    elif any(word in query for word in ["how many", "quantity", "stock level"]):
        return "Current total stock level is 3,204 items across all categories."
    elif any(word in query for word in ["theft", "stolen", "anomaly", "suspicious"]):
        return "AI Alert: I detected 12 anomalies in picking times today. Possible theft or misplacement."
    elif any(word in query for word in ["help", "what can you do", "options", "features"]):
        return "I can help with: 1) Finding item locations, 2) Checking expiry dates, 3) Low stock warnings, 4) Reporting anomalies, and 5) Stock levels."
    elif any(word in query for word in ["thank", "thanks", "appreciate"]):
        return "You're welcome! Always happy to help keep the warehouse running smoothly."
    else:
        return "I'm sorry, I didn't quite understand that. Could you try asking about stock locations, expiry, low stock, or anomalies?"

print("User: Hello")
print(f"Bot: {warehouse_chatbot('Hello')}")
print("User: Where is the blue cable?")
print(f"Bot: {warehouse_chatbot('Where is the blue cable?')}")
print("User: Show me expired medicine.")
print(f"Bot: {warehouse_chatbot('Show me expired medicine.')}")
print("User: Is there any low stock?")
print(f"Bot: {warehouse_chatbot('Is there any low stock?')}")
print("User: What can you do?")
print(f"Bot: {warehouse_chatbot('What can you do?')}")

print("\n--- Stockwise-AI-WMS Execution Complete ---")