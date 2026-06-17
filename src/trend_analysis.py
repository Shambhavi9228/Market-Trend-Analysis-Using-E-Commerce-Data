import pandas as pd

df = pd.read_csv("../data/cleaned_market_data.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

# Monthly Sales Trend
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n===== MONTHLY SALES TREND =====")
print(monthly_sales.tail(12))

# Category Trend
category_sales = df.groupby("Category")["Sales"].sum()

print("\n===== CATEGORY SALES =====")
print(category_sales)

# Regional Trend
region_sales = df.groupby("Region")["Sales"].sum()

print("\n===== REGION SALES =====")
print(region_sales)

print("\nTrend analysis completed successfully!")