# run it using  -> streamlit run 1.hello.py

import streamlit as st

st.title("Demo")
# display textbox
name = st.text_input("Enter your name", "")
if len(name) > 0:
    st.write(f"<h3>Hello {name}, welcome to the Streamlit Library! </h3>", 
          unsafe_allow_html=True )
     