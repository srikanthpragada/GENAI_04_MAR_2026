# TAVILY_API_KEY env variable for Tavily
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

# Create the agent
memory = InMemorySaver()
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
search = TavilySearch(max_results=2)
tools = [search]

agent = create_agent(model, tools, checkpointer=memory)

# thread is identifies the session 
config = {"configurable": {"thread_id": "1"}}

human_message = HumanMessage("Hi, I'm Srikanth and I live in Visakhapatnam.")
response = agent.invoke({"messages": [human_message]}, config=config)

human_message = HumanMessage("Search for the weather where I live")
response = agent.invoke({"messages": [human_message]}, config=config)

for message in response["messages"]:
    message.pretty_print()