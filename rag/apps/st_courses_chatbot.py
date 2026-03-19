import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.messages import HumanMessage, AIMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import os 

st.set_page_config(page_title="RAG Chatbot")

def build_vector_db():
    embeddings_model = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001")
    folder_path = "./courses_vectors"
    if os.path.exists(folder_path):
        db = FAISS.load_local(folder_path, embeddings_model,
                          allow_dangerous_deserialization=True)
        print("Loaded FAISS index")
    else:
        loader = PyPDFLoader("../docs/courses_offered.pdf")
        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500, chunk_overlap=50)
        split_docs = splitter.split_documents(docs)
        db = FAISS.from_documents(split_docs, embeddings_model)
        print('Created FAISS index')
        db.save_local(folder_path)
   
    return db 
 

def newchat():
    st.session_state["chat_history"] = []
    st.session_state["text"] = ""


vector_db = build_vector_db()
retriever = vector_db.as_retriever()

# Initialize chat history in session
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if "text" not in st.session_state:
    st.session_state["text"] = ""

# Button to start a new chat-session
st.button("New Chat", on_click=newchat) 

st.title("Multi-turn Aware RAG Chatbot")
user_query= st.text_input("Ask something:", key = "text")

if user_query:
        # Save user's query in session history
        st.session_state.chat_history.append(HumanMessage(content=user_query))

        # Build multi-turn context (last 3 user messages)
        last_user_messages= [
    msg.content for msg in st.session_state.chat_history if isinstance(msg, HumanMessage)
    ]
        combined_query = "\n".join(last_user_messages[-3:])

        # Retrieve relevant documents
        relevant_docs= retriever.invoke(combined_query)
        print(combined_query)
        # Create context to send to LLM
        context= "\n\n".join([doc.page_content for doc in relevant_docs])
        prompt= f"""You are a helpful AI. Use the context below to answer the question.

Context:
{context}

Question: {combined_query}
"""

        llm= ChatGoogleGenerativeAI(model = "gemini-2.5-flash",temperature = 0.1)
        ai_response= llm.invoke(prompt).content
        
        st.markdown(ai_response)

        