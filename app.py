import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("Mental_Health_Model.pkl")

top_countries = [
    "Other", "India", "USA", "Canada", "Australia",
    "UK", "Germany", "Mexico", "Turkey", "France"
]

st.set_page_config(
    page_title="Mental Health Score",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Mental Health Score Prediction")
st.write("Enter your details to predict the mental health score.")

# Inputs
age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=20
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

country = st.text_input(
    "Country",
    "India"
)

academic_level = st.selectbox(
    "Academic Level",
    ["Undergraduate", "Graduate", "High School"]
)

most_used_platform = st.selectbox(
    "Most Used Platform",
    [
        "Facebook", "LinkedIn", "Instagram", "Snapchat",
        "Twitter", "YouTube", "TikTok", "LINE",
        "KakaoTalk", "VKontakte", "WhatsApp", "WeChat"
    ]
)

purpose_of_use = st.selectbox(
    "Purpose of Use",
    ["Networking", "Education", "Entertainment", "News"]
)

avg_daily_usage_hours = st.number_input(
    "Average Daily Usage Hours",
    min_value=0.0,
    max_value=24.0,
    value=3.0
)

daily_unlocks = st.number_input(
    "Daily Unlocks",
    min_value=0,
    value=20
)

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

physical_activity_hours = st.number_input(
    "Physical Activity Hours",
    min_value=0.0,
    max_value=24.0,
    value=1.0
)

sleep_hours_per_night = st.number_input(
    "Sleep Hours Per Night",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

stress_level = st.selectbox(
    "Stress Level",
    ["Medium", "Low", "Very High", "High"]
)

# Prediction
if st.button("🔮 Predict Mental Health Score"):

    country_group = (
        country if country in top_countries else "Other"
    )

    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Country": country,
        "Academic_Level": academic_level,
        "Most_Used_Platform": most_used_platform,
        "Purpose_Of_Use": purpose_of_use,
        "Avg_Daily_Usage_Hours": avg_daily_usage_hours,
        "Daily_Unlocks": daily_unlocks,
        "Study_Hours": study_hours,
        "Physical_Activity_Hours": physical_activity_hours,
        "Sleep_Hours_Per_Night": sleep_hours_per_night,
        "Stress_Level": stress_level,
        "Grouped_country": country_group
    }])

    prediction = model.predict(input_data)[0]

    st.success(
        f"Predicted Mental Health Score: {prediction:.2f}"
    )

st.info(
    "This prediction is for educational/informational purposes "
    "and is not a clinical assessment."
)
