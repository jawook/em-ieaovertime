import streamlit as st
import pandas as pd
import plotly.express as px

fcsts = pd.read_excel('ConsolSources.xlsx', 'Consolidated')

date = fcsts[(fcsts['Source']=='Coal') & (fcsts['scen']=='Stated Policies Scenario')]
plt = px.line(date, x='fcstYear', y='Value', color='RPT')

st.write("TEST")
st.plotly_chart(plt)
