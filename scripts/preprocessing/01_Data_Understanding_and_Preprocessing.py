import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/insurance_risk/insurance.csv")

print("=" * 60)
print("Before Cleaning")
print("=" * 60)
print("Shape :", df.shape)
print("Duplicate Rows :", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

print("\n" + "=" * 60)
print("After Removing Duplicates")
print("=" * 60)
print("Shape :", df.shape)
print("Duplicate Rows :", df.duplicated().sum())

# Check missing values
print("\nMissing Values")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("data/processed/insurance_clean.csv", index=False)

print("\nClean dataset saved successfully!")