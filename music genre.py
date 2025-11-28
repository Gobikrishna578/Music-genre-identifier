music_genre_webapp/
│├── app.py
│├── templates/
│ └── index.html
└── static/
├── css/
│ └── style.css
└── js/
└── main.js
import streamlit as st
import pandas as pd
import numpy as np
import time
import random
# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(
page_title=" Smart Music Genre Classifier",
page_icon=" ",
layout="wide"
)
# HEADER SECTION
# ------------------------------
st.title(" Smart Music Genre Classifier Dashboard")
st.markdown("##### Predict music genres dynamically and visualize real-time data updates.")
st.divider()
# MAIN CONTAINER
# ------------------------------
col1, col2 = st.columns([1, 2], gap="large")
with col1:
st.subheader(" Input Features")
tempo = st.selectbox("Tempo", ["slow", "medium", "fast"])
instrument = st.selectbox("Instrument", ["guitar", "piano", "drums", "synth"])
mood = st.selectbox("Mood", ["happy", "sad", "energetic", "relaxing"])
if st.button(" Classify Genre"):
features = {"tempo": tempo, "instrument": instrument, "mood": mood}
genre, scores = None, None
# CLASSIFY FUNCTION
def classify_genre(features):
scores = {"Pop":0, "Rock":0, "Jazz":0, "Classical":0, "Hip-Hop":0}
if features["tempo"] == "fast":
scores["Rock"] += 2; scores["Hip-Hop"] += 2; scores["Pop"] += 1
elif features["tempo"] == "medium":
scores["Pop"] += 2; scores["Jazz"] += 1
elif features["tempo"] == "slow":
scores["Classical"] += 2; scores["Jazz"] += 1
if features["instrument"] == "guitar":
scores["Rock"] += 2; scores["Jazz"] += 1
elif features["instrument"] == "piano":
scores["Classical"] += 2; scores["Pop"] += 1
elif features["instrument"] == "drums":
scores["Hip-Hop"] += 2; scores["Rock"] += 1
elif features["instrument"] == "synth":
scores["Pop"] += 2
if features["mood"] == "happy":
scores["Pop"] += 2; scores["Jazz"] += 1
elif features["mood"] == "sad":
scores["Classical"] += 2
elif features["mood"] == "energetic":
scores["Rock"] += 2; scores["Hip-Hop"] += 2
elif features["mood"] == "relaxing":
scores["Jazz"] += 2; scores["Classical"] += 1
genre = max(scores, key=scores.get)
return genre, scores
genre, scores = classify_genre(features)
st.success(f" Predicted Genre: **{genre}**")
st.write("### Genre Scores")
st.bar_chart(pd.Series(scores))
st.toast("Classification completed successfully!", icon=" ")
with col2:
st.subheader(" Live Data & Dashboard")
# Simulated live API data
placeholder = st.empty()
chart_data = pd.DataFrame(columns=["Pop", "Rock", "Jazz", "Classical", "Hip-Hop"])
for i in range(15): # Simulate 15 live updates
new_row = pd.DataFrame({
"Pop": [random.randint(0, 100)],
"Rock": [random.randint(0, 100)],
"Jazz": [random.randint(0, 100)],
"Classical": [random.randint(0, 100)],
"Hip-Hop": [random.randint(0, 100)]
})
chart_data = pd.concat([chart_data, new_row], ignore_index=True)
placeholder.line_chart(chart_data)
time.sleep(0.2)
st.divider()
# ------------------------------
# CHAT SECTION
# ------------------------------
st.subheader(" Chat with Assistant")
user_message = st.text_input("Ask something about music genres:")
if user_message:
responses = {
"pop": "Pop is upbeat and catchy, often focusing on vocals.",
"rock": "Rock is energetic with strong beats and electric guitar.",
"jazz": "Jazz features improvisation and complex chords.",
"classical": "Classical is calm, instrumental, and structured.",
"hip-hop": "Hip-Hop emphasizes rhythm, beats, and rap lyrics."
}
reply = "Hmm, interesting! Tell me more."
for key, val in responses.items():
if key in user_message.lower():
reply = val
st.info(f" {reply}")