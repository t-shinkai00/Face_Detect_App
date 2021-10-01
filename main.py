import streamlit as st
import pandas as pd
import numpy as np

st.title("My 1st App")

st.write("データフレーム")
st.write(
  pd.DataFrame({
    "1st column":[1,2,3,4],
    "2nd column":[10,20,30,40],
  })
)

"""
# My 1st App
## マジックコマンド
Markdown対応
"""

if st.checkbox("Show DataFrame"):
  chart_df=pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"]
  )
  st.line_chart(chart_df)