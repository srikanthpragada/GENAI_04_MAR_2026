from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage

llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")


@tool()
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b


tools = [add]
llm_with_tools = llm.bind_tools(tools)

#query = "What is 11 + 49?"
query = "What is the capital of Australia?"

messages = [SystemMessage('You can use tools when necessary, but otherwise answer the question using your own knowledge.'),
            HumanMessage(query)]

ai_msg = llm_with_tools.invoke(messages)
#print(ai_msg)

# Add AI message to messages
messages.append(ai_msg)

# call tool selected by LLM
if len(ai_msg.tool_calls) > 0:
    #print(ai_msg)
    # If tool call is present then call the tool and pass response to llm
    tool_call = ai_msg.tool_calls[-1]
    selected_tool = eval(tool_call['name'])  # Get function name to call 

    # call the tool with required arguments provided by LLM in tool_call 
    tool_msg = selected_tool.invoke(tool_call)
    messages.append(tool_msg)  # ToolMessage 

    # Provide answer from tool back to LLM
    ai_message = llm_with_tools.invoke(messages)
    messages.append(ai_message)


for message in messages:
    message.pretty_print()
