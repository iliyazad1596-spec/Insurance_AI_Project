import streamlit as st
import joblib

from utils.model_loader import load_fraud_model
from utils.ml_predictor import predict_fraud


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Fraud Detection",
    page_icon="🚨",
    layout="wide"
)


# ============================================================
# PAGE TITLE
# ============================================================

st.title("🚨 Insurance Fraud Detection")

st.markdown(
    """
    This module uses a trained Machine Learning model to
    identify potentially fraudulent insurance claims.
    """
)

st.markdown("---")


# ============================================================
# POLICY INFORMATION
# ============================================================

st.subheader("📋 Policy Information")

col1, col2, col3 = st.columns(3)

with col1:

    policy_state = st.selectbox(
        "Policy State",
        [
            "CA",
            "FL",
            "GA",
            "IL",
            "IN",
            "MI",
            "NY",
            "OH",
            "PA",
            "TX"
        ]
    )

with col2:

    policy_deductible = st.number_input(
        "Policy Deductible",
        min_value=0,
        max_value=5000,
        value=500,
        step=100
    )

with col3:

    policy_annual_premium = st.number_input(
        "Annual Premium",
        min_value=0.0,
        max_value=10000.0,
        value=1200.0,
        step=10.0
    )


# ============================================================
# INSURED INFORMATION
# ============================================================

st.markdown("---")

st.subheader("👤 Insured Information")

col1, col2, col3 = st.columns(3)

with col1:

    insured_age = st.number_input(
        "Insured Age",
        min_value=18,
        max_value=100,
        value=35
    )

with col2:

    insured_sex = st.selectbox(
        "Insured Sex",
        [
            "FEMALE",
            "MALE"
        ]
    )

with col3:

    insured_education_level = st.selectbox(
        "Education Level",
        [
            "Associate",
            "Bachelor",
            "College",
            "High School",
            "JD",
            "Masters",
            "PhD"
        ]
    )


col1, col2 = st.columns(2)

with col1:

    insured_occupation = st.selectbox(
        "Occupation",
        [
            "adm-clerical",
            "armed-forces",
            "craft-repair",
            "exec-managerial",
            "farming-fishing",
            "handlers-cleaners",
            "machine-op-inspct",
            "other-service",
            "priv-house-serv",
            "prof-specialty",
            "protective-serv",
            "sales",
            "tech-support",
            "transport-moving"
        ]
    )

with col2:

    insured_hobbies = st.selectbox(
        "Hobby",
        [
            "base-jumping",
            "basketball",
            "board-games",
            "camping",
            "chess",
            "cross-fit",
            "dancing",
            "exercise",
            "golf",
            "hiking",
            "horseback-riding",
            "kayaking",
            "movies",
            "other",
            "paintball",
            "polo",
            "reading",
            "skydiving",
            "video-games",
            "yachting"
        ]
    )


# ============================================================
# INCIDENT INFORMATION
# ============================================================

st.markdown("---")

st.subheader("🚗 Incident Information")

col1, col2, col3 = st.columns(3)

with col1:

    incident_type = st.selectbox(
        "Incident Type",
        [
            "Multi-vehicle Collision",
            "Other",
            "Parked Car",
            "Single Vehicle",
            "Single Vehicle Collision",
            "Theft",
            "Vehicle Theft"
        ]
    )

with col2:

    collision_type = st.selectbox(
        "Collision Type",
        [
            "Front Collision",
            "No Collision",
            "Rear Collision",
            "Side Collision"
        ]
    )

with col3:

    incident_severity = st.selectbox(
        "Incident Severity",
        [
            "Major Damage",
            "Minor Damage",
            "Total Loss",
            "Trivial Damage"
        ]
    )


col1, col2, col3 = st.columns(3)

with col1:

    authorities_contacted = st.selectbox(
        "Authorities Contacted",
        [
            "Ambulance",
            "Fire",
            "None",
            "Other",
            "Police"
        ]
    )

with col2:

    incident_state = st.selectbox(
        "Incident State",
        [
            "CA",
            "IN",
            "MI",
            "NY",
            "OH",
            "Other",
            "PA"
        ]
    )

with col3:

    incident_city = st.selectbox(
        "Incident City",
        [
            "Arlington",
            "Columbus",
            "Northbend",
            "Other",
            "Riverwood",
            "Springfield"
        ]
    )


# ============================================================
# INCIDENT DETAILS
# ============================================================

st.markdown("---")

st.subheader("📍 Incident Details")

col1, col2, col3, col4 = st.columns(4)

with col1:

    incident_hour = st.number_input(
        "Incident Hour",
        min_value=0,
        max_value=23,
        value=12
    )

with col2:

    number_of_vehicles = st.number_input(
        "Vehicles Involved",
        min_value=1,
        max_value=20,
        value=2
    )

