import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="DriveMe: CA DMV Prep", page_icon="🚗", layout="centered")

# --- HEADER SECTION ---
st.title("🚗 Welcome to DriveMe!")
st.subheader("Your personal California DMV Permit study buddy.")
st.write("I built this app specifically to help you ace your permit test and get on the road in San Diego! 🌴")

st.divider()

# --- DASHBOARD CARDS ---
st.write("### 📍 Your Study Dashboard")
st.write("Use the sidebar menu to navigate to these sections when you're ready:")

# Create a 2x2 grid using columns
col1, col2 = st.columns(2)

with col1:
    st.info("#### 📖 Study Guide\nStart here! Review the core California rules, speed limits, and new 2026 laws.")
    st.warning("#### 📇 Flashcards\nQuick-fire memory test. Flip the cards to memorize the most common questions.")

with col2:
    st.success("#### 📝 Practice Exam\nTake a randomized 10-question test. Aim for 83% or higher to pass!")
    st.error("#### 📺 Video Practice\nSit back, relax, and watch real DMV questions being answered and explained.")

st.divider()

# --- COUNTDOWN WIDGET ---
st.write("### 🎯 Test Day Tracker")
st.write("Set your DMV appointment date below to start the countdown!")

# Interactive calendar widget
test_date = st.date_input("When is your permit test?", value=None)

if test_date:
    today = datetime.date.today()
    days_left = (test_date - today).days
    
    if days_left > 0:
        # Streamlit's metric widget looks very sleek and professional
        st.metric(label="Days until test day!", value=days_left)
        st.write("You've got this! Just take it one study session at a time.")
    elif days_left == 0:
        st.balloons()
        st.success("Today is the day! Take a deep breath. You are going to do great! 🚙💨")
    else:
        st.write("Test day has passed! Hopefully, you're officially holding that permit! 🎉")
