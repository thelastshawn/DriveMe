import streamlit as st

st.title("📱 The Social Feed")
st.write("Real-world tips, tricks, and relatable DMV struggles straight from social media.")

st.divider()

# --- X / TWITTER FEED ---
st.write("### 🐦 Top Tips from X")

st.info("**@DMVPrepBot:** Top reason people fail their California driving test: Not exaggerating head movements when checking blind spots! The examiner needs to SEE you looking over your shoulder. 👀🚗💨")
st.link_button("View on X ➡️", "https://twitter.com/DMVPrepBot/status/1785000000000000000")

st.divider()

# --- TIKTOK FEED ---
st.write("### 🎵 Trending on TikTok")

st.info("**@drivingwithmr.c:** California DMV written test questions 🚗 Breakdowns of exact intersections and right-of-way rules.")
st.link_button("Watch on TikTok 🎵", "https://www.tiktok.com/@drivingwithmr.c/video/7279313219759574314")

st.divider()

st.write("### 📸 Instagram Reels")

st.info("**@caperteendriving:** Parallel parking hacks that actually work for the California road test.")
st.link_button("Watch on Instagram 📸", "https://www.instagram.com/p/Cxa2R0uL1yB/")

st.write("---")
st.success("💡 **How to add more:** Just copy the link to any social media post and create a new `st.link_button` for it in the code!")
