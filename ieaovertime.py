import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'

fcsts = pd.read_excel('ConsolSources.xlsx', 'Consolidated')

date = fcsts[(fcsts['Source']=='Coal') & (fcsts['scen']=='Stated Policies Scenario')]
plt = px.line(date, x='fcstYear', y='Value', color='RPT')
plt.show()

st.write("TEST")
st.plotly_chart(plt)
