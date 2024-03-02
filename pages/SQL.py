import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd


# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Create a df
df = conn.query("select * from books")

st.dataframe(df)
