import streamlit as st
from src.components.home_header import home_header
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    style_base_layout()
    style_background_home()
    home_header()
    
    
    col1, col2 = st.columns(2,gap="large")

    with col1:
        st.header("I'm Student")
        st.image("https://i.ibb.co/nqSQ4pvF/Cheerful-Student-with-Book-and-Backpack.png", width=150)
        if st.button("Student Portal ",type='primary', icon=":material/arrow_outward:", icon_position="right"):
            st.session_state["login_type"] = "student"  # fixed key
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        st.image("https://i.ibb.co/jPdTPPFf/Friendly-Science-Professor-Illustration.png", width=150)
        if st.button("Teacher Portal ", type='primary', icon=":material/arrow_outward:", icon_position="right"):
            st.session_state["login_type"] = "teacher"  # fixed key
            st.rerun()
    footer_home()