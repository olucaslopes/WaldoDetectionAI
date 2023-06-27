import streamlit as st


st.set_page_config(
    page_title="WaldoDetectionAI", page_icon="🔎"
)

st.markdown('''
# 🔎 WaldoDetectionAI

AI model designed to detect the location of Waldo (also known as "Wally") in images

''')

uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    # st.write(bytes_data)
    st.image(bytes_data)
