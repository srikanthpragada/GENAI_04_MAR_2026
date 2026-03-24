from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_core.messages import SystemMessage, ToolMessage, AIMessage, HumanMessage


@tool
def get_weather(location: str) -> str:
    """ 
    Gets weather in the given location
    """
    return "Sunny with 31C"


@tool
def get_population(location: str) -> str:
    """
    Gets population in the given location
    """
    return "1 million."


gemini = init_chat_model(
    "gemini-2.5-flash", model_provider="google_genai", temperature=0
)

messages = [
    SystemMessage(
        'You can use tools when necessary, but otherwise answer the question using your own knowledge.'
    ),
   #HumanMessage(content="What is the capital of India")
   HumanMessage(content="What is the weather in Vizag and its population")
]

gemini_with_tools = gemini.bind_tools([get_weather, get_population])

while True:
    ai_msg = gemini_with_tools.invoke(messages)
    # Add AI message to messages
    messages.append(ai_msg)

    # Terminate loop if no tool is to be called
    if len(ai_msg.tool_calls) == 0:
        break

    # call tool selected by LLM
    for tool_call in ai_msg.tool_calls:
        selected_tool = eval(tool_call["name"])
        tool_result = selected_tool.invoke(tool_call)
        messages.append(tool_result)


for message in messages:
    message.pretty_print()
