import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="DriveMe: CA DMV Prep", page_icon="🚗", layout="centered")

# --- HEADER SECTION ---
# Adding a header image makes it feel much more like a real app!
st.image("https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?q=80&w=1000&auto=format&fit=crop", use_container_width=True)

st.title("🚗 Welcome to DriveMe!")
st.subheader("Your personal California DMV Permit study buddy.")
st.write("I built this app specifically to help you ace your permit test and get on the road in San Diego! 🌴")

st.divider()

# --- CLICKABLE DASHBOARD ---
st.write("### 📍 Your Study Dashboard")
st.write("Tap a section below to jump right in:")

# These create full-width, clickable iOS-style menu buttons!
st.page_link("pages/0_📖_Study_Guide.py", label="📖 Study Guide (Core rules & new 2026 laws)")
st.page_link("pages/1_📇_Flashcards.py", label="📇 Flashcards (Quick-fire memory test)")
st.page_link("pages/2_📝_Practice_Exam.py", label="📝 Practice Exam (Randomized 10-question test)")
st.page_link("pages/3_📺_Video_Practice.py", label="📺 Video Practice (Watch real DMV questions)")

st.divider()

# --- COUNTDOWN WIDGET ---
st.write("### 🎯 Test Day Tracker")
st.write("Set your DMV appointment date below to start the countdown!")

test_date = st.date_input("When is your permit test?", value=None)

if test_date:
    today = datetime.date.today()
    days_left = (test_date - today).days
    
    if days_left > 0:
        st.metric(label="Days until test day!", value=days_left)
        st.write("You've got this! Just take it one study session at a time.")
    elif days_left == 0:
        st.balloons()
        st.success("Today is the day! Take a deep breath. You are going to do great! 🚙💨")
    else:
        st.write("Test day has passed! Hopefully, you're officially holding that permit! 🎉")
