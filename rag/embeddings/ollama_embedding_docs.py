from langchain_ollama import OllamaEmbeddings
embeddings_model = OllamaEmbeddings(model="nomic-embed-text:latest")

embeddings = embeddings_model.embed_documents(
    [
        "This is beautiful",
        "That soup was awful",
        "Your hair looks great",
        "I work for 9 to 10 hours a day",
        "I love football and swimming"
    ]
)

print(len(embeddings), len(embeddings[0]))
print(embeddings[0][:10])  

