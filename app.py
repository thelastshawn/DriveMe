import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="DriveMe: CA DMV Prep", page_icon="🚗", layout="centered")

# --- NAVIGATION ---
st.sidebar.title("DriveMe Menu")
page = st.sidebar.radio("Go to:", ["📖 Study Guide", "📇 Flashcards", "📝 Practice Exam"])

# --- PAGE 1: STUDY GUIDE ---
if page == "📖 Study Guide":
    st.title("🚗 California Permit Study Guide")
    st.write("Master these core concepts before taking the practice exam!")
    
    st.header("1. Speed Limits")
    st.markdown("""
    * **School Zones:** 25 mph (when children are present).
    * **Blind Intersections & Alleys:** 15 mph.
    * **Railroad Crossings (Blind):** 15 mph.
    * **Residential/Business Districts:** 25 mph.
    """)
    
    st.header("2. Right-of-Way")
    st.markdown("""
    * **Four-Way Stop:** First to arrive goes first. If you arrive at the same time, the car on the **right** goes first.
    * **T-Intersections:** Vehicles on the through road have the right-of-way.
    * **Roundabouts:** Traffic inside the circle has the right-of-way. Yield before entering.
    * **Pedestrians:** ALWAYS have the right-of-way in marked or unmarked crosswalks.
    """)
    
    st.header("3. Curbs & Parking")
    st.markdown("""
    * **Red:** No parking, stopping, or standing.
    * **Blue:** Disabled parking only (requires placard).
    * **White:** Passenger drop-off or mail pick-up only.
    * **Yellow:** Commercial loading/unloading.
    * **Green:** Short-term parking (time limit posted).
    * **Hills:** Downhill = wheels toward the curb. Uphill = wheels away from the curb.
    """)

    st.header("4. Alcohol & Drugs")
    st.markdown("""
    * **Under 21:** 0.01% BAC limit (Zero Tolerance).
    * **21 and Older:** 0.08% BAC limit.
    * **Refusing a Test:** Your license will automatically be suspended if you refuse a blood, breath, or urine test.
    """)

    st.header("5. Line Colors & Meanings")
    st.markdown("""
    * **Solid Yellow:** No passing. Separates traffic moving in opposite directions.
    * **Broken Yellow:** You may pass if the line is on your side.
    * **Solid White:** Separates lanes of traffic going in the same direction.
    """)

# --- PAGE 2: FLASHCARDS ---
elif page == "📇 Flashcards":
    st.title("📇 Quick-Fire Flashcards")
    st.write("Test your memory! Click to flip the card.")
    
    # Expanded database of flashcards
    cards = [
        {"q": "What is the speed limit in a blind intersection?", "a": "15 mph"},
        {"q": "What does a solid yellow line mean?", "a": "Separates traffic going in opposite directions; no passing."},
        {"q": "What is the BAC limit for someone under 21?", "a": "0.01% (Zero Tolerance)"},
        {"q": "If you park facing uphill next to a curb, which way do you turn your wheels?", "a": "Away from the curb."},
        {"q": "What is the speed limit in a residential area unless otherwise posted?", "a": "25 mph"},
        {"q": "What should you do if a school bus flashes red lights?", "a": "Stop in both directions until the lights stop flashing (unless on a divided highway)."},
        {"q": "What is the 'Three-Second Rule' used for?", "a": "Maintaining a safe following distance."},
        {"q": "What does a flashing red traffic light mean?", "a": "Treat it exactly like a stop sign."}
    ]
    
    # Initialize session state for the card index and flip state
    if 'card_index' not in st.session_state:
        st.session_state.card_index = 0
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False

    # Current card
    current_card = cards[st.session_state.card_index]

    # Display the card
    st.subheader(f"Card {st.session_state.card_index + 1} of {len(cards)}")
    st.info(current_card['q'])

    # Flip Button
    if st.button("Flip Card 🔄"):
        st.session_state.show_answer = not st.session_state.show_answer

    # Show Answer
    if st.session_state.show_answer:
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
    st.write("Let's test your knowledge! Select the best answer for each question.")

    # Exam questions stored as a list of dictionaries (easy to add more!)
    exam_questions = [
        {
            "q": "1. When you park facing downhill on a street with a curb, turn your wheels:",
            "options": ["Toward the curb", "Away from the curb", "Straight ahead"],
            "answer": "Toward the curb",
            "explanation": "Turning your wheels toward the curb ensures the car will roll into the curb and stop if the brakes fail."
        },
        {
            "q": "2. You must notify the DMV within 5 days if you:",
            "options": ["Paint your vehicle a different color", "Sell or transfer your vehicle", "Fail a smog test"],
            "answer": "Sell or transfer your vehicle",
            "explanation": "California law requires you to submit a Notice of Transfer and Release of Liability within 5 days of a sale."
        },
        {
            "q": "3. It is illegal for a person 21 years of age or older to drive with a blood alcohol concentration (BAC) that is:",
            "options": ["0.08% or higher", "0.04% or higher", "0.01% or higher"],
            "answer": "0.08% or higher",
            "explanation": "For drivers 21 and older, the legal limit is strictly under 0.08%."
        },
        {
            "q": "4. You are approaching a railroad crossing with no warning devices and are unable to see 400 feet down the tracks. The speed limit is:",
            "options": ["15 mph", "20 mph", "25 mph"],
            "answer": "15 mph",
            "explanation": "This is considered a 'blind' railroad crossing, and the speed limit is 15 mph to ensure you can stop safely."
        },
        {
            "q": "5. Solid yellow lines separate:",
            "options": ["Vehicles traveling in the same direction", "Vehicles traveling in opposite directions", "Bicycle lanes from regular traffic"],
            "answer": "Vehicles traveling in opposite directions",
            "explanation": "Yellow lines divide traffic traveling in opposite directions, while white lines divide traffic moving in the same direction."
        }
    ]

    # Store the user's answers in a dictionary
    user_answers = {}

    # Dynamically generate the radio buttons for every question
    for i, q_data in enumerate(exam_questions):
        st.write(f"**{q_data['q']}**")
        # Generate radio buttons. Note the 'key' argument which keeps Streamlit from getting confused.
        user_answers[i] = st.radio(f"Options for Q{i}", q_data['options'], index=None, label_visibility="collapsed", key=f"q_{i}")
        st.write("---")

    # Grading logic
    if st.button("Submit Exam"):
        score = 0
        
        # Check all answers
        for i, q_data in enumerate(exam_questions):
            st.write(f"**{q_data['q']}**")
            if user_answers[i] == q_data['answer']:
                st.success(f"Correct! {q_data['explanation']}")
                score += 1
            elif user_answers[i] is None:
                st.warning("You skipped this question.")
            else:
                st.error(f"Incorrect. The correct answer is: {q_data['answer']}. {q_data['explanation']}")
            st.write("---")
            
        st.subheader(f"Final Score: {score} / {len(exam_questions)}")
        
        # Calculate percentage
        percentage = (score / len(exam_questions)) * 100
        if percentage >= 83:  # 83% is roughly passing for the actual CA DMV
            st.balloons()
            st.success("You passed! Great job!")
        else:
            st.error("Keep studying! You need at least an 83% to pass the real exam.")

