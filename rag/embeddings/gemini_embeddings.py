from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

embeddings_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

docs = [
    Document(page_content="AI is transforming the world."),
    Document(page_content="Machine learning enables data-driven predictions."),
    Document(page_content="Deep learning uses neural networks."),
]

embeddings = embeddings_model.embed_documents([doc.page_content for doc in docs])
print(len(embeddings), len(embeddings[0]))
print(embeddings[0][:10])

