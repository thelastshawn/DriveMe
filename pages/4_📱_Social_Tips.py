import streamlit as st
import streamlit.components.v1 as components

st.title("📱 The Social Feed")
st.write("Stay in the loop with real-world tips, trick questions, and advice from San Diego locals and driving instructors across social media.")

st.divider()

st.subheader("🎵 TikTok Advice")
st.write("Watch driving instructors explain common mistakes on the California test.")

# To change this video: Go to any TikTok on your computer, click "Share" -> "Embed" -> "Copy Code", and paste it between the triple quotes below!
tiktok_embed_code = """
<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@driving_school_answers/video/7198755018698296619" data-video-id="7198755018698296619" style="max-width: 605px;min-width: 325px;" > <section> <a target="_blank" title="@driving_school_answers" href="https://www.tiktok.com/@driving_school_answers?refer=embed">@driving_school_answers</a> California DMV test tips! <a target="_blank" title="♬ original sound - Driving School Answers" href="https://www.tiktok.com/music/original-sound-7198755050180414250?refer=embed">♬ original sound - Driving School Answers</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
"""
components.html(tiktok_embed_code, height=600, scrolling=True)


st.divider()

st.subheader("🐦 X / Twitter Updates")
st.write("Quick reminders for the road.")

# To change this tweet: Go to any Tweet on your computer, click "Share" -> "Embed Tweet", and paste it between the triple quotes below!
tweet_embed_code = """
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Top reason people fail their California driving test: Not exaggerating head movements when checking blind spots! The examiner needs to SEE you looking over your shoulder. Don&#39;t just use your eyes! 👀🚗💨 <a href="https://twitter.com/hashtag/DMVtips?src=hash&amp;ref_src=twsrc%5Etfw">#DMVtips</a> <a href="https://twitter.com/hashtag/California?src=hash&amp;ref_src=twsrc%5Etfw">#California</a></p>&mdash; DMV Prep Bot (@DMVPrepBot) <a href="https://twitter.com/DMVPrepBot/status/1785000000000000000?ref_src=twsrc%5Etfw">April 29, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
"""
components.html(tweet_embed_code, height=450, scrolling=True)

st.info("💡 **Want to add a specific post?** Just grab the 'Embed Code' from any TikTok or Tweet and paste it into the code file for this page!")
