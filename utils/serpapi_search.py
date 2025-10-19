from serpapi import GoogleSearch
import os

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

def serpapi_search(query, num_results=3):
    """
    Perform live web search using SerpAPI (Google Search).
    Returns top results as summarized text.
    """
    if not SERPAPI_API_KEY:
        return "⚠️ SerpAPI key not found. Please set SERPAPI_API_KEY in .env"

    try:
        params = {
            "engine": "google",
            "q": query,
            "num": num_results,
            "api_key": SERPAPI_API_KEY
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        snippets = []
        for r in results.get("organic_results", []):
            title = r.get("title", "")
            snippet = r.get("snippet", "")
            url = r.get("link", "")
            snippets.append(f"{title}: {snippet} ({url})")

        if snippets:
            return "\n\n".join(snippets)
        else:
            return "⚠️ No relevant results found from live search."

    except Exception as e:
        return f"⚠️ SerpAPI search error: {e}"
