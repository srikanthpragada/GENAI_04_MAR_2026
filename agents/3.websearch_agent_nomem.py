# install pacakge using  pip install langchain-tavily
# set environment variable - TAVILY_API_KEY 

from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage 

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
search = TavilySearch(max_results=2)
tools = [search]

agent  = create_agent(model, tools)
human_message = HumanMessage("Hi, I'm Srikanth and I live in Visakhapatnam.")
response = agent.invoke({"messages": [human_message]})

for message in response["messages"]:
    message.pretty_print()


human_message = HumanMessage("Search for the weather where I live")
response = agent.invoke({"messages": [human_message]})

for message in response["messages"]:
    message.pretty_print()