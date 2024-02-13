import streamlit as st
import pandas as pd
import plotly.express as px

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
                    'fcst': ['Hydro']}}

fcsts = pd.read_excel('ConsolSources.xlsx', 'Consolidated')
hists = pd.read_csv('SRofWE.csv')
allHistSer = []
for j in mapper:
    allHistSer.extend(mapper[j]['hist'])
hists = hists[(hists['Country']=='Total World') & 
              (hists['Year'] >= 2000) & 
              (hists['Var'].isin(allHistSer))]

plt = px.line(hists, x='Year', y='Value', animation_frame='Year')

st.write("TEST")
st.plotly_chart(plt)