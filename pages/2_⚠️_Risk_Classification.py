import streamlit as st

from utils.model_loader import load_risk_model
from utils.ml_predictor import predict_risk


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Risk Classification",
    page_icon="⚠️",
    layout="wide"
)


# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("⚠️ Insurance Risk Classification")

st.markdown(
    """
    This module predicts the insurance risk level of a customer
    using the trained Machine Learning model.
    """
)

st.markdown("---")


# ==========================================================
# INPUT SECTION
# ==========================================================

st.subheader("Enter Customer Details")

col1, col2 = st.columns(2)


with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35
    )

    sex = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=30.0,
        step=0.1
    )


with col2:

    children = st.number_input(
        "Number of Children",
        min_value=0,
        max_value=10,
        value=1
    )

    smoker = st.selectbox(
        "Smoker",
        ["No", "Yes"]
    )

    region = st.selectbox(
        "Region",
        [
            "Northeast",
            "Northwest",
            "Southeast",
            "Southwest"
        ]
    )


# ==========================================================
# ENCODING
# ==========================================================

sex_encoded = 1 if sex == "Male" else 0

smoker_encoded = 1 if smoker == "Yes" else 0

region_mapping = {
    "Northeast": 0,
    "Northwest": 1,
    "Southeast": 2,
    "Southwest": 3
}

region_encoded = region_mapping[region]


# ==========================================================
# PREDICTION
# ==========================================================

st.markdown("---")

if st.button(
    "🔍 Predict Risk Level",
    use_container_width=True
):

    try:

        # Load trained model
        model = load_risk_model()

        # Prepare input
        input_values = [
            age,
            sex_encoded,
            bmi,
            children,
            smoker_encoded,
            region_encoded
        ]

        # Make prediction
        prediction = predict_risk(
            model,
            input_values
        )

        # Convert prediction to readable label
        if isinstance(prediction, str):

            risk_level = prediction

        else:

            risk_mapping = {
                0: "High",
                1: "Low",
                2: "Medium"
            }

            risk_level = risk_mapping.get(
                int(prediction),
                str(prediction)
            )


        # ==================================================
        # DISPLAY RESULT
        # ==================================================

        st.subheader("Prediction Result")

        if risk_level.lower() == "high":

            st.error(
                f"⚠️ High Risk\n\n"
                f"The predicted insurance risk level is **{risk_level}**."
            )

        elif risk_level.lower() == "medium":

            st.warning(
                f"⚠️ Medium Risk\n\n"
                f"The predicted insurance risk level is **{risk_level}**."
            )

        else:

            st.success(
                f"✅ Low Risk\n\n"
                f"The predicted insurance risk level is **{risk_level}**."
            )


        # ==================================================
        # INPUT SUMMARY
        # ==================================================

        st.markdown("---")

        st.subheader("Customer Information")

        result_col1, result_col2, result_col3 = st.columns(3)

        with result_col1:

            st.metric(
                "Age",
                age
            )

            st.metric(
                "BMI",
                f"{bmi:.1f}"
            )


        with result_col2:

            st.metric(
                "Children",
                children
            )

            st.metric(
                "Smoker",
                smoker
            )


        with result_col3:

            st.metric(
                "Gender",
                sex
            )

            st.metric(
                "Region",
                region
            )


    except Exception as e:

        st.error(
            "Unable to make the prediction."
        )

        st.exception(e)