from huggingface_hub import InferenceClient
import keys

model_id = "openai/gpt-oss-120b"
client = InferenceClient(model=model_id, api_key=keys.HUGGINGFACE_KEY)

messages = [
    {"role": "user", "content": "What is the capital of France?"}
]

response = client.chat_completion(messages)
# print(response)
print(response.choices[0].message.content)
