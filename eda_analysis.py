import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("Dataset for Data Analytics.xlsx")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nBasic Statistics:\n")

print(df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].describe())

print("\nMedian Values:\n")

print(df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].median())

print("\nMost Sold Products:\n")
print(df["Product"].value_counts())

print("\nPayment Methods:\n")
print(df["PaymentMethod"].value_counts())

print("\nOrder Status:\n")
print(df["OrderStatus"].value_counts())

print("\nReferral Sources:\n")
print(df["ReferralSource"].value_counts())

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["TotalPrice"] < lower_bound) |
    (df["TotalPrice"] > upper_bound)
]

print("\nNumber of Outliers:")
print(len(outliers))

# Product Sales Chart

plt.figure(figsize=(10,6))

df["Product"].value_counts().plot(kind="bar")

plt.title("Product Sales Distribution")
plt.xlabel("Product")
plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig("Product_Sales_Distribution.png", dpi=300)

plt.show()
plt.show()

# Correlation Analysis

print("\nCorrelation Matrix:\n")

correlation = df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].corr()

print(correlation)

# Correlation Graph

plt.figure(figsize=(8,6))

plt.imshow(correlation, cmap="coolwarm")

plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig("Correlation_Matrix.png", dpi=300)

plt.show()