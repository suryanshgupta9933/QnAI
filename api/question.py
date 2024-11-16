# Importing Dependencies
import uuid
import logging
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status

from db.question import create_question, get_question, update_question_votes

# Configure Logging
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create Question Model
class CreateQuestion(BaseModel):
    org_id: str
    user_id: str
    title: str
    content: str
    tags: list

# Update Question Votes Model
class UpdateQuestionVotes(BaseModel):
    org_id: str
    user_id: str
    question_id: str
    upvotes: int = 0
    downvotes: int = 0

# Create Question
@router.post("/question/create", status_code=status.HTTP_201_CREATED)
def create_question_endpoint(question: CreateQuestion):
    try:
        question_id = str(uuid.uuid4())
        create_question(question.org_id, question.user_id, question_id, question.title, question.content, question.tags)
        return {
            "org_id": question.org_id,
            "user_id": question.user_id,
            "question_id": question_id
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to create question due to Internal Server Error.")

# Get question
@router.get("/question", status_code=status.HTTP_200_OK)
def get_question_endpoint(org_id: str, user_id: str, question_id: str):
    try:
        question = get_question(org_id, user_id, question_id)
        if question:
            return question
        else:
            raise HTTPException(status_code=404, detail=f"question not found.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to get question due to Internal Server Error.")

@router.put("/question/update_vote", status_code=status.HTTP_200_OK)
def update_question_votes_endpoint(update: UpdateQuestionVotes):
    try:
        update_question_votes(update.org_id, update.user_id, update.question_id, update.upvotes, update.downvotes)
        return {
            "question_id": update.question_id,
            "upvotes_increment": update.upvotes,
            "downvotes_increment": update.downvotes
        }
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to update question votes due to Internal Server Error.")
