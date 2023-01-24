import streamlit as st
import base64
from PIL import Image
from streamlit.components.v1 import html

# Function adding background to the streamlit page
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('background.jpg')

image = Image.open('candidate1.jpg')
st.image(image, caption='# Candidate No 1')