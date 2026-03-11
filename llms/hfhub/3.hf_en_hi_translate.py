from huggingface_hub import InferenceClient
import keys

model_id = "Helsinki-NLP/opus-mt-en-hi"   
client = InferenceClient(model=model_id, token= keys.HUGGINGFACE_KEY)

english_text = "What did you learn about AI today?"
response = client.translation(english_text)

print(f"Hindi: {response.translation_text}")
