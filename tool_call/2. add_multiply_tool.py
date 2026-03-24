from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")


@tool()
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b


@tool()
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a * b

tools = [add, multiply]
llm_with_tools = llm.bind_tools(tools)

query = "Add 10 and 20 and then multiply it with 40"
#query = "Add 10 and 20, multiply 20 and 40"
#query = "What is the capital of Spain"


messages = [
    SystemMessage(
        "You can use tools when necessary, but otherwise answer the user using your own knowledge."
    ),
    HumanMessage(query),
]

while True:
    ai_msg = llm_with_tools.invoke(messages)
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

