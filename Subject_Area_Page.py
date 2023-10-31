import streamlit as st
import numpy as np
import pandas as pd
import snowflake.connector


st.set_page_config(
    page_title="Subject Area",
    page_icon="👋",
)

st.write("# This will be a page where a user can view and modify subject area description 👋")

def get_subject_area_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from SUBJECT_AREA")
        return my_cur.fetchall()
        
if streamlit.button('Get Subject Area List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_subject_area_list()
    my.cnx.close()
    streamlit.dataframe(my_data_rows)

st.button('Add New')
    


