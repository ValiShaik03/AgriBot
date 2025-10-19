def retrieve_from_rag(vectorstore, query, k=3):
    """
    Retrieve top-k similar chunks for query from FAISS store.
    """
    try:
        docs = vectorstore.similarity_search(query, k=k)
        return "\n\n".join([d.page_content for d in docs])
    except Exception as e:
        return f"RAG retrieval error: {e}"
