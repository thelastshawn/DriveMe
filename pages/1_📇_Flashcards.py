import streamlit as st
import random

st.title("📇 Quick-Fire Flashcards")
st.write("Test your memory! The deck is randomly shuffled. Click to flip the card.")

# --- THE MASTER FLASHCARD DECK ---
MASTER_CARDS = [
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
    {"q": "How many feet before a turn must you activate your turn signal?", "a": "100 feet."},
    {"q": "What is the penalty for abandoning an animal on a highway?", "a": "A fine of up to $1,000, 6 months in jail, or both."},
    {"q": "When passing a bicyclist, how much space must you give them?", "a": "At least 3 feet of clearance."},
    {"q": "What does a diamond-shaped sign indicate?", "a": "Warning of a possible hazard ahead."},
    {"q": "When making a right turn, when should you enter the bike lane?", "a": "No more than 200 feet before the intersection."},
    {"q": "What is the 'No Zone'?", "a": "The large blind spots around commercial trucks and buses where cars disappear from the driver's view."},
    {"q": "How long do you have to notify the DMV if you change your address?", "a": "10 days."},
    {"q": "What is the default speed limit in a school zone when children are present?", "a": "20 mph (new 2026 law) or 25 mph depending on posted signage."},
    {"q": "At a T-intersection without stop signs, who yields?", "a": "Vehicles on the terminating street must yield to vehicles on the through street."},
    {"q": "When is it legal to do a U-turn in a business district?", "a": "Only at intersections or through openings in a concrete divider."},
    {"q": "What must you do if you are involved in a crash with property damage over $1,000?", "a": "Report it to the DMV within 10 days using form SR 1."},
    {"q": "What does a red arrow traffic light mean?", "a": "'STOP'. You may not turn against a red arrow."},
    {"q": "What is the hand signal for a right turn?", "a": "Left arm bent at the elbow, pointing upward."},
    {"q": "What is the hand signal for slowing down or stopping?", "a": "Left arm bent at the elbow, pointing downward."},
    {"q": "When you park on a level street, how close must your wheels be to the curb?", "a": "Within 18 inches."},
    {"q": "Can you legally pass a vehicle on the right by driving off the paved road?", "a": "No, you may never drive off the paved main-traveled portion of the road to pass."},
    {"q": "What shape is a standard Yield sign?", "a": "An inverted (upside-down) triangle."},
    {"q": "If two vehicles arrive at a 4-way stop at the same time, who goes first?", "a": "The vehicle on the right."},
    {"q": "How long must you signal before changing lanes on a freeway?", "a": "At least 5 seconds."},
    {"q": "Is it legal to wear a headset or earplugs covering both ears while driving?", "a": "No, it is illegal to cover both ears."},
    {"q": "What should you do if you are driving and a dust storm blows across the freeway?", "a": "Turn on your headlights. Do not drive with only your parking or fog lights."}
]

# --- SESSION STATE INITIALIZATION ---
# This ensures the deck is shuffled when she first opens the page
if 'shuffled_cards' not in st.session_state:
    st.session_state.shuffled_cards = random.sample(MASTER_CARDS, len(MASTER_CARDS))
if 'card_index' not in st.session_state:
    st.session_state.card_index = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

# Grab the currently active deck and card
deck = st.session_state.shuffled_cards
current_card = deck[st.session_state.card_index]

# --- DISPLAY THE CARD ---
st.subheader(f"Card {st.session_state.card_index + 1} of {len(deck)}")
st.info(current_card['q'])

# Flip Button
if st.button("Flip Card 🔄"):
    st.session_state.show_answer = not st.session_state.show_answer

# Show Answer
if st.session_state.show_answer:
    st.success(current_card['a'])

st.write("---")

# --- NAVIGATION BUTTONS ---
# Using columns to place buttons side-by-side for a clean UI
col1, col2, col3 = st.columns([1, 1, 1.2])

with col1:
    if st.button("⬅️ Previous"):
        st.session_state.show_answer = False
        # Go back, but loop to the end if she is on the first card
        if st.session_state.card_index > 0:
            st.session_state.card_index -= 1
        else:
            st.session_state.card_index = len(deck) - 1 
        st.rerun()

with col2:
    if st.button("Next ➡️"):
        st.session_state.show_answer = False
        # Go forward, but loop to the beginning if she is on the last card
        if st.session_state.card_index < len(deck) - 1:
            st.session_state.card_index += 1
        else:
            st.session_state.card_index = 0 
        st.rerun()

with col3:
    # A manual reshuffle button so she can get a new randomized order anytime
    if st.button("🔀 Reshuffle Deck"):
        st.session_state.shuffled_cards = random.sample(MASTER_CARDS, len(MASTER_CARDS))
        st.session_state.card_index = 0
        st.session_state.show_answer = False
        st.rerun()
