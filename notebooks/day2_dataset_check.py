import pandas as pd
from pathlib import Path

# Build path relative to this script's location, not the working directory
BASE_DIR = Path(__file__).resolve().parent.parent  # goes up to project root
DATA_PATH = BASE_DIR / "data" / "raw" / "Online Retail.xlsx"

# Read the Excel dataset
df = pd.read_excel(DATA_PATH)

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Show number of rows and columns
print("\nNumber of rows and columns:")
print(df.shape)

# Show column names
print("\nColumn names:")
print(df.columns)

# Show data types
print("\nData types:")
print(df.dtypes)

# Show missing values
print("\nMissing values:")
print(df.isnull().sum())

# Show duplicate records
print("\nDuplicate records:")
print(df.duplicated().sum())