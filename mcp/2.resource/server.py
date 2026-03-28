from fastmcp import FastMCP
from datetime import datetime

# Create an MCP server
mcp = FastMCP("Resource Server")

# Template Resource 
@mcp.resource("resource://greeting/{name}")
def get_greeting(name : str) -> str:
    """Provides a simple greeting message."""
    return f"Hello {name}, welcome to MCP Server Resources"

# Static Resource
@mcp.resource("resource://today", name='today')
def get_today() -> str:
    """Provides system date and time"""
    return f"Today is {datetime.now()}"

if __name__ == '__main__':
    mcp.run(transport="http", port=9999)