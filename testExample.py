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

st.write("int:", 1234)

# 样例 3

df = pd.DataFrame({
    '身高cm': [160, 170, 180, 190],
    '体重kg': [50, 60, 70, 80]
})
st.write(df)

# 样例 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 样例 5

df2 = pd.DataFrame(
    np.random.randn(400, 3),
    columns=['身高', '体重', '肤色'])
c = alt.Chart(df2).mark_circle().encode(
    x='身高', y='体重', size='肤色', color='肤色', tooltip=['身高', '体重', '肤色'])
st.write(c)
