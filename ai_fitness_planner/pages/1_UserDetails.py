import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from backend.database import connect_db
from datetime import date

st.title("📝 Enter Your Details")

# ✅ INITIALIZE SESSION STATE (ONLY ONCE)
if "user" not in st.session_state:
    st.session_state.user = {
        "age": 25,
        "gender": "Male",
        "height": 170,
        "weight": 70,
        "activity": "Moderately Active",
        "goal": "Stay Fit",
        "diet": "Vegetarian"
    }

user = st.session_state.user

with st.form("user_form"):
    age = st.number_input("Age", min_value=15, max_value=70)
    gender = st.radio("Gender", ["Male", "Female"])
    height = st.number_input("Height (cm)", min_value=50, max_value=250)
    weight = st.number_input("Weight (kg)", min_value=20, max_value=300)

    activity = st.selectbox(
        "Activity Level",
        ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
    )

    goal = st.selectbox(
        "Fitness Goal",
        ["Weight Loss", "Muscle Gain", "Stay Fit"]
    )

    diet = st.selectbox(
        "Diet Preference",
        ["Vegetarian", "Non-Vegetarian"]
    )

    submit = st.form_submit_button("Generate My Plan")

# -------------------------------------------------

# ✅ UPDATE SESSION STATE ONLY ON SUBMIT
if submit:
    st.session_state.user = {
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "activity": activity,
        "goal": goal,
        "diet": diet
    }

    # ✅ Save to database
    today = date.today().isoformat()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO progress (age, gender, height, weight, goal, calories, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (age, gender, height, weight, goal, 0, today))

    conn.commit()
    conn.close()

    st.success("✅ Details saved successfully! Go to Workout or Diet page.")

