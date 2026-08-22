# ==========================================================
# INSURANCE RISK CLASSIFICATION
# ==========================================================

import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

# ==========================================================
# LOAD DATASET
# ==========================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv("data/processed/insurance_encoded.csv")

# ==========================================================
# CREATE RISK LEVEL
# ==========================================================

df["risk_level"] = pd.qcut(
    df["charges"],
    q=3,
    labels=["Low", "Medium", "High"]
)

print("\nRisk Level Distribution\n")
print(df["risk_level"].value_counts())

# ==========================================================
# FEATURES & TARGET
# ==========================================================

X = df.drop(["charges", "risk_level"], axis=1)
y = df["risk_level"]

# ==========================================================
# TRAIN TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================================================
# MODELS
# ==========================================================

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "Decision Tree":
        DecisionTreeClassifier(random_state=42),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=200,
            random_state=42
        )
}

# ==========================================================
# TRAIN & EVALUATE
# ==========================================================

best_model = None
best_accuracy = 0

print("\n")
print("=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

for name, model in models.items():

    print("\n" + "=" * 40)
    print(name)
    print("=" * 40)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    precision = precision_score(
        y_test,
        predictions,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\nClassification Report")
    print(classification_report(y_test, predictions))

    print("Confusion Matrix")
    print(confusion_matrix(y_test, predictions))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# ==========================================================
# SAVE MODEL
# ==========================================================

os.makedirs("models", exist_ok=True)

joblib.dump(
    best_model,
    "models/risk_classification_model.pkl"
)

print("\n")
print("=" * 60)
print("BEST MODEL SAVED")
print("=" * 60)

print("Location : models/risk_classification_model.pkl")