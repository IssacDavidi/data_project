import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import os




col1, col2 = st.columns(2)

with col1:
  st.subheader('Hello there, welcome to my data analysis project! I hope you like it')
with col2:
  st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/cat1.png?raw=true', 'A beautiful cat', width=600)
  

