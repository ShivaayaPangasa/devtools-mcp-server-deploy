"""
snippets/app.py
---------------
Minimal Flask app for the code snippet sharer.
Interns: wire up MongoDB, add real POST /snippets and GET /snippets/<slug> routes.
"""

from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# In-memory store — replace with MongoDB
_snippets = {}


@app.get("/")
def index():
    return jsonify({"status": "Snippet server running"})


@app.post("/snippets")
def create_snippet():
    """
    Accepts: { "code": "...", "language": "python" }
    Returns: { "slug": "abc123", "url": "http://localhost:5000/s/abc123" }
    TODO: Save to MongoDB with TTL index instead of in-memory dict.
    TODO: Call Gemini to generate a short summary before saving.
    """
    data = request.get_json()
    slug = uuid.uuid4().hex[:8]
    _snippets[slug] = {
        "code": data.get("code", ""),
        "language": data.get("language", "text"),
        "summary": "[Gemini summary coming soon]",
    }
    url = f"http://localhost:5000/s/{slug}"
    return jsonify({"slug": slug, "url": url}), 201


@app.get("/s/<slug>")
def view_snippet(slug):
    """
    Returns snippet data for the frontend viewer to render.
    TODO: Check TTL / expiry before returning.
    """
    snippet = _snippets.get(slug)
    if not snippet:
        return jsonify({"error": "Snippet not found or expired"}), 404
    return jsonify(snippet)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
