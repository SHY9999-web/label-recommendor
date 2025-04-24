
import streamlit as st

# Set page config
st.set_page_config(page_title="AI Label Recommender", layout="centered")

st.title("🎧 AI Label Recommender")
st.markdown("Helping you find the right labels for your sound.")

# User Input
track_description = st.text_area("🎵 Describe Your Track", 
                                 placeholder="Think vibe, BPM, maybe DJs you see playing it...")

subgenres = ["Indie Dance", "Melodic House", "Afro House", 
             "Deep House", "Nu Disco/Disco", "Tech House"]
selected_genres = st.multiselect("🎛️ Choose a Subgenre", options=subgenres)

if st.button("Submit"):
    if not track_description and not selected_genres:
        st.warning("Please describe your track or choose a subgenre.")
    else:
        # Simulated output (placeholder for GPT-4 response)
        st.markdown("## 📌 Recommended Labels:")
        
        label_1 = {
            "name": "Correspondent",
            "genre": "Indie Dance",
            "owner": "Jennifer Cardini",
            "desc": "Moody, dark, groovy.",
            "link": "https://correspondant.net/"
        }

        label_2 = {
            "name": "ANIMS",
            "genre": "Melodic House",
            "owner": "Pole Position",
            "desc": "Emotive melodic sounds for smaller audiences.",
            "link": "https://www.instagram.com/anims_music/"
        }

        for label in [label_1, label_2]:
            st.markdown(f"**{label['name']}** – {label['genre']} / {label['owner']}")
            st.markdown(f"_{label['desc']}_")
            st.markdown(f"[Visit Site]({label['link']})  
`Suggested Pitch:` _Hi {label['name']}, I’d love to share a track I think fits your catalogue..._")
