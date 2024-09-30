import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load the Google Gemini API Key from environment variables
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")  # Make sure to set the API key in your environment variables

# Function to get the response from the Gemini model
def get_gemini_response(user_input):
    if not GEMINI_API_KEY:
        raise ValueError("Google Gemini API key not found. Please set it in your environment variables.")
    
    url = "https://api.gemini.ai/v1/chatbot"  # Ensure this is the correct endpoint
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }

    # Create the payload for the request
    payload = {
        "query": user_input
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            return response_data['response']  # Adjust according to the API's response structure
        else:
            print("Error response:", response.json())  # Print error details for debugging
            return "Sorry, I couldn't analyze your input. Please try again."
    except Exception as e:
        print("Error during API request:", str(e))
        return "Sorry, I couldn't analyze your input. Please try again."

# Chatbot UI using Streamlit
def chatbot_ui():
    st.title("Soft Skill Development Chatbot")

    # Input from the user
    user_input = st.text_input("Ask me anything related to soft skills:")

    # Generate response when the user clicks "Send"
    if st.button("Send"):
        if user_input:
            response = get_gemini_response(user_input)
            st.write("Chatbot: ", response)

