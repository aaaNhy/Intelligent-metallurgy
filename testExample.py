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


st.write('这是输出语句，可以输出各种各样的数据')


st.write("int:", 1234)


df = pd.DataFrame({
    '身高cm': [160, 170, 180, 190],
    '体重kg': [50, 60, 70, 80]
})
st.write(df)


df2 = pd.DataFrame(
    np.random.randn(400, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write("图表：", c)
