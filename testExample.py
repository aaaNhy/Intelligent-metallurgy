import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

st.header('自己做的页面')

st.write('自己做的页面')

if st.button('你要做页面吗'):
     st.write('你猜猜对了')
else:
     st.write('是的')

# 样例 1

st.write('这是输出语句，可以输出各种各样的数据')

# 样例 2

st.write("int:"+1234)

# 样例 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# 样例 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 样例 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)