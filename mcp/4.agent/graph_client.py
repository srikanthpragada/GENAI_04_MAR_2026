from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition
import asyncio 


from langchain.chat_models import init_chat_model
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

client = MultiServerMCPClient(
    {
        "mathserver": {
            "url": "http://localhost:9999/mcp",
            "transport": "streamable_http",
        }
    }
)



async def process():
    tools = await client.get_tools()

    def call_model(state: MessagesState):
        response = model.bind_tools(tools).invoke(state["messages"])
        return {"messages": response}
    
    builder = StateGraph(MessagesState)
    builder.add_node(call_model)
    builder.add_node(ToolNode(tools))
    builder.add_edge(START, "call_model")
    builder.add_conditional_edges(
        "call_model",
        tools_condition,
    )
    builder.add_edge("tools", "call_model")
    graph = builder.compile()
    response = await graph.ainvoke({"messages": "Is 38364323 a prime number?"})
    for message in response['messages']:
        message.pretty_print()


asyncio.run(process())