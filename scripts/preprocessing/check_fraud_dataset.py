import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/insurance_fraud/car_insurance_fraud_dataset.csv")

print("=" * 60)
print("First 5 Rows")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("Dataset Information")
print("=" * 60)
print(df.info())

print("\n" + "=" * 60)
print("Column Names")
print("=" * 60)

for col in df.columns:
    print(col)

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)

print(df.isnull().sum())

print("\nShape :", df.shape)