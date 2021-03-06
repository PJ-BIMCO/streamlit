import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import datetime
from collections import Counter


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
        st.altair_chart(chart, use_container_width=True)
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
    #st.metric(label="Temperature", value="70 ??F", delta="1.2 ??F")
    st.bar_chart(ship_age_weighted, width=400, height=800)




def page5():
    video_file = open('Rick_Astley.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes,start_time=0)

def page6():



    countryList= list(dict.fromkeys(deficiencies_at_port_country['Country Name']))
    cleanedCountryList = [x for x in countryList if str(x) != 'nan']
    cleanedCountryList.sort()

    portsList = list(dict.fromkeys(deficiencies_at_port_country['Port']))
    cleanedPortsList = [x for x in portsList if str(x) != 'nan' or not str(x)]
    cleanedPortsList.sort()


    st.markdown("# Detention based on port or country")


    col1, col2 = st.columns([3, 1])


    # Column 2 
    #col2.subheader("A narrow column with the data")
    countryList = col2.multiselect(
        'Choose a country or state',
        cleanedCountryList)

    #col2.markdown(countryList)
    
    portList = col2.multiselect(
        'Choose a port',
        cleanedPortsList)

    d_from = col2.date_input(
        "From",
        datetime.date(2020, 1, 1))

    d_to = col2.date_input(
        "To",
        datetime.datetime.now().date())

    showDetained = col2.checkbox('Only Show Detained')

    weight = col2.checkbox('Most Found Defeciencies Relative to Global Average')

    #if agree:


    #Column 1 
    #ol1.subheader("A wide column with a chart")

    deficiencies_at_port_country_country_name = deficiencies_at_port_country[deficiencies_at_port_country['Country Name'].isin(countryList)]
    deficiencies_at_port_country_port = deficiencies_at_port_country[deficiencies_at_port_country['Port'].isin(portList)]

    df1 = deficiencies_at_port_country_country_name[deficiencies_at_port_country_country_name['Country Name'].isin(countryList)]
    df2 = deficiencies_at_port_country_port[deficiencies_at_port_country_port['Port'].isin(portList)]

    df_new = pd.concat([df1, df2], ignore_index=False)

    df_new['Date of Inspection'] = df_new['Date of Inspection'].dt.date

    df_new = df_new[df_new['Date of Inspection'] > d_from]
    df_new = df_new[df_new['Date of Inspection'] < d_to]


    if showDetained:
        df_new = df_new[df_new['Detained'] == True]






    deficiencyList = []
    for elem in df_new['Deficiency Descriptions']:
        deficiencyList += elem
    deficiencyList.sort()
    countDict = dict(Counter(deficiencyList))
    try:
        del countDict['']
    except:
        pass
    count_df = pd.DataFrame.from_dict([countDict]).T
    count_df.columns = ['n']
    test = count_df.sort_values(by=['n'], ascending=False)




    
    weightedDict = {}
    if weight:
        
        for index, row in count_df.iterrows():
            try:
                test1 = row['n'] / weighted_global_deficiencies['n'][index]
                weightedDict[index] = test1

                #st.markdown(test)
            except:
                pass
        
        test = pd.DataFrame.from_dict([weightedDict])

        test = test.T
        test.columns = ['n']

        test = test.sort_values(by='n', ascending=False)


        #st.markdown(test)       

    #col1.bar_chart(data=test, width=400, height=800)

    data_country = pd.melt(test.reset_index(), id_vars=["index"])
    # Horizontal stacked bar chart
    chart1 = (
        alt.Chart(data_country)
            .mark_bar()
            .encode(
            x=alt.X("value", type="quantitative", title="Number of Times Found"),
            y = alt.Y("index", sort=alt.SortField(field="n", order='descending'))
        )
    )
    col1.altair_chart(chart1, use_container_width=True)



    #st.markdown(my_time)
    #st.markdown(type(df_new['Date of Inspection'][5714]))
    #st.markdown(df_new.dtypes)
    #st.markdown(type(my_datetime))

    #st.markdown(countryList)
    #st.markdown(portList)
    #st.markdown(test)
    #st.markdown(deficiencyList)


    # Whole page
    #st.map(df)


page_names_to_funcs = {
    "View Data": main_page,
    "Detentions vs Ship Type": page2,
    "Common Deficiencies": page3,
    "Detentions vs Age":page4,
    "Detention based on port or country":page6,

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

deficiencies_at_port_country = pd.read_pickle('deficiencies_at_port_country.pkl')


weighted_global_deficiencies = pd.read_pickle('weighted_global_deficiencies.pkl')

ship_age_weighted = pd.read_pickle('ship_age_weighted.pkl')

with open('Deficiencies.txt') as f:
    lines = f.readlines()



st.set_page_config(page_icon="BIMCO_Logo_small.png", page_title="MoU BIMCO",layout="wide")


st.image(
    "BIMCO_Logo_small.png",
    width=200,
)

selected_page = st.selectbox("", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()




