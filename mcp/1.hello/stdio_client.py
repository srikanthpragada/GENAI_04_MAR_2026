import asyncio
from fastmcp import Client

client = Client("stdio_server.py")

async def get_message(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result.content[0].text)

asyncio.run(get_message("Srikanth"))