import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd


# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

custom_query = "SELECT * FROM books"

# SQL query
data = conn.query(custom_query,table='books', ttl="10m").execute().data

df = pd.DataFrame(data)

st.write(df)
