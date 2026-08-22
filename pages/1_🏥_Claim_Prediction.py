import streamlit as st

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Powered Insurance Analytics System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

st.sidebar.title("🛡️ Insurance AI")

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "🏥 Claim Prediction",
        "⚠️ Risk Classification",
        "🚨 Fraud Detection",
        "👥 Customer Segmentation",
        "😊 Sentiment Analysis",
        "🌍 Policy Translation",
        "📄 Policy Summarization",
        "🤖 Insurance Assistant",
        "ℹ️ About"
    ]
)

# -------------------------------------------------------
# HOME
# -------------------------------------------------------

if page == "🏠 Home":

    st.title("🛡️ AI Powered Insurance Analytics System")

    st.success("Welcome to the Integrated Insurance Analytics Dashboard")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Machine Learning Modules")

        st.write("✅ Claim Prediction")
        st.write("✅ Risk Classification")
        st.write("✅ Fraud Detection")
        st.write("✅ Customer Segmentation")

    with col2:

        st.subheader("Generative AI Modules")

        st.write("✅ Sentiment Analysis")
        st.write("✅ Policy Translation")
        st.write("✅ Policy Summarization")
        st.write("✅ Insurance Assistant")

    st.markdown("---")

    st.info(
        """
        This application integrates Machine Learning and Generative AI
        to support insurance analytics and customer services.
        """
    )

# -------------------------------------------------------
# PLACEHOLDERS
# -------------------------------------------------------

elif page == "🏥 Claim Prediction":

    from utils.model_loader import (
        load_claim_model,
        load_claim_scaler
    )

    from utils.ml_predictor import predict_claim

    st.title("🏥 Insurance Claim Amount Prediction")

    st.markdown("### Enter Customer Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 30)
        bmi = st.number_input("BMI", 15.0, 55.0, 28.0)

        sex = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

    with col2:
        children = st.number_input(
            "Children",
            0,
            10,
            0
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

    if st.button("Predict Claim Amount"):

        sex = 1 if sex == "Male" else 0
        smoker = 1 if smoker == "Yes" else 0

        region_dict = {
            "Northeast": 0,
            "Northwest": 1,
            "Southeast": 2,
            "Southwest": 3
        }

        region = region_dict[region]

        model = load_claim_model()
        scaler = load_claim_scaler()

        prediction = predict_claim(
            model,
            scaler,
            [
                age,
                sex,
                bmi,
                children,
                smoker,
                region
            ]
        )

        st.success(
            f"Estimated Insurance Claim Amount: ${prediction:,.2f}"
        )

elif page == "⚠️ Risk Classification":
    st.title("⚠️ Risk Classification")
    st.info("Module will be connected next.")

elif page == "🚨 Fraud Detection":
    st.title("🚨 Fraud Detection")
    st.info("Module will be connected next.")

elif page == "👥 Customer Segmentation":
    st.title("👥 Customer Segmentation")
    st.info("Module will be connected next.")

elif page == "😊 Sentiment Analysis":
    st.title("😊 Sentiment Analysis")
    st.info("Module will be connected next.")

elif page == "🌍 Policy Translation":
    st.title("🌍 Policy Translation")
    st.info("Module will be connected next.")

elif page == "📄 Policy Summarization":
    st.title("📄 Policy Summarization")
    st.info("Module will be connected next.")

elif page == "🤖 Insurance Assistant":
    st.title("🤖 Insurance Assistant")
    st.info("Module will be connected next.")

elif page == "ℹ️ About":

    st.title("About")

    st.write("AI Powered Insurance Analytics System")

    st.write("Technologies Used")

    st.write("- Python")
    st.write("- Streamlit")
    st.write("- Scikit-learn")
    st.write("- Hugging Face Transformers")
    st.write("- Pandas")
    st.write("- Matplotlib")

    st.success("Developed as a GUVI Final Project")