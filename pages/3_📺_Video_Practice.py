import streamlit as st

st.title("📺 Video Walkthroughs")
st.write("Sometimes it helps to actually *see* the rules in action. Watch these driving instructors break down the California exam and explain the most common mistakes.")

st.divider()

st.subheader("1. The CA DMV Written Test (2026)")
st.write("A full breakdown of the real questions you will see on the test this year.")
# Live link to a 2026 CA DMV Written Test guide
st.video("https://www.youtube.com/watch?v=OebXwcsrxsM") 

st.divider()

st.subheader("2. Right-of-Way Rules Explained")
st.write("A quick visual breakdown of who goes first at 4-way stops and intersections.")
# Live link to Right-of-Way intersection rules
st.video("https://www.youtube.com/watch?v=Uws01yip3WM")

st.divider()

st.subheader("3. 2-Way Stop Intersections")
st.write("One of the most confusing parts of driving—who goes first when only two sides have stop signs?")
# Live link to 2-Way Stop Right-of-Way rules
st.video("https://www.youtube.com/watch?v=7MODqVaQVuY")

st.divider()

st.info("💡 **Pro Tip:** Whenever you find a helpful YouTube video or Short, just paste the link into the code to update your feed!")
