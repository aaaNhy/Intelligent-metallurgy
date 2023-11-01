import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_excel('https://github.com/aaaNhy/Intelligent-metallurgy.git/testB_2022-09-19.xlsx')

pr = df.profile_report()
st_profile_report(pr)
