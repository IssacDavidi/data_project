import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import os
import psycopg2

# Retrieve Supabase URL and API key from Streamlit secrets
user = st.secrets["db_username"]
pwd = st.secrets["db_password"]

# Create a SQLAlchemy engine
engine = create_engine('postgresql://user:pwd@pga.h.filess.io:5432/books_pocketbarn')

