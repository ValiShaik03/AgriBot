import os
from openai import OpenAI
from config.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

class LLMQuotaError(Exception):
    """Custom exception for OpenAI quota exceeded"""
    pass

def generate_llm_response(query, context, mode="Concise"):
    """
    Generate an AI response using the given query and context.
    Raises LLMQuotaError if OpenAI quota is exceeded.
    """
    prompt = f"""
    You are AgriAssist — an AI agricultural advisor. 
    Use the following context to answer the user's query.

    Context:
    {context}

    Question: {query}

    Provide a {mode.lower()} and clear response. Start your answer with:
    🌿 AgriAssist’s Advice:
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        return response.choices[0].message.content

    except Exception as e:
        # Raise custom exception if quota exceeded
        if "insufficient_quota" in str(e).lower() or "429" in str(e):
            raise LLMQuotaError("OpenAI quota exceeded") from e
        else:
            raise e
