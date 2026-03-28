# pip install langchain-mcp-adapters
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain.chat_models import init_chat_model
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

clients = MultiServerMCPClient(
    {"Currency": {
        "url": "https://currency-mcp.wesbos.com/mcp",
        "transport": "streamable_http"}
     })


async def process():
    tools = await clients.get_tools()
    # model = init_chat_model("gpt-5-nano", model_provider="openai")
    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
    agent = create_agent(model, tools)

    response = await agent.ainvoke({"messages":
                                    [HumanMessage("Convert 1000 USD to INR")]})

    for message in response["messages"]:
        message.pretty_print()


asyncio.run(process())
