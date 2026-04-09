import streamlit as st

st.title("📺 Video Walkthroughs")
st.write("Sometimes it helps to actually *see* the rules in action. Watch these driving instructors break down the California exam and explain the most common mistakes.")

st.divider()

st.subheader("1. The Most Common CA DMV Mistakes")
st.write("Examiners in California are incredibly strict about these specific habits. Watch out for them!")
# Streamlit's native video player - loads perfectly on mobile!
st.video("https://www.youtube.com/watch?v=s1RzIEG5DQQ") 

st.divider()

st.subheader("2. How to Perfectly Check Your Blind Spots")
st.write("Remember the daily tip: Examiners watch your head, not your eyes!")
st.video("https://www.youtube.com/watch?v=Fj-E_w2kX3Q")

st.divider()

st.subheader("3. Right-of-Way Rules Explained")
st.write("A quick visual breakdown of who goes first at 4-way stops and intersections.")
st.video("https://www.youtube.com/watch?v=eJt3k1F9n0M")

st.divider()

st.info("💡 **Pro Tip:** Whenever you find a helpful YouTube video or Short, just paste the link into the code to update your feed!")
