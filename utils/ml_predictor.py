# ==========================================================
# ML PREDICTION FUNCTIONS
# ==========================================================

import numpy as np


def predict_claim(model, scaler, values):
    values = np.array(values).reshape(1, -1)
    values = scaler.transform(values)
    prediction = model.predict(values)
    return float(prediction[0])


def predict_risk(model, values):
    values = np.array(values).reshape(1, -1)
    prediction = model.predict(values)
    return prediction[0]


def predict_fraud(model, scaler, values):
    values = np.array(values).reshape(1, -1)
    values = scaler.transform(values)
    prediction = model.predict(values)
    return prediction[0]


def predict_customer(model, scaler, values):
    values = np.array(values).reshape(1, -1)
    values = scaler.transform(values)
    prediction = model.predict(values)
    return prediction[0]