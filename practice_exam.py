import streamlit as st

st.title("📝 Practice Exam")
st.write("Let's test your knowledge! Select the best answer for each question.")

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
    }
]

user_answers = {}

for i, q_data in enumerate(exam_questions):
    st.write(f"**{q_data['q']}**")
    user_answers[i] = st.radio(f"Options for Q{i}", q_data['options'], index=None, label_visibility="collapsed", key=f"q_{i}")
    st.write("---")

if st.button("Submit Exam"):
    score = 0
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
    
    percentage = (score / len(exam_questions)) * 100
    if percentage >= 83:  
        st.balloons()
        st.success("You passed! Great job!")
    else:
        st.error("Keep studying! You need at least an 83% to pass the real exam.")
