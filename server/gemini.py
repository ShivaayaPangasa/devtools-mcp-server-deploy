import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_gemini(prompt: str) -> str:
    """
    Local Llama-based inference using Ollama.
    Replaces Gemini API dependency while preserving workflow.
    """

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3.2:3b",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "")

    except Exception as e:
        return f"Local Llama Error: {str(e)}"