with col3:

    bodily_injuries = st.number_input(
        "Bodily Injuries",
        min_value=0,
        max_value=10,
        value=0
    )

with col4:

    witnesses = st.number_input(
        "Witnesses",
        min_value=0,
        max_value=10,
        value=1
    )


# ============================================================
# CLAIM INFORMATION
# ============================================================

st.markdown("---")

st.subheader("💰 Claim Information")

col1, col2, col3 = st.columns(3)

with col1:

    police_report_available = st.selectbox(
        "Police Report Available",
        [
            "NO",
            "YES"
        ]
    )

with col2:

    claim_amount = st.number_input(
        "Claim Amount",
        min_value=0.0,
        max_value=1000000.0,
        value=10000.0,
        step=100.0
    )

with col3:

    total_claim_amount = st.number_input(
        "Total Claim Amount",
        min_value=0.0,
        max_value=1000000.0,
        value=12000.0,
        step=100.0
    )


# ============================================================
# INCIDENT DATE
# ============================================================

st.markdown("---")

st.subheader("📅 Incident Date")

col1, col2, col3 = st.columns(3)

with col1:

    incident_year = st.number_input(
        "Incident Year",
        min_value=2000,
        max_value=2030,
        value=2025
    )

with col2:

    incident_month = st.number_input(
        "Incident Month",
        min_value=1,
        max_value=12,
        value=6
    )

with col3:

    incident_day = st.number_input(
        "Incident Day",
        min_value=1,
        max_value=31,
        value=15
    )


# ============================================================
# CATEGORY ENCODING
# ============================================================

def encode_value(value, values):
    """
    Convert categorical values to numerical values.
    """

    if value in values:
        return values.index(value)

    return 0


# ============================================================
# ENCODING LISTS
# ============================================================

policy_state_values = [
    "CA",
    "FL",
    "GA",
    "IL",
    "IN",
    "MI",
    "NY",
    "OH",
    "PA",
    "TX"
]


sex_values = [
    "FEMALE",
    "MALE"
]


education_values = [
    "Associate",
    "Bachelor",
    "College",
    "High School",
    "JD",
    "Masters",
    "PhD"
]


occupation_values = [
    "adm-clerical",
    "armed-forces",
    "craft-repair",
    "exec-managerial",
    "farming-fishing",
    "handlers-cleaners",
    "machine-op-inspct",
    "other-service",
    "priv-house-serv",
    "prof-specialty",
    "protective-serv",
    "sales",
    "tech-support",
    "transport-moving"
]


hobby_values = [
    "base-jumping",
    "basketball",
    "board-games",
    "camping",
    "chess",
    "cross-fit",
    "dancing",
    "exercise",
    "golf",
    "hiking",
    "horseback-riding",
    "kayaking",
    "movies",
    "other",
    "paintball",
    "polo",
    "reading",
    "skydiving",
    "video-games",
    "yachting"
]


incident_type_values = [
    "Multi-vehicle Collision",
    "Other",
    "Parked Car",
    "Single Vehicle",
    "Single Vehicle Collision",
    "Theft",
    "Vehicle Theft"
]


collision_type_values = [
    "Front Collision",
    "No Collision",
    "Rear Collision",
    "Side Collision"
]


incident_severity_values = [
    "Major Damage",
    "Minor Damage",
    "Total Loss",
    "Trivial Damage"
]


authorities_values = [
    "Ambulance",
    "Fire",
    "None",
    "Other",
    "Police"
]


incident_state_values = [
    "CA",
    "IN",
    "MI",
    "NY",
    "OH",
    "Other",
    "PA"
]


incident_city_values = [
    "Arlington",
    "Columbus",
    "Northbend",
    "Other",
    "Riverwood",
    "Springfield"
]


police_report_values = [
    "NO",
    "YES"
]


# ============================================================
# PREDICTION
# ============================================================

st.markdown("---")

