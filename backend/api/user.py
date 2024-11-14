# Importing Dependencies
import uuid
import logging
from fastapi import APIRouter, HTTPException, status

from db.user import create_user, get_user

# Configure Logging
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create User
@router.post("/organization/{org_id}/department/{dept_id}/user", status_code=status.HTTP_201_CREATED)
def create_user_endpoint(org_id: str, dept_id: str, name: str, email: str, role: str, profile_picture_url=None):
    try:
        user_id = str(uuid.uuid4())
        create_user(org_id, dept_id, user_id, name, email, role)
        return {
            "user_id": user_id,
            "name": name,
            "email": email,
            "role": role,
            "org_id": org_id,
            "dept_id": dept_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create user due to Internal Server Error.")

# Get User
@router.get("/organization/{org_id}/department/{dept_id}/user/{user_id}", status_code=status.HTTP_200_OK)
def get_user_endpoint(org_id: str, dept_id: str, user_id: str):
    user = get_user(org_id, dept_id, user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found in department {dept_id}.")