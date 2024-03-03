# Lesson 3 multiple pages streamlit
import streamlit as st
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cufflinks as cf
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()

st.set_page_config(layout="centered")



# Title and explaination
st.header('Welcome to my data analysis project') # need to be centered
st.write('This project aims to showcase proficiency in Python, SQL, and data analysis, specifically delving into the data of Steimatzky Books 📚')


#Data info, steimatzky
@st.cache_data
def load_df(csv_loc):
    df = pd.read_csv(csv_loc)
    return df

df = load_df('https://raw.githubusercontent.com/IssacDavidi/data_project/main/steimatzky_cleaned.csv')


#Data table toggle
# Initialize button state using st.session_state
if 'show_data_table' not in st.session_state:
    st.session_state.show_data_table = False

# Show or hide button logic
if st.button('Toggle Data Table'):
    st.session_state.show_data_table = not st.session_state.show_data_table

# Show or hide data table based on button state
if st.session_state.show_data_table:
    st.dataframe(df)
    with st.expander('About the data table'):
        st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/cat2.jpg?raw=true', width=110)
        st.write('The information obtained from the Steimatzky website underwent a web scraping procedure. This dataset comprises 978 books, each available in both physical and digital formats. Any missing values were filled with averages.')



st.write("<br>", unsafe_allow_html=True) # Spacing
 



########### PLOTS

h = 600
w = 300
#Plot 1 - Average prices of books

plots_df = pd.DataFrame()
#Average price Normal VS Membership
plots_df['Normal'] = df['price_physical']
plots_df['Membership'] = df['price_club_physical']
group = ['Normal','Membership']

fig1 = px.bar(plots_df[['Normal', 'Membership']].mean(), orientation='v',
            color = group,color_discrete_map = {'Normal': 'coral', 'Membership': '#007777'})

# Update the layout for better appearance

fig1.update_layout(
    title='Average Prices of Books',
     xaxis_title='',
    yaxis_title='',
    width=w,
    height=h,  # Adjust the margins as needed
    title_x=0,  # Set the title's x-position to the center
    title_y=0.92,  # Set the title's y-position (adjust as needed)
    legend=dict(y=0,x = 0.15,traceorder='normal', orientation='h'),# Set the legend's y-position to 1 (top position)
    title_font=dict(size=24),
     margin=dict(l=0, r=0, t=80, b=80))

fig1.update_traces(marker_line_color='black', marker_line_width=1.3,showlegend=False)


#Plot 2 - Pie chart of Category

plots_df = pd.DataFrame()
plots_df = df.groupby('category').count().reset_index().loc[: , ['category','name']]

# Filtering to show only a count with 10 or more
plots_df = plots_df[plots_df['name']>15]


# Creating a Pie Chart - Count Category
fig2 = px.pie(plots_df, names ='category', values = 'name', color_discrete_sequence=px.colors.qualitative.Set2)
fig2.update_layout(
    title='Category-wise Book Count',
     xaxis_title='',
    yaxis_title='',
    plot_bgcolor='white',
    width=w,
    height=h,
    margin=dict(l=0, r=0, t=50, b=0),  # Adjust the margins as needed
    title_x=0,  # Set the title's x-position to the center
    title_y=0.69,  # Set the title's y-position (adjust as needed)
    legend=dict(y=0.5,x = 1,traceorder='normal', orientation='v'),# Set the legend's y-position to 1 (top position)
    title_font=dict(size=24),    
    annotations=[
        dict(
            text='Fig 2: fiction books stand out<br>as the most common category.',
            xref='paper', yref='paper',
            x=0.3, y=0.15,  # Adjust the position of the subtitle
            showarrow=False,
            font=dict(size=18)  # Adjust the font size of the subtitle
        )
    ])


# Add black marker line color
fig2.update_traces(marker_line_color='black', marker_line_width=0.8)

