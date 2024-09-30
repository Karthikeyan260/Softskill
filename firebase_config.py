import firebase_admin
from firebase_admin import credentials, auth, firestore
import os
import json

# Load Firebase credentials from environment variable
firebase_credentials = os.getenv("FIREBASE_SERVICE_ACCOUNT")

if firebase_credentials:
    try:
        # Parse the credentials JSON string into a dictionary
        service_account_info = json.loads(firebase_credentials)
        # Initialize Firebase with the parsed service account credentials
        cred = credentials.Certificate(service_account_info)
        
        if not firebase_admin._apps:  # Check if the app has already been initialized
            firebase_admin.initialize_app(cred)
            print("Firebase app initialized successfully.")
        
        # Firestore client
        db = firestore.client()
        
    except Exception as e:
        raise ValueError(f"Error initializing Firebase: {e}")
else:
    raise ValueError("Firebase credentials are not set in environment variables.")


# Function to create a new user in Firebase Authentication
def create_user(email, password):
    try:
        user = auth.create_user(email=email, password=password)
        return user.uid
    except Exception as e:
        raise ValueError(f"Error creating user: {e}")


# Function to save user details in Firestore
def save_user_details(uid, name, email):
    try:
        user_data = {"name": name, "email": email}
        db.collection("users").document(uid).set(user_data)
        print(f"User {name} saved to Firestore successfully.")
    except Exception as e:
        raise ValueError(f"Error saving user details: {e}")


# Function to log in an existing user
def login_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        # You might want to add more sophisticated authentication logic here (e.g., password validation)
        return user.uid
    except Exception as e:
        raise ValueError(f"Error logging in user: {e}")
