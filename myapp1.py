import streamlit as st
import numpy as np
import pandas as pd

st.title("This is Jory !!")
st.write("And this one just a sample Application!!")

df= pd.DataFrame({
    'C1':[100,200,300,400,500],
    'C2':['Yogesh','Sachin','Virat','jack','Jones']
})

st.write("Below is the DataFrame:")
st.write(df)

chart_data=pd.DataFrame(np.random.randn(20,4),columns=['p','q','r','s'])

st.line_chart(chart_data)
