import streamlit as st

st.set_page_config(page_title="DriveMe: CA DMV Prep", page_icon="🚗", layout="centered")

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


