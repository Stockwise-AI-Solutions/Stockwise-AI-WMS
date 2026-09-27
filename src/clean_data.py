import pandas as pd

# Load the data we downloaded for the project
df = pd.read_csv('data/warehouse_data.csv')
print("Loaded", len(df), "rows")

# Check for missing values and duplicates
print("Total missing values:", df.isnull().sum().sum())
print("Total duplicate rows:", df.duplicated().sum())

# Fill missing numbers with the median
# We use median because it doesn't get messed up by extreme values like the mean does
for col in df.columns:
    if df[col].dtype == 'float64' or df[col].dtype == 'int64':
        df[col] = df[col].fillna(df[col].median())

# Fill missing text with 'Unknown'
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna('Unknown')

# Remove the duplicates
df = df.drop_duplicates()
print("Rows after removing duplicates:", len(df))

# Make sure the date column is actually a date
df['last_restock_date'] = pd.to_datetime(df['last_restock_date'], errors='coerce')

# Save it to a new file so we don't mess up the original data
df.to_csv('data/cleaned_warehouse_data.csv', index=False)
print("Saved the clean data to cleaned_warehouse_data.csv")