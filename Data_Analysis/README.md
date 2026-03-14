# 🌍 Earthquake Decision Support Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-purple)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black)
![License](https://img.shields.io/badge/License-MIT-green)

An **interactive earthquake monitoring and decision-support dashboard** built using **Python, Streamlit, Pandas, and Plotly**.

This project transforms raw earthquake catalog data into **interactive insights, geospatial visualizations, and automated alerts**, helping geologists and disaster management teams analyze seismic activity efficiently.

---

# 🚀 Live Demo

Experience the dashboard in action! [Live Demo Link](https://earthquake-decision-support.streamlit.app/)


---

# 📊 Project Overview

The **Earthquake Decision Support Dashboard** provides tools for:

- Monitoring earthquake activity
- Identifying high-risk seismic events
- Detecting potential aftershock clusters
- Visualizing earthquake locations globally
- Supporting quick decision-making for emergency response

The dashboard integrates **data preprocessing, feature engineering, interactive visualizations, and decision support logic** into a single analytical platform.

---

# ✨ Key Features

## 📌 Executive Summary
Displays important seismic metrics:

- Total Earthquake Events
- Critical Events
- Events in the Last 24 Hours
- Average Magnitude
- Maximum Magnitude

---

## ⚠️ Real-Time Alert System
Automatically highlights **high-magnitude earthquakes** detected in the last 24 hours.

Example alert:

- Magnitude ≥ 4.5 events flagged
- Displays location and time since occurrence

---

## 📈 Trend Analysis
Interactive visualizations including:

- Risk level distribution
- Earthquakes by hour of day
- Daily earthquake activity
- Magnitude trends over time

These help identify **patterns in seismic activity**.

---

## 🗺️ Interactive Earthquake Risk Map

Global earthquake visualization showing:

- Event location
- Magnitude-based marker size
- Color intensity based on magnitude
- Hover details for event information

Built using **Plotly Mapbox**.

---

## 🔍 Advanced Filtering

Users can filter earthquake data using:

- Time window  
  - All Time  
  - Last 7 Days  
  - Last 30 Days  
  - Last 90 Days  
  - Custom Range  

- Magnitude range
- Depth range
- Risk level
- Tectonic type

---

## 🔗 Aftershock Cluster Detection

Detects earthquake clusters occurring **within 24 hours of each other**.

Cluster summary includes:

- Number of events
- Maximum magnitude
- Cluster center location
- Cluster start time

This helps identify **possible aftershock sequences**.

---

## 🧠 Decision Support System

Based on seismic activity, the dashboard recommends actions such as:

- Increase monitoring frequency
- Issue public safety alerts
- Deploy field assessment teams
- Prepare tsunami early warning

---

## 📤 Data Export

Users can download filtered earthquake data directly from the dashboard as:
- CSV

---

# 🛠 Tech Stack

| Technology | Usage |
|------------|-------|
| **Python** | Core programming language |
| **Streamlit** | Interactive dashboard |
| **Pandas** | Data processing |
| **NumPy** | Numerical computations |
| **Plotly** | Interactive charts |
| **Plotly Mapbox** | Geospatial visualization |

---

# 📂 Project Structure
```Data_Analysis/
├── data/
│   └── eq_catalog.csv
├── src/
│   ├── main.py
├── README.md
├── requirements.txt
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sabbir-sharif/ML-projects.git
cd Data_Analysis/src

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

run:
streamlit run src/main.py

open in browser:
http://localhost:8501
```