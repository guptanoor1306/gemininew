# Q&A Chatbot
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai

# Directly assign the API key here
API_KEY = "AIzaSyDyjhSAk0aI5Q_LRYqyvhBaEg3mGmIN4_M"

# Configure the generative AI client with the API key
genai.configure(api_key=API_KEY)

# Function to load OpenAI model and get response
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

# If ask button is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The Response is")
    st.write(response)
