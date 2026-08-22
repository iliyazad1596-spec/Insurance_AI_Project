import pandas as pd

# Change the filename if your CSV has a different name
df = pd.read_csv(
    "data/raw/customer_segmentation/marketing_campaign.csv",
    sep="\t"
)

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

for column in df.columns:
    print(column)

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)

print(df.isnull().sum())

print("\nShape :", df.shape)