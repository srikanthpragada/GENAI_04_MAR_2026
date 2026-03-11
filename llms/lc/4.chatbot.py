# Set environment variable GOOGLE_API_KEY to Google key.

from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

messages = [SystemMessage(content="Give one line answer")]

while True:
    prompt = input("Enter prompt [q to quit, c to create new chat] :")
    if prompt.lower() == 'q':
        break
    # Alternatively you can create HumanMessage
    # messages.append( {"role" : "user", "content" : prompt})
    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    print(response.content)
    # Alternatively you can use response as AIMessage
    # messages.append( {"role" : "assistant", "content" : response.content})
    messages.append(response) # AIMessage
