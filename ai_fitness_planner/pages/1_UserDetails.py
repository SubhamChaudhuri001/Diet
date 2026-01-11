"""import streamlit as st

st.title("📝 Enter Your Details")

with st.form("user_form"):
    age = st.number_input("Age", 15, 70)
    gender = st.radio("Gender", ["Male", "Female"])
    height = st.number_input("Height (cm)")
    weight = st.number_input("Weight (kg)")
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

    submit = st.form_submit_button("Save Details")

if submit:
    st.success("✅ Details saved successfully!")

"""


#Global data storage

import streamlit as st

st.title("📝 Enter Your Details")

with st.form("user_form"):                            #########################
    age = st.number_input("Age", 15, 70)
    gender = st.radio("Gender", ["Male", "Female"])
    height = st.number_input("Height (cm)")
    weight = st.number_input("Weight (kg)")
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
    st.success("✅ Data saved! Now check Workout & Diet pages.")



#BMI calculation
def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)



#BMR Formula
def calculate_bmr(gender, weight, height, age):
    if gender == "Male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161



#Activity Multiplier
activity_factor = {
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725
}


#Workout Recommendation logic
def workout_plan(goal, bmi):
    if goal == "Weight Loss":
        return [
            "30–40 min Cardio",
            "Jump rope",
            "Bodyweight squats",
            "Plank & core exercises"
        ]
    elif goal == "Muscle Gain":
        return [
            "Strength training",
            "Chest & Back workouts",
            "Leg day & shoulder training",
            "Progressive overload"
        ]
    else:
        return [
            "Mixed cardio + strength",
            "Yoga & stretching",
            "Light resistance training"
        ]



#Diet Recommendation Logic
def diet_plan(goal, calories, diet_type):
    if goal == "Weight Loss":
        calories -= 400
    elif goal == "Muscle Gain":
        calories += 300

    if diet_type == "Vegetarian":
        protein = "Paneer, Dal, Tofu"
    else:
        protein = "Eggs, Chicken, Fish"

    return {
        "Calories": int(calories),
        "Protein": protein,
        "Meals": [
            "Breakfast: Oats & fruits",
            "Lunch: Rice/Roti + protein",
            "Dinner: Salad + protein"
        ]
    }



#Save Progress Data Automatically
from database import connect_db
from datetime import date

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

    today = date.today().isoformat()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO progress (age, gender, height, weight, goal, calories, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (age, gender, height, weight, goal, 0, today))

    conn.commit()
    conn.close()

    st.success("✅ Progress saved successfully!")



