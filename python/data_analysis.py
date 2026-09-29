import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# LOAD DATA
# ==========================================

file_path = "data/Sample - Superstore.xlsx"

df = pd.read_excel(file_path)


# ==========================================
# DATA CLEANING
# ==========================================

df = df.drop_duplicates()

df["Postal Code"] = df["Postal Code"].fillna(0)


# ==========================================
# BUSINESS KPIs
# ==========================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

average_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100


print("\n========== BUSINESS KPIs ==========")

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Average Order Value: ${average_order_value:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")


# ==========================================
# SALES & PROFIT BY CATEGORY
# ==========================================

category_analysis = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).sort_values("Total_Sales", ascending=False)

print("\n========== SALES & PROFIT BY CATEGORY ==========")

print(category_analysis)


# ==========================================
# SALES & PROFIT BY SUB-CATEGORY
# ==========================================

subcategory_analysis = df.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).sort_values("Total_Sales", ascending=False)

print("\n========== SALES & PROFIT BY SUB-CATEGORY ==========")

print(subcategory_analysis)


# ==========================================
# DISCOUNT & PROFIT ANALYSIS
# ==========================================

discount_analysis = df.groupby("Sub-Category").agg(
    Average_Discount=("Discount", "mean"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).sort_values("Average_Discount", ascending=False)

print("\n========== DISCOUNT & PROFIT BY SUB-CATEGORY ==========")

print(discount_analysis)


# ==========================================
# CHART 1: SALES VS PROFIT
# ==========================================

plt.figure(figsize=(12, 7))

plt.scatter(
    subcategory_analysis["Total_Sales"],
    subcategory_analysis["Total_Profit"]
)

for subcategory, row in subcategory_analysis.iterrows():

    plt.annotate(
        subcategory,
        (row["Total_Sales"], row["Total_Profit"]),
        xytext=(5, 5),
        textcoords="offset points"
    )

plt.axhline(y=0, linestyle="--")

plt.title("Sales vs Profit by Sub-Category")
plt.xlabel("Total Sales ($)")
plt.ylabel("Total Profit ($)")

plt.tight_layout()

plt.savefig(
    "visualizations/sales_vs_profit_subcategory.png",
    dpi=300
)

# CLOSE CHART 1
plt.close()


# ==========================================
# MONTHLY SALES
# ==========================================

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n========== MONTHLY SALES ==========")

print(monthly_sales)


# ==========================================
# CHART 2: MONTHLY SALES TREND
# ==========================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Sales ($)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "visualizations/monthly_sales_trend.png",
    dpi=300
)

# CLOSE CHART 2
plt.close()


print("\n===================================")
print("ANALYSIS COMPLETED SUCCESSFULLY!")
print("Charts saved in visualizations folder.")
print("===================================")

# ==========================================
# CUSTOMER ANALYSIS
# ==========================================

# Top 10 customers by sales
top_customers_sales = df.groupby("Customer Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique")
).sort_values("Total_Sales", ascending=False).head(10)

print("\n========== TOP 10 CUSTOMERS BY SALES ==========")

print(top_customers_sales)


# ==========================================
# CUSTOMER SEGMENT ANALYSIS
# ==========================================

segment_analysis = df.groupby("Segment").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Total_Orders=("Order ID", "nunique")
).sort_values("Total_Sales", ascending=False)

print("\n========== CUSTOMER SEGMENT ANALYSIS ==========")

print(segment_analysis)

# ==========================================
# CUSTOMER SEGMENT SALES CHART
# ==========================================

plt.figure(figsize=(8, 5))

plt.bar(
    segment_analysis.index,
    segment_analysis["Total_Sales"]
)

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales ($)")

plt.tight_layout()

plt.savefig(
    "visualizations/sales_by_customer_segment.png",
    dpi=300
)

plt.close()

# ==========================================
# EXPORT CLEANED DATA FOR SQL
# ==========================================

df.to_csv(
    "data/cleaned_superstore.csv",
    index=False
)

print("\nCleaned dataset exported successfully!")