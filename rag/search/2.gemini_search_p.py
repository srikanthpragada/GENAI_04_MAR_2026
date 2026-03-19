from google import genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
import os 

embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

docs = [
    Document(page_content="AI is transforming the world."),
    Document(page_content="Machine learning enables data-driven predictions."),
    Document(page_content="Deep learning uses neural networks."),
    Document(page_content="AWS is super"),
]

# check whether vector store is present, load it if present otherwise create it
folder_path = "./vectors/gemini_vectors"
if os.path.exists(folder_path):
    db = FAISS.load_local(folder_path, embeddings_model,
                          allow_dangerous_deserialization=True)
    print("Loaded FAISS index")
else:
    db = FAISS.from_documents(docs, embeddings_model)
    print('Created FAISS index')
    db.save_local(folder_path)

query = "What uses neural networks?"
results = db.similarity_search(query, k=2)


for i, doc in enumerate(results, start=1):
    print(f"Result {i}: {doc.page_content}")
 
