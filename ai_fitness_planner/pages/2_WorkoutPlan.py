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


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

# ---------------- DOWNLOAD WORKOUT PLAN AS PDF ----------------
st.subheader("📥 Download Your Workout Plan")

def generate_workout_pdf(user, bmi, category, plan):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "YOUTHFIT AI – Personalized Workout Plan")

    # User summary
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 90, f"Goal: {user['goal']}")
    c.drawString(50, height - 110, f"BMI: {bmi:.2f} ({category})")

    # Workout plan
    y = height - 150
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Recommended Exercises:")
    y -= 25

    c.setFont("Helvetica", 11)
    for exercise in plan:
        c.drawString(60, y, f"- {exercise}")
        y -= 18

    # Weekly schedule
    y -= 20
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Weekly Schedule:")
    y -= 20

    c.setFont("Helvetica", 11)
    schedule = [
        "Monday – Cardio",
        "Tuesday – Upper Body",
        "Wednesday – Rest",
        "Thursday – Lower Body",
        "Friday – Core",
        "Saturday – Optional Cardio",
        "Sunday – Rest"
    ]

    for day in schedule:
        c.drawString(60, y, f"- {day}")
        y -= 18

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer


workout_pdf = generate_workout_pdf(user, bmi, category, plan)

st.download_button(
    label="📄 Download Workout Plan (PDF)",
    data=workout_pdf,
    file_name="YOUTHFIT_AI_Workout_Plan.pdf",
    mime="application/pdf"
)


