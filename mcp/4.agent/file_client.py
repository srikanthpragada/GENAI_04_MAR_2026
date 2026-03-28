from fastmcp import Client
import asyncio

# Connect to the Add Server using STDIO transport
client = Client('file_server.py')

async def call_tool():
    async with client:
        result = await client.call_tool("read_file", { "filename" : "test.txt"})
        if len(result.content) > 0:
            print(result.content[0].text)
        else:
            print('Sorry! Could not read file!')



asyncio.run(call_tool())

