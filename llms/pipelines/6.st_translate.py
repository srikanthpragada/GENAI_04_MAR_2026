# pip install -q streamlit
import streamlit as st
from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")

st.title("English to Hindi")
text  = st.text_input("Enligsh Text", "" )
if len(text) > 0:
    hindi = translator(text)
    st.write("<h2>" + hindi[0]['translation_text'] + "</h2>", 
             unsafe_allow_html=True)



     