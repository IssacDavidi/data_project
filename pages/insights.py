import streamlit as st
from sqlalchemy import create_engine
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






@st.cache_data
def load_df(csv_loc):
    df = pd.read_csv(csv_loc)
    return df

df = load_df('https://raw.githubusercontent.com/IssacDavidi/data_project/main/steimatzky_cleaned.csv')
        # Data insights button


st.write("<br>", unsafe_allow_html=True)  # Spacing

########### PLOTS


# Plot 1 - Average prices of books

plots_df = pd.DataFrame()
# Average price Normal VS Membership
plots_df['Normal'] = df['price_physical']
plots_df['Membership'] = df['price_club_physical']
group = ['Normal', 'Membership']

fig1 = px.bar(plots_df[['Normal', 'Membership']].mean(), orientation='v',
              color=group, color_discrete_map={'Normal': 'coral', 'Membership': '#007777'})

# Update the layout for better appearance
fig1.update_layout(
    title='Average Prices of Books',
    autosize=True
)
fig1.update_traces(marker_line_color='black', marker_line_width=1.3, showlegend=False)

# Plot 2 - Pie chart of Category
plots_df = pd.DataFrame()
plots_df = df.groupby('category').count().reset_index().loc[:, ['category', 'name']]

# Filtering to show only a count with 10 or more
plots_df = plots_df[plots_df['name'] > 15]

# Creating a Pie Chart - Count Category
fig2 = px.pie(plots_df, names='category', values='name', color_discrete_sequence=px.colors.qualitative.Set2)
fig2.update_layout(
    title='Category-wise Book Count', 
    autosize=True
)

# Add black marker line color
fig2.update_traces(marker_line_color='black', marker_line_width=0.8)

# Plot 3: Top 5 authors - Pie Chart
plots_df = pd.DataFrame()
plots_df = df.groupby('author').count()['name'].sort_values(ascending=False).reset_index()
plots_df.columns = ['author', 'count']

fig3 = px.pie(plots_df[0:6], names='author', values='count', color_discrete_sequence=px.colors.qualitative.Set3)
fig3.update_layout(
    title='Top 5 Authors<br>with the most published books',
     autosize=True)


# Add black marker line color
fig3.update_traces(marker_line_color='black', marker_line_width=0.8)

# plot 4 - sub category , Filtered , 10 and above
plots_df = pd.DataFrame
plots_df = df.groupby('sub_category').count().reset_index().loc[:, ['sub_category', 'name']]
plots_df = plots_df[plots_df['name'] > 25]

fig4 = px.pie(plots_df, names='sub_category', values='name', color_discrete_sequence=px.colors.qualitative.Prism)

fig4.update_layout(title='Distribution of Books<br>by Subcategory',
    autosize=True)

# Add black marker line color
fig4.update_traces(marker_line_color='black', marker_line_width=0.8, showlegend=True)

#### END OF PLOTS



# Insights button trigger
    # Header 1
colored_header(label =':orange[Data] insights', color_name="violet-70" , description ="")

mcol1, mcol2, mcol3, mcol4 = st.columns(4)  # Metrics columns
# Physical Copies
with mcol1:
    st.metric(label='Physical Copy', value='97₪')

with mcol2:
    st.metric(label='Sale Price', value='77₪', delta='-20.6%', delta_color='inverse')

# Digital
with mcol3:
    st.metric(label='Digital Copy', value='42₪', delta='-56.7%', delta_color='inverse')

with mcol4:
     st.metric(label='Digital Sale', value='33₪', delta='-65.9%', delta_color='inverse')


st.plotly_chart(fig3, use_container_width=True)  # Top authors
st.write('Fig1: the author with the most published books is Dana Levi.')
st.plotly_chart(fig2, use_container_width=True)  # Sub Category Count
st.write('Fig 2: fiction books stand out<br>as the most common category.')
st.plotly_chart(fig4, use_container_width=True)  # Physical VS Digital
st.write('Fig 3: Translated fiction books stand out as the most common subcategory.')
#st.plotly_chart(fig1, use_container_width=True)  # Count Categories


