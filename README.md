# DevTools MCP Server

A local Python-based MCP (Model Context Protocol) server exposing developer utilities to Claude Desktop with AI-powered code snippet sharing, MongoDB storage, FastAPI hosting, and local Llama integration via Ollama.

---

## Features

### Developer Utilities

* Run shell commands
* Read files
* Write files
* List directory contents recursively
* Search text across files using regex
* Git status
* Git diff
* Git log
* Read `.env` variables
* Check open TCP ports

### Code Snippet Sharing

* Accept code snippets through MCP
* Generate AI-powered summaries using Llama 3.2
* Store snippets in MongoDB Atlas
* Generate unique public URLs
* Syntax-highlighted snippet viewer
* Copy-to-clipboard functionality
* Public FastAPI hosting

---

## Tech Stack

* Python
* MCP SDK
* FastMCP
* Ollama
* Llama 3.2 3B
* MongoDB Atlas
* FastAPI
* Jinja2
* Claude Desktop
* Render

---

## Project Structure

```text
devtools-mcp-server/
│
├── server/
│   ├── main.py
│   ├── api.py
│   ├── database.py
│   ├── snippet_service.py
│   └── gemini.py
│
├── templates/
│   └── snippet.html
│
├── .env
├── requirements.txt
└── README.md
```

---

## Environment Variables

Create a `.env` file:

```env
MONGO_URI=your_mongodb_connection_string
BASE_URL=http://127.0.0.1:8000
```

For deployment:

```env
BASE_URL=https://your-render-url.onrender.com
```

---

## Local Setup

### Clone Repository

```bash
git clone <repository-url>
cd devtools-mcp-server
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Install Ollama:

https://ollama.com

Pull model:

```bash
ollama pull llama3.2:3b
```

Start Ollama:

```bash
ollama serve
```

---

## Run MCP Server

```bash
python server/main.py
```

---

## Claude Desktop Configuration

Edit:

```text
%APPDATA%\Claude\claude_desktop_config.json
```

Example:

```json
{
  "mcpServers": {
    "devtools": {
      "command": "C:\\path\\to\\python.exe",
      "args": [
        "C:\\path\\to\\server\\main.py"
      ]
    }
  }
}
```

Restart Claude Desktop.

---

## Run FastAPI Viewer

```bash
uvicorn server.api:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## Example MCP Tool

```python
share_snippet(
    code="print('Hello World')",
    language="python"
)
```

Response:

```json
{
  "message": "Snippet saved successfully",
  "slug": "6580ca2b",
  "viewer_url": "https://your-url/view/6580ca2b"
}
```

---

## Deployment

Hosted using Render.

Start command:

```bash
uvicorn server.api:app --host 0.0.0.0 --port $PORT
```

Environment variables:

```env
MONGO_URI=...
BASE_URL=https://your-render-url.onrender.com
```

---

## Architecture

```text
Claude Desktop
      ↓
MCP Server
      ↓
DevTools Tools
      ↓
Ollama (Llama 3.2)
      ↓
MongoDB Atlas
      ↓
FastAPI Backend
      ↓
Public Snippet Viewer
```

---

## Status

Project Brief 01 Completed

* MCP Server
* Claude Desktop Integration
* Local Llama Integration
* MongoDB Storage
* FastAPI Backend
* Public Deployment
* Snippet Viewer
* AI Summaries

Author: Shivaaya Pangasa
Internship Project - DevLeds
