# ==========================================================
# INSURANCE FRAUD DETECTION
# Professional Version (SMOTE + Scaling + Reports)
# ==========================================================

import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from imblearn.over_sampling import SMOTE

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    auc
)

# ==========================================================
# LOAD DATASET
# ==========================================================

print("=" * 70)
print("Loading Fraud Dataset...")
print("=" * 70)

df = pd.read_csv("data/processed/fraud_processed.csv")

print(df.head())

# ==========================================================
# FEATURES & TARGET
# ==========================================================

X = df.drop("fraud_reported", axis=1)
y = df["fraud_reported"]

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
# FEATURE SCALING
# ==========================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

os.makedirs("models", exist_ok=True)

joblib.dump(
    scaler,
    "models/fraud_scaler.pkl"
)

# ==========================================================
# SMOTE
# ==========================================================

print("\nApplying SMOTE...")

smote = SMOTE(random_state=42)

X_train, y_train = smote.fit_resample(
    X_train,
    y_train
)

print("\nBalanced Dataset")

print(pd.Series(y_train).value_counts())

# ==========================================================
# MODELS
# ==========================================================

models = {

    "Logistic Regression":

        LogisticRegression(
            max_iter=3000,
            class_weight="balanced"
        ),

    "Decision Tree":

        DecisionTreeClassifier(
            random_state=42,
            class_weight="balanced"
        ),

    "Random Forest":

        RandomForestClassifier(
            n_estimators=300,
            random_state=42,
            class_weight="balanced"
        )

}

# ==========================================================
# TRAIN MODELS
# ==========================================================

results = []

best_model = None
best_accuracy = 0

best_predictions = None
best_probabilities = None
best_name = ""

print("\n")
print("=" * 70)
print("MODEL PERFORMANCE")
print("=" * 70)

for name, model in models.items():

    print("\n")
    print("=" * 50)
    print(name)
    print("=" * 50)

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted",
        zero_division=0
    )

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\nClassification Report\n")

    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    results.append([

        name,
        accuracy,
        precision,
        recall,
        f1

    ])

    if accuracy > best_accuracy:

        best_accuracy = accuracy

        best_model = model

        best_predictions = predictions

        best_probabilities = probabilities

        best_name = name

# ==========================================================
# SAVE MODEL
# ==========================================================

joblib.dump(

    best_model,

    "models/fraud_detection_model.pkl"

)

# ==========================================================
# SAVE RESULTS
# ==========================================================

os.makedirs("reports", exist_ok=True)

results_df = pd.DataFrame(

    results,

    columns=[

        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"

    ]

)

results_df.to_csv(

    "reports/fraud_model_results.csv",

    index=False

)

# ==========================================================
# CONFUSION MATRIX
# ==========================================================

cm = confusion_matrix(

    y_test,

    best_predictions

)

plt.figure(figsize=(6, 5))

plt.imshow(cm, cmap="Blues")

plt.title("Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.colorbar()

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(
            j,
            i,
            cm[i, j],
            ha="center",
            va="center"
        )

plt.tight_layout()

plt.savefig(

    "reports/confusion_matrix.png"

)

plt.close()

# ==========================================================
# ROC CURVE
# ==========================================================

fpr, tpr, _ = roc_curve(
    y_test,
    best_probabilities
)

roc_auc = auc(
    fpr,
    tpr
)

plt.figure(figsize=(6,5))

plt.plot(
    fpr,
    tpr,
    label=f"AUC = {roc_auc:.3f}"
)

plt.plot(
    [0,1],
    [0,1],
    "--"
)

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.legend()

plt.tight_layout()

plt.savefig(
    "reports/roc_curve.png"
)

plt.close()

# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

if hasattr(best_model, "feature_importances_"):

    importance = pd.Series(

        best_model.feature_importances_,

        index=X.columns

    )

    importance = importance.sort_values(
        ascending=False
    )

    plt.figure(figsize=(10,6))

    importance.head(10).sort_values().plot(
        kind="barh"
    )

    plt.title(
        "Top 10 Important Features"
    )

    plt.tight_layout()

    plt.savefig(
        "reports/feature_importance.png"
    )

    plt.close()

# ==========================================================
# FINISHED
# ==========================================================

print("\n")
print("=" * 70)
print("BEST MODEL")
print("=" * 70)

print("Model    :", best_name)

print("Accuracy :", round(best_accuracy,4))

print("\nFiles Saved")

print("✔ models/fraud_detection_model.pkl")

print("✔ models/fraud_scaler.pkl")

print("✔ reports/fraud_model_results.csv")

print("✔ reports/confusion_matrix.png")

print("✔ reports/roc_curve.png")

print("✔ reports/feature_importance.png")