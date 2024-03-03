# Seassion State
import streamlit as st
import pandas as pd
import streamlit_pandas as sp
import pandasql as ps


st.title('Explore the data on your own!')
@st.cache_data
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/IssacDavidi/data_project/main/steimatzky_cleaned.csv')
    return df

df = load_data()


custom_widget_look = {
						'category': 'multiselect',
						'sub_category': 'multiselect'


}

ignore_columns = ['description']

all_widgets = sp.create_widgets(df, custom_widget_look, ignore_columns=ignore_columns)
res = sp.filter_df(df, all_widgets)
st.write(res)



# Create an adventure button and style it

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(42, 139, 168);
}
</style>""", unsafe_allow_html=True)

