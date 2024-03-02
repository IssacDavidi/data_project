import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
import os




col1, col2 = st.columns(2)

with col1:
  st.subheader('Lorem ipsum dolor sit amet')
  st.write('consectetur adipiscing elit. Praesent tristique quis sem ut tempus. Curabitur in dui in nibh posuere fringilla.')
  st.write('Nulla facilisi. Ut quis consectetur leo. Cras mollis sapien nec dolor ultricies elementum. Cras tempor ipsum vel ex ullamcorper, eget feugiat neque lobortis. Fusce nec lectus risus.')
with col2:
  st.image('https://github.com/IssacDavidi/data_project/blob/main/photos/cat1.png?raw=true', 'A beautiful cat', width=600)
  

