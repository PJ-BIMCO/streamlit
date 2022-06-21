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

    data = pd.DataFrame({
    'date': [pd.Timestamp('2020-01-01'), pd.Timestamp('2020-01-02'), pd.Timestamp('2020-01-03'),pd.Timestamp('2020-01-04'),pd.Timestamp('2020-01-05'),pd.Timestamp('2020-01-06')],
    'b': [1, 1, 2,3,5,7],
    'c': [0.5, 0.6, 0.1, 0.1,0.4,0.3],
    })

    c = alt.Chart(data).mark_line(point=True).encode(
      alt.Y('c:Q', axis=alt.Axis(format='%')),
      x='date:T',
      color='b:N'
    )
    st.altair_chart(c)


def page3():
    st.markdown("# Common Defeciencies")

    st.markdown("Most common defeciencies found in inspections")
    #st.bar_chart(deficiencies, width=400, height=800)

    # Convert wide-form data to long-form
    # See: https://altair-viz.github.io/user_guide/data.html#long-form-vs-wide-form-data

    deficiencies1 = deficiencies.sort_values(by='n', ascending=False)

    data = pd.melt(deficiencies1.reset_index(), id_vars=["index"])

    # Horizontal stacked bar chart
    chart = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            x="n",
            y="index"
        )
    )

    st.altair_chart(chart, use_container_width=True)



   



    st.markdown("Most common defeciencies found when detained")

def page4():
    st.markdown("# Detentions vs Company")
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")




page_names_to_funcs = {
    "View Data": main_page,
    "Detentions vs Ship Type": page2,
    "Common Defeciencies": page3,
    "Detentions vs Company":page4,
}


df = pd.read_pickle('pretty.pkl')
df100 = pd.read_pickle('latest100.pkl')
dfLatest = pd.read_pickle('latest.pkl')

shipTypeMonth = pd.read_pickle('shipTypeMonth.pkl')
shipTypeTotal = pd.read_pickle('shipTypeTotal.pkl')
shipTypeWeighted = pd.read_pickle('shipTypeWeighted.pkl')

deficiencies = pd.read_pickle('deficiencies.pkl')

st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO",layout="wide")


st.image(
    "BIMCO_Logo_small.png",
    width=200,
)

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()




