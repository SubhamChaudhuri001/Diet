import streamlit as st
from PIL import Image
from backend.database import create_table

create_table()

st.set_page_config(
    page_title="AI Fitness Planner",
    page_icon="💪",
    layout="centered"
)

st.set_page_config(
    page_title="YOUTHFIT AI",
    page_icon="💪",
    layout="centered"
)

# ✅ LOAD IMAGE PROPERLY
logo = Image.open("assets/logo.png")

# ✅ USE st.logo WITHOUT size PARAM
st.logo(logo)



st.sidebar.title("💪 YOUTHFIT AI")
st.sidebar.caption("AI-Based Workout & Diet Planner")

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

'''
if st.sidebar.button("🚀 Get Started"):
    st.switch_page("pages/1_User_Details.py")

st.sidebar.markdown("---")

if "user" in st.session_state:
    user = st.session_state.user
    st.sidebar.markdown("### 👤 User Summary")
    st.sidebar.write(f"🎯 Goal: {user['goal']}")
    st.sidebar.write(f"🥗 Diet: {user['diet']}")
else:
    st.sidebar.info("Please enter your details")

'''




