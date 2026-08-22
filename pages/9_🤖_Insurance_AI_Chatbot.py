import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Insurance AI Chatbot",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# POLICY KNOWLEDGE BASE
# ============================================================

POLICY_DATA = {

    "coverage": """
The insurance policy provides coverage for:

• Accidental damage
• Hospitalization
• Emergency medical expenses
• Third-party liability
• Natural disasters
• Roadside assistance
• Towing services
• Personal accident benefits
""",

    "exclusions": """
Major policy exclusions include:

• Driving under the influence of alcohol
• Intentional damage
• Illegal activities
• War-related events
• Nuclear events
""",

    "claim": """
To file an insurance claim:

1. Report the accident to the insurance company.
2. Notify the insurance company within 24 hours after the accident.
3. Submit the required claim form and supporting documents.
4. Provide relevant accident or medical documentation.
5. Cooperate with the claim assessment process.
""",

    "alcohol": """
Claims arising while driving under the influence of alcohol
are excluded from the policy coverage.
""",

    "notification": """
Policyholders must notify the insurance company within
24 hours after an accident.
"""
}


# ============================================================
# RESPONSE FUNCTION
# ============================================================

def get_response(question):

    question = question.lower().strip()

    # Coverage
    if any(
        word in question
        for word in [
            "cover",
            "coverage",
            "covered",
            "benefits"
        ]
    ):

        return POLICY_DATA["coverage"]

    # Exclusions
    if any(
        word in question
        for word in [
            "exclude",
            "exclusion",
            "not covered",
            "doesn't cover",
            "does not cover"
        ]
    ):

        return POLICY_DATA["exclusions"]

    # Alcohol
    if any(
        word in question
        for word in [
            "alcohol",
            "drink",
            "drunk",
            "drinking",
            "dui"
        ]
    ):

        return POLICY_DATA["alcohol"]

    # Claim
    if any(
        word in question
        for word in [
            "claim",
            "file a claim",
            "submit a claim",
            "claim process"
        ]
    ):

        return POLICY_DATA["claim"]

    # Accident notification
    if any(
        word in question
        for word in [
            "24 hours",
            "report accident",
            "notify",
            "notification"
        ]
    ):

        return POLICY_DATA["notification"]

    # Greeting
    if any(
        word in question
        for word in [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon"
        ]
    ):

        return (
            "Hello! 👋 I am your Insurance AI Assistant. "
            "You can ask me about policy coverage, exclusions, "
            "claims, or accident reporting."
        )

    # Default
    return (
        "I can help you with the following insurance topics:\n\n"
        "• Policy coverage\n"
        "• Policy exclusions\n"
        "• Filing an insurance claim\n"
        "• Accident notification\n"
        "• Alcohol-related exclusions\n\n"
        "Please ask a question about one of these topics."
    )


# ============================================================
# HEADER
# ============================================================

st.title("🤖 Insurance AI Chatbot")

st.write(
    "Ask questions about insurance coverage, exclusions, "
    "claims, and policy procedures."
)

st.markdown("---")


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# ============================================================
# CHAT INPUT
# ============================================================

user_question = st.chat_input(
    "Ask an insurance question..."
)


if user_question:

    # --------------------------------------------------------
    # User message
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):

        st.markdown(
            user_question
        )


    # --------------------------------------------------------
    # Bot response
    # --------------------------------------------------------

    response = get_response(
        user_question
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):

        st.markdown(
            response
        )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("### 🤖 Insurance AI Assistant")

    st.write(
        "Ask questions about:"
    )

    st.markdown(
        """
        - 🛡️ Coverage
        - 🚫 Exclusions
        - 📋 Claims
        - ⏰ Accident reporting
        - 🚗 Driving-related exclusions
        """
    )

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("---")

st.info(
    """
    **Disclaimer:** This chatbot provides information based on
    the policy information included in this application.
    Always refer to the actual insurance policy and contact the
    insurance provider for official claim decisions.
    """
)