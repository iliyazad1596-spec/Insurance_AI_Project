import ast
from pathlib import Path

import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Powered Insurance Analytics System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
PAGES_DIR = BASE_DIR / "pages"


# ============================================================
# GLOBAL STYLE
# ============================================================

st.markdown(
    """
    <style>

    /* Hide Streamlit automatic multipage navigation */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* Sidebar width */
    section[data-testid="stSidebar"] {
        min-width: 280px;
        max-width: 280px;
    }

    /* Radio spacing */
    div[role="radiogroup"] {
        gap: 4px;
    }

    /* Main content */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE FINDER
# ============================================================

def find_page(pattern):

    if not PAGES_DIR.exists():
        return None

    matches = sorted(
        PAGES_DIR.glob(pattern)
    )

    if matches:
        return matches[0]

    return None


# ============================================================
# PROJECT MODULE FILES
# ============================================================

PAGE_FILES = {

    "📊 Claim Prediction":
        find_page("1_*Claim_Prediction.py"),

    "⚠️ Risk Classification":
        find_page("2_*Risk_Classification.py"),

    "🚨 Fraud Detection":
        find_page("3_*Fraud_Detection.py"),

    "👥 Customer Segmentation":
        find_page("4_*Customer_Segmentation.py"),

    "💬 Sentiment Analysis":
        find_page("5_*Sentiment_Analysis.py"),

    "📄 Policy Assistant":
        find_page("6_*Policy_Assistant.py"),

    "🌐 Policy Translator":
        find_page("7_*Policy_Translator.py"),

    "📝 Policy Summarizer":
        find_page("8_*Policy_Summarizer.py"),

    "🤖 Insurance AI Chatbot":
        find_page("9_*Insurance_AI_Chatbot.py"),
}


# ============================================================
# SINGLE CUSTOM SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🛡️ Insurance AI")

    st.markdown("---")

    st.subheader("Select Module")

    modules = [

        "🏠 Home",

        "📊 Claim Prediction",

        "⚠️ Risk Classification",

        "🚨 Fraud Detection",

        "👥 Customer Segmentation",

        "💬 Sentiment Analysis",

        "📄 Policy Assistant",

        "🌐 Policy Translator",

        "📝 Policy Summarizer",

        "🤖 Insurance AI Chatbot",

        "ℹ️ About",
    ]

    selected_module = st.radio(
        "Select Module",
        modules,
        index=0,
        label_visibility="collapsed",
        key="insurance_ai_module",
    )

    st.markdown("---")

    st.caption(
        "AI Powered Insurance Analytics System"
    )

    st.caption(
        "Machine Learning • Generative AI"
    )


# ============================================================
# HOME DASHBOARD
# ============================================================

def show_home():

    st.title(
        "🛡️ AI Powered Insurance Analytics System"
    )

    st.success(
        "Welcome to the Integrated Insurance Analytics Dashboard"
    )

    st.markdown("---")

    # --------------------------------------------------------
    # INTRODUCTION
    # --------------------------------------------------------

    st.header(
        "🚀 Integrated Insurance AI Platform"
    )

    st.write(
        """
        This application combines **Machine Learning** and
        **Generative AI** to support insurance analytics,
        customer analysis, risk assessment, fraud detection,
        sentiment analysis and policy assistance.
        """
    )

    st.markdown("---")

    # --------------------------------------------------------
    # MACHINE LEARNING
    # --------------------------------------------------------

    st.header(
        "📊 Machine Learning Modules"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "📊 Claim Prediction"
        )

        st.write(
            "Predict whether an insurance claim is likely to occur."
        )

        st.subheader(
            "⚠️ Risk Classification"
        )

        st.write(
            "Classify customers according to their insurance risk level."
        )

        st.subheader(
            "🚨 Fraud Detection"
        )

        st.write(
            "Identify potentially fraudulent insurance claims."
        )

    with col2:

        st.subheader(
            "👥 Customer Segmentation"
        )

        st.write(
            """
            Segment insurance customers based on their
            characteristics and behaviour.
            """
        )

        st.subheader(
            "💬 Sentiment Analysis"
        )

        st.write(
            "Analyze customer reviews and classify their sentiment."
        )

    st.markdown("---")

    # --------------------------------------------------------
    # GENERATIVE AI
    # --------------------------------------------------------

    st.header(
        "🧠 Generative AI Modules"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "📄 Policy Assistant"
        )

        st.write(
            """
            Get quick answers about insurance coverage,
            exclusions and claim procedures.
            """
        )

        st.subheader(
            "🌐 Policy Translator"
        )

        st.write(
            "Translate insurance policy content into another language."
        )

    with col2:

        st.subheader(
            "📝 Policy Summarizer"
        )

        st.write(
            """
            Generate concise summaries of lengthy
            insurance policy documents.
            """
        )

        st.subheader(
            "🤖 Insurance AI Chatbot"
        )

        st.write(
            """
            Interact with an AI-powered assistant
            for insurance-related questions.
            """
        )

    st.markdown("---")

    st.info(
        """
        This platform integrates Machine Learning and
        Generative AI to provide intelligent insurance
        analytics and customer support.
        """
    )


# ============================================================
# ABOUT
# ============================================================

def show_about():

    st.title(
        "ℹ️ About Insurance AI"
    )

    st.markdown("---")

    st.header(
        "AI Powered Insurance Analytics System"
    )

    st.write(
        """
        The Insurance AI project is an integrated
        artificial intelligence platform designed for
        insurance analytics and customer support.
        """
    )

    st.markdown(
        "### 📊 Machine Learning"
    )

    st.write(
        """
        • Claim Prediction  
        • Risk Classification  
        • Fraud Detection  
        • Customer Segmentation  
        • Sentiment Analysis
        """
    )

    st.markdown(
        "### 🧠 Generative AI"
    )

    st.write(
        """
        • Policy Assistant  
        • Policy Translation  
        • Policy Summarization  
        • Insurance AI Chatbot
        """
    )

    st.markdown("---")

    st.info(
        "Developed as an integrated Insurance AI analytics project."
    )


# ============================================================
# AST HELPERS
# ============================================================

def is_streamlit_method_call(
    node,
    method_name
):

    return (
        isinstance(node, ast.Call)
        and
        isinstance(node.func, ast.Attribute)
        and
        isinstance(node.func.value, ast.Name)
        and
        node.func.value.id == "st"
        and
        node.func.attr == method_name
    )


def is_sidebar_call(node):

    return (
        isinstance(node, ast.Call)
        and
        isinstance(node.func, ast.Attribute)
        and
        isinstance(node.func.value, ast.Attribute)
        and
        isinstance(node.func.value.value, ast.Name)
        and
        node.func.value.value.id == "st"
        and
        node.func.value.attr == "sidebar"
    )


# ============================================================
# MODULE CLEANER
# ============================================================

class ModuleCleaner(
    ast.NodeTransformer
):

    """
    Converts the existing standalone Streamlit modules
    into modules that can run inside this single dashboard.

    Removes:

    • st.set_page_config()
    • old sidebar title
    • old sidebar radio
    • chatbot sidebar block

    The actual model / UI / prediction logic remains intact.
    """

    def visit_Expr(
        self,
        node
    ):

        # Remove st.set_page_config(...)
        if is_streamlit_method_call(
            node.value,
            "set_page_config"
        ):

            return None

        # Remove standalone sidebar calls
        if is_sidebar_call(
            node.value
        ):

            return None

        return self.generic_visit(node)


    def visit_Assign(
        self,
        node
    ):

        # Remove:
        #
        # page = st.sidebar.radio(...)
        #
        if is_sidebar_call(
            node.value
        ):

            return None

        return self.generic_visit(node)


    def visit_With(
        self,
        node
    ):

        # Remove:
        #
        # with st.sidebar:
        #
        for item in node.items:

            context = item.context_expr

            if (
                isinstance(
                    context,
                    ast.Attribute
                )
                and
                isinstance(
                    context.value,
                    ast.Name
                )
                and
                context.value.id == "st"
                and
                context.attr == "sidebar"
            ):

                return None

        return self.generic_visit(node)


# ============================================================
# PREPARE MODULE
# ============================================================

def prepare_module(
    source,
    forced_page=None
):

    tree = ast.parse(
        source
    )

    cleaner = ModuleCleaner()

    tree = cleaner.visit(
        tree
    )

    # --------------------------------------------------------
    # CLAIM PREDICTION SPECIAL CASE
    # --------------------------------------------------------
    #
    # Your uploaded Claim Prediction file is an older combined
    # dashboard file. It contains:
    #
    # if page == "Home":
    # elif page == "Claim Prediction":
    # ...
    #
    # We force it to execute its Claim Prediction branch.
    #

    if forced_page is not None:

        page_assignment = ast.Assign(

            targets=[
                ast.Name(
                    id="page",
                    ctx=ast.Store()
                )
            ],

            value=ast.Constant(
                value=forced_page
            )
        )

        # Put page assignment after imports
        insert_position = 0

        while (
            insert_position < len(tree.body)
            and
            isinstance(
                tree.body[insert_position],
                (
                    ast.Import,
                    ast.ImportFrom
                )
            )
        ):

            insert_position += 1

        tree.body.insert(
            insert_position,
            page_assignment
        )

    ast.fix_missing_locations(
        tree
    )

    return tree


# ============================================================
# RUN EXISTING MODULE
# ============================================================

def run_existing_module(
    module_name,
    page_file
):

    # --------------------------------------------------------
    # FILE CHECK
    # --------------------------------------------------------

    if page_file is None:

        st.error(
            f"""
            ❌ **{module_name} file was not found.**

            Expected inside:

            `{PAGES_DIR}`
            """
        )

        return


    # --------------------------------------------------------
    # LOAD SOURCE
    # --------------------------------------------------------

    try:

        source = page_file.read_text(
            encoding="utf-8"
        )

    except Exception as exc:

        st.error(
            f"Unable to read {module_name}."
        )

        st.exception(
            exc
        )

        return


    # --------------------------------------------------------
    # PREPARE SOURCE
    # --------------------------------------------------------

    try:

        forced_page = None

        # Your actual uploaded file is:
        #
        # 1_🏥_Claim_Prediction.py
        #
        # and internally uses:
        #
        # "🏥 Claim Prediction"

        if module_name == "📊 Claim Prediction":

            forced_page = (
                "🏥 Claim Prediction"
            )


        tree = prepare_module(
            source,
            forced_page=forced_page
        )


        code = compile(
            tree,
            str(page_file),
            "exec"
        )


    except Exception as exc:

        st.error(
            f"Unable to prepare {module_name}."
        )

        st.exception(
            exc
        )

        return


    # --------------------------------------------------------
    # EXECUTE MODULE
    # --------------------------------------------------------

    try:

        module_globals = {

            "__name__":
                "__main__",

            "__file__":
                str(page_file),

            "__package__":
                None,
        }

        exec(
            code,
            module_globals
        )

    except Exception as exc:

        st.error(
            f"❌ Unable to load {module_name}."
        )

        st.exception(
            exc
        )


# ============================================================
# APPLICATION ROUTER
# ============================================================

if selected_module == "🏠 Home":

    show_home()


elif selected_module == "ℹ️ About":

    show_about()


else:

    run_existing_module(
        selected_module,
        PAGE_FILES.get(
            selected_module
        )
    )