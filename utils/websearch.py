import requests

def duckduckgo_search(query):
    """
    Perform simple web search using DuckDuckGo public API.
    Returns summarized text data.
    """
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        res = requests.get(url)
        data = res.json()
        results = []

        if "AbstractText" in data and data["AbstractText"]:
            results.append(data["AbstractText"])

        for topic in data.get("RelatedTopics", []):
            if isinstance(topic, dict) and "Text" in topic:
                results.append(topic["Text"])

        if results:
            return " ".join(results)[:2000]
        else:
            return "No relevant results found."
    except Exception as e:
        return f"Web search error: {e}"
