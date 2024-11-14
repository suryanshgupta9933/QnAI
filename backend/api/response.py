# Importing Dependencies
import uuid
import logging
from fastapi import APIRouter, HTTPException, status

from db.response import create_response, get_responses

# Configure Logging
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create Response
@router.post("/response/create", status_code=status.HTTP_201_CREATED)
def create_response_endpoint(org_id: str, dept_id: str, user_id: str, post_id: str, content: str):
    """
    Create a response to a post by a user within a department.
    """
    try:
        response_id = str(uuid.uuid4())
        create_response(org_id, dept_id, user_id, post_id, response_id, content)
        return {
            "response_id": response_id,
            "content": content
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to create response due to Internal Server Error.")
    
# Get Responses
@router.get("/responses", status_code=status.HTTP_200_OK)
def get_responses_endpoint(org_id: str, dept_id: str, user_id: str, post_id: str):
    """
    Retrieve all responses to a post by a user.
    """
    try:
        responses = get_responses(org_id, dept_id, user_id, post_id)
        if responses:
            return responses
        else:
            raise HTTPException(status_code=404, detail=f"Responses not found.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to get responses due to Internal Server Error.")