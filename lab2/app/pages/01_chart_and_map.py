import pandas as pd
import streamlit as st
import numpy as np

from common import session_manager
ssm = session_manager.st_session()
# ssm.write_session_info()


st.title("チャート、マップを描画する")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# https://docs.streamlit.io/library/api-reference/charts/st.map
# mapboxのライセンスが必要と書かれている。

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])  # 緯度、経度を指定

st.map(map_data)

