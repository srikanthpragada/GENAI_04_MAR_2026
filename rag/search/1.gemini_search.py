from google import genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

docs = [
    Document(page_content="AI is transforming the world."),
    Document(page_content="Machine learning enables data-driven predictions."),
    Document(page_content="Deep learning uses neural networks."),
    Document(page_content="AWS is cloud platform"),
    Document(page_content="Deep Learning is used in Generative AI"),
]

vectorstore = FAISS.from_documents(docs, embeddings_model)

query = "What uses neural networks?"
results = vectorstore.similarity_search(query, k=2)


for i, doc in enumerate(results, start=1):
    print(f"Result {i}: {doc.page_content}")
 
