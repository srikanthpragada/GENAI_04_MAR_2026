from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
model = init_chat_model("gpt-4o-mini",
                        model_provider="openai",
                        temperature=0.9,
                        max_tokens=200)
response = model.invoke(
      [HumanMessage(content="Write a short story about Moon")])
print(response.content)
