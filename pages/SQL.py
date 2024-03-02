import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd


# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# SQL query
data = conn.query("*", table="books", ttl="10m").execute().data

df = pd.DataFrame(data)

st.write(df)
