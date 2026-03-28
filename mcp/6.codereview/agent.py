from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
import asyncio

clients = MultiServerMCPClient(
    {"File Server": {
        "url": "http://localhost:9999/mcp",
        "transport": "streamable_http"},
    }
)

system_message = SystemMessage(
    content=
    """You are a code reviewer. 
    Review the code and write your suggestions to file with same primary filename and .review extension 
    Use folder is c:\\classroom\\feb14 by default unless specified otherwise
    """)

async def process():
    tools = await clients.get_tools()
    model = init_chat_model("gpt-4o-mini", model_provider="openai")
    agent = create_agent(model, tools)
    human_message = HumanMessage(
        content="Review the code in 1.math_agent.py in c:\\classroom\\feb14\\agents folder")
    response = await agent.ainvoke(
        {"messages": [system_message, human_message]})
    #print(response["messages"][-1].content)

    for message in response['messages']:
        message.pretty_print()


asyncio.run(process())
