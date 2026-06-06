# DecodeLabs Project 2: Exploratory Data Analysis (EDA)
# Run this script after placing Decode_Project1_Final_Output.xlsx in the same folder.

import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "Decode_Project1_Final_Output.xlsx"

# Read cleaned dataset. Supports both common sheet names used in Project 1 outputs.
try:
    df = pd.read_excel(file_path, sheet_name="Cleaned Dataset")
except ValueError:
    df = pd.read_excel(file_path, sheet_name="Cleaned_Data")

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

numeric_cols = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]
categorical_cols = ["Product", "PaymentMethod", "OrderStatus", "ReferralSource", "CouponCode"]
os.makedirs("charts", exist_ok=True)

# Dataset overview
overview = pd.DataFrame({
    "Metric": ["Number of Rows", "Number of Columns", "Total Missing Values", "Duplicate Rows", "Duplicate OrderID", "Unique Orders", "Unique Customers", "Unique Products", "Total Revenue", "Average Order Value", "Invalid Dates"],
    "Value": [df.shape[0], df.shape[1], df.isna().sum().sum(), df.duplicated().sum(), df.duplicated(subset=["OrderID"]).sum(), df["OrderID"].nunique(), df["CustomerID"].nunique(), df["Product"].nunique(), round(df["TotalPrice"].sum(), 2), round(df["TotalPrice"].mean(), 2), df["Date"].isna().sum()]
})

# Descriptive statistics
descriptive_stats = df[numeric_cols].describe().T.round(2)

# Distribution summary
distribution_summary = pd.DataFrame({
    "Column": numeric_cols,
    "Mean": [df[col].mean() for col in numeric_cols],
    "Median": [df[col].median() for col in numeric_cols],
    "Skewness": [df[col].skew() for col in numeric_cols]
}).round(2)

# Outlier detection using IQR
outlier_results = []
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outlier_results.append({
        "Column": col,
        "Q1": Q1,
        "Q3": Q3,
        "IQR": IQR,
        "Lower Bound": lower_bound,
        "Upper Bound": upper_bound,
        "Outlier Count": len(outliers),
        "Outlier Percentage": len(outliers) / len(df) * 100
    })
outlier_report = pd.DataFrame(outlier_results).round(2)

# Categorical analysis
product_revenue = df.groupby("Product")["TotalPrice"].sum().reset_index().sort_values("TotalPrice", ascending=False).round(2)
payment_revenue = df.groupby("PaymentMethod")["TotalPrice"].sum().reset_index().sort_values("TotalPrice", ascending=False).round(2)
status_percentage = (df["OrderStatus"].value_counts(normalize=True) * 100).reset_index()
status_percentage.columns = ["Order Status", "Percentage"]
status_percentage["Percentage"] = status_percentage["Percentage"].round(2)
referral_revenue = df.groupby("ReferralSource")["TotalPrice"].sum().reset_index().sort_values("TotalPrice", ascending=False).round(2)
coupon_usage = df["CouponCode"].value_counts().reset_index()
coupon_usage.columns = ["Coupon Code", "Order Count"]

# Trend analysis
df["Year"] = df["Date"].dt.year
df["YearMonth"] = df["Date"].dt.to_period("M").astype(str)
monthly_revenue = df.groupby("YearMonth")["TotalPrice"].sum().reset_index().sort_values("YearMonth").round(2)
monthly_orders = df.groupby("YearMonth")["OrderID"].count().reset_index()
monthly_orders.columns = ["YearMonth", "Order Count"]
monthly_aov = df.groupby("YearMonth")["TotalPrice"].mean().reset_index()
monthly_aov.columns = ["YearMonth", "Average Order Value"]
monthly_aov["Average Order Value"] = monthly_aov["Average Order Value"].round(2)
monthly_trend = monthly_revenue.merge(monthly_orders, on="YearMonth").merge(monthly_aov, on="YearMonth")
monthly_trend.columns = ["YearMonth", "Total Revenue", "Order Count", "Average Order Value"]

yearly_revenue = df.groupby("Year")["TotalPrice"].sum().reset_index().round(2)
yearly_orders = df.groupby("Year")["OrderID"].count().reset_index()
yearly_orders.columns = ["Year", "Order Count"]

# Correlation analysis
correlation_matrix = df[numeric_cols].corr().round(2)

# Charts
plt.figure(figsize=(10, 5))
plt.plot(monthly_trend["YearMonth"], monthly_trend["Total Revenue"], marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/monthly_revenue_trend.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(product_revenue["Product"], product_revenue["TotalPrice"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/revenue_by_product.png")
plt.show()

# Export Excel report
with pd.ExcelWriter("Decode_Project2_EDA_Report.xlsx") as writer:
    overview.to_excel(writer, sheet_name="Dataset Overview", index=False)
    descriptive_stats.to_excel(writer, sheet_name="Descriptive Stats")
    distribution_summary.to_excel(writer, sheet_name="Distribution", index=False)
    outlier_report.to_excel(writer, sheet_name="Outlier Report", index=False)
    product_revenue.to_excel(writer, sheet_name="Product Revenue", index=False)
    payment_revenue.to_excel(writer, sheet_name="Payment Revenue", index=False)
    status_percentage.to_excel(writer, sheet_name="Order Status", index=False)
    referral_revenue.to_excel(writer, sheet_name="Referral Revenue", index=False)
    coupon_usage.to_excel(writer, sheet_name="Coupon Usage", index=False)
    monthly_trend.to_excel(writer, sheet_name="Monthly Trend", index=False)
    yearly_revenue.to_excel(writer, sheet_name="Yearly Revenue", index=False)
    yearly_orders.to_excel(writer, sheet_name="Yearly Orders", index=False)
    correlation_matrix.to_excel(writer, sheet_name="Correlation Matrix")

print("Project 2 EDA completed successfully.")
