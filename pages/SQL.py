import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd


# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# SQL query
rows = conn.query("*", table="books", ttl="10m").execute()

st.write(rows.data)
