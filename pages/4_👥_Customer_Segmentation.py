import streamlit as st
import joblib
import pandas as pd
import numpy as np


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="👥",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("👥 Customer Segmentation")

st.write(
    """
    Identify the customer segment using the trained
    customer segmentation machine learning model.
    """
)

st.markdown("---")


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    return joblib.load(
        "models/customer_segmentation_model.pkl"
    )


@st.cache_resource
def load_scaler():

    return joblib.load(
        "models/customer_scaler.pkl"
    )


try:

    model = load_model()
    scaler = load_scaler()

except Exception as e:

    st.error("❌ Unable to load customer segmentation files.")

    st.exception(e)

    st.stop()


# ============================================================
# GET EXACT TRAINING FEATURES
# ============================================================

expected_features = None

if hasattr(scaler, "feature_names_in_"):

    expected_features = list(
        scaler.feature_names_in_
    )

elif hasattr(model, "feature_names_in_"):

    expected_features = list(
        model.feature_names_in_
    )


# ============================================================
# DISPLAY MODEL INFORMATION
# ============================================================

if hasattr(scaler, "n_features_in_"):

    st.success(
        f"✅ Model loaded successfully — "
        f"{scaler.n_features_in_} features expected."
    )

else:

    st.success(
        "✅ Customer segmentation model loaded."
    )


# ============================================================
# EDUCATION
# ============================================================

education_map = {
    "Basic": 0,
    "Graduation": 1,
    "Master": 2,
    "PhD": 3
}


# ============================================================
# MARITAL STATUS
# ============================================================

marital_map = {
    "Single": 0,
    "Married": 1,
    "Together": 2,
    "Divorced": 3,
    "Widow": 4,
    "Other": 5
}


# ============================================================
# CUSTOMER INFORMATION
# ============================================================

st.subheader("👤 Customer Information")

col1, col2, col3 = st.columns(3)


with col1:

    year_birth = st.number_input(
        "Year of Birth",
        min_value=1900,
        max_value=2025,
        value=1980
    )


with col2:

    education = st.selectbox(
        "Education",
        list(education_map.keys())
    )


with col3:

    marital_status = st.selectbox(
        "Marital Status",
        list(marital_map.keys())
    )


# ============================================================
# FINANCIAL INFORMATION
# ============================================================

st.markdown("---")

st.subheader("💰 Financial & Family Information")

col1, col2, col3 = st.columns(3)


with col1:

    income = st.number_input(
        "Income",
        min_value=0.0,
        max_value=1000000.0,
        value=50000.0,
        step=1000.0
    )


with col2:

    kidhome = st.number_input(
        "Kids at Home",
        min_value=0,
        max_value=10,
        value=0
    )


with col3:

    teenhome = st.number_input(
        "Teenagers at Home",
        min_value=0,
        max_value=10,
        value=0
    )


# ============================================================
# CUSTOMER ACTIVITY
# ============================================================

st.markdown("---")

st.subheader("📅 Customer Activity")

col1, col2, col3 = st.columns(3)


with col1:

    recency = st.number_input(
        "Recency (Days)",
        min_value=0,
        max_value=365,
        value=30
    )


with col2:

    customer_year = st.number_input(
        "Customer Year",
        min_value=2000,
        max_value=2030,
        value=2014
    )


with col3:

    customer_month = st.number_input(
        "Customer Month",
        min_value=1,
        max_value=12,
        value=1
    )


# ============================================================
# PRODUCT SPENDING
# ============================================================

st.markdown("---")

st.subheader("🛒 Product Spending")

col1, col2, col3 = st.columns(3)


with col1:

    mnt_wines = st.number_input(
        "Wine Spending",
        min_value=0,
        value=300
    )


with col2:

    mnt_fruits = st.number_input(
        "Fruit Spending",
        min_value=0,
        value=50
    )


with col3:

    mnt_meat = st.number_input(
        "Meat Products Spending",
        min_value=0,
        value=200
    )


