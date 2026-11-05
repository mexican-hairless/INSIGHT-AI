import pandas as pd

df = pd.read_csv("data/raw/daily_sales.csv")

print(df.head())
print(df.dtypes)
df["Date"] = pd.to_datetime(df["Date"])
print(df.dtypes)
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Month_Name"] = df["Date"].dt.month_name()
df["Day"] = df["Date"].dt.day
print(df.head())
df["Revenue"] = df["Quantity_Sold"] * df["Unit_Price"]
#monthly_sales = df.groupby("Month_Name")["Revenue"].sum() this is another method which iis not feasable
monthly_sales = df.groupby(
    df["Date"].dt.to_period("M")
)["Revenue"].sum()
print(monthly_sales)
#best day of the sales 
best_day_index = df["Revenue"].idxmax()

best_day = df.loc[best_day_index]

print(best_day)