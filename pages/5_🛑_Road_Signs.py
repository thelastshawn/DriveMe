import streamlit as st

st.title("🛑 Visual Sign Practice")
st.write("The DMV will test your ability to recognize signs strictly by their shape and color. Tap 'Reveal Answer' to see if you got it right!")

# Mega bank of image-based sign questions with ultra-stable URLs
sign_bank = [
    {"img": "https://www.trafficsign.us/signimg/W3-1.gif", "q": "What does this sign mean?", "a": "Stop Ahead."},
    {"img": "https://www.trafficsign.us/signimg/W8-5.gif", "q": "What does this sign mean?", "a": "Slippery When Wet. Slow down and avoid hard braking."},
    {"img": "https://www.trafficsign.us/signimg/R1-2.gif", "q": "What does this shape always indicate?", "a": "Yield. You must let other traffic go first."},
    {"img": "https://www.trafficsign.us/signimg/W4-2.gif", "q": "What does this sign mean?", "a": "Lane Ends / Merge Left."},
    {"img": "https://www.trafficsign.us/signimg/R5-1.gif", "q": "What does this sign mean?", "a": "Do Not Enter. Usually marks a one-way street or off-ramp."}
]

if 'sign_index' not in st.session_state:
    st.session_state.sign_index = 0
if 'show_sign_answer' not in st.session_state:
    st.session_state.show_sign_answer = False

current_sign = sign_bank[st.session_state.sign_index]

# Added a fixed width so the signs aren't massively blown up on her phone screen
st.image(current_sign['img'], width=150)
st.subheader(current_sign['q'])

if st.button("Reveal Answer 👀"):
    st.session_state.show_sign_answer = not st.session_state.show_sign_answer

if st.session_state.show_sign_answer:
    st.success(current_sign['a'])

st.write("---")

if st.button("Next Sign ➡️"):
    st.session_state.show_sign_answer = False
    if st.session_state.sign_index < len(sign_bank) - 1:
        st.session_state.sign_index += 1
    else:
        st.session_state.sign_index = 0
    st.rerun()
