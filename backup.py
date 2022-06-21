import streamlit as st
import pandas as pd
import numpy as np


def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

    st.dataframe(df)

def page2():
    st.markdown("# Page 2 ❄️")
    st.sidebar.markdown("# Page 2 ❄️")

    
    st.markdown("Detentions sorted by ship type past 30 days")

    st.bar_chart(shipTypeMonth, width=400, height=800)

    st.markdown("Detentions sorted by ship type all time")

    st.bar_chart(shipTypeTotal, width=400, height=800)

    st.markdown("Detentions sorted by ship type and weighted by world fleet")

    st.bar_chart(data=shipTypeWeighted, width=400, height=800)
    

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")


    option = st.sidebar.selectbox(
        'Please select a ship by name:',
         df['Ship Name'])

    #st.sidebar.write('You selected: ', option) dsad2d

    options = st.sidebar.multiselect(
         'Select Shiptype',
         ['Container Ship', 'Bulk Carrier', 'Tanker Ship', 'Passenger Ship','Naval Ship','Offshore Ship','Special Purpose Ship','Ro-Ro Cargo Ship','General Cargo','Other'],
         ['Container Ship', 'Bulk Carrier', 'Tanker Ship', 'Passenger Ship','Naval Ship','Offshore Ship','Special Purpose Ship','Ro-Ro Cargo Ship','General Cargo','Other'])




page_names_to_funcs = {
    "View Data": main_page,
    "Detentions vs Ship Type": page2,
    "Common Defeciencies": page3,
}


df = pd.read_pickle('MoU.pkl')

shipTypeMonth = pd.read_pickle('shipTypeMonth.pkl')
shipTypeTotal = pd.read_pickle('shipTypeTotal.pkl')
shipTypeWeighted = pd.read_pickle('shipTypeWeighted.pkl')

st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO",layout="wide")


st.image(
    "BIMCO_Logo_small.png",
    width=200,
)

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()




