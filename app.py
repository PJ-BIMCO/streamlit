import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_pickle('MoU.pkl')


st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO")


st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.image(
    "BIMCO_Logo_small.png",
    width=400,
)


option = st.sidebar.selectbox(
    'Please select a ship:',
     df['Ship Name'])

st.sidebar.write('You selected: ', option)




map_data = pd.DataFrame(
    np.random.randn(60, 2) / [50, 50] + [55.764869, 12.468345],
    columns=['lat', 'lon'])

st.map(map_data)


x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


if st.checkbox('Show dataframe'):
    st.dataframe(df)


st.markdown('pages/page_1.py')
st.sidebar.markdown('pages/page_1.py')
