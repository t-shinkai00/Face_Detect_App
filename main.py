import streamlit as st
from PIL import Image
from Face_API import detect_face

st.title("顔認識アプリ")

uploaded_file=st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
  img=Image.open(uploaded_file)
  st.image(img, caption="Uploaded Image.", use_column_width=True)