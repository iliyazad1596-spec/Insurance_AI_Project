import pandas as pd

df = pd.read_csv("data/raw/customer_reviews/insurance_customer_reviews_gemini_enhanced.csv")

print(df.head())
print("\nShape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nMissing Values:")
print(df.isnull().sum())