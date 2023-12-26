import streamlit as st
import pathlib
import textwrap
import google.generativeai as genai
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image


# Set up the Gemini AI API
API_KEY = st.secrets["API_KEY"]
genai.configure(api_key=API_KEY)
text_model = genai.GenerativeModel('gemini-pro')
vision_model = genai.GenerativeModel('gemini-pro-vision')


# Streamlit app
st.title("Gemini AI App")

option = st.selectbox(
    'Choose a model',
    ('Gemini pro', 'Gemini pro vision', 'Conversation'))

if option == 'Gemini pro':
  prompt = st.text_input(label='Enter your prompt')
  if st.button("Ask Gemini"):
          response = text_model.generate_content(prompt)
          result = response.text
          st.markdown(result)

elif option == 'Gemini pro vision':
  uploaded_file = st.file_uploader("Choose a file")
  prompt = st.text_input(label='Enter your prompt')
  if uploaded_file is not None:
    st.image(uploaded_file)
    pilimage = Image.open(uploaded_file).convert("RGB")
    if st.button("Ask Gemini"):
            response = vision_model.generate_content([prompt, pilimage])
            response.resolve()
            result = response.text
            st.markdown(result)

elif option == 'Conversation':
    prompt = st.text_input(label='Enter your prompt')
    chat = text_model.start_chat(history=[])
    if st.button("Ask Gemini"):
        # Send the prompt to the model
        response = chat.send_message(prompt)

        # Update the chat history with the current turn
        chat_history = chat.history
        chat_history.append(response)

        # Display the chat history
        st.write(len(chat_history))
        st.write(chat_history)
#########################################################
st.markdown("<h1 style='font-size:15px; text-align: center; color: red; font-family:SansSerif;'>Made with 💖 By Ahmed Hossam</h1>", unsafe_allow_html=True)
st.markdown("[My Github](https://github.com/Ahmed-Hossam-Aldeen)")

          
