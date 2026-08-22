# ==========================================================
# CUSTOMER SEGMENTATION PREPROCESSING
# ==========================================================

import os
import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder

print("=" * 60)
print("Loading Customer Dataset...")
print("=" * 60)

df = pd.read_csv(
    "data/raw/customer_segmentation/marketing_campaign.csv",
    sep="\t"
)

print("\nOriginal Shape :", df.shape)

# ----------------------------------------------------------
# Remove ID
# ----------------------------------------------------------

df.drop("ID", axis=1, inplace=True)

# ----------------------------------------------------------
# Missing Values
# ----------------------------------------------------------

df["Income"] = df["Income"].fillna(df["Income"].median())

# ----------------------------------------------------------
# Convert Date
# ----------------------------------------------------------

df["Dt_Customer"] = pd.to_datetime(
    df["Dt_Customer"],
    dayfirst=True
)

df["Customer_Year"] = df["Dt_Customer"].dt.year
df["Customer_Month"] = df["Dt_Customer"].dt.month

df.drop("Dt_Customer", axis=1, inplace=True)

# ----------------------------------------------------------
# Encode Categorical Columns
# ----------------------------------------------------------

label_encoders = {}

categorical_columns = [
    "Education",
    "Marital_Status"
]

for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(df[column])

    label_encoders[column] = encoder

# ----------------------------------------------------------
# Save Encoder
# ----------------------------------------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(
    label_encoders,
    "models/customer_label_encoders.pkl"
)

# ----------------------------------------------------------
# Save Processed Dataset
# ----------------------------------------------------------

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/customer_processed.csv",
    index=False
)

print("\nProcessed Shape :", df.shape)

print("\nFirst Five Rows")

print(df.head())

print("\nCustomer Dataset Saved Successfully!")