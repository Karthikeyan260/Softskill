import streamlit as st
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

# Set page config
st.set_page_config(page_title="Soft Skills Chatbot", layout="wide", initial_sidebar_state="expanded")

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
