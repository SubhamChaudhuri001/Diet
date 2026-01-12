import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
from backend.database import get_progress

st.title("📊 Progress Dashboard")

# -----------------------------------
# FETCH DATA FROM DATABASE
data = get_progress()

if not data:
    st.info("No progress data available yet. Please submit your details first.")
    st.stop()

df = pd.DataFrame(data, columns=["Date", "Weight (kg)"])
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------------
# LATEST METRICS
latest_weight = df.iloc[-1]["Weight (kg)"]
start_weight = df.iloc[0]["Weight (kg)"]
weight_change = round(latest_weight - start_weight, 2)

st.metric(
    label="⚖️ Current Weight",
    value=f"{latest_weight} kg",
    delta=f"{weight_change} kg"
)

st.divider()

# -----------------------------------
# WEIGHT PROGRESS CHART
st.subheader("📉 Weight Progress Over Time")
st.line_chart(df.set_index("Date"))

st.divider()

# -----------------------------------
# OPTIONAL: SIMULATED WEEKLY CALORIE BURN
st.subheader("🔥 Weekly Calories Burned (Sample Data)")

weekly_data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Calories Burned": [2200, 2400, 2100, 2500, 2300, 2600, 2000]
}

cal_df = pd.DataFrame(weekly_data)
st.line_chart(cal_df.set_index("Day"))

st.success("🎯 Consistency is the key to success!")
