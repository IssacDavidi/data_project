import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd
import sqlalchemy

@st.cache_data
def sql_query(txt):
    conn = SupabaseConnection("superbase",type=SupabaseConnection)  # Use SupabaseConnection to create a connection
    df = conn.query(txt)
    return df

query = st.text_area('Explore the data by running SQL queries', 'SELECT * FROM books;')
if st.button('Run Query'):
    result = sql_query(query)
    st.dataframe(result)
