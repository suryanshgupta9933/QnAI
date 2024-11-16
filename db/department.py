# Importing Dependencies
import logging
from datetime import datetime
from firebase_admin import firestore

from connection import db

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_department(org_id, dept_id, name, description):
    """
    Create a department in the database.
    """
    try:
        dept_ref = db.collection("organizations").document(org_id).collection("departments").document(dept_id)
        dept_ref.set({
            "name": name,
            "description": description,
            "created_at": datetime.now()
        })
        logger.info(f"Department {dept_id} created successfully under Organization {org_id}.")
    except Exception as e:
        logger.error(f"Failed to create department {dept_id} under Organization {org_id}: {e}")

def get_department(org_id, dept_id):
    """
    Get a department from the database.
    """
    try:
        dept_ref = db.collection("organizations").document(org_id).collection("departments").document(dept_id)
        dept = dept_ref.get()
        if dept.exists:
            logger.info(f"Department {dept_id} retrieved successfully under Organization {org_id}.")
            return dept.to_dict()
        else:
            logger.error(f"Department {dept_id} not found under Organization {org_id}.")
            return None
    except Exception as e:
        logger.error(f"Failed to get department {dept_id} under Organization {org_id}: {e}")
        return None