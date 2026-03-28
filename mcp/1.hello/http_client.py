import asyncio
from fastmcp import Client

client = Client("http://localhost:9999/mcp")

async def sayhello(name: str):
   async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result.content[0].text)

 

asyncio.run(sayhello("Srikanth"))
 
