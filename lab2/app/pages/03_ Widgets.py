import pandas as pd
import streamlit as st
import numpy as np

from common import session_manager
ssm = session_manager.st_session()

st.title("ウィジェット")
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# ------------------------

st.title("Input box & slider")

# session info init
if 'name' not in st.session_state:
    st.session_state.name = ""

# inputbox
# st.text_input("Your name",st.session_state.name, key="name" )

st.text_input("Your name", key="name" )
st.slider('How old are you?', min_value=0, max_value=130,value=25,key="age")


# ------------------------

st.title("checkbox")

if st.checkbox('Show dataframe',key="chk1"):
    chart_data = pd.DataFrame(
       np.random.randn(5, 3),
       columns=['a', 'b', 'c'])

    chart_data

# ------------------------

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option


# ------------------------


st.title("セッション情報")

# https://docs.streamlit.io/library/api-reference/session-state
# You can access the value at any point with:
ssm.write_session_info()

