import streamlit as st
from sqlalchemy import create_engine
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header 
import streamlit_extras
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

#st.set_page_config(page_icon = '✨', page_title='👉Books Project📚')

# Allow vertical radio buttons
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#SQL query, steimatzky dataset
def sql_query(query):
    global new_df
    global sql_df
    pysqldf = lambda q: sqldf(q, globals())
    sql_df = pd.read_csv('https://raw.githubusercontent.com/IssacDavidi/data_project/main/steimatzky_cleaned.csv')
    new_df = pysqldf(query)
    return st.dataframe(new_df)


# Plots
# data for plots
def load_df(csv_loc):
    df = pd.read_csv(csv_loc)
    return df


# Title and explaination
colored_header(label ='✨Welcome to SQL section.✨', color_name="violet-70" , description ="")  # Centered title
st.write('This section will do its best to show sql skills')


type_query = st.radio('Choose which Query would you like to run.',['Top 5 Authors','Common Category','Common Sub Category','Price Comparison','String Concatenation'])

if type_query == 'Top 5 Authors': # Choose Author Example
    query_text = ''' select count(name) as books_amount,
author
from sql_df
group by author
order by books_amount desc
limit 5;'''

elif type_query == 'Common Category':
    query_text = '''SELECT count(category) as category_count,
category
from sql_df
group by category
order by category_count desc
LIMIT 10;'''

elif type_query == 'Common Sub Category':
    query_text = '''SELECT  count(sub_category) as sub_category_count,
sub_category
from sql_df
group by sub_category
order by sub_category_count desc
LIMIT 10;'''

elif type_query == 'Price Comparison':
    query_text = '''select 'עותק פיזי יותר יקר ב-' ||ROUND(((ROUND(AVG(price_physical))/ROUND(AVG(price_digital))) - 1) *100,2) || '%' as precent_change,
ROUND(AVG(price_physical)) as avg_physical_price, 
ROUND(AVG(price_digital))  as  avg_digital_price,
category
from sql_df
group by category'''

elif type_query == 'String Concatenation':
    query_text = '''select   '"' || name || '"'  || ' '||  'הוא ספר מאת' || ' ' || author || ' ' || 'ומחירו המלא הינו' || '  ' || price_physical || '₪'  as books_details
from sql_df
'''


#query 1
query = st.text_area('Please provide a SQL query', query_text, height = 150)
if st.button('Run query'):
    try:
        sql_query(query)
        st.success(f'Query ran successfully! returned {len(new_df)} rows and {len(new_df.columns)} columns.', icon = '✅')
       # if type_query == 'Top 5 Authors':
        #    pass
            #st.bar_chart(data = new_df ,y = new_df.columns[0], x = new_df.columns[1], use_container_width=True)
      #  elif type_query == 'Common Category':
       #     pass
            #st.scatter_chart(data = new_df ,y = new_df.columns[1], x = new_df.columns[0], use_container_width=True)
     #   elif type_query == 'Common Sub Category':
      #      pass
            #st.scatter_chart(data = new_df ,y = new_df.columns[1], x = new_df.columns[0], use_container_width=True)
      #  elif type_query == 'Price Comparison':
      #      pass
            #st.scatter_chart(data = new_df ,y = new_df.columns[2], x = new_df.columns[1],color = new_df.columns[3], use_container_width=True)
    except:
        st.error(':x: An error occoured running the query provided')

## TO DO : for each A B C in radio , each button change the sql text area text .
# Maybe add graph based on condition

