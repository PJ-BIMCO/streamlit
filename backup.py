import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt


def main_page():
    st.markdown("# Inspection Data")
    st.markdown("Latest Detention")

    st.dataframe(dfLatest)
    st.markdown("Latest 10 Detentions")

    st.dataframe(df100)

    st.markdown("All Inspections")

    st.dataframe(df)
    



def page2():
    st.markdown("# Detentions vs Ship Type")


    st.markdown("Detentions sorted by ship type past 30 days")

    st.bar_chart(shipTypeMonth, width=400, height=800)

    st.markdown("Detentions sorted by ship type all time")

    st.bar_chart(shipTypeTotal, width=400, height=800)

    st.markdown("Detentions sorted by ship type and weighted by world fleet")

    st.bar_chart(data=shipTypeWeighted, width=400, height=800)



def page3():
    st.markdown("# Common Defeciencies")


    genre = st.radio(
     "Choose a Graph to Display",
     ('Deficiency Codes','Defeciencies found in inspections', 'Defeciencies found in detentions', 'Defeciencies found in detentions vs all deficiencies'))

    if genre == 'Deficiency Codes':
        for line in lines:
            st.markdown(line)

    elif genre == 'Defeciencies found in inspections':


        st.markdown("Most common defeciencies found in inspections")
        data = pd.melt(deficiencies.reset_index(), id_vars=["index"])
        # Horizontal stacked bar chart
        chart = (
            alt.Chart(data)
                .mark_bar()
                .encode(
                x=alt.X("value", type="quantitative", title="Number of Times Found"),
                y = alt.Y("index", sort=alt.SortField(field="n", order='descending'))
            )
        )
        st.altair_chart(chart, use_container_width=True,use_container_height=True)
        st.markdown("Most common defeciencies found when detained")

    elif genre == 'Defeciencies found in detentions':

        st.markdown("Most common defeciencies found in when ship has been detained")
        data = pd.melt(deficiencies_detention.reset_index(), id_vars=["index"])
        # Horizontal stacked bar chart
        chart = (
            alt.Chart(data)
                .mark_bar()
                .encode(
                x=alt.X("value", type="quantitative", title="Number of Times Found"),
                y = alt.Y("index", sort=alt.SortField(field="n", order='descending'))
            )
        )
        st.altair_chart(chart, use_container_width=True)
        st.markdown("Most common defeciencies found when detained")

    elif genre == 'Defeciencies found in detentions vs all deficiencies':



        st.markdown("Relative chance of defeciency being grounds for detention")
        data = pd.melt(deficiencies_detention_weighted.reset_index(), id_vars=["index"])
        # Horizontal stacked bar chart
        chart = (
            alt.Chart(data)
                .mark_bar()
                .encode(
                x=alt.X("value", type="quantitative", title="Number of Times Found"),
                y = alt.Y("index", sort=alt.SortField(field="n", order='descending'))
            )
        )
        st.altair_chart(chart, use_container_width=True)
        st.markdown("Relative chance of defeciency being grounds for detention")



def page4():
    st.markdown("# Detentions vs Age")
    #st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    st.bar_chart(ship_age_weighted, width=400, height=800)




page_names_to_funcs = {
    "View Data": main_page,
    "Detentions vs Ship Type": page2,
    "Common Defeciencies": page3,
    "Detentions vs Age":page4,
}

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 10000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)
pd.set_option('display.max_colwidth', 1000)



df = pd.read_pickle('pretty.pkl')
df100 = pd.read_pickle('latest100.pkl')
dfLatest = pd.read_pickle('latest.pkl')

shipTypeMonth = pd.read_pickle('shipTypeMonth.pkl')
shipTypeTotal = pd.read_pickle('shipTypeTotal.pkl')
shipTypeWeighted = pd.read_pickle('shipTypeWeighted.pkl')

deficiencies = pd.read_pickle('deficiencies.pkl')
deficiencies_detention = pd.read_pickle('deficiencies_detention.pkl')
deficiencies_detention_weighted = pd.read_pickle('deficiencies_weighted.pkl')

deficiencyCodes = deficiencies.index.tolist()


ship_age_weighted = pd.read_pickle('ship_age_weighted.pkl')

with open('Deficiencies.txt') as f:
    lines = f.readlines()



st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO",layout="wide")


st.image(
    "BIMCO_Logo_small.png",
    width=200,
)

selected_page = st.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()




