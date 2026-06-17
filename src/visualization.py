import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned_market_data.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

# Monthly Sales Trend
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("../results/monthly_sales_trend.png")
plt.close()

# Category Sales
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.ylabel("Sales")

plt.savefig("../results/category_sales_trend.png")
plt.close()

# Regional Sales
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")

plt.title("Regional Sales Performance")
plt.ylabel("Sales")

plt.savefig("../results/regional_sales_trend.png")
plt.close()

print("Trend analysis graphs generated successfully!")