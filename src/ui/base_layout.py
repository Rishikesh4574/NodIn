
import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background-color: #5865F2 !important;
            }

            /* Homepage column cards */
            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 1.5rem !important;
                border-radius: 3.5rem !important;
                transition: transform 0.25s ease-in-out,
                            box-shadow 0.25s ease-in-out !important;
            }

            /* Card hover effect */
            .stApp div[data-testid="stColumn"]:hover {
                transform: translateY(-6px) !important;
                box-shadow: 0 16px 40px rgba(0, 0, 0, 0.2) !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background-color: #E0E3FF !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Streamlit toolbar */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        /* Main layout */
        .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
        }

        /* Main heading */
        h1 {
            font-family: "Climate Crisis", sans-serif !important;
            font-size: 2.8rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: #FFFFFF !important;
        }

        /* Secondary heading */
        h2 {
            font-family: "Climate Crisis", sans-serif !important;
            font-size: 2rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: #4F46E5 !important;
        }

        /* Other text */
        h3, h4, p {
            font-family: "Outfit", sans-serif !important;
        }

        /* Common button styling */
        .stButton > button {
            border-radius: 1.5rem !important;
            background: #E91E8F !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            font-family: "Outfit", sans-serif !important;
            transition: all 0.25s ease-in-out !important;
        }

        /* Secondary buttons */
        .stButton > button[kind="secondary"] {
            background: #EB459E !important;
            color: white !important;
        }

        /* Tertiary buttons */
        .stButton > button[kind="tertiary"] {
            background: black !important;
            color: white !important;
        }

        /* Button hover effect */
        .stButton > button:hover {
            transform: translateY(-4px) !important;
            filter: brightness(1.15) !important;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25) !important;
            cursor: pointer !important;
        }

        /* Button click effect */
        .stButton > button:active {
            transform: scale(0.97) !important;
        }

        </style>
    """, unsafe_allow_html=True)
