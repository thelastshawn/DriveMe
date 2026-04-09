import streamlit as st

st.title("📇 Quick-Fire Flashcards")
st.write("Test your memory! Click to flip the card.")

cards = [
    {"q": "What is the speed limit in a blind intersection?", "a": "15 mph"},
    {"q": "What does a solid yellow line mean?", "a": "Separates traffic going in opposite directions; no passing."},
    {"q": "What is the BAC limit for someone under 21?", "a": "0.01% (Zero Tolerance)"},
    {"q": "If you park facing uphill next to a curb, which way do you turn your wheels?", "a": "Away from the curb."},
    {"q": "What is the speed limit in a residential area?", "a": "25 mph"},
    {"q": "What should you do if a school bus flashes red lights?", "a": "Stop in both directions until the lights stop flashing (unless on a divided highway)."},
    {"q": "What is the 'Three-Second Rule' used for?", "a": "Maintaining a safe following distance."},
    {"q": "What does a flashing red traffic light mean?", "a": "Treat it exactly like a stop sign."},
    {"q": "When are you allowed to cross double solid yellow lines?", "a": "Only to turn left into or out of a private driveway or business."},
    {"q": "When is it legal to use a cell phone without hands-free mode?", "a": "Only to make an emergency call to law enforcement or medical providers."},
    {"q": "What happens if you refuse a blood or breath test?", "a": "Your license will automatically be suspended."},
    {"q": "When should you use your high-beam headlights?", "a": "On dark city streets or open country roads with no other cars nearby."},
    {"q": "How many feet before a turn must you activate your turn signal?", "a": "100 feet."}
]

if 'card_index' not in st.session_state:
    st.session_state.card_index = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

current_card = cards[st.session_state.card_index]

st.subheader(f"Card {st.session_state.card_index + 1} of {len(cards)}")
st.info(current_card['q'])

if st.button("Flip Card 🔄"):
    st.session_state.show_answer = not st.session_state.show_answer

if st.session_state.show_answer:
    st.success(current_card['a'])

st.write("---")
if st.button("Next Card ➡️"):
    st.session_state.show_answer = False 
    if st.session_state.card_index < len(cards) - 1:
        st.session_state.card_index += 1
    else:
        st.session_state.card_index = 0
    st.rerun()
