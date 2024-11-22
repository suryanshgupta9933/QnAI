# Importing Dependencies
import logging
from datetime import datetime
from firebase_admin import firestore

from connection import initialize_firebase
from utils.ranking import rank_answers

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Firebase
db = initialize_firebase()

def create_answer(org_id, user_id, question_id, answer_id, content):
    """
    Create a answer to a question by a user within a department.
    """
    try:
        answer_ref = db.collection("organizations").document(org_id).collection("questions").document(question_id).collection("answers").document(answer_id)
        answer_ref.set({
            "content": content,
            "created_at": datetime.now(),
            "upvotes": 0,
            "downvotes": 0,
            "author_upvote": False,
            "is_official_answer": False,
            "flagged": False
        })
        logger.info(f"Answer {answer_id} created successfully by User {user_id} for question {question_id}.")

        # AI Moderation and Analysis here

        # Index the answer to Pinecone
        index_answer(org_id, user_id, question_id, answer_id, content)

    except Exception as e:
        logger.error(f"Failed to answer question due to Internal Server Error")

def get_answer(org_id, question_id, answer_id):
    """
    Retrieve a specific answer to a question by a user.
    """
    try:
        answer_ref = db.collection("organizations").document(org_id).collection("questions").document(question_id).collection("answers").document(answer_id)
        answer = answer_ref.get()
        if answer.exists:
            logger.info(f"Answer {answer_id} retrieved successfully.")
            return answer.to_dict()
        else:
            logger.error(f"Answer {answer_id} does not exist.")
            return None
    except Exception as e:
        logger.error(f"Failed to retrieve answer due to Internal Server Error")
        return None

def get_answers(org_id, question_id):
    """
    Retrieve all answers to a question by a user.
    """
    try:
        answers_ref = db.collection("organizations").document(org_id).collection("questions").document(question_id).collection("answers")
        answers = answers_ref.stream()
        answer_list = []
        for answer in answers:
            answer_list.append(answer.to_dict())
        logger.info(f"answers for question {question_id} retrieved successfully.")
        ranked_answers = rank_answers(answer_list)
        return ranked_answers
    except Exception as e:
        logger.error(f"Failed to retrieve answers due to Internal Server Error")
        return None

def update_answer_votes(org_id, question_id, answer_id, upvotes=0, downvotes=0):
    """
    Update the upvotes or downvotes for an answer.
    """
    try:
        answer_ref = db.collection("organizations").document(org_id).collection("questions").document(question_id).collection("answers").document(answer_id)
        answer_ref.update({
            "upvotes": firestore.Increment(upvotes),
            "downvotes": firestore.Increment(downvotes)
        })
    except Exception as e:
        logger.error(f"Failed to update answer votes due to Internal Server Error")