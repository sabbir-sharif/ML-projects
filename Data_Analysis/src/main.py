"""
    Earthquake Decision Support Dashboard
"""
import streamlit as st
import pandas as pd
import plotly.express as px
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

# Load Data
uploaded_file = st.file_uploader("Upload Earthquake Data (CSV)", type=["csv"])

# Data frame creation and processing function
def load_and_process_data(uploaded_file):
    # Step 1: Load the data
    df = pd.read_csv(uploaded_file)

    # Step 2: Process the data
    # 2.1: Convert 'time' column to datetime format, handle errors by coercing into NaT (Not a Time)
    df['time'] = pd.to_datetime(
        df['time'], format='%d-%m-%Y %H:%M:%S', errors='coerce'
        )
    # 2.2: Drop rows where 'time' value is missing
    df = df.dropna(subset=['time'])

    return df

if uploaded_file is not None:
    st.markdown("File uploaded successfully! Processing data...")
    # Data Frame Creation
    df = load_and_process_data(uploaded_file)
    df.head()
    