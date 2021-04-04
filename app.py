import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import norm

st.write("""

# Safety Stock & Reorder Level Calculator!
    
""")

st.sidebar.header('Enter Last 6 Months Sales History, Procurement Lead Time & Desired Service Level')
Month1 = st.sidebar.number_input('Month1')
Month2 = st.sidebar.number_input('Month2')
Month3 = st.sidebar.number_input('Month3')
Month4 = st.sidebar.number_input('Month4')
Month5 = st.sidebar.number_input('Month5')
Month6 = st.sidebar.number_input('Month6')
LeadTime = st.sidebar.number_input('Lead Time in Months')
ServiceLevel = st.sidebar.slider('Service Level', 0.90, 0.95, 0.99)

demand = pd.DataFrame({'Month':[1,2,3,4,5,6], 'Demand': [Month1,Month2,Month3,Month4,Month5,Month6]})

LT= pd.DataFrame({'LeadTime':[LeadTime]})
SL= ServiceLevel
st.subheader('Input Data')
st.write('Demand', demand)
st.write('Lead Time in Months', LeadTime)
st.write('Service Level', SL)

forecast_demand = (Month1+Month2+Month3+Month4+Month5+Month6)/6
Lead_Time_Demand = forecast_demand*LeadTime
Standard_Deviation = demand['Demand'].std()
Service_Factor = norm.ppf(SL)
Lead_Time_Factor =np.sqrt(LeadTime)
Safety_Stock = Standard_Deviation*Service_Factor*Lead_Time_Factor
Reorder_Point = Safety_Stock+Lead_Time_Demand

st.subheader('Calculated Safety Stock & Reorder Point')
st.write('Safety Stock is', round(Safety_Stock,2))
st.write('Reorder Point is', round(Reorder_Point,2))
