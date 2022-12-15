import streamlit as st
import pandas as pd
import numpy as np
import json
import requests

st.title('Marketing Dashboard')

st.sidebar.title('User Inputs')


df = pd.read_json('data.json')

option = st.sidebar.selectbox('Stock Types',('Line Chart','Bar Chart','Area Chart','Scatter Chart','PlotLy'))

st.header(option)

import base64
def add_bg_from_local(blue):
    with open(blue, "rb") as blue:
        encoded_string = base64.b64encode(blue.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: 1024x768
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('blue.jpg')   
    