col1, col2, col3 = st.columns(3)


with col1:

    mnt_fish = st.number_input(
        "Fish Products Spending",
        min_value=0,
        value=50
    )


with col2:

    mnt_sweet = st.number_input(
        "Sweet Products Spending",
        min_value=0,
        value=50
    )


with col3:

    mnt_gold = st.number_input(
        "Gold Products Spending",
        min_value=0,
        value=100
    )


# ============================================================
# PURCHASE BEHAVIOUR
# ============================================================

st.markdown("---")

st.subheader("🛍️ Purchase Behaviour")

col1, col2, col3 = st.columns(3)


with col1:

    deals = st.number_input(
        "Deal Purchases",
        min_value=0,
        value=2
    )


with col2:

    web_purchases = st.number_input(
        "Web Purchases",
        min_value=0,
        value=4
    )


with col3:

    catalog_purchases = st.number_input(
        "Catalog Purchases",
        min_value=0,
        value=2
    )


col1, col2 = st.columns(2)


with col1:

    store_purchases = st.number_input(
        "Store Purchases",
        min_value=0,
        value=5
    )


with col2:

    web_visits = st.number_input(
        "Web Visits per Month",
        min_value=0,
        value=5
    )


# ============================================================
# CAMPAIGN INFORMATION
# ============================================================

st.markdown("---")

st.subheader("📢 Campaign History")

col1, col2, col3 = st.columns(3)


with col1:

    accepted_cmp1 = st.selectbox(
        "Accepted Campaign 1",
        [0, 1]
    )


with col2:

    accepted_cmp2 = st.selectbox(
        "Accepted Campaign 2",
        [0, 1]
    )


with col3:

    accepted_cmp3 = st.selectbox(
        "Accepted Campaign 3",
        [0, 1]
    )


col1, col2 = st.columns(2)


with col1:

    accepted_cmp4 = st.selectbox(
        "Accepted Campaign 4",
        [0, 1]
    )


with col2:

    accepted_cmp5 = st.selectbox(
        "Accepted Campaign 5",
        [0, 1]
    )


# ============================================================
# OTHER INFORMATION
# ============================================================

st.markdown("---")

st.subheader("📋 Other Information")

col1, col2, col3 = st.columns(3)


with col1:

    complain = st.selectbox(
        "Complaint",
        [0, 1],
        format_func=lambda x:
        "Yes" if x == 1 else "No"
    )


with col2:

    response = st.selectbox(
        "Campaign Response",
        [0, 1],
        format_func=lambda x:
        "Yes" if x == 1 else "No"
    )


with col3:

    st.write("")

    st.write(
        "Z_CostContact = 3"
    )

    st.write(
        "Z_Revenue = 11"
    )


# ============================================================
# CREATE ALL POSSIBLE FEATURES
# ============================================================

all_features = {

    "Year_Birth":
        year_birth,

    "Education":
        education_map[education],

    "Marital_Status":
        marital_map[marital_status],

    "Income":
        income,

    "Kidhome":
        kidhome,

    "Teenhome":
        teenhome,

    "Recency":
        recency,

    "MntWines":
        mnt_wines,

    "MntFruits":
        mnt_fruits,

    "MntMeatProducts":
        mnt_meat,

    "MntFishProducts":
        mnt_fish,

    "MntSweetProducts":
        mnt_sweet,

    "MntGoldProds":
        mnt_gold,

    "NumDealsPurchases":
        deals,

    "NumWebPurchases":
        web_purchases,

    "NumCatalogPurchases":
        catalog_purchases,

    "NumStorePurchases":
        store_purchases,

    "NumWebVisitsMonth":
        web_visits,

    "AcceptedCmp3":
        accepted_cmp3,

    "AcceptedCmp4":
        accepted_cmp4,

    "AcceptedCmp5":
        accepted_cmp5,

    "AcceptedCmp1":
        accepted_cmp1,

    "AcceptedCmp2":
        accepted_cmp2,

    "Complain":
        complain,

    "Z_CostContact":
        3,

    "Z_Revenue":
        11,

    "Response":
        response,

    "Customer_Year":
        customer_year,

    "Customer_Month":
        customer_month
}


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.markdown("---")

