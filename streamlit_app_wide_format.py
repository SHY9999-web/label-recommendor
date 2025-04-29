
import streamlit as st
import pandas as pd

# Load the wide-format database
labels_db = pd.read_csv('all-results.csv')

# Page config
st.set_page_config(page_title="Underground Label Finder", layout="centered")

# Title Section
st.markdown("""
<h1 style='text-align: center; font-family: Courier New, monospace;'>🔍 Find Your Perfect Label</h1>
<p style='text-align: center;'>Welcome to the Underground Label Finder. Describe your track, choose a subgenre, and find the best labels to send your demo to!</p>
""", unsafe_allow_html=True)

# Track description input
track_description = st.text_area(
    "🎵 Describe your track (vibe, BPM, DJs, etc.):",
    placeholder="Example: Punchy indie vibe, rolling bassline, 124bpm, sounds like Gerd Janson"
)

# Subgenre dropdown
subgenre = st.selectbox("🎛️ Choose a subgenre:", options=labels_db.columns)

# Submit button
submit_button = st.button("🚀 Find Labels")

if submit_button:
    if track_description.strip() == "":
        st.warning("Please describe your track to get personalized label recommendations.")
    else:
        st.subheader("📌 Recommended Labels:")

        # Fetch non-empty labels under selected subgenre
        recommended_labels = labels_db[subgenre].dropna()

        for label in recommended_labels:
            st.markdown(f"""
            <div style="padding:10px; border: 1px solid #666; border-radius:10px; margin-bottom:10px; background-color:#f5f5f5;">
            <h3 style="font-family: Courier New, monospace;">{label.strip()}</h3>
            <ul>
                <li><strong>Subgenre:</strong> {subgenre}</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

# Footer (Optional)
st.markdown("""
---
<p style='text-align: center; font-size: 12px;'>Built for the underground. 🖤</p>
""", unsafe_allow_html=True)
