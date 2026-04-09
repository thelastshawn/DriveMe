import streamlit as st
import random

st.title("📝 Practice Exam")
st.write("Let's test your knowledge! The test will generate a random set of questions each time.")

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
        "q": "You are driving on a freeway posted for 65 mph. The traffic is traveling at 70 mph. You may legally drive:",
        "options": ["70 mph or faster to keep up with the speed of traffic", "Between 65 mph and 70 mph", "No faster than 65 mph"],
        "answer": "No faster than 65 mph",
        "explanation": "You may never legally drive faster than the posted speed limit, regardless of how fast other traffic is moving."
    },
    {
        "q": "A white painted curb means:",
        "options": ["Loading zone for freight or passengers", "Loading zone for passengers or mail only", "Parking for vehicles with disabled placards"],
        "answer": "Loading zone for passengers or mail only",
        "explanation": "White curbs are strictly for quick passenger drop-offs/pick-ups or depositing mail."
    },
    {
        "q": "When can you drive in a bike lane?",
        "options": ["During rush hour traffic if there are no bicyclists", "When you are within 200 feet of a cross street where you plan to turn right", "Whenever you need to pass a slower vehicle on the right"],
        "answer": "When you are within 200 feet of a cross street where you plan to turn right",
        "explanation": "You must enter the bike lane no more than 200 feet before the corner to make a right turn."
    },
    {
        "q": "Which of these vehicles must always stop before crossing railroad tracks?",
        "options": ["Tank trucks marked with hazardous materials placards", "Motor homes or pickup trucks towing a boat trailer", "Any vehicle with 3 or more axles or weighing more than 4,000 pounds"],
        "answer": "Tank trucks marked with hazardous materials placards",
        "explanation": "Vehicles carrying hazardous materials, as well as most buses, must stop before crossing."
    },
    {
        "q": "California's 'Basic Speed Law' says:",
        "options": ["You should never drive faster than posted speed limits", "You should never drive faster than is safe for current conditions", "The maximum speed limit in California is 70 mph on certain freeways"],
        "answer": "You should never drive faster than is safe for current conditions",
        "explanation": "Even if the limit is 65 mph, if it is raining or foggy, you must slow down to a safe speed."
    },
    {
        "q": "You must turn on your headlights:",
        "options": ["Whenever you use your windshield wipers in bad weather", "Half an hour after sunset to half an hour before sunrise", "Both of the above"],
        "answer": "Both of the above",
        "explanation": "Headlights are required in darkness and whenever weather requires the continuous use of wipers."
    },
    {
        "q": "If you have a green light, but traffic is blocking the intersection, you should:",
        "options": ["Stay out of the intersection until traffic clears", "Enter the intersection and wait until traffic clears", "Merge into another lane and try to go around the traffic"],
        "answer": "Stay out of the intersection until traffic clears",
        "explanation": "It is illegal to block an intersection. Wait until there is enough space for your vehicle on the other side."
    },
    {
        "q": "A flashing yellow traffic signal at an intersection means:",
        "options": ["Stop. Yield to all cross traffic before crossing", "Slow down and be alert at the upcoming intersection", "The traffic signal is broken; treat it as a four-way stop"],
        "answer": "Slow down and be alert at the upcoming intersection",
        "explanation": "A flashing yellow light means 'PROCEED WITH CAUTION'. You do not need to stop, but you must slow down."
    },
    {
        "q": "It is illegal to leave a child age six or younger unattended in a vehicle on a hot day:",
        "options": ["Even if they are secured in a child passenger restraint system", "If they are accompanied by a person 12 years of age or older", "Only if the windows are rolled up"],
        "answer": "Even if they are secured in a child passenger restraint system",
        "explanation": "It is illegal to leave a child 6 or younger unattended. They must be supervised by someone at least 12 years old."
    },
    {
        "q": "Fines in a highway construction or maintenance zone are:",
        "options": ["Tripled", "Doubled", "The same as any other fine"],
        "answer": "Doubled",
        "explanation": "Traffic violation fines can be $1,000 or more and are doubled in highway work zones."
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
    },
    {
        "q": "When you see a school bus stopped with flashing red lights, you must:",
        "options": ["Slow down and pass carefully", "Stop until the lights stop flashing", "Honk to warn the children"],
        "answer": "Stop until the lights stop flashing",
        "explanation": "You must stop from either direction until children are safely across and lights stop flashing, unless on a divided highway."
    },
    {
        "q": "If you are involved in a collision resulting in $1,000+ in damage, you must report it to the DMV within:",
        "options": ["5 days", "10 days", "30 days"],
        "answer": "10 days",
        "explanation": "You have 10 days to file a Report of Traffic Accident Occurring in California (SR 1) to the DMV."
    },
    {
        "q": "Which of these is a safe driving practice?",
        "options": ["Staring right in front of your car", "Keeping your eyes moving to scan surroundings", "Using high beams in rain"],
        "answer": "Keeping your eyes moving to scan surroundings",
        "explanation": "Scanning ahead and checking mirrors keeps you aware of hazards."
    },
    {
        "q": "You are approaching a railroad crossing with no warning devices and cannot see 400 feet down the tracks. The speed limit is:",
        "options": ["15 mph", "25 mph", "35 mph"],
        "answer": "15 mph",
        "explanation": "This is a blind railroad crossing, requiring a speed of 15 mph to stop safely if needed."
    },
    {
        "q": "Who can legally park next to a curb painted blue?",
        "options": ["Anyone dropping off passengers", "Disabled persons with a special placard or plate", "Anyone staying for less than 15 minutes"],
        "answer": "Disabled persons with a special placard or plate",
        "explanation": "Blue curbs are strictly reserved for those with valid disabled placards or license plates."
    },
    {
        "q": "Center turn lanes are marked by:",
        "options": ["Solid yellow lines on both sides", "Broken white lines", "Inner broken yellow lines and outer solid yellow lines"],
        "answer": "Inner broken yellow lines and outer solid yellow lines",
        "explanation": "The center left turn lane is designated by parallel solid and broken yellow lines."
    },
    {
        "q": "When an emergency vehicle with a siren and flashing lights approaches, you must:",
        "options": ["Speed up to get out of the way", "Pull to the right edge of the road and stop", "Stop immediately in your lane"],
        "answer": "Pull to the right edge of the road and stop",
        "explanation": "Always pull over to the right and stop to clear the way for emergency vehicles."
    },
        {
        "q": "You must dim your high-beam headlights to low beams within:",
        "options": ["500 feet of a vehicle coming toward you or 300 feet of a vehicle you are following", "300 feet of a vehicle coming toward you or 500 feet of a vehicle you are following", "200 feet of any other vehicle"],
        "answer": "500 feet of a vehicle coming toward you or 300 feet of a vehicle you are following",
        "explanation": "To avoid blinding other drivers, dim your lights at 500 feet for oncoming traffic and 300 feet when following."
    },
    {
        "q": "A child must be secured in a child passenger restraint system in the rear seat if they are:",
        "options": ["Under 8 years old, or under 4 feet 9 inches tall", "Under 6 years old and weighing less than 60 pounds", "Under 10 years old"],
        "answer": "Under 8 years old, or under 4 feet 9 inches tall",
        "explanation": "California law requires children under 8 years old or under 4'9\" to be properly secured in a rear seat."
    },
    {
        "q": "When merging onto a freeway, you should be driving:",
        "options": ["At or near the same speed as the traffic on the freeway", "5 to 10 mph slower than the traffic on the freeway", "The posted speed limit for traffic on the freeway"],
        "answer": "At or near the same speed as the traffic on the freeway",
        "explanation": "You should merge safely by matching the speed of the flow of traffic, not entering too slowly."
    },
    {
        "q": "A flashing yellow arrow traffic signal means:",
        "options": ["You may turn, but you must first yield to oncoming traffic and pedestrians", "You must stop and wait for a green arrow", "You have the right-of-way to turn"],
        "answer": "You may turn, but you must first yield to oncoming traffic and pedestrians",
        "explanation": "A flashing yellow arrow allows an 'unprotected' turn. You can go, but only when it is safe and clear."
    },
    {
        "q": "When are roadways the most slippery?",
        "options": ["During a heavy downpour", "After it has been raining for a few hours", "The first rain after a dry spell"],
        "answer": "The first rain after a dry spell",
        "explanation": "The first rain mixes with oil and dust on the road, making it incredibly slick for the first few minutes."
    },
    {
        "q": "If your vehicle starts to hydroplane, you should:",
        "options": ["Slam on your brakes to slow down quickly", "Slow down gradually and do not apply the brakes", "Steer sharply toward the shoulder of the road"],
        "answer": "Slow down gradually and do not apply the brakes",
        "explanation": "Hitting the brakes can cause a skid. Take your foot off the gas and let the vehicle slow down naturally."
    },
    {
        "q": "You want to make a right turn at an upcoming intersection. You should slow down and:",
        "options": ["Signal for 100 feet before turning", "Signal only if other vehicles are around", "Move into the left side of your lane"],
        "answer": "Signal for 100 feet before turning",
        "explanation": "Always signal at least 100 feet before making any turn or lane change."
    },
    {
        "q": "What is the correct hand signal for a left turn?",
        "options": ["Left arm extended straight out", "Left arm extended upward", "Left arm extended downward"],
        "answer": "Left arm extended straight out",
        "explanation": "Straight out means left. Pointing up means right. Pointing down means stop or slow down."
    },
]

