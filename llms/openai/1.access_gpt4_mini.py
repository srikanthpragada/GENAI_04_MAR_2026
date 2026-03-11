# Create key using https://platform.openai.com/api-keys
# Set environment variable OPENAI_API_KEY to OpenAI key.


from openai import OpenAI

client = OpenAI()
#client = OpenAI(api_key="")

response = client.responses.create(
    model="gpt-5-nano",
    input="What is the capital of Spain?"
)

#print(response)
print(response.output_text)
