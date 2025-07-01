import streamlit as st
from utils.logic import risk_descriptions, get_gemini_tip

st.title("🎯 Your RiskWise Results")

profile = st.session_state.get("profile", None)

if profile is None:
    st.error("No quiz data found. Please complete the quiz first!")
    st.page_link("pages/1_Quiz.py", label="👉 Go to Quiz")
else:
    persona = risk_descriptions[profile]
    st.header(f"🧑‍💼 Persona Name: **{persona['persona_name']}**")
    st.subheader(f"Risk Level: **{profile}**")
    st.write(persona["description"])

    st.markdown("### 💰 Suggested Investment Types:")
    for inv in persona["suggested_investments"]:
        st.write(f"- {inv}")

    with st.spinner("🤖 Generating a personalized tip..."):
        tip = get_gemini_tip(profile)

    st.success("💬 Gemini AI Tip:")
    st.write(tip)
