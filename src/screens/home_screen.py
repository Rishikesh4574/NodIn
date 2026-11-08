import streamlit as st
from src.components.home_header import home_header
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    style_base_layout()
    style_background_home()
    home_header()
    
    
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Teacher Portal"):
            st.session_state["login_type"] = "teacher"  # fixed key
            st.rerun()

    with col2:
        if st.button("Student Portal"):
            st.session_state["login_type"] = "student"  # fixed key
            st.rerun()