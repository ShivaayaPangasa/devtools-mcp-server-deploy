from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from server.database import snippets_collection

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home():
    return {"message": "DevTools MCP Snippet API Running"}


@app.get("/snippet/{slug}")
def get_snippet(slug: str):

    snippet = snippets_collection.find_one(
        {"slug": slug},
        {"_id": 0}
    )

    if not snippet:
        return {"error": "Snippet not found"}

    return snippet

@app.get("/view/{slug}")
def view_snippet(request: Request, slug: str):

    snippet = snippets_collection.find_one(
        {"slug": slug},
        {"_id": 0}
    )

    if not snippet:
        return {"error": "Snippet not found"}

    return templates.TemplateResponse(
        request=request,
        name="snippet.html",
        context={
            "snippet": snippet
        }
    )