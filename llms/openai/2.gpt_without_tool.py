from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="Who won womens Cricket world cup in 2025. Just give team name."
)

print(response.output_text)