if st.button(
    "🔍 Identify Customer Segment",
    use_container_width=True
):

    try:

        # ====================================================
        # DETERMINE EXACT FEATURES REQUIRED BY SCALER
        # ====================================================

        if expected_features is not None:

            missing_features = [

                feature

                for feature in expected_features

                if feature not in all_features

            ]

            if missing_features:

                st.error(
                    "The saved model requires features "
                    "that are not available in this page:"
                )

                st.write(
                    missing_features
                )

                st.stop()


            # Create DataFrame using EXACT training order

            input_data = pd.DataFrame(

                [
                    {
                        feature:
                        all_features[feature]

                        for feature
                        in expected_features
                    }
                ],

                columns=expected_features

            )

        else:

            # ------------------------------------------------
            # FALLBACK
            # ------------------------------------------------

            input_data = pd.DataFrame(
                [all_features]
            )


        # ====================================================
        # CHECK FEATURE COUNT
        # ====================================================

        if hasattr(
            scaler,
            "n_features_in_"
        ):

            expected_count = (
                scaler.n_features_in_
            )

            actual_count = (
                input_data.shape[1]
            )

            if actual_count != expected_count:

                st.error(
                    f"""
                    ❌ Feature mismatch.

                    Expected features: {expected_count}

                    Supplied features: {actual_count}
                    """
                )

                st.stop()


        # ====================================================
        # SCALE INPUT
        # ====================================================

        scaled_input = scaler.transform(
            input_data
        )


        # ====================================================
        # PREDICT
        # ====================================================

        prediction = model.predict(
            scaled_input
        )


        cluster = int(
            prediction[0]
        )


        # ====================================================
        # DISPLAY RESULT
        # ====================================================

        st.markdown("---")

        st.subheader(
            "🎯 Customer Segment Result"
        )


        st.success(
            f"Customer belongs to Segment {cluster + 1}"
        )


        st.metric(
            "Customer Segment",
            f"Segment {cluster + 1}"
        )


        # ====================================================
        # SEGMENT DESCRIPTION
        # ====================================================

        segment_descriptions = {

            0:
            """
            **Segment 1**

            Customers belonging to this cluster have
            similar purchasing and engagement behaviour.
            Consider personalized offers and retention
            strategies.
            """,

            1:
            """
            **Segment 2**

            Customers in this cluster show a different
            purchasing pattern. Target them with relevant
            promotions and insurance products.
            """,

            2:
            """
            **Segment 3**

            Customers in this cluster may require additional
            engagement and personalized communication.
            """,

            3:
            """
            **Segment 4**

            This cluster represents another customer behaviour
            pattern identified by the trained model.
            """
        }


        description = segment_descriptions.get(
            cluster,
            """
            This customer belongs to a cluster identified
            by the trained segmentation model.
            """
        )


        st.info(
            description
        )


        # ====================================================
        # CUSTOMER SUMMARY
        # ====================================================

        st.markdown("---")

        st.subheader(
            "📊 Customer Summary"
        )


        total_spending = (

            mnt_wines
            + mnt_fruits
            + mnt_meat
            + mnt_fish
            + mnt_sweet
            + mnt_gold

        )


        total_purchases = (

            web_purchases
            + catalog_purchases
            + store_purchases

        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Total Spending",
                f"${total_spending:,.0f}"
            )


        with col2:

            st.metric(
                "Total Purchases",
                total_purchases
            )


        with col3:

            st.metric(
                "Recency",
                f"{recency} days"
            )


    except Exception as e:

        st.error(
            "❌ Unable to perform customer segmentation."
        )

        st.exception(e)