import streamlit as st
from firebase_config import create_user, login_user, save_user_details
from header_footer import display_header, display_footer
from vocabulary import vocabulary_page
from speech import speech_page
from pronunciation import pronunciation_page
from tests import practice_tests_page
from reports import test_reports_page

# Importing chatbot-related libraries
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Google Generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get the response from the Gemini model
def get_gemini_response(user_input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(user_input)
    return response.text

# Main Application
def main():
    # Set page config for the entire app (must be the first Streamlit command)
    st.set_page_config(page_title="Soft Skill Enhancement AI Platform", layout="wide", initial_sidebar_state="expanded")

    # Display the header
    display_header()

    # Sidebar for navigation
    menu = st.sidebar.selectbox("Menu", ["Home", "Sign Up", "Login", "Vocabulary Lessons", "Speech Lessons", "Pronunciation Lessons", "Practice Tests", "Test Reports", "AI Chatbot", "Logout"])

    if menu == "Home":
        st.write("Welcome to the Soft Skill Enhancement AI Platform.")
    elif menu == "Sign Up":
        signup_page()
    elif menu == "Login":
        login_page()
    elif menu == "Vocabulary Lessons":
        vocabulary_page()
    elif menu == "Speech Lessons":
        speech_page()
    elif menu == "Pronunciation Lessons":
        pronunciation_page()
    elif menu == "Practice Tests":
        practice_tests_page()
    elif menu == "Test Reports":
        test_reports_page()
    elif menu == "AI Chatbot":
        chatbot_ui()
    elif menu == "Logout":
        st.session_state['authenticated'] = False
    
    # Clear the session state for authentication
    if 'authenticated' in st.session_state:
        del st.session_state['authenticated']
    
    # Display the footer
    display_footer()

# Sign-Up Functionality
def signup_page():
    st.title("Sign Up")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        try:
            uid = create_user(email, password)
            save_user_details(uid, name, email)
            st.success("Account created successfully! Please log in.")
        except Exception as e:
            st.error(f"Error: {e}")

# Login Functionality
def login_page():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            uid = login_user(email, password)
            st.session_state['authenticated'] = True
            st.session_state['user'] = email
            st.success(f"Logged in as {email}")
        except Exception as e:
            st.error(f"Login failed: {e}")

# Chatbot Functionality
def chatbot_ui():
    # Custom CSS for styling
    st.markdown("""
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                background-color: #ffffff; /* Background color */
                color: #000000; /* Text color */
            }
            .main {
                padding: 2rem;
            }
            .stButton > button {
                background-color: #2bbbad; /* Button color */
                color: white;
                border: none;
                border-radius: 5px;
                padding: 0.5rem 1rem;
                transition: all 0.3s ease;
            }
            .stButton > button:hover {
                background-color: #388e3c; /* Button hover color */
                transform: translateY(-2px);
            }
            .response-box {
                background-color: #f3f8f2; /* Response box color */
                border: 1px solid #78c79e; /* Border color */
                border-radius: 5px;
                padding: 1rem;
                margin-top: 1rem;
            }
            .header {
                color: #1b5e20; /* Header color */
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 1rem;
            }
            .subheader {
                color: #1a8572; /* Subheader color */
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            .footer {
                text-align: center;
                margin-top: 2rem;
                color: #6c757d; /* Gray text for footer */
            }
        </style>
    """, unsafe_allow_html=True)

    # Page title and description
    st.markdown("<h1 class='header'>Soft Skills Chatbot</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>Ask about soft skills or any related queries!</p>", unsafe_allow_html=True)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask about soft skills or related topics:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_gemini_response(prompt)
                st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

    # Footer
    st.markdown("<p class='footer'>Developed by Karthik</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
