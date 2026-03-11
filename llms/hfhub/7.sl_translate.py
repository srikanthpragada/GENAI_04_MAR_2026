# streamlit run sl_translate.py

import streamlit as st
from huggingface_hub import InferenceClient
import keys

model_id = "Helsinki-NLP/opus-mt-en-hi"   
client = InferenceClient(model=model_id, token= keys.HUGGINGFACE_KEY)

st.title("English to Hindi")
text  = st.text_input("Enligsh Text", "" )
if len(text) > 0:
    hindi = client.translation(text)
    st.write(f"<h4>{hindi.translation_text}</h4>", unsafe_allow_html=True)



     