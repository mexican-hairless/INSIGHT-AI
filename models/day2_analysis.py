import pandas as pd

df = pd.read_csv("data/raw/inventory.csv")

# Calculate revenue
df["Revenue"] = df["Quantity_Sold"] * df["Unit_Price"]

# Calculate inventory value
df["Inventory_Value"] = df["Stock"] * df["Unit_Price"]

# Category-wise analysis
category_analysis = df.groupby("Category").agg({
    "Quantity_Sold": "sum",
    "Revenue": "sum",
    "Stock": "sum",
    "Inventory_Value": "sum"
})

print("CATEGORY ANALYSIS")
print(category_analysis)

# Top selling products
top_products = df.sort_values(
    by="Quantity_Sold",
    ascending=False
)

print("\nTOP SELLING PRODUCTS")
print(top_products[["Product", "Quantity_Sold"]])