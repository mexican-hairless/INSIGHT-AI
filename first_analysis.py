import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Quantity_Sold": [15, 40, 25, 8],
    "Stock": [20, 50, 10, 15]
}

df = pd.DataFrame(data)

print(df)

print("\nTotal quantity sold:")
print(df["Quantity_Sold"].sum())

print("\nAverage quantity sold:")
print(df["Quantity_Sold"].mean())
print("\n Maximum quantity sold by product")
print(df["Quantity_Sold"].max())
print("\n Minimum quantity sold by product")
print(df["Quantity_Sold"].min())
low_stock = df[df["Stock"] > 20]
print("\n greater than 20:")
print(low_stock)