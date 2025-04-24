
import streamlit as st
import openai
import os

# Use Streamlit secrets or environment variable for OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

# Page config and basic styling
st.set_page_config(page_title="AI Label Recommender", layout="centered")

st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Courier New', monospace;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎧 AI Label Recommender")
st.markdown("Helping you find the right underground labels for your sound.")

# Inputs
track_description = st.text_area("🎵 Describe Your Track", 
    placeholder="Think vibe, BPM, maybe DJs you see playing it...")

subgenres = ["Indie Dance", "Melodic House", "Afro House", "Deep House", "Nu Disco/Disco", "Tech House"]
selected_genres = st.multiselect("🎛️ Choose a Subgenre", options=subgenres)

# On submit
if st.button("Submit"):
    if not track_description and not selected_genres:
        st.warning("Please describe your track or choose a subgenre.")
    else:
        with st.spinner("Generating label matches..."):
            prompt = f"""
You are an A&R assistant for underground electronic music.

Based on the following track description and selected subgenres, return 3 recommended record labels. 
Structure your response clearly with:

Label Name:  
Label Owner (if known):  
Contact Information (if known):  
Last Release on Label:  

Track Description: {track_description}  
Subgenres: {", ".join(selected_genres)}
"""

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=500
                )
                reply = response['choices'][0]['message']['content']
                st.markdown("## 📌 Recommended Labels:")
                st.markdown(reply)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
