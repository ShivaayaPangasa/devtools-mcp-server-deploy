"""
gemini.py
---------
Stub for Gemini API calls. Interns: replace the placeholder response
with real google-generativeai SDK calls.
"""

import os

# from google import generativeai as genai  # uncomment when ready
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini(prompt: str) -> str:
    """
    Send a prompt to Gemini and return the response text.
    Currently returns a stub response.
    """
    # TODO: Replace with real Gemini call
    # model = genai.GenerativeModel("gemini-pro")
    # response = model.generate_content(prompt)
    # return response.text

    return f"[Gemini stub] Received: {prompt}"
