# Importing Dependencies
import logging
from datetime import datetime
from firebase_admin import firestore

from connection import db

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_response(org_id: str, dept_id: str, user_id: str, post_id: str, response_id: str, content: str):
    """
    Create a response to a post by a user within a department.
    """
    try:
        response_ref = db.collection("organizations").document(org_id).collection("departments").document(dept_id).collection("users").document(user_id).collection("posts").document(post_id).collection("responses").document(response_id)
        response_ref.set({
            "user_id": user_id,
            "content": content,
            "created_at": datetime.now(),
            "upvotes": 0,
            "downvotes": 0,
            "author_upvote": False,
            "is_official_answer": False,
            "flagged": False
        })
        logger.info(f"Response {response_id} created successfully by User {user_id} for Post {post_id}.")

        # AI Moderation and Analysis here

    except Exception as e:
        print(e)
        logger.error(f"Failed to answer post due to Internal Server Error")

def get_responses(org_id, dept_id, user_id, post_id):
    """
    Retrieve all responses to a post by a user.
    """
    try:
        responses_ref = db.collection("organizations").document(org_id).collection("departments").document(dept_id).collection("users").document(user_id).collection("posts").document(post_id).collection("responses")
        responses = responses_ref.stream()
        response_list = []
        for response in responses:
            response_list.append(response.to_dict())
        logger.info(f"Responses for Post {post_id} retrieved successfully.")
        return response_list
    except Exception as e:
        print(e)
        logger.error(f"Failed to retrieve responses due to Internal Server Error")
        return None