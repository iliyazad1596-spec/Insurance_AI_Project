# ==========================================================
# MODEL LOADER
# ==========================================================

import joblib


def load_claim_model():
    return joblib.load("models/claim_prediction_model.pkl")


def load_claim_scaler():
    return joblib.load("models/scaler.pkl")


def load_risk_model():
    return joblib.load("models/risk_classification_model.pkl")


def load_fraud_model():
    return joblib.load("models/fraud_detection_model.pkl")


def load_fraud_scaler():
    return joblib.load("models/fraud_scaler.pkl")


def load_customer_model():
    return joblib.load("models/customer_segmentation_model.pkl")


def load_customer_scaler():
    return joblib.load("models/customer_scaler.pkl")


def load_sentiment_model():
    return joblib.load("models/sentiment_model.pkl")


def load_vectorizer():
    return joblib.load("models/tfidf_vectorizer.pkl")