import streamlit as st
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt


df = pd.read_pickle('MoU.pkl')


st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO")


st.image(
    "BIMCO_Logo_small.png",
    width=400,
)


option = st.sidebar.selectbox(
    'Please select a ship:',
     df['Ship Name'])

st.sidebar.write('You selected: ', option)




options = st.sidebar.multiselect(
     'Select Shiptype',
     ['Container Ship', 'Bulk Carrier', 'Tanker Ship', 'Passenger Ship','Naval Ship','Offshore Ship','Special Purpose Ship','Ro-Ro Cargo Ship','General Cargo','Other'],
     ['Container Ship', 'Bulk Carrier', 'Tanker Ship', 'Passenger Ship','Naval Ship','Offshore Ship','Special Purpose Ship','Ro-Ro Cargo Ship','General Cargo','Other'])



st.dataframe(df)



chart_data = pd.DataFrame(
     np.random.randn(50, 1),
     columns=["a"])

st.bar_chart(chart_data)



d = st.date_input(
     "From:",
     datetime.date(2019, 7, 6))


d = st.date_input(
     "To:",
     datetime.date(2019, 7, 6))



arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)