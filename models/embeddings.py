from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def create_vector_store(uploaded_pdf):
    try:
        loader = PyPDFLoader(uploaded_pdf)
        pages = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(pages)
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_documents(docs, embeddings)
        return vector_store
    except Exception as e:
        return f"Error creating vector store: {e}"

def get_pdf_context(query):
    try:
        # Replace with real FAISS retrieval if persistent vector store
        return f"Relevant PDF context for: {query}"
    except Exception as e:
        return f"Error retrieving PDF context: {e}"



