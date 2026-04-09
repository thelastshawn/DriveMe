import streamlit as st
import random

st.title("🛑 Visual Sign Practice")
st.write("The DMV will test your ability to recognize signs strictly by their shape and color. Tap 'Reveal Answer' to see if you got it right!")

# Mega bank of image-based sign questions
sign_bank = [
    {"img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/MUTCD_W3-1.svg/1024px-MUTCD_W3-1.svg.png", "q": "What does this sign mean?", "a": "Stop Ahead."},
    {"img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/MUTCD_W8-5.svg/1024px-MUTCD_W8-5.svg.png", "q": "What does this sign mean?", "a": "Slippery When Wet. Slow down and avoid hard braking."},
    {"img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/MUTCD_R1-2.svg/1024px-MUTCD_R1-2.svg.png", "q": "What does this shape always indicate?", "a": "Yield. You must let other traffic go first."},
    {"img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/MUTCD_W4-2.svg/1024px-MUTCD_W4-2.svg.png", "q": "What does this sign mean?", "a": "Lane Ends / Merge Left."},
    {"img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/MUTCD_R5-1.svg/1024px-MUTCD_R5-1.svg.png", "q": "What does this sign mean?", "a": "Do Not Enter. Usually marks a one-way street or off-ramp."}
]

if 'sign_index' not in st.session_state:
    st.session_state.sign_index = 0
if 'show_sign_answer' not in st.session_state:
    st.session_state.show_sign_answer = False

current_sign = sign_bank[st.session_state.sign_index]

st.image(current_sign['img'], width=200)
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
