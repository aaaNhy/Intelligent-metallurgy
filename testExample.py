import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
from datetime import time, datetime

st.header('自己做的页面')

if st.button('说说你的梦想'):
     st.write('我要冶金')
else:
     st.write('最大的梦想是什么')

st.write("下面看看冶金工作的具体情况")

df = pd.DataFrame({
    '工时h': [150, 170, 180, 190],
    '工资￥': [2600, 3000, 4000, 6000]
})

st.write("冶金工人工资详情：", df)

st.header('让我们画个折线图来看清楚冶金工人的身高体重年龄')
chart_data = {'身高cm': [150, 160, 170, 180, 190], '体重kg': [50, 55, 60, 70, 80]}

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

st.line_chart(chart_data)

df2 = pd.DataFrame(
    np.random.randn(80, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write("冶金工人随便画的图：", c)


st.write("说出你的详细信息，我们来看看录不录用你：")

age = st.slider('你的年龄是?', 0, 130, 25)
st.write("我", age, '岁了')

st.subheader('选择你的工作年限')

values = st.slider(
     '选择一个区间（默认25-50）',
     18.0, 60.0, (25.0, 50.0))
st.write('你选的工作年限是:', values)

st.subheader('你选择的工作时间是？：')

appointment = st.slider(
     "你的时间表:",
     value=(time(6, 00), time(23, 59)))
st.write("你自愿的工作时间表是:", appointment)

st.subheader('你每年打算从什么时候开始干到年尾')

start_time = st.slider(
     "做出你的打算?",
     value=datetime(2023, 1, 1, 6, 30),
     format="MM/DD/YY - hh:mm")
st.write("你的开始时间是:", start_time)

st.header('你喜欢的怎么去上班')

option = st.selectbox(
     '在以下选项中选择?',
     ('走去', '公交车', '地铁', '打车'))

st.write('原来你喜欢用： ', option, '这种方式去上班')

st.header('在我们公司冶金工人不仅可以选择自己喜欢的衣服,还可以选择衣服的颜色')
option = st.selectbox(
     '在以下选项中选择，你最喜欢的工服是？',
     ('长袖', '短袖', '背心'))

options = st.multiselect(
     '你最喜欢的工服颜色是（默认黄色）',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow'])
st.write('你选择:', option, '作为工服,颜色是', options )

st.write ('选择你的工作零食?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! 你点的 🍦")

if coffee:
     st.write("Okay, 你要的咖啡 ☕")

if cola:
     st.write("喝点可乐 🥤")

st.write ('你的大概情况我们已经了解了，后续等通知吧')

