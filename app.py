import streamlit as st
import pandas as pd
import numpy as np
import datetime

from bokeh.plotting import figure


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





x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
     title='simple line example',
     x_axis_label='x',
     y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)