#Plot 3: Top 5 authors - Pie Chart
plots_df = pd.DataFrame()
plots_df = df.groupby('author').count()['name'].sort_values(ascending=False).reset_index()
plots_df.columns = ['author', 'count']

fig3 = px.pie(plots_df[0:6], names='author', values='count', color_discrete_sequence=px.colors.qualitative.Set3)
fig3.update_layout(
    title='Top 5 Authors<br>with the most published books',
    xaxis_title='',
    yaxis_title='',
    plot_bgcolor='white',
    width=w,
    height=h,
    margin=dict(l=0, r=0, t=50, b=0),  # Adjust the margins as needed
    title_x=0,  # Set the title's x-position to the center
    title_y=0.77,  # Set the title's y-position (adjust as needed)
    legend=dict(y=0.5,x=1),# Set the legend's y-position to 1 (top position)
    title_font=dict(size=24),
    annotations=[
        dict(
            text='Pie Charts',
            xref='paper', yref='paper',
            x=0, y=0.97,  # Adjust the position of the subtitle
            showarrow=False,
            font=dict(size=32)  # Adjust the font size of the subtitle
        )
    ]
)

# Add black marker line color
fig3.update_traces(marker_line_color='black', marker_line_width=0.8)

# plot 4 - sub category , Filtered , 10 and above
plots_df = pd.DataFrame
plots_df = df.groupby('sub_category').count().reset_index().loc[: , ['sub_category', 'name']]
plots_df = plots_df[plots_df['name'] > 20]

fig4 = px.pie(plots_df, names = 'sub_category', values = 'name', color_discrete_sequence = px.colors.qualitative.Prism)

fig4.update_layout(title='Distribution of Books<br>by Subcategory',
     xaxis_title='',
    yaxis_title='',
    plot_bgcolor='white',
    width=w,
    height=h,
    margin=dict(l=0, r=0, t=50, b=0),  # Adjust the margins as needed
    title_x=0,  # Set the title's x-position to the center
    title_y=0.73,  # Set the title's y-position (adjust as needed)
    legend=dict(y=0.5,x = 1,traceorder='normal', orientation='v'),# Set the legend's y-position to 1 (top position)
    title_font=dict(size=24),    
    annotations=[
        dict(
            text='Fig 3: Translated fiction books stand out<br>as the most common subcategory.',
            xref='paper', yref='paper',
            x=0.2, y=0.2,  # Adjust the position of the subtitle
            showarrow=False,
            font=dict(size=16)  # Adjust the font size of the subtitle
        )
    ])

# Add black marker line color
fig4.update_traces(marker_line_color='black', marker_line_width=0.8,showlegend=True)

#### END OF PLOTS


# Data insights button
# Initialize button state using st.session_state
if 'show_insights' not in st.session_state:
    st.session_state.show_insights = False

# Show or hide button logic
if st.button('Toggle insights'):
    st.session_state.show_insights = not st.session_state.show_insights

# Show or hide data table based on button state
if st.session_state.show_insights:
    # Header 1
    st.header('Data insights')
        
        

    mcol1, mcol2, mcol3, mcol4= st.columns(4) # Metrics columns
        #Physical Copies
    with mcol1:
        st.metric(label='Physical Copy', value = '97₪')

    with mcol2:
        st.metric(label='Sale Price', value = '77₪', delta = '-20.6%', delta_color='inverse')

    #Digital
    with mcol3:
        st.metric(label='Digital Copy', value = '42₪', delta = '-56.7%', delta_color='inverse')

    with mcol4:
        st.metric(label='Digital Sale', value = '33₪', delta= '-65.9%', delta_color='inverse')





    col1, col2, col3, col4, col5 = st.columns((1, 1, 5, 1,1 ))
    with col3:
        st.plotly_chart(fig3, use_container_width=True)# Top authors
        st.plotly_chart(fig2, use_container_width=True) #Sub Category Count
        st.plotly_chart(fig4, use_container_width=True) #Physical VS Digital
        st.plotly_chart(fig1, use_container_width=True) # Count Categories


    


