import sys
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
import asyncio


clients = MultiServerMCPClient(
    {"Todos Server": {
        "url": "http://localhost:9999/mcp",
        "transport": "streamable_http"},
    }
)

system_message = SystemMessage(content = 
  """You are a very helpful todos assitant. 
  Filter or classify todos retrieved from a tool based on the user requirement whenever needed. 
  Display output as bullets and display as much information as possible for each todo
  """)

async def process():
    tools = await clients.get_tools()
    model = init_chat_model("gemini-2.5-flash", model_provider="google-genai")
    checkpointer = InMemorySaver()
    agent = create_agent(model, tools, checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "1"}}
    
    # human_message = HumanMessage("Add todo - Complete Deep Learning Material - importance high")
    # response = await agent.ainvoke( {"messages" : [system_message, human_message] },
    #                                 config = config)
    # print(response["messages"][-1].content)

    response = await agent.ainvoke(
        {"messages": "List all todos with high importance as bullets"}, config = config)
    
    for m in response["messages"]:
        m.pretty_print()

    # response = await agent.ainvoke({"messages": "List all todos and their importance as bullets"}, config = config)
    # print(response["messages"][-1].content)

    # human_message = HumanMessage("Show me todos related to book")
    # response = await agent.ainvoke( {"messages" : [system_message, human_message]}, config = config)
    # print(response["messages"][-1].content)

    # human_message = HumanMessage("Show 2 recently added todos")
    # response = await agent.ainvoke({"messages": [system_message, human_message]}, config = config)
    # print(response["messages"][-1].content)

    # human_message = HumanMessage("Get all todos and classify each todo as Finance, Sports, Books and others")
    # response = await agent.ainvoke({"messages": [system_message, human_message]}, config = config)
    # print(response["messages"][-1].content)

    # human_message = HumanMessage("Delete todos related to Java")
    # response = await agent.ainvoke({"messages": [system_message, human_message]}, config = config)
    # print(response["messages"][-1].content)

    # human_message = HumanMessage("Show todos related to book with high importance")
    # response = await agent.ainvoke( {"messages" : [system_message, human_message]}, config)
    # print(response["messages"][-1].content)

    # human_message = HumanMessage("Can you summarize all my todos")
    # response = await agent.ainvoke( {"messages" : [system_message, human_message]}, config)
    # print(response["messages"][-1].content)

    # human_message = HumanMessage("complete todos related to office")
    # response = await agent.ainvoke({"messages": [system_message, human_message]}, config)
    # print(response["messages"][-1].content)

    # human_message = HumanMessage("list all completed todos")
    # response = await agent.ainvoke({"messages": [system_message, human_message]}, config)
    # print(response["messages"][-1].content)

    # human_message = HumanMessage(
    #     "get all completed todos and display only the ones on MCP")
    # response = await agent.ainvoke({"messages": [system_message, human_message]}, config)
    # print(response["messages"][-1].content)

    # human_message = HumanMessage("Count how many todos are there")
    # response = await agent.ainvoke({"messages": [system_message, human_message]}, config)
    # print(response["messages"][-1].content)

asyncio.run(process())
