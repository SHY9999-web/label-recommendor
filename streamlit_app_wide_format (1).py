
import streamlit as st
import pandas as pd

# Load database (wide format)
labels_db = pd.read_csv('all-results.csv')

# Inject custom font and styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

html, body, [class*="css"]  {
    font-family: 'Share Tech Mono', monospace;
    background-color: #0e0e0e;
    color: #f2f2f2;
}

label, .stTextInput > div > div {
    font-size: 16px !important;
    color: #f2f2f2 !important;
}

.card {
    background-color: #1a1a1a;
    border: 1px solid #333;
    padding: 16px;
    border-radius: 12px;
    margin-bottom: 16px;
    transition: all 0.3s ease-in-out;
}
.card:hover {
    background-color: #2c2c2c;
    transform: scale(1.02);
    box-shadow: 0px 0px 12px rgba(255,255,255,0.05);
}

.subgenre {
    color: #aaa;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# Page config
st.set_page_config(page_title="Label Recommender", layout="centered")

# Header
st.markdown("""<h1 style='text-align: center;'>🔍 Underground Label Finder</h1>""", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Describe your track, select a subgenre, and search through real underground labels.</p>", unsafe_allow_html=True)

# Track description input
track_description = st.text_area("🎵 Describe your track (vibe, BPM, DJs, etc.):", placeholder="Example: 124bpm, deep indie vibe, Gerd Janson type groove")

# Subgenre dropdown
subgenre = st.selectbox("🎛️ Choose a subgenre:", options=labels_db.columns)

# Search bar for label filter
search_text = st.text_input("🔍 Optional: Filter labels by name")

# Submit button
submit_button = st.button("🚀 Find Labels")

if submit_button:
    if track_description.strip() == "":
        st.warning("Please describe your track first.")
    else:
        with st.spinner("Finding underground labels..."):
            st.subheader("📌 Recommended Labels:")
            label_series = labels_db[subgenre].dropna()
            filtered_labels = label_series[label_series.str.contains(search_text, case=False, na=False)] if search_text else label_series

            if filtered_labels.empty:
                st.info("No labels matched your search.")
            else:
                for label in filtered_labels:
                    st.markdown(f"""
                    <div class='card'>
                        <h3>{label.strip()}</h3>
                        <p class='subgenre'>Subgenre: {subgenre}</p>
                    </div>
                    """, unsafe_allow_html=True)

# Footer
st.markdown("""---<p style='text-align: center; font-size: 12px;'>Built for the underground. 🖤</p>""", unsafe_allow_html=True)
