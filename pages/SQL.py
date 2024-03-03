import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import os
from pandasql import sqldf





col1, col2, col3 = st.columns((2,1,1))

with col1:
  st.subheader('Lorem ipsum dolor sit amet')
  st.write('consectetur adipiscing elit. Praesent tristique quis sem ut tempus. Curabitur in dui in nibh posuere fringilla.')
  st.write('Nulla facilisi. Ut quis consectetur leo. Cras mollis sapien nec dolor ultricies elementum. Cras tempor ipsum vel ex ullamcorper, eget feugiat neque lobortis. Fusce nec lectus risus.')
with col3:
  st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/cat1.png?raw=true', 'A beautiful cat', width=600)

#Data info, steimatzky
def sql_query(query):
    global df
    pysqldf = lambda q: sqldf(q, globals())
    df = pd.read_csv('https://raw.githubusercontent.com/IssacDavidi/data_project/main/steimatzky_cleaned.csv')
    new_df = pysqldf(query)
    return new_df

sql_query('select * from df limit 2')
  

