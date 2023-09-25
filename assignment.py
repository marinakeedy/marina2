# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:03:08 2023

@author: marin
"""

import pandas as pd
import plotly.express as px
import streamlit as st

# Load the data
github_raw_url = "https://raw.githubusercontent.com/marinakeedy/marina2/main/US_Regional_Sales_Data.csv"
df = pd.read_csv(github_raw_url, encoding='utf-8')


# Create a Streamlit app
#give a title to my web page 
st.title('Global Sales')
#some information 
st.write('Explore Global Sales Data using the visuals below')

st.title('Interactive Histogram')

# Select fixed X and Y axes
x_axis = 'Unit Price'
y_axis = '_ProductID'

# Allow the user to choose the number of bins (1st interactive)
num_bins = st.slider('Select Number of Bins:', min_value=1, max_value=500, value=30)  # Adjust the max_value as needed

# Add an interpretation to guide the user 
st.write("This interactive histogram allows you to explore the distribution of data.")
st.write("You can adjust the number of bins using the slider to see the data in different levels of granularity.")
st.write(f"The X-axis represents '{x_axis}', and the Y-axis represents '{y_axis}'.")
st.write(f"Number of Bins selected: {num_bins}")

# Create the histogram 
fig3 = px.histogram(df, x=x_axis, y=y_axis, nbins=num_bins, title=f'{x_axis} vs. {y_axis}')

# Show the histogram in Streamlit
st.plotly_chart(fig3)

#now for the scatterplot 

# Convert 'OrderDate' column to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Create a Scatter plot 
st.title('Interactive Scatter Plot')

# Add an interpretation before the scatter plot
st.write("This interactive scatter plot allows you to explore and visualize the relationships between different variables in our dataset.")
st.write("Select variables for the X-axis and Y-axis to investigate how they relate to each other and discover patterns and trends.")
st.write('To change the scatter plot color, click on the color picker below and select your desired color.')

# Allow the user to customize the scatter plot
x_axis = st.selectbox('Select X-axis:', df.columns)
y_axis = st.selectbox('Select Y-axis:', df.columns)

# Allow the user to choose the scatter plot color
selected_color = st.color_picker('Select Scatter Plot Color', value='#1f77b4')  # Default color is blue

# Create the scatter plot using Plotly Express with the selected color
fig = px.scatter(df, x=x_axis, y=y_axis, title=f'{x_axis} vs. {y_axis}', color_discrete_sequence=[selected_color])
st.plotly_chart(fig)
