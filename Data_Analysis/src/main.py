"""
    Earthquake Decision Support Dashboard
"""
import streamlit as st
import pandas as pd
#import plotly.express as px
import numpy as np
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Earthquake Decision Support Dashboard", 
    layout="wide",
    initial_sidebar_state="expanded"
    )

# Page Title
st.title("Earthquake Decision Support Dashboard")
st.markdown(
    "**Real-time monitoring, clustering and decision support for geologists**"
)