# Import required libraries
import streamlit as st          # For creating web app UI
import pandas as pd            # For handling CSV data
import firebase_admin          # Firebase SDK
from firebase_admin import credentials, firestore  # For authentication and database

# ------------------ Firebase Initialization ------------------

# Check if Firebase app is already initialized
# (Prevents error if code runs multiple times)
if not firebase_admin._apps:
    # Load Firebase credentials from JSON file
    cred = credentials.Certificate("firebase-key.json")
    
    # Initialize Firebase app
    firebase_admin.initialize_app(cred)

# Create Firestore database client
db = firestore.client()

# ------------------ Streamlit UI ------------------

# Set title of the web app
st.title("CSV Upload to Firebase 🚀")

# Create file uploader widget (only accepts CSV files)
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

# ------------------ File Processing ------------------

# Check if user has uploaded a file
if uploaded_file is not None:
    
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Display preview of uploaded data
    st.write("Preview of Data:")
    st.dataframe(df)

    # ------------------ Upload Button ------------------

    # Create a button to upload data to Firebase
    if st.button("Upload to Firebase"):
        
        # Loop through each row in the DataFrame
        for i, row in df.iterrows():
            
            # Convert row to dictionary format
            data = row.to_dict()
            
            # Add data to Firestore collection named "csv_data"
            db.collection("csv_data").add(data)
        
        # Show success message after upload
        st.success("Data uploaded successfully! 🎉")