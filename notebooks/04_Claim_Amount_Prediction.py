# ==========================================================
# INSURANCE CLAIM AMOUNT PREDICTION
# ==========================================================

import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==========================================================
# LOAD DATASET
# ==========================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv("data/processed/insurance_encoded.csv")

print(df.head())

# ==========================================================
# FEATURES & TARGET
# ==========================================================

X = df.drop("charges", axis=1)
y = df["charges"]

print("\nFeatures Shape :", X.shape)
print("Target Shape   :", y.shape)

# ==========================================================
# TRAIN TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ==========================================================
# FEATURE SCALING
# ==========================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

os.makedirs("models", exist_ok=True)

joblib.dump(scaler, "models/scaler.pkl")

print("\nScaler Saved Successfully!")

# ==========================================================
# MODELS
# ==========================================================

models = {

    "Linear Regression":
        LinearRegression(),

    "Decision Tree":
        DecisionTreeRegressor(
            random_state=42
        ),

    "Random Forest":
        RandomForestRegressor(
            n_estimators=200,
            random_state=42
        )

}

# ==========================================================
# TRAIN & EVALUATE
# ==========================================================

best_model = None
best_score = -999

print("\n")
print("=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

for name, model in models.items():

    print("\n", "=" * 40)
    print(name)
    print("=" * 40)

    # Train
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_test)

    # Metrics

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    mse = mean_squared_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(mse)

    r2 = r2_score(
        y_test,
        predictions
    )

    print(f"MAE  : {mae:.2f}")
    print(f"MSE  : {mse:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"R²   : {r2:.4f}")

    # Save Best Model

    if r2 > best_score:

        best_score = r2
        best_model = model

# ==========================================================
# SAVE MODEL
# ==========================================================

joblib.dump(
    best_model,
    "models/claim_prediction_model.pkl"
)

print("\n")
print("=" * 60)
print("BEST MODEL SAVED SUCCESSFULLY")
print("=" * 60)

print("\nLocation:")
print("models/claim_prediction_model.pkl")

print("\nScaler Saved:")
print("models/scaler.pkl")

print("\nProject Completed Successfully!")