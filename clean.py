import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Fix date columns
df['Order Date'] = pd.to_datetime(df['Order Date']).dt.strftime('%Y-%m-%d')
df['Ship Date'] = pd.to_datetime(df['Ship Date']).dt.strftime('%Y-%m-%d')

# Clean column names (remove spaces)
df.columns = df.columns.str.replace(' ', '_').str.replace('-', '_')

# Save cleaned version
df.to_csv("superstore_clean.csv", index=False)
print("Done! Rows:", len(df))
print(df.head())