import streamlit as st
# import numpy as np
import pandas as pd
# import csv
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


default_file = ("cars_engage_2022.csv")
default_file1 = ("merc.csv")

@st.cache
def load_csv(file):
        csv = pd.read_csv(file)
        return csv
    
# @st.cache
def app():
    st.markdown("## Comprehensive Exploratory Analysis")
    flag = 0
    st.markdown("### Upload a csv file for analysis.") 
    st.write("\n")

    uploaded_file = st.file_uploader("Choose a file", type = ['csv'])
    
    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        flag = 1
        
    else:
        placeholder = st.empty()
        placeholder.info('Awaiting for CSV file to be uploaded.')
        
        
    if st.button('Press to use cars dataset'):
        df = load_csv(default_file)
        flag =1 
        placeholder.empty()
        
    if st.button('Press to use merecedes dataset'):
        df = load_csv(default_file1)
        flag =1 
        placeholder.empty()
        
    if flag == 1:
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Exploratory Data Analysis Report**')
        st_profile_report(pr)
        
    