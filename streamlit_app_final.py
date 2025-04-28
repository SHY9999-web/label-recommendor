
import streamlit as st
import pandas as pd

# Load the database (point to your real CSV when ready)
labels_db = pd.read_csv('discogs_labels_house_full.csv')

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
subgenre = st.selectbox("🎛️ Choose a subgenre:", options=labels_db['Genre'].dropna().unique())

# Submit button
submit_button = st.button("🚀 Find Labels")

if submit_button:
    if track_description.strip() == "":
        st.warning("Please describe your track to get personalized label recommendations.")
    else:
        st.subheader("📌 Recommended Labels:")

        # Filter database by selected subgenre
        recommended_labels = labels_db[labels_db['Genre'] == subgenre]

        for idx, row in recommended_labels.iterrows():
            st.markdown(f"""
            <div style="padding:10px; border: 1px solid #666; border-radius:10px; margin-bottom:10px; background-color:#f5f5f5;">
            <h3 style="font-family: Courier New, monospace;">{row['Label Name']}</h3>
            <ul>
                <li><strong>Genre:</strong> {row['Genre']}</li>
                <li><strong>Country:</strong> {row['Country'] if pd.notnull(row['Country']) else 'Unknown'}</li>
                <li><strong>Profile:</strong> {row['Profile'] if pd.notnull(row['Profile']) else 'No profile available'}</li>
                <li><a href="{row['Discogs URL']}" target="_blank">🌐 Visit Discogs Page</a></li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

# Footer (Optional)
st.markdown("""
---
<p style='text-align: center; font-size: 12px;'>Built for the underground. 🖤</p>
""", unsafe_allow_html=True)
