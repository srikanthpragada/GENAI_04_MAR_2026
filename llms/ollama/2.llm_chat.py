from langchain_ollama import ChatOllama
 
llm = ChatOllama(model="llama3.2:latest")
print(llm.invoke("Which is the capital of Australia?"))
 
