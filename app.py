import streamlit as st
from utils import model
from PIL import Image


st.set_page_config(
    page_title="WaldoDetectionAI", page_icon="🔎"
)

st.markdown('''
# 🔎 WaldoDetectionAI

AI model designed to detect the location of Waldo (also known as "Wally") in images

''')

uploaded_file = st.file_uploader("Choose an image")
if uploaded_file:
    # bytes_data = uploaded_file.read()
    # st.write("filename:", uploaded_file.name)
    # st.write(bytes_data)
    # st.image(bytes_data)
    img = Image.open(uploaded_file)
    st.image(img)
    result = model(img)
    # result_img = Image.fromarray(result[0].plot()).convert("RGB")
    st.image(result[0].plot()[..., ::-1])
