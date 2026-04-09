import streamlit as st
import streamlit.components.v1 as components

st.title("📱 The Social Feed")
st.write("Real-world tips, tricks, and relatable DMV struggles straight from the timeline.")

st.divider()

# --- X / TWITTER FEED ---
st.write("### 🐦 Top Tips from X")

# Notice how the entire embed code (including the <script> tags) is wrapped in triple quotes
tweet_code = """
<blockquote class="twitter-tweet" data-theme="light"><p lang="en" dir="ltr">Top reason people fail their California driving test: Not exaggerating head movements when checking blind spots! The examiner needs to SEE you looking over your shoulder. 👀🚗💨 <a href="https://twitter.com/hashtag/DMVtips?src=hash&amp;ref_src=twsrc%5Etfw">#DMVtips</a></p>&mdash; DMV Prep Bot (@DMVPrepBot) <a href="https://twitter.com/DMVPrepBot/status/1785000000000000000">April 29, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
"""

# components.html actually runs the scripts so the visual widget loads
components.html(tweet_code, height=250, scrolling=True)

st.divider()

# --- TIKTOK FEED ---
st.write("### 🎵 Trending on TikTok")
st.write("Watch instructors break down exact intersections in San Diego.")

tiktok_code = """
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@drivingwithmr.c/video/7279313219759574314" data-video-id="7279313219759574314" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@drivingwithmr.c" href="https://www.tiktok.com/@drivingwithmr.c?refer=embed">@drivingwithmr.c</a> <p>California DMV written test questions 🚗</p> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
"""

# TikToks need a taller height (around 600px) to show the whole vertical video
components.html(tiktok_code, height=650, scrolling=True)

st.write("---")
st.info("💡 **How to add your own:** Go to any TikTok or Tweet, click 'Share', select 'Embed Code', and paste that HTML directly into the code blocks above!")
