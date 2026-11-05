import pandas as pd

df = pd.read_csv("data/raw/inventory.csv")

print(df)
print("-------------------------------------------------------------------------")
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print("-------------------------")
print(df.describe())
df["Inventory_Value"] = df["Stock"] * df["Unit_Price"]

print(df)
df["Revenue"] = df["Quantity_Sold"] * df["Unit_Price"]

print(df.loc[df["Revenue"].idxmax()])