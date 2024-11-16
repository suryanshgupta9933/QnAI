# Importing Dependencies
import uuid
import logging
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status

from db.answer import create_answer, get_answers

# Configure Logging
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create Answer Model
class CreateAnswer(BaseModel):
    org_id: str
    user_id: str
    question_id: str
    content: str

# Get Answer Model
class GetAnswer(BaseModel):
    org_id: str
    user_id: str
    question_id: str

# Update Answer Votes Model
class UpdateAnswerVotes(BaseModel):
    org_id: str
    user_id: str
    question_id: str
    upvotes: int = 0
    downvotes: int = 0

# Create answer
@router.post("/answer/create", status_code=status.HTTP_201_CREATED)
def create_answer_endpoint(answer: CreateAnswer):
    """
    Create a answer to a question by a user within a department.
    """
    try:
        answer_id = str(uuid.uuid4())
        create_answer(answer.org_id, answer.user_id, answer.question_id, answer_id, answer.content)
        return {
            "org_id": answer.org_id,
            "user_id": answer.user_id,
            "question_id": answer.question_id,
            "answer_id": answer_id
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to create answer due to Internal Server Error.")

# Get answers
@router.get("/answers", status_code=status.HTTP_200_OK)
def get_answers_endpoint(answer: GetAnswer):
    """
    Retrieve all answers to a question by a user.
    """
    try:
        answers = get_answers(answer.org_id, answer.user_id, answer.question_id)
        if answers:
            return answers
        else:
            raise HTTPException(status_code=404, detail=f"Answers not found.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to get answers due to Internal Server Error.")

@router.put("/answer/update_vote", status_code=status.HTTP_200_OK)
def update_answer_votes_endpoint(update: UpdateAnswerVotes):
    try:
        update_answer_votes(update.org_id, update.user_id, update.question_id, update.upvotes, update.downvotes)
        return {
            "question_id": update.question_id,
            "upvotes": update.upvotes,
            "downvotes": update.downvotes
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to update answer votes due to Internal Server Error.")