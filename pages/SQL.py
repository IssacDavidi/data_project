import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd
import sqlalchemy

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = conn.query("*", table="books", ttl="10m").execute()

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['pet']}:")
