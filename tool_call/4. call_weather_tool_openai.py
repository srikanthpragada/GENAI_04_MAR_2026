# Program to show how LLM can call a tool based on the requirement
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, ToolMessage, AIMessage, HumanMessage
import requests
from langchain_core.tools import tool

@tool
def get_weather(latitude : float, longitude : float) -> dict:
    """function to return weather information based on latitude and longitude"""

    """This is a publically available API that returns the weather for a given location."""
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    )
    data = response.json()
    return data["current_weather"]


model = init_chat_model("gpt-4o-mini", model_provider="openai")

system_message = SystemMessage(
    "You are a helpful weather assistant.If needed, find out latitude and logitude then provide them to tool. "
)
user_message = HumanMessage("What is the weather in Chicago")
# user_message = HumanMessage("What is the capital of Australia")

messages = [system_message, user_message]

model_with_tools = model.bind_tools([get_weather])
response = model_with_tools.invoke(messages)

messages.append(response)  # Add model response (AIMessage)

# It only tells which tool is to be invoked to get the result. And
# it does NOT call the tool itself

if len(response.tool_calls) > 0:
    tool = response.tool_calls[0]  # get first tool to call
    chosen_function_name = tool["name"]
    chosen_function = eval(chosen_function_name)  # convert name to function
    # Call function with required args
    tool_result = chosen_function.invoke(tool)
    messages.append(tool_result)  # Add ToolMessage with results

    # Call LLM to get final result
    final_result = model_with_tools.invoke(messages)
    messages.append(final_result)


# print all messages
for message in messages:
    message.pretty_print()
