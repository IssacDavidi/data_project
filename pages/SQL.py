import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import os

st.write("DB username:", st.secrets["db_username"])
