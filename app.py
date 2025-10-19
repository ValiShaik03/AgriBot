import streamlit as st
from models.llm import generate_llm_response, LLMQuotaError
from models.embeddings import create_vector_store, get_pdf_context
from utils.websearch import duckduckgo_search
from utils.serpapi_search import serpapi_search

# ==========================
# Streamlit Page Config
# ==========================
st.set_page_config(
    page_title="🌾 AgriAssist — Smart Farming Chatbot",
    page_icon="🌿",
    layout="wide"
)

st.title("🌾 AgriAssist — Smart Farming Chatbot")
st.caption("AI-powered advice for farmers and agri-students")

# ==========================
# PDF Upload
# ==========================
uploaded_pdf = st.file_uploader("📘 Upload Agriculture PDF", type=["pdf"])
vector_store = None

if uploaded_pdf:
    with st.spinner("Processing your PDF..."):
        vector_store = create_vector_store(uploaded_pdf)
        st.success("✅ PDF processed and ready for use!")

# ==========================
# Bot Response Function
# ==========================
def get_bot_response(query, uploaded_pdf=None, response_mode="Concise"):
    """
    Returns a response using PDF+LLM first, fallback to live web search if LLM fails.
    """
    pdf_context = get_pdf_context(query) if uploaded_pdf else None
    context_used = pdf_context if pdf_context and "No relevant results" not in pdf_context else "No PDF context available"

    try:
        # Try LLM first
        return generate_llm_response(query, context_used, response_mode)

    except LLMQuotaError:
        st.warning("⚠️ OpenAI quota exceeded. Fetching live web search results instead...")
        web_data = serpapi_search(query)

    if not web_data or "No relevant" in web_data or "error" in web_data.lower():
        return ("⚠️ LLM quota exceeded and live search did not return relevant answers.\n\n"
                "Please consult official agricultural websites, government portals, or uploaded PDFs for up-to-date information.")
    return web_data

    # except Exception as e:
    #     return f"⚠️ Unexpected error: {e}"

# ==========================
# Main Chat Interface
# ==========================
st.subheader("💬 Ask Your Agriculture Question")

query = st.text_input("Type your question below:")
response_mode = st.radio("Response Mode", ["Concise", "Detailed"], horizontal=True)

if st.button("Get Advice"):
    if not query:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing and fetching data..."):
            response = get_bot_response(query, uploaded_pdf=uploaded_pdf, response_mode=response_mode)
            st.success("🌿 AgriAssist’s Advice:")
            st.write(response)
