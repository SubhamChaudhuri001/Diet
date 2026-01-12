import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ✅ IMPORT LOGIC FUNCTIONS
from backend.calculations import calculate_bmi
from backend.workout_logic import workout_plan

# -----------------------------------------------

st.title("🏋️ Personalized Workout Plan")

# ✅ PAGE PROTECTION
if "user" not in st.session_state:
    st.warning("⚠️ Please enter your details on the User Details page first.")
    st.stop()

# ✅ GET USER DATA
user = st.session_state.user

# ✅ CALCULATIONS
bmi = calculate_bmi(user["weight"], user["height"])
plan = workout_plan(user["goal"], bmi)

# -----------------------------------------------
# ✅ BMI STATUS
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

category = bmi_category(bmi)

# -----------------------------------------------
# ✅ DISPLAY BMI INFO
st.subheader("📏 BMI Analysis")
st.metric("BMI Value", f"{bmi:.2f}")
st.info(f"🧠 BMI Category: **{category}**")

bmi_percent = min(bmi / 40, 1.0)
st.progress(bmi_percent)
st.caption("BMI scale (0–40)")

st.divider()

# -----------------------------------------------
# ✅ WORKOUT PLAN DISPLAY
st.subheader("🔹 Recommended Workout Plan")

for exercise in plan:
    st.write("✅", exercise)

st.expander("📅 Weekly Schedule").write("""
Monday – Cardio  
Tuesday – Upper Body  
Wednesday – Rest  
Thursday – Lower Body  
Friday – Core  
Saturday – Optional Cardio  
Sunday – Rest
""")

st.progress(0.7)
st.caption("Workout Completion Progress")

