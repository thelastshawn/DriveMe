import streamlit as st

st.title("🛑 Visual Sign Practice")
st.write("The DMV will test your ability to recognize signs strictly by their shape and color. Tap 'Reveal Answer' to see if you got it right!")

# Using native iOS emojis as a 100% bulletproof, instant-loading alternative!
sign_bank = [
    {"emoji": "🛑", "q": "What does this 8-sided red sign mean?", "a": "Stop completely before the crosswalk or limit line."},
    {"emoji": "🚸", "q": "What does this yellow pentagon sign mean?", "a": "School Zone / School Crosswalk ahead. Slow down to 25mph (or 20mph in 2026)."},
    {"emoji": "⛔", "q": "What does this red circle with a white line mean?", "a": "Do Not Enter."},
    {"emoji": "🚳", "q": "What does this sign mean?", "a": "No Bicycles allowed."},
    {"emoji": "🔀", "q": "What does a diamond-shaped sign with merging arrows usually indicate?", "a": "Merging Traffic Ahead."},
    {"emoji": "🚦", "q": "What does a sign with a traffic light on it warn you of?", "a": "Traffic Signal Ahead. Be prepared to stop."},
    {"emoji": "🛣️", "q": "What does a green rectangular sign usually indicate?", "a": "Directional guidance, like distances to cities or freeway exits."}
]

if 'sign_index' not in st.session_state:
    st.session_state.sign_index = 0
if 'show_sign_answer' not in st.session_state:
    st.session_state.show_sign_answer = False

current_sign = sign_bank[st.session_state.sign_index]

# This renders the emoji massively in the center of the screen
st.markdown(f"<h1 style='text-align: center; font-size: 120px;'>{current_sign['emoji']}</h1>", unsafe_allow_html=True)
st.subheader(current_sign['q'])

if st.button("Reveal Answer 👀"):
    st.session_state.show_sign_answer = not st.session_state.show_sign_answer

if st.session_state.show_sign_answer:
    st.success(current_sign['a'])

st.write("---")

# Navigation buttons laid out side-by-side
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ Previous Sign"):
        st.session_state.show_sign_answer = False
        if st.session_state.sign_index > 0:
            st.session_state.sign_index -= 1
        else:
            st.session_state.sign_index = len(sign_bank) - 1
        st.rerun()

with col2:
    if st.button("Next Sign ➡️"):
        st.session_state.show_sign_answer = False
        if st.session_state.sign_index < len(sign_bank) - 1:
            st.session_state.sign_index += 1
        else:
            st.session_state.sign_index = 0
        st.rerun()
