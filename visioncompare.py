# Q&A Chatbot
import streamlit as st
from PIL import Image
import google.generativeai as genai

# Directly assign the API key here
API_KEY = "AIzaSyDyjhSAk0aI5Q_LRYqyvhBaEg3mGmIN4_M"

# Configure the generative AI client with the API key
genai.configure(api_key=API_KEY)

# Function to load OpenAI model and get response for a single image
def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Function to compare two images based on input prompt
def compare_images(input, image1, image2):
    model = genai.GenerativeModel('gemini-pro-vision')
    response1 = model.generate_content([input, image1])
    response2 = model.generate_content([input, image2])
    
    # Example comparison logic: comparing the responses based on the input prompt
    comparison_result = {
        'image1': response1.text,
        'image2': response2.text,
        'comparison': {
            'input_prompt': input,
            'response1': response1.text,
            'response2': response2.text
        }
    }
    
    # Add your own comparison logic here based on the responses
    # For demonstration, we just show both responses
    return comparison_result

# Initialize our Streamlit app
st.set_page_config(page_title="Gemini Image Comparison Demo")

st.header("Gemini Image Comparison Application")
input = st.text_input("Input Prompt: ", key="input")

uploaded_file1 = st.file_uploader("Choose the first image...", type=["jpg", "jpeg", "png"], key="image1")
uploaded_file2 = st.file_uploader("Choose the second image...", type=["jpg", "jpeg", "png"], key="image2")

image1, image2 = None, None
if uploaded_file1 is not None:
    image1 = Image.open(uploaded_file1)
    st.image(image1, caption="Uploaded First Image.", use_column_width=True)
if uploaded_file2 is not None:
    image2 = Image.open(uploaded_file2)
    st.image(image2, caption="Uploaded Second Image.", use_column_width=True)

submit = st.button("Compare the images")

# If submit button is clicked
if submit and image1 is not None and image2 is not None:
    response = compare_images(input, image1, image2)
    st.subheader("The Comparison Result is")
    st.write(response)
elif submit:
    st.error("Please upload two images to compare.")
