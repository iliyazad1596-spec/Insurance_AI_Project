# ==========================================================
# SENTIMENT ANALYSIS MODEL TRAINING
# ==========================================================

import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
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
# LOAD DATA
# ==========================================================

print("="*70)
print("Loading Reviews Dataset...")
print("="*70)

df = pd.read_csv(
    "data/processed/reviews_processed.csv"
)

print(df.head())

# ==========================================================
# FEATURES
# ==========================================================

X = df["ReviewText"]

y = df["Sentiment"]

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
# TF-IDF
# ==========================================================

vectorizer = TfidfVectorizer(

    max_features=5000,

    stop_words="english"

)

X_train = vectorizer.fit_transform(X_train)

X_test = vectorizer.transform(X_test)

os.makedirs("models", exist_ok=True)

joblib.dump(

    vectorizer,

    "models/tfidf_vectorizer.pkl"

)

# ==========================================================
# MODELS
# ==========================================================

models = {

    "Logistic Regression":

        LogisticRegression(max_iter=2000),

    "Naive Bayes":

        MultinomialNB(),

    "Random Forest":

        RandomForestClassifier(

            n_estimators=200,

            random_state=42

        )

}

# ==========================================================
# TRAIN
# ==========================================================

results = []

best_model = None
best_accuracy = 0
best_predictions = None
best_name = ""

print("\n")
print("="*70)
print("MODEL PERFORMANCE")
print("="*70)

for name, model in models.items():

    print("\n"+"="*50)
    print(name)
    print("="*50)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

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
        best_name = name

# ==========================================================
# SAVE MODEL
# ==========================================================

joblib.dump(

    best_model,

    "models/sentiment_model.pkl"

)

# ==========================================================
# SAVE REPORT
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

    "reports/sentiment_results.csv",

    index=False

)

# ==========================================================
# CONFUSION MATRIX
# ==========================================================

cm = confusion_matrix(
    y_test,
    best_predictions
)

plt.figure(figsize=(6,5))

plt.imshow(cm, cmap="Blues")

plt.title("Sentiment Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.colorbar()

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(
            j,
            i,
            cm[i,j],
            ha="center",
            va="center"
        )

plt.tight_layout()

plt.savefig(
    "reports/sentiment_confusion_matrix.png"
)

plt.close()

# ==========================================================
# FINISHED
# ==========================================================

print("\n")
print("="*70)
print("BEST MODEL :", best_name)
print("Accuracy   :", round(best_accuracy,4))
print("="*70)

print("\nFiles Saved")

print("models/sentiment_model.pkl")
print("models/tfidf_vectorizer.pkl")
print("reports/sentiment_results.csv")
print("reports/sentiment_confusion_matrix.png")