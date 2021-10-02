import streamlit as st
from PIL import Image
from FaceApi import detect_face
st.title("顔検出アプリ")

uploaded_file=st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
  img=Image.open(uploaded_file)
  # print(uploaded_file,img)
  detect_face(img)
  st.image(img, caption="Uploaded Image.", use_column_width=True)