import asyncio
import streamlit as st
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

# Initialize MCP client
clients = MultiServerMCPClient(
    {"Todos Server": {
        "url": "http://localhost:9999/mcp",
        "transport": "streamable_http"},
     }
)

system_message = SystemMessage(content="""You are a very helpful todos assitant. 
  Filter or classify todos retrieved from a tool based on the user requirement whenever needed. 
  Display output as bullets and display as much information as possible for each todo
  """)


async def run_agent(user_input : str) -> str:
    tools = await clients.get_tools()
    model = init_chat_model("gpt-4.1-nano",model_provider="openai")
    agent = create_agent(model, tools)
    human_message = HumanMessage(user_input)
    response = await agent.ainvoke({"messages": [system_message, human_message]})
    return response["messages"][-1].content


# Streamlit App UI
st.title("Todos Agent")
st.write("Interact with your MCP-enabled AI Todo Agent")

with st.form(key="agent_form"):
    user_input = st.text_area("Enter your message to the assistant:",
                              "", height=100)
    submitted = st.form_submit_button("Send")

if submitted:
    if user_input.strip():
        with st.spinner("Processing..."):
            try:
                response = asyncio.run(run_agent(user_input))
                st.subheader("Agent Response:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message to send to the assistant.")
