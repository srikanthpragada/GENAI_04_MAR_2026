from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Math Server")


# Add an addition tool
@mcp.tool()
def isPrime(num : int) -> bool:
    """Checks whether a number is prime or not"""
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True 

@mcp.tool()
def isPerfect(num : int) -> bool:
    """Checks whether a number is perfect or not"""
    total = 1
    for i in range(2, num//2 + 1):
        if num % i == 0:
            total += i
    
    return total == num 
 

if __name__ == '__main__':  
    mcp.run(transport="http", port=9999)