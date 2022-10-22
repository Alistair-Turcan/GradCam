import streamlit as st
st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
st.image(uploaded_file)
