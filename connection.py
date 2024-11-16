# Importing Dependencies
import os
import logging
import firebase_admin
from firebase_admin import credentials, firestore

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Path to service account key
SERVICE_ACCOUNT_KEY = os.getenv("serviceAccountKey", "serviceAccountKey.json")

# Initialize Firebase app
try:
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_KEY)
        firebase_admin.initialize_app(cred)
    db = firestore.client()
except Exception as e:
    print(f"Error initializing Firebase: {e}")