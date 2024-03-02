import streamlit as st
from st_supabase_connection import SupabaseConnection
import pandas as pd

# Initialize Supabase client
st_supabase_client = StSupabaseClient()

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Your SQL query
query = "SELECT * FROM books"

# Execute the query and get the result
result = st_supabase_client.query("*", table="books", ttl=0).execute()

# Check if data is present in the result
if result.data:
    # Convert the data to a Pandas DataFrame
    df = result.data

    # Display the DataFrame in Streamlit
    st.dataframe(df)
else:
    st.warning("No data found for the given query.")
