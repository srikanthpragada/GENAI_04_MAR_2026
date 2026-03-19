from langchain_huggingface import HuggingFaceEndpointEmbeddings
import keys 

# 1. Access Embedding Model
embeddings_model = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    #huggingfacehub_api_token= keys.HUGGINGFACEKEY
)

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


# 2. Sample Data 
documents = [
    Document(page_content="LangChain is a framework."),
    Document(page_content="Ollama allows running LLMs locally."),
    Document(page_content="Manchester City is doing awesome!"),
    Document(page_content="Bill Gates Founded Microsoft"),
    Document(page_content="Real Madrid won UEFA Champions League 13 times.")
]

# 3. Create FAISS index from documents using the given embeddings model
vectorstore = FAISS.from_documents(documents, embeddings_model)

# 4. Perform a similarity search
query = "Football"
results = vectorstore.similarity_search(query, k=2)  # Get the top 2 results

# 5. Print the results
for doc in results:
    print(doc.page_content)
    print('-' * 50)


 

