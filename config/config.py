import os
import streamlit as st

# Try Streamlit secrets first, fallback to env variable
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))