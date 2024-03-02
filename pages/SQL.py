import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd

@st.cache_data
def sql_query(txt, table_name='books'):
    # Use SupabaseConnection and provide the URL and API key
    conn = st.connection("supabase", type=SupabaseConnection)
    
    # Specify the columns explicitly in the query
    query = f'SELECT column1, column2, ... FROM {table_name};'
    
    # Assuming SyncSelectRequestBuilder has an execute method to get a DataFrame
    df = conn.query(query).execute()
    
    return df

query = st.text_area('Explore the data by running SQL queries', 'SELECT column1, column2, ... FROM books;')
if st.button('Run Query'):
    result = sql_query(query)
    st.dataframe(result)
