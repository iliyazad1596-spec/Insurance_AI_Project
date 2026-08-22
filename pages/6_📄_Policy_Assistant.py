import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Policy Assistant",
    page_icon="📄",
    layout="wide"
)


# ============================================================
# POLICY INFORMATION
# ============================================================

POLICY_COVERAGE = """
The policy provides coverage for:

• Accidental damage
• Hospitalization
• Emergency medical expenses
• Third-party liability
• Natural disasters
• Roadside assistance
• Towing services
• Personal accident benefits
"""

POLICY_EXCLUSIONS = """
The policy does not cover:

• Driving under the influence of alcohol
• Intentional damage
• Illegal activities
• War
• Nuclear events
"""

CLAIM_PROCEDURE = """
To file a claim:

1. Notify the insurance company within 24 hours after an accident.
2. Provide the required accident and policy information.
3. Submit the claim documentation requested by the insurance company.
4. Contact customer support if additional assistance is required.
"""


# ============================================================
# PAGE HEADER
# ============================================================

st.title("📄 Insurance Policy Assistant")

st.write(
    """
    Get quick answers about insurance coverage, exclusions,
    and the claim procedure.
    """
)

st.markdown("---")


# ============================================================
# QUICK INFORMATION CARDS
# ============================================================

st.subheader("📌 Quick Policy Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Coverage Areas",
        "8"
    )

with col2:
    st.metric(
        "Major Exclusions",
        "5"
    )

with col3:
    st.metric(
        "Claim Notification",
        "24 Hours"
    )


st.markdown("---")


# ============================================================
# QUICK QUESTIONS
# ============================================================

st.subheader("🔎 Quick Questions")

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🛡️ What does my policy cover?",
        use_container_width=True
    ):

        st.success("### Policy Coverage")

        st.markdown(
            POLICY_COVERAGE
        )


with col2:

    if st.button(
        "🚫 What is not covered?",
        use_container_width=True
    ):

        st.error("### Policy Exclusions")

        st.markdown(
            POLICY_EXCLUSIONS
        )


col1, col2 = st.columns(2)

with col1:

    if st.button(
        "📋 How do I file a claim?",
        use_container_width=True
    ):

        st.info("### Claim Procedure")

        st.markdown(
            CLAIM_PROCEDURE
        )


with col2:

    if st.button(
        "⏰ When should I report an accident?",
        use_container_width=True
    ):

        st.warning(
            """
            ### Important

            Policyholders must notify the insurance
            company within **24 hours after an accident**.
            """
        )


# ============================================================
# QUESTION & ANSWER
# ============================================================

st.markdown("---")

st.subheader("💬 Ask About Your Policy")

question = st.text_input(
    "Enter your question",
    placeholder="Example: Does my policy cover hospitalization?"
)


if st.button(
    "🔍 Get Answer",
    use_container_width=True
):

    if not question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        q = question.lower()


        # ====================================================
        # COVERAGE QUESTIONS
        # ====================================================

        if any(
            word in q
            for word in [
                "cover",
                "coverage",
                "covered",
                "benefit",
                "hospital",
                "medical",
                "roadside",
                "towing",
                "accident"
            ]
        ):

            st.success(
                "### 🛡️ Policy Coverage"
            )

            st.markdown(
                POLICY_COVERAGE
            )


        # ====================================================
        # EXCLUSION QUESTIONS
        # ====================================================

        elif any(
            word in q
            for word in [
                "exclude",
                "exclusion",
                "not cover",
                "not covered",
                "alcohol",
                "drink",
                "drunk",
                "illegal",
                "war",
                "nuclear",
                "intentional"
            ]
        ):

            st.error(
                "### 🚫 Policy Exclusions"
            )

            st.markdown(
                POLICY_EXCLUSIONS
            )


        # ====================================================
        # CLAIM QUESTIONS
        # ====================================================

        elif any(
            word in q
            for word in [
                "claim",
                "file",
                "submit",
                "accident report"
            ]
        ):

            st.info(
                "### 📋 Claim Procedure"
            )

            st.markdown(
                CLAIM_PROCEDURE
            )


        # ====================================================
        # TIME / NOTIFICATION QUESTIONS
        # ====================================================

        elif any(
            word in q
            for word in [
                "when",
                "how long",
                "24",
                "notify",
                "notification"
            ]
        ):

            st.warning(
                """
                ### ⏰ Accident Notification

                Policyholders must notify the insurance
                company within **24 hours after an accident**.
                """
            )


        # ====================================================
        # UNKNOWN QUESTION
        # ====================================================

        else:

            st.warning(
                """
                I could not find a specific answer for that
                question in the available policy information.

                Try asking about:

                • Coverage
                • Hospitalization
                • Medical expenses
                • Roadside assistance
                • Towing
                • Policy exclusions
                • Alcohol-related incidents
                • Filing a claim
                • Accident notification
                """
            )


# ============================================================
# POLICY SUMMARY
# ============================================================

st.markdown("---")

with st.expander("📝 Policy Summary"):

    st.write(
        """
        The policy provides coverage for accidental damage,
        hospitalization, emergency medical expenses,
        third-party liability, natural disasters, roadside
        assistance, towing services, and personal accident
        benefits.

        Policyholders must notify the insurance company within
        24 hours after an accident.
        """
    )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("---")

st.caption(
    "⚠️ This assistant provides information based on the "
    "available policy content. Refer to the official policy "
    "document for complete terms and conditions."
)