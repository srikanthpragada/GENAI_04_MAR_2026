from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

@tool(description='Get weather for the given location')
def GetWeather(location: str) -> str:
    return f"The weather in {location} is sunny."

@tool(description='Get population for the given location')
def GetPopulation(location: str) -> str:
    return f"The population of {location} is 1 million."

gemini = init_chat_model(
    "gemini-2.5-flash", model_provider="google_genai", temperature=0
)

tools = [GetWeather, GetPopulation]
agent = create_agent(model = gemini, tools = tools,
                     system_prompt="You are a helpful assistant")

response = agent.invoke(
    {"messages":  [HumanMessage("What's the weather in Vizag and its population?")]}
)

for msg in response["messages"]:
    msg.pretty_print()