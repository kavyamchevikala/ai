import pandas as pd
from sklearn.cluster import KMeans
import google.generativeai as genai

# Set your Gemini API key
API_KEY = "AIzaSyB-mlN4U53RzRCsraV121zStA4jUyKNxGI"  # replace with your real key!
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")


def get_gemini_tip(profile):
    prompt = f"Give a short, friendly investment tip for a {profile.lower()} risk teen investor. Keep it under 50 words."
    try:
        response = model.generate_content(prompt)
        return response.text.strip() if response.text else "No tip generated. Try again later."
    except Exception as e:
        return f"Error generating tip: {e}"


def run_kmeans_quiz(answers_dict):
    # Convert answers into a DataFrame
    data = pd.DataFrame([answers_dict])

    fake_data = pd.DataFrame([
        {"risk_attitude": 0, "duration": 0, "reaction": 0,
         "experience": 0, "volatility": 0, "goal": 0, "knowledge": 0},
        {"risk_attitude": 1, "duration": 1, "reaction": 1,
         "experience": 1, "volatility": 1, "goal": 1, "knowledge": 1},
        {"risk_attitude": 2, "duration": 2, "reaction": 2,
         "experience": 2, "volatility": 2, "goal": 2, "knowledge": 2}
    ])

    model_kmeans = KMeans(n_clusters=3, n_init="auto", random_state=42)
    model_kmeans.fit(fake_data)
    cluster = model_kmeans.predict(data)[0]

    risk_map = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}
    profile = risk_map[cluster]
    return profile


risk_descriptions = {
    "Low Risk": {
        "persona_name": "The Safe Saver",
        "description": "You prefer safety and steady growth.",
        "suggested_investments": ["High-yield savings accounts", "Bonds", "Index funds"]
    },
    "Medium Risk": {
        "persona_name": "The Balanced Builder",
        "description": "You balance risk and reward carefully.",
        "suggested_investments": ["ETFs", "Dividend stocks", "Balanced mutual funds"]
    },
    "High Risk": {
        "persona_name": "The Bold Achiever",
        "description": "You’re bold and ready to take big swings!",
        "suggested_investments": ["Individual stocks", "Cryptocurrency", "Growth funds"]
    }
}
