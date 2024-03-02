import streamlit as st
from st_supabase_connection import SupabaseConnection
from st_supabase_client import StSupabaseClient
import pandas as pd

# Initialize Supabase client
st_supabase_client = StSupabaseClient()

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# SQL query
rows = conn.query("*", table="books", ttl="10m").execute()

st.write(rows)
