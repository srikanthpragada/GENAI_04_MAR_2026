from huggingface_hub import InferenceClient
from langchain_core.prompts import PromptTemplate
import keys
 
model_id = "openai/gpt-oss-120b"
client = InferenceClient(model=model_id, 
                         token= keys.HUGGINGFACE_KEY)

text = "Check whether a number is perfect number or not"
prompt = f"""Just give me a Python function for the following task and give no more details:
{text}
"""
messages = [{"role": "user", "content": prompt}]

response = client.chat_completion(messages)
reply = response.choices[0].message.content
print(reply)
