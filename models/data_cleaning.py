import pandas as pd
import numpy as np

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse", "Headphones"],
    "Quantity_Sold": [15, 40, np.nan, 8, 40, 30],
    "Stock": [20, 50, 10, 15, 50, -5],
    "Unit_Price": [50000, 500, 1200, 12000, 500, 2000]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nInvalid Stock:")
print(df[df["Stock"] < 0])