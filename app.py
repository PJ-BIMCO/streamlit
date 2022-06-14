import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO")

st.sidebar.image(
    "BIMCO_Logo_small.png",
    width=100,

)

option = st.selectbox(
    'What ship do you like the best?',
     df['Ship Name'])

'You selected: ', option




df = pd.read_pickle('MoU.pkl')


st.dataframe(df)



map_data = pd.DataFrame(
    np.random.randn(60, 2) / [50, 50] + [55.764869, 12.468345],
    columns=['lat', 'lon'])

st.map(map_data)


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


