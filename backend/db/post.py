# Importing Dependencies
import logging
from datetime import datetime
from firebase_admin import firestore

from connection import db

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_post(org_id: str, dept_id: str, user_id: str, post_id: str, title: str, content: str, tags: list, is_official_answer: bool = False):
    """
    Create a post by a user within a department.
    """
    try:
        post_ref = db.collection("organizations").document(org_id).collection("departments").document(dept_id).collection("users").document(user_id).collection("posts").document(post_id)
        post_ref.set({
            "title": title,
            "content": content,
            "tags": tags,
            "created_at": datetime.now(),
            "is_official_answer": is_official_answer,
            "upvotes": 0,
            "downvotes": 0,
            "flagged": False
        })
        logger.info(f"Post {post_id} created successfully by User {user_id}.")

        # AI Moderation and Analysis here
        
    except Exception as e:
        logger.error(f"Failed to create post {post_id} by User {user_id}: {e}")

def get_post(org_id, dept_id, user_id, post_id):
    """
    Retrieve a post by a user.
    """
    try:
        post_ref = db.collection("organizations").document(org_id).collection("departments").document(dept_id).collection("users").document(user_id).collection("posts").document(post_id)
        post = post_ref.get()
        if post.exists:
            logger.info(f"Post {post_id} retrieved successfully.")
            return post.to_dict()
        else:
            logger.error(f"Post {post_id} not found.")
            return None
    except Exception as e:
        logger.error(f"Failed to retrieve post {post_id}: {e}")
        return None

def update_post_votes(org_id, dept_id, user_id, post_id, upvotes=0, downvotes=0):
    """
    Update the upvotes or downvotes for a post.
    """
    try:
        post_ref = db.collection("organizations").document(org_id).collection("departments").document(dept_id).collection("users").document(user_id).collection("posts").document(post_id)
        post_ref.update({
            "upvotes": firestore.Increment(upvotes),
            "downvotes": firestore.Increment(downvotes)
        })
        logger.info(f"Post {post_id} votes updated successfully.")
    except Exception as e:
        logger.error(f"Failed to update votes for post {post_id}: {e}")