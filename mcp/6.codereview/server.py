from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("File Server")


# Load contents of the file 
@mcp.tool()
def read_from_file(directory : str, filename : str) -> str | None:
    """Reads the contents of the given file from the given directory"""

    print('read_from_file', directory, filename)
    fullpath = f"{directory}\\{filename}"
    try:
        with open(fullpath, "rt") as f:
             return f.read()
    except:
        return None


@mcp.tool()
def write_to_file(directory: str, filename: str, content : str) -> bool:
    """Writes the contents to the given file"""
    print('write_to_file', directory, filename)
    fullpath = f"{directory}\\{filename}"
    try:
        with open(fullpath, "wt") as f:
           f.write(content)

        return True 
    except:
        return False

if __name__ == '__main__':
    mcp.run(transport="http", port=9999)
