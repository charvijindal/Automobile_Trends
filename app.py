import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import eda, mercedes,cars
#"', machine_learning, metadata, data_visualize, redundant # import your pages here'"

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# st.markdown("<h1 style='text-align: center; '>Data Analysis</h1>", unsafe_allow_html=True)

display = Image.open('Logo.png')
display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Analysis")
# st.markdown<img src="Logo.jpg" class="center">
col1, col2 = st.columns(2)
col1.image(display, width = 300)
# col2.st.text(" ")
col2.title("Data Analysis To Determine Automobile Trends")

# Add all your application here
app.add_page("Upload and Analyse the Data", eda.app)
app.add_page("Analysis On Merecedes Dataset", mercedes.app)
app.add_page("Analysis On Cars Dataset", cars.app)
# app.add_page("Data Analysis",data_visualize.app)
# app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()