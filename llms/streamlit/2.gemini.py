# streamlit run 2.gemini.py

import streamlit as st
from langchain.chat_models import init_chat_model
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
st.title("Get Answers from Gemini!")


# display textbox
prompt = st.text_input("Enter your prompt", "")
if len(prompt) > 0:
    response = model.invoke(prompt)
    st.write(response.content, unsafe_allow_html=True)
     