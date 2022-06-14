import streamlit as st
import pandas as pd

st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO")

st.sidebar.image(
    "BIMCO_Logo_small.png",
    width=100,
)



st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))