import os
import streamlit as st

def get_api_key():
    try:
        return st.secrets["GROQ_API_KEY"]
    except:
        return os.getenv("GROQ_API_KEY")

GROQ_API_KEY = get_api_key()