NUM_QUESTIONS_PER_TEST = 10 

if 'current_test' not in st.session_state:
    st.session_state.current_test = random.sample(QUESTION_BANK, NUM_QUESTIONS_PER_TEST)
    st.session_state.exam_submitted = False
    st.session_state.user_answers = {}

if not st.session_state.exam_submitted:
    for i, q_data in enumerate(st.session_state.current_test):
        st.write(f"**{i + 1}. {q_data['q']}**")
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

else:
    st.header("📊 Exam Results")
    score = 0
    wrong_answers = []

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

    percentage = (score / NUM_QUESTIONS_PER_TEST) * 100
    st.subheader(f"Final Score: {score} / {NUM_QUESTIONS_PER_TEST} ({percentage:.0f}%)")
    
    if percentage >= 83:  
        st.balloons()
        st.success("🎉 You passed! Great job!")
    else:
        st.error("Keep studying! You need at least an 83% to pass the real exam.")

    if len(wrong_answers) > 0:
        st.write("### 🛑 Let's review what you missed:")
        for idx, wrong in enumerate(wrong_answers):
            with st.expander(f"Question {idx + 1} Review"):
                st.write(f"**Question:** {wrong['question']}")
                st.write(f"❌ **You answered:** {wrong['user_ans']}")
                st.write(f"✅ **Correct answer:** {wrong['correct_ans']}")
                st.info(f"**Why:** {wrong['explanation']}")

    st.write("---")
    if st.button("🔄 Retake Exam with New Questions"):
        st.session_state.current_test = random.sample(QUESTION_BANK, NUM_QUESTIONS_PER_TEST)
        st.session_state.exam_submitted = False
        st.session_state.user_answers = {}
        st.rerun()
