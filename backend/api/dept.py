# Importing Dependencies
import uuid
import logging
from fastapi import APIRouter, HTTPException, status

from db.department import create_department, get_department

# Configure Logging
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create Department
@router.post("/organization/{org_id}/department", status_code=status.HTTP_201_CREATED)
def create_department_endpoint(org_id: str, name: str):
    try:
        dept_id = str(uuid.uuid4())
        create_department(org_id, dept_id, name)
        return {
            "dept_id": dept_id,
            "name": name,
            "org_id": org_id
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to create department due to Internal Server Error. {e}")

# Get Department
@router.get("/organization/{org_id}/department/{dept_id}", status_code=status.HTTP_200_OK)
def get_department_endpoint(org_id: str, dept_id: str):
    department = get_department(org_id, dept_id)
    if department:
        return department
    else:
        raise HTTPException(status_code=404, detail=f"Department {dept_id} not found in organization {org_id}.")