from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PyPDFLoader("./docs/courses_offered.pdf", mode='page')
docs = loader.load()
print("Loaded documents", len(docs))

# Split docs into chunks 
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, 
    chunk_overlap=50)

chunks = splitter.split_documents(docs)
print("No. of chunks :", len(chunks))

embeddings_model = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2')

db = FAISS.from_documents(chunks, embeddings_model)

retrieved_results = db.similarity_search("Python", k = 3)

for result in retrieved_results:
    print(result.page_content)
    print("-" * 50)
    


