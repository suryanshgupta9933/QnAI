# Importing Dependencies
import uuid
import logging
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status

from db.organization import create_organization, get_organization

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create Organization Model
class CreateOrganization(BaseModel):
    name: str
    description: str

# Get Organization Model
class GetOrganization(BaseModel):
    org_id: str

# Create Organization
@router.post("/organization/create", status_code=status.HTTP_201_CREATED)
def create_organization_endpoint(org: CreateOrganization):
    """
    Create an organization.
    """
    try:
        org_id = str(uuid.uuid4())
        create_organization(org_id, org.name, org.description)
        return {
            "org_id": org_id,
            "name": org.name,
            "description": org.description
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Failed to create organization due to Internal Server Error.")

# Get Organization
@router.get("/organization", status_code=status.HTTP_200_OK)
def get_organization_endpoint(org: GetOrganization):
    """
    Get an organization.
    """
    try:
        org = get_organization(org.org_id)
        if org:
            return org
        else:
            raise HTTPException(status_code=404, detail=f"Organization {org_id} not found.")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Failed to get organization due to Internal Server Error.")