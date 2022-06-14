import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO")

st.sidebar.image(
    "BIMCO_Logo_small.png",
    width=100,
)




df = pd.read_pickle('MoU.pkl')


st.dataframe(df)



map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)