import streamlit as st
import pandas as pd
import plotly.express as px

# dictionary to map data
mapper = {'Coal': {'hist': ['coalcons_ej'], 
                    'fcst': ['Coal']},
          'Oil': {'hist': ['oilcons_ej'],
                  'fcst': ['Oil']},
          'Natural Gas': {'hist': ['gascons_ej'],
                          'fcst': ['Natural gas']},
          'Nuclear': {'hist': ['nuclear_ej'],
                      'fcst': ['Nuclear']},
          'Bioenergy': {'hist': ['biofuels_cons_ej', 'biogeo_ej'],
                        'fcst': ['Bioenergy']},
          'Hydro': {'hist': ['hydro_ej'],
                    'fcst': ['Hydro']},
          'Other Renewables': {'hist': 'renewables_ej',
                               'fcst': 'Other renewables'},
          'Total': {'hist': ['primary_ej'],
                    'fcst': ['Coal', 'Oil', 'Natural Gas',
                             'Nuclear', 'Bioenergy', 'Hydro']}}

# load and pre-process data
fcsts = pd.read_excel('ConsolSources.xlsx', 'Consolidated')
hists = pd.read_csv('SRofWE.csv')
allHistSer = []
for j in mapper:
    allHistSer.extend(mapper[j]['hist'])
hists = hists[(hists['Country']=='Total World') & 
              (hists['Year'] >= 2010) & 
              (hists['Var'].isin(allHistSer))]

#make a list of energy sources
enList = list(mapper.keys())

st.write("TEST")
en = st.selectbox(label="Choose an energy source to evaluate", 
                  options=enList)

#make a year range
yMin = min(min(fcsts['fcstYear']), min(hists['Year']))
yMax = max(max(fcsts['fcstYear']), max(hists['Year']))

#make a forecast range
fcstYMin = min(fcsts['RPT'])
fcstYMax = max(fcsts['RPT'])




plt = px.line(hists, x='Year', y='Value', color='Var', animation_frame='Year')


st.plotly_chart(plt)