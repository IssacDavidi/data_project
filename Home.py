import streamlit as st
from sqlalchemy import create_engine
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header 
import pandas as pd
from pandasql import sqldf
import numpy as np
import matplotlib.pyplot as plt
import cufflinks as cf
import plotly.express as px
import os
import csv
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)
cf.go_offline()

st.set_page_config(page_icon = '✨', page_title='👉Books Project📚')




#SQL query, steimatzky dataset
def sql_query(query):
    global new_df
    global sql_df
    pysqldf = lambda q: sqldf(q, globals())
    sql_df = pd.read_csv('https://raw.githubusercontent.com/IssacDavidi/data_project/main/steimatzky_cleaned.csv')
    new_df = pysqldf(query)
    return st.dataframe(new_df)

if 'expander_triggered' not in st.session_state:
    st.session_state.expander_triggered = False


# Title and explaination
colored_header(label ='✨Welcome to my :blue[data analysis] project✨', color_name="violet-70" , description ="")  # Centered title
st.write('This project aims to showcase proficiency in Python, SQL, and data analysis, specifically delving into the data of Steimatzky Books 📚')

# Data table toggle
# Initialize button state using st.session_state
if 'show_data_table' not in st.session_state:
    st.session_state.show_data_table = False

# Show or hide button logic
if st.button('Get Started!'):
    st.session_state.show_data_table = not st.session_state.show_data_table

if "button" not in st.session_state:
    st.session_state.button = False

# Get Started trigger
if st.session_state.show_data_table:


    query = st.text_area('Please provide a SQL query', '''SELECT * 
        FROM sql_df
        LIMIT 5;
        ''')
    if st.button('Run query'):
        try:
            sql_query(query)
            st.success(f'Query ran successfully! returned {len(new_df)} rows and {len(new_df.columns)} columns.', icon = '✅')

            with st.expander('What is this table?'):
                st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/cat2.jpg?raw=true', width=110)
                st.subheader('General info', divider='rainbow')
                st.write('''👉 This table contains 10 columns and 978 rows, obtained from the Steimatzky website through a web scraping and ETL (Extract, Transform, Load) procedure with Python.
                 Each row represents a book available in both physical and digital formats. Any missing values were filled with averages values. 
       ''')
               #st.subheader('How this project made', divider='rainbow')
               #st.write('name - The book name')
               #st.write('author - the person who wrote the book')
               #st.write('price physical - the price for a physical copy of a book')
               #st.write('price digital - same for digital copy')
               #st.write('description - what is the book about')
        except:
            st.error(':x: An error occoured running the query provided')
    if st.button("Next Page"):
        switch_page('sql')

# REWRITE THE CODE WITH SESSION STATE FOR EACH BUTTON
