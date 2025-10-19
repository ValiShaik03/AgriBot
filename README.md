# 🌾 AgriAssist — Smart Farming Chatbot

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) ![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-orange.svg)![License](https://img.shields.io/badge/License-MIT-green.svg) [![SerpAPI](https://img.shields.io/badge/SerpAPI-Active-blue?logo=google&logoColor=white)](https://serpapi.com/)
[![DuckDuckGo](https://img.shields.io/badge/DuckDuckGo-Integrated-orange?logo=duckduckgo&logoColor=white)](https://duckduckgo.com/)

## **Live Demo**
Try AgriAssist directly on **Streamlit Cloud**:  
[🌾 Launch AgriAssist on Streamlit Cloud](https://smartfarmer.streamlit.app)

**AI-powered advice for farmers and agri-students**

---

## **Overview**

AgriAssist is a context-aware agricultural assistant designed to provide instant, reliable answers to farmers and agri-students. Users can:

- Upload PDF manuals or crop guides for personalized advice.
- Ask questions related to crops, pests, fertilizers, irrigation, and government schemes.
- Receive responses in **Concise** or **Detailed** mode.

The app intelligently combines **local PDF knowledge** with **live web search** and **LLM-generated insights** to ensure accurate and timely information.

---

## **Why Live Web Search is Needed**

1. **Dynamic Nature of Agriculture Information**  
   Agricultural practices, government subsidies, crop prices, and pest alerts change frequently. Static PDFs or manuals cannot provide the latest updates.  

2. **LLM Quota & Knowledge Limits**  
   Large Language Models (LLMs) like GPT-3.5-turbo have:  
   - Knowledge cutoff dates (e.g., Oct 2023)  
   - Quota limitations (API usage caps)  

   This means that relying solely on LLMs may result in **outdated or unavailable answers**.

3. **Fallback for Missing PDF Context**  
   - Users may not always upload PDFs.  
   - PDFs may not contain answers to all queries.  

   **Live web search ensures users still receive a relevant answer** when local context is insufficient.

4. **Real-Time Policy Updates**  
   Example:  
   - Query: *“Latest subsidies for rice farmers in Maharashtra 2025”*  
   - A PDF guide may only include historical subsidies.  
   - DuckDuckGo abstracts may be generic.  
   - **SerpAPI live search fetches real-time government announcements or news**, providing actionable advice.

---

## **How Live Web Search Works**

1. **DuckDuckGo API**  
   - Provides quick abstracts and related topics.  
   - Used first as a lightweight, free search option.  
   - Limitation: May not always have the most recent data.

2. **SerpAPI (Google Search)**  
   - Used as a fallback if DuckDuckGo or PDF RAG doesn’t return relevant results.  
   - Fetches the top real-time Google search results.  
   - Summarizes snippets to provide actionable, up-to-date insights.  

This multi-step approach guarantees **reliable answers even when LLM fails or PDFs don’t cover the query**.

---

## **System Architecture**
```
User Query
│
├─ PDF RAG → Extract context from uploaded PDFs
│
├─ DuckDuckGo Search → Lightweight web info
│
├─ SerpAPI Search → Latest live web results
│
└─ LLM → Generate concise or detailed advice based on available context
│
Output → Display to user
```

**Modules:**

- `models/llm.py` → Integrates LLM for response generation  
- `models/embeddings.py` → Creates embeddings from uploaded PDFs  
- `utils/rag_utils.py` → Retrieves relevant chunks from PDF embeddings  
- `utils/websearch.py` → Performs DuckDuckGo and SerpAPI live searches  
- `utils/helpers.py` → Streamlit UI helpers and PDF upload handling  
- `app.py` → Main Streamlit interface  

---

## **Key Features**

- Upload multiple PDFs for personalized advice  
- Support for **Concise** (quick tips) or **Detailed** (in-depth explanation) modes  
- Live web search ensures up-to-date information  
- Intelligent fallback from PDF → DuckDuckGo → SerpAPI → LLM  

---

## **Setup Instructions**

1. Clone the repo and navigate to the folder:

```bash
git clone <repo-url>
cd agriassist
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Create .env file with your API keys:
```bash
OPENAI_API_KEY=your_openai_key
SERPAPI_API_KEY=your_serpapi_key
```
4. Run the Streamlit app:
```bash
streamlit run app.py
```

## 🖼️ Project Preview

HomePage<br>
![AgriAssist Homepage](https://github.com/ValiShaik03/AgriBot/blob/7db9c3de9ab67ae6370319739146b5049ac8f7fd/output/output1.png) <br>
AgriAssist_Output
![AgriAssist_Output](https://github.com/ValiShaik03/AgriBot/blob/98163f148728a9cf4d9e7e62d793d8694c1e5db7/output/output2.png)

## **Acknowledgements**

We would like to express our gratitude to the following:

- OpenAI for providing powerful language models that enable context-aware responses.

- LangChain and langchain-community for their seamless tools for document embeddings and RAG workflows.

- DuckDuckGo and SerpAPI for allowing us to integrate live web search capabilities to fetch up-to-date agricultural information.

- Streamlit for providing an intuitive and interactive framework to build the web application.

- Agricultural experts and online resources that inspired the content structure and best practices incorporated in AgriAssist.
