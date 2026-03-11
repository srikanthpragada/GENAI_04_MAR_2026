from langchain.chat_models import init_chat_model
import streamlit as st

model = init_chat_model("gemini-2.5-flash", 
                         model_provider="google_genai")

system_prompt = {"role" : "system", "content" : "Give short answers"}

# Add messages to session, if not present 
if 'messages' not in st.session_state:
     st.session_state.messages = [system_prompt]

def clear_text():
    st.session_state.messages = [system_prompt]
    st.session_state.text = ""

st.title("Gemini Demo")
prompt = st.text_area("Enter your prompt", key = "text", height=100)
# Button to clear the text area
st.button("Create New Chat", on_click=clear_text)

if len(prompt) > 0 :
     # add prompt to messages 
    st.session_state.messages.append({"role": "user", "content": prompt})
    ai_response = model.invoke(st.session_state.messages)
    response = ai_response.content
    st.write(response, unsafe_allow_html=True)

    #add response to messages as AIMessage 
    st.session_state.messages.append({"role": "assistant", "content": response})
    
