import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="Simple Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

with st.sidebar:
    st.title('Simple Dashboard')
    
    color_theme_list = ['a', 'b', 'c']
    selected_color_theme = st.selectbox('Select a value', color_theme_list)