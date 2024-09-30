import streamlit as st

# Function to display the logo and header
def display_header():
    st.image("logo.png", width=100)  # Replace with the path to your logo
    st.title("Soft Skill Enhancement AI Application")

# Function to display footer
def display_footer():
    st.markdown("""
        <style>
        footer {
            visibility: hidden;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
        }
        </style>
        <div class="footer">
            <p>Soft Skill Enhancement AI App © 2024 - Built by Karthikeyan</p>
        </div>
        """, unsafe_allow_html=True)
