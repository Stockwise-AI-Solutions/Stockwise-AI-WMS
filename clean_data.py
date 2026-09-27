import pandas as pd

# loading of the raw data
df = pd.read_csv('data/warehouse_data.csv')
print("Original columns:", len(df.columns))
print(df.columns.tolist())

# we only need these specific columns for our AI models and the dashboard
# forecast: item_popularity_score, daily_demand
# anomaly: picking_time_seconds
# slotting: storage_location_id, zone, stock_level
# dashboard: item_id, category, unit_price
columns_to_keep = [
    'item_id', 
    'category', 
    'stock_level', 
    'reorder_point',
    'daily_demand', 
    'item_popularity_score', 
    'storage_location_id', 
    'zone', 
    'picking_time_seconds', 
    'unit_price', 
    'last_restock_date'
]

# we are keeping only those columns
df_clean = df[columns_to_keep].copy()

# making sure the date column is properly formatted
df_clean['last_restock_date'] = pd.to_datetime(df_clean['last_restock_date'], errors='coerce')

# checking the final result
print("New columns:", len(df_clean.columns))
print("Rows in cleaned file:", len(df_clean))

# saving it to a new file
df_clean.to_csv('data/cleaned_warehouse_data.csv', index=False)
print("Saved the clean data to data/cleaned_warehouse_data.csv")