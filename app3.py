import streamlit as st

st.set_page_config(page_title="RiskWise", layout="centered")

st.title("💼 Welcome to RiskWise!")

st.markdown("""
Discover your investing personality and get personalized tips for your financial journey.

Are you ready to find out your Risk Persona?
""")

if st.button("🚀 Start Quiz"):
    st.switch_page("pages/1_Quiz.py")
