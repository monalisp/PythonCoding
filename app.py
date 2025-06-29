import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello")
st.write("This is simple text")
df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})
st.write("Here is the dataframe")
st.write(df)
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    column=['a','b','c']
)
st.line_chart(chart_data)