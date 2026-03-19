from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts.prompt import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chat_models import init_chat_model
import streamlit as st 
import os 

loader = PyPDFLoader(
    r"../docs/courses_offered.pdf",
    mode="page")

docs = loader.load()

# Split docs into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100)

chunks = splitter.split_documents(docs)

# Embeddings model and LLM 
embeddings_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001")
llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")


folder_path = "./courses_vectors"

if os.path.exists(folder_path):
    db = FAISS.load_local(folder_path, embeddings_model,
                          allow_dangerous_deserialization=True)
    print("Loaded FAISS index")
else:
    db = FAISS.from_documents(chunks, embeddings_model)
    print('Created FAISS index')
    db.save_local(folder_path)

prompt_template = """:
Consider the following context and give a short answer for the given question.
Context : {context}
Question:{question}
"""

prompt  = PromptTemplate.from_template(prompt_template)

retriever = db.as_retriever()


st.title("Courses RAG Demo")
query = st.text_input("Enter your query :",  autocomplete = 'false')
   
if len(query) > 0:
    results = retriever.invoke(query)
    matching_docs_str = "\n".join([doc.page_content for doc in results])
    final_prompt = prompt.format(context=matching_docs_str, question=query)
    result =  llm.invoke(final_prompt)
    st.write(result.content)

    