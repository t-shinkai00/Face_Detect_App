import streamlit as st
from PIL import Image
from FaceApi import detect_face
st.title("Face Detector")

uploaded_file=st.file_uploader("Choose a jpg image", type="jpg")

if uploaded_file is not None:
  img=Image.open(uploaded_file)
  # print(uploaded_file,img)
  detect_face(img)
  st.image(img, caption="Result", use_column_width=True)