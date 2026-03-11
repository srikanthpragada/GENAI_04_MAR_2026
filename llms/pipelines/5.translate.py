from transformers import pipeline

client = pipeline("translation",         
                       model="Helsinki-NLP/opus-mt-en-hi")

text = "How are you?"
hindi = client(text)
#print(hindi)
print(hindi[0]['translation_text'])



     