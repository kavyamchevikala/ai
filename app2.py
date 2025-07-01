import streamlit as st
import os
from sklearn.cluster import KMeans
import pandas as pd
import google.generativeai as genai

# === Hardcoded Gemini API Key and Configuration ===
API_KEY = "AIzaSyB-mlN4U53RzRCsraV121zStA4jUyKNxGI"  # 🔒 Replace with your actual key
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def get_gemini_tip(profile):
    prompt = f"Give a short, friendly investment tip for a {profile.lower()} risk teen investor. Keep it under 50 words."
    try:
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "No tip generated. Try again later."
    except Exception as e:
        return f"Error generating tip: {e}"

st.set_page_config(page_title="RiskWise", layout="centered")
st.title("💼 RiskWise: AI Risk Profiler for Teen Investors")
st.markdown("Welcome! Answer a few quick questions to discover your investing personality.")

q1 = st.radio("1. How do you feel about taking risks with money?", ["I avoid it", "I'm okay with it", "I love it"])
q2 = st.radio("2. How long do you want to invest for?", ["Less than 1 year", "1–5 years", "More than 5 years"])
q3 = st.radio("3. If your investment drops 20%, you would:", ["Sell everything", "Wait it out", "Buy more"])
q4 = st.radio("4. How experienced are you with investing?", ["I’ve never invested before", "I’ve tried it a little", "I invest regularly"])
q5 = st.radio("5. How do you feel if prices go up and down every day?", ["It stresses me out", "I can handle some ups and downs", "I love the excitement!"])
q6 = st.radio("6. What’s your main goal for investing?", ["Protect my money", "Grow it moderately", "Make big gains fast"])
q7 = st.radio("7. Do you understand how stocks and ETFs work?", ["Not at all", "A little", "Very well"])

if st.button("🔍 Analyze My Profile", key="analyze_button"):
    data = pd.DataFrame([{
        "risk_attitude": {"I avoid it": 0, "I'm okay with it": 1, "I love it": 2}[q1],
        "duration": {"Less than 1 year": 0, "1–5 years": 1, "More than 5 years": 2}[q2],
        "reaction": {"Sell everything": 0, "Wait it out": 1, "Buy more": 2}[q3],
        "experience": {"I’ve never invested before": 0, "I’ve tried it a little": 1, "I invest regularly": 2}[q4],
        "volatility": {"It stresses me out": 0, "I can handle some ups and downs": 1, "I love the excitement!": 2}[q5],
        "goal": {"Protect my money": 0, "Grow it moderately": 1, "Make big gains fast": 2}[q6],
        "knowledge": {"Not at all": 0, "A little": 1, "Very well": 2}[q7]
    }])

    fake_data = pd.DataFrame([
        {"risk_attitude": 0, "duration": 0, "reaction": 0, "experience": 0, "volatility": 0, "goal": 0, "knowledge": 0},
        {"risk_attitude": 1, "duration": 1, "reaction": 1, "experience": 1, "volatility": 1, "goal": 1, "knowledge": 1},
        {"risk_attitude": 2, "duration": 2, "reaction": 2, "experience": 2, "volatility": 2, "goal": 2, "knowledge": 2}
    ])

    model_kmeans = KMeans(n_clusters=3, n_init="auto", random_state=42)
    model_kmeans.fit(fake_data)
    cluster = model_kmeans.predict(data)[0]

    risk_map = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}
    profile = risk_map[cluster]

    st.subheader(f"🎯 Your Risk Profile: *{profile}*")
    descriptions = {
        "Low Risk": "You prefer safety and steady growth.",
        "Medium Risk": "You balance risk and reward carefully.",
        "High Risk": "You’re bold and ready to take big swings!"
    }
    st.write(descriptions[profile])

    with st.spinner("🤖 Getting an AI tip just for you..."):
        tip = get_gemini_tip(profile)

    st.success("💬 Gemini AI Investment Tip:")
    st.write(tip)