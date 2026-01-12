import streamlit as st
from backend.database import create_table

create_table()

st.set_page_config(
    page_title="AI Fitness Planner",
    page_icon="💪",
    layout="centered"
)

st.title("💪 AI-Based Personalized Workout & Diet Planner")

st.markdown("""
### Train Smarter. Eat Better. Live Healthier.

This AI-powered web application generates **personalized workout and diet plans**
based on your body metrics, fitness goals, and lifestyle.
""")

st.info("👈 Use the sidebar to navigate through the app")

st.markdown("---")

st.subheader("✨ Key Features")
st.write("""
- Personalized workout recommendations  
- AI-based diet planning  
- BMI & calorie calculation  
- Progress tracking dashboard  
""")

st.success("🚀 Internship-Ready AI Project")




