import streamlit as st

st.title("🏋️ Personalized Workout Plan")

st.subheader("🔹 Recommended Training")

st.markdown("""
**Beginner Level**
- 20 min Cardio  
- Bodyweight Squats  
- Push-ups  
- Plank  

**Weekly Schedule**
- 5 days workout  
- 2 days rest
""")

st.expander("📅 View Weekly Plan").write("""
Monday – Cardio  
Tuesday – Upper Body  
Wednesday – Rest  
Thursday – Lower Body  
Friday – Core  
""")

st.progress(70)
st.caption("Workout Completion Progress")





#Connect Logic to Workout Page
import streamlit as st

st.title("🏋️ Personalized Workout Plan")

if "user" not in st.session_state:
    st.warning("⚠️ Please enter your details first.")
else:
    user = st.session_state.user
    bmi = calculate_bmi(user["weight"], user["height"])

    plan = workout_plan(user["goal"], bmi)

    st.metric("BMI", f"{bmi:.2f}")

    for exercise in plan:
        st.write("✅", exercise)



#BMI STATUS
import streamlit as st

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

st.title("🏋️ Personalized Workout Plan")

if "user" not in st.session_state:
    st.warning("⚠️ Please enter your details first.")
else:
    user = st.session_state.user
    bmi = calculate_bmi(user["weight"], user["height"])
    category = bmi_category(bmi)

    st.metric("📏 BMI Value", f"{bmi:.2f}")
    st.info(f"🧠 BMI Category: **{category}**")

    # BMI Progress Visualization
    bmi_percent = min(bmi / 40, 1.0)
    st.progress(bmi_percent)

    st.caption("BMI scale (0–40)")
