import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO",layout="wide")


shipTypeWeighted = pd.read_pickle('shipTypeWeighted.pkl')

