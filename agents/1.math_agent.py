from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

@tool()
def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

@tool()
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

@tool()
def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a // b


# Create the agent with tools 
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
tools = [add, multiply, divide]

agent = create_agent(model, tools)

human_message = HumanMessage("What is 10 + 5 * 20")
#human_message = HumanMessage("Which are 5 best cities in India. Just give names.")
 
#Invoke agent 
response = agent.invoke({"messages": [human_message]})

for message in response['messages']:
    message.pretty_print()
