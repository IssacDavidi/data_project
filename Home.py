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
    sql_df = pd.read_csv('https://raw.githubusercontent.com/IssacDavidi/data_project/main/ETL_py_files/steimatzky_cleaned.csv')
    new_df = pysqldf(query)
    return st.dataframe(new_df)

if 'expander_triggered' not in st.session_state:
    st.session_state.expander_triggered = False


# Title and explaination
st.write("""
<div style='background-color:#0E1117; padding:10px; border-radius:5px;'>
<h2 style='color:#0E1117; text-align:center;'>
<span style='color:#f5f5f5;'>Exploring the Bookshelf: An Insightful Analysis of Steimatzky's Book Catalog
</h2>
</div>
""", unsafe_allow_html=True)
st.subheader('',divider='rainbow')
st.write(":orange[Project Overview:] This project demonstrates my proficiency in Python, SQL, and data analysis techniques. The primary focus is an in-depth exploration of Steimatzky Books' data, a prominent book retailer. Through this analysis, I aim to uncover valuable insights and patterns within Steimatzky's book catalog.")
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
                st.subheader('👉General Info', divider='rainbow')
                st.write('''- The data presented is a tabular format comprising 10 columns and 978 rows. It was acquired from the Steimatzky website through a web scraping and ETL (Extract, Transform, Load) process executed using Python programming language.''')
                st.write('''- The data resides in a cloud environment, requiring the establishment of a new connection for every query execution to access and retrieve the relevant information.''')
                st.write('''- Each row signifies a book that is obtainable in both physical and digital formats. Any missing data points were substituted with average values.''')
                st.write('''- Terminology: Physical - a tangible book edition; Digital - an electronic version of a book.''')
                st.write('''- For comprehensive insights into the methodologies employed in data collection and transformation, you can refer to my [GitHub repository.](https://github.com/IssacDavidi/data_project)''')
        except:
            st.error(':x: An error occoured running the query provided')
    if st.button("Next Page"):
        switch_page('sql')

