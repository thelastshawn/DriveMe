import streamlit as st
import datetime
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="DriveMe: CA DMV Prep", page_icon="🚗", layout="centered")

# --- DARK MODE TOGGLE & CUSTOM CSS ---
night_mode = st.sidebar.toggle("🌙 Night Mode")

if night_mode:
    theme_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');
        .stApp { background-color: #121212; color: #E0E0E0; }
        html, body, [class*="css"], p, h1, h2, h3, h4, h5, h6 { font-family: 'Nunito', sans-serif; color: #E0E0E0 !important; }
        div.stButton > button { border-radius: 30px; border: 2px solid #FF8DA1; background-color: #1E1E1E; color: #FF8DA1; font-weight: bold; transition: all 0.3s ease; }
        div.stButton > button:hover { transform: translateY(-3px); box-shadow: 0px 8px 15px rgba(255, 141, 161, 0.4); background-color: #FF8DA1; color: white !important; }
        div[data-testid="stAlert"] { border-radius: 25px; padding: 20px; background-color: #2A2A2A; color: #E0E0E0; border: none; }
    </style>
    """
else:
    theme_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');
        html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
        div.stButton > button { border-radius: 30px; border: 2px solid #FF8DA1; background-color: transparent; color: #FF8DA1; font-weight: bold; transition: all 0.3s ease; }
        div.stButton > button:hover { transform: translateY(-3px); box-shadow: 0px 8px 15px rgba(255, 141, 161, 0.3); background-color: #FF8DA1; color: white; }
        div[data-testid="stAlert"] { border-radius: 25px; padding: 20px; box-shadow: 0px 4px 10px rgba(0,0,0,0.05); }
    </style>
    """
st.markdown(theme_css, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.image("https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=1000&auto=format&fit=crop", use_container_width=True)
st.title("DriveMe 🚗")
st.subheader("Welcome back, Alyssa! Let's get you that permit. 🌴")
st.divider()

# --- INTERACTIVE DAILY TIP ---
st.write("### 💡 Quick Tip of the Day")
tips = [
    "Examiners watch your head, not your eyes! Exaggerate looking over your shoulder for blind spots.",
    "If you're guessing between 15mph and 25mph on the test, residential areas are almost always 25mph.",
    "Don't cram! Doing just 10 flashcards a day builds better memory than a 2-hour session.",
    "Always yield to pedestrians. Always. Even if they are jaywalking.",
    "Take a deep breath! You only need 38 out of 46 questions correct to pass."
]

if 'daily_tip' not in st.session_state:
    st.session_state.daily_tip = random.choice(tips)

st.info(f"**{st.session_state.daily_tip}**")

if st.button("🔄 Give me another tip!"):
    st.session_state.daily_tip = random.choice(tips)
    st.rerun()

st.divider()

# --- CLICKABLE DASHBOARD ---
st.write("### 📍 Study Modules")
st.page_link("pages/0_📖_Study_Guide.py", label="📖 Comprehensive Study Guide")
st.page_link("pages/1_📇_Flashcards.py", label="📇 Quick-Fire Flashcards")
st.page_link("pages/2_📝_Practice_Exam.py", label="📝 Mock Exam Simulator")
st.page_link("pages/3_📺_Video_Practice.py", label="📺 Video Walkthroughs")
st.page_link("pages/4_📱_Social_Tips.py", label="📱 Real-Time Social Feed")
st.page_link("pages/5_🛑_Road_Signs.py", label="🛑 Visual Sign Practice")
st.page_link("pages/6_✅_Test_Day_Checklist.py", label="✅ Test Day Checklist")

st.divider()

# --- COUNTDOWN WIDGET ---
st.write("### 🎯 Exam Day Tracker")
test_date = st.date_input("Select your test date:", value=None)

if test_date:
    today = datetime.date.today()
    days_left = (test_date - today).days
    
    if days_left > 0:
        st.metric(label="Days Remaining", value=days_left)
        st.write("Consistency is key. You are on track to pass! 📈")
    elif days_left == 0:
        st.balloons()
        st.success("Today is the day! Trust your preparation. You're going to do great! 🚙💨")
    else:
        st.write("Exam day has passed! We hope you're out celebrating your new permit! 🎉")
