import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="CA DMV Study Buddy", page_icon="🚗", layout="centered")

# --- NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["📖 Study Guide", "📇 Flashcards", "📝 Practice Exam"])

# --- PAGE 1: STUDY GUIDE ---
if page == "📖 Study Guide":
    st.title("🚗 California Permit Study Guide")
    st.write("Review these core concepts before taking the practice exam!")
    
    st.header("1. Speed Limits")
    st.markdown("""
    * **School Zones:** 25 mph (when children are present).
    * **Blind Intersections & Alleys:** 15 mph.
    * **Residential Districts:** 25 mph.
    """)
    
    st.header("2. Right-of-Way")
    st.markdown("""
    * **Four-Way Stop:** First to arrive goes first. Tie? The car on the **right** goes first.
    * **Roundabouts:** Traffic inside the circle has the right-of-way.
    """)
    
    st.header("3. Curbs")
    st.markdown("""
    * **Red:** No parking.
    * **Blue:** Disabled parking only.
    * **White:** Passenger drop-off only.
    """)

# --- PAGE 2: FLASHCARDS ---
elif page == "📇 Flashcards":
    st.title("📇 Quick-Fire Flashcards")
    
    # Database of flashcards
    cards = [
        {"q": "What is the speed limit in a blind intersection?", "a": "15 mph"},
        {"q": "What does a solid yellow line mean?", "a": "No passing allowed."},
        {"q": "What is the BAC limit for someone under 21?", "a": "0.01% (Zero Tolerance)"}
    ]
    
    # Initialize session state for the card index and flip state
    if 'card_index' not in st.session_state:
        st.session_state.card_index = 0
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False

    # Current card
    current_card = cards[st.session_state.card_index]

    # Display the card
    st.subheader("Question:")
    st.info(current_card['q'])

    # Flip Button
    if st.button("Flip Card 🔄"):
        st.session_state.show_answer = not st.session_state.show_answer

    # Show Answer
    if st.session_state.show_answer:
        st.subheader("Answer:")
        st.success(current_card['a'])

    # Next Card Button
    st.write("---")
    if st.button("Next Card ➡️"):
        st.session_state.show_answer = False # Reset flip state
        # Loop back to the first card if at the end
        if st.session_state.card_index < len(cards) - 1:
            st.session_state.card_index += 1
        else:
            st.session_state.card_index = 0
        st.rerun()

# --- PAGE 3: PRACTICE EXAM ---
elif page == "📝 Practice Exam":
    st.title("📝 Practice Exam")
    st.write("Let's test your knowledge. Good luck!")

    # Question 1
    st.write("**1. When you park facing downhill on a street with a curb, turn your wheels:**")
    q1 = st.radio("Q1 Options", 
                  ["Toward the curb", "Away from the curb", "Straight ahead"], 
                  label_visibility="collapsed")

    # Question 2
    st.write("**2. You must notify the DMV within 5 days if you:**")
    q2 = st.radio("Q2 Options", 
                  ["Paint your vehicle a different color", "Sell or transfer your vehicle", "Fail a smog test"], 
                  label_visibility="collapsed")

    st.write("---")
    
    # Grading logic
    if st.button("Submit Exam"):
        score = 0
        
        # Check Q1
        if q1 == "Toward the curb":
            st.success("Q1 is Correct! Wheels toward the curb prevents rolling into traffic.")
            score += 1
        else:
            st.error("Q1 is Incorrect. You want your wheels to roll into the curb, not the street.")
            
        # Check Q2
        if q2 == "Sell or transfer your vehicle":
            st.success("Q2 is Correct!")
            score += 1
        else:
            st.error("Q2 is Incorrect. You must notify the DMV when you sell/transfer a car.")
            
        st.subheader(f"Final Score: {score} / 2")
        if score == 2:
            st.balloons() # Streamlit's built-in celebration animation!
