# Load documents from PDF and split them

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.pdf import PyPDFLoader

# Load the PDF file
loader = PyPDFLoader("./docs/courses_offered.pdf", mode='single')

# Load the documents
docs = loader.load()
print("Loaded Documents", len(docs))

text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=200,
      chunk_overlap=20)

chunks = text_splitter.split_documents(docs)
print('Chunks Count :', len(chunks))
