import firebase_admin
from firebase_admin import credentials, auth, firestore

# Initialize Firebase App
if not firebase_admin._apps:  # Check if the app has already been initialized
    cred = credentials.Certificate("softskill-enhancement-firebase-adminsdk-co8f1-666775ebfe.json")  # Replace with the path to your Firebase credentials JSON
    firebase_admin.initialize_app(cred)

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
