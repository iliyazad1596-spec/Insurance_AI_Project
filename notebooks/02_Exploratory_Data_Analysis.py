import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/processed/insurance_clean.csv")

# Create folder for saving graphs
os.makedirs("reports/figures", exist_ok=True)

sns.set_style("whitegrid")

# -----------------------------
# Dataset Overview
# -----------------------------
print("=" * 50)
print("Dataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

# -----------------------------
# Age Distribution
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["age"], bins=20, kde=True)
plt.title("Age Distribution")
plt.savefig("reports/figures/age_distribution.png")
plt.show()

# -----------------------------
# BMI Distribution
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["bmi"], bins=20, kde=True)
plt.title("BMI Distribution")
plt.savefig("reports/figures/bmi_distribution.png")
plt.show()

# -----------------------------
# Smoker Count
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="smoker", data=df)
plt.title("Smoker vs Non-Smoker")
plt.savefig("reports/figures/smoker_count.png")
plt.show()

# -----------------------------
# Region Distribution
# -----------------------------
plt.figure(figsize=(7,5))
sns.countplot(x="region", data=df)
plt.title("Region Distribution")
plt.savefig("reports/figures/region_distribution.png")
plt.show()

# -----------------------------
# Gender Distribution
# -----------------------------
plt.figure(figsize=(6,4))
sns.countplot(x="sex", data=df)
plt.title("Gender Distribution")
plt.savefig("reports/figures/gender_distribution.png")
plt.show()

# -----------------------------
# Charges Distribution
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["charges"], bins=30, kde=True)
plt.title("Insurance Charges Distribution")
plt.savefig("reports/figures/charges_distribution.png")
plt.show()

# -----------------------------
# Correlation Matrix
# -----------------------------
numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("reports/figures/correlation_heatmap.png")
plt.show()

print("\nEDA Completed Successfully!")