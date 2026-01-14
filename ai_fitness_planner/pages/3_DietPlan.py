import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd

from backend.calculations import calculate_bmr
from backend.ml_model import predict_calories
from backend.diet_logic import diet_plan

# ---------------------------------------
st.title("🥗 Personalized Diet Plan")

# ---------------------------------------
activity_factor = {
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725
}

# ---------------------------------------
# SAFETY CHECK
if "user" not in st.session_state:
    st.warning("⚠️ Please enter your details on the User Details page first.")
    st.stop()

user = st.session_state.user

# ---------------------------------------
# BMR & CALORIE CALCULATION
bmr = calculate_bmr(
    user["gender"],
    user["weight"],
    user["height"],
    user["age"]
)

if bmr is None or bmr <= 0:
    st.error("❌ Invalid data detected. Please re-enter your details.")
    st.stop()

daily_cal = int(bmr * activity_factor[user["activity"]])
diet = diet_plan(user["goal"], daily_cal, user["diet"])

# ---------------------------------------
# FORMULA-BASED OUTPUT
st.subheader("🔥 Daily Calorie Target (Formula Based)")
st.success(f"{diet['Calories']} kcal/day")

st.write("🍗 **Protein Sources:**", diet["Protein"])

for meal in diet["Meals"]:
    st.write("•", meal)

# ---------------------------------------
# MACRONUTRIENT DISTRIBUTION
st.subheader("📊 Macronutrient Distribution")

macro_df = pd.DataFrame({
    "Macronutrient": ["Protein", "Carbs", "Fats"],
    "Calories": [
        diet["Calories"] * 0.30,
        diet["Calories"] * 0.45,
        diet["Calories"] * 0.25
    ]
})

st.bar_chart(macro_df.set_index("Macronutrient"))

# ---------------------------------------
# ML CALORIE PREDICTION
ml_calories = predict_calories(
    user["age"],
    user["weight"],
    user["height"],
    activity_factor[user["activity"]]
)

st.subheader("🤖 AI (ML) Calorie Prediction")
st.success(f"{ml_calories} kcal/day")

# ---------------------------------------
# COMPARISON
st.subheader("📊 Formula vs ML Comparison")

st.metric("Formula-Based Calories", daily_cal)
st.metric("ML-Predicted Calories", ml_calories)

# ---------------------------------------
# TIPS
st.expander("💡 Nutrition Tips").write("""
- Drink at least 3L water daily  
- Avoid processed sugar  
- Eat every 3–4 hours  
- Maintain sufficient protein intake  
""")

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

# ---------------- DOWNLOAD DIET PLAN AS PDF ----------------
st.subheader("📥 Download Your Diet Plan")

def generate_diet_pdf(diet, user):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "YOUTHFIT AI – Personalized Diet Plan")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 90, f"Goal: {user['goal']}")
    c.drawString(50, height - 110, f"Diet Preference: {user['diet']}")
    c.drawString(50, height - 130, f"Daily Calories: {diet['Calories']} kcal")

    y = height - 170
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Meals:")
    y -= 20

    c.setFont("Helvetica", 11)
    for meal in diet["Meals"]:
        c.drawString(60, y, f"- {meal}")
        y -= 18

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer


pdf_data = generate_diet_pdf(diet, user)

st.download_button(
    label="📄 Download Diet Plan (PDF)",
    data=pdf_data,
    file_name="YOUTHFIT_AI_Diet_Plan.pdf",
    mime="application/pdf"
)

