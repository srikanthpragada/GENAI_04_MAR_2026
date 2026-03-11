from typing import TypedDict
from langchain.chat_models import init_chat_model

class Country(TypedDict):
    # keys
    name : str 
    population : int 
    capital : str 
    important_cities : list[str]


model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
structured_model = model.with_structured_output(Country)
output = structured_model.invoke("Provide details of Spain")

print(output)   
print(output["important_cities"])
 


 