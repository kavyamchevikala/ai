import streamlit as st
from utils.logic import run_kmeans_quiz

st.title("📊 RiskWise Quiz")

st.markdown("Answer these questions to discover your investing personality.")

q1 = st.radio("1. How do you feel about taking risks with money?", ["I avoid it", "I'm okay with it", "I love it"])
q2 = st.radio("2. How long do you want to invest for?", ["Less than 1 year", "1–5 years", "More than 5 years"])
q3 = st.radio("3. If your investment drops 20%, you would:", ["Sell everything", "Wait it out", "Buy more"])
q4 = st.radio("4. How experienced are you with investing?", ["I’ve never invested before", "I’ve tried it a little", "I invest regularly"])
q5 = st.radio("5. How do you feel if prices go up and down every day?", ["It stresses me out", "I can handle some ups and downs", "I love the excitement!"])
q6 = st.radio("6. What’s your main goal for investing?", ["Protect my money", "Grow it moderately", "Make big gains fast"])
q7 = st.radio("7. Do you understand how stocks and ETFs work?", ["Not at all", "A little", "Very well"])

if st.button("🔍 Analyze My Profile"):
    answers_dict = {
        "risk_attitude": {"I avoid it": 0, "I'm okay with it": 1, "I love it": 2}[q1],
        "duration": {"Less than 1 year": 0, "1–5 years": 1, "More than 5 years": 2}[q2],
        "reaction": {"Sell everything": 0, "Wait it out": 1, "Buy more": 2}[q3],
        "experience": {"I’ve never invested before": 0, "I’ve tried it a little": 1, "I invest regularly": 2}[q4],
        "volatility": {"It stresses me out": 0, "I can handle some ups and downs": 1, "I love the excitement!": 2}[q5],
        "goal": {"Protect my money": 0, "Grow it moderately": 1, "Make big gains fast": 2}[q6],
        "knowledge": {"Not at all": 0, "A little": 1, "Very well": 2}[q7]
    }

    st.session_state["answers_dict"] = answers_dict

    profile = run_kmeans_quiz(answers_dict)
    st.session_state["profile"] = profile

    st.switch_page("pages/2_Results.py")
