# Importing Dependencies
import logging
from datetime import datetime
from firebase_admin import firestore

from connection import db
from utils.ranking import rank_answers

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_answer(org_id, user_id, question_id, answer_id, content):
    """
    Create a answer to a question by a user within a department.
    """
    try:
        answer_ref = db.collection("organizations").document(org_id).collection("users").document(user_id).collection("questions").document(question_id).collection("answers").document(answer_id)
        answer_ref.set({
            "content": content,
            "created_at": datetime.now(),
            "upvotes": 0,
            "downvotes": 0,
            "author_upvote": False,
            "is_official_answer": False,
            "flagged": False
        })
        logger.info(f"answer {answer_id} created successfully by User {user_id} for question {question_id}.")

        # AI Moderation and Analysis here

    except Exception as e:
        print(e)
        logger.error(f"Failed to answer question due to Internal Server Error")

def get_answers(org_id, user_id, question_id):
    """
    Retrieve all answers to a question by a user.
    """
    try:
        answers_ref = db.collection("organizations").document(org_id).collection("users").document(user_id).collection("questions").document(question_id).collection("answers")
        answers = answers_ref.stream()
        answer_list = []
        for answer in answers:
            answer_list.append(answer.to_dict())
        logger.info(f"answers for question {question_id} retrieved successfully.")
        ranked_answers = rank_answers(answer_list)
        return ranked_answers
    except Exception as e:
        print(e)
        logger.error(f"Failed to retrieve answers due to Internal Server Error")
        return None

def update_answer_votes(org_id, user_id, question_id, answer_id, upvotes=0, downvotes=0):
    """
    Update the upvotes or downvotes for an answer.
    """
    try:
        answer_ref = db.collection("organizations").document(org_id).collection("users").document(user_id).collection("questions").document(question_id).collection("answers").document(answer_id)
        answer_ref.update({
            "upvotes": firestore.Increment(upvotes),
            "downvotes": firestore.Increment(downvotes)
        })
    except Exception as e:
        print(e)
        logger.error(f"Failed to update answer votes due to Internal Server Error")