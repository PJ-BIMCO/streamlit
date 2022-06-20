import streamlit as st
import pandas as pd
import numpy as np



df = pd.read_pickle('MoU.pkl')

shipTypeMonth = pd.read_pickle('shipTypeMonth.pkl')
shipTypeTotal = pd.read_pickle('shipTypeTotal.pkl')
shipTypeWeighted = pd.read_pickle('shipTypeWeighted.pkl')


st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO",layout="wide")


st.image(
    "BIMCO_Logo_small.png",
    width=200,
)



option = st.sidebar.selectbox(
    'Please select a ship by name:',
     df['Ship Name'])

#st.sidebar.write('You selected: ', option) dsad2




options = st.sidebar.multiselect(
     'Select Shiptype',
     ['Container Ship', 'Bulk Carrier', 'Tanker Ship', 'Passenger Ship','Naval Ship','Offshore Ship','Special Purpose Ship','Ro-Ro Cargo Ship','General Cargo','Other'],
     ['Container Ship', 'Bulk Carrier', 'Tanker Ship', 'Passenger Ship','Naval Ship','Offshore Ship','Special Purpose Ship','Ro-Ro Cargo Ship','General Cargo','Other'])


st.dataframe(df)

st.bar_chart(shipTypeMonth)

st.bar_chart(shipTypeTotal)

st.bar_chart(data=shipTypeWeighted, width=400, height=800)
