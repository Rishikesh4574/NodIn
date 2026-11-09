import streamlit as st
import base64
from pathlib import Path

def footer_home():

    st.markdown(f"""
        <div style="margin-top: 2rem; display:flex; gap: 6px; justify-content:center; items-align:center">
            <p style="font-weight:bold; color:white; "> Created with ❤️ by Rishikesh Karale</p>
        </div>
    """, unsafe_allow_html=True)