import streamlit as st
import json 
import os


# Always load file relative to this script's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "translations.json")

with open(file_path, "r", encoding="utf-8") as f:
    translations = json.load(f)

lang = st.sidebar.selectbox("Language", options=['en', 'ta'], format_func=lambda x: {'ta': 'தமிழ்', 'en': 'English'}[x])
t = translations[lang]

# Set page configuration
st.set_page_config(page_title="Water Quality Awareness", layout="centered")

# Title and Introduction
st.title(t.get("awareness_title"))

st.markdown(t.get("awareness_intro"))

# Section: Importance of Clean Water
st.header(t.get("why_clean_header"))
st.markdown(t.get("why_clean_content"))

# Section: Global Crisis

st.image("1.png")

st.header(t.get("global_crisis_header"))
st.markdown(t.get("global_crisis_content"))

# Section: Water Quality Analysis
st.header(t.get("analysis_header"))
st.markdown(t.get("analysis_content"))

# Section: Awareness and Education

st.image("3.png")

st.header(t.get("awareness_header"))
st.markdown(t.get("awareness_content"))



# Section: Environmental Impact
st.header(t.get("environmental_header"))
st.markdown(t.get("environmental_content"))

# Section: Policy and Legal Frameworks

st.image("2.png")

st.header(t.get("policy_header"))
st.markdown(t.get("policy_content"))

# Section: Conclusion
st.header(t.get("conclusion_header"))
st.markdown(t.get("conclusion_content"))