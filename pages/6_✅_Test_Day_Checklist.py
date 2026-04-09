import streamlit as st

st.title("✅ Test Day Checklist")
st.write("The San Diego DMV is notoriously strict about paperwork. Use this checklist to make sure you have everything packed in your bag before you leave the house!")

st.subheader("The Essentials")
st.checkbox("Confirmation Code from your online application")
st.checkbox("$45 Application Fee (Cash, check, or debit card - NO credit cards!)")

st.write("---")
st.subheader("REAL ID Documents (Must be physical, printed copies)")
st.checkbox("1. Proof of Identity (Valid Passport OR original Birth Certificate)")
st.checkbox("2. Proof of Social Security (SSN Card OR W-2 Form)")
st.checkbox("3. First Proof of California Residency (e.g., Lease agreement, utility bill)")
st.checkbox("4. Second Proof of California Residency (e.g., Bank statement, cell phone bill)")

st.write("---")
st.info("💡 **Pro Tip:** Make sure your residency documents show your name exactly as it appears on your ID proof, and ensure they are dated within the last 90 days!")
