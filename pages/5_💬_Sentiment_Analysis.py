import streamlit as st
import joblib
import os


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="💬",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("💬 Insurance Review Sentiment Analysis")

st.write(
    """
    Enter an insurance customer review below.
    The trained machine learning model will classify
    the review as Negative, Neutral, or Positive.
    """
)

st.markdown("---")


# ============================================================
# MODEL PATHS
# ============================================================

MODEL_PATH = "models/sentiment_model.pkl"

VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    if not os.path.exists(MODEL_PATH):

        raise FileNotFoundError(
            f"Model not found: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


# ============================================================
# LOAD TF-IDF VECTORIZER
# ============================================================

@st.cache_resource
def load_vectorizer():

    if not os.path.exists(VECTORIZER_PATH):

        raise FileNotFoundError(
            f"Vectorizer not found: {VECTORIZER_PATH}"
        )

    return joblib.load(VECTORIZER_PATH)


# ============================================================
# LOAD FILES
# ============================================================

try:

    model = load_model()

    vectorizer = load_vectorizer()

    st.success(
        "✅ Sentiment model and TF-IDF vectorizer loaded successfully."
    )

except Exception as e:

    st.error(
        "❌ Unable to load sentiment analysis files."
    )

    st.exception(e)

    st.stop()


# ============================================================
# REVIEW INPUT
# ============================================================

st.subheader("📝 Customer Review")

review = st.text_area(
    "Enter customer review",
    height=180,
    placeholder=(
        "Example: The insurance service was excellent "
        "and the claim process was very quick."
    )
)


# ============================================================
# ANALYZE BUTTON
# ============================================================

if st.button(
    "🔍 Analyze Sentiment",
    use_container_width=True
):

    if not review.strip():

        st.warning(
            "⚠️ Please enter a customer review."
        )

        st.stop()


    try:

        # ====================================================
        # TRANSFORM TEXT USING TF-IDF
        # ====================================================

        review_vector = vectorizer.transform(
            [review]
        )


        # ====================================================
        # PREDICT SENTIMENT
        # ====================================================

        prediction = model.predict(
            review_vector
        )[0]


        # ====================================================
        # CONVERT PREDICTION TO LABEL
        # ====================================================

        sentiment_labels = {

            0: "Negative",

            1: "Neutral",

            2: "Positive"
        }


        # Handle both integer and string predictions

        if isinstance(prediction, str):

            sentiment = prediction

        else:

            sentiment = sentiment_labels.get(
                int(prediction),
                "Unknown"
            )


        # ====================================================
        # DISPLAY RESULT
        # ====================================================

        st.markdown("---")

        st.subheader(
            "🎯 Sentiment Result"
        )


        if sentiment.lower() == "positive":

            st.success(
                "😊 Positive Sentiment"
            )


        elif sentiment.lower() == "negative":

            st.error(
                "😞 Negative Sentiment"
            )


        elif sentiment.lower() == "neutral":

            st.warning(
                "😐 Neutral Sentiment"
            )


        else:

            st.info(
                f"Sentiment: {sentiment}"
            )


        # ====================================================
        # CONFIDENCE
        # ====================================================

        if hasattr(
            model,
            "predict_proba"
        ):

            probabilities = model.predict_proba(
                review_vector
            )[0]


            confidence = (
                max(probabilities) * 100
            )


            st.metric(
                "Prediction Confidence",
                f"{confidence:.2f}%"
            )


        # ====================================================
        # REVIEW DISPLAY
        # ====================================================

        st.markdown("---")

        st.subheader(
            "📄 Analyzed Review"
        )

        st.info(
            review
        )


    except Exception as e:

        st.error(
            "❌ Unable to analyze the review."
        )

        st.exception(e)