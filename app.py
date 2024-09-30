import streamlit as st
from firebase_config import create_user, login_user, save_user_details
from header_footer import display_header, display_footer
from chatbot import chatbot_ui
from vocabulary import vocabulary_page
from speech import speech_page
from pronunciation import pronunciation_page
from tests import practice_tests_page
from reports import test_reports_page

# Main Application
def main():
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
    
    # Optionally clear the session state (or specific session variables)
    if 'authenticated' in st.session_state:
        del st.session_state['authenticated']
    
    # Set query params to trigger a rerun (this method will be deprecated after 2024)
    st.experimental_set_query_params()

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

if __name__ == "__main__":
    main()
