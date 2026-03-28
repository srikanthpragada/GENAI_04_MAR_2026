# pip install langchain-mcp-adapters

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.messages import HumanMessage
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import asyncio

clients = MultiServerMCPClient(
    {"Math Server": {
        "url": "http://localhost:9999/mcp",
        "transport": "streamable_http"},
     "File Server:": {
        "command": "python",
        "args": ["./file_server.py"],
        "transport": "stdio"
    }
    }
)


async def process():
    tools = await clients.get_tools()
    for tool in tools:
        print(tool.name)

    model = init_chat_model("gemini-2.5-flash", model_provider="google-genai")
    #model = init_chat_model("gpt-4.1-nano", model_provider="openai")
    agent = create_agent(model, tools)
    human_message = HumanMessage("is 383843 a prime number?")
    response = await agent.ainvoke({"messages": [human_message] })
    
    for message in response['messages']:
        message.pretty_print()

  
    human_message = HumanMessage("Get contents of test.txt file")
    file_response = await agent.ainvoke({"messages": [human_message]})
    #print(file_response["messages"][-1].content)
    
    for msg in file_response['messages']:
        msg.pretty_print()


asyncio.run(process())
