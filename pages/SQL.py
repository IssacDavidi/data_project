import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd
import sqlalchemy

# Retrieve Supabase URL from Streamlit secrets
supabase_url = st.secrets["SUPABASE_URL"]

# Retrieve Supabase API key from Streamlit secrets
supabase_key = st.secrets["SUPABASE_KEY"]

@st.cache_data
def sql_query(txt):
    # Use SupabaseConnection and provide the URL and API key
    conn = SupabaseConnection(url=supabase_url, key=supabase_key)
    df = conn.query(txt)
    return df

query = st.text_area('Explore the data by running SQL queries', 'SELECT * FROM books;')
if st.button('Run Query'):
    result = sql_query(query)
    st.dataframe(result)
