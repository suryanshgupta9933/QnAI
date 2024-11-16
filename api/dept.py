# Importing Dependencies
import uuid
import logging
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status

from db.department import create_department, get_department

# Configure Logging
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create Department Model
class CreateDepartment(BaseModel):
    org_id: str
    name: str
    description: str = None

# Create Department
@router.post("/department/create", status_code=status.HTTP_201_CREATED)
def create_department_endpoint(dept: CreateDepartment):
    """
    Create a department in an organization.
    """
    try:
        dept_id = str(uuid.uuid4())
        create_department(dept.org_id, dept_id, dept.name, dept.description)
        return {
            "org_id": dept.org_id,
            "dept_id": dept_id,
            "name": dept.name,
            "description": dept.description
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to create department due to Internal Server Error.")

# Get Department
@router.get("/department", status_code=status.HTTP_200_OK)
def get_department_endpoint(org_id: str, dept_id: str):
    """
    Get a department in an organization.
    """
    try:
        dept = get_department(org_id, dept_id)
        if dept:
            return dept
        else:
            raise HTTPException(status_code=404, detail=f"Department {dept_id} not found.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Failed to get department due to Internal Server Error.")