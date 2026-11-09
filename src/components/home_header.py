
import streamlit as st

def home_header():

    logo_url = "https://i.ibb.co/d4xnbMQT/Premium-Lavender-Graduation-Logo.png"

    st.markdown(f"""
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-bottom: 15px;
            margin-top: 5px;
        ">
            <img
                src="{logo_url}"
                style="
                    height: 70px;
                    width: 100px;
                    object-fit: contain;
                "
            />
            <h1 style="
                text-align: center;
                color: #E0E3FF;
                margin-top: 5px;
            ">
                NODIN<br>CLASS
            </h1>
        </div>
    """, unsafe_allow_html=True)
