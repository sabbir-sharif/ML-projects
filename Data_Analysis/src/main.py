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

    # 2.3: Time feature engineering - extract year, month, date, hour, day of week
    df['year'] = df['time'].dt.year
    df['month'] = df['time'].dt.month
    df['date'] = df['time'].dt.date
    df['hour'] = df['time'].dt.hour
    df['day_of_week'] = df['time'].dt.day_name()

    # 2.4: Create a 'risk_level' column based on magnitude thresholds
    df['risk_level'] = pd.cut(
        df['magnitude'],
        bins=[0, 4, 5.5, 6.5, np.inf],
        labels=['Low', 'Moderate', 'High', 'Critical']
    )

    # 2.5: Create a 'tectonic_type' column based on depth thresholds
    df['tectonic_type'] = df.where(
        df['depth'] < 70, 'Crustal',
        df.where(
            df['depth'] < 300, 'Intermediate', 'Deep'
        )
    )

    # 2.6: Cluster detection
    df = df.sort_values('time').reset_index(drop=True)
    df['hourse_since_prev'] = df['time'].diff().dt.total_seconds() / 3600
    df['hourse_since_next'] = df['hour_since_prev'].fillna(0)
    df['cluster_flag'] = df['hourse_since_prev'] < 24

    return df

if uploaded_file is not None:
    st.markdown("File uploaded successfully! Processing data...")
    # Data Frame Creation
    df = load_and_process_data(uploaded_file)
    df.head()
    