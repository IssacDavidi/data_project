import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

# Retrieve Supabase URL and API key from Streamlit secrets
supabase_url = st.secrets["connections.supabase.SUPABASE_URL"]
supabase_key = st.secrets["connections.supabase.SUPABASE_KEY"]

# Create a SQLAlchemy engine
engine = create_engine(f"postgresql://{supabase_key}@{supabase_url}/postgres")

# Custom SQL query
custom_query = "SELECT * FROM books"

# Execute the query and get the result as a Pandas DataFrame
df = pd.read_sql_query(custom_query, con=engine)

# Display the DataFrame
st.write(df)
