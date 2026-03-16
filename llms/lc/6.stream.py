# Set environment variable GOOGLE_API_KEY to Google key.

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
response = model.stream("Who is Van Rossum?")

for chunk in response:
    print(chunk.content, end = "\n--------------\n")
