# Import Dependencies
import logging
from datetime import datetime
from firebase_admin import credentials, firestore

from connection import initialize_firebase

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Firebase
db = initialize_firebase()

def create_organization(org_id, name, description):
    """
    Create an organization in the database.
    """
    try:
        org_ref = db.collection("organizations").document(org_id)
        org_ref.set({
            "name": name,
            "description": description,
            "created_at": datetime.now()
        })
        logger.info(f"Organization {org_id} created successfully.")
    except Exception as e:
        logger.error(f"Failed to create organization {org_id}: {e}")

def get_organization(org_id):
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