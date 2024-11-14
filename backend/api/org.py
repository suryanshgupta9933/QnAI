# Importing Dependencies
import uuid
import logging
from fastapi import APIRouter, HTTPException, status

from db.organization import create_org, get_org

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create API Router
router = APIRouter()

# Create Organization
@router.post("/organization", status_code=status.HTTP_201_CREATED)
def create_organization(name: str, description: str):
    """
    Create an organization.
    """
    try:
        org_id = str(uuid.uuid4())
        create_org(org_id, name, description)
        return {
            "org_id": org_id,
            "name": name,
            "description": description
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create organization due to Internal Server Error.")

# Get Organization
@router.get("/organization/{org_id}", status_code=status.HTTP_200_OK)
def get_organization(org_id: str):
    """
    Get an organization.
    """
    org = get_org(org_id)
    if org:
        return org
    else:
        raise HTTPException(status_code=404, detail=f"Organization {org_id} not found.")