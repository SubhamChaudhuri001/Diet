import streamlit as st
import pandas as pd

from backend.calculations import calculate_bmr
from backend.ml_model import predict_calories



st.title("🥗 Personalized Diet Plan")

st.subheader("🔥 Daily Calorie Target")
st.success("2200 kcal/day")

st.markdown("""
### 🥣 Breakfast
- Oats with fruits  
- Boiled eggs / Paneer  

### 🍛 Lunch
- Brown rice / Roti  
- Dal / Chicken  
- Vegetables  

### 🌙 Dinner
- Salad  
- Grilled protein  
""")

st.expander("💡 Nutrition Tips").write("""
- Drink at least 3L water  
- Avoid processed sugar  
- Eat every 3–4 hours  
""")


#Connect Logic to Diet Page
st.title("🥗 Personalized Diet Plan")

if "user" not in st.session_state:
    st.warning("⚠️ Please enter your details first.")
else:
    user = st.session_state.user

    bmr = calculate_bmr(
        user["gender"],
        user["weight"],
        user["height"],
        user["age"]
    )

    daily_cal = bmr * activity_factor[user["activity"]]
    diet = diet_plan(user["goal"], daily_cal, user["diet"])

    st.success(f"🔥 Daily Calories: {diet['Calories']} kcal")

    st.write("🍗 Protein Sources:", diet["Protein"])
    for meal in diet["Meals"]:
        st.write("•", meal)


#DAILY CALORIE BREAKDOWN (CHART)

st.title("🥗 Personalized Diet Plan")

if "user" not in st.session_state:
    st.warning("⚠️ Please enter your details first.")
else:
    user = st.session_state.user

    bmr = calculate_bmr(
        user["gender"],
        user["weight"],
        user["height"],
        user["age"]
    )

    daily_cal = int(bmr * activity_factor[user["activity"]])
    diet = diet_plan(user["goal"], daily_cal, user["diet"])

    st.success(f"🔥 Daily Calories Target: {diet['Calories']} kcal")

    # Macronutrient distribution
    data = {
        "Macronutrient": ["Protein", "Carbs", "Fats"],
        "Calories": [
            diet["Calories"] * 0.30,
            diet["Calories"] * 0.45,
            diet["Calories"] * 0.25
        ]
    }

    df = pd.DataFrame(data)

    st.subheader("📊 Calorie Distribution")
    st.bar_chart(df.set_index("Macronutrient"))




#Integrate ML Model into Diet Page

activity_factor = {
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725
}

user = st.session_state.user

ml_calories = predict_calories(
    user["age"],
    user["weight"],
    user["height"],
    activity_factor[user["activity"]]
)

st.subheader("🤖 AI (ML) Calorie Prediction")
st.success(f"Predicted Daily Calories: {ml_calories} kcal")


#Copare Formula vs ML
st.subheader("📊 Calorie Estimation Comparison")

st.metric("Formula-Based Calories", int(daily_cal))
st.metric("ML-Predicted Calories", ml_calories)


