# Importing Dependencies
import os
import json
import logging
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Path to service account key
SERVICE_ACCOUNT_KEY = os.getenv("serviceAccountKey")
ENV = os.getenv("env")
if not ENV or ENV == "prod":
    with open(SERVICE_ACCOUNT_KEY, "r") as f:
        SERVICE_ACCOUNT_KEY = f.read()
    SERVICE_ACCOUNT_KEY = json.loads(SERVICE_ACCOUNT_KEY)

# Initialize Firebase app
def initialize_firebase():
    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate(SERVICE_ACCOUNT_KEY)
            firebase_admin.initialize_app(cred)
        db = firestore.client()
        return db
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        return None