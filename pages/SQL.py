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
    sql_df = pd.read_csv('https://raw.githubusercontent.com/IssacDavidi/data_project/main/ETL_py_files/steimatzky_cleaned.csv')
    new_df = pysqldf(query)
    return st.dataframe(new_df)


########### PLOTS
@st.cache_data
def load_df(csv_loc):
    df = pd.read_csv(csv_loc)
    return df

df = load_df('https://raw.githubusercontent.com/IssacDavidi/data_project/main/ETL_py_files/steimatzky_cleaned.csv')

w= 800
h= 400
# Plot 1 - Average prices of books
plots_df_1 = pd.DataFrame()
plots_df_1['Normal'] = df['price_physical']
plots_df_1['Membership'] = df['price_club_physical']
group = ['Normal', 'Mermbership']

fig1 = px.bar(plots_df_1[['Normal', 'Membership']].mean(), orientation='h',
              width=800, height=400,
              color=group, color_discrete_map={'Normal': 'coral', 'Membership': '#007777'})

# Update the layout for better appearance
fig1.update_layout(
    title='Average Prices of Books',
    xaxis_title='',
    yaxis_title='',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    width=w,
    height=h,
    legend=dict(y=1)
)

fig1.update_traces(marker_line_color='black', marker_line_width=1.3)

# Plot 2 - Pie chart of Category
plots_df_2 = df.groupby('category').count().reset_index().loc[:, ['category', 'name']]
plots_df_2 = plots_df_2[plots_df_2['name'] > 9]

fig2 = px.pie(plots_df_2, names='category', values='name', color_discrete_sequence=px.colors.qualitative.Set2)
fig2.update_layout(
    title='Count Category',
    xaxis_title='',
    yaxis_title='',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    width=w,
    height=h,
    legend=dict(y=0.95, x=1)
)

# Add black marker line color
fig2.update_traces(marker_line_color='black', marker_line_width=0.8)

# Plot 3: Top 5 authors - Pie Chart
plots_df_3 = df.groupby('author').count()['name'].sort_values(ascending=False).reset_index()
plots_df_3.columns = ['author', 'count']

fig3 = px.pie(plots_df_3[0:6], names='author', values='count', color_discrete_sequence=px.colors.qualitative.Set3)
fig3.update_layout(title='Top 5 Authors with the most published books', xaxis_title='', yaxis_title='',
                   plot_bgcolor='white', legend=dict(y=0.95, x=0),
                   width=w,
                   height=h)

# Add black marker line color
fig3.update_traces(marker_line_color='black', marker_line_width=0.8)

# Plot 4 - Sub-category, Filtered, 10 and above
plots_df_4 = df.groupby('sub_category').count().reset_index().loc[:, ['sub_category', 'name']]
plots_df_4 = plots_df_4[plots_df_4['name'] > 9]

fig4 = px.pie(plots_df_4, names='sub_category', values='name', color_discrete_sequence=px.colors.qualitative.Prism)
fig4.update_layout(title='Sub Category Count', xaxis_title='',
                   yaxis_title='',
                   plot_bgcolor='rgba(0,0,0,0)',
                   paper_bgcolor='rgba(0,0,0,0)',
                   legend=dict(y=0.95, x=1),
                   width=w,
                   height=h
                   )

# Add black marker line color
fig4.update_traces(marker_line_color='black', marker_line_width=0.8)


#Plot 5
prices_df = df.loc[: , ['price_physical', 'price_sale_physical', 'price_digital', 'price_sale_digital']]
fig5 = px.box(prices_df, y=prices_df.columns)


#### END OF PLOTS





# Plots
@st.cache_data
def load_df(csv_loc):
    df = pd.read_csv(csv_loc)
    return df


# Title and explaination
st.header('SQL Proficiency: A Showcase', divider = 'rainbow') # Centered title
st.write('In this section, I showcase my proficiency in SQL through a series of queries and examples.')


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
    query_text = '''select
ROUND(AVG(price_physical)) as physical_price, 
ROUND(AVG(price_digital))  as  digital_price,
ROUND(AVG(price_sale_physical))  as  sale_physical,
ROUND(AVG(price_sale_digital))  as  sale_digital,
category
from sql_df
group by category;'''

elif type_query == 'String Concatenation':
    query_text = '''select   '"' || name || '"'  || ' '||  'הוא ספר מאת' || ' ' || author || ' ' || 'ומחירו המלא הינו' || '  ' || price_physical || '₪'  as books_details
from sql_df
'''
def viz():
    st.subheader('Visualization', divider = 'orange')

#query 1
query = st.text_area('Please provide a SQL query', query_text, height = 150)
if st.button('Run query'):
    try:
        sql_query(query)
        st.success(f'Query ran successfully! returned {len(new_df)} rows and {len(new_df.columns)} columns.', icon = '✅')
        if type_query == 'Common Category':
            viz()
            st.plotly_chart(fig2, use_container_width=True)
            st.write(':blue[Fiction books stand out as the most common category.]')
        if type_query == 'Common Sub Category':
            viz()
            st.plotly_chart(fig4, use_container_width=True)
            st.write(':blue[Translated fiction books stand out as the most common subcategory.]')
        if type_query == 'Top 5 Authors':
            viz()
            st.plotly_chart(fig3, use_container_width=True)
            st.write(':blue[Dana Levi has the highest number of books in our dataset.]')
        if type_query == 'Price Comparison':
            viz()


            with st.container():
                st.write(':blue[Below are the metrics illustrating the average price for each column.]')
                mcol1, mcol2, mcol3, mcol4 = st.columns(4)  # Metrics columns
                
                # Physical Copies
                with mcol1:
                    st.metric(label=':orange[Physical Copy]', value='97₪')
                
                with mcol2:
                    st.metric(label=':orange[Sale Price]', value='77₪', delta='-20.6%', delta_color='inverse')
                
                # Digital
                with mcol3:
                    st.metric(label=':orange[Digital Copy]', value='42₪', delta='-56.7%', delta_color='inverse')
                
                with mcol4:
                    st.metric(label=':orange[Digital Sale]', value='33₪', delta='-65.9%', delta_color='inverse')
                st.plotly_chart(fig5)
    except:
        st.error(':x: An error occoured running the query provided')
# Footer

footer="""<style>
a:link, a:visited {
  color: blue;
  background-color: transparent;
  text-decoration: underline;
}

a:hover, a:active {
  color: red;
  background-color: transparent;
  text-decoration: underline;
}

.footer {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: #22242b;
  color: white;
  text-align: center;
}
</style>

<div class="footer">
  <p style="font-size: 4px"> </p>
  <p style="font-size: 16px">
    Copyright © 2024 Itzhak Davidi <br>
    This project is for educational purposes only and should not be used for commercial purposes or distributed without permission.
  </p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)



