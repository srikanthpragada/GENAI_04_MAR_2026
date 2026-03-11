from typing import TypedDict
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.2:latest")

class Country(TypedDict):
    # keys
    name : str 
    population : int 
    capital : str 
    cities : list[str]

structured_model = model.with_structured_output(Country)
output = structured_model.invoke("Provide details of Australia")

print(output)   
 
 


 