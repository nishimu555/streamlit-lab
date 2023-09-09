import pandas as pd
import streamlit as st
import numpy as np

st.title("ウィジェット")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# ------------------------

st.title("Input box")

# session info init
if 'name' not in st.session_state:
    st.session_state.name = ""

# inputbox
# st.text_input("Your name",st.session_state.name, key="name" )

tmp_name = st.session_state.name
st.text_input("Your name", key="name" )

# https://docs.streamlit.io/library/api-reference/session-state
# You can access the value at any point with:
st.write("session info =",st.session_state.name)

