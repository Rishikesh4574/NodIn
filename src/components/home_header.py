import streamlit as st

def home_header():
    st.markdown("""
        <div style="
            padding: 20px 0 10px 0;
        ">
            <h1 style="
                font-family: 'Climate Crisis', sans-serif;
                font-size: 4rem;
                font-weight: 400;
                letter-spacing: 1px;
                color: #FFFFFF;
                margin: 0;
                line-height: 1.3;
                text-shadow: 0px 2px 8px rgba(0,0,0,0.12);
            ">
                NODIN
            </h1>
        </div>
    """, unsafe_allow_html=True)