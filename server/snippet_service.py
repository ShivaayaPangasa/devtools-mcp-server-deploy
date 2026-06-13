import secrets
from datetime import datetime

from database import snippets_collection
from gemini import ask_gemini


def generate_slug(length=8):
    return secrets.token_hex(length // 2)


def generate_summary(code: str):

    prompt = f"""
    Explain this code snippet briefly and clearly:

    {code}
    """

    return ask_gemini(prompt)


def save_snippet(code: str, language: str):

    slug = generate_slug()

    summary = generate_summary(code)

    snippet_document = {
        "slug": slug,
        "language": language,
        "code": code,
        "summary": summary,
        "created_at": datetime.utcnow()
    }

    snippets_collection.insert_one(snippet_document)

    return slug