import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
from datetime import time, datetime

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


st.write("接着让我们再制作些滑条输入组件：")

age = st.slider('请输入你的年龄?', 0, 130, 25)
st.write("我", age, '岁了')

st.subheader('滑动范围')

values = st.slider(
     '选择一个区间（默认100-800）',
     0.0, 1000.0, (100.0, 800.0))
st.write('Values:', values)

st.subheader('时间范围滑动条：')

appointment = st.slider(
     "制定你的时间表:",
     value=(time(11, 30), time(12, 45)))
st.write("你指定的时间表是:", appointment)

st.subheader('日期滑动条')

start_time = st.slider(
     "什么时候开始?",
     value=datetime(2023, 10, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("开始时间:", start_time)

