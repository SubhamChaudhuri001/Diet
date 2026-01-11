import streamlit as st

st.title("📊 Progress Dashboard")

st.metric("Current Weight", "75 kg", "-1.5 kg")
st.metric("BMI", "24.2", "Improved")

st.subheader("📈 Weekly Progress")
st.line_chart([75, 74.6, 74.2, 73.5])

st.success("🎯 You are on the right track!")


#WEEKLY CALORIE TREND (SIMULATED DATA)
import streamlit as st
import pandas as pd

st.title("📈 Progress Dashboard")

weekly_data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Calories Burned": [2200, 2400, 2100, 2500, 2300, 2600, 2000]
}

df = pd.DataFrame(weekly_data)

st.subheader("🔥 Weekly Calories Burned")
st.line_chart(df.set_index("Day"))

st.success("🎯 Consistency is the key to success!")



#Display Progress History (Dashboard)
import streamlit as st
import pandas as pd
from database import get_progress

st.title("📊 Progress Dashboard")

data = get_progress()

if not data:
    st.info("No progress data available yet.")
else:
    df = pd.DataFrame(data, columns=["Date", "Weight (kg)"])

    st.subheader("📉 Weight Progress Over Time")
    st.line_chart(df.set_index("Date"))

    latest_weight = df.iloc[-1]["Weight (kg)"]
    st.metric("Current Weight", f"{latest_weight} kg")

