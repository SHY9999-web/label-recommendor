
import streamlit as st
import pandas as pd

# Sample label database
label_db = pd.DataFrame([
    {"Label": "Correspondent", "Genres": ["Indie Dance"], "BPM Range": (120, 125), "Owner": "Jennifer Cardini", "Beatport Link": "https://www.beatport.com/label/correspondant/16557"},
    {"Label": "ANIMS", "Genres": ["Melodic House"], "BPM Range": (120, 124), "Owner": "Pole Position", "Beatport Link": "https://www.beatport.com/label/anims/98765"},
    {"Label": "Frank Music", "Genres": ["Indie Dance"], "BPM Range": (116, 122), "Owner": "Johannes Albert", "Beatport Link": "https://www.beatport.com/label/frank-music/12360"},
    {"Label": "Siamese", "Genres": ["Melodic House"], "BPM Range": (120, 126), "Owner": "Adriatique", "Beatport Link": "https://www.beatport.com/label/siamese/67330"},
])

# Sample artist-label association table
artist_label_df = pd.DataFrame([
    {"Artist": "Gerd Janson", "Label": "Running Back"},
    {"Artist": "Gerd Janson", "Label": "Permanent Vacation"},
    {"Artist": "Jennifer Cardini", "Label": "Correspondent"},
    {"Artist": "Jennifer Cardini", "Label": "Kompakt"},
    {"Artist": "Biesmans", "Label": "Watergate Records"},
    {"Artist": "Musumeci", "Label": "Multinotes"},
    {"Artist": "Musumeci", "Label": "Correspondent"},
    {"Artist": "Johannes Albert", "Label": "Frank Music"},
])

# Styling
st.set_page_config(page_title="AI Label Recommender", layout="centered")

st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Courier New', monospace;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎧 AI Label Recommender (Fallback Mode)")
st.markdown("Helping you find the right underground labels for your sound.")

# Inputs
st.header("🎶 Track Information")
track_description = st.text_area("Describe your track", placeholder="Think vibe, BPM, DJs you see playing it...")

st.header("🎛️ Genre Selection")
subgenres = ["Indie Dance", "Melodic House", "Afro House", "Deep House", "Nu Disco/Disco", "Tech House"]
selected_genres = st.multiselect("Choose your subgenre(s)", options=subgenres)

if st.button("Submit"):
    if not track_description and not selected_genres:
        st.warning("Please describe your track or select a subgenre.")
    else:
        with st.spinner("Finding your labels..."):
            user_bpm_guess = None
            # Basic BPM extraction (if user writes "124 BPM")
            for token in track_description.split():
                if token.isdigit() and 90 <= int(token) <= 140:
                    user_bpm_guess = int(token)

            # Match artist mentions
            mentioned_artists = [
                artist for artist in artist_label_df["Artist"].unique()
                if artist.lower() in track_description.lower()
            ]

            boosted_labels = artist_label_df[artist_label_df["Artist"].isin(mentioned_artists)]["Label"].tolist()

            # Scoring function
            def score_label(row):
                score = 0
                # Genre match
                if any(genre in row["Genres"] for genre in selected_genres):
                    score += 3
                # DJ owner or release match
                if row["Label"] in boosted_labels:
                    score += 3
                # BPM match (light bonus)
                if user_bpm_guess:
                    bpm_low, bpm_high = row["BPM Range"]
                    if bpm_low <= user_bpm_guess <= bpm_high:
                        score += 1
                return score

            label_db["Score"] = label_db.apply(score_label, axis=1)
            top_labels = label_db.sort_values(by="Score", ascending=False)

            st.divider()
            st.header("🎯 Recommended Labels")

            for _, row in top_labels.iterrows():
                if row["Score"] > 0:
                    st.markdown(f"**Label Name**: {row['Label']}")
                    st.markdown(f"**Owner**: {row['Owner'] if pd.notnull(row['Owner']) else 'Unknown'}")
                    st.markdown(f"**Beatport Link**: [Visit]({row['Beatport Link']})")
                    st.markdown("---")
