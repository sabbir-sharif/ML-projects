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
    

    # st.write("Raw Data Shape:", df.shape) -> debugging line
    # st.write(df.head())

    # Step 2: Process the data
    # 2.1: Convert 'time' column to datetime format, handle errors by coercing into NaT (Not a Time)
    df['time'] = pd.to_datetime(
        df['time'],
        format='%Y-%m-%d %H:%M:%S.%f',
        errors='coerce'
    )
    # 2.2: Drop rows where 'time' value is missing
    df = df.dropna(subset=['time'])
    # st.write("After time cleaning:", df.shape)

    # 2.3: Time feature engineering - extract year, month, date, hour, day of week
    df['year'] = df['time'].dt.year
    df['month'] = df['time'].dt.month
    df['date'] = df['time'].dt.date
    df['hour'] = df['time'].dt.hour
    df['day_of_week'] = df['time'].dt.day_name()
    # st.write("After feature engineering:", df.shape)

    # 2.4: Create a 'risk_level' column based on magnitude thresholds
    df['risk_level'] = pd.cut(
        df['magnitude'],
        bins=[0, 4, 5.5, 6.5, np.inf],
        labels=['Low', 'Moderate', 'High', 'Critical']
    )

    # 2.5: Create a 'tectonic_type' column based on depth thresholds
    df['tectonic_type'] = np.where(
        df['depth'] < 70, 'Crustal',
        np.where(
            df['depth'] < 300, 'Intermediate', 'Deep'
        )
    )

    # 2.6: Cluster detection
    df = df.sort_values('time').reset_index(drop=True)
    df['hours_since_prev'] = df['time'].diff().dt.total_seconds() / 3600
    df['hours_since_prev'] = df['hours_since_prev'].fillna(0)
    df['cluster_flag'] = df['hours_since_prev'] < 24


    # st.write("Raw Data Shape:", df.shape)
    # st.write(df.head())
    return df

if uploaded_file is not None:
    st.markdown("File uploaded successfully! Processing data...")
    # Data Frame Creation
    with st.spinner("Loading and processing data..."):
        df = load_and_process_data(uploaded_file)
    

    # Executive Summary
    st.markdown("----")
    st.header("Executive Summary")
    col1, col2, col3, col4, col5 = st.columns(5)

    total_events = len(df)
    critical_events = len(df[df['risk_level'] == 'Critical'])
    recent_24h = len(df[df['time'] >= (df['time'].max() - timedelta(hours=24))])
    avg_mag = df['magnitude'].mean()
    max_mag = df['magnitude'].max()

    with col1:
        st.metric("Total Events", total_events)
    with col2:
        st.metric("Critical Events", critical_events)
    with col3:
        st.metric("Events in Last 24h", recent_24h)
    with col4:
        st.metric("Average Magnitude", f"{avg_mag:.2f}")
    with col5:
        st.metric("Max Magnitude", f"{max_mag:.2f}")

    # Alert System
    st.markdown("----")
    st.header("Alert System")

    now = datetime.now()
    recent_events = df[df['time'] >= (now - timedelta(hours=24))]
    alert_df = recent_events[recent_events['magnitude'] >= 4.5].copy()
    alert_df['time_ago'] = (now - alert_df['time']).dt.total_seconds() / 3600

    if len(alert_df) > 0:
        st.error(f"High-risk events in last 24 hours:{len(alert_df)}")
        for _, row in alert_df.head(6).iterrows():
            st.warnings(
                f"**Magnitude {row['magnitude']:.1f}** earthquake at **{row['place'][:50]} | ({row['time_ago']:.1f} hours ago)"
            )
    else:
        st.success("No high-risk events in the last 24 hours.")