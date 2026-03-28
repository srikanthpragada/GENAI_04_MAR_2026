# pip install langchain-mcp-adapters

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
import os

# Get key from environment variable
tavily_key = os.getenv("TAVILY_API_KEY")


clients = MultiServerMCPClient(
    {"Tavily": {
    "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavily_key}",
    "transport": "streamable_http"}
})

async def process():
        tools = await clients.get_tools()
        for tool in tools:
                print(tool.name)

        print('-' * 50)
        
        model = init_chat_model("gpt-5-nano", model_provider="openai")
        #model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
        agent = create_agent(model, tools)
        response = await agent.ainvoke({"messages": "Who won IPL 2025? Just give team name."})

        for message in response["messages"]:
                message.pretty_print()


asyncio.run(process())
