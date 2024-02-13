import streamlit as st
import pandas as pd
import plotly.express as px

fcsts = pd.read_excel('ConsolSources.xlsx', 'Consolidated')
hists = pd.read_excel('ConsolSources.xlsx', 'History')

date = fcsts[(fcsts['Source']=='Coal') & (fcsts['scen']=='Stated Policies Scenario')]
plt = px.line(date, x='fcstYear', y='Value', color='RPT')

st.write("TEST")
st.plotly_chart(plt)