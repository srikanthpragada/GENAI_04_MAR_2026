from fastmcp import FastMCP
from datetime import datetime 

# Create an MCP server
mcp = FastMCP("MCP Server")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add an multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# Template Resource
@mcp.resource("resource://greeting/{name}", name= 'greeting')
def get_greeting(name : str) -> str:
    """Provides a simple greeting message."""
    return f"Hello {name}, welcome to MCP Server Resource"

# Static Resource
@mcp.resource("resource://today", name='today')
def get_today() -> str:
    """Provides system date"""
    return f"Today is {datetime.now()}"

 

if __name__ == '__main__':
    mcp.run(transport="http", port=9999)