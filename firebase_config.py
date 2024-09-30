import firebase_admin
from firebase_admin import credentials, auth, firestore
import os
import json

# Check if the app has already been initialized to avoid re-initialization
if not firebase_admin._apps:
    # Load Firebase credentials from environment variable
    firebase_credentials = os.getenv("FIREBASE_SERVICE_ACCOUNT")
    
    if firebase_credentials:
        # Parse the JSON string stored in the environment variable
        service_account_info = json.loads(firebase_credentials)
        cred = credentials.Certificate(service_account_info)
        firebase_admin.initialize_app(cred)
    else:
        raise ValueError("Firebase credentials are not set in environment variables.")

# Firestore client
db = firestore.client()

# Function to create a new user in Firebase Authentication
def create_user(email, password):
    user = auth.create_user(email=email, password=password)
    return user.uid

# Function to save user details in Firestore
def save_user_details(uid, name, email):
    user_data = {"name": name, "email": email}
    db.collection("users").document(uid).set(user_data)

# Function to log in an existing user
def login_user(email, password):
    user = auth.get_user_by_email(email)
    return user.uid
