# from inspect import EndOfBlock
# from turtle import end_fill, title
import streamlit as st
# import numpy as np
import pandas as pd
# import csv
# import sweetviz as sv
# import IPython
import matplotlib.pyplot as plt
import seaborn as sns
    
def visualisation(df, x, y, sum_mean, line_bar):
    
    if(sum_mean == "sum"):
        data = df.groupby(x)[y].sum().sort_values()
    else:
        data = df.groupby(x)[y].mean().sort_values()
        
    df1 = pd.DataFrame(data)
    st.write(df1)
    
    plt.figure(figsize=(15,5))
    pal = sns.color_palette("Blues", len(data))
    
    if line_bar == "line":
        sns.lineplot(x=data.index , y=data , palette=pal)
    else:
        sns.barplot(x=data.index , y=data , palette=pal)
        
    plt.xticks(rotation=70)

    plt.title(x + " v/s "+ y + " graph")

    plt.savefig(x+"_"+y+".png", bbox_inches="tight")
    
    st.image(x+"_"+y+".png")

default_file = ("cars_engage_2022.csv")

@st.cache
def load_csv(file):
        csv = pd.read_csv(file)
        return csv
    
# @st.cache
def app():
    st.markdown("## Analysis On Cars Dataset")
    flag = 0
    st.markdown("### The Dataset") 
    st.write("\n")
    df = load_csv(default_file)
    st.write(df)
    # placeholder = st.sidebar.empty()
    # placeholder.checkbox("###Basic Analysis")
    # if st.sidebar.checkbox("Data Comprehension"):
    #     st.markdown("###Data Comprehension")
    #     st.write(df.info())
    if st.sidebar.checkbox("Basic Analysis"):
        # st.markdown("### Data Comprehension")
        # st.markdown(df.info())
        # df.info()
        
        st.markdown("### Unique Observations In Each Column")
        for i in df:
            st.write(i)
            st.markdown(df[i].unique().tolist())
            st.write("---")
            
        st.markdown("### Number of Missing Cells in Each Column")    
        st.write(df.isnull().sum())
        
    if st.sidebar.checkbox("Count Similar Models"):
        st.markdown("### Number of Similar Car Models")    
        st.write(df.groupby(['Model']).count())
    
    if st.sidebar.checkbox("Count Models with Similar Make"):
        st.markdown("### Number of Models with Similar Make")    
        st.write(df.groupby(['Make']).count())
    
    if st.sidebar.checkbox("Count Models with Similar Variant"):
        st.markdown("### Number of Models with Similar Variant")    
        st.write(df.groupby(['Variant']).count())
        
#     import sweetviz as sv

# my_report = sv.analyze(my_dataframe)
# my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"