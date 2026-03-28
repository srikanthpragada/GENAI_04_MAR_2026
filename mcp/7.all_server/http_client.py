from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
import asyncio

# Basic connection
transport = StreamableHttpTransport(url="http://localhost:9999/mcp")
client = Client(transport)

async def call_tool():
    async with client:
        # List available tools from the server
        tools = await client.list_tools() 
        print("Available tools:")
        for t in tools:
            print(t.name)

        resources = await client.list_resources() 
        print("Available Static Resources:")
        for resource in resources:
            print(resource.uri)

        resources = await client.list_resource_templates()
        print("Available Template Resources:")
        for resource in resources:
            print(resource.uriTemplate)

        # Call add
        result = await client.call_tool("add", {"a": 5, "b": 7})
        print("Result of add(5, 7):", result.content[0].text)

        # Call resource 
        result = await client.read_resource("resource://greeting/Srikanth")
        print(result[0].text)

        # Call resource 
        result = await client.read_resource("resource://today")
        print(result[0].text)


asyncio.run(call_tool())