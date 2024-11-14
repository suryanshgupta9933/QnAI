# Importing Dependencies
import uuid
import logging
from fastapi import APIRouter, HTTPException, status, Query, Path

from db.department import create_department, get_department

# Configure Logging
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create Department
@router.post("/department/create", status_code=status.HTTP_201_CREATED)
def create_department_endpoint(org_id: str = Path(..., description="The unique identifier for the organization"), 
                               name: str = Query(..., description="The name of the department to be created")):
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
        raise HTTPException(status_code=500, detail="Failed to create department due to Internal Server Error.")

# Get Department
@router.get("/department", status_code=status.HTTP_200_OK)
def get_department_endpoint(org_id: str, dept_id: str):
    try:
        department = get_department(org_id, dept_id)
        if department:
            return department
        else:
            raise HTTPException(status_code=404, detail=f"Department {dept_id} not found.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Failed to get department due to Internal Server Error.")