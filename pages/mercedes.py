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

default_file = ("merc.csv")

@st.cache
def load_csv(file):
        csv = pd.read_csv(file)
        return csv
    
# @st.cache
def app():
    st.markdown("## Analysis On Mercedes Dataset")
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
        st.markdown("### Number of Similar Mercedes Models")    
        st.write(df.groupby(['model']).count())
    
    if st.sidebar.checkbox("Model v/s Miles Per Gallon"):
        st.markdown("### Model v/s Miles Per Gallon")  
        visualisation(df, 'model', 'mpg', 'mean', 'line')  
        st.markdown("""When the miles per gallon mean value is greater, 
                    the automobile can drive further than when the mean 
                    value is lower.
                    \nThe number of models that have a higher 
                    miles per gallon than average is about 14""")
        
    if st.sidebar.checkbox("Model v/s Price"):
        st.markdown("### Model v/s Price") 
        visualisation(df, 'model', 'price', 'sum', 'line')   
        st.markdown("""As we can see in the graph, C Class is the most expensive
                    model followed by A Class and E Class whereas
                    CLC Class is the cheapest model followed by R Class and CLK.""")
        
    if st.sidebar.checkbox("Model v/s Mileage"):
        st.markdown("### Model v/s Mileage")  
        visualisation(df, 'model', 'mileage', 'mean', 'line')  
        st.markdown("""Models with higher mpg values have less fuel consumption,
                    lower maintenance costs and better long distance performance.
                    \nThe number of models that have a better mileage performance
                    than the median is 11.""")
        
    if st.sidebar.checkbox("Year v/s Price"):
        st.markdown("### Year v/s Price")    
        visualisation(df, 'year', 'price', 'sum', 'line')
        st.markdown("""As we can see in the graph, the prices have been growing
                    except for 2019 and 2020 where the sales dropped 
                    due to the pandemic.
                    \n Also, In the late 2010s we can see a 
                    sudden spike in the prices of the cars.""")
        
    if st.sidebar.checkbox("Mileage v/s Transmission"):
        st.markdown("### Mileage v/s Transmission")    
        model_transmission = sns.barplot(x='mileage', y='transmission', data=df)
        st.write(model_transmission)
        plt.title('mileage v/s Transmission graph')
        plt.savefig("model_transmission.png", bbox_inches="tight")
        st.image("model_transmission.png")
        st.markdown("""As we can see from the graph, manual transmission gives the best mileage amongst 
                    all the transmission systems""")
    
    if st.sidebar.checkbox("Model v/s Tax"):
        st.markdown("### Model v/s Tax")    
        visualisation(df, 'model', 'tax', 'sum', 'bar')
        st.markdown("""Mercedes C class it has a far higher road tax 
                    than the Mercedes A class, by 9.29 percent.
                    \nA class vehicle would be a better choice than 
                    a C class model, When it comes to miles per gallon and price""")
    
    if st.sidebar.checkbox("Fueltype v/s Mileage"):
        st.markdown("### Fueltype v/s Mileage")    
        visualisation(df, 'fuelType', 'mileage', 'sum', 'bar')
        st.markdown("""For long distance travel, diesel engines are better.""") 
        
    if st.sidebar.checkbox("Conclusion"):
        st.markdown("### Conclusion") 
        st.markdown("""Mileage determines the cost of maintaining a car.""") 
        st.markdown("""Manual transmissions are lighter and have simple designs.""")
        st.markdown("""Diesel engines are restricted for bigger vehicles
                    and vehicles that travel often due to a higher 
                    negative effect on the environment.""")
        st.markdown("""Miles per gallon number should be greater than 
                    30 miles/gallon for all the people who want a car
                    for daily use or for travelling a lot.""") 
    
    

        
    
        
        
        
    
    