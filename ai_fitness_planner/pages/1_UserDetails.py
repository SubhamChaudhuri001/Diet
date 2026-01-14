import streamlit as st
from backend.database import connect_db
from datetime import date

st.title("📝 Enter Your Details")

# -------------------------------------------------
# DEFAULT USER
DEFAULT_USER = {
    "age": 25,
    "gender": "Male",
    "height": 170,
    "weight": 70,
    "activity": "Moderately Active",
    "goal": "Stay Fit",
    "diet": "Vegetarian"
}

# -------------------------------------------------
# 🔄 RESET BUTTON (MUST BE BEFORE FORM)
if st.button("🔄 Reset Details"):
    for key in ["age", "gender", "height", "weight", "activity", "goal", "diet"]:
        if key in st.session_state:
            del st.session_state[key]

    st.session_state.user = DEFAULT_USER.copy()
    st.success("Details reset to default values.")
    st.rerun()

# -------------------------------------------------
# INITIALIZE USER ONLY ONCE
if "user" not in st.session_state:
    st.session_state.user = DEFAULT_USER.copy()

user = st.session_state.user

# -------------------------------------------------
# FORM
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
# SAVE ON SUBMIT
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

    st.success("✅ Details saved successfully!")
