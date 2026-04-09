import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="DriveMe: CA DMV Prep", page_icon="🚗", layout="centered")

# --- PREMIUM FONT INJECTION ---
# This hides a tiny bit of CSS in the app to make the fonts look sleek and native to iOS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.image("https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=1000&auto=format&fit=crop", use_container_width=True)

st.title("DriveMe 🚗")
st.subheader("Your Fast-Track to the California Driver's Permit.")
st.write("Curated specifically for San Diego drivers. Everything you need to master the 2026 CA DMV exam, all in one place. 🌴")

st.divider()

# --- CLICKABLE DASHBOARD ---
st.write("### 📍 Study Modules")
st.write("Select a module below to begin your session:")

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

