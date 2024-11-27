# Importing Dependencies
import logging
from datetime import datetime
from firebase_admin import firestore

from connection import initialize_firebase

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Firebase
db = initialize_firebase()

def create_user(org_id, dept_id, user_id, name, email, role, profile_picture_url=None):
    """
    Create a user within a department.
    """
    try:
        user_ref = db.collection("organizations").document(org_id).collection("users").document(user_id)
        user_ref.set({
            "name": name,
            "email": email,
            "role": role,
            "department": dept_id,
            "profile_picture_url": profile_picture_url,
            "official": False,
            "created_at": datetime.now()
        })
        logger.info(f"User {user_id} created successfully in Organization {org_id}.")
    except Exception as e:
        logger.error(f"Failed to create user {user_id} in Organization {org_id}: {e}")

def get_user(org_id, dept_id, user_id):
    """
    Retrieve a user within a department.
    """
    try:
        user_ref = db.collection("organizations").document(org_id).collection("users").document(user_id)
        user = user_ref.get()
        if user.exists:
            logger.info(f"User {user_id} retrieved successfully.")
            return user.to_dict()
        else:
            logger.error(f"User {user_id} not found.")
            return None
    except Exception as e:
        logger.error(f"Failed to retrieve user {user_id}: {e}")
        return None