if st.button(
    "🔍 Detect Fraud",
    use_container_width=True
):

    try:

        # ====================================================
        # LOAD MODEL
        # ====================================================

        model = load_fraud_model()


        # ====================================================
        # LOAD SCALER
        # ====================================================

        scaler = joblib.load(
            "models/fraud_scaler.pkl"
        )


        # ====================================================
        # ENCODE CATEGORICAL FEATURES
        # ====================================================

        encoded_policy_state = encode_value(
            policy_state,
            policy_state_values
        )

        encoded_sex = encode_value(
            insured_sex,
            sex_values
        )

        encoded_education = encode_value(
            insured_education_level,
            education_values
        )

        encoded_occupation = encode_value(
            insured_occupation,
            occupation_values
        )

        encoded_hobby = encode_value(
            insured_hobbies,
            hobby_values
        )

        encoded_incident_type = encode_value(
            incident_type,
            incident_type_values
        )

        encoded_collision_type = encode_value(
            collision_type,
            collision_type_values
        )

        encoded_incident_severity = encode_value(
            incident_severity,
            incident_severity_values
        )

        encoded_authorities = encode_value(
            authorities_contacted,
            authorities_values
        )

        encoded_incident_state = encode_value(
            incident_state,
            incident_state_values
        )

        encoded_incident_city = encode_value(
            incident_city,
            incident_city_values
        )

        encoded_police_report = encode_value(
            police_report_available,
            police_report_values
        )


        # ====================================================
        # CREATE MODEL INPUT
        # ====================================================
        #
        # EXACTLY 24 FEATURES
        #
        # fraud_reported is the target and is NOT included.
        #
        # ====================================================

        input_data = [

            encoded_policy_state,

            policy_deductible,

            policy_annual_premium,

            insured_age,

            encoded_sex,

            encoded_education,

            encoded_occupation,

            encoded_hobby,

            encoded_incident_type,

            encoded_collision_type,

            encoded_incident_severity,

            encoded_authorities,

            encoded_incident_state,

            encoded_incident_city,

            incident_hour,

            number_of_vehicles,

            bodily_injuries,

            witnesses,

            encoded_police_report,

            claim_amount,

            total_claim_amount,

            incident_year,

            incident_month,

            incident_day
        ]


        # ====================================================
        # SAFETY CHECK
        # ====================================================

        if len(input_data) != 24:

            raise ValueError(
                f"Expected 24 input features, "
                f"but received {len(input_data)}."
            )


        # ====================================================
        # MAKE PREDICTION
        # ====================================================

        prediction = predict_fraud(
            model,
            scaler,
            input_data
        )


        # ====================================================
        # FRAUD PROBABILITY
        # ====================================================

        fraud_probability = None

        if hasattr(model, "predict_proba"):

            scaled_input = scaler.transform(
                [input_data]
            )

            probabilities = model.predict_proba(
                scaled_input
            )[0]

            if len(probabilities) > 1:

                fraud_probability = (
                    float(probabilities[1]) * 100
                )


        # ====================================================
        # DISPLAY RESULT
        # ====================================================

        st.markdown("---")

        st.subheader("🚨 Fraud Detection Result")


        # Convert prediction safely
        prediction_value = int(prediction)


        if prediction_value == 1:

            st.error(
                "🚨 POTENTIAL FRAUD DETECTED"
            )

            st.warning(
                """
                The Machine Learning model has classified
                this insurance claim as potentially fraudulent.

                Further investigation is recommended before
                processing the claim.
                """
            )

        else:

            st.success(
                "✅ NO FRAUD DETECTED"
            )

            st.info(
                """
                The Machine Learning model has classified
                this insurance claim as non-fraudulent.
                """
            )


        # ====================================================
        # FRAUD PROBABILITY
        # ====================================================

        if fraud_probability is not None:

            st.markdown("---")

            st.subheader("📊 Fraud Probability")

            probability_col1, probability_col2 = st.columns(2)

            with probability_col1:

                st.metric(
                    "Fraud Probability",
                    f"{fraud_probability:.2f}%"
                )

            with probability_col2:

                non_fraud_probability = (
                    100 - fraud_probability
                )

                st.metric(
                    "Non-Fraud Probability",
                    f"{non_fraud_probability:.2f}%"
                )


        # ====================================================
        # CLAIM SUMMARY
        # ====================================================

        st.markdown("---")

        st.subheader("📋 Claim Summary")

        summary_col1, summary_col2, summary_col3 = st.columns(3)

        with summary_col1:

            st.metric(
                "Claim Amount",
                f"${claim_amount:,.2f}"
            )

        with summary_col2:

            st.metric(
                "Total Claim",
                f"${total_claim_amount:,.2f}"
            )

        with summary_col3:

            st.metric(
                "Vehicles Involved",
                number_of_vehicles
            )


        # ====================================================
        # INCIDENT SUMMARY
        # ====================================================

        st.markdown("---")

        st.subheader("🚗 Incident Summary")

        summary_col1, summary_col2, summary_col3 = st.columns(3)

        with summary_col1:

            st.write(
                f"**Incident Type:** {incident_type}"
            )

            st.write(
                f"**Collision Type:** {collision_type}"
            )

        with summary_col2:

            st.write(
                f"**Severity:** {incident_severity}"
            )

            st.write(
                f"**Incident State:** {incident_state}"
            )

        with summary_col3:

            st.write(
                f"**Bodily Injuries:** {bodily_injuries}"
            )

            st.write(
                f"**Witnesses:** {witnesses}"
            )


    # ========================================================
    # ERROR HANDLING
    # ========================================================

    except Exception as e:

        st.error(
            "Unable to perform fraud detection."
        )

        st.exception(e)