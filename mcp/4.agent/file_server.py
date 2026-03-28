from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("File Server")


# Load contents of the file
@mcp.tool()
def read_file(filename: str) -> str | None:
    """Reads the contents of the given file"""
    try:
        with open(filename, "rt") as f:
            return f.read()
    except:
        return None


mcp.run(transport="stdio")
