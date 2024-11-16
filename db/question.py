# Importing Dependencies
import logging
from datetime import datetime
from firebase_admin import firestore

from connection import db

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_question(org_id, user_id, question_id, title, content, tags):
    """
    Create a question by a user within organization.
    """
    try:
        question_ref = db.collection("organizations").document(org_id).collection("users").document(user_id).collection("questions").document(question_id)
        question_ref.set({
            "title": title,
            "content": content,
            "tags": tags,
            "created_at": datetime.now(),
            "upvotes": 0,
            "downvotes": 0,
            "flagged": False
        })
        logger.info(f"Question {question_id} created successfully by User {user_id}.")

        # AI Moderation and Analysis here
        
    except Exception as e:
        logger.error(f"Failed to create question {question_id} by User {user_id}: {e}")

def get_question(org_id, user_id, question_id):
    """
    Retrieve a question by a user.
    """
    try:
        question_ref = db.collection("organizations").document(org_id).collection("users").document(user_id).collection("questions").document(question_id)
        question = question_ref.get()
        if question.exists:
            logger.info(f"question {question_id} retrieved successfully.")
            return question.to_dict()
        else:
            logger.error(f"question {question_id} not found.")
            return None
    except Exception as e:
        logger.error(f"Failed to retrieve question {question_id}: {e}")
        return None

def update_question_votes(org_id, user_id, question_id, upvotes=0, downvotes=0):
    """
    Update the upvotes or downvotes for a question.
    """
    try:
        question_ref = db.collection("organizations").document(org_id).collection("users").document(user_id).collection("questions").document(question_id)
        question_ref.update({
            "upvotes": firestore.Increment(upvotes),
            "downvotes": firestore.Increment(downvotes)
        })
        logger.info(f"Question {question_id} votes updated successfully.")
    except Exception as e:
        logger.error(f"Failed to update votes for question {question_id}: {e}")