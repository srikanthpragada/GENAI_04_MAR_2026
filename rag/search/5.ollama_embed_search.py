from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# 1. Initialize OllamaEmbeddings
embeddings_model = OllamaEmbeddings(model="nomic-embed-text:latest")  

# 2. Sample Data 
documents = [
    Document(page_content="LangChain is a framework."),
    Document(page_content="Ollama allows running LLMs locally."),
    Document(page_content="FAISS is for similarity search."),
    Document(page_content="Bill Gates Founded Microsoft"),
    Document(page_content="Real Madrid won UEFA Champions League 13 times.")
]

# 3. Create FAISS index from documents
vectorstore = FAISS.from_documents(documents, embeddings_model)

# 4. Perform a similarity search
query = "Did real madrid win champions league?"
results = vectorstore.similarity_search(query, k=2)  # Get the top 2 results

# 5. Print the results
for docs in results:
    print(docs.page_content)
    print("-"  * 80)
 

