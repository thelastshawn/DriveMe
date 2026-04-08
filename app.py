import streamlit as st

st.set_page_config(page_title="DriveMe: CA DMV Prep", page_icon="🚗", layout="centered")

st.title("🚗 Welcome to DriveMe!")
st.subheader("Your personal California DMV Permit study buddy.")

st.write("I built this app specifically to help you ace your permit test and get on the road in San Diego! Here is a quick breakdown of how to use it:")

st.markdown("""
* **📖 Study Guide:** Start here. It covers all the core rules, new 2026 laws, speed limits, and right-of-way concepts you need to know.
* **📇 Flashcards:** Once you've read the guide, use these quick-fire cards to test your memory on the most common questions.
* **📝 Practice Exam:** Take a randomized 10-question practice test. You need an 83% to pass the real thing, so keep practicing until you hit that mark consistently!
* **📺 Video Practice:** Sit back and watch a breakdown of essential exam questions to get used to the tricky wording.
""")

st.write("---")
st.success("You've got this! Take your time, review the materials, and you'll be holding that permit in no time. 🚙💨")




