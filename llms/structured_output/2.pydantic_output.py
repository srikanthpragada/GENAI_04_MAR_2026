from langchain.chat_models import init_chat_model
from pydantic import BaseModel 

class Country(BaseModel):
    #Attributes 
    name : str 
    population : int 
    capital : str 
    cities : list[str]


model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
structured_model = model.with_structured_output(Country)
output = structured_model.invoke("Provide details of Spain")

print(output)   
print(output.cities)  # Access an object attribute 
 


 