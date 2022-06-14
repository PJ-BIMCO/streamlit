import streamlit as st
import pandas as pd
import numpy as np
import datetime


def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)



df = pd.read_pickle('MoU.pkl')


st.set_page_config(page_icon=render_svg("BIMCO2016_Logo_RGB.svg"), page_title="MoU BIMCO")


st.image(
    render_svg("BIMCO2016_Logo_RGB.svg"),
    width=200,
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



st.bar_chart(data=df['Ship Type'], width=400, height=200, use_container_width=True)




