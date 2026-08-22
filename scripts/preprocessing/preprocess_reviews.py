# ==========================================================
# CUSTOMER REVIEW PREPROCESSING
# ==========================================================

import os
import re
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

print("=" * 60)
print("Loading Customer Reviews Dataset...")
print("=" * 60)

df = pd.read_csv(
    "data/raw/customer_reviews/insurance_customer_reviews_gemini_enhanced.csv"
)

print("\nOriginal Shape:", df.shape)

# ----------------------------------------------------------
# Keep Required Columns
# ----------------------------------------------------------

df = df[["ReviewText", "Rating", "Sentiment"]]

# ----------------------------------------------------------
# Clean Text
# ----------------------------------------------------------
def clean_text(text):
    text = str(text).lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Keep only letters and spaces
    text = re.sub(r"[^a-zA-Z ]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

df["ReviewText"] = df["ReviewText"].apply(clean_text)

# ----------------------------------------------------------
# Encode Target
# ----------------------------------------------------------

encoder = LabelEncoder()

df["Sentiment"] = encoder.fit_transform(df["Sentiment"])

os.makedirs("models", exist_ok=True)

joblib.dump(
    encoder,
    "models/sentiment_label_encoder.pkl"
)

# ----------------------------------------------------------
# Save Dataset
# ----------------------------------------------------------

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/reviews_processed.csv",
    index=False
)

print("\nProcessed Shape:", df.shape)

print("\nSentiment Distribution")

print(df["Sentiment"].value_counts())

print("\nFirst Five Rows")

print(df.head())

print("\nReviews Dataset Saved Successfully!")