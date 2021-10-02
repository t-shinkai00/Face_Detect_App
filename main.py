import streamlit as st
from PIL import Image
from FaceApi import detect_face
st.title("顔検出アプリ")

uploaded_file=st.file_uploader("画像を選択", type="jpg")

if uploaded_file is not None:
  img=Image.open(uploaded_file)
  # print(uploaded_file,img)
  detect_face(img)
  st.image(img, caption="検出結果", use_column_width=True)