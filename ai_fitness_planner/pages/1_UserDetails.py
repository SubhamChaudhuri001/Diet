import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from backend.database import connect_db
from datetime import date

st.title("📝 Enter Your Details")

# -------------------------------------------------
# 1️⃣ INITIALIZE SESSION STATE ONLY ONCE
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

# -------------------------------------------------
# 2️⃣ SESSION-BOUND FORM
with st.form("user_form"):

    age = st.number_input(
        "Age",
        min_value=15,
        max_value=70,
        value=user["age"],
        key="age"
    )

    gender = st.radio(
        "Gender",
        ["Male", "Female"],
        index=0 if user["gender"] == "Male" else 1,
        key="gender"
    )

    height = st.number_input(
        "Height (cm)",
        min_value=50,
        max_value=250,
        value=user["height"],
        key="height"
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=20,
        max_value=300,
        value=user["weight"],
        key="weight"
    )

    activity_options = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
    activity = st.selectbox(
        "Activity Level",
        activity_options,
        index=activity_options.index(user["activity"]),
        key="activity"
    )

    goal_options = ["Weight Loss", "Muscle Gain", "Stay Fit"]
    goal = st.selectbox(
        "Fitness Goal",
        goal_options,
        index=goal_options.index(user["goal"]),
        key="goal"
    )

    diet = st.selectbox(
        "Diet Preference",
        ["Vegetarian", "Non-Vegetarian"],
        index=0 if user["diet"] == "Vegetarian" else 1,
        key="diet"
    )

    submit = st.form_submit_button("Generate My Plan")

# -------------------------------------------------
# 3️⃣ UPDATE SESSION STATE ONLY ON SUBMIT
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

    # Optional DB save
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

