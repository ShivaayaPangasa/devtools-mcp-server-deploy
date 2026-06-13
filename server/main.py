from mcp.server.fastmcp import FastMCP
import subprocess
import os
import re
import socket
from dotenv import dotenv_values
from snippet_service import save_snippet

# -----------------------------
# FORCE PROJECT WORKING DIRECTORY
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

mcp = FastMCP("DevTools MCP Server")

# -----------------------------
# HELLO TOOL
# -----------------------------
@mcp.tool()
def hello():
    return "Hello from DevTools MCP Server!"


# -----------------------------
# SHELL COMMAND TOOL
# -----------------------------
@mcp.tool()
def run_shell(command: str):

    """
    Run shell command and return stdout/stderr.
    """

    try:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=15
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }

    except Exception as e:
        return str(e)


# -----------------------------
# READ FILE TOOL
# -----------------------------
@mcp.tool()
def read_file(path: str):

    """
    Read file contents.
    """

    try:

        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    except Exception as e:
        return str(e)


# -----------------------------
# WRITE FILE TOOL
# -----------------------------
@mcp.tool()
def write_file(path: str, content: str):

    """
    Write content to file.
    """

    try:

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return "File written successfully."

    except Exception as e:
        return str(e)


# -----------------------------
# LIST DIRECTORY TOOL
# -----------------------------
@mcp.tool()
def list_directory(path: str):

    """
    Recursively list files in directory.
    """

    files = []

    try:

        for root, dirs, filenames in os.walk(path):

            for filename in filenames:

                full_path = os.path.join(root, filename)

                files.append(full_path)

        return files

    except Exception as e:
        return str(e)


# -----------------------------
# REGEX SEARCH TOOL
# -----------------------------
@mcp.tool()
def search_text(path: str, pattern: str):

    """
    Search text across files using regex.
    """

    matches = []

    try:

        for root, dirs, files in os.walk(path):

            for file in files:

                filepath = os.path.join(root, file)

                try:

                    with open(filepath, "r", encoding="utf-8") as f:

                        content = f.read()

                        if re.search(pattern, content):

                            matches.append(filepath)

                except:
                    pass

        return matches

    except Exception as e:
        return str(e)


# -----------------------------
# GIT STATUS TOOL
# -----------------------------
@mcp.tool()
def git_status():

    """
    Get git status.
    """

    try:

        result = subprocess.run(
            ["git", "status"],
            capture_output=True,
            text=True,
            timeout=10
        )

        return result.stdout

    except Exception as e:
        return str(e)


# -----------------------------
# GIT DIFF TOOL
# -----------------------------
@mcp.tool()
def git_diff():

    """
    Get git diff.
    """

    try:

        result = subprocess.run(
            ["git", "diff"],
            capture_output=True,
            text=True,
            timeout=10
        )

        return result.stdout

    except Exception as e:
        return str(e)


# -----------------------------
# GIT LOG TOOL
# -----------------------------
@mcp.tool()
def git_log():

    """
    Get git log.
    """

    try:

        result = subprocess.run(
            ["git", "log", "--oneline"],
            capture_output=True,
            text=True,
            timeout=10
        )

        return result.stdout

    except Exception as e:
        return str(e)


# -----------------------------
# READ ENV TOOL
# -----------------------------
@mcp.tool()
def read_env():

    """
    Read .env key-value pairs.
    """

    try:

        return dict(dotenv_values(".env"))

    except Exception as e:
        return str(e)


# -----------------------------
# TCP PORT CHECK TOOL
# -----------------------------
@mcp.tool()
def check_port(host: str, port: int):

    """
    Check if TCP port is open.
    """

    try:

        s = socket.socket()
        s.settimeout(5)

        result = s.connect_ex((host, port))

        s.close()

        if result == 0:
            return "Port is open"

        else:
            return "Port is closed"

    except Exception as e:
        return str(e)

# -----------------------------
# SHARE SNIPPET TOOL
# -----------------------------
@mcp.tool()
def share_snippet(code: str, language: str):

    """
    Save code snippet, generate AI summary,
    store in MongoDB, and return shareable URL.
    """

    try:

        slug = save_snippet(
            code=code,
            language=language
        )

        return {
            "message": "Snippet saved successfully",
            "slug": slug,
            "viewer_url": f"http://127.0.0.1:8000/view/{slug}"
        }

    except Exception as e:
        return str(e)
    
# -----------------------------
# MAIN
# -----------------------------
def main():

    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()