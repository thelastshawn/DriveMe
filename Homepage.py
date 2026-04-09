import streamlit as st
import datetime
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="DriveMe: CA DMV Prep", page_icon="🚗", layout="centered")

# --- CUSTOM CSS BUBBLE INJECTION ---
# This forces the bubbly font and rounds out the sharp corners of Streamlit's default UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;900&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Nunito', sans-serif; 
    }
    
    /* Make buttons bubbly with hover effects */
    div.stButton > button {
        border-radius: 30px;
        border: 2px solid #FF8DA1;
        background-color: transparent;
        color: #FF8DA1;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0px 8px 15px rgba(255, 141, 161, 0.3);
        background-color: #FF8DA1;
        color: white;
    }
    
    /* Round out the alert boxes to look like message bubbles */
    div[data-testid="stAlert"] {
        border-radius: 25px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
# Swap this link out later with a custom graphic you make in Canva!
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
st.write("Tap a bubble below to begin your session:")

st.page_link("pages/0_📖_Study_Guide.py", label="📖 Comprehensive Study Guide")
st.page_link("pages/1_📇_Flashcards.py", label="📇 Quick-Fire Flashcards")
st.page_link("pages/2_📝_Practice_Exam.py", label="📝 Mock Exam Simulator")
st.page_link("pages/3_📺_Video_Practice.py", label="📺 Video Walkthroughs")
st.page_link("pages/4_📱_Social_Tips.py", label="📱 Real-Time Social Feed")

st.divider()

# --- COUNTDOWN WIDGET ---
st.write("### 🎯 Exam Day Tracker")
st.write("Lock in your DMV appointment date to track your timeline.")

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
