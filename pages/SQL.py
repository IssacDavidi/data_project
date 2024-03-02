import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd


def sql_query(txt, table_name='books'):
    # Use SupabaseConnection and provide the URL and API key
    conn = st.connection("supabase", type=SupabaseConnection)
    
    # Assuming SyncSelectRequestBuilder has an execute method to get a DataFrame
    df = conn.query(txt, table=table_name).execute()
    
    return df

query = st.text_area('Explore the data by running SQL queries', 'SELECT * FROM books;')
if st.button('Run Query'):
    result = sql_query(query)
    st.dataframe(result)
