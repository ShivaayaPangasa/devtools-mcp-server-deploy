# devtools-mcp-server

Python MCP server exposing developer utilities to Claude Desktop. Includes a code snippet sharer backed by MongoDB.

## Structure

```
devtools-mcp-server/
├── server/
│   ├── main.py          # MCP server entry point, register tools here
│   └── gemini.py        # Gemini API wrapper stub
├── snippets/
│   ├── app.py           # Flask backend for snippet storage and retrieval
│   └── frontend/
│       └── index.html   # Snippet viewer page
├── .env.example
├── claude_desktop_config.example.json
└── requirements.txt
```

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Fill in your GEMINI_API_KEY and MONGO_URI in .env
```

## Run the MCP server

```bash
python server/main.py
```

## Run the snippet server

```bash
python snippets/app.py
```

## Register with Claude Desktop

Copy `claude_desktop_config.example.json` into your Claude Desktop config at:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Update the path and API key, then restart Claude Desktop.

## Contributing

- Add new MCP tools in `server/main.py` (see TODO comments)
- Replace in-memory snippet store in `snippets/app.py` with MongoDB
- Wire up real Gemini calls in `server/gemini.py`
- Open a PR for each tool or feature — one thing per PR
