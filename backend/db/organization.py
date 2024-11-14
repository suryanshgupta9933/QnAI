# Import Dependencies
import logging
from datetime import datetime
from firebase_admin import credentials, firestore

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load Firebase Credentials
cred = credentials.Certificate("serviceAccountKey.json")
firebase = firestore.client()
db = firebase.client()

def create_org(org_id, name, description):
    """
    Create an organization in the database.
    """
    org_ref = db.collection("organizations").document(org_id)
    org_ref.set({
        "name": name,
        "description": description,
        "created_at": datetime.now()
    })
    logger.info(f"Organization {org_id} created successfully.")

def get_org(org_id):
    """
    Get an organization from the database.
    """
    org_ref = db.collection("organizations").document(org_id)
    org = org_ref.get()
    if org.exists:
        logger.info(f"Organization {org_id} retrieved successfully.")
        return org.to_dict()
    else:
        logger.error(f"Organization {org_id} not found.")
        return None