from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

# Create the agent
memory = InMemorySaver()
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

search = TavilySearch(max_results=2)
tools = [search]

llm_with_tools = model.bind_tools(tools)

sys_msg = SystemMessage(
    content="Use either tools to perform arithmetic on a set of inputs or just give me answer with your knowledge")


def assistant(state: MessagesState):
   return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# Graph
builder = StateGraph(MessagesState)

# Define nodes: these do the work
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Define edges: these determine how the control flow moves
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")
builder.add_edge("assistant", END)

memory = InMemorySaver()
react_graph = builder.compile(checkpointer=memory)

# thread is identifies the session 
config = {"configurable": {"thread_id": "1"}}

human_message = HumanMessage("Hi, I'm Srikanth and I live in Visakhapatnam.")
response = react_graph.invoke({"messages": [human_message]}, config=config)

human_message = HumanMessage("Search for the weather where I live")
response = react_graph.invoke({"messages": [human_message]}, config=config)

for message in response["messages"]:
    message.pretty_print()