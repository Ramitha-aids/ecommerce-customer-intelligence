import pandas as pd
from pathlib import Path

# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
DATA_PATH = BASE_DIR / "data" / "raw" / "online+retail" / "Online Retail.xlsx"

# Read dataset
df = pd.read_excel(DATA_PATH)

# Show original shape
print("Original dataset shape:")
print(df.shape)

# Show missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Show duplicate rows
print("\nDuplicate rows before cleaning:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Show shape after removing duplicates
print("\nDataset shape after removing duplicates:")
print(df.shape)

# Show duplicate count after cleaning
print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

# Remove rows with missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Show shape after removing missing CustomerID
print("\nDataset shape after removing missing CustomerID:")
print(df.shape)

# Check missing CustomerID
print("\nMissing CustomerID after cleaning:")
print(df["CustomerID"].isnull().sum())

# Fill missing product descriptions
df["Description"] = df["Description"].fillna("Unknown")

# Check missing Description
print("\nMissing Description after cleaning:")
print(df["Description"].isnull().sum())

# Check invalid Quantity values
print("\nQuantity less than or equal to 0:")
print((df["Quantity"] <= 0).sum())

# Check invalid UnitPrice values
print("\nUnitPrice less than or equal to 0:")
print((df["UnitPrice"] <= 0).sum())

# Remove invalid transactions
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# Show shape after removing invalid transactions
print("\nDataset shape after removing invalid transactions:")
print(df.shape)

# Verify invalid values are removed
print("\nQuantity <= 0 after cleaning:")
print((df["Quantity"] <= 0).sum())

print("\nUnitPrice <= 0 after cleaning:")
print((df["UnitPrice"] <= 0).sum())

# Calculate revenue for each transaction
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Show first 5 revenue values
print("\nFirst 5 Revenue values:")
print(df[["Quantity", "UnitPrice", "Revenue"]].head())

# Show total revenue
print("\nTotal Revenue:")
print(df["Revenue"].sum())

# Final validation
print("\nFinal dataset shape:")
print(df.shape)

print("\nFinal missing values:")
print(df.isnull().sum())

print("\nFinal duplicate count:")
print(df.duplicated().sum())

print("\nFinal Revenue statistics:")
print(df["Revenue"].describe())

# Save cleaned dataset
CLEANED_PATH = BASE_DIR / "data" / "cleaned"

# Create cleaned folder if it does not exist
CLEANED_PATH.mkdir(parents=True, exist_ok=True)

# Save as CSV
OUTPUT_FILE = CLEANED_PATH / "online_retail_cleaned.csv"
df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaned dataset saved to:")
print(OUTPUT_FILE)