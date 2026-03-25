from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
import json 


@tool()
def search(name : str) -> list[dict]:
    """Search for a product with the given name and return details as list[dict]

    Args:
        name : str
    """
    with open("products.json", "rt") as f:
         products = json.load(f)
    
    # search
    selected_products = []
    for product in products:
         if name.lower() in product['name'].lower():
              selected_products.append(product)

    return selected_products

 

# Create the agent with tools
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
tools = [search]

agent = create_agent(model, tools)

human_message = HumanMessage("Get me prices of all mouse")

# Invoke agent
response = agent.invoke({"messages": [human_message]})

for message in response['messages']:
    message.pretty_print()
