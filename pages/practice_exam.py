import streamlit as st
import random

st.title("📝 Practice Exam")
st.write("Let's test your knowledge! The test will generate a random set of questions each time.")

# --- THE MASTER QUESTION BANK ---
# Add ALL of your questions here. The app will randomly select from this list.
QUESTION_BANK = [
    {
        "q": "When you park facing downhill on a street with a curb, turn your wheels:",
        "options": ["Toward the curb", "Away from the curb", "Straight ahead"],
        "answer": "Toward the curb",
        "explanation": "Turning wheels toward the curb stops the car from rolling into traffic if brakes fail."
    },
    {
        "q": "You must notify the DMV within 5 days if you:",
        "options": ["Paint your vehicle a different color", "Sell or transfer your vehicle", "Fail a smog test"],
        "answer": "Sell or transfer your vehicle",
        "explanation": "CA law requires a Notice of Transfer and Release of Liability within 5 days of a sale."
    },
    {
        "q": "It is illegal for a person 21 years of age or older to drive with a BAC that is:",
        "options": ["0.08% or higher", "0.04% or higher", "0.01% or higher"],
        "answer": "0.08% or higher",
        "explanation": "For adults 21+, the legal limit is 0.08%."
    },
    {
        "q": "A flashing red traffic light at an intersection means:",
        "options": ["Stop before entering", "Yield to all traffic before entering", "Stop only if other cars are approaching"],
        "answer": "Stop before entering",
        "explanation": "A flashing red light is treated exactly the same as a stop sign."
    },
    {
        "q": "Solid yellow lines separate:",
        "options": ["Vehicles traveling in the same direction", "Vehicles traveling in opposite directions", "Bicycle lanes from regular traffic"],
        "answer": "Vehicles traveling in opposite directions",
        "explanation": "Yellow lines divide opposing traffic. White lines divide traffic moving the same way."
    },
    {
        "q": "What is the speed limit in a residential area unless otherwise posted?",
        "options": ["15 mph", "25 mph", "35 mph"],
        "answer": "25 mph",
        "explanation": "The default speed limit for residential and business districts is 25 mph."
    },
    {
        "q": "Two sets of solid, double, yellow lines that are two or more feet apart:",
        "options": ["May be crossed to enter or exit a private driveway", "May not be crossed for any reason", "Should be treated as a separate traffic lane"],
        "answer": "May not be crossed for any reason",
        "explanation": "Two sets of solid double yellow lines spaced 2+ feet apart are considered a barrier."
    },
    {
        "q": "When driving in fog, you should use your:",
        "options": ["Fog lights only", "High beams", "Low beams"],
        "answer": "Low beams",
        "explanation": "High beams will reflect off the fog and impair your visibility. Always use low beams."
    }
]

# --- EXAM SETUP & RANDOMIZATION ---
# Set how many questions you want per test. Change this to 46 when you have enough questions!
NUM_QUESTIONS_PER_TEST = 5 

# We use session_state so the questions don't randomly change every time she clicks a button
if 'current_test' not in st.session_state:
    # Randomly select a batch of questions from the master bank
    st.session_state.current_test = random.sample(QUESTION_BANK, NUM_QUESTIONS_PER_TEST)
    st.session_state.exam_submitted = False
    st.session_state.user_answers = {}

# --- RENDER THE EXAM ---
if not st.session_state.exam_submitted:
    for i, q_data in enumerate(st.session_state.current_test):
        st.write(f"**{i + 1}. {q_data['q']}**")
        # Save answers to session state as they click
        st.session_state.user_answers[i] = st.radio(
            f"Options for Q{i}", 
            q_data['options'], 
            index=None, 
            label_visibility="collapsed", 
            key=f"q_{i}"
        )
        st.write("---")

    if st.button("Submit Exam"):
        st.session_state.exam_submitted = True
        st.rerun()

# --- GRADING AND REVIEW SCREEN ---
else:
    st.header("📊 Exam Results")
    score = 0
    wrong_answers = []

    # Calculate score and gather wrong answers
    for i, q_data in enumerate(st.session_state.current_test):
        user_ans = st.session_state.user_answers.get(i)
        if user_ans == q_data['answer']:
            score += 1
        else:
            wrong_answers.append({
                "question": q_data['q'],
                "user_ans": user_ans if user_ans else "Skipped",
                "correct_ans": q_data['answer'],
                "explanation": q_data['explanation']
            })

    # Display final score
    percentage = (score / NUM_QUESTIONS_PER_TEST) * 100
    st.subheader(f"Final Score: {score} / {NUM_QUESTIONS_PER_TEST} ({percentage:.0f}%)")
    
    if percentage >= 83:  
        st.balloons()
        st.success("🎉 You passed! Great job!")
    else:
        st.error("Keep studying! You need at least an 83% to pass the real exam.")

    # Show review of wrong answers
    if len(wrong_answers) > 0:
        st.write("### 🛑 Let's review what you missed:")
        for idx, wrong in enumerate(wrong_answers):
            with st.expander(f"Question {idx + 1} Review"):
                st.write(f"**Question:** {wrong['question']}")
                st.write(f"❌ **You answered:** {wrong['user_ans']}")
                st.write(f"✅ **Correct answer:** {wrong['correct_ans']}")
                st.info(f"**Why:** {wrong['explanation']}")

    # Retake button resets the session state to generate a new test
    st.write("---")
    if st.button("🔄 Retake Exam with New Questions"):
        st.session_state.current_test = random.sample(QUESTION_BANK, NUM_QUESTIONS_PER_TEST)
        st.session_state.exam_submitted = False
        st.session_state.user_answers = {}
        st.rerun()

