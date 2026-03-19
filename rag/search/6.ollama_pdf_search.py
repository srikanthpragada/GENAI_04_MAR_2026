from langchain_community.vectorstores import FAISS  
import re 
from langchain_ollama import OllamaEmbeddings   
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("./docs/courses_offered.pdf")
docs = loader.load()
print("Loaded documents", len(docs))
 
embeddings_model  =  OllamaEmbeddings(model="nomic-embed-text:latest")
db = FAISS.from_documents(docs,embeddings_model)
               

retrieved_results = db.similarity_search("Python", k = 3)
print(f"Matching documents count : {len(retrieved_results)}")

for result in retrieved_results:
    print(result.page_content[:50])
    print("-" * 50)
    


