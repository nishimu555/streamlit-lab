import pandas as pd
import streamlit as st
import numpy as np

from common import session_manager
ssm = session_manager.st_session()
# ssm.write_session_info()

st.title("表を描画する")

# データフレームを元に表を表示する
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write("write関数")
st.write(df)

st.write("table関数")
st.table(df)

st.write("dataframe関数、writeとほとんど同じ？")
st.dataframe(df)


# 
df2 = np.random.randn(10, 20)
st.dataframe(df2)

#
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))  # col名を設定

# highlight_max（最大値にハイライトする）、axis=0（インデックス（列？）の対して評価する、１とすると行になる）
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.highlight_max.html#pandas.io.formats.style.Styler.highlight_max
st.dataframe(dataframe.style.highlight_max(axis=1,color="red"))  

# 
st.table(dataframe.style.highlight_max(axis=1,color="red"))
