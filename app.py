import streamlit as st

st.set_page_config(page_title="DriveMe: CA DMV Prep", page_icon="🚗", layout="centered")

st.title("🚗 California Permit Study Guide")
st.write("Master these core concepts to guarantee a passing score!")

st.header("1. Speed Limits & New 2026 Laws")
st.markdown("""
* **School Zones:** 20 mph (New for 2026 - gradually reducing from 25 mph).
* **Blind Intersections & Alleys:** 15 mph.
* **Railroad Crossings (Blind):** 15 mph.
* **Residential/Business Districts:** 25 mph.
* **Slow Down, Move Over:** You must now slow down and move over for *any* stationary vehicle with flashing hazard lights on the side of the road, not just emergency vehicles.
""")

st.header("2. Right-of-Way")
st.markdown("""
* **Four-Way Stop:** First to arrive goes first. If you arrive at the same time, the car on the **right** goes first.
* **T-Intersections:** Vehicles on the through road have the right-of-way.
* **Pedestrians:** ALWAYS have the right-of-way in marked or unmarked crosswalks. Stop and yield.
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

st.header("4. Special Teen Restrictions (Under 18)")
st.markdown("""
* **Curfew:** You may not drive between 11 p.m. and 5 a.m. for the first 12 months.
* **Passengers:** You cannot transport passengers under 20 years old unless accompanied by a licensed driver 25 or older.
* **Cell Phones:** Absolute ban on cell phone use (even hands-free) while driving.
""")



