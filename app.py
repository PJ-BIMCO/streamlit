import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO")

st.sidebar.image(
    "BIMCO_Logo_small.png",
    width=100,
)

df = pd.read_pickle(streamlitPath)


st.dataframe(df)

