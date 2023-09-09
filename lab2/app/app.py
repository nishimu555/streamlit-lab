# from collections import namedtuple
# import altair as alt
# import math
import pandas as pd
import streamlit as st
import numpy as np

from common import session_manager
ssm = session_manager.st_session()

st.title("Hello world!")


# 文字列を表示
st.write("hello!")
st.write("111","222","333") # 複数指定するとスペース区切りで連結される。

# ------------------------
ssm.write_session_info()






