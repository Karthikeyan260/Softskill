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
    """Create a new user in Firebase Authentication."""
    user = auth.create_user(email=email, password=password)
    return user.uid

# Function to save user details in Firestore
def save_user_details(uid, name, email):
    """Save user details in Firestore."""
    user_data = {"name": name, "email": email}
    db.collection("users").document(uid).set(user_data)

# Function to log in an existing user
def login_user(email, password):
    """Log in an existing user."""
    try:
        user = auth.get_user_by_email(email)
        return user.uid
    except Exception as e:
        raise ValueError(f"Login failed: {e}")

# Example usage
if __name__ == "__main__":
    # Example: Create a new user
    try:
        user_uid = create_user("example@example.com", "securePassword")
        print(f"User created with UID: {user_uid}")

        # Save user details
        save_user_details(user_uid, "John Doe", "example@example.com")
        print("User details saved to Firestore.")

        # Log in the user
        logged_in_uid = login_user("example@example.com", "securePassword")
        print(f"User logged in with UID: {logged_in_uid}")

    except ValueError as e:
        print(e)
