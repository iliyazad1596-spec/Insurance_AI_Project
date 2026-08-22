import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# -------------------------
# Load cleaned dataset
# -------------------------
df = pd.read_csv("data/processed/insurance_clean.csv")

print("Original Shape:", df.shape)

# -------------------------
# Encode categorical columns
# -------------------------
label_encoders = {}

categorical_columns = ["sex", "smoker", "region"]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

    label_encoders[col] = le

# -------------------------
# Save encoders
# -------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(label_encoders, "models/label_encoders.pkl")

# -------------------------
# Save processed dataset
# -------------------------
df.to_csv(
    "data/processed/insurance_encoded.csv",
    index=False
)

print("\nEncoded Dataset")
print(df.head())

print("\nDataset saved successfully!")