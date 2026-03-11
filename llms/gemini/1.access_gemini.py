# Create key using https://aistudio.google.com/apikey
# Set environment variable GOOGLE_API_KEY to Gemini API key

from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="List names of 5 important cities in India"
)

print(response.text)
