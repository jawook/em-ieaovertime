import streamlit as st
import pandas as pd
import plotly.express as px

# dictionary to map data
enMap = {'Coal': {'hist': ['coalcons_ej'], 
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

plMap = {'Current Policies': ['Current Policies Scenario', 
                               'Stated Policies Scenario'],
          'New Policies': ['New Policies Scenario', 
                           'Announced Pledges Scenario'],
          'Aspirational Policies': ['450 Scenario', 
                                    'Sustainable Development Scenario',
                                    'Net Zero 2050 Scenario']}

# load and pre-process data
fcsts = pd.read_excel('ConsolSources.xlsx', 'Consolidated')
# need to exclude the SDS scenario in 2021 (both SDS and Net Zero are aspirational)
fcsts = fcsts[~((fcsts['RPT'] == 2021) & (fcsts['scen']=='Sustainable Development Scenario'))]
hists = pd.read_csv('SRofWE.csv')
allHistSer = []
for j in enMap:
    allHistSer.extend(enMap[j]['hist'])
hists = hists[(hists['Country']=='Total World') & 
              (hists['Year'] >= 2010) & 
              (hists['Var'].isin(allHistSer))]

#make a list of energy sources
enList = list(enMap.keys())
scList = list(plMap.keys())


st.write("TEST")
en = st.selectbox(label="Choose an energy source to evaluate:", 
                  options=enList)
sc = st.selectbox(label='Choose a set of policy scenarios to evaluate:',
                  options=scList)

# create a list for the selected items
lvFcsts = fcsts[(fcsts['scen'].isin(plMap[sc])) & (fcsts['Source'].isin(enMap[en]['fcst']))]
lvFcsts = lvFcsts[['fcstYear', 'Value', 'RPT']]
lvHist = hists[hists['Var'].isin(enMap[en]['hist'])]
lvHist['RPT'] = 'History'
lvHist.rename(columns={'Year': 'fcstYear'}, inplace=True)
lvHist = lvHist[['fcstYear', 'Value', 'RPT']]
lvHist['Value'] = lvHist['Value'] * 23.88
lvAll = pd.concat([lvFcsts, lvHist])
plt = px.scatter(lvAll, x='fcstYear', y='Value', color='RPT')

#make a year range
yMin = min(min(fcsts['fcstYear']), min(hists['Year']))
yMax = max(max(fcsts['fcstYear']), max(hists['Year']))

#make a forecast range
fcstYMin = min(fcsts['RPT'])
fcstYMax = max(fcsts['RPT'])




# plt = px.line(hists, x='Year', y='Value', color='Var', animation_frame='Year')


st.plotly_chart(plt)