"""
DevTools MCP Server
-------------------
Boilerplate entry point. Registers a basic MCP server with one hello-world tool.
Interns: add new tools in this file or split into separate modules under server/.
"""

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import asyncio

app = Server("devtools-mcp")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="hello_devtools",
            description="A placeholder tool. Replace this with real dev tools.",
            inputSchema={
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Any message to echo back."
                    }
                },
                "required": ["message"]
            }
        ),
        # TODO: add run_shell_command tool
        # TODO: add read_file tool
        # TODO: add write_file tool
        # TODO: add list_directory tool
        # TODO: add search_in_files tool
        # TODO: add git_status tool
        # TODO: add read_env_file tool
        # TODO: add check_port tool
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "hello_devtools":
        msg = arguments.get("message", "")
        return [TextContent(type="text", text=f"DevTools MCP says: {msg}")]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
