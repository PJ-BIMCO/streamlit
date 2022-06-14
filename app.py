import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO")

st.sidebar.image(
    "BIMCO_Logo_small.png",
    width=100,
)



dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))