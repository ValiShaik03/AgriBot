import streamlit as st

def set_page_config():
    st.set_page_config(page_title="AgriAssist 🌾", page_icon="🌱", layout="wide")

def display_header():
    st.title("🌾 AgriAssist — Smart Farming Chatbot 🤖")
    st.caption("Empowering farmers and agri-students with AI-powered insights.")

def handle_file_upload():
    """
    Allow user to upload PDF files to use as local knowledge base.
    """
    uploaded = st.file_uploader("📄 Upload your Agricultural Guide or Report (PDF)", type=["pdf"])
    if uploaded:
        path = f"./temp_{uploaded.name}"
        with open(path, "wb") as f:
            f.write(uploaded.read())
        st.success("✅ PDF uploaded successfully!")
        return path
    return None
