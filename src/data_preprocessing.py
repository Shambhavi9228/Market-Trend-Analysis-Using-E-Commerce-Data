import pandas as pd

df = pd.read_csv("../data/Sample - Superstore.csv", encoding="latin1")

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

df["Order Date"] = pd.to_datetime(df["Order Date"])

df.to_csv("../data/cleaned_market_data.csv", index=False)

print("\nCleaned dataset saved successfully!")