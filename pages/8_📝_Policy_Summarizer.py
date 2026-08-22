import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Policy Summarizer",
    page_icon="📝",
    layout="wide"
)


# ============================================================
# MODEL
# ============================================================

MODEL_NAME = "facebook/bart-large-cnn"


@st.cache_resource
def load_summarization_model():

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME
    )

    model = AutoModelForSeq2SeqLM.from_pretrained(
        MODEL_NAME
    )

    return tokenizer, model


# ============================================================
# SUMMARIZATION FUNCTION
# ============================================================

def summarize_text(text):

    tokenizer, model = load_summarization_model()

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=1024
    )

    input_length = inputs["input_ids"].shape[1]

    # Keep summary length smaller than source
    max_length = min(
        180,
        max(40, input_length // 2)
    )

    min_length = min(
        80,
        max(20, input_length // 4)
    )

    # Ensure max_length > min_length
    if max_length <= min_length:
        max_length = min_length + 10

    outputs = model.generate(
        **inputs,
        max_length=max_length,
        min_length=min_length,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True
    )

    summary = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return summary


# ============================================================
# HEADER
# ============================================================

st.title("📝 Policy Summarizer")

st.write(
    "Generate a concise summary of lengthy insurance policy "
    "documents using a transformer-based summarization model."
)

st.markdown("---")


# ============================================================
# INPUT
# ============================================================

st.subheader("📄 Enter Insurance Policy")

default_policy = """
The policy provides coverage for accidental damage,
hospitalization, emergency medical expenses, third-party
liability, natural disasters, roadside assistance, towing
services, and personal accident benefits.

Policyholders must notify the insurance company within
24 hours after an accident.

The policy does not cover driving under the influence of
alcohol, intentional damage, illegal activities, war-related
events, or nuclear events.
"""

policy_text = st.text_area(
    "Policy Text",
    value=default_policy,
    height=300,
    placeholder="Paste your insurance policy here..."
)


# ============================================================
# SUMMARY
# ============================================================

if st.button(
    "📝 Generate Summary",
    use_container_width=True
):

    if not policy_text.strip():

        st.warning(
            "Please enter policy text before generating a summary."
        )

    elif len(policy_text.split()) < 20:

        st.warning(
            "Please enter a longer policy text for meaningful summarization."
        )

    else:

        with st.spinner(
            "Generating policy summary..."
        ):

            try:

                summary = summarize_text(
                    policy_text
                )

                st.success(
                    "Policy summary generated successfully."
                )

                st.subheader("📌 Policy Summary")

                st.text_area(
                    "Summary",
                    value=summary,
                    height=220
                )

            except Exception as e:

                st.error(
                    "Unable to summarize the policy."
                )

                st.exception(e)


# ============================================================
# INFORMATION
# ============================================================

st.markdown("---")

st.info(
    """
    **Summarization Model**

    This module uses the Facebook BART-large-CNN transformer
    model to generate concise summaries from insurance policy text.
    """
)