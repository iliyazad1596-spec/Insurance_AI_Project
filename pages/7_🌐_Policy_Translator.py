import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Policy Translator",
    page_icon="🌐",
    layout="wide"
)


# ============================================================
# MODEL
# ============================================================

MODEL_NAME = "Helsinki-NLP/opus-mt-en-fr"


@st.cache_resource
def load_translation_model():

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    return tokenizer, model


# ============================================================
# TRANSLATION FUNCTION
# ============================================================

def translate_text(text):

    tokenizer, model = load_translation_model()

    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_length=512,
        num_beams=4,
        early_stopping=True
    )

    translated_text = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return translated_text


# ============================================================
# HEADER
# ============================================================

st.title("🌐 Policy Translator")

st.write(
    "Translate insurance policy text from English to French "
    "using a transformer-based language model."
)

st.markdown("---")


# ============================================================
# INPUT
# ============================================================

st.subheader("📄 Enter Policy Text")

default_text = """Your insurance policy covers accidental damages,
medical expenses, hospitalization and emergency assistance."""

policy_text = st.text_area(
    "English Policy Text",
    value=default_text,
    height=220,
    placeholder="Enter insurance policy text here..."
)


# ============================================================
# TRANSLATE
# ============================================================

if st.button(
    "🌐 Translate to French",
    use_container_width=True
):

    if not policy_text.strip():

        st.warning(
            "Please enter some policy text before translating."
        )

    else:

        with st.spinner(
            "Translating policy text..."
        ):

            try:

                translated = translate_text(
                    policy_text
                )

                st.success(
                    "Translation completed successfully."
                )

                st.subheader("🇫🇷 French Translation")

                st.text_area(
                    "Translated Text",
                    value=translated,
                    height=220
                )

            except Exception as e:

                st.error(
                    "Unable to translate the policy text."
                )

                st.exception(e)


# ============================================================
# INFORMATION
# ============================================================

st.markdown("---")

st.info(
    """
    **Translation Model**

    English → French translation is performed using the
    Helsinki-NLP OPUS-MT transformer model.
    """
)