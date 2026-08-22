# ==========================================================
# FRAUD DATA PREPROCESSING
# ==========================================================

import os
import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder

print("=" * 60)
print("Loading Fraud Dataset...")
print("=" * 60)

df = pd.read_csv("data/raw/insurance_fraud/car_insurance_fraud_dataset.csv")

print("\nOriginal Shape :", df.shape)

# ----------------------------------------------------------
# Remove ID column
# ----------------------------------------------------------

df.drop("policy_id", axis=1, inplace=True)

# ----------------------------------------------------------
# Handle Missing Values
# ----------------------------------------------------------

df["authorities_contacted"] = df["authorities_contacted"].fillna("Unknown")

# ----------------------------------------------------------
# Convert Date
# ----------------------------------------------------------

df["incident_date"] = pd.to_datetime(df["incident_date"])

df["incident_year"] = df["incident_date"].dt.year
df["incident_month"] = df["incident_date"].dt.month
df["incident_day"] = df["incident_date"].dt.day

df.drop("incident_date", axis=1, inplace=True)

# ----------------------------------------------------------
# Encode Categorical Columns
# ----------------------------------------------------------

label_encoders = {}

categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:

    le = LabelEncoder()

    df[column] = le.fit_transform(df[column])

    label_encoders[column] = le

# ----------------------------------------------------------
# Save Encoders
# ----------------------------------------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(
    label_encoders,
    "models/fraud_label_encoders.pkl"
)

# ----------------------------------------------------------
# Save Processed Dataset
# ----------------------------------------------------------

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/fraud_processed.csv",
    index=False
)

print("\nProcessed Shape :", df.shape)

print("\nFirst 5 Rows")
print(df.head())

print("\nFraud Dataset Saved Successfully!")